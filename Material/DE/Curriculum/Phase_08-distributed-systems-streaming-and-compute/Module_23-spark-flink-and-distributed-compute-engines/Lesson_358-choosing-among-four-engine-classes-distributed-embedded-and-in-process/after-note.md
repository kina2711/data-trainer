# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 358: Choosing among four engine classes - distributed, embedded and in-process

## Thực hành

**Nhiệm vụ.** So bốn lớp engine theo độ trễ, quy mô dữ liệu, mô hình trạng thái, chi phí vận hành và hệ sinh thái. Chạy một công việc đếm theo cửa sổ trên engine dòng chảy, giết một tiến trình quản lý tác vụ và khôi phục từ điểm kiểm tra; tạo một điểm lưu, đổi mức song song rồi khôi phục từ điểm lưu. Chạy **cùng một phép tổng hợp trên cả engine phân tán lẫn hai engine một máy** với ba kích thước dữ liệu tăng dần; tìm kích thước mà engine phân tán bắt đầu thắng. Cho ba bối cảnh khác nhau về quy mô và độ trễ, chọn engine cho từng cái.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective chống lại việc mặc định chọn engine phân tán. Kiểm bằng bảng bốn lớp nhân năm tiêu chí cộng một phép đo; đạt khi ba bối cảnh chọn đúng, ít nhất một bối cảnh chọn engine một máy, và ngưỡng chuyển sang phân tán có số đo.

**Điều kiện đạt.** Bảng bốn lớp nhân năm tiêu chí có luận điểm kèm quan sát từ lab, ngưỡng chuyển sang engine phân tán có số đo từ ba kích thước dữ liệu, ba bối cảnh chọn đúng với ít nhất một chọn engine một máy, và khôi phục từ cả điểm kiểm tra lẫn điểm lưu thành công.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn engine theo độ phổ biến · **dùng engine phân tán cho dữ liệu vừa một máy** · nhầm điểm lưu với điểm kiểm tra · học sâu cả hai engine phân tán cùng lúc · bỏ qua chi phí vận hành khi so.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/246-choosing-among-four-engine-classes-distributed-embedded-and-in-process.md`
- Nội dung học thuật: `note.md` cùng thư mục.
