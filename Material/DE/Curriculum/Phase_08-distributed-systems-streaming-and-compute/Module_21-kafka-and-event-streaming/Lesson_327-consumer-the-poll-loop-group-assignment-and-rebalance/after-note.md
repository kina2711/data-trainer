# Phase 8: Distributed Systems, Streaming and Compute
# Module 21: Kafka and Event Streaming
# Lesson 327: Consumer - the poll loop, group, assignment and rebalance

## Thực hành

**Nhiệm vụ.** Với chủ đề sáu phân vùng, chạy nhóm từ một tới tám thành viên; dự đoán phân bổ trước mỗi lần thay đổi rồi đối chiếu. Đo thông lượng khi số thành viên vượt số phân vùng. Làm xử lý một lô chậm hơn thời hạn và quan sát bão tái cân bằng; đếm số lần tái cân bằng và số bản ghi bị xử lý lại. Áp ba cách giảm và đo lại.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là dự đoán khớp và ca hỏng được chặn có số đo. Kiểm bằng sáu tình huống cộng thí nghiệm xử lý chậm; đạt khi dự đoán đúng ít nhất năm và bão tái cân bằng được chặn với số lần tái cân bằng giảm có số đo.

**Điều kiện đạt.** Dự đoán đúng ≥ 5/6 tình huống phân bổ, và số lần tái cân bằng giảm có số đo sau khi áp biện pháp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thêm thành viên vượt số phân vùng để tăng thông lượng · để việc nặng trong vòng lặp lấy dữ liệu · tăng thời hạn phiên mà không xét thời gian phát hiện chết · bỏ qua số bản ghi bị xử lý lại sau tái cân bằng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/215-consumer-the-poll-loop-group-assignment-and-rebalance.md`
- Nội dung học thuật: `note.md` cùng thư mục.
