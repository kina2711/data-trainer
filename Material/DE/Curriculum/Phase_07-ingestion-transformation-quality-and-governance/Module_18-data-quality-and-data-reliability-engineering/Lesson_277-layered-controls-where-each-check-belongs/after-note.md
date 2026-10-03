# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 277: Layered controls - where each check belongs

## Thực hành

**Nhiệm vụ.** Cho 20 phép kiểm và năm tầng. Ánh xạ từng cái vào tầng rẻ nhất mà nó vẫn bắt được lỗi. Với ba phép kiểm phải đặt muộn, giải thích ngữ cảnh nào chỉ có ở tầng đó. Rà đường dẫn hiện có và tìm mọi chỗ dữ liệu bị bỏ im lặng, rồi chuyển sang cách ly có lý do.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt bản đồ cho tám bài thực hành sau. Kiểm bằng bài ánh xạ; đạt khi đặt đúng ít nhất 16 và ba ca không đặt sớm được có lý do dựa trên ngữ cảnh cần thiết.

**Điều kiện đạt.** Ánh xạ đúng ≥ 16/20 phép kiểm, ba ca đặt muộn có lý do dựa trên ngữ cảnh, và không còn chỗ nào bỏ dữ liệu im lặng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dồn mọi phép kiểm vào tầng phục vụ · bỏ bản ghi hỏng thay vì cách ly · kiểm bất biến nghiệp vụ ở vùng thô nơi chưa đủ ngữ cảnh · trộn dữ liệu cách ly với dữ liệu đã nhận.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/165-layered-controls-where-each-check-belongs.md`
- Nội dung học thuật: `note.md` cùng thư mục.
