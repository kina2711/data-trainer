# ĐỀ XUẤT FORMAT NOTE V2

Trạng thái: **BẢN ĐỀ XUẤT — CHƯA PHẢI BASELINE**  
Ngày: 2026-09-25  
Phạm vi: `note.md` cho 525 bài Data Analyst và Data Engineer  
Hướng đã chọn: Phương án C — một mạch bằng chứng, hai chế độ sử dụng

---

## 1. Cách hiểu “FAANG Style” trong tài liệu này

“FAANG Style” không phải một chuẩn xuất bản chính thức. Trong đề xuất này, cụm đó chỉ cách viết
tài liệu kỹ thuật nội bộ thường thấy ở đội engineering lớn:

- Nêu vấn đề và ràng buộc trước khi giới thiệu công cụ.
- Phân biệt dữ kiện, giả định, quyết định và ý kiến.
- Giải thích cơ chế đủ sâu để dự đoán hành vi khi điều kiện đổi.
- Mọi khuyến nghị đều có điều kiện áp dụng và trade-off.
- Ví dụ chạy được hoặc ghi rõ là dữ liệu mô phỏng.
- Failure mode, quan sát và cách phục hồi là nội dung chính, không phải phụ lục.
- Người khác có thể review, tái hiện và phản biện kết luận.
- Viết ngắn hơn khi có thể; không dùng văn phong để che thiếu bằng chứng.

Tên dùng trong baseline nên là **Engineering Curriculum Note Standard**, không ghi “FAANG” lên
từng bài. Nhãn thương hiệu không làm nội dung tốt hơn và nhanh lỗi thời.

---

## 2. Quyết định thiết kế

### Ba biến thể đã cân nhắc trong hướng C

| Biến thể | Trọng tâm | Điểm yếu |
|---|---|---|
| C1 · RFC-first | Context, proposal, alternatives, decision | Tốt cho design review, cứng với bài nền tảng và DA |
| C2 · Incident-first | Triệu chứng, điều tra, cơ chế, khắc phục | Rất mạnh cho vận hành, gượng với thống kê và nghề nghiệp |
| C3 · Evidence-led field guide | Deliverable, mental model, mechanism, decision, practice, failure | Bao quát nhất; cần template và lint chặt |

**Chọn C3.** Nó giữ kỷ luật của engineering document nhưng không ép 525 bài thành RFC hoặc
postmortem. C1 và C2 trở thành profile dùng cho bài phù hợp, không phải format toàn corpus.

### Câu quyết định

Mỗi note là một field guide có thể dùng để tự học và đứng lớp. Mạch duy nhất đi từ deliverable
đến evidence; phần dành riêng cho giảng viên chỉ chứa cách vận hành mạch đó, không có nội dung
kiến thức riêng.

---

## 3. Kiến trúc note chuẩn

Phần `frontmatter` và `Đặc tả từ roadmap` giữ nguyên vì là hợp đồng máy đọc. Phần giáo trình dùng
mười mục dưới đây.

| Mục | Tên chuẩn | Câu hỏi phải trả lời | Sản phẩm bắt buộc |
|---:|---|---|---|
| 1 | Kết quả cần giao | Học xong phải tạo hoặc làm được gì? | Evidence, ngưỡng, constraint |
| 2 | Tình huống | Vấn đề cụ thể nào khiến kiến thức này cần thiết? | Input, symptom, stakes |
| 3 | Mô hình | Cách đơn giản nhất để nghĩ đúng về vấn đề là gì? | Sơ đồ/quan hệ/bất biến |
| 4 | Cơ chế | Hệ thống hoặc phương pháp thực sự vận hành thế nào? | Causal chain, worked trace |
| 5 | Quyết định | Chọn phương án nào dưới điều kiện nào? | Decision table, trade-off |
| 6 | Thực hành | Người học luyện từ có hướng dẫn tới độc lập ra sao? | Guided + independent task |
| 7 | Lỗi và chẩn đoán | Sai ở đâu, thấy tín hiệu gì, kiểm và phục hồi thế nào? | Failure table, negative test |
| 8 | Kiểm tra | Bằng chứng nào xác nhận đạt trên tình huống mới? | Formative, transfer, rubric |
| 9 | Ghi chú đứng lớp | Buổi 120 phút vận hành thế nào? | Timeline, checkpoint, remediation |
| 10 | Sau buổi học | Cần làm gì để giữ và chuyển giao năng lực? | Assignment, retention, sources |

### Vì sao bỏ tên chín mục cũ

Tên cũ như “Cơ sở lý thuyết và cơ chế vận hành”, “Khung quyết định và tiêu chí lựa chọn”, “Giới
hạn và ngộ nhận phổ biến” đúng nghĩa nhưng dài, mang giọng tài liệu do mẫu sinh ra và khiến 525
bài có nhịp giống hệt nhau. Tên mới ngắn, cụ thể và để H3 mang ngữ nghĩa của từng bài.

### Quy tắc heading

- H2 là mười tên chuẩn trên; không sáng tác lại mỗi bài.
- H3 phải nói đúng nội dung, không nói loại nội dung.
- Dùng sentence case; giữ đúng casing của SQL, API, Power BI, PostgreSQL.
- Không đánh số H3 nếu không có tham chiếu chéo thật.
- Một heading tối đa 12 từ, ưu tiên danh từ cụ thể hoặc câu hỏi kỹ thuật.

**Không dùng:**

- “Tại sao X lại quan trọng?”
- “Bức tranh toàn cảnh”
- “Đi sâu vào X”
- “Hành trình từ X đến Y”
- “Chìa khóa để làm chủ X”
- “Những điều cần biết”
- “Tương lai của X”
- “Kết luận” nếu chỉ lặp lại phần trước

**Dùng:**

- “Một dòng đại diện cho điều gì?”
- “`NULL` đi qua phép so sánh thế nào?”
- “Khi hash join tràn khỏi bộ nhớ”
- “Chọn snapshot hay CDC”
- “Ba tín hiệu cho thấy dashboard đang đếm trùng”

---

## 4. Format chi tiết từng mục

## 1. Kết quả cần giao

Mục này thay “Mục tiêu và chuẩn đầu ra”. Nó bắt đầu bằng artefact hoặc hành vi, không bắt đầu bằng
“sau bài này bạn sẽ hiểu”.

```markdown
## 1. Kết quả cần giao

| Việc phải làm | Bằng chứng | Ngưỡng đạt | Ràng buộc |
|---|---|---|---|
| ... | ... | ... | ... |

**Bài này chưa bao gồm:** ...
```

Quy tắc:

- Mỗi dòng tương ứng một phần của Outcome/Done-when trong roadmap.
- Evidence là sản phẩm quan sát được: query, bảng quyết định, báo cáo, chương trình, chẩn đoán.
- Ngưỡng phải chấm lại được bởi người thứ hai.
- “Bài này chưa bao gồm” chặn scope creep và kỳ vọng sai.
- Không liệt kê sáu objective nhỏ chỉ để bảng trông đầy.

## 2. Tình huống

Mục này mở bằng input cụ thể, không mở bằng định nghĩa hoặc câu dẫn “Trong thế giới dữ liệu...”.

```markdown
## 2. Tình huống

Pipeline báo xanh lúc 08:00. Dashboard 09:00 vẫn thiếu phân vùng hôm qua.

Thông tin ban đầu:

- scheduler đánh dấu task thành công;
- bảng đích có partition mới;
- row count thấp hơn nguồn 18%;
- không có exception trong log.

Yêu cầu: xác định pipeline có đạt cam kết hay không và bằng chứng cần thu tiếp.
```

Phải có:

- Input hoặc trạng thái ban đầu.
- Tín hiệu quan sát được.
- Hậu quả nếu xử lý sai.
- Một câu hỏi mà bài sẽ trả lời.

Không dùng câu chuyện giả có nhân vật, hội thoại và cảm xúc nếu những chi tiết đó không ảnh hưởng
quyết định. Nếu case là mô phỏng, ghi `Tình huống mô phỏng`.

## 3. Mô hình

Đưa ra representation nhỏ nhất giúp người học suy luận. Đây không phải mục từ điển thuật ngữ.

```markdown
## 3. Mô hình

Một dataset chỉ “sẵn sàng” khi cả ba điều kiện cùng đúng:

`đã đến đủ → đã kiểm đúng → đã công bố cho consumer`

Task thành công chỉ chứng minh code đã kết thúc. Nó không chứng minh ba điều kiện trên.
```

Mỗi mô hình cần:

- Thành phần.
- Quan hệ hoặc bất biến.
- Phạm vi dùng được.
- Một trường hợp mô hình không đủ.

## 4. Cơ chế

Đây là phần sâu nhất. Viết theo causal chain, không liệt kê tính năng.

```markdown
## 4. Cơ chế

### Commit xảy ra trước publication

1. Worker ghi dữ liệu vào staging.
2. Transaction commit.
3. Bộ kiểm completeness đọc manifest.
4. Publisher đổi trạng thái partition thành `ready`.
5. Consumer chỉ đọc partition ở trạng thái `ready`.

Nếu bước 2 xong nhưng bước 3 thất bại, dữ liệu tồn tại nhưng chưa được phục vụ. Scheduler vẫn có
thể báo task thành công nếu success condition chỉ là exit code của worker.
```

Quy tắc:

- Cơ chế trước API/cú pháp.
- Dẫn một input qua từng bước tới output.
- Nêu state transition, ordering, ownership và nơi có thể mất thông tin.
- Với code: giải thích invariant và failure behavior, không diễn giải từng dòng hiển nhiên.
- Với thống kê: nêu data-generating assumptions và estimator behavior.
- Với DA: nêu grain, denominator, time window và decision consequence.

## 5. Quyết định

Không viết “best practice” thiếu điều kiện. Mỗi lựa chọn có trigger và cost.

```markdown
## 5. Quyết định

| Điều kiện | Chọn | Vì sao | Chi phí chấp nhận |
|---|---|---|---|
| Nguồn nhỏ, có cửa sổ yên | Snapshot | Dễ đối soát toàn phần | Đọc lại nhiều dữ liệu |
| Nguồn lớn, cần độ trễ thấp | CDC | Chỉ chuyển phần thay đổi | Vận hành offset và schema evolution |
| API không có cursor ổn định | Window + overlap | Chịu được retry và late arrival | Cần dedup theo business key |

**Điểm đảo quyết định:** nếu nguồn cấm quét toàn bảng trong giờ làm việc, snapshot không còn là
phương án hợp lệ dù đơn giản hơn.
```

Mục này phải có ít nhất một điều kiện làm lựa chọn đảo chiều. Nếu không có, tác giả đang viết sở
thích chứ chưa viết quyết định.

## 6. Thực hành

Một mạch practice chuẩn:

1. **Worked trace:** xem một ca được giải, thấy reasoning và phép kiểm.
2. **Guided task:** tự hoàn thành phần còn lại với checkpoint.
3. **Independent task:** input mới, không có template lời giải.
4. **Changed constraint:** thay một giả định và buộc sửa quyết định.

```markdown
## 6. Thực hành

### Trace một lần nạp thiếu dữ liệu

Input gồm log scheduler, manifest nguồn và partition đích. Đọc theo thứ tự:

1. Xác nhận window cần nạp.
2. So manifest với row count theo business key.
3. Tách lỗi arrival khỏi lỗi transform.
4. Chỉ công bố partition khi reconciliation qua.

### Tự xử lý ca mới

Nguồn trả 206 Partial Content và cursor hết hạn sau 30 phút. Thiết kế retry sao cho không mất và
không nhân đôi bản ghi. Nộp state machine, idempotency key và ba negative tests.
```

Không dùng cụm “hãy thử”, “cùng thực hành” hoặc “bây giờ đến lượt bạn”. Ghi thẳng input, nhiệm vụ,
constraint và output.

## 7. Lỗi và chẩn đoán

Mục này dùng bảng vận hành, không viết danh sách “lỗi thường gặp” chung chung.

```markdown
## 7. Lỗi và chẩn đoán

| Hiện tượng | Giả thuyết | Bằng chứng phân biệt | Phép kiểm hồi quy | Phục hồi |
|---|---|---|---|---|
| Task xanh, row count thiếu | Cursor hết hạn | Log API có 410; manifest dừng giữa window | Fixture cursor expiry | Nạp lại từ checkpoint trước |
| Dòng tăng sau retry | Sink không idempotent | Trùng business key cùng run id | Retry cùng payload ba lần | Dedup rồi replay |
```

Yêu cầu:

- Tách symptom khỏi root cause.
- Có evidence phân biệt hai giả thuyết gần nhau.
- Có negative/regression test.
- Có recovery hoặc ghi rõ không phục hồi tự động được.
- Không gọi một tính chất là “cạm bẫy” nếu chưa chỉ ra cách phát hiện.

## 8. Kiểm tra

Ba tầng bắt buộc:

- **Recall có chọn lọc:** chỉ kiểm thuật ngữ/bất biến thật sự phải nhớ.
- **Apply/diagnose:** xử lý input chưa gặp.
- **Transfer:** điều kiện đổi, phải điều chỉnh cách làm.

```markdown
## 8. Kiểm tra

### Checkpoint

Cho ba run có cùng exit code 0 nhưng khác manifest. Chọn run được phép publish và nêu hai bằng
chứng. Đạt khi chọn đúng 3/3 và không dùng exit code làm bằng chứng duy nhất.

### Transfer

Nguồn chuyển từ daily snapshot sang event stream. Chỉ ra phần nào của reconciliation giữ nguyên,
phần nào phải đổi, và phép kiểm nào mới trở thành bắt buộc.

### Cách chấm

| Tiêu chí | Đạt | Chưa đạt |
|---|---|---|
| Phân biệt completion và readiness | Dùng manifest + consumer condition | Chỉ nhìn scheduler |
| Recovery | Có checkpoint và replay boundary | Chạy lại toàn bộ không điều kiện |
```

Không dùng quiz nhận diện để chứng minh objective ở tầng áp dụng, phân tích, đánh giá hoặc sáng tạo.

## 9. Ghi chú đứng lớp

Phần này chỉ trỏ tới nội dung đã có. Không viết thêm lý thuyết.

```markdown
## 9. Ghi chú đứng lớp

| Phút | Hoạt động | Dùng phần | Quan sát | Nếu chưa đạt |
|---:|---|---|---|---|
| 0–8 | Diagnostic | §2 | Phân biệt task success với data ready | Giữ hai câu trả lời sai để chữa ở §3 |
| 8–28 | Mô hình + trace | §3–4 | Nói được ba state | Chạy lại trace với timeline |
| 28–50 | Decision table | §5 | Chỉ ra điểm đảo | Thêm constraint source load |
| 50–85 | Guided practice | §6 | Có reconciliation evidence | Cấp manifest mẫu |
| 85–108 | Independent task | §6 | State machine + tests | Giảm còn một failure |
| 108–120 | Transfer check | §8 | Sửa quyết định khi source đổi | Giao remediation |
```

Phải ghi:

- Vật liệu cần chuẩn bị.
- Checkpoint và dấu hiệu quan sát.
- Nhánh remediation.
- Phần có thể cắt nếu thiếu thời gian; independent practice không được là phần cắt mặc định.

## 10. Sau buổi học

Mục cuối không viết kết luận sáo rỗng. Nó chứa công việc sau lớp và provenance.

```markdown
## 10. Sau buổi học

### Bài làm

Thiết kế readiness contract cho một nguồn khác. Nộp state machine, ba failure modes, năm tests và
một replay procedure. Chạy lại sau 72 giờ không nhìn note; ghi chỗ phải tra cứu.

### Nguồn dùng trong bài

| Claim/mục | Nguồn | Locator | Trạng thái |
|---|---|---|---|
| Commit protocol | ... | Chương 4, tr. 81–93 | Đã đối chiếu |
| Cursor expiry case | Fixture nội bộ | `tests/cursor_expiry.json` | Dữ liệu mô phỏng |

### Giới hạn còn mở

- Chưa kiểm hành vi của connector X ở phiên bản Y.
- Không suy rộng benchmark lab sang production.
```

Retention task phải kiểm lại sau một khoảng thời gian hoặc trên context mới; làm lại ngay cùng
input chỉ đo trí nhớ ngắn hạn.

---

## 5. Profile theo dạng bài

Format giữ mười H2, nhưng trọng lượng khác nhau.

### LT

| Mục nặng | Mục nhẹ |
|---|---|
| 3 Mô hình · 4 Cơ chế · 5 Quyết định | 6 Thực hành vừa · 7 Lỗi vừa |

- Ít nhất một causal trace.
- Ít nhất một phản ví dụ phá intuition.
- Independent task buộc giải thích, không chỉ tính toán hoặc nhớ lại.

### TH

| Mục nặng | Mục nhẹ |
|---|---|
| 6 Thực hành · 7 Lỗi và chẩn đoán · 8 Kiểm tra | 3–4 chỉ đủ để thao tác đúng |

- Setup phải tái tạo được.
- Mọi lệnh có expected output hoặc phép kiểm.
- Có clean-up/recovery khi lab thay đổi state.
- Không biến note thành transcript thao tác giao diện.

### DA

| Mục nặng | Mục nhẹ |
|---|---|
| 1 Deliverable · 2 Tình huống · 5 Quyết định · 8 Rubric | 3–4 chỉ chứa kiến thức cần dùng |

- Nêu stakeholder, decision, constraint và non-goal.
- Có milestone và review protocol.
- Không cung cấp thiết kế hoàn chỉnh trước khi học viên làm.
- Defense phải có changed-constraint question.

### KT

| Mục nặng | Mục bỏ hoặc rút |
|---|---|
| 1 Evidence · 2 Bối cảnh · 6 Đề · 8 Rubric · 9 Vận hành | 3–5 chỉ ghi luật/tài nguyên; không dạy mới |

- Tách bản học viên và answer key nếu web có quyền truy cập chung.
- Critical failure ghi trước khi thi.
- Time budget cộng đúng 120/150/180 phút.
- Remediation kiểm đúng competency trượt, không bắt thi lại toàn bộ theo mặc định.

---

## 6. Chuẩn giọng văn chống “AI-like”

Mục tiêu không phải đánh lừa detector. Mục tiêu là văn bản có tác giả chịu trách nhiệm, có bằng
chứng và có judgment cụ thể.

### 6.1. Cấm dùng như thói quen

| Mẫu | Vấn đề | Cách sửa |
|---|---|---|
| “Trong thế giới dữ liệu ngày nay...” | Mở đầu không chứa thông tin | Mở bằng input hoặc failure cụ thể |
| “X đóng vai trò vô cùng quan trọng” | Tính từ thay bằng chứng | Nêu quyết định/lỗi phụ thuộc X |
| “Không chỉ X mà còn Y” | Nhịp đối xứng lạm dụng | Viết hai claim riêng hoặc bỏ claim yếu |
| “X không phải A mà là B” | Tạo tương phản giả | Nêu định nghĩa và boundary trực tiếp |
| “Hãy tưởng tượng...” | Dựng sân khấu thừa | Đưa case, số và constraint |
| “Cùng khám phá...” | Giọng marketing/courseware | Bắt đầu nội dung |
| “Chìa khóa”, “xương sống”, “trái tim” | Ẩn cơ chế bằng ẩn dụ | Gọi đúng invariant/component |
| “toàn diện”, “mạnh mẽ”, “tối ưu” | Không có baseline | Nêu metric và comparator |
| “rõ ràng”, “hiển nhiên” | Che bước suy luận | Viết bước suy luận hoặc bỏ |
| “best practice” | Thiếu context | Nêu condition, cost và alternative |
| “Kết luận: X rất quan trọng” | Lặp mà không thêm evidence | Kết bằng decision/assignment/open limit |

Không cấm tuyệt đối một cấu trúc khi logic thật sự cần nó. Lint đánh dấu để review, không tự động
xóa câu đúng.

### 6.2. Quy tắc câu và đoạn

- Một đoạn mang một luận điểm chính.
- Câu đầu nêu claim; câu sau giải thích mechanism/evidence; câu cuối chỉ dùng khi có consequence.
- Thay đổi độ dài câu tự nhiên; không ép mọi đoạn thành ba câu cân đối.
- Không tạo danh sách ba ý chỉ vì nhịp văn. Số mục do nội dung quyết định.
- Dùng chủ thể cụ thể: scheduler, consumer, analyst, transaction. Hạn chế “chúng ta”, “người ta”.
- Dùng động từ trực tiếp: đo, ghi, từ chối, retry, đối soát. Hạn chế danh từ hóa.
- Không viết lời khen cho khái niệm hoặc công cụ.
- Không nhân cách hóa hệ thống nếu làm mờ state transition.
- Giữ thuật ngữ tiếng Anh khi bản dịch làm mất nghĩa; giải thích lần đầu, dùng nhất quán sau đó.
- Dấu gạch ngang dùng cho quan hệ thật, không dùng thay mọi liên từ.

### 6.3. Quy tắc nhấn mạnh

- Bold chỉ cho invariant, decision, critical failure hoặc số ngưỡng.
- Không bold cả câu chỉ vì câu đó “hay”.
- Mỗi 500 từ tối đa khoảng 3–5 cụm bold, trừ bảng/rubric.
- Không dùng emoji, icon trang trí, ALL CAPS hoặc nhiều dấu chấm than.
- Blockquote chỉ cho requirement, input, trích dẫn ngắn hoặc cảnh báo; không dùng làm khẩu hiệu.

### 6.4. Quy tắc tính trung thực

- Claim thị trường: nguồn, năm, mẫu và giới hạn.
- Benchmark: phần cứng, phiên bản, input, method; nếu thiếu thì gọi là minh họa.
- Case không có hồ sơ thật: ghi `Tình huống mô phỏng`.
- Output code chưa chạy: ghi `Kết quả kỳ vọng`, không ghi “kết quả”.
- Suy luận của tác giả: ghi rõ là suy luận; không gắn nhầm cho nguồn.
- Nguồn mâu thuẫn: giữ cả hai và nêu version/context.
- Không biết: ghi điều chưa kiểm và cách kiểm.

---

## 7. Quy tắc đặt tiêu đề theo nội dung

Top-level H2 cố định để corpus dễ tra cứu. H3/H4 phải mang giọng của bài.

### Ví dụ DA

| Chung chung | Dùng |
|---|---|
| Tổng quan về grain | Một dòng trong bảng này đại diện cho gì? |
| Tầm quan trọng của denominator | Mẫu số đổi, metric đổi nghĩa |
| Các lỗi phổ biến khi JOIN | Vì sao doanh thu tăng gấp ba sau JOIN |
| Best practices cho dashboard | Khi nào dashboard cần từ chối hiển thị |

### Ví dụ DE

| Chung chung | Dùng |
|---|---|
| Tìm hiểu về retry | Retry nhân tải như thế nào |
| Các khái niệm CDC | Offset, checkpoint và vị trí log khác nhau ở đâu |
| Tổng quan partitioning | Hot key làm một worker giữ hết việc |
| Kubernetes nâng cao | Pod restart nhưng backlog không giảm |

### Công thức H3 tốt

- `Hiện tượng + nguyên nhân`: “Dòng tăng sau retry vì sink không idempotent”.
- `Câu hỏi quyết định`: “Khi nào snapshot rẻ hơn CDC?”.
- `Boundary`: “Task hoàn tất, dữ liệu chưa sẵn sàng”.
- `Mechanism`: “Barrier tạo snapshot nhất quán”.
- `Failure signal`: “Lag tăng dù throughput không đổi”.

---

## 8. Template `note.md` đề xuất

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

<!-- Sinh tự động; phải khớp roadmap từng chữ. -->

---

## 1. Kết quả cần giao

| Việc phải làm | Bằng chứng | Ngưỡng đạt | Ràng buộc |
|---|---|---|---|
| | | | |

**Bài này chưa bao gồm:**

## 2. Tình huống

<!-- Input · tín hiệu · hậu quả · câu hỏi. Ghi rõ nếu mô phỏng. -->

## 3. Mô hình

<!-- Thành phần · quan hệ/bất biến · phạm vi · giới hạn. -->

## 4. Cơ chế

<!-- Causal chain hoặc worked trace. Cơ chế trước cú pháp. -->

## 5. Quyết định

| Điều kiện | Chọn | Vì sao | Chi phí chấp nhận | Điểm đảo |
|---|---|---|---|---|
| | | | | |

## 6. Thực hành

### Worked trace

### Guided task

### Independent task

### Changed constraint

## 7. Lỗi và chẩn đoán

| Hiện tượng | Giả thuyết | Bằng chứng phân biệt | Phép kiểm | Phục hồi |
|---|---|---|---|---|
| | | | | |

## 8. Kiểm tra

### Checkpoint

### Transfer

### Cách chấm

## 9. Ghi chú đứng lớp

**Chuẩn bị:**

| Phút | Hoạt động | Dùng phần | Quan sát | Nếu chưa đạt |
|---:|---|---|---|---|
| | | | | |

## 10. Sau buổi học

### Bài làm

### Kiểm lại sau 72 giờ

### Nguồn dùng trong bài

| Claim/mục | Nguồn | Locator | Trạng thái |
|---|---|---|---|
| | | | |

### Giới hạn còn mở
```

Template là ceiling, không phải quota. Không được tạo bảng rỗng hoặc heading rỗng cho đẹp. Profile
KT/DA được phép thay các subsection ở §6 và §8 theo rubric/brief nhưng giữ H2 chuẩn.

---

## 9. Mẫu viết lại ngắn — lesson 1

Mẫu này chỉ kiểm heading, giọng văn và mật độ. Nó chưa thay thế lesson 1 hiện tại.

```markdown
## 1. Kết quả cần giao

| Việc phải làm | Bằng chứng | Ngưỡng đạt | Ràng buộc |
|---|---|---|---|
| Gán nhiệm vụ cho sáu vai trò dữ liệu | 15 nhiệm vụ, mỗi nhiệm vụ có owner và lý do | Đúng ≥ 12/15 | Không dùng title làm lý do duy nhất |
| Phân tích yêu cầu trong JD | Bảng từ 10 JD có URL và ngày truy cập | Đủ 10 nguồn; tách công cụ, nghiệp vụ, giao tiếp | JD còn mở hoặc có snapshot |
| Ghi khoảng trống năng lực cá nhân | Ma trận 11 module | Mỗi mức từ 2 trở lên có artefact | Đã học không được tính là đã làm được |

**Bài này chưa bao gồm:** cách viết SQL, dựng dashboard hoặc thiết kế pipeline.

## 2. Tình huống

Giám đốc kinh doanh gửi một câu: “Doanh thu tháng 10 giảm 12%, tìm hiểu giúp.”

Con số chưa có baseline. Báo cáo chưa nói ai sẽ quyết định việc gì. Chi nhánh Đà Nẵng đã ngừng
đồng bộ từ ngày 20 nhưng dashboard không báo lỗi.

Nếu analyst mở công cụ trước khi làm rõ ba điểm đó, phần phân tích phía sau có thể đúng trên một
tập dữ liệu thiếu và trả lời sai câu hỏi kinh doanh.

## 3. Mô hình

Phân loại công việc theo sản phẩm bàn giao và trách nhiệm khi sản phẩm hỏng:

| Vai trò | Sản phẩm chính | Chịu trách nhiệm khi |
|---|---|---|
| Data Engineer | Pipeline và storage | Dữ liệu không đến, đến muộn hoặc mất |
| Analytics Engineer | Model và metric contract | Hai consumer hiểu dữ liệu khác nhau |
| Data Analyst | Kết luận và khuyến nghị | Phân tích không trả lời quyết định hoặc suy luận sai |
| BI Analyst | Dashboard theo dõi lặp lại | Chỉ số hiển thị sai, chậm hoặc khó dùng |
| Business Analyst | Requirement và process | Yêu cầu không phản ánh quy trình nghiệp vụ |
| Data Scientist | Mô hình dự báo/tối ưu | Dự báo không giữ chất lượng ngoài mẫu |

Công cụ không xác định owner. Năm vai trò trên đều có thể viết SQL.

## 4. Cơ chế

### Từ yêu cầu đến quyết định

1. Xác định quyết định đang chờ.
2. Chốt metric, baseline và time window.
3. Kiểm dữ liệu có đủ và nhất quán không.
4. Phân rã thay đổi và bác bỏ giả thuyết.
5. Giao kết luận, giới hạn và hành động.

Trong tình huống trên, bước 3 phát hiện 11 ngày dữ liệu bị thiếu. Sau khi bù dữ liệu và chuẩn hóa
theo số ngày, mức giảm còn 4%. Phần giảm tập trung ở khách hàng mới. Khuyến nghị marketing chỉ có
ý nghĩa sau hai phép hiệu chỉnh đó.

### Ranh giới DA và DE

DE chịu trách nhiệm khôi phục luồng đồng bộ và ngăn lỗi tái diễn. DA chịu trách nhiệm định lượng
ảnh hưởng của phần thiếu lên kết luận hiện tại. Hai deliverable khác nhau, dù cùng dùng bảng giao
dịch làm input.

## 5. Quyết định

| Tín hiệu | Owner chính | Collaborator | Điểm đảo |
|---|---|---|---|
| Dữ liệu chưa đến hoặc SLO vỡ | DE | DA cung cấp impact | Nếu đường ống đúng, lỗi nằm ở định nghĩa |
| Định nghĩa metric lệch giữa consumer | AE | DA/BI | Nếu chỉ là phân tích một lần, DA có thể owner |
| Cần kết luận cho một quyết định | DA | AE/DE tùy nguyên nhân | Nếu cần sản phẩm theo dõi lặp lại, chuyển BI |

## 6. Thực hành

### Guided task

Phân loại tám nhiệm vụ. Với mỗi nhiệm vụ, ghi owner chính, collaborator, sản phẩm bàn giao và một
câu lý do. Giảng viên làm mẫu hai nhiệm vụ; học viên hoàn thành sáu nhiệm vụ còn lại.

### Independent task

Nhận một JD đã bỏ title. Từ phần mô tả công việc, suy ra vai trò, ba năng lực bắt buộc và hai vùng
trách nhiệm còn mơ hồ. Chỉ xem title gốc sau khi nộp.

### Changed constraint

Công ty chỉ có một người phụ trách dữ liệu. Viết lại ranh giới trách nhiệm theo thứ tự ưu tiên và
ghi ba việc không được bỏ dù một người kiêm nhiều vai.

## 7. Lỗi và chẩn đoán

| Hiện tượng | Giả thuyết | Bằng chứng phân biệt | Cách sửa |
|---|---|---|---|
| Gán vai theo công cụ | Nhầm tool với deliverable | Cùng SQL nhưng output khác nhau | Hỏi ai chịu failure |
| Mọi việc đều gán cho DA | Bối cảnh công ty nhỏ bị coi là chuẩn nghề | JD chứa vận hành pipeline/SLO | Tách việc đang kiêm khỏi role chuẩn |
| Tự chấm năng lực cao sau khi học | Nhầm exposure với evidence | Không có artefact hoặc task mới | Hạ trạng thái thành chưa có bằng chứng |

## 8. Kiểm tra

**Exit ticket:** phân loại 15 nhiệm vụ và viết một câu lý do cho mỗi nhiệm vụ. Đạt khi đúng ít
nhất 12 nhiệm vụ; lý do phải dùng sản phẩm bàn giao hoặc failure ownership.

**Transfer:** với một công ty 20 người không có AE/BI, chỉ ra ai đang kiêm việc gì và control nào
cần giữ để các định nghĩa metric không phân kỳ.

## 9. Ghi chú đứng lớp

| Phút | Hoạt động | Quan sát | Nếu chưa đạt |
|---:|---|---|---|
| 0–8 | Chọn việc đầu tiên trong case doanh thu | Có hỏi baseline/decision không | Giữ đáp án sai để chữa sau §3 |
| 8–30 | Mô hình sáu vai | Dùng deliverable thay tool | Thêm ba ca cùng dùng SQL |
| 30–55 | Guided task | Đúng ≥ 6/8 | Chữa theo failure ownership |
| 55–85 | JD không title | Có evidence cho suy luận | Cấp bảng ba loại requirement |
| 85–105 | Changed constraint | Giữ được controls cốt lõi | Giảm còn ba vai |
| 105–120 | Exit ticket và chữa | Đúng ≥ 12/15 | Giao remediation theo nhóm lỗi |

## 10. Sau buổi học

Thu thập 10 JD đang mở, lưu URL và ngày truy cập. Nộp bảng tần suất yêu cầu, ba khoảng trống năng
lực và artefact cần tạo để chứng minh từng năng lực. Kiểm lại bài phân loại sau 72 giờ mà không
đọc note trước.

**Giới hạn:** các tỉ lệ thời gian nghề nghiệp không được dùng trong bài nếu chưa có mẫu khảo sát
và phương pháp thu thập đủ để người khác kiểm tra.
```

---

## 10. Lint và review gate

### Lint tự động đề xuất

Lint chỉ phát hiện tín hiệu, không tự động sửa văn.

1. Đúng mười H2 chuẩn; không có heading rỗng.
2. Mỗi dòng objective có evidence và threshold.
3. Có `Independent task` hoặc lý do profile KT không cần.
4. Có ít nhất một negative test/failure row ở LT/TH/DA.
5. Mọi số, phần trăm, benchmark và tên nguồn có locator hoặc nhãn mô phỏng.
6. Cảnh báo các cụm:
   - `trong thế giới .* ngày nay`
   - `không chỉ .* mà còn`
   - `không phải .* mà là`
   - `hãy tưởng tượng`
   - `cùng (tìm hiểu|khám phá)`
   - `vô cùng quan trọng`
   - `chìa khóa|xương sống|trái tim`
   - `toàn diện|mạnh mẽ|tối ưu`
7. Cảnh báo đoạn có hơn ba cụm bold hoặc ba dấu gạch ngang dài.
8. Cảnh báo H3 chung chung trùng trên quá nhiều bài.
9. Cảnh báo code block không có ngôn ngữ, input hoặc expected check.
10. Đối chiếu timeline mục 9 với `thoi_luong_phut`.

### Review người

Reviewer trả lời tám câu:

1. Bỏ tên bài đi, ví dụ và heading có còn phân biệt được bài này với bài khác không?
2. Có đoạn nào trôi chảy nhưng không thêm mechanism, evidence hoặc decision không?
3. Claim nào đang được che bằng tính từ?
4. Người học có tự làm trên input mới hay chỉ lặp worked example?
5. Failure mode có tín hiệu và phép kiểm hay chỉ có tên?
6. Trade-off có điều kiện đảo quyết định không?
7. Note có đoạn chỉ giảng viên cần nhưng lại đặt trong learner flow không?
8. Một người dạy khác có thể chấm cùng kết quả không?

---

## 11. Acceptance criteria trước khi nhân ra 525 bài

Pilot ba bài: một LT, một TH, một KT.

- Hai reviewer độc lập không đánh dấu quá một đoạn “generic/AI-like” trên mỗi 1.000 từ.
- Mọi heading H3 là content-specific; không có heading mẫu chung ngoài mười H2.
- Mọi objective truy được tới practice và assessment.
- Một người dạy khác chạy dry-run trong ngân sách ±10 phút.
- Người học mới hoàn thành được independent task; không cần đoán yêu cầu còn thiếu.
- Người có kinh nghiệm đọc không thấy phần giải thích cơ chế bị thay bằng khẩu hiệu.
- Note build được PDF và render web đúng.
- Lint không còn lỗi cứng; warning còn lại có disposition ghi rõ.
- Thời gian soạn/review được đo. Nếu vượt quá 1,5 lần format cũ mà không cải thiện transfer hoặc
  khả năng đứng lớp, phải thu gọn template trước khi mở rộng.

---

## 12. Những gì cố ý không đưa vào format

- Persona giả, hội thoại giả và câu chuyện cảm xúc để “tăng hấp dẫn”.
- TL;DR lặp lại toàn bài. Mục 1 đã đóng vai trò contract ngắn.
- Phần “Key takeaways” lặp nội dung. Kết thúc bằng evidence và việc sau lớp.
- Glossary trong mọi bài. Thuật ngữ dùng xuyên module thuộc ref/index cấp module.
- FAQ sinh từ nội dung. Chỉ thêm câu hỏi đã xuất hiện trong pilot hoặc review thật.
- “Best practices” không có context.
- Một quota bắt buộc về số bảng, số bullet, số ví dụ hoặc số từ.
- Claim rằng format này giống tài liệu nội bộ của một công ty cụ thể mà không có nguồn công khai.

---

## 13. Cổng phê duyệt

Owner cần chốt năm điểm:

1. Dùng mười H2 mới hay giữ chín tên cũ.
2. Cho phép bảng decision/failure vắng ở bài không phù hợp nếu tác giả ghi lý do hay bắt buộc mọi bài.
3. Có tách answer key của KT khỏi `note.md` để tránh lộ trên web không.
4. Ngưỡng cảnh báo “AI-like” là advisory hay block merge.
5. Chọn ba lesson cụ thể cho pilot LT/TH/KT.

Sau khi chốt, chưa ghi baseline ngay. Viết và dry-run ba pilot trước; baseline cuối mới được ghi vào
`FORMAT-DA-CHOT.md`.

---

## 14. Bản ghi task

```yaml
task: academy-design-learning-module
profile: learning
risk_tier: R1-reviewed
phase_reached: design
deliverable: engineering-curriculum-note-standard-v2-proposal
selected_option: C3-evidence-led-field-guide
approval:
  owner: kina2711
  status: pending
tests_run:
  - inspected-current-note-and-parser
  - checked-build-toolchain
  - defined-LT-TH-DA-KT-profiles
  - defined-editorial-and-lint-gates
not_run:
  - three-lesson-pilot
  - instructor-dry-run
  - learner-transfer-test
  - pdf-and-web-render-of-v2-template
next_task: approve-design-points-and-name-three-pilot-lessons
```
