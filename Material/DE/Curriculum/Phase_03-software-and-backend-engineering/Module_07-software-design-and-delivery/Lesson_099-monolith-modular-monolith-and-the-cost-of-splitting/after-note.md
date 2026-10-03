# Phase 3: Software and Backend Engineering
# Module 7: Software Design and Delivery
# Lesson 99: Monolith, modular monolith and the cost of splitting

## Thực hành

**Nhiệm vụ.** Cho ba tình huống khác nhau về quy mô đội, tải và ranh giới nghiệp vụ. Quyết định dạng kiến trúc cho từng cái. Viết một tài liệu quyết định theo lesson 3 chọn khối đơn có mô đun cho một trong ba, nêu rõ ba điều kiện kích hoạt việc tách về sau.

#### Bằng chứng cho DE-L099

- quyết định cho ba tình huống, trong đó ít nhất hai tình huống không tách ngay;
- một ADR chọn modular monolith;
- ba trigger có metric, ngưỡng/cửa sổ và owner;
- dependency/data ownership diagram;
- danh sách operational tax áp dụng cho hệ cụ thể;
- lý do loại hai phương án còn lại.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Modular monolith khác monolith rối ở invariant nào, ngoài cấu trúc thư mục?
2. Hai service cùng ghi một bảng mất quyền tự chủ ở đâu?
3. Khi nào scaling là lý do thật để tách?
4. Một trigger “khi traffic tăng” thiếu trường gì để kiểm được?
5. Distributed monolith giữ lại hai nhóm chi phí nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *đánh giá*. Objective đòi cân chi phí vận hành với lợi ích tổ chức, chứ theo xu hướng. Kiểm bằng ba tình huống trong đó ít nhất hai không nên tách; đạt khi quyết định đúng cả ba và nêu điều kiện kích hoạt kiểm được.

**Điều kiện đạt.** Quyết định đúng cả ba tình huống, và tài liệu quyết định nêu được ba điều kiện kích hoạt kiểm được.


## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Đọc nguồn tham chiếu và tự giải thích lại; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Tách dịch vụ vì nghe hiện đại · để hai dịch vụ cùng ghi một bảng rồi gọi là đã tách · bỏ qua thuế vận hành khi so · viết điều kiện kích hoạt chung chung.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/11-monolith-modular-monolith-and-cost-of-splitting.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
