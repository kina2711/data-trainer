# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 182: Metric Lifecycle - Propose, Certify, Version, Deprecate

## Thực hành

**Nhiệm vụ.** Dựng vòng đời năm trạng thái với cửa chặn tự động cho danh mục chứng nhận. Đưa ba chỉ số qua vòng đời, trong đó một cái thiếu bộ đối soát và phải bị chặn. Thực hiện một lần đổi định nghĩa mức hai với thông báo và kiểm hồi quy. Thực hiện một lần đổi công thức mức ba theo đủ quy trình: tạo phiên bản thứ hai, chạy song song cả hai trên cùng dữ liệu ít nhất một chu kỳ, đối soát và báo cho bên tiêu thụ chênh lệch bằng số, lấy chấp thuận, rồi gỡ bản cũ và nộp bản ghi khai tử. Khai tử một chỉ số với cửa sổ chuyển tiếp và xác nhận không còn ai dùng trước khi gỡ.

Chỉ dùng fixture, contexts và principals thử nghiệm có phiên bản. Không đổi metric production, xóa version cũ, chạy query tốn kém hoặc dùng dữ liệu nhạy cảm. Lưu input, version, artifact hashes, raw results, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu decision hoặc invariant trung tâm.
2. Đưa một phản ví dụ làm lựa chọn hiện tại sai.
3. Phân biệt evidence độc lập với implementation output.
4. Nêu owner, gate và artifact cần để hoàn thành.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quy trình quản trị có tiêu chí nghiệm thu bằng việc chặn đúng và khai tử sạch. Kiểm bằng ba chỉ số đi qua vòng đời cộng một lần di trú phá vỡ; đạt khi chỉ số thiếu điều kiện bị chặn chứng nhận, lần di trú có số chênh lệch đo được giữa hai phiên bản, và chỉ số khai tử không còn người dùng khi gỡ.

**Điều kiện đạt.** Chỉ số thiếu điều kiện bị chặn chứng nhận, đổi công thức mức ba có chạy song song kèm số chênh lệch và chấp thuận của bên tiêu thụ, bản ghi khai tử đầy đủ, và chỉ số khai tử không còn người dùng khi gỡ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chứng nhận chỉ số chưa có bộ đối soát · **sửa đè công thức tại chỗ thay vì tạo phiên bản mới** · gỡ bản cũ trước khi có chấp thuận của bên tiêu thụ · đổi định nghĩa làm số đổi mà không thông báo · gỡ chỉ số khi còn người dùng · không có quy trình khai tử nên danh mục chỉ phình.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/70-metric-lifecycle-propose-certify-version-deprecate.md`
- Nội dung học thuật: `note.md` cùng thư mục.
