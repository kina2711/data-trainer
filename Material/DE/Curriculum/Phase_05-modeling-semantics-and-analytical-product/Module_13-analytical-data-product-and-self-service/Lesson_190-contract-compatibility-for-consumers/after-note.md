# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 190: Contract Compatibility for Consumers

## Thực hành

**Nhiệm vụ.** Viết hợp đồng năm phần cho sản phẩm. Thực hiện ba thay đổi ở ba mức. Với thay đổi phá vỡ, xác định ai đang dùng bằng nhật ký truy vấn, chạy quy trình hai giai đoạn với cửa sổ chuyển, và chứng minh không bên nào lỗi. Thực hiện một thay đổi mức hai và chứng minh có thông báo.

Chỉ dùng fixture, contexts và principals thử nghiệm có phiên bản. Không đổi metric production, xóa version cũ, chạy query tốn kém hoặc dùng dữ liệu nhạy cảm. Lưu input, version, artifact hashes, raw results, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu decision hoặc invariant trung tâm.
2. Đưa một phản ví dụ làm lựa chọn hiện tại sai.
3. Phân biệt evidence độc lập với implementation output.
4. Nêu owner, gate và artifact cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng việc bên tiêu thụ không lỗi lần nào. Kiểm bằng thí nghiệm đổi có tải; đạt khi không bên tiêu thụ nào lỗi và danh sách người dùng cái cũ được xác định trước khi bỏ.

**Điều kiện đạt.** Không bên tiêu thụ nào lỗi qua toàn bộ quá trình, danh sách người dùng được xác định trước khi bỏ, và thay đổi mức hai có thông báo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đổi nghĩa một cột mà giữ nguyên tên · bỏ cột cũ ngay sau khi thêm cột mới · không biết ai đang dùng · cửa sổ chuyển do kỹ thuật tự đặt.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/78-contract-compatibility-consumers.md`
- Nội dung học thuật: `note.md` cùng thư mục.
