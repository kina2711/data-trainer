# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 24: Asyncio - the event loop, cancellation and timeouts

## Thực hành

**Nhiệm vụ.** Viết trình thu thập gọi 500 địa chỉ với giới hạn 20 kết nối đồng thời. Cố ý chèn một lời gọi chặn và đo tác động lên toàn vòng lặp, rồi sửa bằng cách đẩy sang luồng riêng. Đặt hết giờ và kiểm nó kích hoạt. Huỷ toàn bộ giữa chừng và chứng minh mọi kết nối được đóng.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective gồm ba cơ chế bắt buộc kiểm được bằng thực nghiệm. Kiểm bằng ba phép thử; đạt khi không lời gọi chặn nào lọt, hết giờ kích hoạt đúng, và huỷ bỏ dọn sạch tài nguyên.

**Điều kiện đạt.** Không lời gọi chặn nào trong vòng lặp, hết giờ kích hoạt đúng ngưỡng, và sau khi huỷ thì mọi kết nối đã đóng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Gọi hàm chặn trong hàm bất đồng bộ · không đặt hết giờ · mở không giới hạn kết nối · bỏ qua việc dọn dẹp khi bị huỷ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/024-asyncio-event-loop-cancellation-timeouts.md`
- Nội dung học thuật: `note.md` cùng thư mục.
