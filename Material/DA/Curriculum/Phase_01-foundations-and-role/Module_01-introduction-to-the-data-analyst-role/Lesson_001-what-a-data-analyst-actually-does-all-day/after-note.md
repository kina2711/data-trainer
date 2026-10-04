# Phase 1: Nền tảng và vai trò Data Analyst
# Module 1: Nhập môn vai trò Data Analyst
# Lesson 1: Practice, assessment and transfer

## Thực hành

### Worked trace: tám task được phân ranh giới

| Task | Owner chính | Artifact | Handoff quan trọng |
|---|---|---|---|
| sửa pipeline mất dữ liệu | DE | patch, backfill, run evidence | DA xác nhận fitness-for-analysis |
| định nghĩa net revenue | AE hoặc metric owner | definition, tests | Finance và DA ký semantics |
| dashboard ngày | BI | report, refresh state | consumer xác nhận usability |
| phân tích churn | DA | analysis, memo | owner nhận action và uncertainty |
| dự báo churn | DS | model, evaluation | DA/Business xác nhận decision use |
| đặc tả hoàn tiền | BA | process, requirements | Ops xác nhận acceptance |
| đối soát hai báo cáo | DA cùng AE | discrepancy log | metric owner xử lý root cause |
| trình bày khuyến nghị | DA | decision memo | decision owner nhận trách nhiệm |

Đây không phải answer key duy nhất. Nếu tổ chức khác phân owner khác, câu trả lời vẫn đạt khi artifact, invariant và handoff được bảo vệ.

### Guided task

Nhóm ba người nhận tám thẻ trên và hoàn thành các bước sau:

1. ghi consumer và decision cho từng thẻ
2. chọn owner chính và supporting owner
3. nêu một critical failure
4. viết evidence để handoff được chấp nhận

**Điều kiện đạt:** đúng ít nhất 6/8 theo logic outcome/artifact và không có thẻ nào chỉ giải thích bằng công cụ.

### Independent task

Cho tình huống tỷ lệ hoàn đơn tăng từ 8% lên 12%, tự tạo:

- decision brief
- role map
- ba check phân biệt data issue với business change
- decision memo tối đa 180 từ

### Changed constraint

Công ty chỉ còn một người dữ liệu trong hai tuần. Viết lại RACI nhưng không được xóa invariant của ingestion, metric và conclusion. Đánh dấu phần nào phải defer thay vì giả vờ một người có thể hoàn thành đồng thời.

### Feedback protocol

1. Người học trình bày decision và boundary trước output.
2. Reviewer hỏi evidence nào có thể bác bỏ claim này?
3. Reviewer gắn phản hồi với scene ID và observable artifact, không suy đoán năng lực chung.
4. Người học tự nói lại lỗi, sửa artifact và ghi discrepancy.
5. Retest dùng scenario khác; không chấm việc học thuộc wording.

## Kiểm tra cuối bài

### Recall cần thiết

- Sáu pha của vòng phân tích là gì?
- Artifact và critical failure khác job title thế nào?
- Reconciliation khác decomposition thế nào?

### Apply hoặc diagnose

Dashboard revenue giảm 15%, settlement control chỉ giảm 5%, khách mới giảm còn khách cũ tăng. Hãy chỉ ra:

1. claim nào được phép nói ngay
2. claim nào phải dừng
3. owner cần tham gia
4. evidence tiếp theo
5. action có thể đảo ngược

### Transfer

Một bệnh viện yêu cầu dashboard thời gian chờ. Không dùng lại vocabulary bán lẻ, hãy khóa consumer, decision, population, time boundary, privacy constraint và owner.

### Cách chấm rubric

- 0: nêu output hoặc tool, không có decision
- 1: có decision nhưng thiếu boundary/evidence
- 2: có claim và evidence nhưng thiếu uncertainty/handoff
- 3: có full chain cùng alternative và reversal trigger

## Novel-scenario retest

Một startup tuyển Data Analyst nhưng JD gồm Airflow, dbt, dashboard và churn model. Tách ít nhất bốn mũ, nêu thứ tự ưu tiên triển khai và một condition làm thứ tự đó đảo.

**Pass condition:** có consumer, artifact, failure owner, rejected alternative và blast radius. Không chấm theo việc trùng đáp án mẫu.

## Bài làm sau buổi học

### Bài làm

Hoàn thành quiz.md và homework.md. Ngưỡng quiz là 8/10. Ngưỡng homework là 75/100 cùng zero critical failure.

### Kiểm lại trước khi nộp

- Mọi claim có evidence locator.
- Observed và reconciled không bị trộn.
- Decomposition không bị gọi là causal proof.
- Owner, deadline và reversal trigger tồn tại.
- Assumption có impact-if-wrong.

### Cách nộp

Giữ bốn phiên bản riêng: original, feedback, revision và retest. Không ghi đè failed attempt vì mất dấu vết học tập.

## Remediation map

| Lỗi quan sát | Quay lại | Micro-task | Retest |
|---|---|---|---|
| bắt đầu từ dashboard | S01 | viết ba decision questions | case thời gian chờ |
| coi quy trình tuyến tính | S02, S03 | vẽ feedback loop | case source late |
| gán vai theo tool | S04, S05 | map bằng artifact/failure | JD startup |
| vượt quá evidence | S07 | viết claim ladder | case settlement lệch |
| memo không hành động được | S08 | thêm owner và trigger | case churn |

## Giới hạn

Gói chưa được dạy trên cohort thật nên độ khó chưa được hiệu chỉnh bằng learner evidence. Kết quả chỉ chứng minh performance trong scope DA-L001, không chứng nhận năng lực nghề nghiệp hoặc production readiness.

## References

- [[wiki.da.operating-as-a-data-analyst|Operating as a Data Analyst]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.da.revenue-and-commerce-analytics|Revenue and commerce analytics]]
