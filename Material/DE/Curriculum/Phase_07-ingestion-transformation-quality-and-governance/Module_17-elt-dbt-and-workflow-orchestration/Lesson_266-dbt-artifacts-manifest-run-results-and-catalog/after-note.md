# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 266: dbt Artifacts Manifest Run Results and Catalog

## Thực hành

**Nhiệm vụ.** Chạy dự án và thu ba hiện vật. Trả lời năm câu hỏi chỉ bằng chúng: mô hình nào chậm nhất, mô hình nào đổi so với lần chạy trước, mô hình nào không ai dùng, phép kiểm nào cảnh báo mà không chặn, và một nút báo thành công thì điều đó chứng minh gì về dữ liệu. Thiết lập nơi lưu hiện vật của lần chạy sản xuất.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi lấy bằng chứng từ hiện vật thay vì từ giao diện. Kiểm bằng năm câu hỏi; đạt khi trả lời đúng ít nhất bốn chỉ bằng ba tệp hiện vật.

**Điều kiện đạt.** Trả lời đúng ≥ 4/5 câu hỏi chỉ bằng ba hiện vật, và nơi lưu hiện vật sản xuất được thiết lập kèm chính sách giữ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc trạng thái từ giao diện thay vì hiện vật · coi mọi nút xanh là dữ liệu đúng · không lưu hiện vật sản xuất nên không so sánh trạng thái được · tin tệp danh mục luôn cập nhật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/154-dbt-artifacts-manifest-run-results-catalog.md`
- Nội dung học thuật: `note.md` cùng thư mục.
