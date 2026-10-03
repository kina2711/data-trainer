# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 207: Vectorized Execution and Late Materialization

## Thực hành

**Nhiệm vụ.** Cho bốn tình huống: bộ lọc chọn gần hết số dòng, cột có kiểu phức hợp, hàm do người dùng viết chen giữa, và bảng rất hẹp. Với mỗi cái, chỉ ra cơ chế nào mất tác dụng và vì sao. Đo một truy vấn có hàm do người dùng viết so với bản viết bằng biểu thức có sẵn.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết khép phần cơ chế, chuẩn bị cho phần phân tán. Kiểm bằng bài lập luận bốn tình huống; đạt khi chỉ đúng cơ chế mất tác dụng ở ít nhất ba và lý do dẫn về cơ chế chứ về cấu hình.

**Điều kiện đạt.** Chỉ đúng cơ chế mất tác dụng ở ≥ 3/4 tình huống, và có số đo cho ảnh hưởng của hàm do người dùng viết.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nghĩ xử lý theo lô là một cấu hình bật được · giả định vật chất hoá muộn luôn thắng · chen hàm tự viết vào vòng lặp nóng · bỏ qua chi phí chuyển đổi kiểu giữa các tầng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/95-vectorized-execution-late-materialization.md`
- Nội dung học thuật: `note.md` cùng thư mục.
