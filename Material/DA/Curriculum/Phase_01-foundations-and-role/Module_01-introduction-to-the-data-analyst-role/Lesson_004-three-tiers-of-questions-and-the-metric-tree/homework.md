---
loai: authentic-homework
lesson: 4
lesson_id: DA-L004
tieu_de: "Three tiers of questions and the metric tree"
trang_thai: ready-for-owner-review
nguong_dat: 75
---

# Homework: DA Lesson 4: Three tiers of questions and the metric tree

**Làm cá nhân. Nộp một thư mục chứa artifact, evidence và reflection.**

## Bối cảnh và input cố định

Subscription có MRR giảm từ 1,00 tỷ xuống 0,94 tỷ; new MRR 0,08; expansion 0,03; contraction 0,05; churn 0,12 (tỷ đồng).

Không tự bổ sung dữ kiện làm đổi semantics. Nếu cần assumption, ghi vào assumption ledger và nêu impact-if-wrong.

## Phần A: Build artifact (50 điểm)

Metric tree MRR có reconciliation, owner/lever cho từng lá, ba tầng câu hỏi và recommendation có uncertainty/reversal trigger.

Artifact phải đủ để một reviewer không dự buổi học tái hiện decision path. Mọi con số/command phải kèm source hoặc raw evidence.

## Phần B: Adversarial review (30 điểm)

1. Nêu hai failure mode có thể làm artifact trông đúng nhưng conclusion sai.
2. Tạo một counterexample hoặc fault injection cho mỗi failure mode.
3. Ghi expected observation **trước** khi chạy/đối chiếu.
4. Nêu oracle độc lập và kết quả sẽ khiến bạn bác bỏ recommendation.

## Phần C: Changed constraint và handoff (20 điểm)

Constraint đổi như sau: Nếu margin thay revenue làm outcome, discount có thể đổi từ lever tích cực thành driver phá giá trị; cây phải được dựng lại theo decision.

Viết memo 250-400 từ: phần nào của artifact còn đúng, phần nào phải thay, affected consumer, rollback/recovery và owner tiếp theo.

## Rubric chấm điểm

| Tiêu chí | Điểm | Full-credit evidence |
|---|---:|---|
| Semantics và boundary | 20 | Population/identity/time/state hoặc responsibility được nêu đủ; không có mặc định ẩn |
| Cơ chế và correctness | 20 | Lập luận theo đúng mental model; phép tính/graph/contract tái hiện được |
| Evidence và oracle | 20 | Raw evidence, expected result, independent check và discrepancy được giữ |
| Failure/edge paths | 15 | Hai counterexample thật; không chỉ lặp happy path |
| Decision và trade-off | 15 | Chosen/rejected option, limitation và reversal trigger rõ |
| Handoff và khả năng đọc | 10 | Cấu trúc gọn, owner/next action rõ, reviewer không phải đoán |

**Ngưỡng đạt:** ≥ 75/100 và không có critical failure.

## Critical-failure rules

- Cây chỉ là taxonomy đẹp, lá không có owner, hoặc diễn giải tương quan như nguyên nhân.
- Expected result được sửa sau khi nhìn output mà không ghi discrepancy.
- Không có evidence gốc hoặc dùng implementation đang kiểm làm oracle duy nhất.
- Khẳng định production/mastery vượt quá evidence của bài.

## Remediation và retest

Nếu trượt, reviewer chỉ rõ rubric row và failed invariant. Người học nộp lại phần sai cùng một changed scenario; không cần làm lại phần đã có bằng chứng đạt. Retest phải dùng fixture/scenario khác để tránh học thuộc đáp án.

## References

- [[wiki.da-foundation.three-question-tiers-and-metric-tree|Three question tiers and the metric tree]]
- [[wiki.data-product.metric-tree|Question decomposition and the metric tree]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
