# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 206: Zone Maps Statistics and Pruning

## Thực hành

**Nhiệm vụ.** Ghi bảng có thống kê theo khối. Chạy sáu truy vấn và đọc số khối bị cắt từ kế hoạch. Ba truy vấn cố ý làm cắt tỉa thất bại theo ba nguyên nhân; sửa từng cái và đo lại. Ghi cùng dữ liệu theo hai thứ tự sắp xếp khác nhau và so tỉ lệ cắt tỉa cho cùng bộ truy vấn.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một cơ chế không hoạt động mà truy vấn vẫn trả đúng kết quả. Kiểm bằng số khối đọc trong kế hoạch; đạt khi ba trường hợp hỏng được sửa và tỉ lệ cắt tỉa tăng có số đo ở cả ba.

**Điều kiện đạt.** Ba trường hợp cắt tỉa thất bại được sửa với tỉ lệ cắt tỉa tăng có số đo, và hiệu ứng thứ tự sắp xếp lên cắt tỉa được định lượng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tin cắt tỉa đang xảy ra vì truy vấn nhanh · bọc cột lọc trong hàm · so cột kiểu chuỗi với giá trị kiểu số · đánh giá cắt tỉa mà không đọc số khối trong kế hoạch.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/94-zone-maps-statistics-pruning.md`
- Nội dung học thuật: `note.md` cùng thư mục.
