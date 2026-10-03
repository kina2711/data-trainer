# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 161: Domain Modelling, Bounded Context and the Canonical Model Trap

## Thực hành

**Nhiệm vụ.** Cho mô tả ba đội cùng dùng ba từ chung nhưng nghĩa khác nhau. Chỉ ra xung đột. Với mỗi từ, viết định nghĩa theo từng ngữ cảnh và một hợp đồng để hai bên trao đổi. Viết hai câu giải thích vì sao ép một định nghĩa chung sẽ thất bại ở đây.

Chỉ chạy fixture, profiling, reconciliation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa production model, metric, identity mapping hay history để minh họa. Lưu input, assumptions, query/test, raw output và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu context/grain và invariant chính.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra source fact, quyết định thiết kế và curriculum synthesis.
4. Đề xuất phép kiểm tái chạy được cùng bằng chứng cần lưu.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra xung đột ngữ nghĩa trước khi nó thành xung đột kỹ thuật. Kiểm bằng bài phân tích; đạt khi chỉ ra đúng ít nhất hai từ mang hai nghĩa và đề xuất hợp đồng thay vì mô hình chung.

**Điều kiện đạt.** Chỉ đúng ≥ 2 từ mang hai nghĩa, và đề xuất tích hợp bằng hợp đồng kèm định nghĩa theo từng ngữ cảnh.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Ép một định nghĩa chung cho cả công ty · đổi tên để né xung đột mà không giải quyết nghĩa · coi xung đột ngữ nghĩa là vấn đề kỹ thuật · bỏ qua ai sở hữu dữ liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/49-domain-modelling-bounded-context-canonical-model-trap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
