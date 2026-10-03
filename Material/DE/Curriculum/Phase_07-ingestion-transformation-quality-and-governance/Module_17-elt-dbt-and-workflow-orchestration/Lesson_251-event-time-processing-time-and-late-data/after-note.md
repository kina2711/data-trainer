# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 251: Event Time Processing Time and Late Data

## Thực hành

**Nhiệm vụ.** Đo phân bố độ trễ giữa thời gian sự kiện và thời gian nạp trên dữ liệu thật; chọn độ rộng cửa sổ từ một phân vị có lý do. Cài cập nhật lại phân vùng trong cửa sổ. Tiêm dữ liệu muộn cả trong và ngoài cửa sổ. Đối soát báo cáo theo ngày trước và sau. Áp chính sách cho phần vượt cửa sổ và ghi lại số dòng bị ảnh hưởng.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi rút tham số từ dữ liệu quan sát chứ đặt tuỳ ý. Kiểm bằng đối soát báo cáo sau khi dữ liệu muộn tới; đạt khi báo cáo phân vùng cũ tự đúng lại trong cửa sổ và phần vượt cửa sổ có chính sách áp dụng được.

**Điều kiện đạt.** Độ rộng cửa sổ dẫn được từ phân bố độ trễ thật, báo cáo phân vùng cũ tự đúng lại trong cửa sổ, và phần vượt cửa sổ có chính sách cùng số dòng ghi lại.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân vùng theo thời gian nạp rồi báo cáo theo ngày sự kiện mà không nói rõ · đặt cửa sổ cập nhật lại bằng một con số tròn · bỏ dữ liệu vượt cửa sổ im lặng · trộn ba trục thời gian trong một cột.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/139-event-time-processing-time-late-data.md`
- Nội dung học thuật: `note.md` cùng thư mục.
