---
marp: true
theme: default
paginate: true
title: "DA-L001: What a Data Analyst actually does all day"
---

# What a Data Analyst actually does all day

DA-L001

**Câu hỏi trung tâm:** DA tạo giá trị ở đâu từ yêu cầu tới quyết định?

<!-- scene: S01 | source: note.md heading 'Giá trị bắt đầu từ quyết định, không bắt đầu từ dashboard' -->

---

## Mục tiêu kiểm chứng được

- khóa consumer, decision, question, evidence và action
- phân vai bằng trách nhiệm và artifact
- audit một claim trước khi khuyến nghị
- viết memo có owner và reversal trigger

---

## Một dashboard, ba hành động khác nhau

Dashboard báo revenue tháng 10 giảm 12%.

- Thiếu dữ liệu: mở incident
- Khách mới giảm: điều tra acquisition
- Khách cũ giảm: điều tra retention

**Output giống nhau. Cơ chế và owner khác nhau.**

---

## Câu hỏi phải đứng trước query

> Nếu kết quả là A, B hoặc chưa đủ chắc chắn, ai sẽ thay đổi quyết định gì?

| Khóa | Case |
|---|---|
| Consumer | Trưởng bộ phận bán lẻ |
| Decision | Giữ hay cắt ngân sách |
| Evidence | Transaction và coverage |

---

## Luồng kiểm soát

 Ask -> Prepare -> Process -> Analyze -> Share -> Act
 ^ |
 +------------------------------------------------+

<!-- scene: S02 | source: note.md heading 'Sáu pha tạo thành một vòng kiểm soát' -->

---

## Checkpoint 1

Ở pha Process, bạn phát hiện Đà Nẵng thiếu 11 ngày dữ liệu.

Chọn hành động đầu tiên và giải thích:

1. Vẽ chart đẹp hơn
2. Tiếp tục tìm nguyên nhân kinh doanh
3. Quay lại source, cutoff và coverage

<!-- scene: S03 | expected: option 3 -->

---

## Vai trò không phải danh sách công cụ

| Vai | Sở hữu |
|---|---|
| DA | conclusion và recommendation |
| DE | data flow và recovery |
| AE | model và metric dùng chung |
| BI | trải nghiệm theo dõi |
| BA | requirement và process |
| DS | estimate và forecast |

---

## Phân vai bằng critical failure

Nếu artifact hỏng:

- Ai giải thích hậu quả cho consumer?
- Invariant nào bị phá?
- Ai sửa cơ chế?
- Ai xác nhận handoff hoàn tất?

SQL và Python không trả lời bốn câu này.

<!-- scene: S05 | source: note.md heading 'Ranh giới vai trò nằm ở thứ phải chịu trách nhiệm' -->

---

## Guided practice: tám thẻ việc

- sửa pipeline mất dữ liệu
- định nghĩa net revenue
- dashboard ngày
- phân tích churn
- dự báo churn
- đặc tả hoàn tiền
- đối soát hai báo cáo
- trình bày khuyến nghị

Nộp: role, artifact, consumer, failure, handoff.

<!-- scene: S04 | source: UNSOURCED guided practice -->

---

## Case: 12% có thật không?

| Tháng | Dashboard |
|---|---:|
| 09 | 3,00 tỷ |
| 10 | 2,64 tỷ |

Quan sát ban đầu: giảm 12%.

Chưa được phép kể câu chuyện nguyên nhân.

---

## Reconciliation trước explanation

| Tháng 10 | Giá trị |
|---|---:|
| Dashboard cũ | 2,64 tỷ |
| Bổ sung Đà Nẵng | 0,24 tỷ |
| Reconciled | 2,88 tỷ |

Mức giảm trong boundary: 4%.

---

## Decomposition không phải causal proof

| Nhóm | Tháng 09 | Tháng 10 | Chênh |
|---|---:|---:|---:|
| Khách cũ | 2,10 | 2,12 | +0,02 |
| Khách mới | 0,90 | 0,76 | -0,14 |

Biến động tập trung ở khách mới.

**Chưa đủ để nói marketing gây ra giảm.**

<!-- scene: S07 | source: note.md heading 'Một con số chỉ có giá trị khi giữ được chuỗi lập luận' -->

---

## Changed constraint

Công ty chỉ có một người dữ liệu.

- Phạm vi thực thi rộng hơn
- Tiêu chí hoàn thành không biến mất
- Mỗi mũ vẫn có artifact và invariant

<!-- scene: S06 | source: UNSOURCED changed-constraint scenario -->

---

## Transfer challenge

Viết memo cho case revenue:

- tách incident dữ liệu khỏi business action
- giữ claim trong strength của evidence
- có owner, deadline và trigger đảo quyết định

<!-- scene: S08 | source: UNSOURCED curriculum transfer scenario -->

---

## Exit check

DA và DE cùng điều tra dữ liệu thiếu. Khác nhau ở điều gì?

- fitness-for-decision và conclusion
- ingestion, delivery và recovery
- evidence chung nhưng failure ownership khác

<!-- scene: S09 -->

---

## Mang theo sau buổi học

Không hỏi cần dashboard nào? trước.

> Quyết định nào đang bị chặn, bằng chứng nào đủ và ai chịu trách nhiệm cho hành động tiếp theo?

---

## References

- [[wiki.da.operating-as-a-data-analyst|Operating as a Data Analyst]]
- [[wiki.data-product.decision-first-discovery|Decision-First Discovery]]
- [[wiki.da.revenue-and-commerce-analytics|Revenue and commerce analytics]]
