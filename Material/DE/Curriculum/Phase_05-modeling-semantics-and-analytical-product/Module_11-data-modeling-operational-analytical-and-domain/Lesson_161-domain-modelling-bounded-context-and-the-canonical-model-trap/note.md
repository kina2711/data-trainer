# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 161: Domain Modelling, Bounded Context and the Canonical Model Trap

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nhận ra hai ngữ cảnh giới hạn xung đột nhau trong một mô tả và đề xuất cách tích hợp bằng hợp đồng.

**Điều kiện hoàn thành.** Chỉ đúng ≥ 2 từ mang hai nghĩa, và đề xuất tích hợp bằng hợp đồng kèm định nghĩa theo từng ngữ cảnh.

> [!abstract] Câu hỏi trung tâm
> Khi nhiều đội dùng cùng một từ với nghĩa khác nhau, làm thế nào giữ mô hình riêng của từng context nhưng vẫn tích hợp được mà không dựng một canonical model khổng lồ?

## 1. Mô hình chỉ đúng trong một ngữ cảnh

Một domain model là tập khái niệm, quy tắc và quan hệ được dùng để giải quyết một nhóm vấn đề. Từ `customer` có thể là pháp nhân ký hợp đồng trong sales, người đang dùng sản phẩm trong product, người mở ticket trong support và đối tượng chịu kiểm soát trong risk. Các định nghĩa không nhất thiết cạnh tranh; chúng trả lời câu hỏi khác nhau. Bounded context đặt ranh giới nơi một vocabulary và model có thể nhất quán. Bên trong ranh giới, tên phải ổn định; đi qua ranh giới, nghĩa phải được dịch có chủ ý.

## 2. Phát hiện xung đột ngữ nghĩa

Xung đột không chỉ là hai cột cùng tên. Cần so identity, lifecycle, cardinality, time và authority. Sales có thể nhận dạng customer bằng contract account; support bằng contact; billing bằng payer. Một context coi merge account là correction, context khác coi là event. Cùng `revenue` nhưng thời điểm ghi nhận, currency, refund và tax khác nhau sẽ tạo số khác dù schema giống hệt. Bảng so sánh phải ghi term, context, definition, identifier, valid time, owner và permitted uses.

## 3. Canonical-model trap

Canonical enterprise model thường bắt đầu với mục tiêu giảm trùng lặp nhưng dễ trở thành phép hợp của mọi thuộc tính, mọi trạng thái và mọi ngoại lệ. Một thay đổi cục bộ kéo theo review toàn công ty; trường optional tăng; ownership mờ; release của một đội bị chặn bởi đội khác. Vấn đề không phải mọi canonical artifact đều sai. Một chuẩn trao đổi hẹp hoặc reference data chung có thể hữu ích. Cái bẫy là coi một model toàn cục, giàu chi tiết và thay đổi đồng bộ là điều kiện bắt buộc trước khi các miền được vận hành.

## 4. Tích hợp bằng hợp đồng và mapping

Mỗi context giữ model nội bộ, rồi công bố contract nhỏ cho nhu cầu trao đổi. Contract phải nêu producer, consumer, event/entity grain, identity, schema, semantics, time, compatibility, quality, ownership và version. Mapping đứng ở boundary: `sales_contract_account_id` có thể ánh xạ sang một hay nhiều `support_contact_id`, kèm effective period và confidence nếu cần. Anti-corruption layer hoặc translation view ngăn vocabulary ngoại lai lan vào model nội bộ. Không dùng rename như biện pháp chữa xung đột; đổi tên chỉ có giá trị khi đi kèm định nghĩa và phép ánh xạ.

## 5. Context map và ownership

Context map ghi quan hệ upstream/downstream, published language, conformist, customer-supplier hoặc translation boundary. Nó làm rõ đội nào có quyền thay contract, đội nào chịu migration và thời hạn deprecation. Ownership dữ liệu theo miền không có nghĩa producer tự quyết mọi thứ: consumer requirements, privacy, interoperability và governance vẫn tạo ràng buộc. Một contract không có owner, changelog, compatibility test và kênh thông báo chỉ là tài liệu tĩnh.

## 6. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần một dữ liệu phản ví dụ, một invariant và một bằng chứng chạy lại được. Tên pattern, sơ đồ hoặc một query chạy thành công không đủ để xác nhận đúng ngữ nghĩa.

### 6.1. customer có identity khác nhau giữa sales và support

**Mệnh đề cần kiểm.** customer có identity khác nhau giữa sales và support.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.2. cùng tên cột không chứng minh cùng nghĩa

**Mệnh đề cần kiểm.** cùng tên cột không chứng minh cùng nghĩa.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.3. khác tên không chứng minh khác nghĩa

**Mệnh đề cần kiểm.** khác tên không chứng minh khác nghĩa.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.4. lifecycle và valid time là một phần của definition

**Mệnh đề cần kiểm.** lifecycle và valid time là một phần của definition.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.5. canonical model dạng union tạo nhiều optional fields

**Mệnh đề cần kiểm.** canonical model dạng union tạo nhiều optional fields.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.6. một model toàn cục làm tăng change blast radius

**Mệnh đề cần kiểm.** một model toàn cục làm tăng change blast radius.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.7. published contract phải nhỏ hơn internal model

**Mệnh đề cần kiểm.** published contract phải nhỏ hơn internal model.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.8. mapping phải có cardinality và effective period

**Mệnh đề cần kiểm.** mapping phải có cardinality và effective period.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.9. anti-corruption layer bảo vệ vocabulary nội bộ

**Mệnh đề cần kiểm.** anti-corruption layer bảo vệ vocabulary nội bộ.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.10. rename không thay semantic mapping

**Mệnh đề cần kiểm.** rename không thay semantic mapping.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.11. shared kernel chỉ phù hợp phạm vi nhỏ và ổn định

**Mệnh đề cần kiểm.** shared kernel chỉ phù hợp phạm vi nhỏ và ổn định.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.12. context boundary không bắt buộc trùng org chart

**Mệnh đề cần kiểm.** context boundary không bắt buộc trùng org chart.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.13. owner phải chịu compatibility và deprecation

**Mệnh đề cần kiểm.** owner phải chịu compatibility và deprecation.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.14. glossary phải giữ nhiều định nghĩa theo context

**Mệnh đề cần kiểm.** glossary phải giữ nhiều định nghĩa theo context.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

**Điều kiện kết luận.** Chỉ đánh dấu đạt khi artifact thực thi cho kết quả lặp lại ở cùng cutoff và không vi phạm grain, identity, time hoặc ownership contract. Nếu chưa thực thi, trạng thái là thiết kế kiểm chứng, không phải kết quả production.

### 6.15. integration test phải kiểm meaning chứ không chỉ schema

**Mệnh đề cần kiểm.** integration test phải kiểm meaning chứ không chỉ schema.

**Cách kiểm.** Dùng ba context sales, support và billing. Lập bảng term–identity–lifecycle–time–owner; viết contract trao đổi và mapping cardinality/effective period. Thử một schema change cục bộ để đo số artifacts và teams bị ảnh hưởng. Tách phép kiểm cấu trúc khỏi xác nhận của owner về business meaning. Lưu input snapshot, assumptions, executable query/test, output thô, control totals và phản ví dụ.

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
1. [[SRC-BOYLE-DDD-GOLANG-1E]]
2. [[SRC-STOPFORD-DESIGNING-EVENT-DRIVEN-SYSTEMS]]
3. [[SRC-FOWLER-BOUNDED-CONTEXT]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-BOYLE-DDD-GOLANG-1E]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-STOPFORD-DESIGNING-EVENT-DRIVEN-SYSTEMS]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |
| [[SRC-FOWLER-BOUNDED-CONTEXT]] | Khái niệm, cơ chế và giới hạn liên quan trực tiếp | Đã đọc phạm vi có locator; không suy ngoài phạm vi |

## Key takeaways
- Bắt đầu từ nghĩa, context, grain, identity, time và ownership; schema và công cụ là phần triển khai.
- Mọi trường hợp unmatched, unknown hoặc duplicated definition phải có trạng thái quan sát được, không được mất trong im lặng.
- Tài liệu chỉ đạt khi một người khác dùng đúng mà không dựa vào trí nhớ của tác giả.
- So sánh mô hình chỉ hợp lệ sau khi kết quả ngữ nghĩa đã được đối chiếu trên cùng dữ liệu và cutoff.
- Chưa chạy phép kiểm thì note là tài liệu học thuật có truy nguồn, không phải chứng nhận production.
