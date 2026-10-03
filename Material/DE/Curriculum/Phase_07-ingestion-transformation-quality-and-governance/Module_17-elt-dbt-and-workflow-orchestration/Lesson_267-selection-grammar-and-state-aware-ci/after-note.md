# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 267: Selection Grammar and State Aware CI

## Thực hành

**Nhiệm vụ.** Dựng tích hợp liên tục dùng chọn theo trạng thái với tệp kê khai tham chiếu từ lần chạy sản xuất. Tiêm ba thay đổi ở ba vị trí trong đồ thị và so tập nút được chọn với tập đúng tính bằng tay. Tạo một lỗi chỉ lộ ra do dữ liệu mới chứ do mã đổi, và chứng minh lần kiểm đầy đủ theo lịch bắt được. Thử tham chiếu sai môi trường và ghi lại hậu quả.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có hai ràng buộc: nhanh và không bỏ sót. Kiểm bằng ba thay đổi tiêm; đạt khi tập nút được chọn khớp tập đúng ở cả ba và lần kiểm đầy đủ bắt được một lỗi do dữ liệu mà lần chạy phần đổi bỏ qua.

**Điều kiện đạt.** Tập nút được chọn khớp tập đúng ở cả ba thay đổi, và lần kiểm đầy đủ theo lịch bắt được lỗi do dữ liệu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chạy biểu thức chọn ở sản xuất mà không xem danh sách nút · bỏ lần kiểm đầy đủ vì đã có chọn theo trạng thái · lấy tệp kê khai tham chiếu từ môi trường phát triển · dùng thông tin xác thực sản xuất trong tích hợp liên tục.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/155-selection-grammar-state-aware-ci.md`
- Nội dung học thuật: `note.md` cùng thư mục.
