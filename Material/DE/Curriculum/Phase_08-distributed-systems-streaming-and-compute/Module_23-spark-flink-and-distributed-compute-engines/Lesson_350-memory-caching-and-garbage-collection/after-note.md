# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 350: Memory, caching and garbage collection

## Thực hành

**Nhiệm vụ.** Cho ba tình huống với số lần đọc lại khác nhau là một, ba và mười. Chạy có và không có lưu tạm ở từng tình huống; đo thời gian, mức tràn đĩa và thời gian thu dọn rác. Thử ba mức lưu tạm khác nhau cho tình huống đọc lại nhiều. Tạo một ca giữ quá nhiều đối tượng sống và quan sát thu dọn rác; giảm bằng biểu diễn ngoài vùng quản lý.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective chống lại phản xạ lưu tạm mọi thứ. Kiểm bằng ba tình huống đo song song; đạt khi quyết định đúng ở cả ba và ca lưu tạm sai được định lượng mức chậm thêm.

**Điều kiện đạt.** Quyết định lưu tạm đúng ở cả ba tình huống, và ca lưu tạm sai được định lượng mức chậm thêm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Lưu tạm mọi tập dữ liệu trung gian · lưu tạm tập dùng một lần · không giải phóng bộ nhớ lưu tạm · tăng bộ nhớ khi nguyên nhân là thu dọn rác.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/238-memory-caching-and-garbage-collection.md`
- Nội dung học thuật: `note.md` cùng thư mục.
