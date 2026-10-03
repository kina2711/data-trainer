# FORMAT NOTE V3 — TEXTBOOK × C3

Trạng thái: **BẢN ĐỀ XUẤT — CHỜ DUYỆT**  
Ngày: 2026-09-25  
Phạm vi: `note.md` cho 525 bài Data Analyst và Data Engineer  
Nguồn tham khảo hình thức: *Designing Event-Driven Systems* — Ben Stopford, O’Reilly, 2018  
Hướng thiết kế: trình bày như một chương giáo trình kỹ thuật; deep-dive và đánh giá theo C3

---

## 1. Quyết định đề xuất

Chọn cấu trúc **Textbook spine + C3 evidence frame**:

```text
Hợp đồng bài học
      ↓
Mạch chương sách: vấn đề → mô hình → cơ chế → hệ thống hoàn chỉnh → lựa chọn → giới hạn
      ↓
Thực hành: worked trace → guided task → independent task → changed constraint
      ↓
Đánh giá, hướng dẫn đứng lớp, nguồn và giới hạn
```

Phần giữa đọc như một chương sách, không như form được điền. C3 bao quanh chương sách để bảo đảm
objective, evidence, transfer và khả năng đứng lớp không bị bỏ quên.

Tên baseline đề xuất: **Technical Curriculum Chapter Standard**.

---

## 2. Những gì học từ cuốn tham khảo

Đã kiểm PDF 166 trang, metadata ghi First Edition 2018. Chỉ phân tích cấu trúc và trình bày; không
sao chép văn bản hoặc hình của sách vào format.

| Trang PDF | Trang in | Đặc điểm quan sát được | Cách dùng trong format mới |
|---:|---:|---|---|
| 4–7 | iii–vi | TOC chia Part → Chapter → section; section mang nội dung cụ thể | Bài thuộc module/phase; heading con phải nói đúng khái niệm |
| 28 | 13 | Chương 3 mở bằng một cách hiểu sai/phân mảnh rồi so các cách nhìn | Mở bài bằng tension hoặc misconception có thật |
| 44 | 29 | Chương 5 mở từ kiến trúc quen thuộc, chỉ ra failure khi scale, rồi mới đưa hướng khác | Vấn đề và causal pressure đi trước solution |
| 53 | 38 | “Which Approach to Use” so lợi ích hai phía và gắn lựa chọn với quy mô/context | Decision section phải có điều kiện đảo quyết định |
| 116 | 101 | Chương 11 làm rõ thuật ngữ bị dùng quá rộng, giới hạn scope ngay đầu | Định nghĩa boundary và non-goal trước deep-dive |
| 125 | 110 | Tách “Limitations” khỏi “Summary”; thừa nhận pattern không phải lời giải tổng quát | Mỗi bài có giới hạn thật, không kết bằng khẩu hiệu |
| 126 | 111 | Chương 12 nêu ba việc transaction giải quyết, rồi đi xuống cơ chế bên dưới | Từ observable problem xuống mechanism |
| 154 | 139 | Chương 15 dùng một hệ thống xuyên suốt, có hình, code link và footnote | Một worked system/case chạy xuyên chương |
| 163 | 148 | “Reflecting on the Design” cân cost của distributed design với simplicity | Deep-dive phải trở lại trade-off vận hành |

### Các đặc điểm trình bày nên giữ

- Một chương có thesis rõ nhưng không mở bằng bảng objective dài.
- Văn xuôi nối ý; bảng và bullet chỉ dùng khi cấu trúc dữ liệu đòi hỏi.
- Heading cụ thể theo nội dung, không lặp một bộ nhãn ở mọi trang.
- Hình nằm gần luận điểm và có caption.
- Cross-reference giúp khái niệm tích lũy qua nhiều chương.
- Footnote chứa nguồn hoặc ngoại lệ, không làm đứt mạch chính.
- Có decision point, limitations và reflection.
- Case lớn xuất hiện xuyên chương thay vì nhiều ví dụ nhỏ không liên quan.

### Những điểm không lấy nguyên từ sách

Cuốn sách không phải giáo án 120 phút nên thiếu:

- Outcome có ngưỡng.
- Guided và independent practice.
- Formative checkpoint.
- Rubric và critical failure.
- Remediation.
- Runbook cho giảng viên.
- Traceability từng claim về note ref của repo.

C3 bổ sung các phần này ở “khung ngoài”; không chèn bảng sư phạm vào giữa mọi đoạn của chương.

---

## 3. Kiến trúc tổng thể

Một note gồm năm lớp. Chỉ lớp 1, 2, 4, 5 có heading cố định; lớp 3 dùng heading theo nội dung.

```text
Lớp 1 · Metadata máy đọc
Lớp 2 · Hợp đồng bài học
Lớp 3 · Chương giáo trình
Lớp 4 · Thực hành và đánh giá
Lớp 5 · Vận hành lớp học và provenance
```

### Lớp 1 · Metadata máy đọc

Giữ nguyên:

- Frontmatter bảy khoá.
- H1 của lesson.
- `## Đặc tả từ roadmap` khớp từng chữ.

Không biên tập văn phong trong khối roadmap tại bước viết note. Roadmap và giáo trình là hai artefact
khác nhau; thay một bên âm thầm làm mất traceability.

### Lớp 2 · Hợp đồng bài học

Hai mục cố định, ngắn, đặt trước chương sách:

```markdown
## Kết quả cần đạt
## Trước khi bắt đầu
```

`Kết quả cần đạt` trả lời evidence và threshold. `Trước khi bắt đầu` chứa prerequisite check,
environment, dữ liệu và boundary. Tổng hai mục không quá 10% note.

### Lớp 3 · Chương giáo trình

Đây là phần chính, chiếm 55–70% note. Không có bộ heading cố định. Tác giả đặt 3–7 H2 theo đúng
mạch của chủ đề.

Một chương LT điển hình:

```text
Đoạn mở chương, không heading
  ↓
<vấn đề cụ thể>
  ↓
<mô hình hoặc cách nhìn>
  ↓
<cơ chế dưới nắp máy>
  ↓
<case/hệ thống xuyên suốt>
  ↓
<lựa chọn và trade-off>
  ↓
<giới hạn và điều còn chưa giải quyết>
```

Ví dụ heading hợp lệ:

- `Một dòng trong bảng này đại diện cho gì?`
- `Log giữ thứ tự trong một partition`
- `Retry tạo bản ghi trùng ở đâu`
- `Snapshot và CDC dưới cùng một tải nguồn`
- `Khi single writer không còn đủ`

Không dùng `Tổng quan`, `Cơ sở lý thuyết`, `Khung quyết định`, `Nghiên cứu tình huống` làm heading
thân bài. Đó là nhãn template, không phải nội dung.

### Lớp 4 · Thực hành và đánh giá

Ba mục cố định:

```markdown
## Thực hành
## Kiểm tra cuối bài
## Bài làm sau buổi học
```

Thực hành đi từ trace có lời giải tới task mới. Kiểm tra cuối bài chỉ chứa evidence đủ để xác
nhận Outcome. Bài làm sau buổi học đo retention hoặc transfer, không lặp lab.

### Lớp 5 · Vận hành và provenance

Ba mục cố định ở cuối:

```markdown
## Hướng dẫn đứng lớp
## Nguồn và phạm vi sử dụng
## Điểm còn mở
```

`Hướng dẫn đứng lớp` không đưa lên luồng đọc chính trên web nếu sau này parser hỗ trợ role-based
rendering. Trong phiên bản hiện tại, giữ nó ngắn và đặt cuối để không cắt mạch chương sách.

---

## 4. Anatomy của một chương giáo trình

## Đoạn mở chương

Không đặt heading “Giới thiệu”. Dùng 2–5 đoạn văn để thiết lập:

1. Trạng thái hoặc cách làm quen thuộc.
2. Điều kiện khiến cách làm đó hỏng hoặc thiếu.
3. Câu hỏi kỹ thuật của bài.
4. Scope và non-goal nếu dễ hiểu quá rộng.

Mẫu:

```markdown
Một job kết thúc với exit code 0. Partition đích đã xuất hiện. Dashboard vẫn thiếu 18% giao dịch
của hôm qua.

Ba tín hiệu trên không mâu thuẫn. Job chỉ chứng minh tiến trình đã kết thúc; partition chỉ chứng
minh có dữ liệu được ghi. Consumer cần một điều kiện mạnh hơn: dữ liệu đã đến đủ, đã vượt phép
kiểm và đã được công bố.

Bài này xây readiness contract cho batch pipeline. Nó không bàn scheduling algorithm hoặc cách
chọn orchestrator.
```

Không mở bằng:

- định nghĩa từ điển;
- lịch sử dài;
- “Trong thế giới dữ liệu ngày nay”;
- “Bài này sẽ giúp bạn...”;
- câu chuyện có nhân vật giả nếu nhân vật không ảnh hưởng quyết định.

## Mô hình trước chi tiết

Sau đoạn mở, đưa ra representation nhỏ nhất cho phép suy luận:

- state machine;
- data flow;
- invariant;
- grain statement;
- causal diagram;
- numerator/denominator/window;
- ownership boundary.

Mô hình phải có caption hoặc một câu giải thích phạm vi. Không đặt sơ đồ chỉ để trang đẹp.

## Cơ chế theo causal chain

Mỗi deep-dive trả lời bốn câu:

1. State nào tồn tại?
2. Event hoặc operation nào làm state đổi?
3. Ordering/atomicity/ownership nằm ở đâu?
4. Failure chen vào bước nào và để lại dấu vết gì?

Với bài DA/statistics, thay bằng:

1. Dữ liệu được sinh theo giả định nào?
2. Grain, population và sample là gì?
3. Estimator/metric biến input thành output thế nào?
4. Bias hoặc missingness làm kết luận đổi ở đâu?

Deep-dive không đồng nghĩa với dài. Nó nghĩa là đi tới cơ chế đủ để người học dự đoán ca chưa gặp.

## Case xuyên suốt

Mỗi bài ưu tiên một case chính. Case được mở rộng dần khi thêm khái niệm.

Một case tốt có:

- input hữu hạn;
- constraint rõ;
- ít nhất hai phương án hợp lệ;
- một failure được tiêm;
- phép đo hoặc output đối chiếu được;
- changed constraint làm quyết định đổi.

Không ghép năm ví dụ mini chỉ để mỗi heading có một ví dụ.

## Lựa chọn và trade-off

Trình bày giống logic ở phần “Which Approach to Use” của sách tham khảo:

- Lợi ích của mỗi lựa chọn.
- Cost vận hành/nhận thức.
- Context mà lựa chọn thắng.
- Context làm lựa chọn mất hiệu lực.
- Phương án pha trộn nếu có, kèm cost mới.

Không viết “X tốt hơn Y”. Viết “X thắng Y khi...” và nêu tín hiệu đo được.

## Giới hạn

Mục giới hạn không phải disclaimer. Nó trả lời:

- Model nào đã bị đơn giản hóa?
- Pattern nào chỉ đúng trong common case?
- Constraint nào chưa được xử lý?
- Claim nào cần benchmark/nguồn mới?
- Phần nào thuộc bài sau?

Một bài deep-dive không có giới hạn thường đang nói quá phạm vi.

## Nhìn lại thiết kế

Không bắt buộc có heading riêng. Sau case lớn hoặc cuối chương, dành 1–3 đoạn trả lời:

- Ta đã mua được tính chất nào?
- Ta trả giá bằng complexity, cost hoặc coupling nào?
- Với hệ nhỏ hơn, lựa chọn đơn giản hơn có thắng không?

Đây là phần “reflection” kiểu giáo trình kỹ thuật, không phải “Key takeaways”.

---

## 5. Hệ thống figure, table, code và callout

### Figure

Đánh số theo lesson để link ổn định:

```markdown
![Luồng publish partition sau reconciliation](materials/lesson-243-readiness-flow.svg)

*Hình L243-1. Consumer chỉ đọc partition sau khi ba điều kiện readiness cùng đạt.*
```

Quy tắc:

- Caption nói figure chứng minh điều gì, không chỉ gọi tên hình.
- Figure phải được viện dẫn trong văn xuôi trước hoặc ngay sau nó.
- Một figure chỉ có một thông điệp chính.
- Sơ đồ kiến trúc có boundary, direction, state owner và failure point.
- Alt text mô tả quan hệ, không mô tả màu sắc.
- Hình từ nguồn ngoài phải có source/locator và quyền sử dụng.

### Table

Chỉ dùng bảng cho dữ liệu có schema lặp:

- lựa chọn × tiêu chí;
- state transition;
- failure × signal × test × recovery;
- input × expected output;
- rubric.

Không dùng bảng để nhét các đoạn văn dài vào ô.

### Code

Mỗi code block cần bốn phần:

1. Mục đích.
2. Input hoặc state ban đầu.
3. Code tối thiểu chạy được.
4. Expected check hoặc output.

````markdown
Đoạn dưới chứng minh retry cùng `event_id` không tạo thêm dòng.

```sql
insert into target(event_id, amount)
values ('evt-42', 120000)
on conflict (event_id) do nothing;
```

Chạy hai lần. Phép kiểm đạt khi:

```sql
select count(*) from target where event_id = 'evt-42';
-- expected: 1
```
````

Không dùng code dài làm bằng chứng về độ sâu. Code dài chuyển vào `materials/`, note chỉ giữ đoạn
đang được phân tích và link tới artefact đầy đủ.

### Callout

Chỉ có bốn loại, viết bằng nhãn chữ để web/PDF không phụ thuộc màu:

```markdown
> **NOTE** — Chi tiết hữu ích nhưng không nằm trên critical path.

> **WARNING** — Failure có thể làm sai dữ liệu, mất dữ liệu hoặc tạo rủi ro vận hành.

> **DEEP DIVE** — Cơ chế bên dưới cần cho bài hiện tại hoặc bài sau.

> **SCOPE** — Phần bị loại khỏi bài và nơi sẽ học tiếp.
```

Không dùng callout cho câu “hay”, takeaway hoặc lời động viên.

### Cross-reference

- Dùng `lesson N` khi dependency là một bài cụ thể.
- Dùng tên khái niệm kèm lesson ở lần đầu: `idempotency (lesson 157)`.
- Không viết “như đã nói ở trên” nếu có thể trỏ section hoặc figure.
- Cross-reference phải giải thích thứ được tái sử dụng, không chỉ nêu số bài.

---

## 6. Traceability và citation

Giáo trình khoa học cần nguồn, nhưng citation không được phá nhịp đọc.

### Trong thân bài

Dùng marker ngắn:

```markdown
Kafka giữ thứ tự trong phạm vi một partition, không phải toàn topic [S1, ch. 4, pp. 21–22].
```

### Cuối bài

```markdown
## Nguồn và phạm vi sử dụng

| ID | Nguồn | Phạm vi đã dùng | Phục vụ phần | Trạng thái |
|---|---|---|---|---|
| S1 | Ben Stopford, *Designing Event-Driven Systems*, 2018 | ch. 4, pp. 17–25 | Broker/log/ordering | Đã đối chiếu PDF |
| S2 | Kafka documentation 4.1 | Transactions | Mechanism | Đã đối chiếu docs |
```

### Bốn trạng thái claim

- `Nguồn`: nguồn nói trực tiếp.
- `Tổng hợp`: nối từ ít nhất hai nguồn.
- `Suy luận`: tác giả suy ra; cần ghi assumption.
- `Mô phỏng`: case/dataset được dựng để dạy.

Không cần gắn nhãn vào mọi câu. Chỉ ghi khi người đọc có thể hiểu nhầm suy luận là fact của nguồn.

### Quy tắc freshness

- Concept ổn định: ghi edition/năm.
- Tool/API: ghi version và ngày kiểm.
- Market/company: ghi năm, sample và nguồn.
- Benchmark: ghi hardware, software, input và method.

---

## 7. C3 trong format giáo trình

C3 không xuất hiện như mười bảng xen giữa prose. Nó được gắn vào ba điểm.

### Đầu bài — learning contract

```markdown
## Kết quả cần đạt

| Năng lực | Bằng chứng | Ngưỡng | Ràng buộc |
|---|---|---|---|
| Chọn snapshot, incremental pull hoặc CDC | Decision record cho ba nguồn | 3/3 lựa chọn có evidence; nêu điểm đảo | Không mặc định chọn tool đang quen |
```

### Giữa bài — checkpoint tại điểm khó

Checkpoint nằm ngay sau mechanism hoặc decision cần kiểm, nhưng chỉ chiếm 3–8 dòng:

```markdown
**Checkpoint.** Offset đã commit nhưng sink chưa ghi xong. Sau restart, hệ có thể mất hay trùng?
Vẽ timeline bốn bước trước khi đọc tiếp.
```

Đáp án đầy đủ đặt cuối mục hoặc trong `<details>` nếu web hỗ trợ; không phá reasoning bằng cách
hiện đáp án ngay cạnh câu hỏi.

### Cuối bài — evidence và transfer

```markdown
## Kiểm tra cuối bài

### Diagnose

Đọc log và manifest của một lần nạp hỏng. Xác định failure boundary và bằng chứng bác hai giả
thuyết còn lại.

### Changed constraint

Nguồn cấm query replica và giảm rate limit còn một nửa. Sửa decision record; nêu phần giữ nguyên,
phần đổi và cost mới.

### Cách chấm

| Tiêu chí | Đạt | Critical failure |
|---|---|---|
| Failure boundary | Dẫn được timeline + evidence | Kết luận từ một log line |
| Source protection | Có rate/retry budget | Retry không giới hạn |
```

---

## 8. Profile theo dạng bài

Không ép mọi bài thành chương LT.

### LT · Concept chapter

Mạch chính:

```text
tension → model → mechanism → worked system → alternatives → limits → transfer
```

- Prose và figure là trục chính.
- 1 case xuyên suốt.
- 1–2 deep dive boxes.
- Practice chiếm khoảng 25–35% thời gian lớp.

### TH · Lab chapter

Mạch chính:

```text
observable goal → environment → minimal mechanism → worked trace → lab → failure injection → verify
```

Body theo kiểu manual khoa học:

- setup tái tạo được;
- hypothesis trước command;
- expected observation sau command;
- checkpoint state;
- clean-up/recovery;
- independent variant.

Không chụp thao tác UI thành chuỗi ảnh nếu command/config có thể mô tả tái lập hơn.

### DA · Design/project brief

Mạch chính:

```text
context → decision → constraints → evidence → milestones → design review → defence
```

- Chapter body giải thích domain và trade-off, không đưa lời giải hoàn chỉnh.
- Practice là project work.
- Assessment dùng artefact, decision record và changed-constraint defence.
- Source code đẹp nhưng không bảo vệ được quyết định thì chưa đạt.

### KT · Assessment specification

Không viết như chương sách. Dùng profile riêng:

```text
scope → environment → task → deliverables → rubric → critical failures → remediation
```

- Không có nội dung mới.
- Bản công khai không chứa answer key.
- Answer key/rubric chi tiết để file riêng không được parser đưa lên web.
- Time budget phải cộng đúng `thoi_luong_phut`.

---

## 9. Template chuẩn

```markdown
---
chuong_trinh: <giữ nguyên>
module: <giữ nguyên>
lesson: <giữ nguyên>
tieu_de: <giữ nguyên>
dang_bai: <giữ nguyên>
thoi_luong_phut: <giữ nguyên>
trang_thai: <state>
---

# Lesson <N> — <Title>

## Đặc tả từ roadmap

<!-- Sinh từ roadmap; không biên tập tại đây. -->

---

## Kết quả cần đạt

| Năng lực | Bằng chứng | Ngưỡng | Ràng buộc |
|---|---|---|---|
| | | | |

## Trước khi bắt đầu

**Cần biết:**  
**Cần có:**  
**Kiểm tra nhanh:**  
**Không nằm trong bài:**

<!-- ĐOẠN MỞ CHƯƠNG: 2–5 đoạn, không heading “Giới thiệu”. -->

## <Heading theo nội dung 1>

<!-- Problem/model. -->

## <Heading theo nội dung 2>

<!-- Mechanism + worked trace. -->

> **DEEP DIVE** — <chỉ dùng khi cơ chế này cần để dự đoán hành vi>

## <Heading theo nội dung 3>

<!-- Case/hệ thống xuyên suốt. Figure hoặc code nếu cần. -->

## <Heading quyết định/trade-off theo nội dung>

<!-- Hai hoặc nhiều lựa chọn; condition, cost, điểm đảo. -->

## <Heading giới hạn theo nội dung>

<!-- Limits, non-generalizable parts, open question. -->

## Thực hành

### Worked trace

### Guided task

### Independent task

### Changed constraint

## Kiểm tra cuối bài

### Checkpoint

### Diagnose hoặc build

### Transfer

### Cách chấm

## Bài làm sau buổi học

<!-- Retention/transfer; không lặp lab. -->

## Hướng dẫn đứng lớp

**Chuẩn bị:**

| Phút | Hoạt động | Dùng phần | Quan sát | Nếu chưa đạt |
|---:|---|---|---|---|
| | | | | |

## Nguồn và phạm vi sử dụng

| ID | Nguồn | Locator | Phục vụ phần | Trạng thái |
|---|---|---|---|---|
| | | | | |

## Điểm còn mở

<!-- Điều chưa kiểm, assumption, benchmark/source còn thiếu. -->
```

### Template không phải quota

- Không giữ H2 placeholder nếu bài không có nội dung.
- Profile KT thay toàn bộ chapter body bằng assessment specification.
- Với bài foundation ngắn, chapter body có thể chỉ ba H2 nội dung.
- Với deep-dive DE, có thể có bảy H2 nội dung và nhiều figure.
- Không tạo “Deep Dive” chỉ để bài trông sâu.

---

## 10. Mẫu lai — lesson 1

Mẫu dưới đây cho thấy nhịp giáo trình và C3 cùng tồn tại. Nó chưa thay thế lesson 1 hiện tại.

```markdown
## Kết quả cần đạt

| Năng lực | Bằng chứng | Ngưỡng | Ràng buộc |
|---|---|---|---|
| Gán nhiệm vụ cho sáu vai trò dữ liệu | 15 nhiệm vụ, mỗi nhiệm vụ có owner và lý do | Đúng ≥ 12/15 | Không dùng công cụ làm lý do duy nhất |
| Đọc một JD mà không dựa vào title | Bảng yêu cầu và vai trò suy ra | Phân loại đủ công cụ, nghiệp vụ, giao tiếp | JD có URL và ngày truy cập |
| Ghi khoảng trống năng lực | Ma trận 11 module | Mỗi mức từ 2 trở lên có artefact | Exposure không được tính là evidence |

## Trước khi bắt đầu

**Cần biết:** không.  
**Cần có:** ba JD đang mở hoặc snapshot hợp lệ.  
**Kiểm tra nhanh:** với yêu cầu “xây pipeline lấy dữ liệu mỗi giờ”, ghi người chịu trách nhiệm khi
dữ liệu đến muộn.  
**Không nằm trong bài:** SQL, dashboard, pipeline implementation.

Giám đốc kinh doanh gửi một câu: “Doanh thu tháng 10 giảm 12%, tìm hiểu giúp.” Một analyst mở
dashboard, cắt theo vùng và sản phẩm rồi gửi báo cáo vào cuối ngày. Không con số nào trong báo cáo
sai. Báo cáo vẫn chưa cho biết 12% được so với mốc nào, dữ liệu có đủ không và quyết định nào đang
chờ kết quả.

Ba câu hỏi đó phân biệt thao tác phân tích với công việc phân tích. Công cụ chỉ xử lý dữ liệu đã
được chọn; nó không chọn hộ baseline, owner hay hành động sau kết luận.

## Sản phẩm bàn giao xác định vai trò

Trong một đội dữ liệu, title thay đổi theo công ty. Sản phẩm bàn giao và trách nhiệm khi sản phẩm
hỏng ổn định hơn.

| Vai trò | Sản phẩm chính | Failure phải chịu trách nhiệm |
|---|---|---|
| Data Engineer | Pipeline, storage, platform | Dữ liệu mất, muộn hoặc không phục vụ được |
| Analytics Engineer | Model, test, metric contract | Consumer hiểu khác nhau hoặc model phá vỡ |
| Data Analyst | Phân tích và khuyến nghị | Kết luận sai hoặc không hỗ trợ quyết định |
| BI Analyst | Dashboard và semantic model | Chỉ số hiển thị sai, chậm hoặc khó dùng |
| Business Analyst | Requirement và process | Yêu cầu không phản ánh nghiệp vụ |
| Data Scientist | Predictive/optimization model | Chất lượng không giữ ngoài mẫu |

Sáu vai có thể cùng dùng SQL. Vì vậy “công việc này dùng SQL” không đủ để gán owner.

## Từ một yêu cầu đến một quyết định

Một phân tích có thể audit đi qua năm bước:

1. Xác định quyết định và người ra quyết định.
2. Chốt metric, baseline, grain và time window.
3. Kiểm completeness, validity và reconciliation.
4. Phân rã biến động; giữ cả giả thuyết bị bác bỏ.
5. Giao kết luận, giới hạn và hành động.

Trong case doanh thu, bước ba phát hiện chi nhánh Đà Nẵng dừng đồng bộ từ ngày 20. Sau khi bù dữ
liệu và chuẩn hóa theo số ngày, mức giảm còn 4%. Phần giảm tập trung ở khách hàng mới. DE nhận
việc khôi phục luồng đồng bộ; DA định lượng ảnh hưởng và trả lời quyết định marketing. Hai vai dùng
cùng dữ liệu nhưng giao hai sản phẩm khác nhau.

> **SCOPE** — Case này là tình huống mô phỏng. Các con số chỉ minh họa chuỗi kiểm chứng; không
> được dùng làm số liệu thị trường hoặc benchmark.

## Ba ranh giới thường đổi theo tổ chức

### DA và AE

Nếu deliverable là một kết luận dùng một lần, DA có thể giữ owner. Nếu deliverable là định nghĩa
metric được nhiều consumer dùng lại và phải version, ownership nghiêng về AE.

### DA và DE

DE sửa lỗi phát sinh ở đường vận chuyển hoặc storage. DA xử lý logic phân tích và định lượng tác
động của lỗi lên kết luận. Một đội nhỏ có thể để một người làm cả hai, nhưng hai trách nhiệm vẫn
phải được kiểm riêng.

### DA và BA

BA tập trung requirement và process. DA kiểm requirement bằng dữ liệu và chịu trách nhiệm cho
phương pháp phân tích. Ở nơi không có BA, analyst phải làm rõ yêu cầu nhưng không vì thế mà mọi
thay đổi quy trình trở thành quyết định của analyst.

## Khi sơ đồ vai trò không còn đủ

Sơ đồ sáu vai mô tả ownership, không mô tả headcount. Startup có thể có một người kiêm bốn vai;
doanh nghiệp lớn có thể chia một vai thành nhiều nhóm. Phân loại theo title sẽ hỏng trong cả hai
trường hợp.

Khi tổ chức đổi, giữ ba câu hỏi: sản phẩm nào được giao, ai chịu failure và control nào không được
bỏ. Câu trả lời có thể gán một người cho nhiều ô nhưng không được xóa trách nhiệm.

## Thực hành

### Worked trace

Yêu cầu: “Hai dashboard doanh thu ra hai số; tạo một định nghĩa dùng chung và ngăn tái diễn.”

- Sản phẩm: metric contract dùng lại.
- Owner chính: AE.
- Collaborator: DA chốt business meaning; BI kiểm consumer behavior.
- Điểm đảo: nếu chỉ cần giải thích chênh lệch hôm nay, không tạo artefact dùng lại, DA có thể owner.

### Guided task

Phân loại tám nhiệm vụ. Với mỗi nhiệm vụ, ghi owner, collaborator, deliverable và failure owner.
Giảng viên làm mẫu hai nhiệm vụ; học viên hoàn thành sáu nhiệm vụ còn lại.

### Independent task

Nhận một JD đã bỏ title. Suy vai trò từ deliverable, rồi mở title gốc và giải thích chỗ khớp hoặc
lệch. Nộp ba requirement còn mơ hồ cần hỏi nhà tuyển dụng.

### Changed constraint

Công ty chỉ có một người phụ trách dữ liệu. Viết lại ownership map và giữ ít nhất ba control:
source reconciliation, metric definition review và independent validation trước khi công bố.

## Kiểm tra cuối bài

Phân loại 15 nhiệm vụ. Mỗi nhiệm vụ cần owner và một câu lý do. Đạt khi đúng ít nhất 12/15 và lý
do dựa trên deliverable hoặc failure ownership.

Critical failure: dùng title hoặc tool làm bằng chứng duy nhất cho hơn ba nhiệm vụ.

## Bài làm sau buổi học

Thu thập 10 JD đang mở. Lưu URL và ngày truy cập; phân loại yêu cầu; đối chiếu 11 module; ghi ba
khoảng trống năng lực. Mỗi năng lực tự chấm từ 2 trở lên phải dẫn một artefact. Kiểm lại bài phân
loại sau 72 giờ mà không đọc note trước.
```

---

## 11. Chuẩn văn phong

Giữ các rule mạnh của V2, nhưng điều chỉnh để văn xuôi giống giáo trình hơn.

### Giữ

- Mỗi đoạn một luận điểm.
- Claim → mechanism/evidence → consequence.
- Chủ thể cụ thể; động từ trực tiếp.
- Không marketing, không khen công cụ.
- Không “best practice” thiếu context.
- Không claim định lượng thiếu source/method.
- Không câu chuyện giả nếu chi tiết không ảnh hưởng reasoning.
- Bold chỉ cho invariant, decision, warning hoặc threshold.

### Bổ sung cho nhịp giáo trình

- Cho phép đoạn dài 3–6 câu khi đang dẫn causal chain; không bẻ mọi ý thành bullet.
- Cho phép lịch sử ngắn nếu nó giải thích vì sao abstraction hiện tại tồn tại.
- Cho phép analogy khi mapping chính xác và ghi điểm analogy hỏng.
- Ưu tiên transition theo logic: nguyên nhân, đối chiếu, hệ quả. Không dùng gạch ngang thay liên từ.
- Summary cuối chương tối đa một đoạn; không lặp toàn bộ heading.
- Mỗi section phải dẫn tự nhiên sang section sau, không mở lại bối cảnh từ đầu.

### Danh sách cảnh báo AI-like

Lint cảnh báo, reviewer quyết định:

- “Trong thế giới ... ngày nay”
- “không chỉ ... mà còn ...”
- “không phải ... mà là ...”
- “hãy tưởng tượng”
- “cùng khám phá/tìm hiểu”
- “vô cùng quan trọng”
- “chìa khóa”, “xương sống”, “trái tim”
- “toàn diện”, “mạnh mẽ”, “tối ưu” không có comparator
- các đoạn liên tiếp cùng nhịp ba ý
- H2/H3 lặp nguyên xi ở nhiều lesson ngoài nhóm heading cố định

Không dùng AI detector làm acceptance test; detector không chứng minh authorship hoặc chất lượng.

---

## 12. Review gate

### Review khoa học

- Mỗi claim có source, method hoặc nhãn mô phỏng/suy luận.
- Thuật ngữ có boundary; không dùng một từ cho nhiều nghĩa mà không phân biệt.
- Figure/table/code được viện dẫn và có phép kiểm.
- Alternative được so trên cùng tiêu chí.
- Limitations đủ để ngăn suy rộng sai.

### Review deep-dive

- Có causal mechanism, không chỉ definition/features.
- Có state/ordering/ownership hoặc data-generating assumptions tương ứng.
- Có worked trace xuyên suốt.
- Có failure injection và evidence phân biệt giả thuyết.
- Changed constraint làm người học sửa quyết định.

### Review sư phạm

- Outcome ↔ evidence ↔ practice ↔ assessment khớp.
- Independent task dùng input mới.
- Rubric cho phép người thứ hai chấm lại.
- Timeline cộng đúng thời lượng.
- Có remediation cho competency trượt.

### Review văn phong

- Xóa tên lesson đi, heading vẫn nhận ra chủ đề.
- Không có đoạn trôi chảy nhưng thiếu claim mới.
- Không dùng tính từ thay cho measurement.
- Prose không bị xé thành bullet quá mức.
- Không lặp phần đầu ở summary.

---

## 13. Pilot đề xuất

Ba bài DA giữ nguyên để so format với chi phí thấp:

| Profile | Lesson | Lý do |
|---|---|---|
| LT | 1 · What a Data Analyst actually does all day | Có bản cũ để so cấu trúc, giọng và độ dài |
| TH | 36 · Data cleaning in practice | Kiểm lab, evidence, reconciliation và failure table |
| KT | 16 · Gate 1 - Excel assessment | Kiểm profile KT không bị ép thành chương lý thuyết |

### Acceptance criteria

- Hai reviewer nhận ra chapter prose không phải form điền.
- Heading nội dung không lặp máy móc giữa ba bài.
- LT đọc liên tục như một chương sách; TH tái tạo được lab; KT không lộ answer key.
- Mọi objective có evidence và ngưỡng.
- Một giảng viên khác dry-run trong ±10 phút.
- Independent/changed-constraint task kiểm transfer, không lặp worked trace.
- Citation truy được tới locator.
- PDF/web render figure, caption, table, code và callout đúng.
- Không có source text bị sao chép vượt ngưỡng quyền sử dụng.

---

## 14. Những quyết định cần owner chốt

1. Chọn kiến trúc `Textbook spine + C3 evidence frame` làm hướng pilot.
2. Chấp nhận **không cố định heading thân chương**; chỉ cố định các bookend.
3. Chọn citation ngắn `[S1, ch./p.]` hay footnote Markdown.
4. Cho phép bốn callout `NOTE/WARNING/DEEP DIVE/SCOPE`.
5. Xác nhận ba lesson pilot ở §13.
6. Xác nhận answer key KT phải nằm ngoài note công khai.

Sau khi chốt sáu điểm, bước kế tiếp mới là viết ba pilot. Chưa ghi `FORMAT-DA-CHOT.md` trước khi
pilot và dry-run qua acceptance criteria.

---

## 15. Bản ghi task

```yaml
task: academy-design-learning-module
profile: learning
risk_tier: R1-reviewed
phase_reached: design
deliverable: technical-curriculum-chapter-standard-v3-proposal
selected_option: textbook-spine-plus-c3-evidence-frame
reference_inspected:
  title: Designing Event-Driven Systems
  author: Ben Stopford
  edition: first
  year: 2018
  pages_inspected: [iii-vi, 13, 29, 38, 101, 110, 111, 139, 148]
approval:
  owner: kina2711
  status: pending
tests_run:
  - pdf-metadata-and-toc-inspection
  - representative-page-text-extraction
  - representative-page-visual-inspection
  - current-parser-and-build-constraint-review
not_run:
  - LT-TH-KT-pilot
  - instructor-dry-run
  - learner-transfer-test
  - v3-web-and-pdf-render
next_task: owner-approves-six-design-decisions-then-build-three-pilots
```
