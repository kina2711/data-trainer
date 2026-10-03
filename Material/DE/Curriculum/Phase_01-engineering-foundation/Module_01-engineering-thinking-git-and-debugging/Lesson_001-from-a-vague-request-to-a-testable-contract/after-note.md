# DE Lesson 1 — Practice, feedback and retest

## Thực hành có hướng dẫn

Biến sáu câu requirement mơ hồ thành Given/When/Then có fixture, invariant và failure path.

**Dấu hiệu đạt:** Mỗi check có input cụ thể, expected result duy nhất, oracle và requirement ID; không dùng từ định tính chưa có threshold.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Một expected output tốt phải có tính chất gì?** — Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture.
- **Identity thiếu gây rủi ro gì?** — Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không.
- **Traceability hai chiều là gì?** — Requirement tới test/artifact và failed evidence quay về đúng requirement/owner.
- **Non-goal bảo vệ điều gì?** — Boundary và change control khỏi mở rộng scope âm thầm.

## Novel-scenario retest

API trả 202 nhưng commit outcome unknown. Định nghĩa behavior client, idempotency key và evidence phân biệt accepted với completed.

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DE-L001, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

DE-L002 — phân rã responsibility, interface, state và failure domain.
