# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 322: Topic, partition, key and the ordering boundary

## Thực hành

**Nhiệm vụ.** Dựng cụm ba máy chủ với một chủ đề sáu phân vùng. Với mười tình huống về khoá và nhóm tiêu thụ, dự đoán phân vùng, thứ tự và bên sở hữu trước khi chạy, rồi đối chiếu. Tăng số phân vùng và chứng minh một khoá cụ thể chuyển sang phân vùng khác, làm bản ghi mới của nó không còn thứ tự với bản ghi cũ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dự đoán khớp thực tế. Kiểm bằng mười tình huống; đạt khi dự đoán đúng ít nhất tám trước khi chạy, và ca phá thứ tự khi tăng phân vùng được tái hiện.

**Điều kiện đạt.** Dự đoán đúng ≥ 8/10 tình huống trước khi chạy, và ca khoá chuyển phân vùng sau khi tăng được tái hiện bằng dữ liệu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Giả định thứ tự toàn cục trong một chủ đề · dùng vị trí như định danh bản ghi · tăng phân vùng mà không xử lý khoá và thứ tự · gửi bản ghi không khoá rồi mong có thứ tự.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/210-topic-partition-key-and-the-ordering-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
