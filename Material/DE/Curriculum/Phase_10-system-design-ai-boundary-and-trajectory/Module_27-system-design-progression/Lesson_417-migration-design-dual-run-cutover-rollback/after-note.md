# Phase 10: System Design, AI Boundary and Trajectory
# Module 27: System Design Progression
# Lesson 417: Migration design - dual run, cutover, rollback

## Thực hành

**Nhiệm vụ.** Lập kế hoạch di trú cho một thay đổi kiến trúc thật. Kiểm kê bên tiêu thụ bằng khai báo cộng nhật ký truy vấn. Thiết kế giai đoạn chạy song song kèm tiêu chí đối soát để chuyển sang giai đoạn sau. Chia chuyển đổi theo từng phần. Diễn tập quay lui ở một môi trường thử. Tính thời hạn giữ hệ cũ từ thời gian phát hiện vấn đề.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là bằng chứng từ giai đoạn chạy song song. Kiểm bằng rà soát kế hoạch cộng một lần diễn tập; đạt khi kiểm kê bên tiêu thụ đầy đủ, đối soát chạy song song có tiêu chí đạt, và quay lui được diễn tập.

**Điều kiện đạt.** Kiểm kê bên tiêu thụ đầy đủ, đối soát chạy song song có tiêu chí đạt, quay lui diễn tập thành công, và thời hạn giữ hệ cũ có căn cứ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chuyển đổi toàn bộ một lần · bỏ giai đoạn chạy song song vì tốn gấp đôi · gỡ hệ cũ theo lịch thay vì theo kiểm kê · không diễn tập quay lui.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/305-migration-design-dual-run-cutover-rollback.md`
- Nội dung học thuật: `note.md` cùng thư mục.
