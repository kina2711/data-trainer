# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 211: MPP Strong Scaling - MIMD SPMD Batch and SIMD

## Thực hành

**Nhiệm vụ.** Chạy cùng một truy vấn với 1, 2, 4 và 8 nút; tính tăng tốc và hiệu suất song song ở mỗi mức. Tách thời gian tính, thời gian trao đổi dữ liệu và thời gian chờ rào đồng bộ. Tìm mức mà thêm nút không còn giúp và quy trần về phần tuần tự, lệch tải, truyền thông hay nút cổ chai bên ngoài. Với một tác vụ, truy tiếp xuống tầng lô và tầng làn theo lesson 208.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi quy mức tăng về đúng tầng thay vì gộp. Kiểm bằng thí nghiệm tăng quy mô; đạt khi hiệu suất song song được đo ở ít nhất bốn mức và trần được quy về một trong bốn nguyên nhân bằng bằng chứng.

**Điều kiện đạt.** Hiệu suất song song có số đo ở ≥ 4 mức nút, trần được quy về một nguyên nhân có bằng chứng, và hệ phân cấp ba tầng truy được trên một tác vụ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm nút khi trần là nguồn dữ liệu bên ngoài · coi chênh lệch thời gian giữa các tác vụ là lỗi · gộp ba tầng song song thành một lời giải thích.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/99-mpp-strong-scaling-mimd-spmd-batch-simd.md`
- Nội dung học thuật: `note.md` cùng thư mục.
