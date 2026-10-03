# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 279: Row, aggregate and relationship tests

## Thực hành

**Nhiệm vụ.** Cài đủ ba nhóm cho một mô hình phục vụ. Tiêm một phép kết nhân dòng và một phân vùng thiếu. Chứng minh kiểm theo dòng vẫn xanh ở cả hai. Thêm đối soát tổng và kiểm độ đầy đủ theo phân vùng kỳ vọng, rồi xác nhận bắt được. Lập bảng ánh xạ loại lỗi với nhóm phép kiểm bắt được nó.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của nhóm phép kiểm quen dùng nhất. Kiểm bằng hai lỗi tiêm; đạt khi cả hai lọt qua kiểm theo dòng, bị nhóm khác bắt, và độ phủ được ánh xạ theo loại lỗi chứ theo số lượng.

**Điều kiện đạt.** Hai lỗi tiêm lọt qua kiểm theo dòng và bị hai nhóm còn lại bắt, và bảng ánh xạ loại lỗi với nhóm phép kiểm đầy đủ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi số lượng phép kiểm là độ phủ · chỉ kiểm theo dòng rồi kết luận dữ liệu sạch · không kiểm phân vùng kỳ vọng nên phân vùng thiếu không ai biết · kiểm quan hệ mà bỏ chiều bản số.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/167-row-aggregate-and-relationship-tests.md`
- Nội dung học thuật: `note.md` cùng thư mục.
