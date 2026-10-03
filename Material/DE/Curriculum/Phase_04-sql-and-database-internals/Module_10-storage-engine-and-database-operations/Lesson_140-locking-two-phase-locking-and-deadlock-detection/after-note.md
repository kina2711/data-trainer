# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 140: Locking, two-phase locking and deadlock detection

## Thực hành

**Nhiệm vụ.** Mở một giao dịch dài không chốt rồi chạy tải; quan sát hệ treo và dùng khung nhìn khoá để định vị giao dịch chặn. Tạo khoá chết giữa hai giao dịch, đọc thông báo và xác định nạn nhân. Cài xử lý thử lại cho lỗi bị huỷ và chạy 1000 lần chứng minh không mất giao dịch nào.

Chỉ thực hiện trên database/cluster thử nghiệm cô lập, có seed và đường khôi phục. Không giữ lock dài, ép vacuum, đổi isolation/durability, kill node, promote hay rebalance trên production. Lưu script, cấu hình, operation-ID ledger, raw counters và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary của cơ chế.
2. Dựng schedule hoặc topology nhỏ nhất tái hiện lỗi.
3. Chọn ba chỉ số phân biệt triệu chứng với nguyên nhân.
4. Nêu một phát biểu chỉ đúng cho PostgreSQL và nguồn kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là chẩn đoán một sự cố hay gặp và khó đoán từ bên ngoài. Kiểm bằng hai tình huống tiêm sẵn tính giờ; đạt khi định vị đúng giao dịch chặn ở cả hai và xử lý đúng lỗi bị huỷ.

**Điều kiện đạt.** Định vị đúng giao dịch chặn ở cả hai tình huống, và sau khi cài thử lại thì 1000 lần chạy không mất giao dịch nào.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Khởi động lại cơ sở dữ liệu để gỡ treo · không xử lý lỗi bị huỷ nên mất giao dịch · giữ giao dịch mở trong lúc chờ người dùng · đặt mức khoá bảng cho thao tác chỉ cần khoá dòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/28-locking-two-phase-locking-and-deadlock-detection.md`
- Nội dung học thuật: `note.md` cùng thư mục.
