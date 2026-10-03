# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 320: History analysis project - judge a guarantee from evidence

## Thực hành

**Nhiệm vụ.** Nhận bốn lịch sử, trong đó một lịch sử hợp lệ. Viết bộ kiểm cho thanh ghi. Với mỗi lịch sử vi phạm, chỉ ra chuỗi thao tác cụ thể chứng minh. Chạy thử nghiệm riêng có tiêm phân vùng và lệch đồng hồ, thu lịch sử và phân tích. Nộp bảng bảo đảm với giả định và chế độ hỏng phá vỡ.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp toàn module thành một năng lực lập luận có bằng chứng. Kiểm bằng bốn lịch sử cộng rà soát bộ kiểm; đạt khi xác định đúng ít nhất ba kèm chuỗi thao tác chứng minh, và giới hạn của bộ kiểm được nêu rõ.

**Điều kiện đạt.** Xác định đúng ≥ 3/4 lịch sử kèm chuỗi thao tác chứng minh, lịch sử hợp lệ không bị báo nhầm, và giới hạn bộ kiểm được nêu rõ.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Tuyên bố đã kiểm chứng toàn hệ từ một bộ kiểm nhỏ · kết luận vi phạm mà không chỉ ra chuỗi thao tác · dùng dấu thời gian cục bộ làm thứ tự toàn cục · bỏ lịch sử hợp lệ nên không kiểm được báo giả.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/208-history-analysis-project-judge-a-guarantee-from-evidence.md`
- Nội dung học thuật: `note.md` cùng thư mục.
