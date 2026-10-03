# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 353: Nested parallelism and oversubscription

## Thực hành

**Nhiệm vụ.** Chạy một công việc có dùng thư viện gốc đa luồng. Đếm tổng số luồng thật trên một máy và so với số lõi. Đo băng thông bộ nhớ và tỉ lệ chuyển ngữ cảnh. Đặt giới hạn luồng cho thư viện gốc và chạy lại; đo thông lượng cùng thời gian phân vị 95 của tác vụ. Lập bảng bốn nguồn song song với giá trị hiện tại của từng nguồn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective nhắm vào một nguồn song song không xuất hiện trong cấu hình engine. Kiểm bằng cặp số đo; đạt khi tổng số luồng và số lõi được đo, và sau khi đặt giới hạn thì thông lượng tăng có số đo.

**Điều kiện đạt.** Tổng số luồng và số lõi được đo, và sau khi đặt giới hạn thì thông lượng tăng với thời gian phân vị 95 của tác vụ giảm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tăng số lõi mỗi tiến trình mà không biết thư viện gốc đang tạo bao nhiêu luồng · chỉ đếm song song ở tầng engine · kết luận thiếu tài nguyên khi nguyên nhân là tranh chấp · không đặt giới hạn luồng tường minh.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/241-nested-parallelism-and-oversubscription.md`
- Nội dung học thuật: `note.md` cùng thư mục.
