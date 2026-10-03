# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 199: Reverse ETL and the Shadow Operational System

## Thực hành

**Nhiệm vụ.** Cho ba kiến trúc có đẩy dữ liệu ngược. Với mỗi cái, kiểm bốn ràng buộc và chỉ ra cái nào bị vi phạm. Với kiến trúc có vòng phản hồi, vẽ đường đi của dữ liệu và chỉ ra chỗ vòng lặp hình thành. Đề xuất cách chặn cho từng vi phạm.

Chỉ dùng fixture, synthetic principals, isolated load environment và cost/event extracts đã loại dữ liệu nhạy cảm. Không mở quyền production, load-test hệ dùng chung, gửi reverse-ETL action thật, xóa product hoặc thu personal data. Lưu versions, commands, raw outputs, unknown sets, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, product scope và owner trung tâm.
2. Đưa một failure vẫn có thể tạo tín hiệu xanh hoặc completed.
3. Nêu denominator, identity hoặc allocation rule cần khóa trước khi đo.
4. Phân biệt protocol đã viết với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là nhận ra một rủi ro kiến trúc trước khi nó cố định. Kiểm bằng ba kiến trúc; đạt khi nhận ra đúng ít nhất hai trường hợp có rủi ro và chỉ ra ràng buộc bị vi phạm.

**Điều kiện đạt.** Nhận đúng ≥ 2/3 trường hợp có rủi ro kèm ràng buộc bị vi phạm, và vẽ đúng chỗ vòng phản hồi hình thành.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi đẩy ngược là một pipeline bình thường · để kho phân tích thành nguồn sự thật cho nghiệp vụ · không chặn vòng phản hồi · hứa cam kết mức dịch vụ của hệ vận hành trên hạ tầng phân tích.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/87-reverse-etl-shadow-operational-system.md`
- Nội dung học thuật: `note.md` cùng thư mục.
