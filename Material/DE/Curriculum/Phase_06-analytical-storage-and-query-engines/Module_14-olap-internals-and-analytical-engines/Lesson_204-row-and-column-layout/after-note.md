# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 204: Row and Column Layout - Isolating Physical Layout

## Thực hành

**Nhiệm vụ.** Ghi cùng một bảng trăm cột ở hai bố cục, tắt nén ở cả hai. Chạy bốn truy vấn chọn lần lượt 1, 3, 10 và 100 cột. Đo lượng byte đọc và thời gian. Vẽ quan hệ giữa số cột chọn và lượng byte đọc, kiểm nó tuyến tính ở bố cục cột và phẳng ở bố cục hàng. Đo chi phí cập nhật một dòng ở cả hai.

Chỉ dùng fixture, file và engine thử nghiệm có version; không dùng dữ liệu cá nhân, mở quyền production hoặc chạy benchmark trên hệ dùng chung. Lưu dataset generator/hash, configuration, commands, raw outputs, cache state, reviewer và limitations.

## Kiểm tra cuối bài

1. Nêu decision, invariant hoặc workload characteristic trung tâm.
2. Đưa một confounder có thể làm kết luận sai.
3. Phân biệt expected result với evidence đã quan sát.
4. Nêu counterexample hoặc changed constraint làm lựa chọn phải đảo.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi cô lập một biến, nên thiết kế đo phải tắt các cơ chế còn lại. Kiểm bằng phép đo có đối chứng; đạt khi lượng byte đọc được giải thích bằng tỉ lệ số cột chọn và sai số dưới mức thoả thuận.

**Điều kiện đạt.** Quan hệ số cột chọn với byte đọc tuyến tính ở bố cục cột và phẳng ở bố cục hàng, và có số đo chi phí cập nhật một dòng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bật nén khi đo bố cục nên không tách được phần đóng góp · chọn toàn bộ cột rồi kết luận hệ cột không nhanh hơn · đo thời gian mà không đo byte đọc · so hai bố cục ở hai bộ dữ liệu khác nhau.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/92-row-column-layout-isolating-physical-layout.md`
- Nội dung học thuật: `note.md` cùng thư mục.
