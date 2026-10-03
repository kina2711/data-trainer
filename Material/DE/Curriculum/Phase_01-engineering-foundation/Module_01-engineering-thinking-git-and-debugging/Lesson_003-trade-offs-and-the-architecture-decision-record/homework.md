---
loai: authentic-homework
lesson: 3
lesson_id: DE-L003
tieu_de: "Trade-offs and the architecture decision record"
thoi_gian_uoc_tinh_gio: 2.5
trang_thai: ready-for-owner-review
nguong_dat: 75
---

# Homework — DE Lesson 3: Trade-offs and the architecture decision record

**Thời gian ước tính:** 2–3 giờ · **Làm cá nhân** · **Nộp:** một thư mục chứa artifact, evidence và reflection.

## Bối cảnh và input cố định

Chọn format lưu 500 GB/ngày, retention 90 ngày, 4 consumer gồm Spark, DuckDB, Python và spreadsheet; schema đổi hàng tuần.

Không tự bổ sung dữ kiện làm đổi semantics. Nếu cần assumption, ghi vào assumption ledger và nêu impact-if-wrong.

## Phần A — Build artifact (50 điểm)

ADR ≤2 trang, option matrix, spike plan với expected discriminating outcomes, consequence owners và supersede/revisit procedure.

Artifact phải đủ để một reviewer không dự buổi học tái hiện decision path. Mọi con số/command phải kèm source hoặc raw evidence.

## Phần B — Adversarial review (30 điểm)

1. Nêu hai failure mode có thể làm artifact trông đúng nhưng conclusion sai.
2. Tạo một counterexample hoặc fault injection cho mỗi failure mode.
3. Ghi expected observation **trước** khi chạy/đối chiếu.
4. Nêu oracle độc lập và kết quả sẽ khiến bạn bác bỏ recommendation.

## Phần C — Changed constraint và handoff (20 điểm)

Constraint đổi như sau: Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.

Viết memo 250–400 từ: phần nào của artifact còn đúng, phần nào phải thay, affected consumer, rollback/recovery và owner tiếp theo.

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

- Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.
- Expected result được sửa sau khi nhìn output mà không ghi discrepancy.
- Không có evidence gốc hoặc dùng implementation đang kiểm làm oracle duy nhất.
- Khẳng định production/mastery vượt quá evidence của bài.

## Remediation và retest

Nếu trượt, reviewer chỉ rõ rubric row và failed invariant. Người học nộp lại phần sai cùng một changed scenario; không cần làm lại phần đã có bằng chứng đạt. Retest phải dùng fixture/scenario khác để tránh học thuộc đáp án.
