# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 253: dbt Mental Model Parse Compile Run Build

## Thực hành

**Nhiệm vụ.** Dựng một dự án tối thiểu trên cơ sở dữ liệu cục bộ với ba mô hình. Chạy cả bốn lệnh và ghi lại đồ thị được chọn, hành động thực hiện và hiện vật sinh ra. Mở câu lệnh SQL đã kết xuất của một mô hình và đối chiếu từng phần với mã nguồn. Vẽ đồ thị phụ thuộc và chỉ ra hàm tham chiếu nào tạo cạnh nào.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết mở phần công cụ sau sáu bài nguyên lý. Kiểm bằng bài đối chiếu bốn lệnh; đạt khi bảng bốn lệnh đúng ở cả ba cột và câu lệnh kết xuất được đối chiếu với mã nguồn.

**Điều kiện đạt.** Bảng bốn lệnh đúng ở cả ba cột, và câu lệnh kết xuất của một mô hình được đối chiếu đầy đủ với mã nguồn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết cứng tên bảng thay vì dùng hàm tham chiếu · dùng công cụ này để nạp dữ liệu · nhầm lệnh chạy với lệnh xây dựng · không bao giờ đọc câu lệnh đã kết xuất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/141-dbt-mental-model-parse-compile-run-build.md`
- Nội dung học thuật: `note.md` cùng thư mục.
