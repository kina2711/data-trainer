# ĐỀ XUẤT FORMAT GIÁO TRÌNH VÀ SLIDE

Trạng thái: **BẢN ĐỀ XUẤT — CHỜ OWNER CHỐT**  
Ngày: 2026-09-25  
Phạm vi: format dùng chung cho 525 bài Data Analyst và Data Engineer  
Không thay đổi file nào trong `material/` ở vòng này.

---

## 1. Kết luận khuyến nghị

Chọn **Phương án C — một mạch bằng chứng, hai chế độ sử dụng**.

> Note chỉ có một mạch nội dung: bằng chứng cần nộp → vấn đề → mô hình → ví dụ → thực hành →
> phản hồi → kiểm tra chuyển giao. Người tự học đọc phần chính; người dạy dùng timebox và callout
> ngay trong cùng mạch. Slide là các “điểm chiếu” của mạch đó, không phải một bản tóm tắt độc lập.

Lý do chọn, trong 40 từ: phương án C đáp ứng đồng thời người tự học, người đứng lớp và tiêu chí
đo được; tránh hai bản nội dung lệch nhau, đồng thời vẫn dùng được chín mục La Mã, parser và Marp
hiện có.

Quyết định này **chưa có hiệu lực** cho tới khi owner phê duyệt. Khi phê duyệt, ghi bản chuẩn cuối
cùng vào `FORMAT-DA-CHOT.md`; không dùng chính file đề xuất này làm baseline sản xuất.

---

## 2. Bằng chứng hiện trạng đã đọc

1. `lesson_001` là bài duy nhất đã soạn: 340 dòng, khoảng 4.747 từ, đủ chín mục La Mã. Nội dung
   có chiều sâu nhưng đang đồng thời làm sách đọc, kịch bản lớp và ghi chú giảng viên.
2. 524 note còn lại dùng cùng khung chín mục; bài LT, TH và KT hiện có cùng skeleton.
3. `Web/parse_curriculum.py` bỏ frontmatter, H1 và khối “Đặc tả từ roadmap”, rồi đưa toàn bộ phần
   La Mã còn lại lên web. Vì vậy heading/callout trong thân bài có thể đổi mà không làm hỏng parser.
4. `slides.md` đã có frontmatter Marp; `package.json` khoá `@marp-team/marp-cli` 4.5.0;
   `build_bai.py` sinh cả PPTX và PDF với theme `volt.css`.
5. Theme hiện có hỗ trợ slide mở đầu, slide nhấn mạnh, bảng, code, trích dẫn, header/footer và
   flow table. Không cần đề xuất thêm công cụ slide.
6. Roadmap đã chứa Outcome, Đánh giá, Lab và Done-when. Note không được phát minh một hợp đồng
   học tập thứ hai; nó phải triển khai đúng hợp đồng đó.

---

# PHẦN A — FORMAT GIÁO TRÌNH `note.md`

## 3. Những bất biến áp dụng cho cả ba phương án

### 3.1. Phần máy đọc — không được đổi

- Giữ nguyên bảy khoá frontmatter hiện có.
- Giữ nguyên khối `## Đặc tả từ roadmap`; nội dung khối này phải khớp từng chữ với roadmap.
- Giữ chín heading La Mã để toàn corpus có cùng địa chỉ nội dung.
- Mọi claim bên ngoài phải dẫn tới note ref; note ref dẫn tiếp tới nguồn và locator.
- `quiz.md`, `homework.md`, `slides.md` không được thêm objective mới.

### 3.2. Một đơn vị nội dung tối thiểu

Mỗi khái niệm quan trọng phải có đủ chuỗi sau, có thể ngắn nhưng không được thiếu:

```text
Vấn đề → mô hình/cơ chế → ví dụ đã giải → phản ví dụ/lỗi → việc người học tự làm → bằng chứng đạt
```

Một đoạn chỉ định nghĩa thuật ngữ không phải một đơn vị dạy học hoàn chỉnh.

### 3.3. Quy tắc độ dài

Không đặt quota từ cứng cho mọi bài. Dùng ngân sách theo phút và loại hoạt động:

| Dạng | Nội dung để đọc/dạy | Hoạt động trên lớp | Độ dài note mục tiêu |
|---|---:|---:|---:|
| LT | 45–60 phút | 45–60 phút ví dụ, kiểm tra, thảo luận | 3.000–4.500 từ |
| TH | 20–35 phút | 70–90 phút guided + independent practice | 1.800–3.000 từ, chưa tính code |
| DA | 15–25 phút brief | 80–95 phút làm, review, bảo vệ | 1.500–2.500 từ + rubric |
| KT | 0–15 phút hướng dẫn | phần còn lại làm và chữa | 800–1.800 từ + đề/rubric |

Lesson 1 hiện khoảng 4.747 từ: chấp nhận được ở biên trên cho một LT mở chương trình, nhưng không
nên trở thành quota mặc định cho 525 bài.

---

## 4. Phương án A — Chương sách tham chiếu

### 4.1. Cấu trúc

Chín mục La Mã hoạt động như một chương sách tuyến tính:

1. Mục tiêu.
2. Bối cảnh.
3. Lý thuyết đầy đủ.
4. Bảng quyết định.
5. Case study dài.
6. Ngộ nhận.
7. Ghi chú dạy học tách riêng.
8. Câu hỏi.
9. Bài tập.

Người học đọc từ II tới VI như sách; giảng viên tự biến chương sách thành kế hoạch buổi học.

### 4.2. Tối ưu cho gì

- Đọc lại sau khóa học.
- Tra cứu khái niệm và thuật ngữ.
- Soạn nhanh vì gần với lesson 1 hiện tại.
- PDF A4 đẹp, ít callout vận hành chen vào văn xuôi.

### 4.3. Bắt buộc và tùy chọn

**Bắt buộc:** objective đo được, ít nhất một ví dụ đã giải, một phản ví dụ, một decision aid, câu
hỏi có đáp án, assignment gắn Done-when.

**Tùy chọn:** lịch sử, bảng so sánh dài, case study thứ hai, phần mở rộng.

### 4.4. LT / TH / KT khác nhau thế nào

- LT: mục III dài nhất; V là một worked case.
- TH: III rút còn prerequisite và cơ chế; V biến thành tutorial từng bước.
- KT: II–VI chỉ mô tả bối cảnh, dữ liệu, quy tắc và rubric; không dạy kiến thức mới.

### 4.5. Nó hỏng ở đâu

- Người dạy vẫn phải tự quyết lúc nào dừng, hỏi, demo và cho làm.
- Dễ biến 120 phút thành lecture dài.
- Người viết có xu hướng “phủ đủ kiến thức” thay vì bảo đảm transfer.
- Slide dễ trở thành bản tóm tắt khác cấu trúc và lệch dần khỏi note.

### 4.6. Mẫu thật — lesson 1 theo phương án A

```markdown
## III. Cơ sở lý thuyết và cơ chế vận hành

### 3.1. Giá trị của Data Analyst nằm ở quyết định, không ở biểu đồ

Một yêu cầu như “doanh thu tháng 10 giảm 12%, tìm hiểu giúp” chứa ít nhất ba câu hỏi chưa được
trả lời: 12% so với mốc nào, con số có đáng tin không, và ai sẽ làm gì sau khi nhận kết quả.
Data Analyst tạo giá trị bằng cách biến yêu cầu đó thành một quyết định có bằng chứng.

Chuỗi công việc tối thiểu gồm năm bước:

1. Làm rõ quyết định cần hỗ trợ.
2. Kiểm chứng metric và dữ liệu đầu vào.
3. Phân rã biến động thành các phần có thể giải thích.
4. Loại các giả thuyết không phù hợp với bằng chứng.
5. Trình bày kết luận, giới hạn và hành động đề xuất.

Một dashboard có thể xuất hiện ở bước năm, nhưng dashboard không thay thế bốn bước trước.

### 3.2. Sáu vai trò quanh một câu hỏi dữ liệu

| Vai trò | Câu hỏi chính | Sản phẩm bàn giao |
|---|---|---|
| Data Engineer | Dữ liệu đi tới nơi dùng có đúng và đúng giờ không? | Pipeline, storage, vận hành |
| Analytics Engineer | Định nghĩa và mô hình có nhất quán không? | Model, test, metric contract |
| Data Analyst | Điều gì xảy ra, vì sao, nên làm gì? | Phân tích và khuyến nghị |
| BI Analyst | Chỉ số cần được theo dõi lặp lại thế nào? | Semantic model, dashboard |
| Business Analyst | Quy trình và yêu cầu nghiệp vụ cần thay đổi gì? | Requirement, process |
| Data Scientist | Có thể dự báo hoặc tối ưu quyết định nào? | Model, experiment |

**Phản ví dụ.** “Xây pipeline lấy dữ liệu giao dịch mỗi giờ” không trở thành việc của DA chỉ vì
đầu ra cuối cùng là một dashboard. Sản phẩm bàn giao trực tiếp vẫn là pipeline có SLO vận hành.

## IV. Khung quyết định và tiêu chí lựa chọn

Khi nhận một yêu cầu, hỏi theo thứ tự:

1. Sản phẩm trực tiếp cần bàn giao là hệ thống, mô hình dùng chung, báo cáo lặp lại hay kết luận?
2. Lỗi nếu xảy ra thuộc đường vận chuyển, định nghĩa, cách phân tích hay quy trình nghiệp vụ?
3. Ai có quyền quyết định trade-off cuối cùng?

Nếu sản phẩm là kết luận phục vụ một quyết định và độ đúng được chứng minh bằng phân tích, DA là
owner chính. Nếu sản phẩm là hệ thống phải vận hành liên tục, DA là consumer hoặc collaborator.
```

---

## 5. Phương án B — Runbook đứng lớp theo thời gian

### 5.1. Cấu trúc

Nội dung được tổ chức quanh timeline 120 phút. Chín mục vẫn tồn tại, nhưng từng mục có timebox,
lời dẫn, câu hỏi giảng viên, dấu hiệu quan sát và nhánh xử lý khi lớp không theo kịp.

```text
0–10  Diagnostic hook
10–25 Mental model
25–40 Worked example
40–55 Checkpoint + feedback
55–85 Guided practice
85–105 Independent practice
105–115 Debrief
115–120 Exit ticket
```

### 5.2. Tối ưu cho gì

- Người dạy khác cầm lên có thể vận hành buổi học ngay.
- Kiểm soát 120 phút và nhịp tương tác.
- Dễ quan sát lớp đang mất ở đâu.
- Phù hợp đào tạo instructor-led có facilitator guide rõ.

### 5.3. Bắt buộc và tùy chọn

**Bắt buộc:** timebox, câu lệnh chuyển hoạt động, vật liệu cần chuẩn bị, đáp án/dấu hiệu đạt, nhánh
remediation và một exit ticket.

**Tùy chọn:** lời thoại gợi ý, câu hỏi mở rộng, biến thể cho lớp nhanh/chậm.

### 5.4. LT / TH / KT khác nhau thế nào

- LT: chu kỳ ngắn 10–20 phút giữa giải thích và kiểm tra.
- TH: demo tối đa 15 phút rồi guided practice → independent practice → review.
- KT: setup → làm độc lập → thu bài → chữa bằng evidence; không có mini-lecture cứu bài.

### 5.5. Nó hỏng ở đâu

- Đọc như giáo trình tự học khá vụn vì bị ngắt bởi chỉ dẫn vận hành.
- Timebox cứng giả định quy mô lớp và mức đầu vào giống nhau.
- Lời dẫn dễ trở thành kịch bản sân khấu, khiến người dạy đọc chép.
- Nội dung tra cứu sau khóa học kém hơn phương án A.

### 5.6. Mẫu thật — lesson 1 theo phương án B

```markdown
## II. Bối cảnh và vấn đề đặt ra

### 0–8 phút · Chẩn đoán trước khi dạy

**Chiếu cho lớp:** “Doanh thu tháng 10 giảm 12%. Hãy chọn việc đầu tiên bạn sẽ làm.”

A. Mở Power BI.  
B. Viết SQL lấy doanh thu theo ngày.  
C. Hỏi 12% so với mốc nào và quyết định nào đang chờ.  
D. Kiểm tra chiến dịch marketing tháng 10.

Yêu cầu học viên chọn cá nhân trong 30 giây, rồi giải thích cho người bên cạnh trong 90 giây.
Không công bố đáp án trước khi nghe ít nhất ba lý do.

**Dấu hiệu cần can thiệp:** nếu quá nửa lớp chọn A hoặc B, chưa giới thiệu sáu vai trò. Dùng hai
câu hỏi: “Nếu 12% là sai thì sao?” và “Nếu không ai hành động từ báo cáo thì sao?”

### 8–15 phút · Chốt vấn đề

Đáp án tốt nhất là C. Nó chưa giải quyết yêu cầu, nhưng làm lộ hai bất định có thể khiến toàn bộ
phân tích phía sau vô dụng: baseline và quyết định. Ghi lên bảng chuỗi:

`yêu cầu → quyết định → định nghĩa → dữ liệu → phân tích → hành động`

## III. Cơ sở lý thuyết và cơ chế vận hành

### 15–30 phút · Sáu vai trò, một luồng dữ liệu

Vẽ sáu sản phẩm bàn giao lên bảng: pipeline, model dùng chung, kết luận, dashboard lặp lại,
requirement, predictive model. Học viên ghép vai trò với sản phẩm trong nhóm ba người.

**Checkpoint 1:** đưa tám nhiệm vụ; mỗi nhóm giơ thẻ vai trò. Đạt khi phân đúng ít nhất 6/8.

### 30–45 phút · Debrief vùng chồng lấn

Không chữa bằng “đáp án chức danh”. Hỏi sản phẩm trực tiếp là gì, ai chịu lỗi khi nó hỏng và ai
quyết trade-off. Dùng ba ca DA–AE, DA–DE và DA–BA.

## V. Nghiên cứu tình huống

### 55–85 phút · Guided practice

Phát một JD đã ẩn tên công ty và chức danh. Cả lớp đánh dấu ba màu: công cụ, nghiệp vụ, giao tiếp.
Làm mẫu hai dòng; học viên tự làm phần còn lại. Sau 12 phút, ghép cặp so kết quả và buộc giải
thích mọi chỗ khác nhau.

### 85–105 phút · Independent practice

Mỗi học viên làm một JD mới. Sản phẩm nộp gồm bảng phân loại, owner của năm nhiệm vụ và ba khoảng
trống năng lực cá nhân. Không hỏi giảng viên về “đáp án”; chỉ được hỏi về dữ kiện trong JD.

### 115–120 phút · Exit ticket

Trong 5 phút, không nhìn tài liệu: phân đúng ít nhất 6/8 nhiệm vụ và viết hai câu trả lời câu hỏi
“DA khác DE ở sản phẩm bàn giao và trách nhiệm vận hành như thế nào?”.
```

---

## 6. Phương án C — Một mạch bằng chứng, hai chế độ sử dụng — KHUYẾN NGHỊ

### 6.1. Cấu trúc

Phương án này dùng backward design. Mục I khai bằng chứng kết thúc; II–VI chỉ chứa nội dung cần
để tạo bằng chứng đó; VII biến cùng mạch nội dung thành runbook; VIII kiểm retrieval và transfer;
IX chuyển giao sang bài làm độc lập.

| Mục | Người học dùng để | Người dạy dùng để | Bắt buộc |
|---|---|---|---|
| I | Biết phải làm/nộp gì | Chốt evidence và ngưỡng | Objective → evidence → threshold |
| II | Gặp vấn đề trước thuật ngữ | Chạy diagnostic hook | Tình huống + câu hỏi chẩn đoán |
| III | Học mental model/cơ chế | Giải thích và demo | Cơ chế + worked example |
| IV | Ra quyết định trong ca mới | Chữa reasoning | Decision rule + boundary |
| V | Luyện có giàn giáo rồi bỏ giàn giáo | Guided/independent practice | Input, bước, output, answer check |
| VI | Nhận lỗi và giới hạn | Tiêm lỗi/phản ví dụ | Failure mode + cách phát hiện |
| VII | — | Vận hành đúng 120 phút | Timeline, setup, checkpoint, remediation |
| VIII | Tự kiểm retrieval và transfer | Formative + exit ticket | Đáp án/rubric, không chỉ câu hỏi |
| IX | Làm độc lập sau lớp | Retention/retest | Deliverable, constraint, rubric, handoff |

Không lặp nội dung giữa phần chính và VII. Mục VII trỏ tới block đã có, ví dụ “phút 25–40: chạy
Worked example 3.2”, không chép lại lời giải.

### 6.2. Tối ưu cho gì

- Một nguồn nội dung cho web, PDF, lớp học và slide.
- Mỗi phần đều truy được về Outcome/Done-when.
- Người tự học không phải đọc lời thoại giảng viên xen trong lý thuyết.
- Người dạy không phải tự dựng lại nhịp 120 phút.
- Dùng được cho LT, TH, DA và KT bằng profile, không ép mọi dạng thành bài lý thuyết.

### 6.3. Bắt buộc và tùy chọn

**Bắt buộc trong mọi bài:**

- Một bảng traceability ở mục I: objective, evidence, ngưỡng, nơi luyện, nơi kiểm.
- Một diagnostic hoặc prerequisite check trước khi dạy.
- Ít nhất một worked example và một novel task, trừ KT.
- Một phản ví dụ hoặc failure injection.
- Một checkpoint giữa buổi và một exit ticket.
- Rubric hoặc answer key đủ để người thứ hai chấm lại.
- Nguồn/locator cho claim; nhãn rõ cho suy luận của tác giả.

**Tùy bài:** lịch sử, định nghĩa mở rộng, case thứ hai, so sánh công cụ, code phụ, enrichment task.

### 6.4. Profile theo dạng bài

#### LT

- Mục III và IV chiếm trọng tâm.
- Mục V gồm một worked case có hướng dẫn và một ca mới ngắn.
- VIII kiểm giải thích, phân loại, chẩn đoán; không chỉ nhận diện thuật ngữ.

#### TH

- III chỉ giữ mental model, prerequisite, lệnh/cơ chế tối thiểu.
- V chiếm 40–55% note: setup → demo tối thiểu → guided practice → independent challenge → verify.
- VI tập trung lỗi runtime, dữ liệu biên, cách đọc thông báo lỗi và recovery.
- IX là biến thể mới, không lặp y nguyên lab.

#### DA

- II là brief và stakeholder context.
- IV là constraint/trade-off framework.
- V là milestones, checkpoints và review protocol, không phải lời giải từng bước.
- VIII/IX dùng rubric sản phẩm, defense và changed-assumption question.

#### KT

- Không thêm lý thuyết mới.
- II mô tả bối cảnh và dữ liệu chưa gặp; III chỉ ghi tài nguyên được phép dùng.
- IV nêu quy tắc, critical failures và cách xử lý ambiguity.
- V là đề và artefact cần nộp; VI là lỗi làm trượt; VII là vận hành/thu bài/chữa.
- VIII là rubric/answer key dành cho giảng viên; IX là remediation/retest, không giao homework mới.

### 6.5. Nó hỏng ở đâu

- Tốn công thiết kế traceability và rubric hơn phương án A.
- Nếu callout giảng viên không có cú pháp thống nhất, web sẽ rối.
- Người viết dễ lặp worked example ở III và V; review phải bắt duplication.
- Với 525 bài, rubric quá chi tiết có thể thành gánh nặng nếu chưa có thư viện mẫu tái sử dụng.

**Biện pháp chặn:** chốt một template thật trên ba bài pilot LT/TH/KT; lint heading; kiểm mỗi
objective có đúng một evidence chính; giới hạn mục VII trong một trang.

### 6.6. Mẫu thật — lesson 1 theo phương án C

```markdown
## I. Mục tiêu và chuẩn đầu ra

| Objective | Bằng chứng kết thúc | Ngưỡng | Luyện ở | Kiểm ở |
|---|---|---|---|---|
| Phân định trách nhiệm sáu vai trò trên nhiệm vụ mới | Bảng gán 15 nhiệm vụ kèm lý do | ≥ 12/15; lý do không mâu thuẫn ranh giới | §V.1 | Exit ticket §VIII.3 |
| Phân tích một JD thành công cụ, nghiệp vụ và giao tiếp | Bảng tần suất từ 10 JD có URL/ngày | Đủ 10 nguồn; mỗi yêu cầu vào đúng một nhóm chính | §V.2 | Homework §IX |
| Xác định khoảng trống năng lực cá nhân | Ma trận tự đánh giá 11 module | Mỗi mức có một bằng chứng hoặc ghi “chưa có” | §V.3 | Homework §IX |

**Câu chuyển giao:** gặp một yêu cầu chưa từng thấy, bạn phải chỉ ra sản phẩm bàn giao, owner chính
và lý do; chức danh trong JD không được dùng làm bằng chứng duy nhất.

## II. Bối cảnh và vấn đề đặt ra

> “Doanh thu tháng 10 giảm 12%, tìm hiểu giúp.”

Trước khi đọc tiếp, chọn việc đầu tiên: mở dashboard; viết SQL; hỏi baseline và quyết định đang
chờ; hay kiểm tra chiến dịch. Ghi một câu lý do.

Câu hỏi này chẩn đoán một ngộ nhận: đồng nhất nghề DA với thao tác trên công cụ. Nếu con số 12%
sai hoặc không có quyết định nào phụ thuộc kết quả, một báo cáo đẹp vẫn không tạo giá trị.

## III. Cơ sở lý thuyết và cơ chế vận hành

### 3.1. Mental model: sản phẩm bàn giao quyết định owner

Đi theo dòng đời dữ liệu:

`pipeline → model/metric dùng chung → phân tích → dashboard lặp lại → quyết định`

- DE chịu trách nhiệm chủ yếu với pipeline và độ tin cậy vận hành.
- AE chịu trách nhiệm model, test và định nghĩa dùng chung.
- DA chịu trách nhiệm kết luận phân tích phục vụ quyết định.
- BI Analyst chịu trách nhiệm sản phẩm theo dõi lặp lại.
- BA làm rõ yêu cầu và quy trình nghiệp vụ.
- DS xây bằng chứng dự báo/tối ưu khi câu hỏi vượt phân tích mô tả và chẩn đoán.

Tên chức danh thay đổi giữa công ty; sản phẩm bàn giao và failure ownership ổn định hơn.

### 3.2. Worked example

Yêu cầu: “Hai dashboard doanh thu ra hai số; hãy tạo một định nghĩa dùng chung và chặn việc tái
diễn.” Owner chính là AE vì deliverable là metric contract dùng lại. DA là domain collaborator;
DE tham gia nếu sai lệch bắt nguồn từ ingestion. Nếu yêu cầu chỉ là “giải thích chênh lệch tháng
này để CFO quyết định”, deliverable đổi thành kết luận, DA có thể là owner chính.

### 3.3. Phản ví dụ

“Dùng SQL” không chứng minh đây là việc DA: DE, AE, BI và DA đều dùng SQL. Công cụ không xác định
owner; trách nhiệm với sản phẩm khi nó hỏng mới là tín hiệu mạnh.

## IV. Khung quyết định và tiêu chí lựa chọn

Với mỗi nhiệm vụ, trả lời bốn câu theo thứ tự:

1. Sản phẩm trực tiếp là hệ thống, định nghĩa dùng chung, theo dõi lặp lại hay kết luận?
2. Ai chịu trách nhiệm khi sản phẩm sai hoặc không sẵn sàng?
3. Người nhận sẽ dùng nó cho quyết định nào?
4. Cần phối hợp vai trò nào, và ranh giới bàn giao ở đâu?

Nếu câu 1–2 chưa rõ, chưa được gán owner chỉ từ tên công cụ hoặc title.

## V. Nghiên cứu tình huống và thực hành

### 5.1. Guided practice — 8 nhiệm vụ

Giảng viên làm mẫu hai nhiệm vụ bằng bốn câu ở §IV. Học viên làm sáu nhiệm vụ còn lại theo cặp.
Mỗi câu trả lời phải có owner chính, collaborator và sản phẩm bàn giao.

### 5.2. Independent practice — một JD mới

Nhận một JD đã bỏ title và tên công ty. Phân loại từng yêu cầu thành công cụ, nghiệp vụ hoặc giao
tiếp; sau đó suy ra vai trò từ tập sản phẩm bàn giao. Chỉ xem title gốc sau khi đã nộp phán đoán.

### 5.3. Self-assessment có bằng chứng

Chấm bản thân 1–5 cho 11 module. Mỗi điểm từ 2 trở lên phải dẫn một artefact đã làm; không có
artefact thì ghi “chưa có bằng chứng”, không tự suy mastery từ việc đã xem video hoặc đọc sách.

## VI. Giới hạn và ngộ nhận phổ biến

| Ngộ nhận | Phép thử bác bỏ | Hậu quả nếu giữ |
|---|---|---|
| DA là người làm báo cáo | Đưa một báo cáo đúng số nhưng không hỗ trợ quyết định | Tối ưu hình thức thay vì câu hỏi |
| Công cụ xác định vai trò | Đưa cùng một SQL task với ba deliverable khác nhau | Gán sai owner |
| Công ty nào cũng có đủ sáu vai | Cho bối cảnh startup 20 người | Ranh giới trên giấy không dùng được |

## VII. Ghi chú phương pháp giảng dạy

| Phút | Hoạt động | Dùng phần | Bằng chứng quan sát |
|---:|---|---|---|
| 0–8 | Diagnostic cá nhân + pair explain | §II | Lý do ban đầu được lưu |
| 8–25 | Mental model + worked example | §III.1–3.2 | Học viên nói được “deliverable trước tool” |
| 25–40 | Phản ví dụ và boundary | §III.3, §IV | Sửa được ít nhất một gán sai |
| 40–60 | Guided practice | §V.1 | ≥ 6/8 trước feedback |
| 60–85 | Independent JD | §V.2 | Bảng phân loại hoàn chỉnh |
| 85–100 | Debrief vùng chồng lấn | §VI | Nêu owner + collaborator |
| 100–112 | Self-assessment | §V.3 | Không khai mastery thiếu evidence |
| 112–120 | Exit ticket | §VIII.3 | ≥ 12/15 |

Nếu lớp dưới 60% ở checkpoint phút 40, bỏ self-assessment trên lớp và dùng 15 phút đó chạy thêm
bốn nhiệm vụ có vùng chồng lấn. Self-assessment chuyển sang homework.

## VIII. Câu hỏi tự kiểm tra

1. Một pipeline chạy chậm làm dashboard trễ. Ai là owner chính và DA phải cung cấp bằng chứng gì?
2. Hai DA tự định nghĩa “khách hàng hoạt động” khác nhau. Deliverable nào đang thiếu?
3. Vì sao “cả hai đều dùng SQL” không đủ để phân biệt DA và AE?

**Exit ticket:** gán 15 nhiệm vụ cho sáu vai trò, mỗi nhiệm vụ một câu lý do. Đạt khi đúng ít nhất
12/15 và lý do không mâu thuẫn với khung §IV.

## IX. Bài tập về nhà

Thu thập 10 JD đang mở, lưu URL và ngày truy cập. Tạo bảng tần suất yêu cầu theo ba nhóm; đối chiếu
với 11 module; nộp ba khoảng trống năng lực có evidence hiện tại và hành động tiếp theo. Không dùng
một JD đã hết hạn mà không lưu snapshot hoặc trích đoạn cần thiết.
```

---

## 7. Bảng chấm ba phương án

Thang 1–5; 5 là tốt nhất. Trọng số phản ánh rủi ro nhân format ra 525 bài.

| Tiêu chí | Trọng số | A · Chương sách | B · Runbook | C · Một mạch bằng chứng |
|---|---:|---:|---:|---:|
| Tốc độ soạn hàng loạt | 25% | 5 | 3 | 3 |
| Người tự học đọc hiểu | 25% | 5 | 2 | 5 |
| Người dạy cầm lên dạy ngay | 25% | 2 | 5 | 5 |
| Hiển thị trên web/PDF | 15% | 5 | 3 | 4 |
| Truy vết objective → evidence | 10% | 3 | 4 | 5 |
| **Điểm có trọng số** | 100% | **4,00** | **3,40** | **4,35** |

### Phương án bị loại và tín hiệu mở lại

- **A thua** vì không đạt yêu cầu “người khác cầm lên dạy 120 phút mà không hỏi thêm”. Mở lại nếu
  sản phẩm chính chuyển thành sách tự học, không còn instructor-led delivery.
- **B thua** vì web/PDF dành cho người học bị nhiễu bởi runbook và khó dùng để tra cứu. Mở lại nếu
  repo tách hẳn learner handbook và instructor guide, có cơ chế chống lệch tự động.
- **C được chọn** vì giữ một nguồn nội dung nhưng phục vụ được hai chế độ. Quyết định phải xem lại
  nếu pilot ba bài cho thấy thời gian soạn vượt quá 1,5 lần A mà chất lượng dạy không cải thiện.

---

# PHẦN B — FORMAT SLIDE `slides.md`

## 8. Công cụ được chọn

Giữ **Marp** hiện có. Không thêm Reveal.js hay Slidev.

Lý do:

- Dependency đã được khoá trong `package.json`.
- `build_bai.py` đã sinh PPTX chỉnh sửa được và PDF trình chiếu.
- Theme `volt.css` đã xử lý typography, table, code, contrast và header/footer.
- Thêm công cụ thứ hai tạo thêm một pipeline, một theme và một failure mode mà không giải quyết
  vấn đề học tập nào ở Vòng 0.

## 9. Quan hệ note–slide

**Slide là các điểm chiếu của cùng mạch note, không phải bản tóm tắt toàn bộ note và không phải
một câu chuyện riêng.**

Mỗi slide phải trỏ ngầm hoặc tường minh tới một block trong note:

```text
note: vấn đề → cơ chế → worked example → practice → debrief → evidence
slide: cue      cue       reveal            prompt       compare     exit ticket
```

Chi tiết, nguồn, lời giải đầy đủ và remediation nằm trong note. Slide chỉ chứa thứ cả lớp cần
nhìn cùng lúc. Nếu một đoạn chỉ giảng viên cần, để ở mục VII của note, không đưa lên slide.

## 10. Số slide và nhịp 120 phút

| Dạng | Số slide mục tiêu | Nhịp dùng slide | Thời gian không nhìn slide |
|---|---:|---|---:|
| LT | 30–38 | 1,5–3 phút/slide khi giảng; checkpoint sau 8–10 phút | 45–60 phút |
| TH | 16–24 | 1–2 phút/slide hướng dẫn; code/demo trực tiếp | 70–90 phút |
| DA | 10–18 | brief, milestone, critique protocol, rubric | 80–95 phút |
| KT | 6–12 | luật, thời gian, deliverable, rubric, chữa bài | 75–110 phút |

Không dùng công thức “mỗi phút một slide”. Một slide activity có thể nằm trên màn hình 20 phút;
một chuỗi reveal của worked example có thể đổi sau 30–60 giây.

## 11. Giới hạn mật độ

- Một slide = một việc nhận thức: một luận điểm, một bước, một câu hỏi hoặc một so sánh.
- Tối đa khoảng 45 từ nội dung thường; slide activity/rubric có thể tới 70 từ nếu chữ vẫn ≥ 21 px.
- Tối đa 5 bullet, mỗi bullet tối đa 2 dòng.
- Code: tối đa 12 dòng; phần không liên quan thay bằng `…`; highlight đúng dòng đang nói.
- Bảng: tối đa 4 cột × 5 dòng trên một slide; bảng lớn tách hoặc đưa vào note.
- Hình/sơ đồ phải có mục đích: quan hệ, trình tự, không gian hoặc so sánh. Không dùng ảnh trang trí.
- Mọi hình bên ngoài có source/alt text trong comment hoặc note ref.
- Không thu nhỏ font để cứu một slide quá tải; tách slide.

## 12. Ngôn ngữ slide chuẩn

| Loại slide | Chứa | Không chứa |
|---|---|---|
| `lead` | bài, câu hỏi lớn, phase chuyển | mục lục dài |
| Problem | một tình huống và một câu hỏi | lời giải ngay trên slide |
| Mental model | 3–6 thành phần và quan hệ | đoạn văn giải thích đầy đủ |
| Worked example | một bước + dữ kiện đang dùng | toàn bộ lời giải một lần |
| Compare | tối đa 2–4 lựa chọn, cùng tiêu chí | bảng 12×12 |
| Checkpoint | prompt, thời gian, output | đáp án |
| Debrief | khác biệt giữa đáp án, failure mode | lặp nguyên prompt |
| Takeaway | một mệnh đề có thể dùng lại | khẩu hiệu sáo rỗng |

## 13. Khác biệt theo dạng bài

### LT

Slide luân phiên `problem → model → example → checkpoint`. Không chạy hơn 10 phút mà không có
một thao tác của người học.

### TH

Slide chỉ giữ setup, mục tiêu, checkpoint, lệnh/đoạn code ngắn và phép kiểm. Demo thật chạy ở
công cụ; không chụp 20 màn hình thao tác thành slide.

### DA

Slide là project brief, constraint, milestone, critique protocol và rubric. Không đưa “mẫu đáp
án đẹp” trước khi học viên tự ra quyết định.

### KT

Slide chứa luật, tài nguyên được phép dùng, đồng hồ mốc, artefact cần nộp, critical failures và
quy trình chữa. Không chứa hint nội dung làm thay bài.

## 14. Bộ slide mẫu thật — lesson 1

Đây là mẫu đủ để kiểm format và build, không phải deck cuối cùng của lesson 1. Deck cuối sẽ mở
rộng phần practice/debrief lên 30–38 slide nhưng giữ nguyên mạch dưới đây.

```markdown
---
marp: true
theme: volt
paginate: true
size: 16:9
header: 'Data Analyst · Lesson 1'
footer: 'Module 1 — Introduction to the Data Analyst Role'
---

<!-- _class: lead -->

# Data Analyst thực sự làm gì?
## Sản phẩm bàn giao trước công cụ

**LT · 120 phút**

---

## Tình huống mở đầu

> “Doanh thu tháng 10 giảm 12%, tìm hiểu giúp.”

**Việc đầu tiên bạn làm là gì?**

A. Mở Power BI  
B. Viết SQL  
C. Hỏi baseline và quyết định đang chờ  
D. Kiểm tra chiến dịch marketing

<!-- 30 giây chọn cá nhân · 90 giây giải thích theo cặp -->

---

<!-- _class: punch -->

# Một báo cáo có thể đúng mọi con số — và vẫn vô dụng.

---

## Bằng chứng cuối buổi

- Gán đúng **≥ 12/15 nhiệm vụ** cho sáu vai trò
- Mỗi gán có **một câu lý do** theo sản phẩm bàn giao
- Phân tích **10 JD** thành công cụ · nghiệp vụ · giao tiếp
- Chỉ khai năng lực khi có **evidence**

---

## Mental model

|  |  |  |  |  |
|---|---|---|---|---|
| Pipeline | → | Model / metric | → | Phân tích |
| **DE** |  | **AE** |  | **DA** |

|  |  |  |  |  |
|---|---|---|---|---|
| Dashboard lặp lại | → | Quyết định | → | Dự báo / tối ưu |
| **BI** |  | **BA + business** |  | **DS** |

---

## Sáu vai — sáu sản phẩm chính

| Vai | Sản phẩm trực tiếp |
|---|---|
| DE | Pipeline và hệ vận hành |
| AE | Model, test, metric contract |
| DA | Phân tích và khuyến nghị |
| BI | Dashboard theo dõi lặp lại |
| BA | Requirement và process |
| DS | Predictive/optimization model |

---

<!-- _class: punch -->

# Tool không xác định owner.

**Deliverable + failure ownership** mới là tín hiệu mạnh.

---

## Worked example · Hai dashboard, hai số

Yêu cầu:

> “Tạo một định nghĩa doanh thu dùng chung và chặn việc tái diễn.”

1. Deliverable là gì?  
2. Ai chịu lỗi nếu định nghĩa lệch?  
3. Ai cần phối hợp?

<!-- Chưa hiện đáp án; lấy ba ý kiến -->

---

## Debrief

**Owner chính: Analytics Engineer**

- Deliverable: metric contract dùng lại
- DA: domain collaborator
- DE: tham gia nếu lỗi từ ingestion

Nếu yêu cầu đổi thành “giải thích chênh lệch để CFO quyết định hôm nay”, owner có thể đổi sang DA.

---

## Khung bốn câu

1. Sản phẩm trực tiếp là gì?
2. Ai chịu trách nhiệm khi nó sai hoặc không sẵn sàng?
3. Quyết định nào phụ thuộc kết quả?
4. Ranh giới bàn giao giữa các vai ở đâu?

---

## Checkpoint · 8 nhiệm vụ

**12 phút · làm theo cặp**

Với mỗi nhiệm vụ, nộp:

- owner chính
- collaborator
- sản phẩm bàn giao
- một câu lý do theo khung bốn câu

**Mốc đạt trước feedback: ≥ 6/8**

---

## Ba vùng chồng lấn

| Cặp | Câu hỏi phân ranh giới |
|---|---|
| DA ↔ AE | Kết luận một lần hay định nghĩa dùng chung? |
| DA ↔ DE | Phân tích dữ liệu hay vận hành đường đi dữ liệu? |
| DA ↔ BA | Phân tích bằng chứng hay thiết kế quy trình? |

---

## Independent practice · JD không có title

**25 phút · làm cá nhân**

1. Đánh dấu: công cụ / nghiệp vụ / giao tiếp
2. Suy vai trò từ deliverable
3. Viết ba khoảng trống năng lực
4. Mỗi năng lực hiện có phải dẫn một artefact

---

## Failure mode

> “Tôi đã học Power BI nên tôi đã có năng lực dashboard.”

Exposure ≠ evidence.

Evidence có thể là dashboard chạy được, phép kiểm người dùng, rubric và phần bảo vệ trade-off.

---

## Exit ticket

**5 phút · không nhìn tài liệu**

- Gán 15 nhiệm vụ cho sáu vai
- Mỗi nhiệm vụ một câu lý do
- Đạt: **≥ 12/15** và không mâu thuẫn khung bốn câu

---

## Sau buổi học

Thu thập 10 JD đang mở:

- lưu URL + ngày truy cập
- lập bảng tần suất ba nhóm yêu cầu
- đối chiếu với 11 module
- chọn ba khoảng trống cần xử lý trước

---

<!-- _class: lead -->

# Bài sau
## Dữ liệu đi qua những chặng nào trước khi thành một con số?
```

---

## 15. Quy tắc đồng bộ note–slide

1. Viết note tới mức passed review trước khi viết slide.
2. Mỗi slide ghi comment `<!-- note: §x.y -->` trong bản production; checker có thể xác nhận section
   tồn tại.
3. Slide không được chứa claim, số hoặc ví dụ không có trong note/note ref.
4. Mọi checkpoint trong slide phải có answer/rubric trong note.
5. Mọi objective bắt buộc phải xuất hiện ít nhất một lần trong deck: objective, practice hoặc exit.
6. Khi note đổi outcome/evidence, test phải báo deck cần review lại; không sửa âm thầm một phía.

---

## 16. Kiểm thử format trước khi nhân rộng

Không duyệt format chỉ bằng lesson 1. Sau khi owner chọn phương án, tạo ba pilot:

| Pilot | Mục đích |
|---|---|
| Một LT | Kiểm explanatory depth, mental model, self-study và nhịp checkpoint |
| Một TH | Kiểm setup, guided → independent, verify và recovery |
| Một KT | Kiểm rubric, critical failure, timing và remediation |

### Acceptance criteria

- Người dạy thứ hai lập được buổi 120 phút chỉ từ note + slide, không hỏi tác giả câu nào về nội dung.
- Người tự học hoàn thành novel task và tự đối chiếu được bằng evidence/rubric.
- Tổng thời gian dạy nằm trong 110–120 phút ở dry run; không cắt phần independent practice.
- Mọi objective có evidence, ngưỡng, practice và assessment.
- Note build PDF; slide build PPTX/PDF; web render không mất bảng, details hoặc code.
- Không có claim mới trong slide; không có đáp án checkpoint chỉ tồn tại trong đầu người dạy.
- TH và KT không bị ép thành văn phong LT.

### Chưa chạy ở Vòng 0

- Chưa dry-run với giảng viên thứ hai.
- Chưa build deck mẫu vì deck đang nằm trong tài liệu đề xuất, chưa phải `slides.md` được duyệt.
- Chưa kiểm accessibility trực quan bằng projector/phòng học.
- Chưa đo thời gian soạn thực tế của ba phương án.

Các kiểm tra này phải chạy sau khi owner chọn format, trước khi ghi `FORMAT-DA-CHOT.md` là baseline.

---

## 17. Bản ghi lựa chọn có cấu trúc

```yaml
decision_id: curriculum-format-v0
status: proposed
scope: 525-lessons
options:
  - id: A
    name: reference-chapter
    optimizes_for: self-study-and-reference
    rejected_because: instructor-must-reconstruct-the-120-minute-session
    reopen_when: instructor-led-delivery-is-no-longer-a-primary-use-case
  - id: B
    name: timed-instructor-runbook
    optimizes_for: classroom-operability
    rejected_because: learner-facing-web-and-pdf-become-fragmented
    reopen_when: learner-and-instructor-artifacts-are-separated-with-drift-control
  - id: C
    name: evidence-spine-two-use-modes
    optimizes_for: traceable-learning-and-classroom-delivery
    selected: true
    selection_reason: one-content-spine-serves-self-study-and-teaching-without-duplicating-claims
approval:
  required: true
  owner: kina2711
  status: pending
next_gate:
  action: approve-or-reject-option-C
  then: pilot-one-LT-one-TH-one-KT-and-write-FORMAT-DA-CHOT.md
```

---

## 18. Điểm cần owner chốt

Chốt hoặc bác **Phương án C**. Nếu chốt, cần xác nhận thêm ba thông số trong pilot:

1. Cho phép callout giảng viên nằm trong note/web hay chỉ cho phép ở mục VII?
2. Target độ dài mặc định có dùng các khoảng ở §3.3 không?
3. Deck LT mục tiêu 30–38 slide có phù hợp cách dạy dự kiến không?

Không sang Vòng 1 trước khi ba điểm này có quyết định.

---

## 19. Dấu vết task contract

- Task: `academy-design-learning-module`.
- Profile/risk/path: `learning` · `R1-reviewed` · standard path.
- Deliverable: đề xuất format giáo trình và slide.
- Evidence: lesson 1, scaffold LT/KT, parser web, `build_bai.py`, Marp dependency và `volt.css`.
- Validation đã chạy: kiểm file/tool hiện hữu, kiểm parser boundary, đếm độ dài/headings lesson 1.
- Approval: **đang chờ owner**, chưa phải baseline.
- Residual risks: chưa dry-run, chưa user-test self-study, chưa build deck pilot, chưa đo authoring effort.
- Next owner/task: owner chọn format; sau đó pilot LT/TH/KT và chốt `FORMAT-DA-CHOT.md`.
