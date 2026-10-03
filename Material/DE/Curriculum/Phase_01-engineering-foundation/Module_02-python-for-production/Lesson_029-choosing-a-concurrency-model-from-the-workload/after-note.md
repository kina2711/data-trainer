# Phase 1: Engineering Foundation
# Module 2: Python for Production
# Lesson 29: Choosing a concurrency model from the workload

## Thực hành

**Nhiệm vụ.** Cho bốn khối lượng công việc. Với mỗi cái, chọn mô hình và dẫn một số đo từ lesson 16, 22, 23 hoặc 24 làm căn cứ. Với khối lượng công việc không nên đồng thời, ước lượng phần phức tạp thêm vào so với phần thời gian tiết kiệm được.

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi áp một quy tắc quyết định có bằng chứng, chuẩn bị cho mọi module vận hành sau. Kiểm bằng bốn khối lượng công việc trong đó ít nhất một không nên đồng thời; đạt khi chọn đúng ít nhất ba và nhận ra trường hợp không nên đồng thời.

**Điều kiện đạt.** Chọn đúng ≥ 3/4 khối lượng công việc với số đo dẫn chứng, và nhận ra đúng trường hợp không nên đồng thời.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Chọn theo mô hình đang thịnh hành · dùng bất đồng bộ cho việc thiên CPU · bỏ qua phương án không đồng thời · dẫn lời khuyên thay vì dẫn số đo.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/029-choosing-concurrency-model-workload.md`
- Nội dung học thuật: `note.md` cùng thư mục.
