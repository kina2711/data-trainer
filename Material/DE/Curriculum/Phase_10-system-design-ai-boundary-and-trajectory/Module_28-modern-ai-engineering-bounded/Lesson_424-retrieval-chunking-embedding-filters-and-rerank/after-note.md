# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 424: Retrieval - chunking, embedding, filters and rerank

## Thực hành

**Nhiệm vụ.** Dựng tập tài liệu có phân quyền theo khách hàng. Cài ba cấu hình truy hồi: chỉ từ khoá, chỉ véctơ, và kết hợp có sắp xếp lại. Xây tập đối chứng gồm truy vấn và tài liệu đúng. Đo độ phủ ở k và độ chính xác cho cả ba. Chạy phép thử phủ định về quyền. Đổi phiên bản mô hình nhúng và đo ảnh hưởng khi chưa dựng lại chỉ mục.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective đo tầng truy hồi riêng chứ đo kết quả cuối. Kiểm bằng tập đối chứng truy hồi; đạt khi độ phủ ở k đo được cho ba cấu hình, và phép thử phủ định về quyền không trả về tài liệu ngoài phạm vi.

**Điều kiện đạt.** Độ phủ ở k đo được cho ba cấu hình, phép thử phủ định về quyền không rò tài liệu, và ảnh hưởng của việc đổi mô hình nhúng được định lượng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Coi kho véctơ là nguồn sự thật · lọc quyền sau khi truy hồi · chia đoạn theo số ký tự cố định cắt ngang câu · đổi mô hình nhúng mà không dựng lại chỉ mục.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/312-retrieval-chunking-embedding-filters-and-rerank.md`
- Nội dung học thuật: `note.md` cùng thư mục.
