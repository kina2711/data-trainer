# Phase 8: Distributed Systems, Streaming and Compute
# Module 20: Distributed Systems Fundamentals
# Lesson 314: Consistency models named by what the client observes

## Thực hành

**Nhiệm vụ.** Cho bốn lịch sử thao tác của một thanh ghi; với mỗi cái, xác định mô hình nào bị vi phạm và giải thích bằng lời gọi cùng phản hồi cụ thể. Lấy tài liệu của hai hệ thật và phát biểu lại bảo đảm của chúng theo năm mô hình. Với một hệ hứa cuối cùng nhất quán, tìm hợp đồng về mức cũ tối đa; nếu không có thì ghi rõ là không có.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho hai bài về số đông và đồng thuận. Kiểm bằng bài phân tích bốn lịch sử thao tác; đạt khi xác định đúng mô hình bị vi phạm ở ít nhất ba và nêu được đánh đổi khi không có phân vùng.

**Điều kiện đạt.** Xác định đúng mô hình bị vi phạm ở ≥ 3/4 lịch sử, và hai hệ thật được phát biểu lại bảo đảm theo năm mô hình.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng định lý đánh đổi để biện minh cho mọi quyết định · nói cuối cùng nhất quán mà không kèm mức cũ tối đa · nhầm tuần tự với tuần tự hoá được · đặt tên mô hình theo cơ chế bên trong.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/202-consistency-models-named-by-what-the-client-observes.md`
- Nội dung học thuật: `note.md` cùng thư mục.
