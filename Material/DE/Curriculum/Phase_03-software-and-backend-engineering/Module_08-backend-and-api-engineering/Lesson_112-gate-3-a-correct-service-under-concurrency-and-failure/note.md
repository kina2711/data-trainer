# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 112: Gate 3 - a correct service under concurrency and failure

## Mục tiêu bài học

**Năng lực cần chứng minh.** Nộp một dịch vụ giữ đúng bất biến dưới truy cập đồng thời và dưới sự cố, với bằng chứng từ phép kiểm chạy song song.

**Điều kiện hoàn thành.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Bất biến nào chỉ được chứng minh bằng phép kiểm tuần tự thì không tính điểm ở phần C.

> [!abstract] Phạm vi
> Đây là bản thiết kế đánh giá, không dạy thêm khái niệm. Bài thi yêu cầu học viên chứng minh các năng lực đã học bằng code, phép thử lặp lại được, telemetry và giải thích kỹ thuật.

## 1. Construct cần đo

Gate đo sáu năng lực: tách core khỏi dependency; giữ idempotency qua retry; bảo toàn invariant dưới concurrency; đặt timeout/retry có giới hạn; chẩn đoán bằng telemetry; ngăn truy cập trái ownership. Điểm không được cộng cho framework nhiều, giao diện đẹp hoặc slide trau chuốt nếu không tạo bằng chứng cho construct.

Assessment phải tránh construct under-representation: chỉ unit test core sẽ bỏ concurrency, failure và security. Đồng thời tránh construct-irrelevant variance: lỗi setup không liên quan không nên chi phối toàn bộ nếu candidate cung cấp reproducible environment đúng contract.

## 2. Artifact đầu vào

- repository và commit SHA;
- lệnh dựng/chạy/test một lần từ môi trường sạch;
- dependency graph hoặc module map;
- schema/migration;
- automated tests và fault-injection harness;
- raw results, metric query, logs/traces cần thiết;
- ngắn gọn ADR về idempotency, transaction boundary và failure semantics;
- threat model và negative authorization tests.

Không chấp nhận video/screenshot thay cho artifact thực thi. Evidence có thể gồm ảnh để đọc nhanh nhưng grader phải chạy lại được.

## 3. Môi trường kiểm tra

Pin runtime/dependency version, seed data và config không chứa secret. Grader chạy baseline, sau đó fault cases theo script. Thời gian, concurrency và random seed được lưu. Nếu test phụ thuộc timing, chạy nhiều lần và báo flake rate; một lần pass không đủ.

External service được stub có contract và injected latency/error rõ. Candidate không được gọi production hoặc site bên thứ ba. Database thật được dùng cho behavior phụ thuộc transaction/lock; in-memory fake không thay thế được.

## 4. Rubric A — dependency graph và core không phụ thuộc DB (15)

Điểm đầy đủ khi business policy có thể chạy bằng deterministic unit test không khởi động DB/network; ports biểu diễn dependency thực; adapter chịu trách nhiệm serialization/persistence; dependency direction kiểm được bằng import/build rule. “Có thư mục domain” nhưng entity gọi ORM/global client không đạt.

Bằng chứng: graph, một core test, một adapter integration test, và chỉ ra boundary. Trừ điểm khi abstraction chỉ bọc library mà không bảo vệ policy hoặc khi test mock toàn bộ đến mức không kiểm logic.

## 5. Rubric B — idempotent retry (25)

Candidate phải định nghĩa scope/key/payload equivalence, durable record, concurrent duplicate và failure trước/sau commit. Phép thử gửi 50 request cùng key; tất cả quan sát cùng logical result; side effect chỉ một lần. Cùng key khác payload phải có deterministic conflict.

Timeout response được retry bằng cùng key. Evidence gồm DB constraints/query, request/result table và side-effect counter. Check-then-act không constraint, key lưu trong memory hoặc duplicate chỉ test tuần tự không đạt điểm chính.

## 6. Rubric C — concurrency với 50 threads (20)

Chọn invariant định lượng, ví dụ balance không âm, chỉ một owner hoặc version tăng không mất update. Barrier đồng bộ 50 worker tạo race window. Test chạy lặp, assert final state và số success/conflict. Giải pháp phải giải thích optimistic/pessimistic/atomic update và behavior khi contention.

Nếu candidate chỉ chạy tuần tự, phần C bằng 0 dù kết quả cuối đẹp. Nếu dùng global mutex chỉ hoạt động một process nhưng claim distributed correctness, không đạt. Lock/transaction phải được đặt đúng scope và timeout/deadlock path có xử lý.

## 7. Rubric D — timeout và retry limits (15)

Mọi network call có deadline phù hợp request budget; retry chỉ với lỗi an toàn/retryable; max attempts, backoff+jitter và total deadline hữu hạn. Fault test làm dependency chậm/lỗi và chứng minh request không treo, work không nhân vô hạn, pool không cạn. Retry nested không được làm số attempt bùng theo cấp số nhân.

Bằng chứng gồm timeline, config và metric attempts. Circuit/bulkhead nếu có phải được kiểm state/isolation; chỉ thêm library không có fault test không có điểm.

## 8. Rubric E — telemetry chẩn đoán (15)

Một injected failure phải được chẩn đoán mà không đọc code: metric cho thấy rate/error/duration hoặc saturation; log có stable reason/correlation; trace chỉ ra critical path khi phù hợp. Candidate nêu query và kết luận, đồng thời chứng minh không log secret/PII.

Dashboard nhiều panel nhưng không trả câu hỏi được tính thấp. Request ID không truyền qua hop hoặc high-cardinality user ID trong metric là lỗi thiết kế.

## 9. Rubric F — negative authorization tests (10)

Ít nhất ba test: unauthenticated; authenticated sai owner; role thiếu quyền. Query phải scope resource theo owner/tenant hoặc policy tương đương. Đổi object ID không được đọc/sửa tài nguyên khác. Response tránh leak không cần thiết; audit event có actor/action/outcome.

Happy-path authentication không chứng minh authorization. Chỉ ẩn nút UI hoặc dùng ID khó đoán bằng 0 cho ownership control.

## 10. Hard gates và cách tính

Tổng 100, đạt từ 70; đồng thời B và C mỗi phần phải đạt ít nhất 60% số điểm phần đó. Hard gate này ngăn một service sai retry/concurrency bù bằng tài liệu. Security critical failure như truy cập cross-tenant đã tái hiện được có thể buộc remediation trước khi pass, dù tổng điểm đủ; policy phải công bố trước kỳ thi.

Grader ghi điểm theo evidence ID, không theo cảm giác. Hai grader chấm độc lập một sample đầu để hiệu chỉnh. Chênh lệch lớn phải thảo luận rubric descriptor, không chia trung bình máy móc.

## 11. Kịch bản điều hành

1. Verify clean build và baseline tests.
2. Review dependency boundary bằng một trace từ entry đến adapter.
3. Chạy duplicate/idempotency suite.
4. Chạy concurrency suite 50 threads nhiều vòng.
5. Inject timeout/retry failure.
6. Yêu cầu candidate chẩn đoán từ telemetry.
7. Chạy negative authorization suite.
8. Ghi evidence, điểm và remediation.

Không đổi kịch bản giữa candidates ngoài accommodation đã phê duyệt. Nếu infrastructure của grader lỗi, đánh dấu invalid attempt và chạy lại, không chấm fail candidate.

## 12. Critical failures cần phân biệt

- dữ liệu sai hoặc invariant bị phá;
- duplicate side effect dưới retry;
- test race chỉ tuần tự;
- timeout vô hạn/retry storm;
- cross-tenant access;
- secret xuất hiện trong log;
- evidence không tái hiện được.

Style issue, naming hoặc minor documentation gap không được đánh đồng với correctness failure. Severity phải phản ánh impact và khả năng tái hiện.

## 13. Remediation

Feedback nêu invariant nào vỡ, lệnh tái hiện, evidence và năng lực cần sửa. Candidate sửa phạm vi hẹp rồi chạy lại phần liên quan cùng regression suite. Không cho “viết lại toàn dự án” nếu lỗi chỉ ở transaction boundary; không pass chỉ vì giải thích miệng đúng khi artifact vẫn sai.

## 14. Evidence ledger

Mỗi rubric item có evidence ID, command, expected invariant, actual output, timestamp, environment fingerprint và grader note. Evidence ledger ngăn việc một artifact mơ hồ được dùng để cộng điểm nhiều phần. Ví dụ trace chẩn đoán dependency timeout hỗ trợ E; nó không tự chứng minh retry idempotent ở B. Concurrency result phải giữ iteration count và failure distribution, không chỉ dòng cuối `PASS`.

Khi candidate dùng alternative design, grader chấm outcome/invariant thay vì ép một pattern. Optimistic version, row lock hoặc atomic SQL đều có thể đạt C nếu proof đúng. Tuy nhiên explanation không cứu được implementation phá invariant. Ngược lại, code tình cờ pass một run nhưng candidate không chỉ ra boundary và repeatability cũng chưa đủ evidence.

## 15. Phân tích flakiness và false pass

Race test có thể false pass khi threads không thực sự overlap. Barrier, injected delay tại critical window và nhiều iteration tăng sức phát hiện. Test timeout có thể false pass vì stub trả lỗi ngay thay vì treo. Authorization test có thể false pass vì object B không tồn tại. Dataset và assertions phải chứng minh precondition trước khi thực thi hành vi cần chấm.

Flaky test không tự động là lỗi candidate hoặc grader. Ghi seed, schedule evidence và infrastructure health; phân loại product race, brittle assertion, resource shortage hay harness defect. Chỉ retry đến khi xanh là che lỗi. Báo pass rate và sửa root cause trước quyết định cuối.

## 16. Câu hỏi tự kiểm tra

1. Evidence nào chứng minh core không phụ thuộc database thay vì chỉ nằm ở thư mục khác?
2. Duplicate test tuần tự bỏ sót race nào?
3. Một injected timeout phải quan sát attempt budget và pool health ra sao?
4. Vì sao cross-tenant read là critical failure dù tổng điểm trên 70?
5. Grader calibration giảm loại bất nhất nào?

## 17. Giới hạn và điều chưa cho phép kết luận

- Gate đo phạm vi Phase 3, không chứng nhận toàn bộ năng lực production engineering.
- Năm fault family không bao phủ mọi network partition, data corruption hay supply-chain attack.
- Điểm số chỉ so sánh được khi environment, rubric và accommodations nhất quán.
- Telemetry evidence phụ thuộc instrumentation đã cài; missing signal không tự chứng minh code path không chạy.

Gate cũng không đo khả năng tối ưu chi phí, thiết kế dữ liệu dài hạn hoặc vận hành nhiều vùng. Một service đạt bài vẫn có thể thiếu disaster recovery, privacy review, capacity forecast hay schema evolution strategy. Kết quả cần được ghi là “đạt các outcomes của Phase 3 trong environment kiểm tra”, không phải “production-ready” chung chung. Cách ghi phạm vi này bảo vệ tính trung thực của assessment và giúp module sau biết chính xác năng lực nào còn phải xây tiếp.

## Source coverage

| Source slice | Nội dung phải giữ | Vị trí trong note | Trạng thái |
|---|---|---|---|
| [[SRC-NEWMAN-BUILDING-MICROSERVICES-2E]] | boundaries, testing và operability | §§1–4 | Đã dùng làm nền assessment |
| [[SRC-POSTGRESQL-CONCURRENCY-CONTROL]] | transaction/concurrency behavior | §6 | Đã gắn với executable evidence |
| [[SRC-RFC9110-HTTP-SEMANTICS]] | timeout và retry semantics | §§5, 7 | Đã giữ ambiguity boundary |
| [[SRC-OWASP-BOLA-2023]] | object-level authorization | §9 | Đã chuyển thành negative tests |
| [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]] | resilience/observability | §§7–8 | Đã dùng cho fault evidence |
| [[SRC-OPENTELEMETRY-SIGNALS]] | metrics, logs, traces | §8 | Đã giới hạn theo instrumentation |
| Tổng hợp Gate 3 | rubric, hard gate, calibration | §§10–16 | Đã ghi thành assessment protocol |

## Key takeaways
- Gate đo evidence của correctness, không đo độ đẹp demo.
- Idempotency và concurrency là hard gates, không được bù bằng phần khác.
- Fault injection phải có invariant assertion và raw artifact.
- Authorization cần negative tests theo ownership.
- Rubric phải dùng descriptor tái hiện được và hiệu chỉnh grader.

## Reference
1. [[SRC-NEWMAN-BUILDING-MICROSERVICES-2E]] — boundaries/testing.
2. [[SRC-POSTGRESQL-CONCURRENCY-CONTROL]] — concurrency.
3. [[SRC-RFC9110-HTTP-SEMANTICS]] — HTTP semantics.
4. [[SRC-OWASP-BOLA-2023]] — object authorization.
5. [[SRC-TITMUS-CLOUD-NATIVE-GO-1E]] — resilience.
6. [[SRC-OPENTELEMETRY-SIGNALS]] — telemetry signals.
