#!/usr/bin/env python3
"""Promote verified L135-L139 knowledge notes into curriculum notes."""
from __future__ import annotations
import argparse, re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = "Material/DE/Curriculum/Phase_04-sql-and-database-internals/Module_10-storage-engine-and-database-operations"
PACK = "Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01"

@dataclass(frozen=True)
class Lesson:
    number: int; directory: str; title: str; source: str

LESSONS = (
    Lesson(135, "Lesson_135-lsm-trees-memtable-sstable-and-compaction", "LSM trees - memtable, SSTable and compaction", "23-lsm-trees-memtable-sstable-and-compaction.md"),
    Lesson(136, "Lesson_136-amplification-read-write-and-space", "Amplification - read, write and space", "24-read-write-and-space-amplification.md"),
    Lesson(137, "Lesson_137-the-write-ahead-log-and-group-commit", "The write-ahead log and group commit", "25-write-ahead-log-and-group-commit.md"),
    Lesson(138, "Lesson_138-crash-recovery-redo-undo-and-checkpoints", "Crash recovery - redo, undo and checkpoints", "26-crash-recovery-redo-undo-and-checkpoints.md"),
    Lesson(139, "Lesson_139-acid-and-the-transaction-state-machine", "ACID and the transaction state machine", "27-acid-and-transaction-state-machine.md"),
)

def field(text, name):
    m = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", text)
    if not m: raise ValueError(f"Thiếu {name}")
    return m.group(1).strip()

def section(text, heading):
    m = re.search(rf"(?ms)^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", text)
    if not m: raise ValueError(f"Thiếu section {heading}")
    return m.group(1).strip()

def strip_source(text):
    if text.startswith("---\n"): text = text[text.find("\n---\n", 4) + 5:]
    return re.sub(r"^# .+\n+", "", text.strip(), count=1)

def folder(x): return ROOT / BASE / x.directory

def contract(x):
    note = (folder(x) / "note.md").read_text(encoding="utf-8")
    after = (folder(x) / "after-note.md").read_text(encoding="utf-8")
    if "**Outcome.**" in note:
        return tuple(field(note, k) for k in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    return (field(section(note,"Mục tiêu bài học"),"Năng lực cần chứng minh"), field(section(after,"Tiêu chí hoàn thành"),"Cách đánh giá"), field(section(after,"Thực hành"),"Nhiệm vụ"), field(section(after,"Bài làm sau buổi học"),"Lỗi cần chủ động loại trừ"), field(section(after,"Bài làm sau buổi học"),"Nhiệm vụ"), field(section(note,"Mục tiêu bài học"),"Điều kiện hoàn thành"))

def build(x):
    outcome, assessment, lab, pitfalls, homework, done = contract(x)
    source = ROOT / PACK / x.source
    header = f"# Phase 4: SQL and Database Internals\n# Module 10: Storage Engine and Database Operations\n# Lesson {x.number}: {x.title}"
    questions = {
        135:["Memtable cần WAL vì sao?","Flush phải giữ read-view invariants nào?","Tombstone được drop khi nào?","Compaction debt biểu hiện qua metrics nào?"],
        136:["Ba amplification ratio có numerator/denominator gì?","Vì sao cần drain maintenance debt?","Durability parity khóa những gì?","Negative lookup đo read amplification ra sao?"],
        137:["Hai write-ahead rules là gì?","Group commit đổi throughput/latency ra sao?","Async commit khác fsync off thế nào?","ACK ledger dùng để kiểm điều gì?"],
        138:["PostgreSQL khác ARIES undo ở đâu?","Checkpoint là point hay interval?","Crash trong commit tạo ambiguity nào?","Đo recovery trade-off cần counters gì?"],
        139:["Bốn chữ ACID chia trách nhiệm ra sao?","Partially committed khác committed thế nào?","Client timeout chứng minh được gì?","State machine cần những transitions nào?"]
    }[x.number]
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{strip_source(source.read_text(encoding='utf-8'))}\n"
    safety = "Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy."
    after = f"{header}\n\n## Thực hành\n\n**Nhiệm vụ.** {lab}\n\n{safety}\n\n## Kiểm tra cuối bài\n\n" + "\n".join(f"{i}. {q}" for i,q in enumerate(questions,1)) + f"\n\n## Tiêu chí hoàn thành\n\n**Cách đánh giá.** {assessment}\n\n**Điều kiện đạt.** {done}\n\n## Bài làm sau buổi học\n\n**Nhiệm vụ.** {homework}\n\n**Lỗi cần chủ động loại trừ.** {pitfalls}\n\n## Reference\n\n- Knowledge note: `{source.relative_to(ROOT)}`\n- Nội dung học thuật: `note.md` cùng thư mục.\n"
    return note, after

def main():
    p=argparse.ArgumentParser(); p.add_argument("--check",action="store_true"); args=p.parse_args(); stale=[]
    for x in LESSONS:
        for path,content in zip((folder(x)/"note.md",folder(x)/"after-note.md"),build(x)):
            if args.check:
                if path.read_text(encoding="utf-8") != content: stale.append(str(path.relative_to(ROOT)))
            else: path.write_text(content,encoding="utf-8")
    if stale: print("STALE\n"+"\n".join(stale)); return 1
    print(f"checked={len(LESSONS)*2} stale=0" if args.check else f"written={len(LESSONS)*2}"); return 0

if __name__ == "__main__": raise SystemExit(main())
