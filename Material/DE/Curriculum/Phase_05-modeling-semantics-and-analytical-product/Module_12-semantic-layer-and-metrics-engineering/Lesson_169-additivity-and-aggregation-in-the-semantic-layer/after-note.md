# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 169: Additivity and Aggregation in the Semantic Layer

## Thực hành

**Nhiệm vụ.** Khai báo mười độ đo gồm cả cộng được, bán cộng và không cộng được. Viết năm truy vấn cố ý cộng sai và chứng minh tầng ngữ nghĩa từ chối hoặc xử lý đúng. Viết năm truy vấn hợp lệ và chứng minh không cái nào bị chặn nhầm. Đo chi phí của một chỉ số đếm giá trị phân biệt ở ba mức.

Chỉ chạy metric fixtures, graph validation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa metric production, BI definitions hay calendar dùng chung để minh họa. Lưu input, version, cutoff, query/compiled SQL, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu population, grain, time và aggregation contract.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra phần khái niệm ổn định và phần phụ thuộc phiên bản sản phẩm.
4. Đề xuất phép kiểm tái chạy được cùng valid control.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu bằng phép thử phủ định. Kiểm bằng năm truy vấn cộng sai; đạt khi cả năm bị từ chối hoặc trả về đúng, và không truy vấn hợp lệ nào bị chặn nhầm.

**Điều kiện đạt.** Năm truy vấn cộng sai đều bị chặn hoặc xử lý đúng, năm truy vấn hợp lệ đều chạy, và có số đo chi phí của chỉ số đếm phân biệt.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Khai báo phép gộp mặc định là cộng cho mọi độ đo · dùng bảng tổng hợp tính sẵn cho chỉ số không cộng được · chặn quá tay nên truy vấn hợp lệ cũng bị từ chối.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/57-additivity-aggregation-semantic-layer.md`
- Nội dung học thuật: `note.md` cùng thư mục.
