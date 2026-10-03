# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 330: Controller quorum and metadata

## Thực hành

**Nhiệm vụ.** Cho bốn tình huống với triệu chứng và số đo. Với mỗi cái, xác định sự cố thuộc mặt phẳng nào và liệt kê việc cụm còn làm được. Trên cụm lab, dừng số đông điều khiển và quan sát: ghi và đọc trên phân vùng cũ còn chạy không, tạo chủ đề mới có được không, người dẫn mới có bầu được không.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho bài diễn tập. Kiểm bằng bốn tình huống chẩn đoán; đạt khi phân đúng ít nhất ba và nêu đúng việc cụm còn làm được gì trong mỗi tình huống.

**Điều kiện đạt.** Phân đúng ≥ 3/4 tình huống, và quan sát thật trên cụm xác nhận đúng việc cụm còn làm được khi mất số đông điều khiển.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nhầm sự cố điều khiển với sự cố dữ liệu · giả định mất số đông điều khiển là cụm ngừng hoàn toàn · theo dõi cụm chỉ bằng chỉ số của mặt phẳng dữ liệu · đổi cấu hình khi số đông điều khiển chưa lành.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/218-controller-quorum-and-metadata.md`
- Nội dung học thuật: `note.md` cùng thư mục.
