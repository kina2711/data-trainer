# Phase 7: Ingestion, Transformation, Quality and Governance
# Module 17: ELT, dbt and Workflow Orchestration
# Lesson 258: Jinja and Macros Where Abstraction Stops Paying

## Thực hành

**Nhiệm vụ.** Cho ba khuôn mẫu lặp trong một dự án. Tách hai cái thành macro có kiểm tham số, tài liệu và phép kiểm kết xuất. Với cái thứ ba, lập luận vì sao tách làm mã khó đọc hơn. Đo thời gian phân tích dự án trước và sau. Viết một macro gọi cơ sở dữ liệu lúc phân tích và đo mức chậm nó gây ra.

Chỉ dùng fixture/sandbox được phép. Lưu input snapshot hoặc data interval, versions, commands, compiled SQL, run artifacts, query IDs, state trước–sau, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant và input boundary.
2. Phân biệt parse, compile, execute và publish evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi phán đoán về mức trừu tượng chứ chỉ viết được macro. Kiểm bằng ba khuôn mẫu lặp; đạt khi tách đúng hai và giải thích được vì sao cái thứ ba không nên tách.

**Điều kiện đạt.** Hai macro có kiểm tham số và phép kiểm kết xuất, lý do không tách cái thứ ba được lập luận, và chi phí gọi cơ sở dữ liệu lúc phân tích được đo.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Tách macro cho mỗi đoạn lặp hai lần · gọi cơ sở dữ liệu trong ngữ cảnh phân tích · viết macro che giấu quy tắc nghiệp vụ · nâng cấp gói mà không rà soát thay đổi.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/146-jinja-macros-abstraction-boundary.md`
- Nội dung học thuật: `note.md` cùng thư mục.
