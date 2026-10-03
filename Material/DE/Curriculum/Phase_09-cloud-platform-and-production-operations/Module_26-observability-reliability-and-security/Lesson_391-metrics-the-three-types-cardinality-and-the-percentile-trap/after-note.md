# Phase 9: Cloud Platform and Production Operations
# Module 26: Observability, Reliability and Security
# Lesson 391: Metrics - the three types, cardinality and the percentile trap

## Thực hành

**Nhiệm vụ.** Thêm một nhãn có miền giá trị lớn và đo số chuỗi cùng mức dùng bộ nhớ của hệ thu thập; gỡ nhãn và đo lại. Tính phân vị 95 của một dịch vụ theo hai cách: lấy trung bình phân vị của từng bản sao, và gộp từ biểu đồ phân bố; so hai con số với giá trị đúng tính từ dữ liệu thô. Dựng bộ chỉ số theo yêu cầu cho một dịch vụ và theo tài nguyên cho một hàng đợi.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi chứng minh hai lỗi thường gặp bằng dữ liệu. Kiểm bằng hai thí nghiệm; đạt khi số chuỗi nhãn được đo trước sau và chênh lệch giữa phân vị gộp đúng với phân vị lấy trung bình được định lượng.

**Điều kiện đạt.** Số chuỗi nhãn đo được trước sau, và chênh lệch giữa phân vị gộp đúng với phân vị lấy trung bình được định lượng so với giá trị đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Đặt định danh người dùng làm nhãn · lấy trung bình của các phân vị · theo dõi bằng giá trị trung bình · dùng đồng hồ đo cho thứ cần tính tốc độ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/279-metrics-the-three-types-cardinality-and-the-percentile-trap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
