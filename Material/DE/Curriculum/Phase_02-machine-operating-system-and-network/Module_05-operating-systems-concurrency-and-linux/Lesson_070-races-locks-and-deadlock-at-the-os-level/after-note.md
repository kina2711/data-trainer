# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 70: Races, locks and deadlock at the OS level

## Thực hành

**Nhiệm vụ.** Viết chương trình có hai khoá lấy theo thứ tự chéo nhau và làm nó treo. Dùng công cụ theo dõi lời gọi hệ thống để thấy cả hai luồng đang chờ ở đâu. Sửa bằng cách quy định thứ tự lấy khoá. Đo thời gian chờ ở nguyên hàm đồng bộ trước và sau khi giảm vùng tranh chấp.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi truy từ hiện tượng treo về cấu trúc lấy khoá, dùng bằng chứng hệ thống. Kiểm bằng tình huống khoá chết tiêm sẵn tính giờ; đạt khi định vị đúng cặp khoá và nêu đúng điều kiện đã phá.

**Điều kiện đạt.** Định vị đúng cặp khoá gây treo bằng bằng chứng hệ thống, sửa xong chương trình không treo qua 1000 lần chạy, và có số đo tranh chấp trước sau.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Thêm khoá bao quanh mọi thứ · tăng thời gian chờ khoá thay vì sửa thứ tự · kết luận treo do mạng mà chưa xem tiến trình đang chờ gì · không đo tranh chấp.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/070-races-locks-and-deadlock-at-the-os-level.md`
- Nội dung học thuật: `note.md` cùng thư mục.
