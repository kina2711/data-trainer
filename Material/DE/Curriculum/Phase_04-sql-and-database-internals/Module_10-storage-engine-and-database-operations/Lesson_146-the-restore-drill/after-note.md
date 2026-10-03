# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 146: The restore drill

## Thực hành

**Nhiệm vụ.** Chạy buổi diễn tập theo kịch bản. Khôi phục về mốc ngay trước lệnh xoá nhầm, trên máy mới. Đối soát dữ liệu với bản chụp đã lưu trước đó. Đo cả hai đại lượng. So với hai mục tiêu và ghi rõ chỗ không đạt. Viết sổ tay khôi phục từ chính quy trình vừa làm.

Chỉ chạy backup/restore, fault injection, lock workload hoặc schema experiment trong môi trường cô lập có dữ liệu giả và đường xoá/khôi phục rõ. Không restore đè, đổi retention, kill process hoặc chạy destructive command trên production. Lưu exact version, config, script, raw log, operation ledger và kết quả đối soát.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary chính.
2. Thiết kế phép kiểm có đối chứng và artifact tái chạy.
3. Chỉ ra một phát biểu phụ thuộc PostgreSQL hoặc phương pháp modeling.
4. Nêu stop condition bảo vệ dữ liệu và môi trường.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo so với cam kết. Kiểm bằng buổi diễn tập tính giờ cộng đối soát dữ liệu; đạt khi dữ liệu khôi phục khớp trạng thái tại mốc và hai số đo được ghi lại.

**Điều kiện đạt.** Dữ liệu khôi phục khớp trạng thái tại mốc, hai đại lượng được đo và so với mục tiêu, và sổ tay viết ra từ quy trình thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Khôi phục trên chính máy đang hỏng · bỏ qua bước đối soát sau khi khôi phục · ước lượng thời gian thay vì đo · không ghi lại quy trình nên lần sau làm lại từ đầu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/34-the-restore-drill.md`
- Nội dung học thuật: `note.md` cùng thư mục.
