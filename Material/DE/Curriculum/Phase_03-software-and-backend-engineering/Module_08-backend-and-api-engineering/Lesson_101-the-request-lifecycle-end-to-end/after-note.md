# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 101: The request lifecycle end to end

## Thực hành

**Nhiệm vụ.** Dựng một dịch vụ tối thiểu có lớp trung gian ghi nhật ký. Gửi một yêu cầu và ghi lại dấu thời gian ở từng chặng bằng nhật ký có mã theo dõi. Vẽ đường đi có chú thích hạn chờ và chế độ hỏng. Phân biệt điểm kiểm sức khoẻ với điểm kiểm sẵn sàng bằng cách ngắt kết nối cơ sở dữ liệu và xem cái nào đổi trạng thái.

#### Thí nghiệm ngắt database

1. Dịch vụ đang ready và live.
2. Ngắt database hoặc route tới endpoint test thất bại.
3. Readiness phải chuyển fail trong thời gian đã định.
4. Liveness vẫn pass nếu process/event loop còn hoạt động.
5. Request phụ thuộc database trả lỗi bounded, không treo vô hạn.
6. Khôi phục database; readiness trở lại sau successful check và hysteresis nếu có.
7. Kiểm log/metric/trace ghi đúng stage và reason.

Nếu mọi instance cùng unready, service có thể không nhận traffic để trả controlled 503. Kiến trúc cần quyết định behavior ở load balancer/orchestrator, không chỉ endpoint code.

#### Bằng chứng cho DE-L101

- sơ đồ đủ bảy chặng và đường response quay lại;
- mỗi chặng có timeout/budget và ít nhất một failure mode;
- request log có timestamp/correlation ở từng stage;
- thí nghiệm database outage làm readiness fail nhưng liveness giữ pass;
- dependency timeout bounded và trace xác định stage lỗi;
- ghi rõ concurrency model của server.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Client timeout cho biết gì và không cho biết gì về side effect?
2. Middleware order làm thay đổi evidence và security ra sao?
3. Vì sao pool wait cần tách khỏi query execution?
4. Khi database mất, liveness và readiness nên phản ứng khác nhau thế nào?
5. Cancellation khác rollback ở điểm nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, tổng hợp kiến thức đã có thành một bản đồ. Kiểm bằng bài vẽ có chú thích; đạt khi đủ bảy chặng, mỗi chặng có hạn chờ và ít nhất một chế độ hỏng.

**Điều kiện đạt.** Sơ đồ đủ bảy chặng với hạn chờ và chế độ hỏng, và hai điểm kiểm phản ứng khác nhau khi mất kết nối cơ sở dữ liệu.


## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Đọc nguồn tham chiếu và tự giải thích lại; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Vẽ sơ đồ mà bỏ qua lớp trung gian · dùng một điểm kiểm cho cả hai mục đích · không đặt hạn chờ ở chặng gọi cơ sở dữ liệu.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/13-request-lifecycle-end-to-end.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
