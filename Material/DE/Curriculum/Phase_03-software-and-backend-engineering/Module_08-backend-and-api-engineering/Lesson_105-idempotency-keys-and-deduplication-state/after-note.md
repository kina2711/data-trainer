# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 105: Idempotency keys and deduplication state

## Thực hành

**Nhiệm vụ.** Cài khoá bất biến cho điểm tạo công việc. Ba thí nghiệm: gọi lại cùng khoá sau khi thành công, gọi lại sau khi máy chủ chết giữa chừng, và gọi hai yêu cầu cùng khoá đồng thời. Với mỗi thí nghiệm, đếm số công việc thật được tạo. Viết phần hợp đồng mô tả điều kiện và thời hạn thử lại.

#### Ba thí nghiệm bắt buộc

#### A. Response mất sau success

Cho server commit rồi cắt response. Client retry cùng key. Chứng minh chỉ có một business row/job và response replay trỏ đúng effect.

#### B. Process chết giữa chừng

Giết process tại từng fault point: sau reserve, sau business write, trước outcome, sau commit. Đọc lại bằng process mới và chứng minh policy recovery không tạo effect kép.

#### C. Hai request cùng key

Dùng barrier gửi hai request cùng lúc tới hai worker/replica. Một request sở hữu reservation; request kia chờ hoặc nhận trạng thái theo contract. Lặp đủ số vòng và đối soát effect count bằng unique business identity.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Vì sao timeout không cho biết request đã commit hay chưa?
2. HTTP idempotence khác idempotency key thế nào?
3. Vì sao hash request không thay được client-generated key?
4. Same key + different payload phải xử lý ra sao?
5. `SELECT` rồi `INSERT` hỏng ở lịch chạy nào?
6. Vì sao lưu response sau business commit tạo cửa sổ duplicate?
7. Request thứ hai thấy `IN_PROGRESS` có các lựa chọn nào?
8. Retention thay đổi semantics ra sao?
9. Tại sao replay resource state hiện tại có thể sai?
10. Khi effect ở hệ ngoài, cần thêm cơ chế gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Objective đòi ghép giao dịch, lưu trạng thái và xử lý đồng thời thành một cơ chế mà thư viện không cho sẵn. Kiểm bằng ba thí nghiệm; đạt khi cả ba đều không sinh tác động kép.

**Điều kiện đạt.** Cả ba thí nghiệm đều tạo đúng một công việc, và hợp đồng nêu rõ điều kiện cùng thời hạn thử lại.

#### Ma trận đánh giá DE-L105

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Identity | key do client tạo, scope rõ | key global hoặc derive mù từ body |
| Collision | fingerprint khác bị từ chối | trả response cũ cho payload mới |
| Atomicity | reservation, effect, outcome cùng boundary khi có thể | effect commit trước cache không có recovery |
| Concurrency | unique constraint quyết owner | check-then-insert |
| Lifecycle | in-progress, terminal, expiry có policy | chỉ có cache hit/miss |
| Retry contract | conditions và window công bố | “cứ retry” |
| Evidence | ba fault scenario, command/output và reconciliation | chỉ unit test tuần tự |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Lưu khoá ngoài giao dịch · để hai yêu cầu cùng khoá cùng đi qua · không nêu thời hạn trong hợp đồng · dùng dấu thời gian làm khoá bất biến.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/17-idempotency-keys-and-deduplication-state.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
