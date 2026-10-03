# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 378: Infrastructure as code - desired state and the dependency graph

## Thực hành

**Nhiệm vụ.** Cho ba bản kế hoạch thật, mỗi cái chứa ít nhất một hành động thay thế. Với mỗi cái, liệt kê bốn loại hành động và chỉ ra tài nguyên nào bị thay thế cùng thuộc tính nào gây ra. Vẽ đồ thị phụ thuộc của một tập tài nguyên và suy ra thứ tự xoá. Tạo một ca có phụ thuộc ngầm và chỉ ra lỗi thứ tự nó gây ra.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết đặt khung cho hai bài thực hành. Kiểm bằng bài đọc kế hoạch; đạt khi nhận đúng mọi hành động thay thế trong ba kế hoạch và giải thích được nguyên nhân gây thay thế.

**Điều kiện đạt.** Nhận đúng mọi hành động thay thế trong ba kế hoạch kèm thuộc tính gây ra, và thứ tự xoá suy đúng từ đồ thị phụ thuộc.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Áp dụng mà không đọc kế hoạch · bỏ qua hành động thay thế vì thấy thay đổi nhỏ · dựa vào thứ tự viết trong tệp thay vì đồ thị phụ thuộc · không khai báo phụ thuộc ngầm.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/266-infrastructure-as-code-desired-state-and-the-dependency-graph.md`
- Nội dung học thuật: `note.md` cùng thư mục.
