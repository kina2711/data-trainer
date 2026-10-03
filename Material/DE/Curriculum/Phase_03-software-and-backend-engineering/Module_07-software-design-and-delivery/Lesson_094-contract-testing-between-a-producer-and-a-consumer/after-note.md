# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 94: Contract testing between a producer and a consumer

## Thực hành

**Nhiệm vụ.** Dựng một bên cung cấp và một bên tiêu thụ. Viết hợp đồng từ phía tiêu thụ và đưa vào quy trình của bên cung cấp. Thực hiện ba thay đổi: thêm trường tuỳ chọn, xoá trường bắt buộc, và đổi kiểu. Ghi lại phép kiểm hợp đồng phản ứng thế nào với từng cái. Thực hiện thay đổi phá vỡ theo quy trình hai giai đoạn mà không làm bên tiêu thụ lỗi.

#### Bằng chứng cho DE-L094

Nộp:

1. producer và consumer source/version;
2. ít nhất một contract happy path và hai error paths;
3. consumer-side verification result;
4. provider-side verification result;
5. compatibility matrix cho ba thay đổi;
6. log chứng minh optional-field case pass theo policy;
7. failure chứng minh remove/type-change bị chặn;
8. commit sequence của migration hai giai đoạn;
9. active-consumer inventory;
10. final verification matrix và artifact hashes.

#### Ma trận ba thay đổi

| Thay đổi | Kỳ vọng policy mẫu | Consumer verify | Provider verify | Release |
|---|---|---|---|---|
| thêm optional `note` | compatible nếu reader tolerant | pass | pass | cho phép |
| xóa required `order_id` | breaking | contract không đổi | fail | chặn |
| đổi `total` number → string | breaking | có thể fail decode | fail matcher | chặn |

Policy mẫu phải được thay nếu consumer thực dùng strict decoder hoặc payload limit khác.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Vì sao unit test xanh hai phía vẫn chưa đủ?
2. Contract artifact được dùng khác nhau ở consumer và provider ra sao?
3. Contract test không chứng minh phần nào của business logic?
4. Vì sao thêm optional field có thể breaking?
5. Shape compatibility và semantic compatibility khác nhau thế nào?
6. Active-consumer inventory quyết định contraction ra sao?
7. Hai giai đoạn expand/contract gồm các bước nào?
8. Event contract cần thêm điều gì so với HTTP?
9. Matcher nào tránh brittle nhưng vẫn bảo vệ semantics?
10. Bằng chứng nào cho thấy breaking change bị chặn trước deploy?

> [!synthesis]
> Bộ ba thay đổi bắt buộc, evidence pack và scoring matrix là phép kiểm tổng hợp cho DE-L094. Các nguồn cung cấp contract-testing và compatibility semantics; rubric cụ thể thuộc thiết kế giáo trình này.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cơ chế kiểm được bằng thí nghiệm đổi lược đồ. Kiểm bằng ba thay đổi; đạt khi phép kiểm hợp đồng chặn đúng thay đổi phá vỡ và cho qua thay đổi tương thích.

**Điều kiện đạt.** Phép kiểm hợp đồng chặn đúng thay đổi phá vỡ, cho qua thay đổi tương thích, và quy trình hai giai đoạn hoàn tất không gây lỗi.

#### Ma trận chấm

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Ownership | expectation xuất phát từ consumer và được producer review | producer tự snapshot response |
| Two-sided proof | cả client serializer và provider endpoint được chạy | chỉ validate schema tĩnh |
| CI integration | breaking change chặn trước release | report chỉ để tham khảo |
| Version lineage | contract gắn consumer/provider version và hash | file latest không identity |
| Migration | expand, migrate, observe, contract | xóa trước rồi báo consumer |
| Semantics | có policy và semantic cases | coi shape pass là đủ |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Dùng phép kiểm đầu cuối thay cho hợp đồng · viết hợp đồng từ phía cung cấp nên nó chỉ mô tả cái đang có · đổi lược đồ rồi mới báo bên tiêu thụ.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/06-consumer-provider-contract-testing.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
