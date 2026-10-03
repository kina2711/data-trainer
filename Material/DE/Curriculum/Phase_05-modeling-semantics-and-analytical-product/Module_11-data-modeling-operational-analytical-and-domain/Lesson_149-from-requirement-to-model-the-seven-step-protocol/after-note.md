# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 149: From requirement to model - the seven-step protocol

## Thực hành

**Nhiệm vụ.** Cho ba mô tả nghiệp vụ. Với mỗi cái, chạy đủ bảy bước và nộp kết quả từng bước. Đổi bài: người khác đọc phát biểu hạt của bạn và viết lại bằng lời của họ; nếu hai bản khác nghĩa thì phát biểu còn mơ hồ và phải sửa.

Chỉ chạy backup/restore, fault injection, lock workload hoặc schema experiment trong môi trường cô lập có dữ liệu giả và đường xoá/khôi phục rõ. Không restore đè, đổi retention, kill process hoặc chạy destructive command trên production. Lưu exact version, config, script, raw log, operation ledger và kết quả đối soát.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary chính.
2. Thiết kế phép kiểm có đối chứng và artifact tái chạy.
3. Chỉ ra một phát biểu phụ thuộc PostgreSQL hoặc phương pháp modeling.
4. Nêu stop condition bảo vệ dữ liệu và môi trường.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Bài mở module, áp một quy trình có sẵn vào tình huống mới. Kiểm bằng rà soát chéo phát biểu hạt; đạt khi hai người đọc cùng một phát biểu hiểu giống nhau ở cả ba mô tả nghiệp vụ.

**Điều kiện đạt.** Ba phát biểu hạt đều được người đọc thứ hai diễn đạt lại đúng nghĩa, và cả bảy bước có kết quả ghi ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ tới cột trước khi chốt hạt · chọn lược đồ sao rồi mới đọc yêu cầu · bỏ bước mô hình hoá hiệu chỉnh và dữ liệu tới muộn · viết hạt bằng một cụm danh từ thay vì một câu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/37-from-requirement-to-model-seven-step-protocol.md`
- Nội dung học thuật: `note.md` cùng thư mục.
