# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 210: MPP - Coordinator Fragments and Exchange

## Thực hành

**Nhiệm vụ.** Cho ba kế hoạch phân tán của cùng một truy vấn ở ba cách bố trí dữ liệu. Với mỗi cái, chỉ ra mảnh, bước trao đổi và lượng dữ liệu qua mạng. Dự đoán hiệu ứng khi gấp đôi số nút, rồi chạy thật và so với dự đoán.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho bài thực hành về lệch tải. Kiểm bằng bài đọc ba kế hoạch; đạt khi chỉ đúng bước trao đổi ở cả ba và dự đoán đúng hiệu ứng thêm nút ở ít nhất hai.

**Điều kiện đạt.** Chỉ đúng bước trao đổi ở cả ba kế hoạch, và dự đoán hiệu ứng thêm nút khớp thực tế ở ≥ 2/3.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cho rằng thêm nút luôn làm nhanh hơn · bỏ qua lượng dữ liệu qua mạng khi đọc kế hoạch · nhầm song song trong một nút với phân tán giữa các nút · thiết kế bố cục mà không xem cách kết.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/98-mpp-coordinator-fragments-exchange.md`
- Nội dung học thuật: `note.md` cùng thư mục.
