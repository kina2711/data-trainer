# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 110: Load testing and capacity notes

## Thực hành

**Nhiệm vụ.** Chạy tải tăng theo sáu bậc trên giao diện. Ở mỗi bậc đo cả bốn đại lượng. Vẽ đường cong và xác định điểm công suất. Chỉ ra tài nguyên nút thắt bằng số đo. Chạy tải kéo dài 30 phút và kiểm bộ nhớ cùng số kết nối có tăng đơn điệu không. Viết ghi chú công suất một trang.

Bài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Vì sao throughput đơn lẻ không phải capacity?
2. Phân biệt offered load, throughput và goodput.
3. Làm sao chứng minh bottleneck thay vì chỉ nêu correlation?
4. Kết luận tối đa nào hợp lệ từ soak test 30 phút?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi đọc đường cong và định vị nút thắt chứ chỉ chạy công cụ tải. Kiểm bằng đường cong bốn đại lượng; đạt khi xác định đúng điểm công suất và chỉ đúng tài nguyên nút thắt.

**Điều kiện đạt.** Đường cong bốn đại lượng đủ sáu bậc, xác định đúng điểm công suất và tài nguyên nút thắt, và phép thử kéo dài không cho thấy rò rỉ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Báo thông lượng đỉnh mà không báo tỉ lệ lỗi · đo ngay khi vừa tăng tải · không đo mức bão hoà hồ kết nối · bỏ phép thử kéo dài nên không phát hiện rò rỉ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/22-load-testing-and-capacity-notes.md`
- Nội dung học thuật: `note.md` cùng thư mục.
