# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 88: Gate 2 - trace a request and diagnose the system

## Thực hành

**Nhiệm vụ.** Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Làm trên một hệ có ba sự cố cài sẵn ở ba tầng. Bài chấm sáu phần: A (20đ) phân loại đúng loại tải bằng chỉ số hệ thống · B (20đ) chẩn đoán sự cố mạng bằng bản bắt gói, chỉ đúng gói làm bằng chứng · C (20đ) giải thích một hiện tượng hiệu năng bằng mô hình chi phí, dẫn số đo của chính mình · D (15đ) sửa cả ba và xác nhận đã hồi phục · E (15đ) dòng thời gian chẩn đoán có ghi nhánh sai đã thử · F (10đ) báo cáo hiệu năng sáu phần cho một phép đo trong buổi.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Cổng đo năng lực chẩn đoán dưới áp lực thời gian, nên hình thức là buổi thực hành tính giờ chứ bài viết.

**Điều kiện đạt.** Đạt ≥ 70/100, phần A và B đều ≥ 60%. Kết luận nào không dẫn được về số đo hoặc gói tin thì phần đó bằng không.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Khởi động lại hệ rồi mất bằng chứng · kết luận từ một chỉ số · đoán trúng mà không có bằng chứng · bỏ phần dòng thời gian vì hết giờ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/088-gate-2-trace-a-request-and-diagnose-the-system.md`
- Nội dung học thuật: `note.md` cùng thư mục.
