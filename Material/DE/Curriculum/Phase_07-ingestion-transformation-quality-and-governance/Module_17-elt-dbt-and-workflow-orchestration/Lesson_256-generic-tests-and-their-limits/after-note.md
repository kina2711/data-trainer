# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 256: Generic Tests and Their Limits

## Thực hành

**Nhiệm vụ.** Cài bốn phép kiểm cho một mô hình phục vụ. Tiêm bốn lỗi nằm trong tầm và bốn lỗi nằm ngoài tầm gồm giá trị canh chừng, khoá tổ hợp trùng, cha không có con, và mã mới hợp lệ. Ghi lại phép kiểm nào bắt được cái nào. Với mỗi lỗi không bắt được, viết một phép kiểm bổ sung. Bật lưu bản ghi hỏng và điều tra một ca.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra giới hạn của công cụ kiểm. Kiểm bằng phép thử tiêm; đạt khi bốn lỗi trong tầm bị bắt và ít nhất ba lỗi ngoài tầm được chỉ ra kèm cách kiểm bổ sung.

**Điều kiện đạt.** Bốn lỗi trong tầm bị bắt đúng, ≥ 3 lỗi ngoài tầm được chỉ ra và có phép kiểm bổ sung, và một ca hỏng được điều tra từ bản ghi lưu.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kiểm duy nhất trên một cột khi khoá là tổ hợp · tắt phép kiểm luôn đỏ thay vì đặt ngưỡng · tin bốn phép kiểm là đủ · không lưu bản ghi hỏng nên không điều tra được.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/144-generic-tests-and-their-limits.md`
- Nội dung học thuật: `note.md` cùng thư mục.
