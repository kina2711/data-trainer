# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 96: Static analysis, dependency and security scanning

## Thực hành

**Nhiệm vụ.** Thêm bốn loại kiểm vào quy trình ở lesson 31. Đặt ngưỡng chặn và ghi thành tài liệu ngắn. Tiêm bốn vi phạm: sai định dạng, một lỗi soát tĩnh thật, một thư viện có lỗ hổng đã biết, và một bí mật trong lịch sử. Chứng minh cả bốn bị chặn. Sinh danh mục thành phần và đọc nó.

#### Bốn phép thử tiêm cho DE-L096

| Injection | Gate kỳ vọng | Bằng chứng |
|---|---|---|
| file sai format | formatter | diff và exit code khác 0 |
| resource không đóng hoặc branch luôn đúng | static analysis | rule ID và path |
| dependency test có advisory cố định | SCA | component identity, advisory, DB timestamp |
| token giả theo test pattern trong commit cũ | history secret scan | commit SHA; token không có quyền thật |

Không dùng credential thật và không cố tình kéo một package nguy hiểm vào artifact production. Fixture phải cô lập và được xóa khỏi đường build sau phép thử.

## Kiểm tra cuối bài

#### Bài tự kiểm tra

1. Vì sao quét `requirements.txt` chưa đủ để biết artifact Python đang chạy gì?
2. Khi nào high-severity CVE có thể không chặn, và bằng chứng ngoại lệ phải gồm gì?
3. Vì sao secret bị xóa khỏi `main` vẫn cần rotate?
4. SBOM và vulnerability report khác nhau ở dữ liệu và thời điểm sử dụng nào?
5. Làm sao nâng rule pack mà không khiến CI của toàn đội đồng loạt đỏ không giải thích được?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cấu hình có tiêu chí nghiệm thu bằng phép thử tiêm. Kiểm bằng bốn vi phạm tiêm; đạt khi cả bốn bị chặn ở đúng bước và ngưỡng chặn được ghi lại thành tài liệu.

**Điều kiện đạt.** Bốn vi phạm đều bị chặn ở đúng bước, và tài liệu ngưỡng chặn nêu rõ mức nào chặn mức nào cảnh báo.


## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Bật mọi luật rồi bị tắt vì quá ồn · chỉ quét mã hiện tại · không đặt ngưỡng chặn · coi quét phụ thuộc là việc làm một lần.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/08-automated-code-and-supply-chain-checks.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
