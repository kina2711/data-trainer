# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 83: Timeout budgets, retries and connection pools

## Thực hành

**Nhiệm vụ.** Dựng tuyến ba tầng gọi nhau. Đặt hạn chờ độc lập mỗi tầng thử ba lần, đếm số lời gọi thật tới tầng cuối khi nó lỗi. Đặt lại theo ngân sách toàn tuyến và đếm lại. Mô phỏng nguồn trả byte rất chậm và chứng minh hạn tổng cắt đúng lúc. Làm cạn hồ kết nối và ghi triệu chứng.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có ràng buộc số học kiểm được bằng đếm lời gọi thật. Kiểm bằng thí nghiệm nguồn chậm; đạt khi tổng số lời gọi thật nằm trong ngân sách và không yêu cầu nào treo quá hạn tổng.

**Điều kiện đạt.** Tổng lời gọi thật nằm trong ngân sách đã đặt, hạn tổng cắt đúng với nguồn trả chậm, và mô tả đúng triệu chứng hồ cạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ đặt một hạn chờ chung · để thử lại độc lập từng tầng · không có hạn tổng · chẩn đoán hồ cạn thành mạng chậm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/083-timeout-budgets-retries-and-connection-pools.md`
- Nội dung học thuật: `note.md` cùng thư mục.
