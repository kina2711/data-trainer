# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 123: Window functions - partition, order and frame

## Thực hành

**Nhiệm vụ.** Trên dữ liệu cố ý có giá trị trùng, viết ba truy vấn: top ba sản phẩm mỗi chi nhánh, đơn gần nhất của mỗi khách, và chia khách thành năm nhóm theo chi tiêu. Với mỗi cái, thử cả bốn hàm xếp hạng và giải thích vì sao chọn cái đã chọn.

Lưu SQL, seed data, dự đoán trước khi chạy, output thô, đối soát độc lập và giải thích theo rule. Ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Partition, order và frame khác nhau thế nào?
2. Bốn ranking functions xử lý tie ra sao?
3. Vì sao window không đặt trong WHERE cùng level?
4. Lag có đồng nghĩa kỳ lịch trước không?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi chọn đúng biến thể theo ngữ nghĩa, chỗ khác biệt chỉ lộ ra ở ca biên. Kiểm bằng ba yêu cầu trên dữ liệu có trùng; đạt khi cả ba chọn đúng hàm và kết quả đúng ở ca có trùng.

**Điều kiện đạt.** Ba truy vấn đúng trên dữ liệu có trùng, và giải thích được vì sao chọn hàm xếp hạng đó thay vì ba hàm kia.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng hàm xếp hạng có trùng khi cần đúng một dòng mỗi nhóm · quên phân vùng nên xếp hạng toàn bảng · đặt hàm cửa sổ vào mệnh đề lọc dòng · thử trên dữ liệu không có giá trị trùng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/11-window-functions-partition-order-and-frame.md`
- Nội dung học thuật: `note.md` cùng thư mục.
