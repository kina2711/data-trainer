# Phase 4: Data Analyst
# Module 9: Python for Data Analysts
# Lesson 71: pandas (2) - grouping, joining, pivoting

## Thực hành

**Nhiệm vụ.** Làm lại 10 truy vấn SQL từ lesson 22–24 bằng pandas. So kết quả từng dòng. Đo và so thời gian chạy của hai cách.

Giữ input snapshot, grain, identity, version, raw output, reconciliation và limitation.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Kiểm bằng hai số đo: kết quả khớp từng dòng với truy vấn SQL gốc, và thời gian chạy của cả hai cách. Số đo thứ hai cung cấp bằng chứng cho tiêu chí quyết định nơi chạy phép gộp, thay vì để người học kết luận theo cảm tính.

**Điều kiện đạt.** Cả 10 kết quả khớp từng dòng với truy vấn SQL, và bảng so thời gian chạy được nộp kèm kết luận về nơi nên chạy phép gộp.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 60 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 25 phút trả lời bốn câu kiểm tra · 15 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ tham số `validate` nên không phát hiện nhân bản dòng khi `merge` · kéo toàn bộ bảng về rồi gộp trong pandas · dùng `apply` theo dòng ở nơi có phép vector hoá.

## Reference
- Knowledge note: `Material/DA/Reference/Library/Knowledge-Notes/PACK-DA-CURRICULUM-01/071-pandas-2-grouping-joining-pivoting.md`
