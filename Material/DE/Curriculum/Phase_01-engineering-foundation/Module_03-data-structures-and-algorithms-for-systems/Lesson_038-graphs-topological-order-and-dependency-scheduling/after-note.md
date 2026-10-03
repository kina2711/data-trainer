# Phase 1: Engineering Foundation
# Module 3: Data Structures and Algorithms for Systems
# Lesson 38: Graphs, topological order and dependency scheduling

## Thực hành

**Nhiệm vụ.** Cài bộ thực thi nhận một đồ thị nhiệm vụ. Chạy trên ba đồ thị: một chuỗi thẳng, một đồ thị có nhánh song song, và một đồ thị có chu trình. Chứng minh thứ tự chạy hợp lệ bằng nhật ký, chu trình bị báo lỗi rõ ràng, và số nhiệm vụ chạy đồng thời không vượt giới hạn. Thêm trạng thái thử lại cho nhiệm vụ hỏng.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Objective đòi ghép sắp thứ tự tô pô với giới hạn đồng thời ở lesson 29 thành một bộ thực thi. Kiểm bằng ba đồ thị thử trong đó một có chu trình; đạt khi thứ tự chạy hợp lệ, chu trình bị phát hiện, và giới hạn đồng thời được tôn trọng.

**Điều kiện đạt.** Thứ tự chạy hợp lệ trên cả ba đồ thị, chu trình bị báo lỗi rõ, và số nhiệm vụ đồng thời không vượt giới hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không phát hiện chu trình nên chạy vô hạn · chạy song song không giới hạn · bắt đầu một nhiệm vụ khi phụ thuộc chưa xong · không giữ trạng thái nên chạy lại từ đầu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/038-graphs-topological-order-dependency-scheduling.md`
- Nội dung học thuật: `note.md` cùng thư mục.
