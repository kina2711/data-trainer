# Phase 4: SQL and Database Internals
# Module 10: Storage Engine and Database Operations
# Lesson 139: ACID and the transaction state machine

## Thực hành

**Nhiệm vụ.** Với mỗi chữ trong bốn chữ, viết một phản ví dụ bằng dữ liệu cụ thể và chỉ ra cơ chế nào chặn nó. Với chữ nhất quán, nêu rõ phần nào do engine bảo đảm và phần nào do người thiết kế. Vẽ máy trạng thái của một giao dịch và chỉ ra các đường chuyển quan sát được trong hệ thật.

Chỉ chạy workload, compaction, cấu hình WAL/checkpoint hoặc crash injection trong instance thử nghiệm cô lập có seed/snapshot khôi phục. Không tắt `fsync`, phá cache, kill hoặc ép compaction trên production. Lưu config, raw counters, client operation-ID ledger và log; ảnh chụp không thay artifact tái chạy.

## Kiểm tra cuối bài

1. Bốn chữ ACID chia trách nhiệm ra sao?
2. Partially committed khác committed thế nào?
3. Client timeout chứng minh được gì?
4. State machine cần những transitions nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết nối bốn bài trước thành một khung; chuẩn bị cho ba bài sau. Kiểm bằng bài viết phản ví dụ; đạt khi cả bốn có phản ví dụ cụ thể và gắn đúng cơ chế.

**Điều kiện đạt.** Bốn phản ví dụ đều cụ thể và gắn đúng cơ chế, và phần nhất quán phân định rõ trách nhiệm engine với trách nhiệm người thiết kế.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi cả bốn chữ đều do engine bảo đảm tự động · nghĩ mức cô lập mặc định là mức cao nhất · giải thích bằng định nghĩa trừu tượng mà không có phản ví dụ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/27-acid-and-transaction-state-machine.md`
- Nội dung học thuật: `note.md` cùng thư mục.
