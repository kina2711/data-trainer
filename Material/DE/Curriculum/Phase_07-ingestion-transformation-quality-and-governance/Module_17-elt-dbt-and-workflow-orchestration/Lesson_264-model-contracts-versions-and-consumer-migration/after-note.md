# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 264: Model Contracts Versions and Consumer Migration

## Thực hành

**Nhiệm vụ.** Khai báo hợp đồng cho ba mô hình phục vụ và chứng minh lần xây dựng hỏng khi mô hình sai hợp đồng. Kiểm kê bên tiêu thụ bằng khai báo cộng nhật ký truy vấn. Thực hiện một lần đổi tên cột theo quy trình có phiên bản với hai bên tiêu thụ chạy thật. Gỡ phiên bản cũ sau khi kiểm kê rỗng. Thực hiện một lần quay lại.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là không bên tiêu thụ nào hỏng suốt quá trình. Kiểm bằng thí nghiệm chuyển đổi có bên tiêu thụ chạy thật; đạt khi không bên nào lỗi và phiên bản cũ chỉ bị gỡ sau khi kiểm kê rỗng.

**Điều kiện đạt.** Không bên tiêu thụ nào lỗi suốt quá trình, phiên bản cũ chỉ gỡ sau khi kiểm kê rỗng, và đường quay lại thực hiện được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đổi cột rồi báo bên tiêu thụ sau · gỡ phiên bản cũ theo lịch thay vì theo kiểm kê · không khai báo hợp đồng nên dữ liệu sai chảy xuống hạ nguồn · không có đường quay lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/152-model-contracts-versions-consumer-migration.md`
- Nội dung học thuật: `note.md` cùng thư mục.
