# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 62: Scheduling, priority and load average

## Thực hành

**Nhiệm vụ.** Tạo bốn tình huống tải: bão hoà CPU, chờ vào ra nặng, áp lực bộ nhớ, và nhiều tiến trình chờ được cấp CPU. Với mỗi tình huống, ghi tải trung bình, mức dùng CPU chia theo loại, và độ dài hàng đợi chạy. Phân loại từng tình huống. Chỉ ra tình huống nào có tải trung bình cao mà CPU rảnh.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là đọc và diễn giải chỉ số đúng, kỹ năng dùng trực tiếp khi trực. Kiểm bằng bốn máy mô phỏng; đạt khi phân loại đúng ít nhất ba và mỗi lần dẫn được chỉ số phân biệt chứ chỉ tải trung bình.

**Điều kiện đạt.** Phân loại đúng ≥ 3/4 tình huống, và chỉ ra đúng tình huống tải trung bình cao trong khi CPU rảnh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận CPU bận vì tải trung bình cao · so tải trung bình mà quên số lõi · bỏ qua phần chờ vào ra trong mức dùng CPU.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/062-scheduling-priority-and-load-average.md`
- Nội dung học thuật: `note.md` cùng thư mục.
