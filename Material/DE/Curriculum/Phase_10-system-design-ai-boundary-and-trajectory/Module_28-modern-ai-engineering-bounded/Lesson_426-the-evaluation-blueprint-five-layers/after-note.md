# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 426: The evaluation blueprint - five layers

## Thực hành

**Nhiệm vụ.** Dựng bộ đánh giá năm tầng trên tập đối chứng cố định. Chạy lấy đường cơ sở. Tiêm ba thay đổi: đổi cách chia đoạn, đổi câu lệnh nhắc, và đổi phiên bản mô hình. Với mỗi cái, chỉ ra tầng nào xuống điểm. Đặt ngưỡng chặn phát hành và xác nhận nó chặn đúng. Thêm một vòng rà soát người cho phần không đo được.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cửa chặn hồi quy có số đo theo tầng. Kiểm bằng ba thay đổi tiêm; đạt khi mỗi thay đổi làm đúng tầng tương ứng xuống điểm và bộ đánh giá chặn được bản phát hành.

**Điều kiện đạt.** Ba thay đổi tiêm làm đúng tầng tương ứng xuống điểm, và bộ đánh giá chặn được bản phát hành theo ngưỡng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử vài câu rồi kết luận · chỉ đo kết quả cuối nên không biết sửa tầng nào · đổi tập đối chứng mỗi lần đánh giá · bỏ tầng chi phí và độ trễ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/314-the-evaluation-blueprint-five-layers.md`
- Nội dung học thuật: `note.md` cùng thư mục.
