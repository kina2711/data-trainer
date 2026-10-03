# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 248: Load Semantics Append Upsert Merge Replace and Swap

## Thực hành

**Nhiệm vụ.** Cài năm ngữ nghĩa cho cùng một tập dữ liệu. Chạy mỗi cái hai lần liên tiếp và so trạng thái đích sau lần một với sau lần hai. Tạo nguồn có hai bản ghi cùng khoá và quan sát hành vi của ghi đè cùng trộn. Lập bảng năm hàng gồm điều kiện đúng, hành vi chạy lại và chi phí đo được.

Chỉ chạy trên fixture/sandbox được phép. Lưu versions, inputs, state trước–sau, kill points, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và phạm vi bảo đảm.
2. Chỉ ra một failure window.
3. Phân biệt expected result với evidence đã chạy.
4. Đưa counterexample làm thiết kế thất bại.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là chạy lại hai lần cho cùng trạng thái. Kiểm bằng phép thử chạy lại; đạt khi bảng năm hàng có kết quả thực nghiệm và mọi ngữ nghĩa được tuyên bố luỹ đẳng đều qua phép thử chạy hai lần.

**Điều kiện đạt.** Bảng năm hàng có kết quả thực nghiệm, và mọi ngữ nghĩa tuyên bố luỹ đẳng đều cho trạng thái đích giống nhau sau hai lần chạy.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng thêm mới rồi khử trùng ở bước sau mà không có quy tắc chọn thắng · ghi đè theo khoá không thật sự duy nhất · trộn mà không xác định bản ghi thắng · cho rằng nạp thành công là luỹ đẳng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/136-load-semantics-append-upsert-merge-replace-swap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
