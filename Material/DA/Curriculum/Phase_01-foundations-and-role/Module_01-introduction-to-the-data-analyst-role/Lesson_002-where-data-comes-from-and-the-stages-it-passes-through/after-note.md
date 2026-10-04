# DA Lesson 2: Practice, feedback and retest

## Thực hành có hướng dẫn

Xếp 14 thẻ artifact vào bảy chặng và nối mỗi chặng với một failure mode: missing event, duplicate, timezone, filter, join fan-out, stale cache, wrong action.

**Dấu hiệu đạt:** Đúng ≥ 12/14 thẻ và nêu được một phép kiểm độc lập tại ít nhất năm boundary.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **Ba lớp nào dễ bị đánh đồng?**: Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích.
- **Khi hai nguồn lệch, nên bắt đầu ở đâu?**: Boundary gần nguồn nhất còn giữ được bằng chứng độc lập.
- **Event time khác processing time thế nào?**: Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi.
- **Một phép reconciliation tốt cần gì?**: Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm.

## Novel-scenario retest

Dashboard retention giảm đúng ngày đổi SDK. Thiết kế thứ tự kiểm chứng để phân biệt hành vi thật, mất event và đổi identity.

**Pass condition:** câu trả lời nêu boundary, evidence, lựa chọn, ít nhất một alternative, blast radius/consumer harm và reversal trigger. Không chấm theo việc trùng wording của đáp án mẫu.

## Post-Lesson Work

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

Gói này chưa được dạy trên cohort thật. Điểm quiz và homework chỉ là evidence trong scope của DA-L002, không phải chứng nhận vai trò hoặc kinh nghiệm production.

## Bắc cầu

L003: khóa entity, record và grain trước khi đếm hoặc join.

## References

- [[wiki.da-foundation.data-lifecycle-seven-stages|Data lifecycle and its seven stages]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.da.reconciliation-and-the-discipline-of-verification|Reconciliation and the discipline of verification]]
