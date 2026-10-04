# Giai đoạn 1: Nền tảng và vai trò Data Analyst

Giai đoạn này kết hợp M01-M02. Người học chuyển từ `Không yêu cầu bằng chứng kỹ thuật trước chương trình` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L016.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Không yêu cầu bằng chứng kỹ thuật trước chương trình | Không yêu cầu | Không áp dụng |

## Đầu ra giai đoạn

Thực hiện trọn quy trình từ tệp không chuẩn tới báo cáo có đối soát, trên dữ liệu chưa gặp, trong giới hạn thời gian.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DA-M01](Module_01-introduction-to-the-data-analyst-role/roadmap.md) | Chuyển một yêu cầu phát biểu mơ hồ thành đặc tả phân tích mà người thứ hai triển khai được không cần hỏi lại | Không | Nộp sáu đặc tả cho sáu yêu cầu mơ hồ. Một học viên khác đọc và triển khai được ít nhất năm trong sáu, không đặt câu hỏi làm rõ nào |
| [DA-M02](Module_02-excel-for-data-analysis/roadmap.md) | Chuyển một tệp Excel không chuẩn thành quy trình nạp và làm sạch chạy lại được bằng một thao tác, có đối soát | M01 | Đạt Cổng 1 ≥ 70/100, không phần nào dưới 50% |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P01["Giai đoạn 1<br/>Nền tảng và vai trò Data Analyst<br/>Roadmap hiện hành"]
  M01["M01 · Nhập môn vai trò Data Analyst<br/>Bài 1–5"]
  P01 --> M01
  M02["M02 · Excel cho phân tích dữ liệu<br/>Bài 6–16"]
  M01 --> M02
  G01["Bài kiểm tra cuối giai đoạn<br/>Bài 16"]
  M02 --> G01

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P01 phase;
  class M01,M02 module;
  class G01 gate;
```

## Lý do sắp xếp

- M01 đứng trước M02 vì điều kiện đầu vào của M02 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Phần A (25đ) chuyển tệp không chuẩn về dạng dài · Phần B (25đ) làm sạch văn bản và ngày tháng có đối soát · Phần C (20đ) ghép ba bảng và truy nguyên mã không khớp · Phần D (20đ) PivotTable trả lời 8 câu hỏi nghiệp vụ · Phần E (10đ) một trang tổng quan có biểu đồ chọn đúng loại kèm lý do.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Thực hiện trọn quy trình từ tệp không chuẩn tới báo cáo có đối soát, trên dữ liệu chưa gặp, trong giới hạn thời gian. | Phần A (25đ) chuyển tệp không chuẩn về dạng dài · Phần B (25đ) làm sạch văn bản và ngày tháng có đối soát · Phần C (20đ) ghép ba bảng và truy nguyên mã không khớp · Phần D (20đ) PivotTable trả lời 8 câu hỏi nghiệp vụ · Phần E (10đ) một trang tổng quan có biểu đồ chọn đúng loại kèm lý do. | ≥ 70/100 và không phần nào dưới 50%. Không đạt thì áp dụng quy trình khắc phục của roadmap giai đoạn, thi lại một lần. Đạt ≥ 70/100 và không phần nào dưới 50%. Đây là exit criterion của Mô-đun 2. | Thao tác tay thay vì Power Query rồi hết giờ · bỏ phần đối soát · chọn biểu đồ không nêu được lý do. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| Không | M01 | Chuyển một yêu cầu phát biểu mơ hồ thành đặc tả phân tích mà người thứ hai triển khai được không cần hỏi lại |
| M01 | M02 | Chuyển một tệp Excel không chuẩn thành quy trình nạp và làm sạch chạy lại được bằng một thao tác, có đối soát |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Thao tác tay thay vì Power Query rồi hết giờ · bỏ phần đối soát · chọn biểu đồ không nêu được lý do. | Bài làm, nhật ký và phản hồi theo tiêu chí L016 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Học lướt vì tưởng là module dẫn nhập, dẫn tới ở M7 không định vị được điểm bắt đầu điều tra | Không đạt tiêu chí hoàn thành M01 | Khắc phục tại M01 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Bỏ qua module vì đã dùng Excel trong công việc trước đó, trong khi phần Power Query và dạng dữ liệu dài mới là phần vai trò phân tích cần | Không đạt tiêu chí hoàn thành M02 | Khắc phục tại M02 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DA-M01 | Roadmap mô-đun | `Module_01-introduction-to-the-data-analyst-role/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DA-M02 | Roadmap mô-đun | `Module_02-excel-for-data-analysis/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
