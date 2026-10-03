# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 422: AI-assisted engineering with verification

## Thực hành

**Nhiệm vụ.** Chọn ba nhiệm vụ lập trình có tiêu chí rõ. Với mỗi cái, viết đặc tả gồm giao diện, ràng buộc và kiểm thử trước khi yêu cầu sinh mã. Chạy kiểm thử, rà soát tĩnh và rà soát bảo mật. Ghi lại mọi chỗ mã sinh ra sai, gồm cả tham số hoặc thư viện không tồn tại. Đo hiệu năng và so với bản viết tay.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi kiểm chứng chứ tiêu thụ. Kiểm bằng ba nhiệm vụ; đạt khi mọi đoạn mã sinh ra đều qua kiểm thử cùng rà soát bảo mật trước khi hợp nhất, và ít nhất một lỗi trong mã sinh ra được phát hiện bằng kiểm thử.

**Điều kiện đạt.** Mọi đoạn mã sinh ra qua kiểm thử và rà soát bảo mật trước khi hợp nhất, và ≥ 1 lỗi trong mã sinh ra được kiểm thử phát hiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Hợp nhất mã sinh ra mà chưa có kiểm thử · dán nhật ký chứa bí mật vào công cụ · tin lời giải thích thay vì tái hiện lỗi · dùng tham số công cụ đề xuất mà không tra tài liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/310-ai-assisted-engineering-with-verification.md`
- Nội dung học thuật: `note.md` cùng thư mục.
