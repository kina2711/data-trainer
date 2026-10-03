# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 285: Normalization before comparison

## Thực hành

**Nhiệm vụ.** Đối soát hai hệ khi chưa chuẩn hoá và đếm số chênh lệch. Phân loại từng chênh lệch vào bảy nhóm. Viết một thư viện chuẩn hoá dùng chung cho cả hai phía. Đối soát lại và chứng minh số chênh lệch giả về không. Với mỗi chênh lệch còn lại, nêu nguyên nhân thật. Đưa thư viện chuẩn hoá vào bộ kiểm để nó không lệch giữa hai phía.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi tách chênh lệch giả khỏi chênh lệch thật. Kiểm bằng phép đối soát trước và sau chuẩn hoá; đạt khi số chênh lệch giả về không và mọi chênh lệch còn lại được nêu tên nguyên nhân.

**Điều kiện đạt.** Số chênh lệch giả về không sau khi chuẩn hoá, mọi chênh lệch còn lại có nguyên nhân nêu tên, và thư viện chuẩn hoá dùng chung cho hai phía.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Mỗi bên tự viết quy tắc chuẩn hoá · băm trực tiếp trên giá trị thô · coi chênh lệch nhỏ là chấp nhận được mà không tìm nguyên nhân · bỏ nhóm thời điểm tham chiếu khi so dữ liệu có lịch sử.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/173-normalization-before-comparison.md`
- Nội dung học thuật: `note.md` cùng thư mục.
