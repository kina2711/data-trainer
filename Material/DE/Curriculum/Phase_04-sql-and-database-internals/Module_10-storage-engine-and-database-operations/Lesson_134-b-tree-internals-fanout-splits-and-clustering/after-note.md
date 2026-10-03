# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 134: B-tree internals - fanout, splits and clustering

## Thực hành

**Nhiệm vụ.** Tạo chỉ mục trên bảng một triệu dòng và đo chiều cao cây cùng kích thước. Chèn 100.000 dòng theo khoá tăng dần rồi theo khoá ngẫu nhiên vào hai bảng riêng; so thông lượng chèn và độ phân mảnh. Xoá 50% dòng và đo phình chỉ mục, rồi dựng lại và đo lại.

Lưu SQL, dữ liệu sinh, tham số, dự đoán trước khi chạy, plan dạng máy đọc được, output thô, đối soát và thông số môi trường. Chỉ chạy `EXPLAIN ANALYZE`, DML, tải dữ liệu, thao tác cache, `pageinspect` hoặc extension trong PostgreSQL thử nghiệm cô lập; không dùng production để tạo cold cache hay benchmark. Ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Fanout ảnh hưởng độ sâu cây B-tree thế nào?
2. Insert tuần tự và ngẫu nhiên tạo hai profile chi phí nào?
3. Free space tái sử dụng khác bloat cần reclaim thế nào?
4. CLUSTER thay đổi locality nhưng không duy trì điều gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối cấu trúc bên trong với hiện tượng đo được. Kiểm bằng hai thí nghiệm chèn; đạt khi đo đúng chiều cao cây và chỉ ra khác biệt giữa hai thứ tự chèn bằng số.

**Điều kiện đạt.** Chiều cao cây đo đúng, và chênh lệch giữa hai thứ tự chèn cùng mức phình sau khi xoá đều có số chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ chỉ mục là danh sách sắp xếp · bỏ qua phình chỉ mục sau nhiều lần xoá · gom cụm theo nhiều thứ tự cùng lúc · chèn theo khoá tăng dần ở hệ ghi rất nhiều mà không lường điểm nóng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/22-btree-internals-fanout-splits-and-clustering.md`
- Nội dung học thuật: `note.md` cùng thư mục.
