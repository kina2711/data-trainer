# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 303: Catalog and discovery - search, relevance and the asset page

## Thực hành

**Nhiệm vụ.** Dựng trang tài sản đủ mười mục cho 20 tài sản. Cài xếp hạng có lọc theo quyền. Chạy phép thử khả năng tìm thấy với năm người, mỗi người một nhu cầu, tính giờ ba phút. Chạy phép thử phủ định với một tài khoản hạn chế và kiểm không kết quả nào lộ tài sản ngoài quyền. Tạo một tài sản phổ biến nhưng chưa chứng nhận và chứng minh giao diện không làm nó trông như đã chứng nhận.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đo bằng hành vi người dùng và bằng phép thử rò rỉ. Kiểm bằng phép thử với năm người cộng phép thử quyền; đạt khi tỉ lệ tìm thấy vượt ngưỡng và không kết quả nào lộ siêu dữ liệu ngoài quyền.

**Điều kiện đạt.** Tỉ lệ tìm thấy trong ba phút vượt ngưỡng, không kết quả nào lộ siêu dữ liệu ngoài quyền, và tài sản phổ biến chưa chứng nhận không bị hiển thị như đã chứng nhận.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Trả kết quả tìm kiếm trước khi lọc quyền · xếp hạng chỉ theo mức phổ biến · trang tài sản thiếu hạt và chủ sở hữu · đo danh mục bằng số tài sản đã đăng ký.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/191-catalog-and-discovery-search-relevance-and-the-asset-page.md`
- Nội dung học thuật: `note.md` cùng thư mục.
