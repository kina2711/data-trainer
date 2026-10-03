# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 208: Vectorized Execution Is Not SIMD

## Thực hành

**Nhiệm vụ.** Chạy cùng một phép tổng hợp ở ba cấu hình: xử lý từng dòng, xử lý theo lô nhưng tắt lệnh véctơ, và xử lý theo lô có lệnh véctơ. Đo thời gian cùng số chu kỳ trên mỗi dòng ở từng cấu hình. Lặp lại với bốn kích thước lô và với một biểu thức lọc nhiều rẽ nhánh. Giải thích vì sao lô nhỏ làm mức tăng sụt.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi tách hai cơ chế thường bị gộp thành một lời giải thích. Kiểm bằng ba cấu hình đo song song; đạt khi hai phần đóng góp được tách bằng số và mức tăng thấp ở lô nhỏ được giải thích.

**Điều kiện đạt.** Hai phần đóng góp được tách bằng số ở cả bốn kích thước lô, và mức sụt ở lô nhỏ được giải thích bằng cơ chế.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Nói hệ cột nhanh vì dùng lệnh véctơ mà không tách hai cơ chế · đo ở một kích thước lô duy nhất · bỏ qua mặt nạ giá trị rỗng khi giải thích · kết luận từ thời gian tổng mà không có số chu kỳ trên mỗi dòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/96-vectorized-execution-not-simd.md`
- Nội dung học thuật: `note.md` cùng thư mục.
