# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 260: Incremental Strategies by Adapter

## Thực hành

**Nhiệm vụ.** Cài cùng một mô hình với ba chiến lược khác nhau. Với mỗi cái, xuất câu lệnh sinh ra và mô tả chính xác nó làm gì ở đích. Đo chi phí và thời gian. Tạo nguồn có hai bản ghi cùng khoá và quan sát bản nào thắng ở từng chiến lược. Kiểm tính nguyên tử của từng chiến lược bằng phép đọc song song theo lesson 249.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi kiểm chứng hành vi công cụ thay vì tin tên gọi. Kiểm bằng bài đọc câu lệnh sinh ra; đạt khi ba chiến lược được đối chiếu với câu lệnh thật và chi phí đo được cho từng cái.

**Điều kiện đạt.** Ba chiến lược được đối chiếu với câu lệnh sinh ra, có số đo chi phí, và bản ghi thắng ở mỗi chiến lược được xác định.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn chiến lược theo tên mà không đọc câu lệnh sinh ra · dùng thêm mới đơn thuần cho nguồn có sửa · trộn theo khoá không duy nhất · giả định mọi chiến lược đều nguyên tử.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/148-incremental-strategies-by-adapter.md`
- Nội dung học thuật: `note.md` cùng thư mục.
