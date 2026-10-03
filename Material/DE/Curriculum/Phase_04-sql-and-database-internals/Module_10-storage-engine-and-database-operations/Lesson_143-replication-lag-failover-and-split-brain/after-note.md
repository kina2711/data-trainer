# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 143: Replication, lag, failover and split brain

## Thực hành

**Nhiệm vụ.** Dựng một bản chính và một bản sao bất đồng bộ. Chạy tải ghi và đo độ trễ bản sao. Đọc ngay sau khi ghi trên bản sao và tái hiện hiện tượng không thấy. Giết bản chính, chuyển đổi, và đếm số giao dịch mất. Lặp lại với nhân bản đồng bộ và so hai con số.

Chỉ thực hiện trên database/cluster thử nghiệm cô lập, có seed và đường khôi phục. Không giữ lock dài, ép vacuum, đổi isolation/durability, kill node, promote hay rebalance trên production. Lưu script, cấu hình, operation-ID ledger, raw counters và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary của cơ chế.
2. Dựng schedule hoặc topology nhỏ nhất tái hiện lỗi.
3. Chọn ba chỉ số phân biệt triệu chứng với nguyên nhân.
4. Nêu một phát biểu chỉ đúng cho PostgreSQL và nguồn kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo. Kiểm bằng lần chuyển đổi thật; đạt khi đo được độ trễ dưới tải và lượng dữ liệu mất khớp với cấu hình đã chọn.

**Điều kiện đạt.** Có số đo độ trễ bản sao dưới tải, và lượng dữ liệu mất khi chuyển đổi khớp với cam kết của cấu hình ở cả hai chế độ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đọc bản sao cho bước đối soát · nghĩ bản sao còn kết nối là còn bắt kịp · chuyển đổi mà không rào chặn nút cũ · không đo độ trễ bản sao dưới tải thật.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/31-replication-lag-failover-and-split-brain.md`
- Nội dung học thuật: `note.md` cùng thư mục.
