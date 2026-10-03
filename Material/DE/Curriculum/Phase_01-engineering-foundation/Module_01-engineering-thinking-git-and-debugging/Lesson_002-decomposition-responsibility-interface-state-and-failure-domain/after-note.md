# DE Lesson 2 — Practice, feedback and retest

## Thực hành có hướng dẫn

Phân rã order-payment-fulfillment trên bốn trục; inject timeout payment và database outage rồi trace impact.

**Dấu hiệu đạt:** Mỗi component có một responsibility, interface tối thiểu, state owner, dependencies không vòng và failure trace tới recovery.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Responsibility nên được tìm bằng gì?** — Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer.
- **Interface tối thiểu phải nêu gì?** — Operation, input/output semantics, error contract và invariant caller được dựa vào.
- **Authoritative writer có tác dụng gì?** — Ngăn nhiều component cập nhật cùng state machine mà không có protocol.
- **Failure domain được xác định thế nào?** — Trace fault qua dependency/state tới consumer harm và recovery.

## Novel-scenario retest

Hai team cần đổi schema với cadence khác nhưng dùng chung dedup ledger. Chọn tách ở đâu và ai sở hữu migration/recovery.

**Pass condition:** câu trả lời nêu boundary, evidence, lựa chọn, ít nhất một alternative, blast radius/consumer harm và reversal trigger. Không chấm theo việc trùng wording của đáp án mẫu.

## Bài làm sau buổi học

- Làm `quiz.md`, ngưỡng 8/10.
- Làm `homework.md`, ngưỡng 75/100 và không có critical failure.
- Giữ artifact gốc, feedback, bản sửa và retest như bốn evidence riêng; không ghi đè failed attempt.

## Remediation map

| Lỗi quan sát được | Quay lại | Bài retest |
|---|---|---|
| Không gọi tên được claim trung tâm | S02 | Giải thích bằng ví dụ khác, không dùng thuật ngữ trong tiêu đề |
| Chọn action trước boundary/evidence | S01, S05 | Viết ba câu hỏi phải đóng trước mutation |
| Chỉ chạy happy path | S06, S07 | Thêm counterexample và expected failure observation |
| Không chuyển được sang scenario mới | S08 | Giải changed constraint và nêu điều kiện đảo quyết định |

## Giới hạn

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DE-L002, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

DE-L003 — ghi trade-off và reversal trigger bằng ADR.
