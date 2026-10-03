# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 162: Late Arriving Data, Early Arriving Facts and the Unknown Member

## Thực hành

**Nhiệm vụ.** Tạo dữ liệu có cả ba ca biên. Xử lý từng ca. Đối soát tổng số dòng và tổng tiền với nguồn để chứng minh không mất dòng. Truy vấn phân biệt được ba nghĩa của thành viên chưa biết. Với ca chiều tới muộn, sửa lại liên kết lịch sử và đối soát báo cáo trước sau.

Chỉ chạy fixture, profiling, reconciliation, semantic diff hoặc benchmark trên dataset thử nghiệm/versioned snapshot. Không sửa production model, metric, identity mapping hay history để minh họa. Lưu input, assumptions, query/test, raw output và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu context/grain và invariant chính.
2. Nêu phản ví dụ cho kết quả hợp lệ cú pháp nhưng sai nghĩa.
3. Chỉ ra source fact, quyết định thiết kế và curriculum synthesis.
4. Đề xuất phép kiểm tái chạy được cùng bằng chứng cần lưu.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là ba ca biên có tiêu chí nghiệm thu bằng đối soát. Kiểm bằng đối soát tổng; đạt khi không dòng nào bị bỏ và ba nghĩa của thành viên chưa biết phân biệt được.

**Điều kiện đạt.** Đối soát tổng khớp tuyệt đối với nguồn, ba nghĩa phân biệt được bằng truy vấn, và liên kết lịch sử sau khi sửa cho báo cáo đúng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ dòng sự kiện không kết được · dùng một thành viên chưa biết cho cả ba nghĩa · để sự kiện tham chiếu khoá không tồn tại · sửa chiều tới muộn mà không sửa liên kết lịch sử.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/50-late-arriving-data-early-facts-unknown-member.md`
- Nội dung học thuật: `note.md` cùng thư mục.
