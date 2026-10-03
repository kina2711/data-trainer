# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 335: Three ways to capture change and their cost

## Thực hành

**Nhiệm vụ.** Dựng một bảng nguồn có ghi liên tục. Chạy cách hỏi theo dấu thời gian mỗi 10 giây trong khi ghi nhiều lần một bản ghi và xoá vài bản ghi; đếm số thay đổi bị bỏ sót và số bản xoá không thấy. Cài một bẫy và đo chi phí ghi thêm trên nguồn. Lập bảng ba cách nhân ba tiêu chí.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, kiểm bằng một thí nghiệm nhỏ chứ chỉ lập luận. Kiểm bằng phép đếm bỏ sót; đạt khi số thay đổi bị bỏ sót được đo thật và bảng ba cách nhân ba tiêu chí có số ở tiêu chí tải nguồn.

**Điều kiện đạt.** Số thay đổi bỏ sót và số bản xoá không thấy được đo thật, và bảng ba cách có số đo ở tiêu chí tải nguồn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng cách hỏi theo dấu thời gian rồi tuyên bố bắt đủ thay đổi · cài bẫy mà không đo chi phí ghi thêm · nhầm bắt thay đổi với nguồn sự kiện · chọn đọc nhật ký mà chưa tính phụ thuộc thời hạn giữ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/223-three-ways-to-capture-change-and-their-cost.md`
- Nội dung học thuật: `note.md` cùng thư mục.
