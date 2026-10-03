# Phase 5: Modeling, Semantics and Analytical Product
# Module 11: Data Modeling - Operational, Analytical and Domain
# Lesson 155: Additivity - additive, semi-additive and non-additive measures

## Thực hành

**Nhiệm vụ.** Cho mười độ đo, phân vào ba nhóm. Với ba độ đo không cộng được hoặc cộng được một phần, tính theo cách sai và cách đúng rồi so số. Thiết kế lại cách lưu cho một tỉ lệ theo quy tắc tử số mẫu số riêng và chứng minh nó gộp đúng ở mọi mức.

Chỉ chạy profiling, merge/backfill hoặc schema experiments trên dataset thử nghiệm/versioned snapshot. Không sửa identity mapping, history, keys hoặc production mart để minh họa. Lưu input snapshot, SQL/notebook, assumptions, counts/control totals và diff trước–sau.

## Kiểm tra cuối bài

1. Phát biểu grain và invariant chính.
2. Nêu phản ví dụ làm thiết kế sai cho kết quả hợp lệ cú pháp.
3. Chỉ ra phần nào là source fact và phần nào là curriculum synthesis.
4. Đề xuất phép kiểm dữ liệu tái chạy được.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective đòi nhận ra một lỗi không báo lỗi, nên phải chứng minh bằng đối chứng số. Kiểm bằng ba phép cộng sai; đạt khi định lượng được mức sai ở cả ba và đề xuất cách lưu đúng.

**Điều kiện đạt.** Mười độ đo phân đúng nhóm, ba phép cộng sai được định lượng mức sai, và bản lưu tử số mẫu số gộp đúng ở mọi mức.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Cộng số dư theo thời gian · lưu sẵn tỉ lệ trong bảng sự kiện · trung bình các tỉ lệ · giả định đếm giá trị phân biệt cộng được.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/43-additivity-additive-semi-additive-non-additive.md`
- Nội dung học thuật: `note.md` cùng thư mục.
