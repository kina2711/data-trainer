# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 49: SIMD from lane to operator - width, mask, tail and gather

## Thực hành

**Nhiệm vụ.** Viết cùng một phép tính ở ba dạng: vô hướng, để trình biên dịch tự véctơ hoá, và dùng thư viện đã véctơ hoá. Đo thời gian cùng bộ đếm gồm số chu kỳ, số lệnh, lỗi bộ nhớ đệm và băng thông; tính số chu kỳ trên mỗi dòng. Chạy lại với ba biến thể dữ liệu: liền kề, rải rác cần thu thập, và nhiều giá trị rỗng. Quy mỗi lần tăng tốc thấp về một trong sáu chế độ hỏng.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi giải thích một con số chứ chỉ tạo ra nó. Kiểm bằng ba vòng lặp có đặc trưng khác nhau; đạt khi mỗi vòng lặp có số đo kèm bộ đếm phần cứng và mức tăng tốc thấp được quy đúng nguyên nhân ở ít nhất hai.

**Điều kiện đạt.** Ba dạng đều có số đo kèm bộ đếm phần cứng và số chu kỳ trên mỗi dòng, và ≥ 2 lần tăng tốc thấp được quy đúng chế độ hỏng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận từ một số đo thời gian duy nhất · dùng lô quá nhỏ rồi kết luận véctơ hoá vô dụng · so hai bản mà không kiểm kết quả giống nhau · viết mã đặc thù tập lệnh trước khi đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/049-simd-lane-operator-width-mask-tail-gather.md`
- Nội dung học thuật: `note.md` cùng thư mục.
