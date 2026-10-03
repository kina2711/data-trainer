# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 193: Documentation Tests

## Thực hành

**Nhiệm vụ.** Viết bốn loại kiểm tài liệu và đưa vào quy trình có cửa chặn. Tiêm bốn vi phạm: thêm cột công khai không mô tả, làm hỏng một truy vấn mẫu, nhắc một chỉ số đã khai tử, và đổi lịch làm mới mà không sửa tài liệu. Xác nhận cả bốn bị chặn. Liệt kê ba thứ phải rà soát bằng người.

Chỉ dùng product, fixture và accounts thử nghiệm; không thu recording hoặc dữ liệu cá nhân khi chưa có consent và retention rule. Khóa task, oracle, protocol và version trước khi đo. Lưu raw observations, invalid-attempt rules, deviations và artifact hashes; không suy population result từ sample nhỏ.

## Kiểm tra cuối bài

1. Nêu user task và oracle xác định kết quả đúng.
2. Phân biệt tool capability với user outcome.
3. Nêu một failure nhanh nhưng sai nghĩa và cách phát hiện.
4. Nêu bằng chứng, giới hạn mẫu và owner cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn tự động có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng bốn vi phạm tiêm; đạt khi cả bốn bị chặn ở đúng loại kiểm.

**Điều kiện đạt.** Bốn vi phạm đều bị chặn ở đúng loại kiểm, và ba thứ cần rà soát người được liệt kê rõ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ kiểm sự tồn tại của tài liệu chứ không kiểm nội dung · không chạy truy vấn mẫu · để tài liệu ngoài quy trình kiểm · tin rằng kiểm tự động thay được rà soát người.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/81-documentation-tests.md`
- Nội dung học thuật: `note.md` cùng thư mục.
