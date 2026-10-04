# DE Lesson 3: Practice, feedback and retest

## Thực hành có hướng dẫn

Điền ADR one-page cho format trao đổi dữ liệu từ evidence packet; mỗi nhóm đóng vai reviewer tấn công một assumption.

**Dấu hiệu đạt:** ADR dưới hai trang, có ≥2 option thật, hard constraints, evidence, consequence owner và measurable revisit signal.

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

- **ADR lưu gì quan trọng nhất?**: Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi.
- **Hard constraint khác weighted criterion thế nào?**: Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác.
- **Một option tốt cần mô tả gì?**: Lợi ích, cost, failure mode và evidence có thể đảo đánh giá.
- **Revisit signal tốt có tính chất gì?**: Đo được, có owner và gắn với assumption/constraint cụ thể.

## Novel-scenario retest

Option rẻ nhất vi phạm RPO nhưng có tổng điểm cao nhất. Giải thích vì sao scoring sai và sửa decision rule.

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

Gói này chưa được dạy trên cohort thật. Điểm quiz và homework chỉ là evidence trong scope của DE-L003, không phải chứng nhận vai trò hoặc kinh nghiệm production.

## Bắc cầu

DE-L004: hiểu Git object graph để reasoning về thay đổi và phục hồi.

## References

- [[wiki.engineering-foundation.adr-trade-offs|Trade-offs and architecture decision records]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.data-product.requirements-traceability|Requirements traceability]]
