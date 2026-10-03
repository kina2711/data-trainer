# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 392: Traces - span, context propagation and the queue boundary

## Thực hành

**Nhiệm vụ.** Gắn đo lường cho ba dịch vụ nối nhau qua một hàng đợi. Chạy tải và kiểm tỉ lệ vết nối đủ chặng. Cố ý bỏ truyền ngữ cảnh qua hàng đợi và quan sát vết đứt. Tạo ba yêu cầu chậm vì ba nguyên nhân khác nhau; đọc vết và chỉ ra chặng tốn nhất cùng phân biệt chờ với tính. Bật lấy mẫu theo đuôi và đo chi phí.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là vết liền mạch qua ranh giới bất đồng bộ. Kiểm bằng phép thử nối vết; đạt khi vết nối đủ chặng qua hàng đợi ở ít nhất 95 phần trăm mẫu, và chặng tốn nhất của ba yêu cầu chậm được chỉ đúng.

**Điều kiện đạt.** Vết nối đủ chặng qua hàng đợi ở ≥ 95% mẫu, và chặng tốn nhất của ba yêu cầu chậm được chỉ đúng kèm phân biệt chờ với tính.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Không truyền ngữ cảnh qua hàng đợi · lấy mẫu đầu với tỉ lệ thấp rồi mất hết vết lỗi · nhét dữ liệu lớn vào dữ liệu đính kèm · đọc vết mà không phân biệt chờ với tính.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/280-traces-span-context-propagation-and-the-queue-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
