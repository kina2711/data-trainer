# Phase 3: Data Analyst
# Module 6: Visualization and Power BI
# Lesson 49: Power BI - loading data and modeling

## Thực hành

**Nhiệm vụ.** Nạp `DS1` từ PostgreSQL. Dựng mô hình sao có bảng lịch. Kiểm chứng tổng khớp với SQL.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng đối chiếu chéo công cụ: tổng trên mô hình Power BI phải khớp tuyệt đối với tổng tính bằng SQL trên cùng dữ liệu. Sai hướng lọc hoặc sai bản số sẽ làm lệch tổng và lộ ra ngay ở phép đối chiếu này.

**Điều kiện đạt.** Tổng trên mô hình Power BI khớp tuyệt đối với tổng tính bằng SQL, và mô hình không chứa quan hệ vòng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nạp bảng phẳng thay vì lược đồ sao · để hướng lọc hai chiều mặc định gây vòng lặp · quên đánh dấu bảng ngày nên hàm thời gian không chạy đúng.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/049-power-bi-loading-data-and-modeling.md`
