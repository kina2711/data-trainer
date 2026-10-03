# Phase 9: Cloud Platform and Production Operations
# Module 24: Cloud Abstractions before Service Names
# Lesson 363: Network - CIDR, route, trust boundary, egress and DNS

## Thực hành

**Nhiệm vụ.** Dựng mạng có dải công khai và dải riêng, cổng dịch địa chỉ và ít nhất một điểm cuối riêng. Từ một máy ở dải riêng, thử ra internet trực tiếp và xác nhận bị chặn; thử gọi dịch vụ nhà cung cấp qua điểm cuối riêng và xác nhận thành công. Truy vết đường đi và vẽ sơ đồ. So chi phí ước tính giữa đi qua cổng dịch địa chỉ và đi qua điểm cuối riêng cho một khối lượng cho trước.

Chỉ dùng fixture hoặc sandbox được phép. Lưu input snapshot, versions, commands, resolved rules, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, grain và population.
2. Phân biệt declared, executed và published evidence.
3. Tái hiện một failure hoặc changed-assumption case.
4. Đối soát bằng independent oracle và công bố coverage.

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective có tiêu chí nghiệm thu là đường đi thật quan sát được. Kiểm bằng phép thử kết nối; đạt khi tài nguyên ở dải riêng không ra được internet trực tiếp, vẫn gọi được dịch vụ qua điểm cuối riêng, và sơ đồ khớp kết quả truy vết thật.

**Điều kiện đạt.** Tài nguyên ở dải riêng bị chặn ra internet nhưng gọi được dịch vụ qua điểm cuối riêng, và sơ đồ khớp kết quả truy vết thật.

## Bài làm sau buổi học

**Nhiệm vụ.** 20 phút viết ghi chú chín phần · 70 phút **làm lại lab từ đầu, không nhìn hướng dẫn**, rồi làm phần mở rộng · 30 phút trả lời bốn câu kiểm tra · 24 phút nhật ký lỗi

**Lỗi cần chủ động loại trừ.** Mở quy tắc cho toàn bộ internet để gỡ lỗi nhanh · đặt mọi thứ ở dải công khai · bỏ qua chi phí lưu lượng qua cổng dịch địa chỉ · vẽ sơ đồ hộp thay vì sơ đồ đường đi gói tin.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-DATABASE-MODELING-BOOK-01/251-network-cidr-route-trust-boundary-egress-and-dns.md`
- Nội dung học thuật: `note.md` cùng thư mục.
