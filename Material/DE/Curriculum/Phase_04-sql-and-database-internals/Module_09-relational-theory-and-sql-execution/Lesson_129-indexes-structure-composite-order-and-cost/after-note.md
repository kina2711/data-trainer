# Phase 4: SQL and Database Internals
# Module 9: Relational Theory and SQL Execution
# Lesson 129: Indexes - structure, composite order and cost

## Thực hành

**Nhiệm vụ.** Nhận nhật ký 50 truy vấn thật. Thiết kế bộ chỉ mục. Đo thời gian bộ truy vấn trước và sau, và đo thông lượng ghi trước và sau. Cố ý tạo một chỉ mục sai thứ tự cột và chứng minh nó không được dùng. Tìm và bỏ các chỉ mục không bao giờ được dùng.

Lưu SQL, seed/workload, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy DDL/spill/load test trong môi trường cô lập với lock/statement timeout; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Leftmost rule có skip-scan nuance gì?
2. INCLUDE khác key columns thế nào?
3. Vì sao idx_scan bằng zero chưa đủ để drop?
4. Định lượng read gain và write cost bằng gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi cân hai chiều đối nghịch, chứ chỉ thêm chỉ mục. Kiểm bằng bảng đo hai chiều; đạt khi đọc nhanh lên có số, ghi chậm đi được định lượng, và không chỉ mục nào thừa.

**Điều kiện đạt.** Bộ truy vấn nhanh lên có số, tác động lên thông lượng ghi được định lượng, và chứng minh được chỉ mục sai thứ tự không được dùng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thêm chỉ mục cho mọi cột trong điều kiện lọc · đặt sai thứ tự cột trong chỉ mục tổ hợp · bọc hàm quanh cột lọc làm chỉ mục vô hiệu · không đo tác động lên ghi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/17-index-structure-composite-order-and-cost.md`
- Nội dung học thuật: `note.md` cùng thư mục.
