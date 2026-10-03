# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 103: Transaction boundaries and the unit of work

## Thực hành

**Nhiệm vụ.** Cài ba ca sử dụng, mỗi cái ghi nhiều bảng. Tiêm lỗi ở giữa và đối soát để chứng minh không dở dang. Đếm số truy vấn cho mỗi yêu cầu và phát hiện truy vấn lặp, rồi sửa. Giữ một giao dịch mở trong lúc gọi hệ ngoài chậm và quan sát hồ kết nối cạn.

#### Bằng chứng cho DE-L103

Evidence pack cho ba use case gồm:

1. boundary diagram chỉ điểm begin, commit, rollback và external call;
2. transaction ownership table cho application service, repository và adapter;
3. fault-injection matrix với ít nhất năm fault point;
4. reconciliation query chứng minh không có trạng thái dở dang;
5. query-count report ở ba cỡ dataset;
6. pool metrics trước và trong thí nghiệm external call chậm;
7. trace cho một success và một rollback;
8. decision note giải thích phần nào cần atomic, phần nào eventual.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Vì sao repository không đủ ngữ cảnh để tự chọn commit boundary?
2. Flush khác commit ở bằng chứng nào?
3. Savepoint giải quyết được gì và không giải quyết được gì?
4. Vì sao external API call trong transaction vừa không atomic vừa gây cạn pool?
5. Một timeout sau commit tạo trạng thái bất định gì cho client?
6. Aggregate và table khác nhau thế nào khi chọn repository?
7. Metric nào phân biệt chờ pool với query chậm?
8. Vì sao assert mock `rollback()` chưa chứng minh atomicity?
9. Khi nào “một use case — một transaction” không phù hợp?
10. Cách chứng minh N+1 bằng thực nghiệm thay vì đọc code là gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quyết định thiết kế kiểm được bằng thí nghiệm lỗi giữa chừng. Kiểm bằng ba ca sử dụng có tiêm lỗi; đạt khi không ca nào để lại trạng thái dở dang và số truy vấn cho mỗi yêu cầu nằm trong ngưỡng.

**Điều kiện đạt.** Ba ca sử dụng không để lại trạng thái dở dang khi lỗi, số truy vấn mỗi yêu cầu trong ngưỡng, và tái hiện được hồ kết nối cạn.

#### Ma trận đánh giá

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Ownership | application use case điều khiển boundary | mỗi repository tự commit |
| Atomicity | lỗi giữa chừng không để state dở dang | có row hoặc invariant lệch |
| Resource scope | connection được trả sau commit/rollback | leak hoặc giữ qua external wait |
| External effect | có intent/idempotency/reconciliation rõ | giả định database rollback được API call |
| Query behavior | query count có ngưỡng và không tăng tuyến tính ngoài chủ đích | không đo hoặc có N+1 |
| Evidence | database thật, connection mới, command/output lưu được | chỉ mock call hoặc ảnh chụp |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Mở giao dịch ở tầng kho dữ liệu · gọi hệ ngoài trong giao dịch · giữ giao dịch qua nhiều bước chờ người dùng · không đếm số truy vấn mỗi yêu cầu.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/15-transaction-boundaries-and-unit-of-work.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
