# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 250: Batch Idempotency Deterministic Keys and Overwrite

## Thực hành

**Nhiệm vụ.** Cài bốn cơ chế cho bốn đường dẫn có hình dạng dữ liệu khác nhau. Chạy mỗi đường dẫn 20 lần với thời điểm bắt đầu ngẫu nhiên và có lần bị giết giữa chừng. So trạng thái cuối với trạng thái của một lần chạy sạch. Đo chi phí của ghi đè phân vùng khi phân vùng lớn dần.

Chỉ chạy trên fixture/sandbox được phép. Lưu versions, inputs, state trước–sau, kill points, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và phạm vi bảo đảm.
2. Chỉ ra một failure window.
3. Phân biệt expected result với evidence đã chạy.
4. Đưa counterexample làm thiết kế thất bại.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái hội tụ sau nhiều lần chạy ngẫu nhiên. Kiểm bằng phép thử chạy lại hỗn loạn; đạt khi trạng thái sau 20 lần chạy chồng chéo khớp trạng thái sau một lần chạy sạch.

**Điều kiện đạt.** Trạng thái sau 20 lần chạy chồng chéo khớp trạng thái của một lần chạy sạch ở cả bốn đường dẫn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Băm trên giá trị chưa chuẩn hoá · ghi dấu hiệu hoàn tất trước dữ liệu · dùng ghi đè phân vùng cho phân vùng quá lớn · tuyên bố đúng một lần mà không nêu ranh giới.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/138-batch-idempotency-deterministic-keys-overwrite.md`
- Nội dung học thuật: `note.md` cùng thư mục.
