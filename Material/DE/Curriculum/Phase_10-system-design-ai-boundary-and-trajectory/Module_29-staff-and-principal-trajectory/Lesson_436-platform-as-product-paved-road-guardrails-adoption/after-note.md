# Phase 10: System Design, AI Boundary and Trajectory
# Module 29: Staff and Principal Trajectory
# Lesson 436: Platform as product - paved road, guardrails, adoption

## Thực hành

**Nhiệm vụ.** Chọn một quy trình mà đội dùng hay phải xin phê duyệt. Dựng đường dẫn mẫu gồm khuôn mẫu, tài liệu và ví dụ chạy được. Thay ít nhất ba điểm phê duyệt thủ công bằng rào chắn tự động. Nhờ hai người thuộc hai đội khác nhau dùng đường dẫn mẫu và bấm giờ tới thay đổi đầu tiên chạy được; đếm số lần họ phải hỏi mình. Đo ba chỉ số mức áp dụng và ghi mọi chỗ họ vấp; mỗi lần phải hỏi là một thiếu sót của tài liệu hoặc của rào chắn, sửa rồi đo lại với người thứ hai.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng nội bộ chứ bằng tính năng đã xây. Kiểm bằng phép thử người; đạt khi **hai người thuộc hai đội khác nhau** đều đưa được thay đổi đầu tiên lên sản xuất trong giới hạn thời gian mà không hỏi mình, và ít nhất ba rào chắn thay được phê duyệt thủ công.

**Điều kiện đạt.** Hai người thuộc hai đội khác nhau đều đưa được thay đổi đầu tiên lên sản xuất trong giới hạn thời gian mà không hỏi mình, ≥ 3 điểm phê duyệt được thay bằng rào chắn, và ba chỉ số mức áp dụng có số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Xây nền tảng rồi chờ người ta tới · đo bằng số phiếu đã đóng · giữ phê duyệt thủ công vì an tâm hơn · không có ví dụ chạy được trong tài liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/324-platform-as-product-paved-road-guardrails-adoption.md`
- Nội dung học thuật: `note.md` cùng thư mục.
