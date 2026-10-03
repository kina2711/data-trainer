# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 205: Encoding and Compression - Choosing from Data Shape

## Thực hành

**Nhiệm vụ.** Tạo bốn cột có bốn đặc trưng khác nhau. Ghi mỗi cột bằng cả bốn cách mã hoá cộng ba mức nén khối. Đo kích thước và thời gian giải nén. Lập ma trận. Sắp lại bảng theo một cột và đo lại độ dài chạy để chứng minh nó phụ thuộc thứ tự. Chọn cấu hình cho từng cột và chứng minh tổng thời gian truy vấn giảm.

Chỉ dùng fixture, file và engine thử nghiệm có version; không dùng dữ liệu cá nhân, mở quyền production hoặc chạy benchmark trên hệ dùng chung. Lưu dataset generator/hash, configuration, commands, raw outputs, cache state, reviewer và limitations.

## Kiểm tra cuối bài

1. Nêu decision, invariant hoặc workload characteristic trung tâm.
2. Đưa một confounder có thể làm kết luận sai.
3. Phân biệt expected result với evidence đã quan sát.
4. Nêu counterexample hoặc changed constraint làm lựa chọn phải đảo.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quyết định có hai ràng buộc đối nghịch. Kiểm bằng ma trận cách mã hoá nhân đặc trưng dữ liệu; đạt khi mỗi ô có cặp số và lựa chọn cho mỗi cột dẫn được từ ma trận.

**Điều kiện đạt.** Ma trận có cặp số ở mọi ô, hiệu ứng thứ tự sắp xếp lên độ dài chạy được chứng minh, và cấu hình chọn làm giảm tổng thời gian truy vấn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bật nén mạnh nhất cho mọi cột · dùng từ điển cho cột gần như duy nhất · đo kích thước mà không đo thời gian giải nén · quên rằng độ dài chạy phụ thuộc thứ tự sắp xếp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/93-encoding-compression-choosing-data-shape.md`
- Nội dung học thuật: `note.md` cùng thư mục.
