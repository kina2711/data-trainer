# DE Lesson 5 — Practice, feedback and retest

## Thực hành có hướng dẫn

Bốn scenario card: branch riêng, shared branch, bad release, noisy fixups. Chọn operation, vẽ graph và nêu affected users.

**Dấu hiệu đạt:** Đúng ≥3/4 lựa chọn; mỗi lựa chọn có merge base/OID reasoning, blast radius và recovery.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Fast-forward xảy ra khi nào?** — Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển.
- **Three-way merge dùng ba trạng thái nào?** — Hai tips và merge base chung.
- **Vì sao rebase đổi commit identity?** — Commit được tạo lại trên parent mới nên object content và OID đổi.
- **Squash mất thông tin gì?** — Các commit boundary và topology trung gian trên history đích.

## Novel-scenario retest

Pipeline pin commit SHA cũ trong khi team muốn rebase branch. Thiết kế migration hoặc chọn operation không phá consumer.

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DE-L005, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

DE-L006 — phục hồi lost work bằng reflog, detached HEAD và bisect.
