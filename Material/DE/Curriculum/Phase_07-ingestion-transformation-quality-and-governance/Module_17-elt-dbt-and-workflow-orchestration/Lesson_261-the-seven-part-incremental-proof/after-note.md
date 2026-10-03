# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 261: The Seven Part Incremental Proof

## Thực hành

**Nhiệm vụ.** Với ba mô hình tăng dần đã cài, viết chứng minh bảy phần cho từng cái. Với mỗi phần, viết một phép kiểm tự động tương ứng và đưa vào bộ kiểm. Đổi bài chéo: người khác đọc chứng minh và tìm một giả định chưa được kiểm. Sửa theo phản hồi.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective là một nghĩa vụ chứng minh, nên tiêu chí là tính đầy đủ và kiểm được của lập luận. Kiểm bằng rà soát chéo; đạt khi ba mô hình có đủ bảy phần và mỗi phần dẫn tới một phép kiểm tự động chứ dừng ở lời văn.

**Điều kiện đạt.** Ba mô hình có đủ bảy phần, mỗi phần dẫn tới một phép kiểm tự động, và rà soát chéo không tìm thấy giả định chưa kiểm.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Viết chứng minh bằng lời mà không có phép kiểm · bỏ phần xoá vì nguồn hiện chưa xoá · bỏ phần phục hồi vì chưa từng hỏng · chấp nhận điều kiện lọc theo mốc mà chưa chứng minh năm giả định.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/149-seven-part-incremental-proof.md`
- Nội dung học thuật: `note.md` cùng thư mục.
