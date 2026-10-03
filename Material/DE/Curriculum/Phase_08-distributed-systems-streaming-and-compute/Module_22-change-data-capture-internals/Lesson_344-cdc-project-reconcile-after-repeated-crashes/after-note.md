# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 344: CDC project - reconcile after repeated crashes

## Thực hành

**Nhiệm vụ.** Dựng đường đầy đủ. Chạy tải ghi liên tục gồm thêm, sửa, xoá và một lần cập nhật khoá chính. Giết ba thành phần ngẫu nhiên ít nhất 30 lần. Dừng ghi và đối soát. Thực hiện một lần chụp lại vào không gian cách ly rồi hoán đổi. Nộp sổ tay đủ năm mục bắt buộc.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module. Kiểm bằng đối soát sau giết lặp lại; đạt khi đích khớp nguồn tuyệt đối về tập khoá và giá trị, và bốn vị trí tiến độ đều có số đo độ trễ.

**Điều kiện đạt.** Đích khớp nguồn tuyệt đối về tập khoá và giá trị sau ≥ 30 lần giết, bốn vị trí tiến độ có số đo độ trễ, và lần chụp lại có đối soát trước khi hoán đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Coi trình kết nối báo chạy là bằng chứng đầy đủ · chụp lại đè lên đích đang phục vụ · bỏ ca cập nhật khoá chính · đối soát bằng cách đếm tổng mà không so tập khoá.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/232-cdc-project-reconcile-after-repeated-crashes.md`
- Nội dung học thuật: `note.md` cùng thư mục.
