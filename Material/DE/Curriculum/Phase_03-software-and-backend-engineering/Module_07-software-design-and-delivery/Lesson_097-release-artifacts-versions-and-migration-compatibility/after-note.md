# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 97: Release artifacts, versions and migration compatibility

## Thực hành

**Nhiệm vụ.** Dựng dịch vụ đọc ghi một bảng. Cần đổi tên một cột. Thực hiện theo hai giai đoạn trong lúc có tải liên tục: thêm cột mới, ghi cả hai, chuyển dữ liệu, đổi mã đọc, rồi xoá cột cũ. Ở mỗi bước, chạy đồng thời cả phiên bản cũ lẫn mới và đếm số yêu cầu thất bại.

#### Phép thử có tải cho DE-L097

1. Chạy traffic gồm read và write liên tục.
2. Ghi version phục vụ mỗi request và failure count.
3. Thực hiện từng bước migration, không gộp.
4. Ở mọi bước trung gian, giữ ít nhất một instance cũ và một instance mới.
5. Reconcile hai cột sau backfill.
6. Chỉ contract sau khi chứng minh không còn old reader.

Tiêu chí `0 failed request` chỉ có nghĩa khi định nghĩa failure gồm status, timeout, parse error và semantic mismatch. Không được loại request retry khỏi mẫu số mà không ghi rõ.

## Kiểm tra cuối bài

#### Bài tự kiểm tra

1. Vì sao build lại cùng commit ở production làm mất chuỗi bằng chứng?
2. Khi nào artifact version khác API version?
3. Bốn cặp writer-reader nào quyết định khả năng coexist và rollback?
4. Vì sao dual-write chưa đủ nếu thiếu reconciliation?
5. Bước nào của expand–migrate–contract thường làm rollback binary mất an toàn?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một quy trình có tiêu chí nghiệm thu bằng việc dịch vụ không lỗi trong suốt quá trình. Kiểm bằng thí nghiệm triển khai có tải; đạt khi không yêu cầu nào thất bại và cả hai phiên bản cùng chạy được.

**Điều kiện đạt.** Không yêu cầu nào thất bại qua toàn bộ quá trình, và cả hai phiên bản cùng chạy được ở mọi bước trung gian.

#### Evidence package của một release

Một release candidate nên mang theo:

- artifact digest và chữ ký/attestation nếu hệ có;
- source commit và build run;
- dependency lock/SBOM;
- test, contract và scanner report;
- configuration schema version;
- migration state và compatibility matrix;
- release notes theo hành vi quan sát;
- deploy/rollback runbook;
- owner phê duyệt đúng digest.

Evidence này cho phép trả lời “cái gì đang chạy, được kiểm bằng gì, dữ liệu đang ở state nào và còn lùi được không”.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Đổi tên cột trong một bước · dựng lại sản phẩm cho từng môi trường · xoá cột cũ ngay sau khi đổi mã · viết nhật ký thay đổi bằng danh sách commit.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/09-release-artifacts-versioning-and-compatible-migrations.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
