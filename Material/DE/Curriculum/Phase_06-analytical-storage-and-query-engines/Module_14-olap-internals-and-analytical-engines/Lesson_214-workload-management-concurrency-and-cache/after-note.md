# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 214: Workload Management Concurrency and Cache

## Thực hành

**Nhiệm vụ.** Chạy tải tăng dần tới khi hàng đợi hình thành. Đo và tách thời gian chờ khỏi thời gian chạy ở từng mức tải. Tạo hai tình huống: một cái nghẽn vì hàng đợi, một cái nghẽn vì truy vấn nặng. Chọn cách sửa cho từng cái và chứng minh cách sửa của tình huống này không giúp gì cho tình huống kia.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi phân giải một triệu chứng gộp thành hai nguyên nhân cần hai cách sửa khác nhau. Kiểm bằng hai tình huống; đạt khi tách đúng hai thành phần thời gian ở cả hai và cách sửa chọn đúng.

**Điều kiện đạt.** Hai thành phần thời gian tách được ở mọi mức tải, và cách sửa của mỗi tình huống được chứng minh không áp dụng cho tình huống kia.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đo thời gian tổng mà không tách chờ · mở rộng cụm để chữa một truy vấn viết kém · để đệm kết quả làm sai phép đo · không cô lập nhóm khối lượng công việc nên báo cáo nặng chặn truy vấn tương tác.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/102-workload-management-concurrency-cache.md`
- Nội dung học thuật: `note.md` cùng thư mục.
