#!/usr/bin/env python3
"""Render the single Mermaid block in every roadmap to an Artifact SVG."""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MATERIAL = ROOT / "Material"
OUTPUT = ROOT / "Artifact" / "Rabbit-Data" / "Roadmaps"
MMDC = ROOT / "node_modules" / ".bin" / "mmdc"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output_path(source: Path) -> Path:
    relative = source.relative_to(MATERIAL)
    parts = list(relative.parts)
    code = parts[0]
    scope = parts[2:-1]
    if not scope:
        return OUTPUT / code / "programme.svg"
    if len(scope) == 1:
        return OUTPUT / code / scope[0] / "phase.svg"
    return OUTPUT / code / scope[0] / scope[1] / "module.svg"


def extract_mermaid(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    blocks = re.findall(r"```mermaid\n(.*?)\n```", text, re.DOTALL)
    if len(blocks) != 1:
        raise ValueError(f"{source}: cần đúng một khối Mermaid, hiện có {len(blocks)}")
    return blocks[0].strip() + "\n"


def title(source: Path) -> str:
    first_line = source.read_text(encoding="utf-8").splitlines()[0]
    return first_line.removeprefix("# ").strip()


def build_gallery(items: list[dict[str, str]]) -> str:
    cards = []
    for item in items:
        svg = (ROOT / item["image"]).relative_to(OUTPUT.parent).as_posix()
        cards.append(
            "\n".join(
                [
                    f'<article class="diagram" data-programme="{item["programme"]}">',
                    f'  <header><span>{item["programme"]}</span><h2>{html.escape(item["title"])}</h2></header>',
                    f'  <a href="{svg}" target="_blank" rel="noopener" aria-label="Mở sơ đồ {html.escape(item["title"])} ở kích thước đầy đủ">',
                    f'    <img src="{svg}" alt="Sơ đồ {html.escape(item["title"])}" loading="lazy">',
                    "  </a>",
                    f'  <p><code>{html.escape(item["source"])}</code></p>',
                    "</article>",
                ]
            )
        )
    return f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sơ đồ roadmap · Rabbit Data</title>
  <style>
    :root{{--ink:#2b1b12;--paper:#fffdf8;--wash:#fff4e8;--line:#d9c8b8;--accent:#c85e16}}
    *{{box-sizing:border-box}}
    body{{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,ui-sans-serif,system-ui,sans-serif}}
    main{{width:min(1500px,calc(100% - 32px));margin:0 auto;padding:48px 0 80px}}
    nav{{margin-bottom:40px}} a{{color:var(--accent);text-underline-offset:4px}}
    h1{{max-width:900px;margin:0;font-family:Georgia,serif;font-size:clamp(2.4rem,6vw,5.8rem);line-height:.94;letter-spacing:-.04em}}
    .intro{{max-width:760px;margin:24px 0 48px;font-size:1.05rem;line-height:1.7}}
    .grid{{display:grid;gap:28px}}
    .diagram{{overflow:hidden;border:1px solid var(--line);border-radius:20px;background:#fff;box-shadow:0 12px 36px rgba(43,27,18,.07)}}
    .diagram header{{display:flex;gap:18px;align-items:baseline;padding:22px 24px;border-bottom:1px solid var(--line);background:var(--wash)}}
    .diagram header span{{font:700 .75rem/1 ui-monospace,monospace;letter-spacing:.12em;color:var(--accent)}}
    .diagram h2{{margin:0;font:600 1.15rem/1.3 Georgia,serif}}
    .diagram a{{display:block;overflow:auto;padding:24px;background:#fff}}
    .diagram img{{display:block;max-width:none;min-width:100%;height:auto;margin:auto}}
    .diagram p{{margin:0;padding:14px 24px;border-top:1px solid var(--line);color:#6e5c4e;font-size:.78rem;overflow-wrap:anywhere}}
    @media(max-width:640px){{main{{width:min(100% - 20px,1500px);padding-top:28px}}.diagram a{{padding:12px}}.diagram header{{display:block}}}}
  </style>
</head>
<body>
<main>
  <nav><a href="index.html">← Quay lại Artifact</a></nav>
  <h1>Bản đồ chương trình, giai đoạn và mô-đun</h1>
  <p class="intro">Toàn bộ sơ đồ dưới đây được render thành SVG từ đúng một khối Mermaid trong mỗi roadmap nguồn. Chọn một sơ đồ để mở ảnh ở kích thước đầy đủ.</p>
  <section class="grid" aria-label="Sơ đồ roadmap">
{chr(10).join(cards)}
  </section>
</main>
</body>
</html>
"""


def main() -> int:
    if not MMDC.is_file():
        raise SystemExit("Thiếu Mermaid CLI. Chạy npm install trước khi render.")
    chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if not chrome:
        raise SystemExit("Không tìm thấy Chrome/Chromium để render Mermaid.")

    def source_order(source: Path) -> tuple[str, int, int, int]:
        relative = source.relative_to(MATERIAL)
        code = relative.parts[0]
        scope = relative.parts[2:-1]
        if not scope:
            return code, 0, 0, 0
        phase_number = int(scope[0].split("_", 1)[1].split("-", 1)[0])
        if len(scope) == 1:
            return code, phase_number, 0, 0
        module_number = int(scope[1].split("_", 1)[1].split("-", 1)[0])
        return code, phase_number, 1, module_number

    sources = sorted(MATERIAL.glob("*/Roadmap/**/roadmap.md"), key=source_order)
    if len(sources) != 56:
        raise SystemExit(f"Cần 56 roadmap, tìm thấy {len(sources)}")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    manifest_path = OUTPUT / "manifest.json"
    previous_items: dict[str, dict[str, str]] = {}
    if manifest_path.is_file():
        previous_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        previous_items = {item["source"]: item for item in previous_manifest.get("items", [])}
    items: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="rabbit-roadmap-") as temporary:
        temp = Path(temporary)
        puppeteer_config = temp / "puppeteer.json"
        puppeteer_config.write_text(
            json.dumps({"executablePath": chrome, "args": ["--no-sandbox"]}),
            encoding="utf-8",
        )
        for index, source in enumerate(sources, start=1):
            image = output_path(source)
            source_relative = source.relative_to(ROOT).as_posix()
            source_digest = sha256(source)
            previous = previous_items.get(source_relative)
            reusable = (
                previous is not None
                and previous.get("source_sha256") == source_digest
                and image.is_file()
                and previous.get("image_sha256") == sha256(image)
            )
            if not reusable:
                diagram_source = temp / f"roadmap-{index:02d}.mmd"
                diagram_source.write_text(extract_mermaid(source), encoding="utf-8")
                image.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(
                    [
                        str(MMDC),
                        "--input",
                        str(diagram_source),
                        "--output",
                        str(image),
                        "--backgroundColor",
                        "transparent",
                        "--puppeteerConfigFile",
                        str(puppeteer_config),
                    ],
                    cwd=ROOT,
                    check=True,
                )
            items.append(
                {
                    "programme": source.relative_to(MATERIAL).parts[0],
                    "title": title(source),
                    "source": source_relative,
                    "source_sha256": source_digest,
                    "image": image.relative_to(ROOT).as_posix(),
                    "image_sha256": sha256(image),
                }
            )

    manifest = {
        "schema_version": 1,
        "renderer": "@mermaid-js/mermaid-cli",
        "diagram_count": len(items),
        "items": items,
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUTPUT.parent / "roadmaps.html").write_text(build_gallery(items), encoding="utf-8")
    print(f"Rendered {len(items)} Mermaid diagrams to {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
