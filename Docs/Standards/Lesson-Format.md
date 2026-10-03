# FORMAT NOTE V4 — TEXTBOOK × C3

Trạng thái: **ĐÃ ĐƯỢC OWNER CHỐT — ĐANG TRIỂN KHAI THEO GIAI ĐOẠN**  
Ngày: 2026-09-25  
Phạm vi: `note.md` và `after-note.md` cho 525 bài  
Nguồn hình thức: *Designing Event-Driven Systems* — Ben Stopford, O’Reilly, 2018

---

## 1. Các quyết định đã ghi nhận

1. `note.md` không bị giới hạn bởi thời lượng đứng lớp.
2. Người dạy tự chọn phần và tự căn thời gian.
3. `note.md` trình bày như một chương giáo trình hoặc khóa luận kỹ thuật.
4. Bỏ YAML frontmatter khỏi `note.md`.
5. Bỏ mục `Trước khi bắt đầu`.
6. Đầu note có ba dòng H1: Phase → Module → Lesson.
7. Đổi `Nguồn và phạm vi sử dụng` thành `Reference`.
8. Bảng nguồn bỏ cột trạng thái.
9. Chuyển thực hành, kiểm tra cuối bài và bài sau buổi học sang `after-note.md`.
10. Thêm `Key takeaways` vào cuối phần nội dung, trước `Reference`.

Hệ quả thiết kế: `note.md` trở thành tài liệu học thuật thuần nội dung. `after-note.md` là companion
workbook chứa phần áp dụng và đánh giá. Metadata build không còn nằm trong nội dung xuất bản.

---

## 2. Cấu trúc thư mục sau thay đổi

```text
lesson_<NNN>_<title>/
├── lesson.yaml       metadata cho tool; không xuất bản
├── note.md           chương giáo trình
├── after-note.md     thực hành, kiểm tra, bài làm
├── quiz.md           ngân hàng câu hỏi hoặc đề quiz riêng
├── homework.md       artefact cũ; ngừng dùng sau migration
├── slides.md
├── materials/
└── *.drawio
```

`lesson.yaml` là đề xuất kỹ thuật để thay frontmatter. Nó không xuất hiện trong PDF hoặc web.

```yaml
schema_version: 1
status: draft          # draft | review | ready
publish:
  note: true
  after_note: true
  answer_key: false
```

Không lặp chương trình, phase, module, lesson, title, dạng bài hoặc thời lượng trong sidecar. Các
giá trị đó đã có trong roadmap và đường dẫn. Sidecar chỉ giữ trạng thái workflow và visibility.

Nếu owner không muốn sidecar, lựa chọn còn lại là build suy trạng thái từ nội dung. Phương án đó
mong manh: scaffold và bài đã viết đều có `note.md`, nên file existence không phân biệt được draft
với ready. V4 khuyến nghị sidecar.

---

## 3. Đầu mỗi `note.md`

Đúng ba H1 theo yêu cầu:

```markdown
# Phase x: <Tên phase>
# Module x: <Tên module>
# Lesson x: <Tên lesson>
```

Quy tắc:

- Data Analyst không có phase chính thức: dùng `# Phase 1: Data Analyst Core Curriculum` cho toàn
  chương trình, hoặc bổ sung phase DA trong roadmap trước khi sinh note. Không tự bịa phase theo bài.
- Tên lấy từ roadmap; không dịch hoặc đổi casing trong note.
- Không lặp chương trình, loại bài, thời lượng, đối tượng hoặc trạng thái ở đầu file.
- Không thêm cover table, abstract metadata hoặc “Thông tin bài học”.
- Ngay sau ba H1 là phần văn mở chương hoặc `## Kết quả cần đạt`.

### Lưu ý kỹ thuật về ba H1

Ba H1 liên tiếp không tạo hierarchy HTML chuẩn; về ngữ nghĩa, Phase và Module là cấp cha của Lesson.
Vì đây là yêu cầu trình bày đã chọn, renderer cần thêm class hoặc CSS để ba dòng trông như running
title và chỉ Lesson được đưa vào mục lục cấp cao. Không đổi ba dòng thành H1/H2/H3 trong source.

---

## 4. Cấu trúc `note.md`

```text
# Phase...
# Module...
# Lesson...

## Kết quả cần đạt

[Đoạn mở chương, không heading “Giới thiệu”]

## <Heading nội dung 1>
## <Heading nội dung 2>
## <Heading nội dung 3>
...
## <Heading về lựa chọn hoặc trade-off, nếu có>
## <Heading về giới hạn, nếu có>

## Key takeaways
## Reference
```

Chỉ ba heading cố định trong thân note:

- `Kết quả cần đạt`
- `Key takeaways`
- `Reference`

Mọi heading giữa chúng phải mang nội dung riêng của bài.

Không còn trong `note.md`:

- Frontmatter.
- `Đặc tả từ roadmap`.
- `Trước khi bắt đầu`.
- Dạng bài và thời lượng.
- Phân bổ phút đứng lớp.
- Hướng dẫn giảng viên.
- Thực hành.
- Kiểm tra cuối bài.
- Bài làm sau buổi học.
- Trạng thái nguồn.
- Kết luận chung chung.

---

## 5. Kết quả cần đạt

Mục này giữ C3 nhưng viết gọn như learning contract, không giống bảng metadata.

### Dạng prose — khuyến nghị cho LT

```markdown
## Kết quả cần đạt

Sau khi hoàn thành chương này, người học có thể:

- dựng một latency hierarchy từ số đo trên chính máy đang dùng;
- phân biệt workload bị giới hạn bởi CPU, memory bandwidth và I/O;
- dự đoán điểm dữ liệu vượt cache trước khi chạy benchmark;
- bảo vệ một lựa chọn layout bằng số đo, không bằng tên công nghệ.
```

### Dạng bảng — dùng khi evidence phức tạp

```markdown
## Kết quả cần đạt

| Năng lực | Bằng chứng | Ngưỡng đạt |
|---|---|---|
| Phân biệt ba bottleneck | Bảng số đo của ba workload | Kết luận đúng 3/3 và dẫn đúng counter |
| Chọn data layout | Decision record | Có baseline, trade-off và điểm đảo |
```

Không ghi:

- thời lượng;
- audience;
- prerequisite;
- thiết bị cần có;
- “bài này chưa bao gồm”.

Scope được xử lý tự nhiên trong đoạn mở hoặc phần giới hạn của chương.

---

## 6. Phần mở chương

Không dùng heading `Giới thiệu`. Viết 2–6 đoạn theo nhịp giáo trình:

1. Cách làm hoặc intuition quen thuộc.
2. Trường hợp khiến intuition đó thiếu hoặc sai.
3. Câu hỏi trung tâm của chương.
4. Ranh giới nội dung nếu cần.

Mẫu:

```markdown
Một phép đọc bộ nhớ và một phép đọc từ đĩa đều được viết thành thao tác “đọc dữ liệu”. Chi phí của
chúng không cùng thang đo. Khi chương trình đi qua ranh giới cache, cùng một vòng lặp có thể đổi
hẳn hình dạng hiệu năng dù độ phức tạp thuật toán không đổi.

Chênh lệch đó giải thích vì sao hai cách bố trí cùng một bảng cho kết quả khác nhau, vì sao batching
thắng xử lý từng phần tử và vì sao thêm thread có thể làm chương trình chậm hơn. Chương này xây một
mô hình chi phí đủ dùng để dự đoán các hiện tượng đó trước khi chọn công cụ tối ưu.
```

Không mở bằng:

- “Trong thế giới dữ liệu ngày nay...”;
- “Bài này sẽ giúp bạn...”;
- lịch sử dài chưa phục vụ câu hỏi;
- danh sách thuật ngữ;
- tình huống giả có nhân vật và hội thoại thừa.

---

## 7. Thân chương giáo trình

Thân chương chiếm phần lớn `note.md` và không có giới hạn từ. Độ dài do độ sâu khái niệm quyết định.

### Trật tự khoa học

```text
quan sát → mô hình → cơ chế → bằng chứng → hệ quả → lựa chọn → giới hạn
```

Không buộc mỗi bài phải có đủ bảy block tách biệt. Chúng là trật tự suy luận, không phải checklist
heading.

### Heading theo nội dung

Đạt:

- `Cache line biến truy cập một byte thành truy cập một vùng`
- `Khi working set vượt L3 cache`
- `Hash join tràn khỏi bộ nhớ`
- `Một dòng trong bảng này đại diện cho gì?`
- `Mẫu số đổi, metric đổi nghĩa`
- `Snapshot và CDC dưới cùng một tải nguồn`

Không đạt:

- `Tổng quan`
- `Cơ sở lý thuyết`
- `Deep dive`
- `Các khái niệm quan trọng`
- `Ứng dụng thực tế`
- `Những điều cần lưu ý`
- `Kết luận`

### Mỗi section phải có luận điểm

Một section tốt có thể gồm:

- claim hoặc câu hỏi;
- mechanism;
- figure, table, equation hoặc trace nếu cần;
- evidence hoặc nguồn;
- consequence cho thiết kế/phân tích;
- boundary hoặc counterexample.

Không cần đủ sáu thành phần khi một section chỉ làm cầu nối. Nhưng section dài không được chỉ kể
tính năng hoặc diễn giải thuật ngữ.

---

## 8. Deep-dive theo C3

Deep-dive nằm trong mạch chương, không được tách thành mục có tên `Deep dive`.

### Với systems/DE

Đi xuống tới:

- state;
- state transition;
- ordering;
- ownership;
- atomicity;
- failure boundary;
- dấu vết có thể quan sát;
- recovery path.

### Với DA/statistics

Đi xuống tới:

- grain;
- population và sample;
- data-generating assumptions;
- numerator, denominator và window;
- estimator/metric behavior;
- bias, missingness và confounding;
- consequence cho quyết định.

### Với modeling/AE

Đi xuống tới:

- business process;
- grain và key;
- invariant;
- change semantics;
- consumer contract;
- compatibility;
- reconciliation và lineage.

Độ sâu đạt khi người đọc dự đoán được ca chưa gặp. Số trang, số thuật ngữ và độ dài code không
phải bằng chứng của độ sâu.

---

## 9. Case xuyên chương

Một chương ưu tiên một case chính được mở rộng dần. Case có thể là:

- hệ thống;
- dataset;
- truy vấn;
- thiết kế thí nghiệm;
- metric;
- sự cố;
- decision memo.

Case tốt có input, constraint, hai phương án hợp lệ, một failure, một phép kiểm và ít nhất một điều
kiện làm quyết định đổi.

Ghi rõ `Tình huống mô phỏng` nếu không có hồ sơ thực. Không viết case giả như sự kiện đã xảy ra.

---

## 10. Figure, table, code và callout

### Figure

```markdown
![Luồng publish partition sau reconciliation](materials/lesson-243-readiness-flow.svg)

*Hình L243-1. Consumer chỉ đọc partition sau khi ba điều kiện readiness cùng đạt.*
```

- Đánh số theo lesson.
- Caption nói figure chứng minh điều gì.
- Figure được viện dẫn trong văn xuôi.
- Sơ đồ hệ thống có boundary, direction, state owner và failure point.
- Hình ngoài có source/locator và quyền sử dụng.

### Table

Dùng khi dữ liệu có schema lặp: lựa chọn, state transition, failure matrix, benchmark, rubric hoặc
expected output. Không nhét nhiều đoạn văn vào ô.

### Code

Mỗi code block có mục đích, input/state ban đầu và phép kiểm output. Code dài chuyển vào
`materials/`; note giữ đoạn đang được phân tích.

### Callout

Giữ bốn loại:

```markdown
> **NOTE** — Chi tiết bổ trợ không nằm trên critical path.

> **WARNING** — Failure có thể làm sai hoặc mất dữ liệu.

> **DEEP DIVE** — Cơ chế bên dưới cần để dự đoán hành vi.

> **SCOPE** — Phần nằm ngoài chương hoặc được xử lý ở lesson khác.
```

Không dùng callout cho khẩu hiệu hoặc câu chỉ vì muốn nhấn mạnh.

---

## 11. Key takeaways

Đặt gần cuối note, ngay trước `Reference`.

```markdown
## Key takeaways

- Ordering của Kafka chỉ được bảo đảm trong một partition.
- Consumer offset cho biết vị trí đã cam kết, không chứng minh side effect đã hoàn tất.
- Exactly-once trong một boundary không biến toàn bộ hệ thống thành exactly-once.
- Retry an toàn cần idempotency hoặc atomic boundary phù hợp.
- Khi boundary đổi, guarantee phải được đánh giá lại từ đầu.
```

Quy tắc:

- 4–8 ý.
- Mỗi ý là một proposition kỹ thuật có thể kiểm hoặc phản biện.
- Không mở bằng “hãy nhớ”, “điều quan trọng nhất”, “chìa khóa”.
- Không lặp nguyên tiêu đề section.
- Không thêm claim mới.
- Không biến thành executive summary dài.

---

## 12. Reference

Tên cố định: `## Reference`.

### Citation trong thân bài

```markdown
Kafka giữ thứ tự trong phạm vi một partition [S1, ch. 4, pp. 21–22].
```

### Bảng cuối bài

```markdown
## Reference

| ID | Tài liệu | Locator | Phần sử dụng |
|---|---|---|---|
| S1 | Ben Stopford, *Designing Event-Driven Systems*, 2018 | ch. 4, pp. 17–25 | Log, ordering, durability |
| S2 | Apache Kafka Documentation 4.1 | Design → Transactions | Transaction mechanism |
```

Không có cột trạng thái.

Nếu có điểm chưa xác minh, ghi trong prose gần claim hoặc trong một mục `Giới hạn` của chương;
không dùng cột trạng thái nguồn để giấu uncertainty.

---

## 13. Cấu trúc `after-note.md`

`after-note.md` là workbook đi cùng lesson. Nó không lặp lý thuyết trong `note.md`.

```markdown
# Phase x: <Tên phase>
# Module x: <Tên module>
# Lesson x: <Tên lesson>

## Thực hành

### Worked trace

<!-- Một ca có lời giải hoặc reasoning trace. -->

### Guided task

<!-- Input · constraint · checkpoint · output. -->

### Independent task

<!-- Input mới; không dùng lại lời giải worked trace. -->

### Changed constraint

<!-- Một điều kiện đổi làm quyết định hoặc thiết kế phải đổi. -->

## Kiểm tra cuối bài

### Recall cần thiết

### Apply hoặc diagnose

### Transfer

### Cách chấm

| Tiêu chí | Đạt | Chưa đạt | Critical failure |
|---|---|---|---|
| | | | |

## Bài làm sau buổi học

### Bài làm

### Kiểm lại sau một khoảng thời gian

### Cách nộp và bằng chứng cần giữ
```

### Nguyên tắc tách file

- `note.md` giải thích và lập luận.
- `after-note.md` buộc người học làm và tạo evidence.
- Không copy section lý thuyết từ note sang after-note.
- Cross-link bằng section/figure rõ ràng.
- Answer key đầy đủ không đặt trong file công khai nếu web xuất file này cho học viên.
- `quiz.md` có thể tiếp tục làm ngân hàng câu hỏi; tránh lặp nguyên kiểm tra trong after-note.
- `homework.md` được thay thế bởi `after-note.md` sau migration; không duy trì hai nguồn lâu dài.

---

## 14. Profile LT, TH, DA và KT

### LT

`note.md` là chương giáo trình đầy đủ. `after-note.md` chứa worked trace, application và transfer.

### TH

`note.md` vẫn giải thích cơ chế, state, invariant và failure. Quy trình lab, lệnh chạy, expected
output, failure injection và cleanup nằm trong `after-note.md`.

### DA

`note.md` trình bày domain, decision, constraints, alternatives và tiêu chuẩn thiết kế.
`after-note.md` chứa brief, milestone, review protocol, rubric và defense question.

### KT

`note.md` có thể rất ngắn hoặc không phát hành thêm nội dung mới. `after-note.md` chứa đề, artefact
cần nộp, rubric công khai và critical failures. Answer key nằm trong file private riêng.

---

## 15. Template `note.md`

```markdown
# Phase x: <Tên phase>
# Module x: <Tên module>
# Lesson x: <Tên lesson>

## Kết quả cần đạt

<!-- Prose hoặc bảng năng lực/evidence/ngưỡng. Không ghi time/audience/prerequisite. -->

<!-- ĐOẠN MỞ CHƯƠNG: 2–6 đoạn, không heading “Giới thiệu”. -->

## <Heading nội dung 1>

<!-- Observation/problem → model. -->

## <Heading nội dung 2>

<!-- Mechanism/causal chain. -->

## <Heading nội dung 3>

<!-- Case xuyên chương, figure, table hoặc code khi cần. -->

## <Heading về lựa chọn và trade-off>

<!-- Context, cost, điểm đảo quyết định. -->

## <Heading về giới hạn>

<!-- Chỉ giữ nếu có giới hạn cần nói rõ. -->

## Key takeaways

- ...

## Reference

| ID | Tài liệu | Locator | Phần sử dụng |
|---|---|---|---|
| | | | |
```

Không giữ heading placeholder rỗng. Body có thể có 3–10 H2 theo nội dung; không có giới hạn số từ.

---

## 16. Mẫu `note.md` rút gọn

```markdown
# Phase 1: Engineering Foundations
# Module 4: Computer Architecture and the Performance Model
# Lesson 45: The memory hierarchy and the cost model

## Kết quả cần đạt

Sau khi hoàn thành chương này, người học có thể dựng một memory hierarchy từ số đo trên máy đang
dùng, phân biệt workload bị giới hạn bởi CPU, memory bandwidth và I/O, rồi bảo vệ một lựa chọn
data layout bằng benchmark có kiểm soát.

Hai thao tác cùng được gọi là “đọc dữ liệu” có thể lệch nhau nhiều bậc độ lớn. Một phép đọc trúng
L1 cache và một phép đọc ngẫu nhiên từ storage không nằm trên cùng thang chi phí. Khi working set
đi qua ranh giới cache, cùng một thuật toán có thể đổi hình dạng hiệu năng mà Big-O không đổi.

Chương này xây mô hình chi phí để dự đoán các điểm gãy đó. Các con số cụ thể phụ thuộc CPU,
storage, compiler và workload; mô hình quan tâm tới thứ tự tương đối và cách đo trên hệ đang dùng.

## Dữ liệu đi qua nhiều tầng trước khi tới CPU

CPU không đọc trực tiếp mọi giá trị từ RAM. Dữ liệu đi qua register và nhiều mức cache; mỗi tầng
đổi latency lấy capacity. Cache nạp theo line, không theo biến mà source code đang truy cập.

Hệ quả là một phép đọc một byte có thể kéo cả vùng lân cận vào cache. Duyệt tuần tự dùng phần dữ
liệu đã được kéo vào; truy cập ngẫu nhiên thường bỏ phí nó. Đây là cơ chế phía dưới spatial locality,
không phải thuộc tính riêng của một ngôn ngữ hoặc thư viện.

## Working set tạo ra cache cliff

Benchmark một vòng lặp ở nhiều kích thước input. Khi working set còn nằm trong một mức cache,
latency trên mỗi phần tử tương đối ổn định. Khi input vượt capacity hiệu dụng của tầng đó, số miss
tăng và đường đo tạo một bậc mới.

Capacity hiệu dụng không bằng con số danh nghĩa. Code, dữ liệu khác, associativity và access pattern
cùng cạnh tranh không gian cache. Vì vậy benchmark phải sweep nhiều kích thước và lặp đủ để tách
warm-up khỏi steady state.

## Row layout và column layout trả giá ở hai workload khác nhau

Row layout đặt các field của một record cạnh nhau. Nó phù hợp khi workload đọc phần lớn record.
Column layout đặt giá trị cùng field cạnh nhau, giảm lượng dữ liệu phải đưa qua cache khi truy vấn
chỉ dùng vài cột.

Không có layout thắng tuyệt đối. Điểm đảo nằm ở projection width, selectivity, compression và cost
của write/update. Một benchmark chỉ quét một cột không đủ để kết luận layout cột tốt hơn cho toàn
hệ thống.

## Khi mô hình phân tầng không còn đủ

Memory hierarchy giải thích locality và nhiều cache effect, nhưng không tự giải thích NUMA,
prefetcher behavior, contention hoặc I/O scheduling. Những yếu tố đó cần phép đo và mô hình bổ sung.
Không suy benchmark trên laptop thành guarantee cho production server.

## Key takeaways

- Cache hoạt động theo line, không theo biến trong source code.
- Working set vượt một tầng cache tạo điểm gãy có thể đo được.
- Sequential access tận dụng spatial locality; random access thường làm mất lợi ích đó.
- Row và column layout tối ưu cho các access pattern khác nhau.
- Kết luận hiệu năng chỉ có giá trị trong điều kiện benchmark đã ghi lại.

## Reference

| ID | Tài liệu | Locator | Phần sử dụng |
|---|---|---|---|
| S1 | *Computer Systems: A Programmer’s Perspective* | Chương về memory hierarchy | Cache, locality, working set |
| S2 | Tài liệu kiến trúc CPU của nhà cung cấp | Phiên bản được dùng trong lab | Cache line và counter |
```

---

## 17. Ảnh hưởng tới toolchain hiện tại

Yêu cầu mới **không tương thích** với toolchain hiện tại nếu chỉ sửa 525 note.

| Thành phần | Phụ thuộc hiện tại | Thay đổi bắt buộc |
|---|---|---|
| `Web/parse_curriculum.py` | Đọc `trang_thai`, `tieu_de` từ frontmatter | Lấy title/ID từ roadmap + path; status từ `lesson.yaml` |
| `build_bai.py` | Đọc frontmatter và lọc `chua-viet` | Đọc `lesson.yaml`; build thêm `after-note.md` |
| `make status` | Đếm `trang_thai` trong note | Đếm `lesson.yaml.status` |
| `scaffold_material.py` | Sinh note có frontmatter và chín mục | Sinh note/after-note/lesson.yaml theo V4 |
| `check_curriculum.py` | Bắt frontmatter và bốn component cũ | Kiểm ba H1, structure, sidecar và after-note |
| Web lesson view | Chỉ đưa nội dung note đã “xong” | Render note và after-note thành hai tab/section |
| PDF build | `note.md` → giáo trình; `homework.md` → homework | `note.md` → chapter; `after-note.md` → workbook |

### Migration phải nguyên tử

Không được xóa frontmatter trước rồi mới sửa parser ở commit sau. Thứ tự an toàn:

1. Thêm parser/build hỗ trợ song song schema cũ và V4.
2. Thêm test fixture V4.
3. Migrate ba pilot LT/TH/KT.
4. Build web/PDF và so output.
5. Owner duyệt pilot.
6. Migrate scaffold còn lại.
7. Khi 525 bài đã sang V4, bỏ hỗ trợ schema cũ.

Rollback: trong giai đoạn dual-read, revert ba pilot về schema cũ mà không ảnh hưởng 522 bài còn lại.

---

## 18. Test bắt buộc cho V4

- Ba H1 tồn tại, đúng thứ tự Phase → Module → Lesson và khớp roadmap.
- `note.md` không có YAML frontmatter.
- `note.md` không chứa `Trước khi bắt đầu`, thời lượng, dạng bài hoặc trạng thái.
- Có `Kết quả cần đạt`, `Key takeaways`, `Reference`.
- Bảng Reference đúng bốn cột, không có `Trạng thái`.
- `note.md` không có ba phần đã chuyển sang after-note.
- `after-note.md` có Thực hành, Kiểm tra cuối bài và Bài làm sau buổi học.
- Timeline/phút không còn là contract của note.
- Cross-reference từ after-note tới note resolve được.
- Parser/build đọc title và status mà không cần frontmatter.
- PDF/web render ba H1, figure, caption, code, callout và Reference đúng.
- `make test` chỉ được coi là pass sau khi có các kiểm tra V4 trên.

---

## 19. Cổng phê duyệt còn lại

Các quyết định nội dung/format ở §1 được coi là yêu cầu đã chốt. Còn ba quyết định triển khai:

1. Dùng `lesson.yaml` hay cơ chế status khác ngoài note.
2. Data Analyst dùng một Phase chung hay bổ sung phase chính thức vào roadmap.
3. `after-note.md` hiển thị công khai trên web hay chỉ được đóng gói thành workbook/PDF.

Chưa migrate toolchain hoặc bài học trước khi ba điểm này được chốt.

---

## 20. Bản ghi task

```yaml
task: academy-design-learning-module
profile: learning
risk_tier: R1-reviewed
phase_reached: design
deliverable: technical-curriculum-chapter-standard-v4-proposal
selected_option: textbook-note-plus-after-note-workbook
content_decisions:
  duration_bound: false
  note_frontmatter: removed
  prerequisites_block: removed
  chapter_headers: phase-module-lesson
  key_takeaways: added
  reference_heading: Reference
  reference_status_column: removed
  application_file: after-note.md
approval:
  owner: kina2711
  content_format: accepted-with-user-specified-changes
  implementation_decisions: pending
tests_run:
  - inspected-current-parser-build-scaffold-test-dependencies
  - validated-note-and-after-note-templates
  - documented-dual-read-migration-and-rollback
not_run:
  - toolchain-migration
  - LT-TH-KT-pilot
  - web-and-pdf-render
  - instructor-or-learner-test
next_task: owner-selects-status-storage-DA-phase-policy-and-after-note-visibility
```
