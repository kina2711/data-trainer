# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 284: The reconciliation ladder - seven levels

## Thực hành

**Nhiệm vụ.** Dựng bộ đối soát chạy bảy bậc tại bốn chốt. Tiêm ba lỗi ở ba đoạn: mất dữ liệu khi nạp, nhân dòng khi biến đổi, và lệch làm tròn ở tầng phục vụ. Với mỗi lỗi, chỉ ra bậc nào và chốt nào phát hiện, rồi quy về đoạn gây ra. Viết một tuyên bố đối soát nêu rõ tổng thể, cửa sổ, phép kiểm và dung sai.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi định vị chênh lệch chứ chỉ phát hiện. Kiểm bằng ba lỗi tiêm ở ba đoạn khác nhau; đạt khi cả ba được quy đúng đoạn và mọi tuyên bố đối soát nêu đủ bốn yếu tố phạm vi.

**Điều kiện đạt.** Ba lỗi tiêm được quy đúng đoạn gây ra, và tuyên bố đối soát nêu đủ tổng thể, cửa sổ, phép kiểm và dung sai.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chỉ đối soát hai đầu nên không biết chênh lệch sinh ở đâu · đối soát bằng lấy mẫu rồi tuyên bố đầy đủ · bỏ bậc bảy nên người dùng thấy sai mà hệ báo xanh · đối soát hai bên ở hai thời điểm khác nhau.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/172-the-reconciliation-ladder-seven-levels.md`
- Nội dung học thuật: `note.md` cùng thư mục.
