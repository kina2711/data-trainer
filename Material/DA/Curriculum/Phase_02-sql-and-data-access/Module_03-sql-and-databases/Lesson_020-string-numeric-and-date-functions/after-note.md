# Phase 2: Data Analyst
# Module 3: SQL and Databases
# Lesson 20: String, numeric and date functions

## Thực hành

**Nhiệm vụ.** Trên `DS2`: chuẩn hoá cột tên khách, tách họ và tên, gom ngày về đầu tháng, tính tuổi đơn hàng theo ngày.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng đối chiếu: kết quả chuẩn hoá trong SQL phải khớp từng dòng với bản làm bằng Excel ở lesson 10. Ràng buộc đối chiếu chéo công cụ được đặt ở đây vì nó là mẫu lặp lại ở lesson 71 và 72.

**Điều kiện đạt.** Kết quả chuẩn hoá trên `DS2` khớp từng dòng với bản đối chứng, và không có dòng nào bị loại trong im lặng do lỗi ép kiểu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng `CAST` không bắt lỗi trên dữ liệu bẩn nên truy vấn dừng giữa chừng · chia nguyên khi cần chia thực · `DATE_TRUNC` sai đơn vị làm lệch kỳ báo cáo.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/020-string-numeric-and-date-functions.md`
