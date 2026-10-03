# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 428: Prompt injection, tool permission and tenant isolation

## Thực hành

**Nhiệm vụ.** Dựng bộ 30 kịch bản đối kháng gồm tiêm chỉ dẫn qua tài liệu, cố lấy dữ liệu của khách hàng khác, và cố gọi công cụ ngoài quyền. Chạy trên hệ chưa có phòng thủ và đếm số kịch bản thành công. Thêm ba lớp phòng thủ và chạy lại. Chứng minh phòng thủ nằm ở mã chứ ở câu lệnh nhắc. Đặt giới hạn số bước gọi công cụ và ngân sách.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi đặt chốt kiểm soát đúng chỗ. Kiểm bằng bộ 30 kịch bản đối kháng; đạt khi mọi kịch bản rò rỉ dữ liệu hoặc vượt quyền bị chặn ở ranh giới công cụ, và không phòng thủ nào chỉ dựa trên câu lệnh nhắc.

**Điều kiện đạt.** Mọi kịch bản rò rỉ hoặc vượt quyền bị chặn ở ranh giới công cụ, không phòng thủ nào chỉ dựa vào câu lệnh nhắc, và vòng lặp gọi công cụ có giới hạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chặn tiêm chỉ dẫn bằng cách viết thêm vào câu lệnh nhắc · cho công cụ dùng quyền của dịch vụ thay vì của người dùng · không giới hạn số bước gọi công cụ · ghi cả nội dung nhạy cảm vào vết theo dõi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/316-prompt-injection-tool-permission-and-tenant-isolation.md`
- Nội dung học thuật: `note.md` cùng thư mục.
