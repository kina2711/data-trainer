# Giai đoạn 1: Nền tảng kỹ thuật

Giai đoạn này kết hợp M01-M03. Người học chuyển từ `Không yêu cầu bằng chứng kỹ thuật trước chương trình` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L044.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Không yêu cầu bằng chứng kỹ thuật trước chương trình | Không yêu cầu | Không áp dụng |

## Đầu ra giai đoạn

Nộp lời giải cho một bài toán dữ liệu cho trước, bảo vệ lựa chọn cấu trúc bằng số đo của chính mình, và chẩn đoán được một lỗi tiêm sẵn.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DE-M01](Module_01-engineering-thinking-git-and-debugging/roadmap.md) | Biến một yêu cầu mơ hồ thành hợp đồng kiểm thử được, quản lý thay đổi an toàn, và chẩn đoán lỗi bằng bằng chứng chứ bằng thử sai | Không. Dùng được terminal và sửa được tệp văn bản | Vẽ đúng đồ thị đối tượng của một kho Git và dự đoán đúng `HEAD` sau merge, rebase, reset; nhật ký gỡ lỗi có ít nhất ba giả thuyết bị bác bỏ bằng bằng chứng |
| [DE-M02](Module_02-python-for-production/roadmap.md) | Viết Python có hợp đồng, có kiểm thử, đóng gói được, quan sát được, và chọn đúng mô hình đồng thời theo khối lượng công việc | M01 | Gói cài được, có chú thích kiểu, có CI xanh, môi trường tái tạo được trên máy khác; một dịch vụ bất đồng bộ không có tác vụ mồ côi, không phát tán không giới hạn, không rò bể kết nối, và phân biệt được hết giờ cục bộ với hạn chót đầu cuối |
| [DE-M03](Module_03-data-structures-and-algorithms-for-systems/roadmap.md) | Chọn cấu trúc dữ liệu theo mẫu truy cập, tính cục bộ và tỉ lệ đọc ghi, rồi bảo vệ lựa chọn bằng số đo chứ bằng ký hiệu độ phức tạp | M02 | Với mỗi cấu trúc đã học, nêu được độ phức tạp thao tác, cách xếp trong bộ nhớ, khối lượng công việc phù hợp, và ca biên làm nó sụp |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P01["Giai đoạn 1<br/>Nền tảng kỹ thuật<br/>Roadmap hiện hành"]
  M01["M01 · Tư duy kỹ thuật, Git và gỡ lỗi<br/>Bài 1–12"]
  P01 --> M01
  M02["M02 · Python cho môi trường vận hành<br/>Bài 13–32"]
  M01 --> M02
  M03["M03 · Cấu trúc dữ liệu và thuật toán cho hệ thống<br/>Bài 33–44"]
  M02 --> M03
  G01["Bài kiểm tra cuối giai đoạn<br/>Bài 44"]
  M03 --> G01

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P01 phase;
  class M01,M02,M03 module;
  class G01 gate;
```

## Lý do sắp xếp

- M01 đứng trước M02 vì điều kiện đầu vào của M02 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.
- M02 đứng trước M03 vì điều kiện đầu vào của M03 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Nhận một bài toán xử lý tệp 3 GB với ngân sách bộ nhớ 200 MB. Bài chấm sáu phần: A (15đ) phát biểu bài toán sáu phần và phép kiểm chấp nhận · B (20đ) chương trình chạy đúng trong ngân sách bộ nhớ · C (20đ) lựa chọn cấu trúc dẫn bằng số đo của chính mình, không dẫn lý thuyết suông · D (15đ) bộ kiểm đủ bốn loại và quy trình tích hợp xanh · E (20đ) chẩn đoán một lỗi tiêm sẵn bằng bảng giả thuyết có ít nhất ba dòng bị bác bỏ · F (10đ) nhật ký có cấu trúc đủ để người khác chẩn đoán lại.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Nộp lời giải cho một bài toán dữ liệu cho trước, bảo vệ lựa chọn cấu trúc bằng số đo của chính mình, và chẩn đoán được một lỗi tiêm sẵn. | Nhận một bài toán xử lý tệp 3 GB với ngân sách bộ nhớ 200 MB. Bài chấm sáu phần: A (15đ) phát biểu bài toán sáu phần và phép kiểm chấp nhận · B (20đ) chương trình chạy đúng trong ngân sách bộ nhớ · C (20đ) lựa chọn cấu trúc dẫn bằng số đo của chính mình, không dẫn lý thuyết suông · D (15đ) bộ kiểm đủ bốn loại và quy trình tích hợp xanh · E (20đ) chẩn đoán một lỗi tiêm sẵn bằng bảng giả thuyết có ít nhất ba dòng bị bác bỏ · F (10đ) nhật ký có cấu trúc đủ để người khác chẩn đoán lại. | Đạt ≥ 70/100, phần B và C đều ≥ 60%. Lựa chọn cấu trúc không dẫn được về số đo của chính mình thì phần C bằng không. | Nạp cả tệp vào bộ nhớ · chọn cấu trúc rồi mới tìm lý do · bỏ phần chẩn đoán vì hết giờ · dẫn bậc độ phức tạp thay vì số đo. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| Không. Dùng được terminal và sửa được tệp văn bản | M01 | Biến một yêu cầu mơ hồ thành hợp đồng kiểm thử được, quản lý thay đổi an toàn, và chẩn đoán lỗi bằng bằng chứng chứ bằng thử sai |
| M01 | M02 | Viết Python có hợp đồng, có kiểm thử, đóng gói được, quan sát được, và chọn đúng mô hình đồng thời theo khối lượng công việc |
| M02 | M03 | Chọn cấu trúc dữ liệu theo mẫu truy cập, tính cục bộ và tỉ lệ đọc ghi, rồi bảo vệ lựa chọn bằng số đo chứ bằng ký hiệu độ phức tạp |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Nạp cả tệp vào bộ nhớ · chọn cấu trúc rồi mới tìm lý do · bỏ phần chẩn đoán vì hết giờ · dẫn bậc độ phức tạp thay vì số đo. | Bài làm, nhật ký và phản hồi theo tiêu chí L044 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Học thuộc lệnh Git rời rạc mà không có mô hình đối tượng, nên mất commit là mất luôn, và sửa lỗi bằng cách đổi thử tới khi hết báo lỗi | Không đạt tiêu chí hoàn thành M01 | Khắc phục tại M01 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Viết script chạy được trên máy mình rồi gọi đó là xong: không đóng gói, không kiểm thử, không đo, và chọn mô hình đồng thời theo lời khuyên trên mạng | Không đạt tiêu chí hoàn thành M02 | Khắc phục tại M02 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Học độ phức tạp như công thức để đọc, rồi không giải thích được vì sao một phép quét tuyến tính thắng một cấu trúc có độ phức tạp tốt hơn | Không đạt tiêu chí hoàn thành M03 | Khắc phục tại M03 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DE-M01 | Roadmap mô-đun | `Module_01-engineering-thinking-git-and-debugging/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M02 | Roadmap mô-đun | `Module_02-python-for-production/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M03 | Roadmap mô-đun | `Module_03-data-structures-and-algorithms-for-systems/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
