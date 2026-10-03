# Phase 8: Distributed Systems, Streaming and Compute
# Module 23: Spark, Flink and Distributed Compute Engines
# Lesson 355: Tuning project - the decision tree on three unknown jobs

## Thực hành

**Nhiệm vụ.** Nhận ba công việc chậm với ba nguyên nhân khác nhau. Với mỗi cái, chạy đủ cây quyết định và ghi số đo ở từng bước. Nêu giả thuyết trước khi sửa. Áp đúng một thay đổi, đo lại và đối soát kết quả. Nộp báo cáo hiệu năng theo chuẩn ở lesson 59, bắt đầu từ số đo chứ từ cấu hình.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *sáng tạo*. Bài tổng hợp phần hiệu năng thành một quy trình chẩn đoán có kỷ luật. Kiểm bằng ba công việc; đạt khi chẩn đoán đúng nguyên nhân ở ít nhất hai, mỗi cải thiện chỉ dùng một thay đổi, và kết quả đối soát không đổi.

**Điều kiện đạt.** Chẩn đoán đúng nguyên nhân ở ≥ 2/3 công việc, mỗi cải thiện dùng đúng một thay đổi có số đo trước sau, và kết quả đối soát không đổi.

## Bài làm sau buổi học

**Nhiệm vụ.** 144 phút hoàn thiện dự án ngoài lớp; nộp trước buổi kế tiếp

**Lỗi cần chủ động loại trừ.** Đổi nhiều cấu hình cùng lúc · tăng bộ nhớ tiến trình thực thi trước khi đọc kế hoạch · sửa mà không đối soát kết quả · viết báo cáo bắt đầu bằng việc đã đổi gì thay vì đã đo gì.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/243-tuning-project-the-decision-tree-on-three-unknown-jobs.md`
- Nội dung học thuật: `note.md` cùng thư mục.
