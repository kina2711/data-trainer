# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 167: The Semantic Graph - Entities, Dimensions, Measures and Metrics

## Thực hành

**Nhiệm vụ.** Từ lược đồ mart đã dựng ở M11, vẽ đồ thị ngữ nghĩa với bốn loại nút và cạnh có bản số. Chỉ ra mọi cặp thực thể có nhiều hơn một đường kết. Với mỗi cặp đó, viết hai câu hỏi nghiệp vụ mà hai đường cho hai câu trả lời khác nhau.

Chỉ chạy metric fixtures, graph validation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa metric production, BI definitions hay calendar dùng chung để minh họa. Lưu input, version, cutoff, query/compiled SQL, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu population, grain, time và aggregation contract.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra phần khái niệm ổn định và phần phụ thuộc phiên bản sản phẩm.
4. Đề xuất phép kiểm tái chạy được cùng valid control.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho ba bài về tính đúng của phép kết. Kiểm bằng bài vẽ cộng nhận dạng; đạt khi đồ thị đủ bốn loại nút và chỉ ra đúng ít nhất một cặp thực thể có nhiều đường kết.

**Điều kiện đạt.** Đồ thị đủ bốn loại nút và cạnh có bản số, và chỉ ra được ít nhất một cặp có nhiều đường kèm hai câu hỏi cho hai kết quả.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chép sơ đồ bảng thành đồ thị ngữ nghĩa · nhầm độ đo với chỉ số · bỏ bản số trên cạnh · giả định luôn chỉ có một đường kết.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/55-semantic-graph-entities-dimensions-measures-metrics.md`
- Nội dung học thuật: `note.md` cùng thư mục.
