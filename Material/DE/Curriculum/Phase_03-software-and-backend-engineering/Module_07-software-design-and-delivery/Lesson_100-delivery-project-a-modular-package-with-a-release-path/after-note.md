# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 100: Delivery project: a modular package with a release path

## Thực hành

**Nhiệm vụ.** Nâng công cụ thành sản phẩm đạt tám điểm. Nộp bảng danh mục kiểm, mỗi điểm dẫn tới tệp hoặc số đo. Thực hiện phép thử đổi bộ chuyển đổi và phép thử lùi. Nộp tài liệu quyết định kiến trúc.


## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Bằng chứng nào phân biệt modular package thật với ba thư mục trang trí?
2. Vì sao core test hash cần giữ trong adapter replacement experiment?
3. Một scanner report pass nhưng injection không bị chặn cho thấy lỗi gì?
4. Rollback replica thành công nhưng data invariant sai có đạt không?
5. Evidence ledger cần locator và reproduce command để làm gì?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm có kiến trúc và quy trình phát hành. Kiểm bằng hai phép thử cộng rà soát danh mục; đạt khi cả tám điểm có bằng chứng và cả hai phép thử qua.

**Điều kiện đạt.** Tám điểm đều dẫn được tới tệp hoặc số đo, đổi bộ chuyển đổi không sửa phép kiểm lõi, và lùi hoàn tất trong hạn.

#### Ma trận chấm

| Hạng mục | Pass | Fail |
|---|---|---|
| Architecture | zero forbidden edge; adapter thay được | layer chỉ là thư mục |
| Contract | bốn phần, có examples/errors | chỉ có function signature |
| Error | taxonomy + injection | catch-all/log-and-continue |
| Tests | risk mapped, real boundary tests | mock internal implementation |
| Contract test | consumer/provider verification | provider tự mirror response |
| Gates | policy + four injections | tool list không có evidence |
| Release | same digest promoted | rebuild per environment |
| Migration | mixed-version + reconcile | one-step breaking DDL |
| Adapter experiment | core tests unchanged | sửa core test |
| Rollback experiment | recovery in threshold + invariant | chỉ deploy lại thành công |

## Bài làm sau buổi học

**Nhiệm vụ.** Hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp.

**Lỗi cần chủ động loại trừ.** Dựng ba tầng cho phần không cần · mô phỏng thành phần bên trong nên phép kiểm đỏ khi tái cấu trúc · bỏ phép thử lùi vì tốn thời gian · dẫn bằng chứng chung chung.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/12-delivery-project-modular-package-release-path.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
