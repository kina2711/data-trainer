# Phase 10: System Design, AI Boundary and Trajectory
# Module 28: Modern AI Engineering, Bounded
# Lesson 429: Serving - latency, cost, fallback and version lineage

## Thực hành

**Nhiệm vụ.** Chạy tải và đo độ trễ phân vị cùng chi phí trên mỗi truy vấn. Giới hạn độ dài đầu ra và đo lại. Bật hai mức đệm và chạy phép thử phủ định: hai người dùng có quyền khác nhau hỏi cùng câu và kiểm không ai thấy tài liệu ngoài quyền. Cài ghi nguồn gốc bốn thứ. Tiêm lỗi nhà cung cấp và kiểm đường dự phòng.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có ba tiêu chí nghiệm thu gồm một ca bảo mật. Kiểm bằng phép thử tải cộng phép thử đệm; đạt khi độ trễ phân vị 95 và chi phí trên mỗi truy vấn dưới ngưỡng, đệm không rò dữ liệu giữa người dùng, và mọi câu trả lời truy được bốn thứ.

**Điều kiện đạt.** Độ trễ phân vị 95 và chi phí trên mỗi truy vấn dưới ngưỡng, đệm không rò dữ liệu giữa người dùng, và mọi câu trả lời truy được đủ bốn thứ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đệm theo câu hỏi mà bỏ qua quyền người dùng · tối ưu độ trễ bằng cách bỏ bước truy hồi · không ghi phiên bản chỉ mục nên không điều tra được câu trả lời cũ · không có đường dự phòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/317-serving-latency-cost-fallback-and-version-lineage.md`
- Nội dung học thuật: `note.md` cùng thư mục.
