# Phase 2: Machine, Operating System and Network
# Module 4: Computer Architecture and the Performance Model
# Lesson 56: MIMD - shared memory, distributed memory and SPMD

## Thực hành

**Nhiệm vụ.** Chạy cùng khối lượng công việc với 1, 2, 4 và 8 đơn vị thực thi; tính tăng tốc và hiệu suất song song ở mỗi mức. Ước lượng phần tuần tự từ đường cong và đối chiếu với dự đoán của định luật tăng tốc. Tái hiện chia sẻ giả và đo chi phí của nó. Chạy một bản đặt bộ nhớ ở nút xa và đo chênh lệch. Với bản phân tán, đo thời gian truyền thông tách khỏi thời gian tính.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi giải thích vì sao đường tăng tốc bão hoà chứ chỉ vẽ nó. Kiểm bằng thí nghiệm thay đổi quy mô; đạt khi đường hiệu suất song song được vẽ tới ít nhất tám đơn vị và trần được quy về nguyên nhân bằng số đo.

**Điều kiện đạt.** Đường hiệu suất song song có số đo tới ≥ 8 đơn vị, phần tuần tự được ước lượng từ dữ liệu, và trần hiệu năng được quy về nguyên nhân cụ thể.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo cáo tăng tốc mà không báo hiệu suất song song · thêm đơn vị thực thi khi trần là băng thông bộ nhớ · bỏ qua chia sẻ giả vì không thấy tranh chấp trong mã · so bản phân tán mà không tách thời gian truyền thông.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/056-mimd-shared-memory-distributed-memory-and-spmd.md`
- Nội dung học thuật: `note.md` cùng thư mục.
