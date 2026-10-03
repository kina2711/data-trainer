# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 252: Backfill Plan Isolate Validate Promote

## Thực hành

**Nhiệm vụ.** Lập kế hoạch nạp bù 90 phân vùng gồm ước lượng chi phí, ngưỡng dừng và trần chi phí. Chạy vào đích cách ly, đồng thời với lần chạy hằng ngày. Đối soát đích cách ly với nguồn. Thăng cấp bằng hoán đổi nguyên tử rồi thực hiện quay lại. So kết quả nạp bù với kết quả lịch sử và giải thích mọi chênh lệch do mã đổi.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là cam kết hằng ngày không vỡ và đối soát đạt trước khi thăng cấp. Kiểm bằng thí nghiệm nạp bù đầy đủ; đạt khi độ tươi hằng ngày trong cam kết, đối soát đạt ở đích cách ly, và quay lại được sau khi thăng cấp.

**Điều kiện đạt.** Độ tươi hằng ngày trong cam kết suốt nạp bù, đối soát đạt ở đích cách ly trước khi thăng cấp, và quay lại thực hiện được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nạp bù thẳng vào bảng phục vụ · không có trần chi phí nên hoá đơn vượt dự kiến · thăng cấp trước khi đối soát · coi kết quả nạp bù bằng kết quả lịch sử mà không kiểm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/140-backfill-plan-isolate-validate-promote.md`
- Nội dung học thuật: `note.md` cùng thư mục.
