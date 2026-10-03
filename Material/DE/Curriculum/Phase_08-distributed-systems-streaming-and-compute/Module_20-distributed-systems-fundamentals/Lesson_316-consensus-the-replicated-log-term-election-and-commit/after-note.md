# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 316: Consensus - the replicated log, term, election and commit

## Thực hành

**Nhiệm vụ.** Cài bầu chọn người dẫn và sao chép nhật ký cho cụm năm nút. Chạy 200 chu kỳ giết ngẫu nhiên một hoặc hai nút rồi cho khôi phục, kèm phân vùng mạng ngắn. Sau mỗi chu kỳ, kiểm ba tính chất an toàn. Tái hiện ca người dẫn cũ quay lại và chứng minh nó bị từ chối bằng nhiệm kỳ. Vẽ trình tự một lần chốt đi qua một lần người dẫn chết.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là bất biến an toàn giữ được dưới lỗi ngẫu nhiên. Kiểm bằng phép thử hỗn loạn; đạt khi ba tính chất an toàn không bị vi phạm lần nào qua 200 chu kỳ giết và khôi phục nút.

**Điều kiện đạt.** Ba tính chất an toàn không bị vi phạm qua 200 chu kỳ, và ca người dẫn cũ quay lại bị từ chối bằng nhiệm kỳ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bầu người dẫn mà không so nhật ký nên mất mục đã chốt · dùng thời gian phát hiện nhanh thay cho nhiệm kỳ · chỉ kiểm ở trường hợp thuận lợi · nhầm đã sao chép với đã chốt.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/204-consensus-the-replicated-log-term-election-and-commit.md`
- Nội dung học thuật: `note.md` cùng thư mục.
