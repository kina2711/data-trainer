# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 168: Metric Types - Simple, Ratio, Derived and Cumulative

## Thực hành

**Nhiệm vụ.** Phân loại mười chỉ số thật vào bốn nhóm. Cài một chỉ số tỉ lệ theo hai cách: lưu sẵn tỉ lệ, và lưu tử mẫu riêng. Gộp lên ba mức khác nhau và so hai bộ kết quả với bản tính tay. Cài một chỉ số tích luỹ và kiểm ở kỳ không có dữ liệu.

Chỉ chạy metric fixtures, graph validation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa metric production, BI definitions hay calendar dùng chung để minh họa. Lưu input, version, cutoff, query/compiled SQL, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu population, grain, time và aggregation contract.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra phần khái niệm ổn định và phần phụ thuộc phiên bản sản phẩm.
4. Đề xuất phép kiểm tái chạy được cùng valid control.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra lỗi không báo lỗi, nên bắt buộc chứng minh bằng đối chứng. Kiểm bằng bài phân loại cộng đối chứng số; đạt khi phân đúng ít nhất tám trong mười và định lượng được sai lệch của cách cài sai.

**Điều kiện đạt.** Phân đúng ≥ 8/10 chỉ số, và sai lệch của cách lưu sẵn tỉ lệ được định lượng ở cả ba mức gộp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Lưu sẵn tỉ lệ trong bảng · chỉ số phái sinh không kế thừa ràng buộc gộp · chỉ số tích luỹ không dựng trên bảng lịch đầy đủ · kiểm chỉ ở mức đã tính sẵn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/56-metric-types-simple-ratio-derived-cumulative.md`
- Nội dung học thuật: `note.md` cùng thư mục.
