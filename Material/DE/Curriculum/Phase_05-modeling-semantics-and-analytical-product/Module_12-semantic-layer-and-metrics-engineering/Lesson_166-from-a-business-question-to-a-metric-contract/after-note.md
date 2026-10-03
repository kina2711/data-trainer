# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 166: From a Business Question to a Metric Contract

## Thực hành

**Nhiệm vụ.** Nhận ba câu hỏi nghiệp vụ mơ hồ. Với câu thứ nhất, liệt kê tám cách hiểu đều hợp lệ và con số tương ứng. Viết hợp đồng sáu phần cho cả ba. Đưa hợp đồng cho một học viên khác; hai người cài độc lập và so ba cặp con số.

Chỉ chạy metric fixtures, graph validation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa metric production, BI definitions hay calendar dùng chung để minh họa. Lưu input, version, cutoff, query/compiled SQL, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu population, grain, time và aggregation contract.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra phần khái niệm ổn định và phần phụ thuộc phiên bản sản phẩm.
4. Đề xuất phép kiểm tái chạy được cùng valid control.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có phép kiểm chứng khách quan bằng hai bản cài độc lập. Kiểm bằng phép thử hai người; đạt khi ba chỉ số đều cho hai con số khớp tuyệt đối giữa hai người cài độc lập.

**Điều kiện đạt.** Ba cặp con số từ hai người cài độc lập đều khớp tuyệt đối, và tám cách hiểu của câu đầu được liệt kê đủ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ phần tập hợp nên không rõ loại trừ gì · không nêu mốc thời gian dùng để quy kỳ · để bộ lọc trong định nghĩa lẫn với bộ lọc người dùng chọn · không có chủ sở hữu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/54-business-question-to-metric-contract.md`
- Nội dung học thuật: `note.md` cùng thư mục.
