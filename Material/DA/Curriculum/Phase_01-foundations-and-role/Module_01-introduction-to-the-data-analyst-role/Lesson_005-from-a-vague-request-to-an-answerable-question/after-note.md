# DA Lesson 5 — Practice, feedback and retest

## Thực hành có hướng dẫn

Phỏng vấn role-play: stakeholder chỉ nói 'campaign vừa rồi có hiệu quả không?'; nhóm có 12 phút để tạo contract và read-back.

**Dấu hiệu đạt:** Contract đủ tám trường semantic, có non-goal, acceptance và ít nhất một unknown với owner.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Trường đầu tiên của analytical contract là gì?** — Decision và hành động mà kết quả sẽ hỗ trợ.
- **Vì sao comparison phải ghi rõ?** — So với kỳ trước, cùng kỳ hay target có thể tạo kết luận trái nhau.
- **Một unknown khi nào là blocker?** — Khi nó làm đổi semantics, blast radius hoặc acceptance criteria.
- **Non-goal có tác dụng gì?** — Ngăn scope mở rộng âm thầm và làm rõ phần chưa được kết luận.

## Novel-scenario retest

CEO muốn câu trả lời trong hai giờ nhưng identity khách đa thiết bị chưa được giải quyết. Chọn dừng, co claim hay dùng proxy và nêu điều kiện.

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DA-L005, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

DA-L006 — cấu trúc dữ liệu đúng trong Excel theo contract đã khóa.
