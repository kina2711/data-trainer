# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 247: ETL and ELT Where the Compute Lives

## Thực hành

**Nhiệm vụ.** Cho ba khối lượng công việc. Chấm hai kiến trúc theo năm chiều cho từng cái. Đo thời gian và chi phí của cùng một phép biến đổi chạy ở hai nơi. Người chấm đổi một ràng buộc, chẳng hạn cấm dữ liệu cá nhân thô vào đích hoặc nhân đôi giá tính toán; điều chỉnh thiết kế và chứng minh vẫn chạy lại được.

Chỉ chạy trên fixture/sandbox được phép. Lưu versions, inputs, state trước–sau, kill points, raw outputs, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và phạm vi bảo đảm.
2. Chỉ ra một failure window.
3. Phân biệt expected result với evidence đã chạy.
4. Đưa counterexample làm thiết kế thất bại.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Bài mở module, đòi chọn theo ràng buộc chứ theo xu hướng. Kiểm bằng ba bối cảnh cộng một thay đổi ràng buộc do người chấm đưa ra; đạt khi thiết kế thích ứng mà không mất khả năng chạy lại.

**Điều kiện đạt.** Ba bối cảnh có bảng chấm năm chiều kèm số đo, và thiết kế thích ứng được với ràng buộc đảo chiều mà vẫn chạy lại được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết luận nạp thô rồi biến đổi luôn tốt hơn · đưa dữ liệu cá nhân thô vào đích vì tiện · bỏ khả năng chạy lại khi chuyển sang biến đổi trước · so hai kiến trúc mà không đo chi phí tính toán.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/135-etl-elt-where-compute-lives.md`
- Nội dung học thuật: `note.md` cùng thư mục.
