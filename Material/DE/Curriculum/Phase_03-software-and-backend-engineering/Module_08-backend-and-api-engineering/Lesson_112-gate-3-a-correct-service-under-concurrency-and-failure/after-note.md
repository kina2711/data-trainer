# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 112: Gate 3 - a correct service under concurrency and failure

## Thực hành

**Nhiệm vụ.** Buổi 155 phút: 110 phút làm bài độc lập, 45 phút chữa bài. Nhận một đặc tả dịch vụ nhỏ. Bài chấm sáu phần: A (15đ) đồ thị phụ thuộc không có cạnh sai chiều và phép kiểm lõi không cần cơ sở dữ liệu · B (25đ) không sinh tác động kép khi máy khách thử lại, chứng minh bằng ba thí nghiệm · C (20đ) bất biến giữ đúng dưới 50 luồng đồng thời, chứng minh bằng phép kiểm chạy song song · D (15đ) hạn chờ và giới hạn thử lại đặt đủ, không khuếch đại · E (15đ) chẩn đoán một sự cố tiêm sẵn bằng chỉ số và theo vết · F (10đ) phép thử phủ định cho mọi điểm vào đều từ chối đúng.

Bài làm phải lưu lệnh tái hiện, dữ liệu đầu vào, đầu ra thô và assertion của invariant. Mọi kết luận phải chỉ được evidence ID tương ứng; ảnh chụp không thay artifact chạy lại được.

## Kiểm tra cuối bài

1. Vì sao phần B và C là hard gate?
2. Một concurrency test hợp lệ cần barrier và invariant nào?
3. Telemetry evidence nào đủ để chẩn đoán injected failure?
4. Negative authorization test phải phủ những actor nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Cổng đo năng lực xây hệ đúng dưới điều kiện thật, nên hình thức là bài làm có tiêm lỗi và có chất vấn.

**Điều kiện đạt.** Đạt ≥ 70/100, phần B và C đều ≥ 60%. Bất biến nào chỉ được chứng minh bằng phép kiểm tuần tự thì không tính điểm ở phần C.

## Bài làm sau buổi học

**Nhiệm vụ.** Không có bài tự học. Nếu không đạt, theo phụ lục khắc phục khi không đạt cổng

**Lỗi cần chủ động loại trừ.** Chỉ kiểm tuần tự rồi kết luận đúng · bỏ phần chẩn đoán vì hết giờ · thử lại mà không có khoá bất biến · để lõi phụ thuộc cơ sở dữ liệu.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/24-gate-3-correct-service-assessment.md`
- Nội dung học thuật: `note.md` cùng thư mục.
