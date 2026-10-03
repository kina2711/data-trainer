# DA Lesson 1 — Practice, feedback and retest

## Thực hành có hướng dẫn

Phân loại tám thẻ việc: sửa pipeline mất dữ liệu, định nghĩa revenue, dashboard ngày, phân tích churn, dự báo churn, đặc tả hoàn tiền, đối soát hai báo cáo, trình bày khuyến nghị.

**Dấu hiệu đạt:** Ít nhất 6/8 thẻ đúng và mỗi lý do gọi tên outcome hoặc artifact bàn giao.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Phần giá trị cao nhất của DA là gì?** — Biến câu hỏi thành kết luận kiểm chứng được và hành động cụ thể.
- **Vì sao phải kiểm chứng con số trước khi giải thích?** — Một thay đổi có thể đến từ thiếu dữ liệu hoặc khác định nghĩa, không phải hành vi kinh doanh.
- **Artifact điển hình của AE là gì?** — Mô hình dữ liệu và định nghĩa chỉ số dùng chung.
- **Khi nào một yêu cầu gần với BI Analyst?** — Khi cần theo dõi chỉ số ổn định, lặp lại và có trạng thái tương tác rõ.

## Novel-scenario retest

Một startup 20 người tuyển 'Data Analyst' nhưng JD gồm Airflow, dbt, Power BI và churn model. Hãy tách bốn vai, rủi ro và thứ tự tuyển/bàn giao.

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

Gói này chưa được dạy trên cohort thật; thời lượng là ước tính. Điểm quiz/homework chỉ là evidence trong scope của DA-L001, không phải chứng nhận vai trò hay kinh nghiệm production.

## Bắc cầu

L002 — theo dấu một con số qua vòng đời dữ liệu.
