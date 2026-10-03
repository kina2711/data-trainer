# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 217: CSV and JSON Ambiguity Contracts

## Thực hành

**Nhiệm vụ.** Ghi cùng dữ liệu ra hai định dạng. Tái hiện ba lỗi: giá trị rỗng bị đọc thành chuỗi rỗng, số lớn mất độ chính xác, và dấu thời gian lệch múi giờ. Với mỗi lỗi, chỉ ra giả định nào khác nhau giữa hai bên và khai báo tường minh chặn nó. Tạo một tệp có xuống dòng trong giá trị trích dẫn và chứng minh không chia được.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu schema/source hashes, versions, commands, raw bytes, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu identity và compatibility boundary trung tâm.
2. Đưa một ca parse sạch nhưng sai nghĩa.
3. Nêu counterexample đảo quyết định.
4. Phân biệt configured intent với observed evidence.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Bài mở module, kiểm bằng phép thử vòng tròn. Kiểm bằng ba lỗi tái hiện; đạt khi cả ba được tái hiện, chẩn đoán đúng, và chặn bằng một khai báo tường minh.

**Điều kiện đạt.** Ba lỗi được tái hiện và chặn bằng khai báo tường minh, và tệp không chia được được chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Giả định bên đọc hiểu giá trị rỗng giống bên ghi · để số định danh dài đi qua định dạng đối tượng lồng nhau · tin tệp phân tách bằng dấu luôn chia được · suy kiểu dữ liệu từ một mẫu nhỏ đầu tệp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/105-csv-json-ambiguity-contracts.md`
- Nội dung học thuật: `note.md` cùng thư mục.
