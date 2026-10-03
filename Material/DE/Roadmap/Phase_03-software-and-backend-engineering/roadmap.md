# Giai đoạn 3: Kỹ nghệ phần mềm và backend

Giai đoạn này kết hợp M07–M08. Người học chuyển từ `Bằng chứng hoàn thành Giai đoạn 2` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L112.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Bằng chứng hoàn thành Giai đoạn 2 | Sản phẩm và kết quả đánh giá của giai đoạn trước | Hoàn thành lại tiêu chí chưa đạt trước khi vào bài kiểm tra tích hợp |

## Đầu ra giai đoạn

Nộp một dịch vụ giữ đúng bất biến dưới truy cập đồng thời và dưới sự cố, với bằng chứng từ phép kiểm chạy song song.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DE-M07](Module_07-software-design-and-delivery/roadmap.md) | Xây một kho mã đổi được mà không phá hợp đồng, có chiến lược kiểm thử theo tầng, và có đường phát hành cùng đường lùi đáng tin | M01 · M02, cộng M05 và M06 ở mức nền | Đồ thị phụ thuộc không có tầng nghiệp vụ phụ thuộc khung hay cơ sở dữ liệu; đổi một bộ chuyển đổi mà phép kiểm lõi không sửa một dòng |
| [DE-M08](Module_08-backend-and-api-engineering/roadmap.md) | Vận hành đúng một giao diện lập trình web có trạng thái dưới ràng buộc đồng thời, sự cố và bảo mật | M05 · M06 · M07 | Không sinh tác động kép khi máy khách thử lại trong hợp đồng đã định; bất biến giao dịch được kiểm bằng phép chạy song song; có mô hình mối đe doạ và sổ tay chẩn đoán |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P03["Giai đoạn 3<br/>Kỹ nghệ phần mềm và backend<br/>Roadmap hiện hành"]
  M07["M07 · Thiết kế và chuyển giao phần mềm<br/>Bài 89–100"]
  P03 --> M07
  M08["M08 · Kỹ nghệ backend và API<br/>Bài 101–112"]
  M07 --> M08
  G03["Bài kiểm tra cuối giai đoạn<br/>Bài 112"]
  M08 --> G03

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P03 phase;
  class M07,M08 module;
  class G03 gate;
```

## Lý do sắp xếp

- M07 đứng trước M08 vì điều kiện đầu vào của M08 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Buổi 155 phút: 110 phút làm bài độc lập, 45 phút chữa bài. Nhận một đặc tả dịch vụ nhỏ. Bài chấm sáu phần: A (15đ) đồ thị phụ thuộc không có cạnh sai chiều và phép kiểm lõi không cần cơ sở dữ liệu · B (25đ) không sinh tác động kép khi máy khách thử lại, chứng minh bằng ba thí nghiệm · C (20đ) bất biến giữ đúng dưới 50 luồng đồng thời, chứng minh bằng phép kiểm chạy song song · D (15đ) hạn chờ và giới hạn thử lại đặt đủ, không khuếch đại · E (15đ) chẩn đoán một sự cố tiêm sẵn bằng chỉ số và theo vết · F (10đ) phép thử phủ định cho mọi điểm vào đều từ chối đúng.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Nộp một dịch vụ giữ đúng bất biến dưới truy cập đồng thời và dưới sự cố, với bằng chứng từ phép kiểm chạy song song. | Buổi 155 phút: 110 phút làm bài độc lập, 45 phút chữa bài. Nhận một đặc tả dịch vụ nhỏ. Bài chấm sáu phần: A (15đ) đồ thị phụ thuộc không có cạnh sai chiều và phép kiểm lõi không cần cơ sở dữ liệu · B (25đ) không sinh tác động kép khi máy khách thử lại, chứng minh bằng ba thí nghiệm · C (20đ) bất biến giữ đúng dưới 50 luồng đồng thời, chứng minh bằng phép kiểm chạy song song · D (15đ) hạn chờ và giới hạn thử lại đặt đủ, không khuếch đại · E (15đ) chẩn đoán một sự cố tiêm sẵn bằng chỉ số và theo vết · F (10đ) phép thử phủ định cho mọi điểm vào đều từ chối đúng. | Đạt ≥ 70/100, phần B và C đều ≥ 60%. Bất biến nào chỉ được chứng minh bằng phép kiểm tuần tự thì không tính điểm ở phần C. | Chỉ kiểm tuần tự rồi kết luận đúng · bỏ phần chẩn đoán vì hết giờ · thử lại mà không có khoá bất biến · để lõi phụ thuộc cơ sở dữ liệu. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| M01 · M02, cộng M05 và M06 ở mức nền | M07 | Xây một kho mã đổi được mà không phá hợp đồng, có chiến lược kiểm thử theo tầng, và có đường phát hành cùng đường lùi đáng tin |
| M05 · M06 · M07 | M08 | Vận hành đúng một giao diện lập trình web có trạng thái dưới ràng buộc đồng thời, sự cố và bảo mật |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Chỉ kiểm tuần tự rồi kết luận đúng · bỏ phần chẩn đoán vì hết giờ · thử lại mà không có khoá bất biến · để lõi phụ thuộc cơ sở dữ liệu. | Bài làm, nhật ký và phản hồi theo tiêu chí L112 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Áp nguyên tắc thiết kế như luật tuyệt đối, chia lớp thật nhiều rồi mã khó đọc hơn; hoặc kiểm thử mô phỏng cả thành phần bên trong nên đổi cấu trúc là phép kiểm đỏ | Không đạt tiêu chí hoàn thành M07 | Khắc phục tại M07 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Xây giao diện chạy đúng khi gọi lần lượt rồi hỏng khi có hai máy khách gọi cùng lúc, vì ranh giới giao dịch và khoá bất biến chưa được thiết kế | Không đạt tiêu chí hoàn thành M08 | Khắc phục tại M08 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DE-M07 | Roadmap mô-đun | `Module_07-software-design-and-delivery/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M08 | Roadmap mô-đun | `Module_08-backend-and-api-engineering/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
