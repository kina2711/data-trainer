# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 263: Snapshots and SCD2 Invariants

## Thực hành

**Nhiệm vụ.** Cài ghi lịch sử cho một bảng nguồn bằng cả hai chiến lược phát hiện. Chạy 500 lần cập nhật gồm cả hiệu chỉnh tới muộn. Kiểm ba bất biến sau mỗi chu kỳ. Tạo một kịch bản có hai thay đổi giữa hai lần chạy và đếm số thay đổi bị bỏ sót. Chọn tường minh hành vi khi bản ghi biến mất khỏi nguồn.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có ba bất biến kiểm được cộng một giới hạn phải nhận ra. Kiểm bằng ba phép kiểm bất biến cộng thí nghiệm bỏ sót; đạt khi ba bất biến giữ qua 500 lần cập nhật và ca bỏ sót được định lượng.

**Điều kiện đạt.** Ba bất biến giữ qua 500 lần cập nhật, và số thay đổi bị bỏ sót giữa hai lần chạy được định lượng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Để hành vi khi bản ghi biến mất theo giá trị mặc định · dùng chiến lược theo dấu thời gian khi trường đó không tin cậy · không kiểm bất biến chồng lấn · coi cơ chế này thay được bắt thay đổi từ nhật ký.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/151-snapshots-scd2-invariants.md`
- Nội dung học thuật: `note.md` cùng thư mục.
