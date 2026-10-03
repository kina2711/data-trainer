# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 162: Late Arriving Data, Early Arriving Facts and the Unknown Member

## Mục tiêu bài học

**Năng lực cần chứng minh.** Xử lý đúng ba ca biên và chứng minh tổng không thiếu dòng nào so với nguồn.

**Điều kiện hoàn thành.** Đối soát tổng khớp tuyệt đối với nguồn, ba nghĩa phân biệt được bằng truy vấn, và liên kết lịch sử sau khi sửa cho báo cáo đúng.

> [!abstract] Câu hỏi trung tâm
> Làm thế nào nạp sự kiện khi dimensional context chưa có, phân biệt các loại unknown và sửa lịch sử sau đó mà không mất dòng hoặc làm sai tổng?

## 1. Ba ca biên khác nhau

Late-arriving fact là fact đến sau business event; nó phải lookup dimension version có hiệu lực tại event time, không phải current row lúc load. Early-arriving fact là fact đến trước dimension detail; pipeline chưa có surrogate key đúng. Late-arriving dimension change là thuộc tính/version đáng lẽ có hiệu lực trong quá khứ nhưng chỉ biết sau này. Ba trường hợp dùng cùng chữ “muộn” nhưng khác thao tác: insert fact vào lịch sử, dùng placeholder/inferred member, hoặc tách interval và relink/restatement.

## 2. Không loại bỏ fact vì lookup thất bại

Inner join lookup rồi bỏ unmatched row làm control total thấp hơn source mà pipeline vẫn báo thành công. Thiết kế an toàn giữ fact bằng special member hoặc quarantine có ledger, tùy contract; mọi row phải có disposition. Reconciliation tối thiểu gồm source count, accepted count, quarantined count, rejected count, duplicate count và phương trình tổng. Với amount còn phải đối soát theo currency, business date và batch, không chỉ grand total.

## 3. Unknown không phải một nghĩa

`Unknown` nên được tách ít nhất ba trạng thái: `not-yet-known` khi dimension dự kiến sẽ tới; `not-applicable` khi quan hệ không tồn tại theo nghiệp vụ; `invalid/error` khi source key vi phạm contract hoặc không map được. Ba rows có surrogate keys ổn định và labels rõ. Gộp chúng làm mất khả năng đo backlog enrichment, data-quality defect và optional relationship. NULL foreign key cũng làm fact biến mất trong inner join và buộc consumer tự hiểu three-valued logic.

## 4. Inferred member và sửa liên kết

Nếu business key đáng tin, pipeline có thể tạo inferred dimension row tối thiểu, giữ surrogate key, rồi bổ sung attributes khi dimension đến. Nếu chưa xác định được identity, dùng shared not-yet-known member và lưu source key/event identity để relink. Khi late SCD Type 2 change đến, chèn version đúng effective interval, sửa boundaries không overlap và cập nhật fact foreign keys thuộc interval theo restatement policy. Rerun phải idempotent; không tạo thêm inferred member hoặc lặp correction.

## 5. Hai thời gian và chính sách công bố lại

Event/effective time quyết định dimension version nào đúng về nghiệp vụ; load/system time ghi lúc warehouse biết. Báo cáo lịch sử có thể restate theo sự thật mới, đóng băng theo số đã công bố, hoặc cung cấp hai view original/revised. Không có lựa chọn mặc định đúng cho mọi miền. Policy phải nêu cutoff, accounting period, materiality, approver, consumer notification và lineage từ correction tới outputs bị ảnh hưởng.

## 6. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần một dữ liệu phản ví dụ, một invariant và một bằng chứng chạy lại được. Tên pattern, sơ đồ hoặc một query chạy thành công không đủ để xác nhận đúng ngữ nghĩa.

### 6.1. late fact lookup dùng event time

**Mệnh đề cần kiểm.** late fact lookup dùng event time.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.2. early fact không được bị inner join làm mất

**Mệnh đề cần kiểm.** early fact không được bị inner join làm mất.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.3. mọi source row phải có disposition

**Mệnh đề cần kiểm.** mọi source row phải có disposition.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.4. not-yet-known khác not-applicable

**Mệnh đề cần kiểm.** not-yet-known khác not-applicable.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.5. invalid khác optional relationship

**Mệnh đề cần kiểm.** invalid khác optional relationship.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.6. NULL foreign key làm join semantics khó kiểm soát

**Mệnh đề cần kiểm.** NULL foreign key làm join semantics khó kiểm soát.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.7. inferred member cần stable business key

**Mệnh đề cần kiểm.** inferred member cần stable business key.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.8. shared unknown member cần giữ source identity để relink

**Mệnh đề cần kiểm.** shared unknown member cần giữ source identity để relink.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.9. late SCD2 change có thể tách interval

**Mệnh đề cần kiểm.** late SCD2 change có thể tách interval.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.10. SCD intervals không được overlap

**Mệnh đề cần kiểm.** SCD intervals không được overlap.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.11. fact relink phải theo effective interval

**Mệnh đề cần kiểm.** fact relink phải theo effective interval.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.12. rerun không sinh placeholder trùng

**Mệnh đề cần kiểm.** rerun không sinh placeholder trùng.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.13. row và amount reconciliation đều cần thiết

**Mệnh đề cần kiểm.** row và amount reconciliation đều cần thiết.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.14. original và revised reports cần version

**Mệnh đề cần kiểm.** original và revised reports cần version.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.15. quarantine không được trở thành nơi bỏ quên dữ liệu

**Mệnh đề cần kiểm.** quarantine không được trở thành nơi bỏ quên dữ liệu.

**Cách kiểm.** Dựng fixture gồm normal fact, late fact, early fact, optional relationship, invalid key và late SCD2 change. Lưu ledger disposition; kiểm count/amount equation, no-overlap, relink theo effective time và rerun idempotency. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

## 7. Quy trình làm bài và phản biện

1. Viết business question, phạm vi, vocabulary, grain, identity và time semantics trước khi chọn bảng hoặc công cụ.
2. Gắn từng định nghĩa với context, owner, version và canonical artifact; không dùng tên cột thay nghĩa.
3. Tách nội dung lấy trực tiếp từ nguồn, quyết định thiết kế và phần tổng hợp của giáo trình.
4. Dựng normal case cùng các ca biên có thể tạo kết quả hợp lệ cú pháp nhưng sai nghĩa.
5. Đo row count, distinct keys, unmatched/disposition counts, control totals và semantic diff trước–sau transform.
6. Thử replay, late correction hoặc schema/contract change phù hợp với bài; ghi change blast radius.
7. Giữ failed run, assumptions và limitation trong hồ sơ. Chúng cho người khác khả năng bác bỏ kết luận.

## 8. Câu hỏi tự kiểm tra

1. Artifact nào giữ dữ liệu, artifact nào giữ nghĩa và ai có quyền thay đổi?
2. Một row/term/metric đại diện điều gì trong context và khoảng thời gian nào?
3. Ca biên nào làm con số sai nhưng pipeline hoặc dashboard vẫn xanh?
4. Phép kiểm nào xác nhận cấu trúc; phần nào vẫn cần owner xác nhận?
5. Khi contract thay đổi, consumer nào bị ảnh hưởng và migration được kiểm ra sao?
6. Phần nào của note là source fact, phần nào là synthesis có điều kiện?

## 9. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy các lab, handover test hoặc benchmark mô tả trong note; chúng là giao thức kiểm chứng, không phải số đo đã thu.
- Nguồn sách cung cấp khái niệm và patterns; lựa chọn cho một doanh nghiệp còn phụ thuộc domain, engine, workload, policy và owner.
- Tài liệu web được kiểm ngày 2026-10-01 và có thể thay đổi theo phiên bản sản phẩm.
- Không suy một tool, model hay kiến trúc là chuẩn duy nhất từ ví dụ của nguồn.
- Không có owner review thì trạng thái vẫn là `review`, chưa phải policy được phê duyệt.

## Reference
1. [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]]
2. [[SRC-ADAMSON-STAR-SCHEMA-COMPLETE-REFERENCE]]
3. [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-KIMBALL-ROSS-DW-TOOLKIT-3E]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-ADAMSON-STAR-SCHEMA-COMPLETE-REFERENCE]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-SILBERSCHATZ-DATABASE-SYSTEM-CONCEPTS-7E]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Bắt đầu từ nghĩa, context, grain, identity, time và ownership; schema và công cụ là phần triển khai.
- Mọi trường hợp unmatched, unknown hoặc duplicated definition phải có trạng thái quan sát được, không được mất trong im lặng.
- Tài liệu chỉ đạt khi một người khác dùng đúng mà không dựa vào trí nhớ của tác giả.
- So sánh mô hình chỉ hợp lệ sau khi kết quả ngữ nghĩa đã được đối chiếu trên cùng dữ liệu và cutoff.
- Chưa chạy phép kiểm thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.
