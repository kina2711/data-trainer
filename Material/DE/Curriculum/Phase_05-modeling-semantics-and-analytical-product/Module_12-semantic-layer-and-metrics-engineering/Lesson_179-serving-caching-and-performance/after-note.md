# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 179: Serving, Caching and Performance

## Thực hành

**Nhiệm vụ.** Chạy bộ 20 truy vấn chuẩn và đo bốn chỉ số ở trạng thái chưa tối ưu. Dựng bảng tổng hợp tính sẵn cho các chỉ số cộng được. Bật đệm với chiến lược làm mới phù hợp. Đo lại. Phục vụ cùng bộ chỉ số cho hai bên tiêu thụ khác loại, ví dụ một công cụ báo cáo và một ứng dụng gọi qua giao diện lập trình, rồi đối soát hai bên cho cùng con số. Chạy phép thử cách ly đệm: hai người dùng khác quyền hỏi cùng câu, chứng minh không ai nhận mục đệm của người kia. Đổi một định nghĩa và chứng minh đệm cũ bị vô hiệu nhờ phiên bản ngữ nghĩa trong khoá.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi tối ưu dưới hai ràng buộc đối nghịch là tốc độ và độ tươi. Kiểm bằng cặp số đo cộng phép thử cách ly đệm; đạt khi thời gian phân vị 95 dưới ngưỡng, độ tươi trong cam kết, và hai người dùng khác quyền không bao giờ nhận cùng một mục đệm.

**Điều kiện đạt.** Thời gian phân vị 95 dưới ngưỡng, độ tươi trong cam kết, hai bên tiêu thụ cho cùng con số, và phép thử cách ly đệm không có lần nào hai người khác quyền dùng chung một mục.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dựng bảng tổng hợp cho chỉ số không cộng được · đặt thời gian sống của đệm dài hơn cam kết độ tươi · tối ưu mà đổi kết quả · **đặt khoá đệm bỏ ngữ cảnh bảo mật hoặc bỏ phiên bản ngữ nghĩa** · chỉ phục vụ một bên tiêu thụ rồi coi là đã kiểm · không đo chi phí trên mỗi truy vấn.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/67-serving-caching-performance.md`
- Nội dung học thuật: `note.md` cùng thư mục.
