# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 365: Storage and managed databases chosen by the data contract

## Thực hành

**Nhiệm vụ.** Cho ba hợp đồng dữ liệu khác nhau; chọn lưu trữ và cơ sở dữ liệu cho từng cái kèm lý do theo bốn thuộc tính. Bật phiên bản và vòng đời trên kho đối tượng, rồi xoá nhầm một đối tượng và khôi phục. Kích hoạt chuyển dự phòng của cơ sở dữ liệu nhiều khu và đo thời gian gián đoạn cùng số kết nối bị đứt.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi đọc đúng hợp đồng của nhà cung cấp chứ so tên dịch vụ. Kiểm bằng ba lựa chọn cộng một diễn tập; đạt khi mỗi lựa chọn dẫn từ bốn thuộc tính và diễn tập chuyển dự phòng cho số đo gián đoạn thật.

**Điều kiện đạt.** Ba lựa chọn dẫn từ bốn thuộc tính, khôi phục được đối tượng xoá nhầm, và chuyển dự phòng có số đo thời gian gián đoạn.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi nhiều khu là đã có sao lưu · đọc nhầm độ bền thành độ khả dụng · bỏ qua giới hạn số kết nối tới cơ sở dữ liệu · chọn dịch vụ theo tên rồi ép hợp đồng dữ liệu vào nó.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/253-storage-and-managed-databases-chosen-by-the-data-contract.md`
- Nội dung học thuật: `note.md` cùng thư mục.
