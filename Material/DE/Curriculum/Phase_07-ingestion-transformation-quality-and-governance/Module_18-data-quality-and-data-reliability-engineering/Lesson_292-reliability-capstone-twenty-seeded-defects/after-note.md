# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 18: Data Quality and Data Reliability Engineering
# Lesson 292: Reliability capstone - twenty seeded defects

## Thực hành

**Nhiệm vụ.** Dựng lớp kiểm soát theo bảy hạng mục. Gieo 20 lỗi thuộc nhiều loại, trong đó ít nhất bốn lỗi thuộc loại phép kiểm theo dòng không bắt được. Đo độ phủ phát hiện, thời gian phát hiện và tỉ lệ báo giả. Người chấm tiêm thêm một lỗi thầm lặng chưa từng gặp; định vị phạm vi ảnh hưởng và chạy phục hồi an toàn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một hệ vận hành có bằng chứng định lượng. Kiểm bằng 20 lỗi gieo; đạt khi phát hiện ít nhất 16 với tỉ lệ báo giả dưới ngưỡng, và hai sự cố được sửa cùng đối soát cùng ghi lại.

**Điều kiện đạt.** Phát hiện ≥ 16/20 lỗi gieo với tỉ lệ báo giả dưới ngưỡng, hai sự cố được sửa và đối soát và ghi lại, và không vi phạm sáu điều kiện tự động chưa đạt.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Thêm quy tắc để tăng độ phủ mà không ánh xạ rủi ro · tắt quy tắc ồn ngay trước khi chấm · công bố bản sửa trước khi đối soát · ghi đè bằng chứng sự cố khi dọn dẹp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/180-reliability-capstone-twenty-seeded-defects.md`
- Nội dung học thuật: `note.md` cùng thư mục.
