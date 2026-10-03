# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 338: The event envelope - before, after, op and source metadata

## Thực hành

**Nhiệm vụ.** Thu sự kiện cho một bảng và kiểm từng trường của phong bì. Cài đích áp dụng bằng ghi đè theo khoá với so phiên bản theo vị trí nhật ký. Chạy 10.000 thao tác hỗn hợp gồm thêm, sửa, xoá. Cố ý đảo thứ tự một số sự kiện khi giao và chứng minh so phiên bản giữ trạng thái đúng. Đối soát cuối cùng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là trạng thái đích khớp nguồn sau một chuỗi thao tác hỗn hợp. Kiểm bằng đối soát sau 10.000 thao tác; đạt khi đích khớp nguồn tuyệt đối và sự kiện tới sai thứ tự không làm sai trạng thái.

**Điều kiện đạt.** Đích khớp nguồn tuyệt đối sau 10.000 thao tác, và sự kiện bị đảo thứ tự không làm sai trạng thái nhờ so phiên bản.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ dùng trạng thái sau nên không biết cái gì đã đổi · áp dụng theo thứ tự tới thay vì theo vị trí nhật ký · xử lý sự kiện từ bản chụp như một lần sửa · bỏ qua sự kiện bia mộ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/226-the-event-envelope-before-after-op-and-source-metadata.md`
- Nội dung học thuật: `note.md` cùng thư mục.
