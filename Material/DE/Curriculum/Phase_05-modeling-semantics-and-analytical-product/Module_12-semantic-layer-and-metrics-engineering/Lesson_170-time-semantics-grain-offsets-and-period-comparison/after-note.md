# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 170: Time Semantics - Grain, Offsets and Period Comparison

## Thực hành

**Nhiệm vụ.** Với một bộ ba chỉ số, chốt bốn quyết định thời gian và ghi vào hợp đồng. Dựng bảng lịch đầy đủ có kỳ tài chính. Tính so kỳ trước và cùng kỳ năm trước bằng ba cách dịch chuyển, trên dữ liệu cố ý thiếu ba tháng và bắc qua năm nhuận. Đối soát với bản tính tay.

Chỉ chạy metric fixtures, graph validation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa metric production, BI definitions hay calendar dùng chung để minh họa. Lưu input, version, cutoff, query/compiled SQL, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu population, grain, time và aggregation contract.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra phần khái niệm ổn định và phần phụ thuộc phiên bản sản phẩm.
4. Đề xuất phép kiểm tái chạy được cùng valid control.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có hai ca biên cụ thể mà bản làm ẩu luôn sai. Kiểm bằng đối soát ở ca biên; đạt khi kết quả khớp bản tính tay ở cả tháng thiếu dữ liệu lẫn ngày 29 tháng 2.

**Điều kiện đạt.** Kết quả khớp bản tính tay ở cả tháng thiếu dữ liệu lẫn năm nhuận, và bốn quyết định thời gian có trong hợp đồng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không chốt mốc thời gian dùng để quy kỳ · bỏ qua múi giờ · không dựng bảng lịch nên kỳ rỗng biến mất · dùng một cách dịch kỳ cho mọi chỉ số mà không hỏi nghiệp vụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/58-time-semantics-grain-offsets-period-comparison.md`
- Nội dung học thuật: `note.md` cùng thư mục.
