---
loai: authentic-homework
lesson_id: DA-L001
trang_thai: ready-for-owner-review
nguong_dat: 75
---

# Homework: Decision-ready role map

## Bối cảnh cố định

Một công ty bán lẻ có sáu yêu cầu trong cùng tuần:

1. POS Đà Nẵng thiếu dữ liệu từ ngày 21 tới 31.
2. Finance và Growth dùng hai định nghĩa net revenue khác nhau.
3. Ban điều hành muốn dashboard revenue mỗi ngày.
4. Growth muốn biết vì sao tỷ lệ hoàn đơn tăng.
5. Supply muốn dự báo tồn kho bốn tuần.
6. Operations muốn viết lại quy trình phê duyệt hoàn tiền.

Nguồn lực hiện có: một DA, một DE hỗ trợ theo phạm vi, một BI Developer và một Operations Manager. Chưa có Analytics Engineer hay Data Scientist chuyên trách.

Không tự thêm dữ kiện làm đổi semantics. Mọi assumption phải nằm trong assumption ledger cùng impact-if-wrong.

## Artifact phải nộp

Một thư mục gồm:

- role-map.md
- decision-memo.md
- evidence-register.md
- reflection.md

### Phần A: Role map, 35 điểm

Với từng yêu cầu, ghi:

| Task | Consumer | Decision | Primary owner | Supporting owner | Artifact | Critical failure | Handoff evidence |
|---|---|---|---|---|---|---|---|

Sau bảng, giải thích hai vùng chồng lấn có rủi ro cao. Không được dùng tên công cụ làm lý do chính.

### Phần B: Audit case revenue, 30 điểm

Dùng fixture của bài:

- tháng 09: 3,00 tỷ
- tháng 10 trên dashboard: 2,64 tỷ
- dữ liệu nạp bù đã đối soát: 0,24 tỷ
- khách cũ tháng 10: 2,12 tỷ
- khách mới tháng 10: 0,76 tỷ

Nộp:

1. phép tính mức giảm observed và reconciled
2. claim ledger gồm claim, evidence, strength, uncertainty
3. ít nhất ba giả thuyết cạnh tranh cho phần giảm khách mới
4. evidence plan để phân biệt các giả thuyết
5. một decision memo từ 350 tới 500 từ

### Phần C: Adversarial review, 20 điểm

Tạo hai failure mode khiến artifact trông hợp lý nhưng conclusion sai. Với mỗi failure mode:

- ghi expected observation trước khi kiểm
- nêu oracle độc lập
- mô tả consumer harm
- nêu condition bác bỏ recommendation

### Phần D: Changed constraint, 15 điểm

**Changed constraint:** DE không còn tham gia; DA là người dữ liệu duy nhất.

Viết memo từ 250 tới 350 từ:

- phần trách nhiệm nào DA tạm thời nhận
- tiêu chí nào không được hạ
- work nào phải defer
- blast radius nếu chọn sai
- owner phê duyệt rủi ro
- reversal trigger để quay lại mô hình cũ

## Rubric chấm điểm

| Tiêu chí | Điểm | Full-credit evidence |
|---|---:|---|
| Decision framing và role boundary | 20 | Consumer, decision, owner và handoff rõ; không gán vai theo tool |
| Data validation và phép tính | 20 | Tái lập được 12% và 4%; tách observed khỏi reconciled |
| Claim, evidence và uncertainty | 20 | Claim không vượt evidence; có giả thuyết cạnh tranh |
| Failure paths và oracle | 15 | Hai phản ví dụ thật, expected result viết trước, oracle độc lập |
| Recommendation và trade-off | 15 | Action, owner, deadline, alternative và reversal trigger |
| Handoff và khả năng audit | 10 | Evidence register đủ để reviewer độc lập lần lại lập luận |

**Ngưỡng đạt:** từ 75/100 và không có critical failure.

## Critical-failure rules

- Gán vai chỉ bằng tên công cụ.
- Dùng mức giảm 12% để khuyến nghị sau khi đã biết coverage thiếu.
- Gọi khách mới là nguyên nhân mà không nêu đây mới là decomposition.
- Sửa expected result sau khi thấy output nhưng không ghi discrepancy.
- Không có evidence gốc hoặc dùng chính implementation đang kiểm làm oracle duy nhất.
- Khẳng định mastery hay production readiness vượt evidence của bài.

## Remediation và retest

Reviewer chỉ rõ rubric row và failed invariant. Người học sửa đúng phần trượt, sau đó làm lại trên scenario mới: subscription revenue lệch do refund đến muộn. Retest phải giữ bản gốc, feedback, bản sửa và evidence mới thành bốn artifact riêng.

## References

- [[wiki.da.operating-as-a-data-analyst|Operating as a Data Analyst]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.da.revenue-and-commerce-analytics|Revenue and commerce analytics]]
