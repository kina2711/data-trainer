# Phase 2: Machine, Operating System and Network
# Module 5: Operating Systems, Concurrency and Linux
# Lesson 65: Non-blocking descriptors, select, poll and epoll

## Thực hành

**Nhiệm vụ.** Viết máy chủ một luồng dùng bộ mô tả không chặn. Cài cả hai cơ chế theo dõi. Đo thời gian mỗi vòng lặp ở 100, 1.000 và 10.000 kết nối nhàn rỗi, vẽ hai đường. Chuyển sang chế độ báo theo sườn mà không đọc tới khi hết dữ liệu, tái hiện kết nối treo, rồi sửa theo quy tắc đọc cạn.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường chi phí theo số kết nối. Kiểm bằng phép đo thay đổi quy mô; đạt khi hai đường chi phí tách nhau rõ ở 10.000 kết nối và ca báo theo sườn bị treo được tái hiện rồi sửa.

**Điều kiện đạt.** Hai đường chi phí tách nhau rõ ở 10.000 kết nối, và ca treo do báo theo sườn được tái hiện rồi sửa.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng bộ mô tả chặn trong vòng lặp sự kiện · dùng chế độ báo theo sườn mà không đọc cạn · đo chi phí chỉ ở số kết nối nhỏ · giả định tệp thường có ngữ nghĩa sẵn sàng như ổ cắm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/065-non-blocking-descriptors-select-poll-and-epoll.md`
- Nội dung học thuật: `note.md` cùng thư mục.
