# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 361: Regions, zones, failure domains and shared responsibility

## Thực hành

**Nhiệm vụ.** Cho một kiến trúc bốn thành phần; vẽ sơ đồ miền hỏng và chỉ ra thành phần nào cùng chết khi mất một khu khả dụng. Với bốn dịch vụ thuộc bốn mức quản lý khác nhau, liệt kê phần nhà cung cấp lo và phần mình lo. Tìm ba khoảng trống không ai lo trong một kiến trúc thật.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài mở module, đặt từ vựng. Kiểm bằng bài phân định; đạt khi vẽ đúng miền hỏng và chỉ đúng phần khách hàng phải lo ở ít nhất ba trong bốn dịch vụ.

**Điều kiện đạt.** Sơ đồ miền hỏng đúng cho kiến trúc bốn thành phần, và phần trách nhiệm khách hàng đúng ở ≥ 3/4 dịch vụ kèm ba khoảng trống tìm được.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Giả định dịch vụ được quản lý thì không cần sao lưu · coi nhiều khu khả dụng là thay được sao lưu · nhầm sự cố mặt phẳng điều khiển với sự cố mặt phẳng dữ liệu · vẽ kiến trúc mà không đánh dấu miền hỏng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/249-regions-zones-failure-domains-and-shared-responsibility.md`
- Nội dung học thuật: `note.md` cùng thư mục.
