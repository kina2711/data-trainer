# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 92: Error design: expected failure against defect

## Thực hành

**Nhiệm vụ.** Lập bảng hai trục cho mười lỗi có thể xảy ra trong pipeline nạp dữ liệu. Cài đặt xử lý cho từng ô. Tiêm bốn lỗi đại diện bốn ô và chứng minh đường đi đúng: thất bại dự kiến thử lại được thì thử lại, vĩnh viễn thì vào vùng cách ly, còn khiếm khuyết thì dừng và lộ ra.

#### Bốn thí nghiệm fault injection cho DE-L092

#### A. Expected + transient

Dependency trả 503 hai lần rồi thành công. Chứng minh attempt count, backoff và success cuối.

#### B. Expected + permanent

CSV thiếu cột bắt buộc. Chứng minh không retry, file vào quarantine và run report nêu số record chưa xử lý.

#### C. Defect + stable

Tiêm invariant violation sau validation. Chứng minh process dừng, stack/cause còn nguyên và không có record sau điểm lỗi được commit.

#### D. Defect + intermittent

Tiêm race làm counter âm ở một phần số lần chạy. Chứng minh assertion bắt được, run không bị ghi thành success và evidence giữ seed/concurrency level.

#### Phép kiểm bắt buộc

- retry count không vượt policy;
- permanent error có 0 retry;
- quarantine giữ raw locator và checksum;
- defect không bị generic catch chuyển thành success;
- unknown outcome gọi reconcile trước retry;
- error translation giữ cause chain;
- log không chứa secret hoặc toàn bộ PII payload;
- failure-atomicity assertion kiểm state sau lỗi.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Expectedness được quyết định bởi exception class hay contract?
2. Vì sao transient và defect không loại trừ nhau?
3. Timeout sau commit khác connection refused trước request ở đâu?
4. Retry cần sáu điều kiện nào?
5. Quarantine record cần lineage gì?
6. Exception translation giữ abstraction và cause ra sao?
7. Failure atomicity được kiểm bằng state nào?
8. Khi nào một unique violation là expected failure?
9. Vì sao generic catch gây mất completeness?
10. Bốn fault injection của DE-L092 phủ bốn ô nào?

> [!synthesis]
> Ma trận hai trục, workflow quarantine và bộ bốn fault injection là cấu trúc giảng dạy tổng hợp từ contract/failure guidance của Hunt–Thomas và Bloch cùng retry/resilience của Titmus. Không nguồn nào đặt tên toàn bộ mô hình này như một framework độc lập.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một thiết kế có bốn trường hợp kiểm được riêng. Kiểm bằng bốn loại lỗi tiêm; đạt khi cả bốn đi đúng đường và khiếm khuyết không bị nuốt.

**Điều kiện đạt.** Bảng mười lỗi phân loại đủ hai trục, và bốn lỗi tiêm đều đi đúng đường với khiếm khuyết không bị nuốt.

#### Ma trận chấm DE-L092

| Tiêu chí | Đạt | Không đạt |
|---|---|---|
| Taxonomy | đủ 10 lỗi, hai trục và qualifier | gắn nhãn theo tên exception |
| Retry | có budget, idempotency và deadline | retry mọi lỗi hoặc retry vô hạn |
| Permanent failure | quarantine/reject có lineage | lặp lại cùng input |
| Defect | dừng và giữ evidence | catch rồi tiếp tục |
| Translation | error tầng trên + cause | leak driver error hoặc mất cause |
| Atomicity | state sau lỗi được kiểm | chỉ kiểm có exception |

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Bắt mọi ngoại lệ rồi chạy tiếp · thử lại một lỗi dữ liệu vĩnh viễn · để lỗi lên tới tầng trên mà mất ngữ cảnh · coi mọi lỗi là thất bại dự kiến.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và một đoạn giải thích ngắn cho mỗi quyết định kỹ thuật. Không chấp nhận ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/04-error-design-data-pipeline.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
