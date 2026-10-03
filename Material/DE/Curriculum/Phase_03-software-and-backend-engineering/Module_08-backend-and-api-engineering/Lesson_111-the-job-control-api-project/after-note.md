# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 111: The job-control API project

## Thực hành

**Nhiệm vụ.** Xây giao diện theo đặc tả. Chạy năm phép thử hỏng và ghi kết quả từng cái. Chạy tải và viết ghi chú công suất. Viết mô hình mối đe doạ ngắn nêu ba mối đe doạ chính và cách chặn. Viết sổ tay ba mục gồm bão hoà, cơ sở dữ liệu hỏng, và triển khai lỗi.

Bài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Lease hết hạn khi worker cũ còn sống gây race nào?
2. Worker chết sau external effect cần protocol gì?
3. Cancellation requested khác cancelled thế nào?
4. Fault artifact nào chứng minh không mất job?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một dịch vụ có trạng thái chịu được sự cố. Kiểm bằng năm phép thử hỏng cộng rà soát tài liệu; đạt khi không phép thử nào sinh tác động kép hoặc mất công việc.

**Điều kiện đạt.** Năm phép thử hỏng đều không sinh tác động kép và không mất công việc, và ba tài liệu đều có nội dung kiểm được.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Thêm kho đệm mà chưa đo · không có cơ chế thuê nên hai thợ cùng nhận một việc · bỏ phép thử triển khai khi đang chạy · sổ tay viết sau khi bảo vệ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/23-job-control-api-project.md`
- Nội dung học thuật: `note.md` cùng thư mục.
