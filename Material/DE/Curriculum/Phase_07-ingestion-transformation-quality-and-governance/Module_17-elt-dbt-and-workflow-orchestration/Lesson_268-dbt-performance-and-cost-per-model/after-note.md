# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 268: dbt Performance and Cost per Model

## Thực hành

**Nhiệm vụ.** Vẽ đồ thị và xác định đường găng, đo thời gian của nó. Tăng số luồng qua bốn mức và vẽ quan hệ giữa số luồng với tổng thời gian cùng chi phí, chỉ ra điểm tăng luồng bắt đầu phản tác dụng. Chọn ba mô hình tốn nhất, đọc kế hoạch, tìm quét toàn bộ âm thầm và sửa. Đối soát kết quả trước sau.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi tách hai nguyên nhân chậm và chống việc tăng luồng theo phản xạ. Kiểm bằng cặp số đo trước sau; đạt khi đường găng ngắn lại và ba mô hình giảm chi phí với kế hoạch giải thích được, mà kết quả không đổi.

**Điều kiện đạt.** Đường găng ngắn lại có số đo, ba mô hình giảm chi phí với kế hoạch giải thích, và kết quả đối soát không đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tăng số luồng để chữa đồ thị có đường găng dài · tối ưu mô hình rẻ vì dễ · sửa mà không đối soát kết quả · không phát hiện quét toàn bộ trong mô hình tăng dần.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/156-dbt-performance-cost-per-model.md`
- Nội dung học thuật: `note.md` cùng thư mục.
