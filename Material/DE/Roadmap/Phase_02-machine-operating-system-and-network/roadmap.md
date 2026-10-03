# Giai đoạn 2: Máy tính, hệ điều hành và mạng

Giai đoạn này kết hợp M04–M06. Người học chuyển từ `Bằng chứng hoàn thành Giai đoạn 1` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L088.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Bằng chứng hoàn thành Giai đoạn 1 | Sản phẩm và kết quả đánh giá của giai đoạn trước | Hoàn thành lại tiêu chí chưa đạt trước khi vào bài kiểm tra tích hợp |

## Đầu ra giai đoạn

Chẩn đoán đúng ba sự cố thuộc ba tầng khác nhau, mỗi kết luận dẫn được về số đo hoặc gói tin làm bằng chứng.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DE-M04](Module_04-computer-architecture-and-the-performance-model/roadmap.md) | Dự đoán rồi đo được chi phí từ tầng lệnh, bộ nhớ đệm, RAM và thiết bị lưu trữ, và dùng mô hình đó giải thích hành vi của cơ sở dữ liệu, engine phân tán và dịch vụ | M03 | Vẽ được đường đi của một phép đọc và một phép ghi từ ứng dụng tới CPU, bộ nhớ đệm, RAM, bộ đệm trang và thiết bị; phân loại đúng SISD, SIMD và MIMD và giải thích SPMD chạy trên nền MIMD; dùng số đo tìm trần tính toán, bộ nhớ đệm, băng thông, đồng bộ hay mạng trước khi thêm làn, lõi hoặc nút |
| [DE-M05](Module_05-operating-systems-concurrency-and-linux/roadmap.md) | Dùng bằng chứng từ Linux để chẩn đoán tiến trình, bộ nhớ, hệ tệp, socket và tranh chấp, thay vì đoán từ triệu chứng | M02 · M04 | Chẩn đoán đúng bốn tình huống tải khác nhau chỉ bằng số đo hệ thống, sửa được một rò rỉ mô tả tệp cùng một khoá chết, và truy được đường từ hiệp trình tới tác vụ tới vòng lặp sự kiện tới bộ theo dõi tới mô tả tệp không chặn |
| [DE-M06](Module_06-networking-from-packet-to-api/roadmap.md) | Theo được một yêu cầu qua phân giải tên, bắt tay, mã hoá, giao thức ứng dụng, proxy và cân bằng tải, rồi chẩn đoán độ trễ cùng hết giờ bằng gói tin và nhật ký | M05 | Vẽ được trình tự từ phân giải tên tới phản hồi và chỉ ra trạng thái cùng hạn chờ ở từng bước; từ một bản bắt gói phân biệt được truyền lại, đặt lại kết nối và lỗi ứng dụng |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P02["Giai đoạn 2<br/>Máy tính, hệ điều hành và mạng<br/>Roadmap hiện hành"]
  M04["M04 · Kiến trúc máy tính và mô hình hiệu năng<br/>Bài 45–60"]
  P02 --> M04
  M05["M05 · Hệ điều hành, đồng thời và Linux<br/>Bài 61–76"]
  M04 --> M05
  M06["M06 · Mạng từ gói tin đến API<br/>Bài 77–88"]
  M05 --> M06
  G02["Bài kiểm tra cuối giai đoạn<br/>Bài 88"]
  M06 --> G02

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P02 phase;
  class M04,M05,M06 module;
  class G02 gate;
```

## Lý do sắp xếp

- M04 đứng trước M05 vì điều kiện đầu vào của M05 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.
- M05 đứng trước M06 vì điều kiện đầu vào của M06 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Làm trên một hệ có ba sự cố cài sẵn ở ba tầng. Bài chấm sáu phần: A (20đ) phân loại đúng loại tải bằng chỉ số hệ thống · B (20đ) chẩn đoán sự cố mạng bằng bản bắt gói, chỉ đúng gói làm bằng chứng · C (20đ) giải thích một hiện tượng hiệu năng bằng mô hình chi phí, dẫn số đo của chính mình · D (15đ) sửa cả ba và xác nhận đã hồi phục · E (15đ) dòng thời gian chẩn đoán có ghi nhánh sai đã thử · F (10đ) báo cáo hiệu năng sáu phần cho một phép đo trong buổi.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Chẩn đoán đúng ba sự cố thuộc ba tầng khác nhau, mỗi kết luận dẫn được về số đo hoặc gói tin làm bằng chứng. | Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Làm trên một hệ có ba sự cố cài sẵn ở ba tầng. Bài chấm sáu phần: A (20đ) phân loại đúng loại tải bằng chỉ số hệ thống · B (20đ) chẩn đoán sự cố mạng bằng bản bắt gói, chỉ đúng gói làm bằng chứng · C (20đ) giải thích một hiện tượng hiệu năng bằng mô hình chi phí, dẫn số đo của chính mình · D (15đ) sửa cả ba và xác nhận đã hồi phục · E (15đ) dòng thời gian chẩn đoán có ghi nhánh sai đã thử · F (10đ) báo cáo hiệu năng sáu phần cho một phép đo trong buổi. | Đạt ≥ 70/100, phần A và B đều ≥ 60%. Kết luận nào không dẫn được về số đo hoặc gói tin thì phần đó bằng không. | Khởi động lại hệ rồi mất bằng chứng · kết luận từ một chỉ số · đoán trúng mà không có bằng chứng · bỏ phần dòng thời gian vì hết giờ. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| M03 | M04 | Dự đoán rồi đo được chi phí từ tầng lệnh, bộ nhớ đệm, RAM và thiết bị lưu trữ, và dùng mô hình đó giải thích hành vi của cơ sở dữ liệu, engine phân tán và dịch vụ |
| M02 · M04 | M05 | Dùng bằng chứng từ Linux để chẩn đoán tiến trình, bộ nhớ, hệ tệp, socket và tranh chấp, thay vì đoán từ triệu chứng |
| M05 | M06 | Theo được một yêu cầu qua phân giải tên, bắt tay, mã hoá, giao thức ứng dụng, proxy và cân bằng tải, rồi chẩn đoán độ trễ cùng hết giờ bằng gói tin và nhật ký |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Khởi động lại hệ rồi mất bằng chứng · kết luận từ một chỉ số · đoán trúng mà không có bằng chứng · bỏ phần dòng thời gian vì hết giờ. | Bài làm, nhật ký và phản hồi theo tiêu chí L088 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Học thông số phần cứng như kiến thức rời, rồi không nối được với việc vì sao một truy vấn chậm hay vì sao thêm luồng không tăng thông lượng | Không đạt tiêu chí hoàn thành M04 | Khắc phục tại M04 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Học thuộc danh sách lệnh mà không biết mỗi lệnh đo cái gì, nên khi hệ chậm thì chạy lần lượt mọi lệnh và vẫn không kết luận được | Không đạt tiêu chí hoàn thành M05 | Khắc phục tại M05 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Gọi giao diện lập trình web mà không đặt hạn chờ và không giới hạn thử lại, rồi một nguồn chậm kéo sập cả pipeline | Không đạt tiêu chí hoàn thành M06 | Khắc phục tại M06 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DE-M04 | Roadmap mô-đun | `Module_04-computer-architecture-and-the-performance-model/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M05 | Roadmap mô-đun | `Module_05-operating-systems-concurrency-and-linux/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M06 | Roadmap mô-đun | `Module_06-networking-from-packet-to-api/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
