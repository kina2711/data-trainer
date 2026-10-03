# Phase 5: Modeling, Semantics and Analytical Product
# Module 13: Analytical Data Product and Self-service
# Lesson 196: Serving, Access and Security for Consumers

## Thực hành

**Nhiệm vụ.** Mở ba đường phục vụ. Chạy cùng bộ phép thử phủ định ở cả ba và chứng minh kết quả giống nhau. Chạy tải tới ngưỡng người dùng đồng thời mục tiêu và đo ba yêu cầu phi chức năng. Dựng quy trình che dữ liệu cho môi trường thử và kiểm không còn trường định danh.

Chỉ dùng fixture, synthetic principals, isolated load environment và cost/event extracts đã loại dữ liệu nhạy cảm. Không mở quyền production, load-test hệ dùng chung, gửi reverse-ETL action thật, xóa product hoặc thu personal data. Lưu versions, commands, raw outputs, unknown sets, approvals mô phỏng và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, product scope và owner trung tâm.
2. Đưa một failure vẫn có thể tạo tín hiệu xanh hoặc completed.
3. Nêu denominator, identity hoặc allocation rule cần khóa trước khi đo.
4. Phân biệt protocol đã viết với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu gồm cả bảo mật lẫn hiệu năng. Kiểm bằng phép thử phủ định ở cả ba đường cộng phép thử tải; đạt khi chính sách nhất quán ở ba đường và ba yêu cầu phi chức năng đạt.

**Điều kiện đạt.** Phép thử phủ định cho kết quả giống nhau ở cả ba đường, ba yêu cầu phi chức năng đạt, và dữ liệu môi trường thử đã che.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cấu hình quyền khác nhau ở ba đường · cấp quyền theo cá nhân · chép dữ liệu sản xuất sang môi trường thử chưa che · không đo hành vi khi quá tải.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/84-serving-access-security-consumers.md`
- Nội dung học thuật: `note.md` cùng thư mục.
