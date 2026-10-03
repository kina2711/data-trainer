# Phase 5: Modeling, Semantics and Analytical Product
# Module 12: Semantic Layer and Metrics Engineering
# Lesson 171: Ambiguous Joins and the Chasm Trap

## Thực hành

**Nhiệm vụ.** Dựng hai bảng sự kiện cùng nối vào chiều khách hàng. Viết truy vấn kết cả ba và so tổng của từng bảng với tổng thật; định lượng mức thổi phồng. Sửa bằng cả ba cách và so ba kết quả. Tạo một cặp thực thể có hai đường kết và chứng minh hai đường cho hai con số.

Chỉ chạy join fixtures, MetricFlow validation/compile và execution plans trên dataset/môi trường thử nghiệm có version. Không chạy query tốn kém hoặc thay semantic configuration production. Redact credentials; lưu config/tool version, seed, commands, raw output và diff.

## Kiểm tra cuối bài

1. Phát biểu grains, identities và expected cardinalities.
2. Nêu phản ví dụ cho fanout, lost population hoặc ambiguous path.
3. Phân biệt parse, validate, compile và business reconciliation.
4. Đề xuất independent oracle cùng valid/invalid controls.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi im lặng rồi sửa bằng cơ chế đúng. Kiểm bằng đối chứng với tổng thật; đạt khi định lượng được mức thổi phồng và bản sửa khớp tổng thật.

**Điều kiện đạt.** Mức thổi phồng được định lượng, cả ba cách sửa đều cho tổng khớp tổng thật, và hai đường kết cho hai con số khác nhau được chỉ ra.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Kết hai bảng sự kiện qua một chiều chung · để công cụ tự chọn đường kết · phát hiện bằng cách nhìn số rồi thấy hợp lý · dùng phép chọn phân biệt để chữa nhân dòng.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/59-ambiguous-joins-chasm-trap.md`
- Nội dung học thuật: `note.md` cùng thư mục.
