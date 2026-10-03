# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 281: Metamorphic and property tests for pipelines

## Thực hành

**Nhiệm vụ.** Viết bốn phép kiểm biến hình cho một mô hình phục vụ. Viết thêm một phép kiểm theo tính chất sinh 1.000 trường hợp có ràng buộc. Giảng viên sửa một dòng logic biến đổi sao cho kết quả vẫn hợp lệ nhưng sai; chạy toàn bộ phép kiểm và xác định quan hệ nào bắt được. Đo thời gian chạy của nhóm này và đặt lịch phù hợp.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective nhắm vào loại lỗi mà mọi phép kiểm giá trị đều bỏ qua. Kiểm bằng lỗi logic tiêm; đạt khi bốn quan hệ chạy tự động và lỗi tiêm bị ít nhất một quan hệ phát hiện.

**Điều kiện đạt.** Bốn quan hệ chạy tự động, lỗi logic thầm lặng bị ít nhất một quan hệ phát hiện, và nhóm này có lịch chạy phù hợp thời gian đo được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ kiểm bằng giá trị kỳ vọng cố định · bỏ quan hệ chia rồi gộp vì nghĩ hiển nhiên đúng · sinh dữ liệu ngẫu nhiên không ràng buộc nên toàn ca vô nghĩa · chạy nhóm này ở mỗi lần nộp mã dù nó chậm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/169-metamorphic-and-property-tests-for-pipelines.md`
- Nội dung học thuật: `note.md` cùng thư mục.
