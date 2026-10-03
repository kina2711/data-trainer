# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 95: Refactoring in small behaviour-preserving steps

## Thực hành

**Nhiệm vụ.** Nhận một mô đun 300 dòng không có phép kiểm. Viết phép kiểm đặc tả chốt hành vi hiện tại. Tái cấu trúc thành ba tầng theo lesson 91 bằng ít nhất sáu bước nhỏ, mỗi bước một commit chạy được. Chứng minh hành vi đầu ra không đổi trên cùng bộ dữ liệu.

#### Case study: tách module nạp dữ liệu 300 dòng

Giả sử `run_import()` đang đọc file, parse, validate, gọi API enrichment, ghi PostgreSQL và gửi metric. Mục tiêu là tách application service cùng adapters mà không đổi contract CLI.

| Commit | Thay đổi | Bằng chứng |
|---|---|---|
| 1 | thêm characterization fixtures cho valid, invalid và partial input | output, exit code, rejected rows |
| 2 | extract `parse_rows` | fixture parity |
| 3 | extract `validate_record` | decision-table tests |
| 4 | đưa enrichment qua port | contract test cho adapter thật |
| 5 | đưa persistence qua port | integration test transaction |
| 6 | tạo application service | public CLI tests không đổi |
| 7 | chuyển wiring vào composition root | architecture/import test |
| 8 | xóa dead path | search, coverage và full parity |

Nếu commit 5 làm error class đổi từ `ImportFailed` sang driver exception, refactor đã làm rò abstraction. Nếu commit 6 thay thứ tự enrichment và validation, số lần gọi API có thể đổi dù output của fixture nhỏ vẫn giống; side-effect ledger phải phát hiện.

## Kiểm tra cuối bài

#### Bài tự kiểm tra

1. Vì sao test private method làm giảm khả năng refactor dù coverage tăng?
2. Khi nào byte-for-byte golden master chặt quá mức?
3. Vì sao sửa một bug đã biết phải nằm ngoài commit refactor?
4. Một thay đổi làm query count từ 10 xuống 1 nhưng output không đổi có còn là refactor không? Contract vận hành nào cần ghi?
5. Nếu old và new implementation cùng fail trên một input, parity có chứng minh cả hai đúng không?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi kỷ luật quy trình chứ kiến thức mới. Kiểm bằng lịch sử Git cộng bộ kiểm; đạt khi mọi commit đều chạy được và bộ kiểm xanh, và hành vi cuối giống hành vi đầu.

**Điều kiện đạt.** Mọi commit đều chạy được với bộ kiểm xanh, và đầu ra trên bộ dữ liệu chuẩn khớp tuyệt đối với bản gốc.

#### Checklist nghiệm thu DE-L095

- [ ] Có baseline chạy lại được và ghi tool/dependency version.
- [ ] Behavior inventory gồm output, schema, lỗi và side effect.
- [ ] Ít nhất sáu commit; mỗi commit compile và test xanh.
- [ ] Không commit nào trộn sửa lỗi hoặc feature.
- [ ] Output chuẩn trước–sau khớp theo rule đã công bố.
- [ ] Có danh sách hành vi đáng ngờ được hoãn sang change riêng.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Đập ra viết lại từ đầu · trộn sửa lỗi vào commit tái cấu trúc · tái cấu trúc khi chưa có phép kiểm nào · đưa mẫu thiết kế vào vì thấy hay.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/07-behavior-preserving-refactoring.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
