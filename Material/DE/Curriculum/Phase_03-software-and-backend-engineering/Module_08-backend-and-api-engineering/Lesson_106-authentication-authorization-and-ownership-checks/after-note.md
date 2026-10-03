# Phase 3: Software and Backend Engineering
# Module 8: Backend and API Engineering
# Lesson 106: Authentication, authorization and ownership checks

## Thực hành

**Nhiệm vụ.** Cài xác thực bằng thẻ có thời hạn ngắn và cơ chế làm mới. Cài kiểm vai và kiểm quyền sở hữu. Với mỗi điểm vào, viết phép thử phủ định. Thử truy cập tài nguyên của người khác bằng thẻ hợp lệ và chứng minh bị từ chối. Thu hồi quyền một người dùng và đo bao lâu thẻ cũ còn dùng được.

#### Negative test là bằng chứng chính

Positive test chỉ chứng minh happy path. Ma trận tối thiểu cho mỗi entry point:

| Principal | Token | Role/scope | Object relation | Kỳ vọng |
|---|---|---|---|---|
| hợp lệ | hợp lệ | đủ | own/same tenant | allow |
| hợp lệ | hợp lệ | thiếu action | own | deny |
| hợp lệ | hợp lệ | đủ | other user | deny |
| hợp lệ | hợp lệ | đủ | other tenant | deny |
| đã revoke | token cũ | claim cũ còn role | own | deny trong window cam kết |
| anonymous | không token | none | ID biết trước | deny |
| service A | token audience A | đủ role giả định | object B | deny |

Thêm test alternate paths: list/filter, export, bulk, nested route, background job, GraphQL node, file download URL và admin endpoint. Nhiều BOLA xuất hiện vì một path có check còn path khác không.

#### Đo revocation latency

Thí nghiệm:

1. cấp access token và refresh token;
2. xác nhận request hợp lệ;
3. thu hồi membership/session tại thời điểm `t0`;
4. gửi request bằng access token cũ theo chu kỳ;
5. thử refresh token cũ và rotated token;
6. ghi thời điểm request đầu tiên bị từ chối `t1`;
7. báo `t1 - t0`, cache path, clock source và policy target.

Nếu mục tiêu “dưới 60 giây”, test phải kiểm cả p95/p99 qua nhiều replica và tình huống cache/identity provider gián đoạn. Một lần chạy local không chứng minh SLO.

## Kiểm tra cuối bài

#### Câu hỏi tự kiểm tra

1. Token hợp lệ chứng minh và không chứng minh điều gì?
2. Vì sao role check không thay object-level check?
3. UUID có ngăn BOLA không?
4. Nested route cần kiểm những quan hệ nào?
5. Vì sao authorization phải chạy trên mọi request?
6. Self-contained token có những chiến lược thu hồi nào?
7. Refresh-token rotation phát hiện replay ra sao?
8. TOCTOU xuất hiện ở đâu giữa check và mutation?
9. Negative test nào bắt tenant escape?
10. Revocation latency phải được đo thế nào?

## Tiêu chí hoàn thành

**Cách đánh giá.** Tầng *áp dụng*. Objective là một cơ chế bảo mật kiểm được bằng phép thử phủ định, chứ bằng việc đường đi thuận chạy được. Kiểm bằng phép thử phủ định cho mọi điểm vào; đạt khi mọi truy cập trái phép bị từ chối và có ghi nhật ký.

**Điều kiện đạt.** Mọi điểm vào có phép thử phủ định và đều từ chối đúng, và đo được khoảng thời gian thẻ cũ còn hiệu lực sau khi thu hồi.

#### Bằng chứng cho DE-L106

Evidence pack gồm:

1. principal schema và trust boundary;
2. authorization matrix action × role/scope × relationship;
3. danh mục mọi entry point và policy tương ứng;
4. negative tests cho own/other-user/other-tenant/missing-scope/revoked;
5. short-lived access token và refresh flow có replay test;
6. đo revocation latency bằng clock và nhiều replica;
7. audit sample đã redaction;
8. threat note giải thích deny-default và failure behavior.

## Bài làm sau buổi học

**Nhiệm vụ.** Viết ghi chú chín phần; Làm lại lab từ đầu, không nhìn hướng dẫn, rồi làm phần mở rộng; Trả lời bốn câu kiểm tra; Nhật ký lỗi.

**Lỗi cần chủ động loại trừ.** Chỉ kiểm vai mà quên kiểm quyền sở hữu · đặt thời hạn thẻ rất dài cho tiện · kiểm quyền trong từng hàm xử lý nên sót đường vào · không viết phép thử phủ định.

Bài làm phải kèm lệnh tái hiện, đầu ra kiểm chứng và giải thích cho từng quyết định kỹ thuật. Không dùng ảnh chụp màn hình thay cho artifact có thể chạy lại.

## Reference

- Knowledge note: `Material/DE/Reference/Library/Knowledge-Notes/PACK-SOFTWARE-DESIGN-BOOK-01/18-authentication-authorization-and-ownership-checks.md`
- Nội dung lý thuyết của bài: `note.md` cùng thư mục.
