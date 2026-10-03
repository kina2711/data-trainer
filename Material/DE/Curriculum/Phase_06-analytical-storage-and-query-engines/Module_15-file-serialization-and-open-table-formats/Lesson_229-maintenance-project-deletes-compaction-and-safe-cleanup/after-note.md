# Phase 6: Analytical Storage and Query Engines
# Module 15: File, Serialization and Open Table Formats
# Lesson 229: Iceberg Maintenance Compaction Retention and Cleanup

## Thực hành

**Nhiệm vụ.** Tạo hàng nghìn tệp nhỏ và một lượng tệp xoá đáng kể; đo thời gian quét và kích thước siêu dữ liệu. Chạy gộp tệp trong khi một bên ghi vẫn đang thêm dữ liệu; đo lại và đối soát số dòng. Hết hạn ảnh chụp với thời hạn giữ có căn cứ. Chạy dọn tệp mồ côi và chứng minh thời hạn giữ lớn hơn lần ghi dài nhất. Quay lại một ảnh chụp trước đó và đối soát.

Chỉ dùng fixture tổng hợp và môi trường cô lập. Lưu input/schema hashes, versions, commands, metadata, plans, counters, outputs, logs và limitations.

## Kiểm tra cuối bài

1. Nêu publication hoặc identity boundary.
2. Đưa failure/counterexample có thể tái hiện.
3. Phân biệt format guarantee với implementation observation.
4. Nêu reconciliation oracle và reversal condition.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình vận hành có tiêu chí an toàn kiểm được. Kiểm bằng đối soát trước sau cộng phép thử quay lại; đạt khi số dòng khớp tuyệt đối qua mọi thao tác và quay lại được ảnh chụp trước bảo trì.

**Điều kiện đạt.** Số dòng khớp tuyệt đối qua cả ba thao tác, thời hạn giữ được chứng minh lớn hơn lần ghi dài nhất, và quay lại ảnh chụp trước bảo trì thành công.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Xoá tệp dữ liệu bằng tay · dọn tệp mồ côi với thời hạn giữ mặc định mà không đo lần ghi dài nhất · hết hạn ảnh chụp còn cần cho quay lại · gộp tệp mà không đối soát số dòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/117-iceberg-maintenance-compaction-retention-cleanup.md`
- Nội dung học thuật: `note.md` cùng thư mục.
