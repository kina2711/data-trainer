# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 301: Column lineage - why a parser cannot always prove it

## Thực hành

**Nhiệm vụ.** Chuẩn bị 15 câu lệnh đại diện gồm chọn toàn bộ cột, biểu thức bảng chung lồng nhau, hàm tự viết, câu lệnh sinh động, phép hợp và hàm cửa sổ. Chạy bộ phân tích và đối chiếu kết quả với dòng dõi đúng do người xác định. Đếm số cạnh đúng, số cạnh sai và số cạnh bị bỏ sót. Đánh dấu không rõ cho mọi ca không chứng minh được. Tìm một cột ảnh hưởng qua điều kiện lọc mà không nằm trong biểu thức đầu ra.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của công cụ và biểu diễn giới hạn đó. Kiểm bằng tập câu lệnh có ca khó; đạt khi mọi ca bộ phân tích chịu thua đều được đánh dấu không rõ và không ca nào bị vẽ thành cạnh sự thật.

**Điều kiện đạt.** Mọi ca bộ phân tích chịu thua được đánh dấu không rõ, không cạnh suy đoán nào được vẽ thành sự thật, và ca ảnh hưởng qua điều kiện lọc được tìm ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin kết quả bộ phân tích là đầy đủ · bỏ ca chọn toàn bộ cột vì khó · vẽ cạnh cho hàm tự viết theo phỏng đoán · bỏ qua ảnh hưởng qua điều kiện lọc.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/189-column-lineage-why-a-parser-cannot-always-prove-it.md`
- Nội dung học thuật: `note.md` cùng thư mục.
