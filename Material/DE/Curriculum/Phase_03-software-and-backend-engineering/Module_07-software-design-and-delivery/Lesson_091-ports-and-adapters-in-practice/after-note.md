# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 91: Ports and adapters in practice

## Thực hành

**Nhiệm vụ.** Tái cấu trúc công cụ nạp CSV ở lesson 32 thành ba tầng. Viết phép kiểm cho tầng miền không dùng tệp và không dùng cơ sở dữ liệu. Thay bộ chuyển đổi từ tệp sang PostgreSQL. Chứng minh phép kiểm lõi không sửa dòng nào. Đếm số tệp phải sửa cho lần thay đó.

#### Bằng chứng cho DE-L091

Nộp một evidence pack gồm:

1. dependency graph trước và sau;
2. import-policy report;
3. danh sách core test cùng checksum trước/sau;
4. test result với file adapter;
5. test result với PostgreSQL adapter;
6. changed-file manifest có phân loại core/application/adapter/bootstrap;
7. error translation table cho adapter mới;
8. decision note giải thích vì sao mức tách này xứng đáng.

#### Lệnh kiểm chứng gợi ý

```bash
sha256sum tests/core/*.py
git diff --name-only BEFORE_ADAPTER_REPLACEMENT..AFTER_ADAPTER_REPLACEMENT
pytest tests/core tests/adapters
```

Không dùng chỉ một ảnh chụp “tests passed”; cần command, exit status và commit hoặc tree hash.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Ai sở hữu outbound port và vì sao?
2. Runtime call và source dependency ngược chiều ở đâu?
3. Ba dấu hiệu type hoặc error leakage là gì?
4. Vì sao `Session` trong use-case signature làm replacement test mất ý nghĩa?
5. Core test chứng minh được gì và không chứng minh được gì?
6. Composition root biết những gì mà domain không được biết?
7. Khi nào in-memory adapter là hợp lệ?
8. File count và file category khác nhau thế nào trong replacement experiment?
9. Khi nào ports/adapters là overengineering?
10. Evidence nào chứng minh core test thật sự không bị sửa?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một phép biến đổi cấu trúc có tiêu chí nghiệm thu khách quan. Kiểm bằng phép thử đổi bộ chuyển đổi; đạt khi phép kiểm lõi không sửa dòng nào và vẫn xanh.

**Điều kiện đạt.** Phép kiểm lõi không sửa dòng nào và vẫn xanh sau khi đổi bộ chuyển đổi, và tầng miền không nhập thư viện ngoài nào.

#### Ma trận chấm

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Dependency direction | core chỉ trỏ vào contract nó sở hữu | core import adapter hoặc thư viện ngoài |
| Type boundary | chữ ký core dùng type core | ORM/DataFrame/driver type lọt vào |
| Error boundary | lỗi được dịch và giữ cause | lỗi thư viện lan ra hoặc mất context |
| Replacement | core test không đổi và xanh | phải sửa expectation/fixture core |
| Integration proof | adapter test dùng hệ thật | chỉ dùng fake rồi kết luận PostgreSQL đúng |
| Proportionality | decision note nêu cost/benefit | thêm tầng theo mẫu mà không có pressure |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Cho kiểu dữ liệu của thư viện lọt vào tầng miền · gọi thẳng cơ sở dữ liệu từ miền · dựng ba tầng cho một script dùng một lần · để lỗi thư viện lan ra ngoài chưa dịch.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/03-ports-adapters-data-pipeline.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
