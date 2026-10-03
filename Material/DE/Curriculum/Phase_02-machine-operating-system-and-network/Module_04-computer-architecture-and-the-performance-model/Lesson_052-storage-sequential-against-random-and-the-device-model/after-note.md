# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 52: Storage - sequential against random, and the device model

## Thực hành

**Nhiệm vụ.** Đo đọc tuần tự và đọc ngẫu nhiên ở hai độ sâu hàng đợi, ghi cả ba đại lượng cho mỗi cấu hình. Tính tỉ lệ chênh lệch. Chạy ghi liên tục 10 phút và vẽ tốc độ theo thời gian để quan sát mức tụt. So kết quả với thông số nhà sản xuất công bố.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một phép đo theo quy trình cộng đọc kết quả đúng. Kiểm bằng bảng đo bốn cấu hình; đạt khi cả ba đại lượng có số và chênh lệch tuần tự so với ngẫu nhiên đúng chiều.

**Điều kiện đạt.** Bảng bốn cấu hình đủ ba đại lượng, chênh lệch tuần tự so với ngẫu nhiên đúng chiều, và đồ thị ghi liên tục cho thấy mức tụt.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đo với tệp nhỏ hơn bộ đệm trang nên chỉ đo RAM · đo ở một độ sâu hàng đợi rồi kết luận · gộp ba đại lượng làm một · tin thông số nhà sản xuất mà không đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/052-storage-sequential-against-random-and-the-device-model.md`
- Nội dung học thuật: `note.md` cùng thư mục.
