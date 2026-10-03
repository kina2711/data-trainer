# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 142: Isolation levels chosen by anomaly, not by name

## Thực hành

**Nhiệm vụ.** Tái hiện cập nhật mất và lệch ghi bằng hai phiên chạy song song. Thử lại ở từng mức cô lập và lập bảng dị thường nào còn ở mức nào. Cho ba bất biến nghiệp vụ, chọn mức cô lập hoặc cơ chế khoá để chặn, và chứng minh bằng phép kiểm chạy song song.

Chỉ thực hiện trên database/cluster thử nghiệm cô lập, có seed và đường khôi phục. Không giữ lock dài, ép vacuum, đổi isolation/durability, kill node, promote hay rebalance trên production. Lưu script, cấu hình, operation-ID ledger, raw counters và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Nêu contract và failure boundary của cơ chế.
2. Dựng schedule hoặc topology nhỏ nhất tái hiện lỗi.
3. Chọn ba chỉ số phân biệt triệu chứng với nguyên nhân.
4. Nêu một phát biểu chỉ đúng cho PostgreSQL và nguồn kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi chọn theo dị thường chứ theo tên, và là chỗ nhiều hệ thật chọn sai. Kiểm bằng hai thí nghiệm tái hiện cộng bài chọn; đạt khi tái hiện được cả hai dị thường và chọn đúng cơ chế chặn cho ba bất biến cho trước.

**Điều kiện đạt.** Tái hiện được cả hai dị thường, bảng ánh xạ đúng, và ba bất biến đều được chặn có phép kiểm chạy song song chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn mức cô lập theo tên · nghĩ mức cao nhất luôn là lựa chọn đúng · cho rằng cùng tên mức thì cùng hành vi giữa các engine · kiểm bằng phép chạy tuần tự.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/30-isolation-levels-by-anomaly.md`
- Nội dung học thuật: `note.md` cùng thư mục.
