# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 141: MVCC, snapshots and vacuum

## Thực hành

**Nhiệm vụ.** Mở một giao dịch và để nguyên không chốt. Chạy tải cập nhật liên tục trong 20 phút. Đo mức phình bảng và tuổi giao dịch cũ nhất theo thời gian. Chốt giao dịch kia rồi chạy dọn và đo lại. Dựng cảnh báo trên ba chỉ số.

Chỉ thực hiện trên database/cluster thử nghiệm cô lập, có seed và đường khôi phục. Không giữ lock dài, ép vacuum, đổi isolation/durability, kill node, promote hay rebalance trên production. Lưu script, cấu hình, operation-ID ledger, raw counters và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary của cơ chế.
2. Dựng schedule hoặc topology nhỏ nhất tái hiện lỗi.
3. Chọn ba chỉ số phân biệt triệu chứng với nguyên nhân.
4. Nêu một phát biểu chỉ đúng cho PostgreSQL và nguồn kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối một hành vi ứng dụng với một hậu quả vận hành, chỗ rất khó đoán nếu không biết cơ chế. Kiểm bằng thí nghiệm có đo; đạt khi tái hiện được hiện tượng và ba chỉ số theo dõi cho thấy đúng nguyên nhân.

**Điều kiện đạt.** Tái hiện được mức phình tăng khi có giao dịch dài, và sau khi chốt thì dọn đưa mức phình về, cả hai có số đo theo thời gian.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin rằng dọn tự động luôn đủ · để giao dịch mở lâu trong mã ứng dụng · dùng lệnh dọn toàn phần trên bảng lớn đang có tải · chỉ theo dõi dung lượng mà không theo dõi tuổi giao dịch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/29-mvcc-snapshots-and-vacuum.md`
- Nội dung học thuật: `note.md` cùng thư mục.
