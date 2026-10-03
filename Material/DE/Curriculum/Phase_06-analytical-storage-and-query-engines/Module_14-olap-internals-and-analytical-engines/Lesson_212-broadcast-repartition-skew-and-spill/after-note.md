# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 212: Broadcast Repartition Skew and Spill

## Thực hành

**Nhiệm vụ.** Ép kết phát tán trên một bảng đủ lớn để tràn bộ nhớ. Ép kết phân bố lại và đo lượng dữ liệu qua mạng. Làm lệch một khoá tới mức chiếm phần lớn số dòng và quan sát tác vụ chạy lâu. Giảm bộ nhớ làm việc để gây tràn đĩa. Với mỗi hiện tượng, chỉ ra bằng chứng trong kế hoạch và số đo, rồi sửa.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nối triệu chứng với nguyên nhân trong hệ phân tán. Kiểm bằng bốn tình huống tái hiện; đạt khi chẩn đoán đúng cả bốn từ bằng chứng và sửa được ít nhất ba với số đo trước sau.

**Điều kiện đạt.** Bốn hiện tượng được tái hiện và chẩn đoán đúng từ bằng chứng, và ≥ 3 được sửa với số đo trước sau.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ép kết phát tán mà không kiểm kích thước thật · kết luận truy vấn chậm mà không tách lệch tải khỏi tràn đĩa · tăng bộ nhớ để che lệch tải · sửa mà không đo lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/100-broadcast-repartition-skew-spill.md`
- Nội dung học thuật: `note.md` cùng thư mục.
