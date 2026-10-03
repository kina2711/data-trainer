# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 53: Buffering, page cache and fsync

## Thực hành

**Nhiệm vụ.** Ghi 100.000 bản ghi ở ba cấu hình: ghi đệm, ghi đệm rồi đẩy một lần cuối, và gọi `fsync` sau mỗi bản ghi. Đo thông lượng từng cấu hình. Mô phỏng mất điện bằng cách giết tiến trình cứng và đếm số bản ghi còn lại ở mỗi cấu hình. Lập bảng ba cột.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối một tham số cấu hình với một cam kết ngữ nghĩa và một con số. Kiểm bằng bảng ba cấu hình cộng thí nghiệm mất điện mô phỏng; đạt khi ba mức cam kết được phát biểu đúng và số đo đúng chiều.

**Điều kiện đạt.** Bảng ba cấu hình có cả thông lượng lẫn số bản ghi sống sót, và ba mức cam kết bền vững được phát biểu đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin rằng ghi xong là dữ liệu đã bền · gọi `fsync` sau mỗi bản ghi rồi thắc mắc vì sao chậm · đo lần hai mà quên bộ đệm trang đã ấm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/053-buffering-page-cache-and-fsync.md`
- Nội dung học thuật: `note.md` cùng thư mục.
