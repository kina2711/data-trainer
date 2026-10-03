# DA Lesson 3 — Practice, feedback and retest

## Thực hành có hướng dẫn

Cho năm schema nhỏ; viết grain, candidate key, cardinality dự kiến và một query/profile chứng minh cho từng bảng.

**Dấu hiệu đạt:** 5/5 câu grain có entity + thời gian/trạng thái phù hợp và mỗi câu có phép kiểm uniqueness/fan-out tương ứng.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Grain là gì?** — Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu.
- **Dấu hiệu trực tiếp của fan-out là gì?** — Row count hoặc multiplicity trên base key tăng sau join.
- **Measure phía one nên xử lý thế nào trước one-to-many join?** — Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép.
- **Candidate key cần được kiểm bằng gì?** — Count so với count distinct cùng kiểm NULL và duplicate distribution.

## Novel-scenario retest

Một bảng customer_address lưu lịch sử hiệu lực. Chọn grain và join rule để gán đúng địa chỉ tại thời điểm order.

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DA-L003, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

L004 — phân rã outcome thành metric tree có driver hành động được.
