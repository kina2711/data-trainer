# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 102: API contracts: resources, errors and versioning

## Thực hành

**Nhiệm vụ.** Thiết kế và cài giao diện cho tài nguyên công việc: tạo, xem, liệt kê có phân trang theo con trỏ, và huỷ. Viết đặc tả giao diện. Dựng phép kiểm hợp đồng từ phía một máy khách. Thực hiện ba thay đổi và ghi phản ứng của phép kiểm. Chèn bản ghi mới giữa lúc phân trang và chứng minh không trùng không sót.

#### Bằng chứng cho DE-L102

- resource contract cho create/get/list/cancel;
- error envelope và status/error matrix;
- cursor format/version cùng ordering invariant;
- thí nghiệm concurrent insert có tập kết quả đối chiếu;
- consumer/provider contract artifacts;
- kết quả ba thay đổi: additive pass, removal/type change bị chặn;
- deprecation/compatibility policy.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Vì sao resource action đôi khi rõ hơn ép mọi thứ vào CRUD?
2. Cursor pagination cần total order và immutable key ra sao?
3. Thêm field tùy chọn có thể phá consumer nào?
4. HTTP status và stable application error code khác vai trò gì?
5. Versioning vì sao không thay deprecation/adoption telemetry?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép kiểm hợp đồng ở lesson 94. Kiểm bằng ba thay đổi hợp đồng; đạt khi thêm trường không làm bên tiêu thụ lỗi và hai thay đổi phá vỡ bị phép kiểm chặn.

**Điều kiện đạt.** Phân trang theo con trỏ không trùng không sót khi dữ liệu đổi, và ba thay đổi hợp đồng cho phản ứng đúng như thiết kế.


## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Phân trang theo số trang · phong bì lỗi mỗi chỗ một kiểu · trả mã trạng thái chung cho mọi lỗi · đổi kiểu một trường mà giữ nguyên phiên bản.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/14-api-contract-resources-errors-versioning.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
