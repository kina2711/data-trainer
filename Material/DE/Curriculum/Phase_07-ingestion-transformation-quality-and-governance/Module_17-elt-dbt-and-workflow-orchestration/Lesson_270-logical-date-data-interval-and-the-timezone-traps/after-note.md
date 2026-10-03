# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 270: Logical Date Data Interval and the Timezone Traps

## Thực hành

**Nhiệm vụ.** Viết một việc cố ý dùng thời điểm hiện tại. Nạp bù 30 phân vùng và chứng minh mọi phân vùng chứa cùng dữ liệu dù mọi lần chạy đều thành công. Sửa bằng cách dùng khoảng dữ liệu của lần chạy và đối soát lại. Cài một lịch hằng giờ và chạy qua hai lần chuyển giờ mùa hè, đếm số kỳ lặp và kỳ thiếu.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi làm mọi lần chạy đều báo thành công. Kiểm bằng nạp bù 30 phân vùng cộng thí nghiệm chuyển giờ; đạt khi lỗi được tái hiện và định lượng, bản sửa cho dữ liệu đúng theo từng phân vùng, và lịch không có kỳ lặp hay kỳ thiếu.

**Điều kiện đạt.** Lỗi dùng thời điểm hiện tại được tái hiện và định lượng, bản sửa cho dữ liệu đúng theo từng phân vùng, và lịch qua hai lần chuyển giờ không có kỳ lặp hay kỳ thiếu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng thời điểm hiện tại trong mã xử lý · nhầm thời điểm kích hoạt với khoảng dữ liệu · bật chạy bù tự động cho khoảng quá khứ dài mà không giới hạn đồng thời · đặt lịch theo giờ địa phương có giờ mùa hè.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/158-logical-date-data-interval-timezone-traps.md`
- Nội dung học thuật: `note.md` cùng thư mục.
