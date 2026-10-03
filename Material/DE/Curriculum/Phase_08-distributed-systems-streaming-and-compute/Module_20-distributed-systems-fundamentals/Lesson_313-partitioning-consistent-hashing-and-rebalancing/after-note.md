# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 313: Partitioning, consistent hashing and rebalancing

## Thực hành

**Nhiệm vụ.** Cài ba cách chia trên cùng tập khoá thật có phân bố lệch. Đo độ lệch tải giữa các phân vùng. Thêm một nút và đo lượng dữ liệu phải di chuyển ở từng cách. Tạo một khoá nóng chiếm phần lớn lưu lượng, thử ba cách xử lý và đo lại. Chạy tái cân bằng có giới hạn tốc độ trong lúc hệ đang phục vụ và đo ảnh hưởng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là độ lệch tải giảm có số đo. Kiểm bằng phép đo phân bố; đạt khi ba cách chia có số đo độ lệch, lượng dữ liệu di chuyển khi thêm nút được đo, và phân vùng nóng giảm lệch sau khi xử lý.

**Điều kiện đạt.** Ba cách chia có số đo độ lệch và lượng dữ liệu di chuyển, và phân vùng nóng giảm độ lệch sau khi xử lý.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chia theo băm rồi vẫn cần quét theo khoảng · thêm nút để chữa phân vùng nóng · tái cân bằng không giới hạn tốc độ · đo phân bố bằng khoá sinh ngẫu nhiên đều thay vì khoá thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/201-partitioning-consistent-hashing-and-rebalancing.md`
- Nội dung học thuật: `note.md` cùng thư mục.
