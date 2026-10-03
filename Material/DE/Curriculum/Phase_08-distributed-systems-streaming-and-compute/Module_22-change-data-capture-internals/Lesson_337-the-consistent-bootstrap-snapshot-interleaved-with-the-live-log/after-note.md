# Phase 8: Distributed Systems, Streaming and Compute
# Module 22: Change Data Capture Internals
# Lesson 337: The consistent bootstrap - snapshot interleaved with the live log

## Thực hành

**Nhiệm vụ.** Chạy tải ghi liên tục trên nguồn. Khởi tạo bản chụp trong lúc đó. Sau khi hoàn tất, dừng ghi và đối soát tập khoá cùng giá trị giữa nguồn và đích. Cài thêm một bản cố ý bỏ bước đan xen và chứng minh nó tạo ra dữ liệu lùi về quá khứ; đếm số bản ghi sai. Đo ảnh hưởng của việc chụp lên nguồn.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đối soát khớp tuyệt đối dưới ghi đồng thời. Kiểm bằng đối soát tập khoá và giá trị; đạt khi đích khớp nguồn tại một ranh giới bất biến, và bản cài sai được chứng minh tạo ghi đè ngược.

**Điều kiện đạt.** Đích khớp nguồn tuyệt đối tại ranh giới bất biến, và bản bỏ bước đan xen được chứng minh tạo ghi đè ngược kèm số bản ghi sai.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chụp xong rồi mới bắt đầu thu dòng thay đổi · để dòng bản chụp ghi đè sự kiện mới hơn · khoá bảng để chụp cho đơn giản · không đối soát sau khi hoàn tất.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/225-the-consistent-bootstrap-snapshot-interleaved-with-the-live-log.md`
- Nội dung học thuật: `note.md` cùng thư mục.
