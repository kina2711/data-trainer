# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 81: HTTP semantics - methods, status, idempotency and caching

## Thực hành

**Nhiệm vụ.** Cho mười tổ hợp phương thức và mã trạng thái. Với mỗi tổ hợp, quyết định có thử lại không và giải thích bằng tính bất biến cùng ngữ nghĩa mã trạng thái. Gọi một giao diện thật có giới hạn tốc độ và đọc tiêu đề cho biết phải chờ bao lâu.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho lesson 83 và cho M16; chưa đòi cài đặt. Kiểm bằng bảng quyết định trên mười tổ hợp; đạt khi đúng ít nhất tám và giải thích được bằng tính bất biến chứ bằng thói quen.

**Điều kiện đạt.** Quyết định đúng ≥ 8/10 tổ hợp kèm giải thích bằng tính bất biến, và đọc đúng tiêu đề chờ từ giao diện thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thử lại mọi lỗi · thử lại một yêu cầu tạo tài nguyên mà không có khoá bất biến · bỏ qua tiêu đề chờ của giới hạn tốc độ · nhầm an toàn với bất biến.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/081-http-semantics-methods-status-idempotency-and-caching.md`
- Nội dung học thuật: `note.md` cùng thư mục.
