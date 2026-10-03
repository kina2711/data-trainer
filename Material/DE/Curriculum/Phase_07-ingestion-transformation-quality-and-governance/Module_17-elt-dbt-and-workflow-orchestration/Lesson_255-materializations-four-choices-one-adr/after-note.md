# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 255: Materializations Four Choices One ADR

## Thực hành

**Nhiệm vụ.** Chạy cùng một mô hình với cả bốn cách hiện thực hoá. Đo chi phí dựng, chi phí truy vấn và dung lượng cho từng cách. Đánh giá mức dễ gỡ lỗi bằng cách thử truy vấn kết quả trung gian. Lập bảng bốn nhân bốn. Viết bản ghi quyết định nêu ngưỡng khối lượng dữ liệu mà lựa chọn đổi.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo số đo và chống việc mặc định dùng tăng dần. Kiểm bằng bảng bốn cách nhân bốn chiều; đạt khi ba chiều đầu có số đo thật và lựa chọn kèm ngưỡng chuyển đổi.

**Điều kiện đạt.** Bảng bốn nhân bốn có số đo ở ba chiều đầu, và bản ghi quyết định nêu ngưỡng khối lượng làm lựa chọn đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Mặc định dùng tăng dần từ đầu · dùng dạng phù du cho mô hình cần gỡ lỗi · chọn khung nhìn cho mô hình được truy vấn rất nhiều lần · so bốn cách mà không đo dung lượng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/143-materializations-four-choices-one-adr.md`
- Nội dung học thuật: `note.md` cùng thư mục.
