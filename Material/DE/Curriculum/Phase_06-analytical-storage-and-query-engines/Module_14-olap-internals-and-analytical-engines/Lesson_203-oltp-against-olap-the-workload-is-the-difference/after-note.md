# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 203: OLTP and OLAP - Workload Before Product Name

## Thực hành

**Nhiệm vụ.** Cho sáu mô tả khối lượng công việc, trong đó hai cái nằm ở ranh giới. Chấm từng cái theo năm chiều và suy ra hệ phù hợp. Với hai ca ranh giới, nêu hai điều kiện đẩy nó về mỗi phía. Đo một truy vấn phân tích chạy trên cơ sở dữ liệu giao dịch và trên hệ cột, ghi lại chênh lệch.

Chỉ dùng fixture, file và engine thử nghiệm có version; không dùng dữ liệu cá nhân, mở quyền production hoặc chạy benchmark trên hệ dùng chung. Lưu dataset generator/hash, configuration, commands, raw outputs, cache state, reviewer và limitations.

## Kiểm tra cuối bài

1. Nêu decision, invariant hoặc workload characteristic trung tâm.
2. Đưa một confounder có thể làm kết luận sai.
3. Phân biệt expected result với evidence đã quan sát.
4. Nêu counterexample hoặc changed constraint làm lựa chọn phải đảo.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt khung giải thích cho mười bài sau. Kiểm bằng bài phân loại sáu khối lượng công việc; đạt khi phân đúng ít nhất năm và lý do dẫn được về năm chiều chứ về tên sản phẩm.

**Điều kiện đạt.** Phân đúng ≥ 5/6 khối lượng công việc, lý do dẫn về năm chiều, và có số đo chênh lệch giữa hai hệ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân loại theo tên sản phẩm thay vì theo khối lượng công việc · giả định hệ phân tích luôn nhanh hơn · bỏ qua chiều đồng thời · chạy báo cáo nặng trên bản sao đọc rồi tưởng đã tách tải.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/91-oltp-olap-workload-before-product-name.md`
- Nội dung học thuật: `note.md` cùng thư mục.
