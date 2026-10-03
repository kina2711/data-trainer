# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 402: Supply chain and the secure delivery pipeline

## Thực hành

**Nhiệm vụ.** Dựng bốn chốt trong quy trình. Tiêm bốn vi phạm và xác nhận bị chặn ở đúng chốt. Giới hạn danh tính của quy trình theo nhánh và môi trường; mở một yêu cầu hợp nhất từ một nhánh không tin cậy và chứng minh nó không lấy được quyền triển khai. Với một lỗ hổng giả định mới công bố, dùng bản kê thành phần trả lời trong bao lâu mình đang chạy nó ở đâu.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm cả bảo vệ chính quy trình tự động. Kiểm bằng bốn vi phạm tiêm cộng một phép thử nâng quyền; đạt khi bốn vi phạm bị chặn và yêu cầu hợp nhất từ nguồn không tin cậy không chạm được vào quyền triển khai.

**Điều kiện đạt.** Bốn vi phạm bị chặn ở đúng chốt, yêu cầu hợp nhất từ nguồn không tin cậy không chạm được quyền triển khai, và câu hỏi về lỗ hổng mới trả lời được từ bản kê thành phần.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cho quy trình tự động quyền triển khai rộng · chạy mã của yêu cầu hợp nhất từ nguồn không tin cậy với bí mật · không quét bí mật trong nhật ký quy trình · không có bản kê thành phần nên không biết mình chạy gì.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/290-supply-chain-and-the-secure-delivery-pipeline.md`
- Nội dung học thuật: `note.md` cùng thư mục.
