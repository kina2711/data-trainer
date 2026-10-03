# Phase 6: Analytical Storage and Query Engines
# Module 14: OLAP Internals and Analytical Engines
# Lesson 213: Shared Nothing and Separated Storage Compute

## Thực hành

**Nhiệm vụ.** Chạy cùng bộ truy vấn ở đệm lạnh và đệm nóng, đo chênh lệch. Thiết kế một quy trình đo công bằng nêu rõ trạng thái đệm được đặt thế nào trước mỗi lần chạy. Cho hai tình huống thay đổi quy mô và suy ra thao tác cần làm ở mỗi kiến trúc.

Chỉ dùng synthetic fixture, local/isolated engines và benchmark host được phép. Không chạy load trên hệ dùng chung, đổi compiler/system settings toàn máy hoặc dùng dữ liệu nhạy cảm. Lưu version, configuration, data hash, commands, raw counters, result oracle, repetitions và limitations.

## Kiểm tra cuối bài

1. Nêu mechanism và tầng thực thi trung tâm.
2. Đưa một counter trực tiếp và một proxy dễ gây hiểu sai.
3. Nêu counterexample làm optimization mất tác dụng.
4. Phân biệt expected result với evidence đã quan sát.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *hiểu*. Bài lý thuyết chuẩn bị cho phần chi phí và phần chọn engine. Kiểm bằng bài thiết kế phép đo; đạt khi phép đo kiểm soát được trạng thái đệm và chênh lệch nóng lạnh được định lượng.

**Điều kiện đạt.** Chênh lệch đệm nóng và đệm lạnh được định lượng, và quy trình đo nêu rõ cách đặt trạng thái đệm trước mỗi lần chạy.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút đọc nguồn tham chiếu và tự giải thích lại · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** So một lần chạy nóng với một lần chạy lạnh · quên rằng siêu dữ liệu là thành phần dùng chung có thể nghẽn · giả định tách lưu trữ và tính toán luôn rẻ hơn · thay đổi quy mô cụm không chia sẻ mà không tính thời gian phân bố lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/101-shared-nothing-separated-storage-compute.md`
- Nội dung học thuật: `note.md` cùng thư mục.
