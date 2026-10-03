# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 423: The LLM API contract - structured output, tools, budgets

## Thực hành

**Nhiệm vụ.** Cài lớp gọi có kiểm lược đồ đầu ra, thử lại có giới hạn, ngân sách đơn vị mã hoá và giới hạn đồng thời. Tiêm ba chế độ hỏng: hết giờ, vượt hạn mức, và đầu ra sai lược đồ. Chứng minh không đầu ra sai nào lọt xuống hạ nguồn. Đặt câu lệnh nhắc và cấu hình vào kho mã có phiên bản. Kiểm phương án dự phòng khi mô hình chính không dùng được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là hệ vẫn đúng dưới lỗi của bên ngoài. Kiểm bằng ba chế độ hỏng tiêm; đạt khi cả ba được xử lý không sập, đầu ra sai lược đồ không lọt xuống hạ nguồn, và ngân sách không bị vượt.

**Điều kiện đạt.** Ba chế độ hỏng được xử lý không sập, không đầu ra sai lược đồ nào lọt hạ nguồn, ngân sách không bị vượt, và dự phòng hoạt động.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân tích đầu ra bằng cách tìm chuỗi thay vì kiểm lược đồ · thử lại mọi lỗi · không ghim phiên bản mô hình · để câu lệnh nhắc nằm ngoài kho mã.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/311-the-llm-api-contract-structured-output-tools-budgets.md`
- Nội dung học thuật: `note.md` cùng thư mục.
