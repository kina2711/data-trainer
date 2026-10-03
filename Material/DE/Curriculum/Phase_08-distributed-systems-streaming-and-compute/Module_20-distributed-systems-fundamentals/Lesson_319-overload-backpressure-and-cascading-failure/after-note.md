# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 319: Overload, backpressure and cascading failure

## Thực hành

**Nhiệm vụ.** Dựng ba dịch vụ nối nhau. Làm dịch vụ cuối chậm dần và đo chuỗi lan truyền: thời gian giữ kết nối, độ sâu hàng đợi, tỉ lệ hết giờ, tỉ lệ thử lại. Ghi lại thời điểm sập toàn bộ. Thêm lần lượt bốn cơ chế và đo đóng góp của từng cái. Tái hiện cơn bão thử lại đồng bộ rồi chặn bằng nhiễu ngẫu nhiên.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ giữ được một phần năng lực thay vì sập toàn bộ. Kiểm bằng phép thử tải có phụ thuộc chậm; đạt khi bản chưa phòng thủ sập hoàn toàn và bản có phòng thủ giữ được tỉ lệ phục vụ trên ngưỡng.

**Điều kiện đạt.** Bản chưa phòng thủ sập hoàn toàn còn bản có phòng thủ giữ tỉ lệ phục vụ trên ngưỡng, và đóng góp của từng cơ chế có số đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại không có ngân sách · dùng một bể kết nối chung cho mọi phụ thuộc · lùi dần không có nhiễu · coi sập toàn bộ và suy giảm một phần là như nhau.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/207-overload-backpressure-and-cascading-failure.md`
- Nội dung học thuật: `note.md` cùng thư mục.
