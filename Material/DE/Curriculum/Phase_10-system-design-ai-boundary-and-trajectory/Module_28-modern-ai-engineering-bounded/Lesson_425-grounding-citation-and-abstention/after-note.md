# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 425: Grounding, citation and abstention

## Thực hành

**Nhiệm vụ.** Xây tập đối chứng gồm câu hỏi có đáp án, câu hỏi không có đáp án trong tài liệu, và câu hỏi có hai tài liệu mâu thuẫn. Cài trích dẫn ở mức đoạn và kiểm trích dẫn bằng máy. Cài cơ chế từ chối có ngưỡng. Đo tỉ lệ trích dẫn bịa, tỉ lệ từ chối đúng và tỉ lệ từ chối nhầm. Áp chính sách cho tài liệu mâu thuẫn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có một tiêu chí nghiệm thu nhị phân về tính trung thực. Kiểm bằng tập đối chứng có tài liệu mâu thuẫn và câu hỏi không có đáp án; đạt khi không trích dẫn bịa nào lọt và tỉ lệ từ chối đúng trên nhóm câu không có đáp án vượt ngưỡng.

**Điều kiện đạt.** Không trích dẫn bịa nào lọt qua phép kiểm máy, tỉ lệ từ chối đúng vượt ngưỡng trên nhóm không có đáp án, và tài liệu mâu thuẫn được trình bày kèm phiên bản.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Trích dẫn ở mức tài liệu · không kiểm trích dẫn bằng máy · coi từ chối là thất bại rồi ép mô hình luôn trả lời · chọn một tài liệu khi có mâu thuẫn mà không nói.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/313-grounding-citation-and-abstention.md`
- Nội dung học thuật: `note.md` cùng thư mục.
