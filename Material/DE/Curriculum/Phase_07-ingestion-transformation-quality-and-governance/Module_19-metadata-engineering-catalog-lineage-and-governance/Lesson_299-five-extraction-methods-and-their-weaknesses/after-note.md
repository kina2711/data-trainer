# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 19: Metadata Engineering, Catalog, Lineage and Governance
# Lesson 299: Five extraction methods and their weaknesses

## Thực hành

**Nhiệm vụ.** Trên cùng một nền tảng, lấy dòng dõi bằng khai báo tường minh, phân tích câu lệnh, và sự kiện thời gian chạy. Hợp nhất ba đồ thị. Với mỗi cách, tính tỉ lệ tài sản được phủ và liệt kê loại tài sản nó không thấy. Chỉ ra phần không cách nào phủ và đánh dấu trạng thái không rõ thay vì bỏ trống.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi đo độ phủ chứ chỉ dựng được đồ thị. Kiểm bằng bảng độ phủ ba cách; đạt khi mỗi cách có tỉ lệ phủ đo được trên cùng tập tài sản và phần không cách nào phủ được đánh dấu rõ.

**Điều kiện đạt.** Ba cách đều có tỉ lệ phủ đo được trên cùng tập tài sản, và phần không cách nào phủ được đánh dấu trạng thái không rõ.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Dùng một cách rồi coi đồ thị là đầy đủ · lấp khoảng trống bằng suy đoán · bỏ lịch sử truy vấn nên không biết ai đang tiêu thụ · không đo độ phủ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/187-five-extraction-methods-and-their-weaknesses.md`
- Nội dung học thuật: `note.md` cùng thư mục.
