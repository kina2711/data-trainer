# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 125: DML, DDL, constraints and views

## Thực hành

**Nhiệm vụ.** Viết lệnh hợp nhất theo khoá nghiệp vụ và chạy lại năm lần trên cùng dữ liệu, chứng minh không sinh trùng. Tạo nguồn có dòng trùng và quan sát kết quả không xác định. Thêm một ràng buộc lên bảng 5 triệu dòng đang có tải, đo thời gian khoá ở hai cách làm.

Lưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Vì sao MERGE chưa tự là idempotent?
2. NOT VALID và VALIDATE tách rủi ro nào?
3. View khác materialized view thế nào?
4. Lock budget cần đo những đại lượng gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm hai thao tác có ràng buộc vận hành kiểm được. Kiểm bằng thí nghiệm ghi lặp và thí nghiệm đổi cấu trúc có tải; đạt khi ghi lặp không sinh trùng và thời gian khoá dưới ngưỡng.

**Điều kiện đạt.** Ghi lặp năm lần không sinh trùng, và thời gian khoá khi thêm ràng buộc dưới ngưỡng ở cách làm hai bước.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng lệnh hợp nhất với nguồn chưa khử trùng · thêm ràng buộc trực tiếp lên bảng lớn đang có tải · chồng khung nhìn nhiều tầng · nhầm khung nhìn với khung nhìn vật chất hoá.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/13-dml-ddl-constraints-and-views.md`
- Nội dung học thuật: `note.md` cùng thư mục.
