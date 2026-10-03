# Phase 1: Engineering Foundation
# Module 4: Computer Architecture and the Performance Model
# Lesson 46: Cache lines, locality and the cache cliff

## Thực hành

**Nhiệm vụ.** Viết phép đo duyệt mảng với bước nhảy thay đổi, quét kích thước dữ liệu từ 4 KB tới 256 MB. Vẽ đồ thị thời gian trên mỗi phần tử và chỉ ra các bậc. So thông số suy ra với thông số thật của máy. Tái hiện chia sẻ giả với hai luồng và đo mức chậm đi, rồi sửa bằng cách chèn đệm.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi suy đặc tính phần cứng từ dữ liệu đo, chứ đọc thông số. Kiểm bằng đồ thị quét kích thước; đạt khi đồ thị có bậc rõ và dung lượng suy ra gần đúng với thông số thật.

**Điều kiện đạt.** Đồ thị có bậc rõ ràng, dung lượng suy ra cùng bậc với thông số thật, và bản sửa chia sẻ giả nhanh hơn có số chứng minh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đo với dữ liệu nhỏ hơn bộ nhớ đệm nên không thấy bậc nào · quên hâm nóng trước khi đo · kết luận chia sẻ giả mà không đo bản đã chèn đệm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/046-cache-lines-locality-cache-cliff.md`
- Nội dung học thuật: `note.md` cùng thư mục.
