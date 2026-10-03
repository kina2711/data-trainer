# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 27: End-to-end deadlines and backpressure

## Thực hành

**Nhiệm vụ.** Dựng dịch vụ ba chặng, mỗi chặng gọi một phụ thuộc có thể chậm. Cài bản chỉ có hết giờ cục bộ cộng thử lại, chạy tải với một chặng chậm, và đo phân vị 99. Cài bản truyền hạn chót và đo lại. Thêm hàng đợi có giới hạn cùng bể kết nối có giới hạn, chọn tường minh hành vi khi đầy. Tạo một đoạn giữ kết nối qua điểm chờ dài và quan sát bể cạn.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có hai tiêu chí nghiệm thu đo được dưới tải. Kiểm bằng phép thử tải có chặng chậm; đạt khi phân vị 99 của thời gian yêu cầu nằm trong ngân sách và không lần nào bể kết nối cạn.

**Điều kiện đạt.** Phân vị 99 của thời gian yêu cầu nằm trong ngân sách hạn chót, và không lần nào bể kết nối cạn dưới tải.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ đặt hết giờ cục bộ rồi tin yêu cầu có giới hạn · thử lại ở mọi chặng mà không có ngân sách chung · để hàng đợi không giới hạn · giữ kết nối qua một điểm chờ dài.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/027-end-to-end-deadlines-backpressure.md`
- Nội dung học thuật: `note.md` cùng thư mục.
