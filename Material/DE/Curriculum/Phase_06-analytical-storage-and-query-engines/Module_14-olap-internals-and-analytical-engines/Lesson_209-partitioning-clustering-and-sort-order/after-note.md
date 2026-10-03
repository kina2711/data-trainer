# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 209: Partitioning Clustering and Sort Order

## Thực hành

**Nhiệm vụ.** Ghi cùng dữ liệu theo ba phương án: phân vùng theo cột ít giá trị, phân vùng theo cột nhiều giá trị, và phân vùng thô cộng sắp xếp trong phân vùng. Đo số tệp, kích thước tệp trung bình, thời gian liệt kê siêu dữ liệu, và thời gian bộ năm truy vấn. Chỉ ra phương án hai tạo bao nhiêu tệp và chi phí thêm bao nhiêu.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi cân hai hiệu ứng ngược chiều, và chống lại quy tắc phân vùng theo cột hay lọc. Kiểm bằng ba phương án đo song song; đạt khi cả lợi ích lẫn hình phạt đều có số và lựa chọn dẫn được từ hai số đó.

**Điều kiện đạt.** Ba phương án có đủ bốn số đo, hình phạt tệp nhỏ được định lượng, và lựa chọn dẫn được từ cặp lợi ích với chi phí.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Phân vùng theo cột chỉ vì hay lọc theo nó · không đo số tệp sinh ra · sắp theo nhiều cột mà không cân nhắc thứ tự · bỏ qua thời gian liệt kê siêu dữ liệu khi đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/97-partitioning-clustering-sort-order.md`
- Nội dung học thuật: `note.md` cùng thư mục.
