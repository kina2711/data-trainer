# Phase 2: Machine, Operating System and Network
# Module 6: Networking from Packet to API
# Lesson 78: DNS - resolution, caching and stale records

## Thực hành

**Nhiệm vụ.** Dựng một tên miền thử trỏ tới một máy, gọi thành công, rồi đổi sang máy khác. Quan sát thời gian bản ghi cũ còn hiệu lực ở từng tầng đệm. Tạo tình huống một số tiến trình gọi được và một số không, rồi chẩn đoán. So thời gian sống đặt trước và sau khi hạ xuống.

Chỉ dùng fixture, VM hoặc sandbox được phép. Viết prediction trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Tái hiện một failure hoặc changed-constraint case.
3. Đối soát bằng independent oracle.
4. Phân biệt protocol, observation và kết luận.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *phân tích*. Objective là nhận ra một loại sự cố có triệu chứng gây hiểu nhầm. Kiểm bằng hai tình huống trong đó một là bản ghi cũ; đạt khi phân biệt đúng và chỉ ra tầng đệm nào đang giữ bản ghi.

**Điều kiện đạt.** Phân biệt đúng hai tình huống, chỉ ra đúng tầng đệm giữ bản ghi cũ, và có số đo thời gian hiệu lực ở từng tầng.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Bỏ qua bước phân giải tên khi chẩn đoán · đổi bản ghi rồi mong có hiệu lực ngay · quên đệm trong tiến trình · kết luận lỗi mạng khi thực ra là bản ghi cũ.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/078-dns-resolution-caching-and-stale-records.md`
- Nội dung học thuật: `note.md` cùng thư mục.
