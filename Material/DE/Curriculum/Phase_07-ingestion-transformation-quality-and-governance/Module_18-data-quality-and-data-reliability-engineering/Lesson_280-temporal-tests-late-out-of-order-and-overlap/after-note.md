# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 280: Temporal tests - late, out of order and overlap

## Thực hành

**Nhiệm vụ.** Cài bốn phép kiểm thời gian. Dựng một bộ đối chứng có mốc thời gian biết trước. Tiêm bốn lỗi: dữ liệu muộn vượt cửa sổ, sự kiện sai thứ tự, khoảng hiệu lực chồng nhau, và toàn bộ dữ liệu bị dịch một múi giờ. Chứng minh ba nhóm phép kiểm ở lesson 279 đều xanh với ca dịch múi giờ, còn phép kiểm ranh giới ngày thì đỏ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective nhắm vào một lỗi đi qua được toàn bộ phép kiểm thông thường. Kiểm bằng bốn lỗi tiêm gồm ca dịch múi giờ; đạt khi cả bốn bị bắt và hai bất biến không có dung sai.

**Điều kiện đạt.** Bốn lỗi thời gian đều bị bắt, ca dịch múi giờ được chứng minh lọt qua ba nhóm kia, và hai bất biến chạy không dung sai.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt dung sai cho bất biến khoảng hiệu lực · kiểm thời gian mà không có bộ đối chứng · giả định mốc thời gian nguồn luôn cùng múi giờ · bỏ kiểm chuyển trạng thái ngược chiều vì hiếm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/168-temporal-tests-late-out-of-order-and-overlap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
