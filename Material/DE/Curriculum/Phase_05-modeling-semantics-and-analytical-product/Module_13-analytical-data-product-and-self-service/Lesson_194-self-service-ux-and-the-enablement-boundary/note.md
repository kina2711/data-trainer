# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 194: Self-Service UX and the Enablement Boundary

## Mục tiêu bài học

**Năng lực cần chứng minh.** Chấm mức tự phục vụ hiện tại theo bốn điều kiện và xác định ranh giới hỗ trợ cho một đội cho trước.

**Điều kiện hoàn thành.** Bốn điều kiện được chấm có bằng chứng, phân đúng ≥ 7/10 câu hỏi vào ba mức, và ranh giới hỗ trợ nêu rõ hai phía.

> [!abstract] Câu hỏi trung tâm
> Một data product chỉ được gọi là self-service khi bốn điều kiện nào có bằng chứng, và ranh giới hỗ trợ được thiết kế ra sao để vừa giảm phụ thuộc vừa không đẩy rủi ro sang người dùng?

## 1. Self-service là khả năng hoàn tất việc

Cấp quyền chỉ mở một cánh cửa. Self-service đạt khi người dùng thuộc persona đã định có thể tìm đúng product, hiểu nghĩa, thao tác bằng interface phù hợp và tin kết quả trong một class câu hỏi, với mức trợ giúp đã công bố. Scope phải nêu role, task, stakes, environment và excluded decisions. Một analyst tự viết SQL phức tạp không chứng minh business user tự phục vụ; một dashboard dễ dùng cũng không chứng minh metric đúng. GOV.UK nhấn mạnh thành công lần đầu với trợ giúp tối thiểu và kiểm với actual/likely users; giáo trình chuyển nguyên tắc đó sang analytical product.

## 2. Bốn điều kiện và evidence

Findable: task test có success/time/failed terms. Understandable: explain-back về grain, population, time, dimensions và limits. Usable: hoàn tất representative task qua public interface mà không cần workaround hay SQL vượt năng lực persona. Trustworthy: result reconciled, freshness/quality/security visible và người dùng phản ứng đúng khi status degraded. Chấm pass/partial/fail với locator và observation, không chấm cảm nhận. Bốn điều kiện là AND gate trong scope; access count, page views hoặc training attendance không thay được.

## 3. Ba mức câu hỏi

Mức 1 repeatable lookup: câu hỏi chuẩn, metric certified, dimensions hợp lệ, thao tác có path rõ. Mức 2 bounded exploration: slice/comparison mới nhưng vẫn trong semantic contract; cần skill về filters, uncertainty và data quality. Mức 3 analytical investigation: ambiguity, causal inference, forecast, policy trade-off hoặc novel modeling; cần analyst/data scientist và review. Classification dựa reasoning risk, reversibility, cost of error và contract coverage, không dựa chức danh người hỏi. Một câu hỏi có thể đổi mức khi product, evidence hoặc stakes đổi.

## 4. Ranh giới hỗ trợ hai phía

Data team chịu product correctness, contract, access policy, reliability, documentation, supported paths, incident communication và enablement material. Consumer chịu đặt câu hỏi trong scope, chọn đúng cohort/time, tuân thủ interpretation limits, bảo vệ exports và báo lỗi kèm context. Shared duties gồm validation cho high-stakes use, change acceptance và vocabulary. Boundary ghi service channels, response class, escalation, office hours, unsupported requests và handoff criteria. Không dùng boundary để từ chối mọi help; cũng không nhận bespoke query vô hạn.

## 5. Enablement thay cho ticket treadmill

Mỗi ticket được phân loại product defect, documentation gap, discoverability gap, access issue, skill gap hoặc novel analysis. Lỗi lặp chuyển thành product/docs/training change có owner; novel analysis đi intake riêng. Theo dõi assistance rate theo natural decision cadence, repeat-contact rate, time-to-independence và wrong-confident outcomes. Giảm ticket bằng cách từ chối hỗ trợ có thể làm metric đẹp nhưng đẩy shadow copies và sai số sang consumer. Guardrails gồm sampled outcome audit, user interviews và escalation accessibility.

## 6. Không phải mọi thứ nên tự phục vụ

Causal claim, legal/regulatory interpretation, sparse subgroup, privacy-sensitive join, novel forecast và irreversible high-stakes decision thường cần chuyên gia. Một interface có thể cho phép query nhưng policy vẫn yêu cầu review. Honest stop message phải nêu vì sao, evidence còn thiếu, ai hỗ trợ và artifact cần chuẩn bị. Đây là feature an toàn, không phải failure của UX. Mục tiêu là self-service tối đa trong bounded safe space, không phải loại bỏ chuyên gia hoặc biến mọi consumer thành data engineer.

## 7. Chấm mười câu hỏi và kiểm ranh giới

Lấy mười câu hỏi thật đủ ba mức, ẩn đáp án mẫu khỏi người chấm, ghi reasoning, contract coverage, required evidence, risk và route. Reviewer độc lập so classification; disagreements tạo decision rule mới. Với product hiện tại, chấm bốn điều kiện bằng artifact và observed task. Boundary one-pager được thử bằng tình huống: metric không reconcile, user cần causal answer, access expired, stale data, unsupported export. Done khi cả hai phía biết next action; wording “liên hệ data team” mà không owner/SLA/context yêu cầu là chưa đủ.

## 8. Ma trận kiểm chứng từng mệnh đề

Mỗi mệnh đề dưới đây cần artifact hoặc observation lưu được. Một trang tài liệu tồn tại, catalog có search box hoặc người dùng nói ‘dễ’ không tự là bằng chứng.

### 8.1. access entitlement không đồng nghĩa self-service

**Mệnh đề cần kiểm.** access entitlement không đồng nghĩa self-service.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.2. self-service luôn có persona task và risk scope

**Mệnh đề cần kiểm.** self-service luôn có persona task và risk scope.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.3. findable cần task evidence

**Mệnh đề cần kiểm.** findable cần task evidence.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.4. understandable cần explain-back

**Mệnh đề cần kiểm.** understandable cần explain-back.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.5. usable phụ thuộc public interface và persona skill

**Mệnh đề cần kiểm.** usable phụ thuộc public interface và persona skill.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.6. trustworthy cần degraded-state behavior

**Mệnh đề cần kiểm.** trustworthy cần degraded-state behavior.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.7. bốn điều kiện là AND gate trong scope

**Mệnh đề cần kiểm.** bốn điều kiện là AND gate trong scope.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.8. câu hỏi mức một là repeatable lookup

**Mệnh đề cần kiểm.** câu hỏi mức một là repeatable lookup.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.9. bounded exploration khác causal investigation

**Mệnh đề cần kiểm.** bounded exploration khác causal investigation.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.10. classification dựa reasoning risk không dựa title

**Mệnh đề cần kiểm.** classification dựa reasoning risk không dựa title.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.11. support boundary nêu trách nhiệm hai phía

**Mệnh đề cần kiểm.** support boundary nêu trách nhiệm hai phía.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.12. repeated ticket trở thành product finding

**Mệnh đề cần kiểm.** repeated ticket trở thành product finding.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.13. ticket reduction cần wrong-outcome guardrail

**Mệnh đề cần kiểm.** ticket reduction cần wrong-outcome guardrail.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.14. high-stakes causal question cần expert review

**Mệnh đề cần kiểm.** high-stakes causal question cần expert review.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

### 8.15. stop message phải có rationale và next action

**Mệnh đề cần kiểm.** stop message phải có rationale và next action.

**Cách kiểm.** Chấm bốn điều kiện bằng artifacts và observed tasks; phân loại mười câu hỏi theo repeatable lookup, bounded exploration hoặc expert investigation. Diễn tập năm support scenarios để kiểm owner, escalation, context và stop boundary. Với mệnh đề này, ghi participant/task hoặc artifact version, điều kiện đầu vào, expected observation, failure signal và yếu tố làm kết luận không còn đúng.

**Bằng chứng đạt.** Lưu protocol hoặc command, raw observations, numerator/denominator nếu có, exact product/docs version, reviewer và artifact hash. Nếu chưa chạy study/lab, chỉ ghi đây là protocol; không biến expected result thành kết quả quan sát.

## 9. Quy trình phản biện

1. Viết user need, task, persona, stakes và scope trước khi chọn catalog, tài liệu hoặc metric.
2. Tách source fact, curriculum synthesis, organizational policy và observation từ study.
3. Khóa task/protocol/oracle trước khi đo; mọi deviation phải được ghi.
4. Kiểm correct outcome và interpretation, không chỉ completion hoặc cảm nhận.
5. Phân loại lỗi theo cơ chế để sửa đúng lớp: metadata, docs, interface, trust, access hay skill.
6. Kiểm changed user group, changed task và degraded state trước khi khái quát.
7. Chưa có execution evidence thì giữ trạng thái `review`.

## 10. Câu hỏi tự kiểm tra

1. User task nào đang được hỗ trợ, và điều gì nằm ngoài scope?
2. Oracle nào xác định product hoặc kết quả đúng?
3. Số đo dùng denominator nào và loại invalid attempt theo rule nào?
4. Điểm nào cần automation, điểm nào bắt buộc human judgment?
5. Một kết quả nhanh nhưng sai nghĩa được phát hiện ở đâu?
6. Điều kiện nào làm kết luận từ sample hoặc catalog hiện tại không còn áp dụng?

## 11. Giới hạn và điều chưa cho phép kết luận

- Chưa chạy user study, catalog experiment, documentation CI hoặc support-boundary exercise; note mô tả protocol và expected evidence.
- Tài liệu web được kiểm ngày 2026-10-01; tính năng, giao diện, license và guidance có thể đổi.
- Bốn tầng documentation, bốn điều kiện self-service và bốn số đo của module là curriculum synthesis; không gán nguyên văn cho một nguồn.
- Cỡ mẫu nhỏ cho formative discovery không cho phép kết luận tỷ lệ toàn population hoặc statistical significance.
- Dữ liệu người tham gia, recording và screen capture cần consent, minimization, retention và access controls riêng.
- Note giữ trạng thái `review` cho tới khi chủ dự án duyệt semantic meaning.

## Reference
1. [[SRC-DEHGHANI-DATA-MESH-PRINCIPLES]]
2. [[SRC-GOVUK-SIMPLE-TO-USE]]
3. [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]]

## Source coverage

| Source slice | Nội dung sử dụng | Trạng thái |
|---|---|---|
| [[SRC-DEHGHANI-DATA-MESH-PRINCIPLES]] | Khái niệm, mechanism hoặc study boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-GOVUK-SIMPLE-TO-USE]] | Khái niệm, mechanism hoặc study boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |
| [[SRC-GOVUK-UNDERSTAND-USER-NEEDS]] | Khái niệm, mechanism hoặc study boundary liên quan | Đã đọc locator trong source record; không suy ngoài phạm vi |

## Key takeaways
- Self-service là bounded capability gồm find, understand, use và trust; không phải số tài khoản được cấp quyền.
- Chỉ số phải gắn task, persona, product version, protocol và denominator.
- Correct completion gồm cả kết quả và cách diễn giải đúng; confident-wrong là failure nghiêm trọng.
- Công cụ catalog, docs generator và CI cung cấp mechanism, không tự chứng minh outcome.
- Chưa chạy study hoặc lab thì artifact là tài liệu học thuật đã kiểm cấu trúc, không phải chứng nhận thực tế.
