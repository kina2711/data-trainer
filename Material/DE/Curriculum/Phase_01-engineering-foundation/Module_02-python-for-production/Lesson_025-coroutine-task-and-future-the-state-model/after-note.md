# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 25: Coroutine, task and future - the state model

## Thực hành

**Nhiệm vụ.** Viết chương trình tạo bốn tác vụ: một chạy xong, một ném ngoại lệ, một bị huỷ, một treo. Sau mỗi bước, liệt kê tác vụ đang sống và ghi trạng thái từng cái. Tái hiện hai ca lỗi bị nuốt: gọi hàm hiệp trình mà không chờ, và tạo tác vụ rồi không ai lấy kết quả. Bật chế độ gỡ lỗi của thư viện bất đồng bộ và ghi lại cảnh báo nó đưa ra.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi quan sát trạng thái thời gian chạy chứ đọc tài liệu. Kiểm bằng bài truy trạng thái; đạt khi năm trạng thái được quan sát bằng công cụ và hai ca lỗi bị nuốt được tái hiện.

**Điều kiện đạt.** Năm trạng thái được quan sát bằng công cụ, và hai ca lỗi bị nuốt được tái hiện cùng chỉ ra cách phát hiện.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi hàm hiệp trình mà quên chờ · tạo tác vụ rồi không giữ tham chiếu · nhầm đối tượng hiệp trình với tác vụ đang chạy · không bao giờ liệt kê tác vụ đang sống.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/025-coroutine-task-future-state-model.md`
- Nội dung học thuật: `note.md` cùng thư mục.
