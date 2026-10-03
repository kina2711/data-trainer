# Phase 9: Cloud Platform and Production Operations
# Module 25: Containers, Infrastructure as Code and Kubernetes
# Lesson 374: Images, layers, digests and the multi-stage build

## Thực hành

**Nhiệm vụ.** Dựng một ảnh theo cách thông thường rồi dựng lại theo nhiều giai đoạn; so kích thước và số lớp. Đảo thứ tự bước cài phụ thuộc và bước sao chép mã, đo thời gian dựng lại sau khi sửa một dòng mã ở cả hai cách. Ghim ảnh nền theo mã băm. Cố ý đưa một bí mật vào một lớp rồi xoá ở lớp sau; dùng công cụ tìm lại nó trong lịch sử lớp.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có ba tiêu chí nghiệm thu đo được. Kiểm bằng cặp số đo cộng bộ quét; đạt khi kích thước giảm có số đo, thời gian dựng lại giảm nhờ bộ đệm, và bộ quét lớp không tìm thấy bí mật.

**Điều kiện đạt.** Kích thước ảnh giảm có số đo, thời gian dựng lại giảm nhờ thứ tự lớp, và bí mật đã xoá vẫn tìm lại được ở bản sai rồi được loại bỏ hẳn ở bản đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Sao chép mã nguồn trước khi cài phụ thuộc · ghim ảnh nền theo thẻ · đưa bí mật vào thời điểm dựng · chạy bằng người dùng cao nhất trong vùng chứa.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/262-images-layers-digests-and-the-multi-stage-build.md`
- Nội dung học thuật: `note.md` cùng thư mục.
