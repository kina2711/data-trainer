# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 367: Reliability - failure domains, RPO and RTO with a tested restore

## Thực hành

**Nhiệm vụ.** Đặt mục tiêu hai con số cho một dịch vụ. Tạo sao lưu và phục hồi vào một tài khoản hoặc dự án sạch; bấm giờ và đối soát dữ liệu. Kiểm ba nguyên nhân thất bại bằng cách thử phục hồi khi thiếu quyền và khi thiếu khoá. Mất một khu khả dụng có kiểm soát và đo lại. Kiểm hạn mức còn đủ để tạo tài nguyên thay thế.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là số đo từ một lần phục hồi thật, không phải một kế hoạch. Kiểm bằng diễn tập phục hồi; đạt khi hai con số đo được, dữ liệu sau phục hồi đối soát khớp, và ba nguyên nhân thất bại được kiểm tường minh.

**Điều kiện đạt.** Hai con số phục hồi đo được từ một lần phục hồi thật vào môi trường sạch, dữ liệu đối soát khớp, và ba nguyên nhân thất bại được kiểm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi có lịch sao lưu là có khả năng phục hồi · phục hồi vào chính môi trường cũ nên không kiểm được phụ thuộc · để sao lưu cùng tài khoản với dữ liệu gốc · bỏ qua hạn mức khi lập kế hoạch phục hồi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/255-reliability-failure-domains-rpo-and-rto-with-a-tested-restore.md`
- Nội dung học thuật: `note.md` cùng thư mục.
