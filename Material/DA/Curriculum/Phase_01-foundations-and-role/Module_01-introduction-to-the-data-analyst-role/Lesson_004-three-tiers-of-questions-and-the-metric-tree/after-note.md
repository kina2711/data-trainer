# DA Lesson 4 — Practice, feedback and retest

## Thực hành có hướng dẫn

Dựng cây revenue cho marketplace từ GMV tới traffic, conversion, orders, AOV, take rate và refunds; đánh dấu stock/flow/rate.

**Dấu hiệu đạt:** Cây cân bằng trên số mẫu, không double count, mọi lá có owner và ít nhất một lever kiểm được.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Ba tầng câu hỏi là gì?** — Descriptive: chuyện gì; diagnostic: vì sao; prescriptive: nên làm gì.
- **Điều kiện tối thiểu của một lá cây chỉ số?** — Definition, grain, owner, lever và bằng chứng đo.
- **Revenue có thể phân rã cơ bản thế nào?** — Orders nhân Average Order Value.
- **Vì sao phải giữ residual/interaction?** — Để không ép toàn bộ biến động vào driver khi identity hoặc tương tác không giải thích hết.

## Novel-scenario retest

Conversion giảm nhưng revenue tăng do AOV. Quyết định ưu tiên driver nào khi mục tiêu đổi từ tăng trưởng sang contribution margin?

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DA-L004, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

L005 — biến yêu cầu mơ hồ thành analytical contract trả lời được.
