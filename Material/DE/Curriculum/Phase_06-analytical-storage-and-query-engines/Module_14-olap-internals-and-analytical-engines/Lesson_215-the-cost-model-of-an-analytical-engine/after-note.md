# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 215: Analytical Engine Cost Model

## Thực hành

**Nhiệm vụ.** Dựng một khối lượng công việc gồm ba loại truy vấn với tần suất khác nhau. Tính năm thành phần chi phí theo hai mô hình tính tiền. Tìm điểm mà thứ hạng đảo ngược khi đổi tần suất hoặc lượng dữ liệu. Áp ba đòn bẩy giảm chi phí theo thứ tự và đo mức giảm của từng đòn bẩy.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đòi tính chi phí theo mô hình chứ tra bảng giá. Kiểm bằng bài tính hai mô hình; đạt khi tính đúng cả năm thành phần và chỉ ra được điều kiện làm thứ hạng đảo ngược.

**Điều kiện đạt.** Năm thành phần được tính cho cả hai mô hình, điểm đảo ngược thứ hạng được chỉ ra, và ba đòn bẩy có mức giảm riêng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** So engine bằng đơn giá · bỏ thành phần truyền dữ liệu ra ngoài · bỏ thời gian người vận hành khỏi tổng chi phí · tăng kích thước cụm trước khi sửa truy vấn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/103-analytical-engine-cost-model.md`
- Nội dung học thuật: `note.md` cùng thư mục.
