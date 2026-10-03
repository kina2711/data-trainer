# RÀ SOÁT PHẢN BIỆN ROADMAP DATA ENGINEER

Ngày rà soát: 2026-09-24  
Phạm vi: `material/data-engineer/roadmap/roadmap.md`, 29 roadmap module và 440 cây bài trong `material/data-engineer/curriculum/`.  
Nguồn chuẩn nội dung: 29 hợp đồng tại `/home/kina2711/PROJECT/roadmap-de/about me/06_LO_TRINH_CHI_TIET_THEO_MODULE/`, coverage audit và các artefact build được nêu trong yêu cầu.  
Phương pháp: đọc-only; không chạy `make scaffold`, `make diagrams` hay `assemble_ade.py`; chỉ tạo báo cáo này.

Baseline `make test`: **PASS toàn bộ**. Kết luận này không được dùng thay cho các kiểm tra độc lập bên dưới.

Script audit độc lập đã chạy tại `/tmp/audit_de_review.py` (`sha256 fc118daa94feade7d2ca4840e6f6a3d6c8b154c65f90e776caa8aeb4d96cdc52`); kết quả máy đọc được tại `/tmp/audit_de_review.json` (`sha256 d9702d716830b25c60b6d165a0beffb4c996f92d338a74469bbfd3082cf1d09f`).

---

# Phần 1 — Lỗi phải sửa

## 1. Tham chiếu isolation bị đánh số sai: `lesson 140 tới 132`

**Mức nghiêm trọng: NẶNG — tham chiếu sai nội dung.**

**Mô tả.** Đoạn giải thích ACID nói các mức cô lập nằm ở “lesson 140 tới 132”. Lesson 132 là `SQL tuning project - five slow queries`, không phải bài về isolation. Dải đúng theo chính mục lục hiện tại phải kết thúc ở lesson 142.

**File và dòng.**

- `material/data-engineer/roadmap/roadmap.md:2946`
- `material/data-engineer/curriculum/module_10-Storage Engine and Database Operations/roadmap/roadmap.md:161`
- `material/data-engineer/curriculum/module_10-Storage Engine and Database Operations/curriculum/lesson_139_ACID and the transaction state machine/note.md:26`

**Trích dẫn.**

> Cô lập: giao dịch chạy song song cho kết quả như thể chạy lần lượt, và đây là chữ có nhiều mức nhất, nội dung của lesson 140 tới 132.

**Bằng chứng tái hiện.**

```bash
rg -n "lesson 140 tới 132|^### Lesson (132|140|141|142) " \
  material/data-engineer/roadmap/roadmap.md \
  material/data-engineer/curriculum/module_10-*/roadmap/roadmap.md \
  material/data-engineer/curriculum/module_10-*/curriculum/lesson_139_*/note.md
```

Đây là một trong 60 ngữ cảnh tham chiếu được đọc nghĩa thủ công. 59 ngữ cảnh còn lại trong mẫu trỏ đúng chủ đề đích.

## 2. Mười tám module sau M11 vẫn tự gọi mình bằng mã hợp đồng cũ

**Mức nghiêm trọng: NẶNG — renumber lần 2 chưa hoàn tất trong văn xuôi.**

**Mô tả.** Dòng prerequisite của bài đầu mỗi module giữ mã module nguồn ở vế `Module X`, trong khi vế sau dấu hai chấm đã dùng mã hiện tại. Ví dụ lesson 345 thuộc M23 nhưng ghi `Module 18: M21`. Lỗi có ở toàn bộ M12–M29: `11B, 11C, 12, 13, 14B, 14, 14C, 14D, 15…24` thay vì `12…29`.

**File và dòng đại diện.**

- `material/data-engineer/roadmap/roadmap.md:3472,3870,4230,4514,4798,5120,5670,6030,6352,6596,6878,7086,7408,7654,7976,8298,8620,8828`
- `material/data-engineer/curriculum/module_23-Spark, Flink and Distributed Compute Engines/roadmap/roadmap.md:43`
- `material/data-engineer/curriculum/module_23-Spark, Flink and Distributed Compute Engines/curriculum/lesson_345_Cluster roles and the execution hierarchy/note.md:22`

**Trích dẫn.**

> **Prerequisites.** Module 18: M21

Trong ngữ cảnh hiện tại phải nhận diện đây là module 23; `M21` ở vế prerequisite là hợp lệ.

**Bằng chứng tái hiện.**

```bash
rg -n '^\*\*Prerequisites\.\*\* Module ' material/data-engineer/roadmap/roadmap.md

rg -n '^\*\*Prerequisites\.\*\* Module (11B|11C|12|13|14B|14|14C|14D|15|16|17|18|19|20|21|22|23|24):' \
  material/data-engineer/roadmap/roadmap.md \
  material/data-engineer/curriculum/module_*/roadmap/roadmap.md \
  material/data-engineer/curriculum/module_*/curriculum/lesson_*/note.md | wc -l
```

Kết quả: **54 bản sao** = 18 ở roadmap tổng + 18 ở roadmap module + 18 trong note bài đầu module.

## 3. Bảy bài cổng vừa là bài 120 phút, vừa là bài 150/180 phút

**Mức nghiêm trọng: NẶNG — không thể lập lịch và tính tổng giờ nhất quán.**

**Mô tả.** Bảng “Mười cổng kiểm tra” ghi lessons 44, 112, 308, 360, 404, 440 là 180 phút và lesson 230 là 150 phút. Đặc tả chính các bài này vẫn ghi `In-class (120 phút)`; frontmatter note cũng là 120 phút. Một số `Lab` ngay trong cùng bài lại mở bằng “Buổi 180 phút”.

**File và dòng.**

- Bảng gate: `material/data-engineer/roadmap/roadmap.md:101-110`
- Ví dụ gate 8: `material/data-engineer/roadmap/roadmap.md:7373` ghi 120 phút, `:7381` ghi 180 phút.
- Ví dụ tốt nghiệp: `:9001` ghi 120 phút, `:9009` ghi 180 phút.

**Bằng chứng tái hiện.**

```bash
rg -n '^\| (1|3|6|7|8|9|Tốt nghiệp) \|' material/data-engineer/roadmap/roadmap.md
rg -n -A10 '^### Lesson (44|112|230|308|360|404|440) ' material/data-engineer/roadmap/roadmap.md
```

Nếu bảng gate là chuẩn, tổng giờ lớp là **886,5 giờ**, không phải 880. Nếu công thức 440 × 2 giờ là chuẩn, bảng gate sai.

## 4. Tổng tự học 1.056 giờ tính cả 10 bài được ghi rõ là không có tự học

**Mức nghiêm trọng: NẶNG — sai tải lượng chương trình.**

**Mô tả.** Đầu roadmap công bố 440 × 2,4 = 1.056 giờ tự học, nhưng cả 10 bài KT đều ghi “Không có bài tự học”. Tổng theo đặc tả bài là 430 × 2,4 = **1.032 giờ**, lệch 24 giờ.

**File và dòng.**

- Tổng công bố: `material/data-engineer/roadmap/roadmap.md:21`
- Mười dòng không tự học: `:1035,1919,2409,3127,4207,4775,6329,7385,8275,9013`.

**Bằng chứng tái hiện.**

```bash
rg -n '^\*\*Self-study \(2,4 giờ\)\.\*\* Không có bài tự học' \
  material/data-engineer/roadmap/roadmap.md
```

Kết quả: 10 dòng. Công thức tái hiện: `(440 - 10) * 2.4 = 1032`.

## 5. `ade-module-map.md` vẫn mang tổng giờ của bản 428 bài

**Mức nghiêm trọng: NẶNG — artefact điều khiển build tự mâu thuẫn sau lần chèn 12 bài.**

**Mô tả.** Bảng module trong map cộng đúng 440 bài, nhưng dòng tổng giờ vẫn là 856 giờ lớp và 1.027 giờ tự học. Đây chính là 428 × 2 và xấp xỉ 428 × 2,4, tức số cũ trước khi chèn 12 bài.

**File và dòng.**

- `.data-2026/build/ade-module-map.md:64-66`
- Đối chiếu roadmap hiện tại: `material/data-engineer/roadmap/roadmap.md:14,21`.

**Trích dẫn.**

> **440 bài · 29 module · 856 giờ trên lớp + 1.027 giờ tự học = ~1.883 giờ.**

**Bằng chứng tái hiện.**

```bash
python3 - <<'PY'
print(440 * 2, 440 * 2.4, 440 * 4.4)
print(428 * 2, 428 * 2.4, 428 * 4.4)
PY
```

Kết quả: `880 1056 1936` và `856 1027.2 1883.2`.

## 6. Một `note.md` không còn khớp từng chữ với roadmap vì dấu phân cách dính vào `Done when`

**Mức nghiêm trọng: NẶNG — lỗi generator/serialization, dù nội dung ngữ nghĩa chưa đổi.**

**Mô tả.** So sánh chính xác toàn bộ khối từ `Prerequisites` tới `Done when` cho cả 440 bài cho kết quả 439 khớp và 1 lệch. Note lesson 440 dính `---` vào cuối dòng Done when, trong khi roadmap không có.

**File và dòng.**

- Roadmap: `material/data-engineer/roadmap/roadmap.md:9015`
- Note: `material/data-engineer/curriculum/module_29-Staff and Principal Trajectory/curriculum/lesson_440_Graduation defence - one design, three audiences/note.md:38-40`

**Bằng chứng tái hiện.**

```bash
nl -ba 'material/data-engineer/curriculum/module_29-Staff and Principal Trajectory/curriculum/lesson_440_Graduation defence - one design, three audiences/note.md' | sed -n '36,41p'
python3 /tmp/audit_de_review.py
```

Kết quả script: `note_spec_mismatches = 1`, lesson 440.

## 7. Frontmatter `module` lệch đúng-chữ ở 70 note

**Mức nghiêm trọng: NHẸ — khác casing, nhưng không đạt yêu cầu khớp chính xác.**

**Mô tả.** Năm module có cách viết khác bảng module của roadmap tổng:

| Module | Số note | Trong note | Trong roadmap tổng |
|---|---:|---|---|
| M13 | 18 | `Self-service` | `Self-Service` |
| M14 | 14 | `Olap` | `OLAP` |
| M24 | 12 | `Before` | `before` |
| M25 | 16 | `as Code` | `As Code` |
| M28 | 10 | `Ai` | `AI` |

Tổng: **70**.

**File và dòng đại diện.** Mỗi note có lỗi tại frontmatter dòng 3, ví dụ:

- `material/data-engineer/curriculum/module_14-Olap Internals and Analytical Engines/curriculum/lesson_203_OLTP against OLAP - the workload is the difference/note.md:3`
- Bảng chuẩn: `material/data-engineer/roadmap/roadmap.md:134-150`.

**Bằng chứng tái hiện.**

```bash
python3 - <<'PY'
import re, collections
from pathlib import Path
r=Path('material/data-engineer/roadmap/roadmap.md').read_text()
names={int(m.group(1)):m.group(2).strip() for m in re.finditer(
 r'^\| \*\*M(\d+)\*\* \| (.*?) \| \d+–\d+ \|',r,re.M)}
bad=[]
for p in Path('material/data-engineer/curriculum').glob('module_*/curriculum/lesson_*/note.md'):
 s=p.read_text(); fm=s.split('\n---\n',1)[0]
 got=re.search(r'^module:\s*(.+)$',fm,re.M).group(1)
 mn=int(re.search(r'module_(\d+)-',str(p)).group(1))
 if got != f'{mn} — {names[mn]}': bad.append((p,got,names[mn]))
print(len(bad))
PY
```

Kết quả: `70`.

## 8. Mười một `Done when` dùng ngưỡng không được định nghĩa

**Mức nghiêm trọng: NẶNG — không thể tái lập quyết định đạt/không đạt từ roadmap.**

**Mô tả.** Các lessons 10, 31, 72, 125, 179, 238, 283, 292, 368, 429, 436 dùng `dưới ngưỡng`, `ngưỡng thoả thuận` hoặc `trong giới hạn thời gian` nhưng không ghi giá trị, nơi lưu baseline, hoặc ai duyệt ngưỡng. Một assessor khác không thể chấm lại cùng kết quả chỉ từ hợp đồng này.

**File và dòng.** `material/data-engineer/roadmap/roadmap.md:359,774,1601,2676,3754,4947,5838,6009,7557,8788,8939`.

**Trích dẫn đại diện.**

> Thời gian phân vị 95 dưới ngưỡng, độ tươi trong cam kết...

> Người chưa quen đưa được thay đổi đầu tiên lên sản xuất trong giới hạn thời gian...

**Bằng chứng tái hiện.**

```bash
rg -n '^\*\*Done when\.\*\*.*(dưới ngưỡng|ngưỡng thoả thuận|trong giới hạn thời gian)' \
  material/data-engineer/roadmap/roadmap.md
```

## 9. Năm nhóm khẳng định định lượng được trình bày như sự thật nhưng không có nguồn hoặc điều kiện áp dụng

**Mức nghiêm trọng: VỪA — phát biểu khoa học không truy vết được.**

**File và dòng.** `material/data-engineer/roadmap/roadmap.md`:

- `:1060`: truy cập dữ liệu “một nhịp” đến “hàng triệu nhịp”, mỗi bậc chậm hơn 1–3 bậc độ lớn.
- `:1079`: cache line “thường 64 byte” và duyệt tuần tự nhanh hơn ngẫu nhiên “hàng chục lần”.
- `:1231`: một triệu lần đọc từng byte chậm hơn đọc khối 64 KB “hàng trăm lần”.
- `:4253`: đọc 3 cột trong bảng 100 cột “chỉ tốn ba phần trăm lượng byte”; chỉ đúng dưới các giả định về kích thước cột, encoding, metadata và compression không được nêu.
- `:5561`: một ngày có 23/25 giờ “hai lần mỗi năm”; chỉ áp dụng cho một số múi giờ có DST và quy tắc cụ thể.

**Bằng chứng tái hiện.**

```bash
rg -n 'hàng (chục|trăm|triệu)|ba phần trăm|23 hoặc 25 giờ|64 byte|một tới ba bậc' \
  material/data-engineer/roadmap/roadmap.md
```

Roadmap hiện không có URL/citation nào để truy ngược các con số này. Các con số tạo cho lab và ngưỡng chấm do chương trình tự định nghĩa không bị tính là claim bên ngoài.

---

# Phần 2 — Nội dung bị mất so với hợp đồng gốc

Đã đối chiếu sáu module: M1, M12, M16, M18, M23, M29. Bốn module bắt buộc được giữ nguyên: M12, M16, M18, M23. Hai module tự chọn: M1 và M29.

| Hợp đồng gốc | Mục bị mất hoặc bị hạ chuẩn | Module hiện tại | Bằng chứng |
|---|---|---|---|
| `01_ENGINEERING_THINKING_GIT_DEBUGGING.md:105-113` | Failure matrix yêu cầu ca “rollback không chạy do schema change → compatibility plan”. M1 hiện có rollback note nhưng không có bài/pitfall/lab kiểm rollback qua schema migration. | M1 | `rg -n 'schema change|compatibility plan|di trú lược đồ'` trong block M1 cho 0 kết quả liên quan đến rollback |
| `11B_SEMANTIC_AND_METRICS_LAYER.md:323` | Exit yêu cầu **15+ governed metrics thuộc ít nhất 5 loại**. Capstone hiện chỉ yêu cầu **ít nhất 8 chỉ số, đủ 4 loại**. | M12 | Roadmap `:3837`; source `:323` |
| `11B_...md:325` | Bộ fixture bắt buộc phải phủ NULL, duplicate, refund, late data, SCD và fiscal boundary. Roadmap chỉ nói chung “ba ca biên”; không nêu và không cưỡng chế sáu ca này. | M12 | Source `:325`; roadmap `:3723-3735,3843` |
| `11B_...md:327` và `:285-289` | Two-consumer serving cùng cache isolation bị hạ thành ba “đường phục vụ” không có phép thử cache theo consumer/security context. | M12 | Source `:287-289,327`; roadmap `:3737-3773` |
| `11B_...md:328` và `:308` | Breaking migration phải có dual-run, reconciliation và deprecation record. Lesson 182 chỉ yêu cầu thông báo, regression test và cửa sổ khai tử; không yêu cầu dual-run/reconciliation. | M12 | Source `:308,328`; roadmap `:3794-3811` |
| `11B_...md:336-338` | Critical failure “formula breaking change overwrite in place không migration” và “cache bỏ security context hoặc semantic version” không xuất hiện đầy đủ dưới dạng Pitfall/điểm không. | M12 | Source `:336-338`; Pitfalls roadmap `:3750,3769,3807,3826,3845` |
| `18_SPARK_FLINK_COMPUTE.md:53` | Exit yêu cầu chọn giữa **Spark/Flink/Polars/DuckDB** theo workload/scale/latency/state/ops. Roadmap chỉ dạy so hai engine Spark/Flink; `Polars` và `DuckDB` không xuất hiện trong M23. | M23 | Source `:53`; roadmap `:7337-7349`; `rg -n 'Polars|DuckDB'` trong block M23 trả 0 |
| `24_STAFF_PRINCIPAL_ARCHITECT.md:67` | Exit yêu cầu **ba RFC được review, một RFC triển khai và đo sau adoption**. Lesson 433 chỉ yêu cầu một RFC và một vòng review. | M29 | Source `:67`; roadmap `:8865-8882` |
| `24_...md:69` | Exit yêu cầu ít nhất hai kỹ sư/đội có thể tự làm nhờ interface/docs/guardrails. Roadmap chỉ đo một người chưa quen; câu “hai đội” chỉ xuất hiện trong phần giải thích, không nằm trong Outcome/Done when. | M29 | Source `:69`; roadmap `:8927-8939,8965-8977` |
| `24_...md:54` | Practicum bắt buộc “cut 30% cost hoặc improve SLO có measurement” bị mất. | M29 | `rg -n '30%|improve SLO'` trong M29 trả 0 |
| `24_...md:55` | Practicum bắt buộc game day/postmortem xuyên hai component bị mất. | M29 | `rg -n 'game day|postmortem|phân tích sau sự cố|diễn tập'` trong M29 trả 0 |

## Kết quả theo từng module được chọn

| Module | Exit Criteria | Critical failures/failure matrix | Lab bắt buộc | Nội dung bịa thêm không có biện minh |
|---|---|---|---|---|
| M1 | Phần lớn giữ; thiếu failure case rollback/schema compatibility | Thiếu 1 hàng failure matrix | 5/5 lab chính có bài tương ứng | Không tìm thấy |
| M12 | Bị hạ chuẩn ở số metric/type, fixture, serving và migration | Thiếu/giảm 2 critical controls về migration/cache key | Thiếu production migration/consumer-cache proof | Không tìm thấy |
| M16 | Đủ | 6/6 critical failures có Pitfall/bài kiểm | 5 lab + capstone/game day có bài tương ứng | Không tìm thấy |
| M18 | Đủ | 6/6 được đưa vào capstone như điều kiện tự động chưa đạt | 5 lab + capstone có bài tương ứng | Không tìm thấy |
| M23 | Thiếu exit lựa chọn 4 engine | Failure/performance matrix được phản ánh trong Pitfalls và gate | 6/6 lab chính có bài tương ứng | Không tìm thấy |
| M29 | Bị hạ từ 3 RFC xuống 1 và từ 2 đội xuống 1 người | Critical fail về nói quá bằng chứng được giữ | Thiếu cost/SLO practicum và cross-component game day | Không tìm thấy |

---

# Phần 3 — Không nhất quán nhưng chưa chắc sai

## 1. “Không yêu cầu đầu vào” so với yêu cầu biết terminal và sửa tệp

- `material/data-engineer/roadmap/roadmap.md:20`: “Không. Giả định chưa biết lập trình”.
- `material/data-engineer/roadmap/roadmap.md:162`: “Không. Dùng được terminal và sửa được tệp văn bản”.

**Cách hiểu 1:** terminal/text editing là kỹ năng đầu vào thật, nên tuyên bố “Không” sai.  
**Cách hiểu 2:** “không đầu vào” chỉ nói không cần kiến thức lập trình/data; kỹ năng máy tính cơ bản nằm ngoài phạm vi.  
Roadmap chưa định nghĩa ranh giới này nên không thể kết luận một phía.

## 2. Mười ba `Done when` dùng cụm “chọn đúng” nhưng không chỉ ra oracle/rubric

Các lessons 5, 29, 42, 63, 71, 98, 154, 181, 233, 298, 321, 358, 389 dùng “chọn đúng”.

**Cách hiểu 1:** tình huống có đáp án/rubric riêng trong quiz hoặc tài liệu giảng viên, nên tiêu chí có thể chấm được.  
**Cách hiểu 2:** không có một lựa chọn duy nhất; đúng phải được định nghĩa bằng ràng buộc và bằng chứng, nên từ “đúng” làm tiêu chí không tái lập được.  
Các `quiz.md` hiện là khung, nên trong phạm vi được đọc chưa có oracle để chọn cách hiểu 1.

**Bằng chứng.**

```bash
rg -n '^\*\*Done when\.\*\*.*chọn đúng' material/data-engineer/roadmap/roadmap.md
```

## 3. M29 là module trong chương trình nhưng điều kiện đạt phụ thuộc kinh nghiệm ngoài chương trình

- Roadmap đầu chương trình `:19` nói đầu ra “Junior vững tới Senior”.
- M29 `:8816,8821` yêu cầu ít nhất một hệ đã vận hành đủ lâu và nói phần lớn bằng chứng chỉ có khi đi làm.

**Cách hiểu 1:** M29 là trajectory/reference, không phải năng lực được chương trình cam kết tạo ra; cách viết trung thực.  
**Cách hiểu 2:** nếu M29 và graduation defence là điều kiện hoàn tất 440 bài, người chưa có môi trường sản xuất không thể hoàn thành theo đúng hợp đồng dù học đủ chương trình.

## 4. Link tài nguyên

Trong roadmap tổng và 29 roadmap module hiện có **0 URL HTTP/HTTPS**. Vì vậy không có link chết, link lậu hoặc link trả phí không ghi chú để kết luận. Hai cách hiểu:

- Đây là chủ ý: roadmap chỉ chứa đặc tả, tài nguyên nằm ở hợp đồng nguồn.
- Đây là mất traceability khi đưa hợp đồng sang `material/`.

Không đủ dữ kiện trong phạm vi hiện tại để chọn một phía.

---

# Phần 4 — Loại lỗi mà `make test` không phủ

## 1. Không kiểm nghĩa của tham chiếu chéo

`material/_shared/tools/check_curriculum.py` không tìm `lesson N` hay `M#` trong văn xuôi, không kiểm tồn tại/chiều prerequisite và không kiểm target có đúng chủ đề. Vì vậy nó bỏ sót lỗi `lesson 140 tới 132` và 18 mã module cũ.

**Test bổ sung:** parse toàn bộ lesson/module reference; kiểm range/order tự động; xuất context + target title/Learn cho semantic review bắt buộc theo mẫu phân tầng, lưu kết quả review theo commit hash.

## 2. Test “đủ đặc tả” thực tế chỉ yêu cầu hai trường

`check_curriculum.py:102-111` đếm các field nhưng chỉ báo thiếu khi `has < 2` và không có một nhãn thay thế. Nó không yêu cầu đủ chín trường như tên test in ra.

**Test bổ sung:** so tập field chính xác với chín khóa, đúng một lần mỗi khóa, đúng thứ tự; không chấp nhận nhãn thay thế cho bài thường.

## 3. Gate chỉ được đếm số dòng

`check_curriculum.py:89-92` chỉ so số bài KT với số hàng trong bảng gate. Nó không so lesson number với cuối phase, không so thời lượng, outcome, ngưỡng hay zero-score rule.

**Test bổ sung:** derive phase end từ map, so tập KT, so từng row gate với spec bài và frontmatter; fail nếu 120/150/180 mâu thuẫn.

## 4. Không kiểm công thức giờ và không đối chiếu map sau insertion

Test không cộng `Lessons a–b · N giờ`, không kiểm `N = số bài × 2`, không kiểm tổng tự học theo bài KT, và không đọc tổng ở `ade-module-map.md`.

**Test bổ sung:** tính lại class/self-study từ từng spec; so roadmap head, module headers, gate durations và build map.

## 5. Không kiểm frontmatter với roadmap tổng

Test chỉ kiểm thư mục/file tồn tại. Nó không so `module`, `lesson`, `tieu_de`, `dang_bai` với spec nguồn, nên bỏ sót 70 khác biệt casing.

**Test bổ sung:** parse frontmatter 440 note và so exact string/enum với roadmap canonical.

## 6. Không kiểm “Đặc tả từ roadmap” từng chữ

Không có diff roadmap tổng → roadmap module → note. Vì vậy dấu `---` dính vào Done when của lesson 440 vẫn PASS.

**Test bổ sung:** canonical extraction và byte-for-byte comparison cho chín trường trên cả ba tầng; in unified diff khi lệch.

## 7. Drawio chỉ cần “ít nhất một”, không phải đúng một

`check_curriculum.py:131-135` dùng glob và chỉ kiểm không rỗng. Một lesson có hai `.drawio` vẫn PASS. XML parse ở `:159-165` là tốt nhưng không kiểm cardinality theo lesson.

**Test bổ sung:** đúng một lesson drawio, đúng một module roadmap drawio; XML parse riêng theo scope.

## 8. Không kiểm hợp đồng gốc

Không có coverage matrix Outcomes/Labs/Exit Criteria/Critical failures → lessons/assessment. Do đó việc M12 giảm 15 metrics/5 types xuống 8/4 vẫn PASS.

**Test bổ sung:** manifest requirement ID cho từng bullet nguồn; mỗi ID phải ánh xạ ít nhất một lesson và một evidence/zero-score rule; kiểm orphan hai chiều.

## 9. Không kiểm chất lượng `Done when`, claim và văn phong

Test không phát hiện ngưỡng chưa định nghĩa, claim định lượng không nguồn, “chọn đúng” không rubric, link tài nguyên, hoặc dấu hiệu văn phong sáo rỗng.

**Test bổ sung:** lint các placeholder ngưỡng; bắt buộc `threshold_id` hoặc giá trị; inventory claims/URLs; style scan chỉ tạo review queue, không tự động kết luận.

---

# Phần 5 — Những gì đã kiểm và ĐẠT

## A. Toàn vẹn cấu trúc

| Kiểm tra | Kết quả |
|---|---|
| Lesson 1..440 liên tục, không trùng/thiếu | ĐẠT |
| Module 1..29 liên tục | ĐẠT |
| Khoảng bài module liền nhau, không chồng/hở | ĐẠT |
| Số bài từng module khớp cột `Bài` trong `ade-module-map.md` | ĐẠT |
| Phase từng module khớp phase map | ĐẠT |
| Tổng dòng module = 880 giờ | ĐẠT |
| Công thức 440 × 2 = 880 giờ | ĐẠT |
| Mỗi bài đủ 9 trường | ĐẠT, 440/440 |
| Mỗi bài đúng một nhãn LT/TH/DA/KT | ĐẠT; LT 83, TH 322, DA 25, KT 10 |
| 10 KT ở cuối Phase 1..10 | ĐẠT: 44, 88, 112, 148, 202, 230, 308, 360, 404, 440 |
| Nội dung/giờ của gate khớp hoàn toàn | **KHÔNG ĐẠT về giờ**, xem Phần 1 |

## B. Tham chiếu chéo

- Đếm được **447** occurrence `lesson N` trong văn xuôi sau khi loại heading, bảng và trường Prerequisites; 447/447 có N trong 1..440.
- Mọi `Lesson N` trong Prerequisites đều có `N < lesson hiện tại`; không có prerequisite đi ngược.
- Đếm được **208** occurrence `M#` trong văn xuôi; 208/208 nằm trong 1..29.
- Đã đọc nghĩa thủ công **60 ngữ cảnh** rải qua đủ 29 module: lấy một occurrence giữa mỗi module, sau đó lấy đều 31 occurrence còn lại. Một ngữ cảnh hỏng là dòng ACID ở Phần 1; 59 ngữ cảnh còn lại trỏ đúng nội dung đích.
- Cột `Hợp đồng nguồn` có đủ 29 mã và mọi file tương ứng tồn tại. Các remap không tầm thường đều đúng: M12→11B, M13→11C, M14→12, M15→13, M16→14B, M17→14, M18→14C, M19→14D, M20→15 … M29→24.

Lệnh tái hiện phần máy:

```bash
python3 /tmp/audit_de_review.py
python3 - <<'PY'
import json
x=json.load(open('/tmp/audit_de_review.json'))
print(x['B']['lesson_ref_count'], x['B']['lesson_ref_oob'])
print(x['B']['prereq_bad_order'])
print(x['B']['module_ref_count'], x['B']['module_ref_oob'])
PY
```

## C. Sáu hợp đồng nguồn

- M16: không tìm thấy Exit Criteria, Critical failure hoặc lab bắt buộc bị mất.
- M18: không tìm thấy Exit Criteria, Critical failure hoặc lab bắt buộc bị mất.
- M1, M12, M23, M29 có các mất mát đã liệt kê đầy đủ ở Phần 2.
- Trong sáu module, không tìm thấy nội dung mới nào không truy được về track, lab, assessment, coverage audit hoặc mục tiêu module nguồn.

## D. Bản cập nhật SIMD/MIMD/async

Release `curriculum-refresh-2026-09-24.1` được phủ đúng vị trí:

| Yêu cầu | Bài hiện tại | Module hiện tại | Kết quả |
|---|---|---|---|
| Flynn taxonomy | 48 | M4 | ĐẠT |
| SIMD lanes/mask/tail/gather | 49 | M4 | ĐẠT |
| Auto-vectorization | 50 | M4 | ĐẠT |
| Amdahl/Gustafson + efficiency | 55 | M4 | ĐẠT |
| MIMD shared/distributed memory + SPMD | 56 | M4 | ĐẠT |
| Structured concurrency/TaskGroup | 26 | M2 | ĐẠT |
| Deadline propagation + backpressure | 27 | M2 | ĐẠT |
| Async failure matrix | 28 | M2 | ĐẠT |
| Non-blocking FD/select/poll/epoll | 65 | M5 | ĐẠT |
| Readiness vs completion, partial I/O, cancellation, io_uring awareness | 66 | M5 | ĐẠT |
| Vectorized execution ≠ SIMD | 208 | M14 | ĐẠT |
| MPP dưới MIMD/SPMD + strong scaling | 211 | M14 | ĐẠT |
| Distributed MIMD/SPMD trong compute engine | 352 | M23 | ĐẠT |
| Nested parallelism/oversubscription | 353 | M23 | ĐẠT |
| Strong scaling efficiency | 354 | M23 | ĐẠT |

Hierarchy `MIMD workers → vectorized operators → SIMD lanes` có thể truy được ở cả hai nơi:

- M14: `material/data-engineer/roadmap/roadmap.md:4219,4386-4398`.
- M23: `material/data-engineer/roadmap/roadmap.md:7223-7235`.

## E. Cây `curriculum/`

| Kiểm tra | Kết quả |
|---|---|
| 29 thư mục module | ĐẠT |
| 440 thư mục lesson | ĐẠT |
| Mỗi lesson có note/quiz/homework/slides và đúng một `.drawio` | ĐẠT |
| 469 drawio trong scope (440 lesson + 29 roadmap module) parse XML | ĐẠT, 0 lỗi |
| `lesson`, `tieu_de`, `dang_bai` frontmatter khớp roadmap | ĐẠT, 440/440 |
| `module` frontmatter khớp exact | KHÔNG ĐẠT, 70 lỗi casing |
| Chín trường đặc tả note khớp exact roadmap tổng | ĐẠT 439/440; lesson 440 lỗi |
| Roadmap module liệt kê đúng tập lesson | ĐẠT, 29/29 |

## F. Văn phong và phát biểu

- Không tìm thấy kiểu dùng gạch ngang dài thay mọi liên từ: chỉ có 2 em dash `—` ngoài các vị trí định dạng.
- Mẫu “không phải X mà là Y” xuất hiện 10 lần trên 440 bài; các lần đọc mẫu đều dùng để phân biệt khái niệm, chưa đủ bằng chứng kết luận văn AI hệ thống.
- Từ bơm phồng trong danh sách scan (`đột phá`, `toàn diện`, `xuất sắc`, `tối thượng`, `hoàn hảo`, `cách mạng`, `vượt trội`) chỉ có một hit “quy ước hoàn hảo”, dùng trong câu phản biện chứ không quảng cáo.
- Bold chủ yếu là chín nhãn field bắt buộc; không tìm thấy pattern bôi đậm trang trí dày đặc ngoài các điểm nhấn khái niệm.
- 0 URL trong phạm vi, nên không có link chết/lậu/trả phí bị che giấu để báo.

## Data Analyst không bị hỏng lây

- `make test` vẫn PASS phần DA.
- Cây DA vẫn có 11 module và 85 bài.
- `git diff --name-only -- material/data-analyst` trả rỗng.

## Giới hạn của lần rà soát

- Kiểm nghĩa thủ công 60/447 tham chiếu prose, không tuyên bố 387 occurrence còn lại đã được đọc nghĩa. Toàn bộ 447 đã được kiểm range tự động.
- Đối chiếu nội dung sâu đúng 6 module theo yêu cầu, không suy rộng kết luận coverage sang 23 module còn lại.
- Không chạy các lệnh sinh lại vì chúng có thể ghi file. Vì vậy chưa kiểm idempotence của `make scaffold`, `make diagrams` hoặc `assemble_ade.py`.
- Không có URL trong output roadmap để chạy link checker; trạng thái link trong hợp đồng nguồn nằm ngoài phạm vi output được yêu cầu.
- Báo cáo là audit R1, chưa có owner approval. Quyết định sửa và duyệt lại thuộc curriculum owner.
