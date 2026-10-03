# Giai đoạn 7: Nạp, chuyển đổi, chất lượng và quản trị dữ liệu

Giai đoạn này kết hợp M16–M19. Người học chuyển từ `Bằng chứng hoàn thành Giai đoạn 6` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L308.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Bằng chứng hoàn thành Giai đoạn 6 | Sản phẩm và kết quả đánh giá của giai đoạn trước | Hoàn thành lại tiêu chí chưa đạt trước khi vào bài kiểm tra tích hợp |

## Đầu ra giai đoạn

Chứng minh tính đầy đủ từ nguồn tới đích bằng đối soát, bảo vệ một khẳng định về dòng dõi trước chất vấn, và phục hồi một sự cố dữ liệu an toàn.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DE-M16](Module_16-data-ingestion-and-integration-engineering/roadmap.md) | Đưa dữ liệu từ cơ sở dữ liệu, giao diện lập trình, tệp, dịch vụ ngoài và nguồn sự kiện vào vùng thô với tính đầy đủ, khả năng chạy lại, tiến hoá lược đồ và bảo vệ nguồn | M06 · M09 · M10 · M15 | Ba loại nguồn chạy được cả khởi tạo, tăng dần, nạp bù và chạy lại; hỏng giữa chừng không mất dữ liệu im lặng; đối soát độc lập từ nguồn tới vùng thô đạt trong phạm vi đã ghi |
| [DE-M17](Module_17-elt-dbt-and-workflow-orchestration/roadmap.md) | Thiết kế đường dẫn theo lô có tính đúng qua chạy lại, nạp bù và đổi lược đồ; thành thạo dbt và thành thạo một bộ điều phối | M01 · M02 · M09 · M10 · M11 · M14 · M15 · M16 | Ít nhất ba mô hình tăng dần qua trọn ma trận chế độ hỏng kèm chứng minh bảy phần; một lần đổi lược đồ phá vỡ có phiên bản, kế hoạch chuyển đổi cho bên tiêu thụ và đường quay lại |
| [DE-M18](Module_18-data-quality-and-data-reliability-engineering/roadmap.md) | Biến câu dữ liệu đúng thành hợp đồng, bất biến, cam kết dịch vụ, chốt kiểm soát và một vòng đời sự cố có phục hồi | M09 · M10 · M11 · M16 · M17 | Kế hoạch kiểm soát theo tầng có chủ sở hữu, mức nghiêm trọng, hành động và đường phục hồi cho mọi tài sản trọng yếu; hai sự cố được sửa, đối soát và ghi lại |
| [DE-M19](Module_19-metadata-engineering-catalog-lineage-and-governance/roadmap.md) | Thiết kế mô hình siêu dữ liệu chuẩn, thu thập được dòng dõi có xuất xứ và độ tin cậy, rồi vận hành quyền sở hữu, từ điển, chứng nhận và khai tử | M11 · M13 · M17 · M18 | Định danh chuẩn phân giải cùng một tài sản xuyên hệ và xuyên môi trường mà không đụng độ; đường dòng dõi trọng yếu có xuất xứ cùng độ tin cậy; chú thích thủ công không bị thu thập tự động ghi đè |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P07["Giai đoạn 7<br/>Nạp, chuyển đổi, chất lượng và quản trị dữ liệu<br/>Roadmap hiện hành"]
  M16["M16 · Kỹ nghệ nạp và tích hợp dữ liệu<br/>Bài 231–246"]
  P07 --> M16
  M17["M17 · ELT, dbt và điều phối workflow<br/>Bài 247–274"]
  M16 --> M17
  M18["M18 · Chất lượng và độ tin cậy dữ liệu<br/>Bài 275–292"]
  M17 --> M18
  M19["M19 · Metadata, catalog, lineage và quản trị<br/>Bài 293–308"]
  M18 --> M19
  G07["Bài kiểm tra cuối giai đoạn<br/>Bài 308"]
  M19 --> G07

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P07 phase;
  class M16,M17,M18,M19 module;
  class G07 gate;
```

## Lý do sắp xếp

- M16 đứng trước M17 vì điều kiện đầu vào của M17 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.
- M17 đứng trước M18 vì điều kiện đầu vào của M18 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.
- M18 đứng trước M19 vì điều kiện đầu vào của M19 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) chứng minh tính đầy đủ từ nguồn tới tầng phục vụ bằng thang đối soát, nêu rõ tổng thể, cửa sổ, phép kiểm và dung sai · B (20đ) trình chứng minh bảy phần cho một mô hình tăng dần và chạy hai ô của ma trận chế độ hỏng tại chỗ · C (15đ) một lỗi thầm lặng được tiêm; định vị phạm vi ảnh hưởng bằng dòng dõi và chạy phục hồi an toàn · D (20đ) bảo vệ một khẳng định về dòng dõi: cạnh này đến từ đâu, độ tin cậy bao nhiêu, phần nào chưa biết · E (15đ) giải thích ranh giới giữa danh mục ghi nhận và hệ cưỡng chế cho ba nghĩa vụ · F (10đ) rà một bộ quy tắc chất lượng và tìm phép kiểm có phạm vi che dữ liệu hỏng.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Chứng minh tính đầy đủ từ nguồn tới đích bằng đối soát, bảo vệ một khẳng định về dòng dõi trước chất vấn, và phục hồi một sự cố dữ liệu an toàn. | Buổi 180 phút: 135 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) chứng minh tính đầy đủ từ nguồn tới tầng phục vụ bằng thang đối soát, nêu rõ tổng thể, cửa sổ, phép kiểm và dung sai · B (20đ) trình chứng minh bảy phần cho một mô hình tăng dần và chạy hai ô của ma trận chế độ hỏng tại chỗ · C (15đ) một lỗi thầm lặng được tiêm; định vị phạm vi ảnh hưởng bằng dòng dõi và chạy phục hồi an toàn · D (20đ) bảo vệ một khẳng định về dòng dõi: cạnh này đến từ đâu, độ tin cậy bao nhiêu, phần nào chưa biết · E (15đ) giải thích ranh giới giữa danh mục ghi nhận và hệ cưỡng chế cho ba nghĩa vụ · F (10đ) rà một bộ quy tắc chất lượng và tìm phép kiểm có phạm vi che dữ liệu hỏng. | Đạt ≥ 70/100, phần A và D đều ≥ 60%. Tuyên bố đầy đủ dựa trên lấy mẫu thì phần A bằng không; trình bày cạnh suy ra như sự thật mà không nêu xuất xứ thì phần D bằng không. | Dùng mọi việc xanh làm bằng chứng đầy đủ · trình bày cạnh suy ra như sự thật · công bố bản sửa trước khi đối soát · tuyên bố danh mục cưỡng chế chính sách. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| M06 · M09 · M10 · M15 | M16 | Đưa dữ liệu từ cơ sở dữ liệu, giao diện lập trình, tệp, dịch vụ ngoài và nguồn sự kiện vào vùng thô với tính đầy đủ, khả năng chạy lại, tiến hoá lược đồ và bảo vệ nguồn |
| M01 · M02 · M09 · M10 · M11 · M14 · M15 · M16 | M17 | Thiết kế đường dẫn theo lô có tính đúng qua chạy lại, nạp bù và đổi lược đồ; thành thạo dbt và thành thạo một bộ điều phối |
| M09 · M10 · M11 · M16 · M17 | M18 | Biến câu dữ liệu đúng thành hợp đồng, bất biến, cam kết dịch vụ, chốt kiểm soát và một vòng đời sự cố có phục hồi |
| M11 · M13 · M17 · M18 | M19 | Thiết kế mô hình siêu dữ liệu chuẩn, thu thập được dòng dõi có xuất xứ và độ tin cậy, rồi vận hành quyền sở hữu, từ điển, chứng nhận và khai tử |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Dùng mọi việc xanh làm bằng chứng đầy đủ · trình bày cạnh suy ra như sự thật · công bố bản sửa trước khi đối soát · tuyên bố danh mục cưỡng chế chính sách. | Bài làm, nhật ký và phản hồi theo tiêu chí L308 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Đồng nhất việc trình kết nối chạy xong với việc đường dẫn dữ liệu đúng, và đẩy mốc tiến độ trước khi dữ liệu được công bố bền vững | Không đạt tiêu chí hoàn thành M16 | Khắc phục tại M16 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Tắt phép kiểm hoặc hạ mức nghiêm trọng để đường dẫn xanh, và dùng nạp lại toàn bộ như cách mặc định để chữa lỗi của mô hình tăng dần mà không truy nguyên nhân | Không đạt tiêu chí hoàn thành M17 | Khắc phục tại M17 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Dùng số lượng phép kiểm làm bằng chứng độ phủ mà không ánh xạ với rủi ro, và chọn ngưỡng sao cho bảng theo dõi luôn xanh | Không đạt tiêu chí hoàn thành M18 | Khắc phục tại M18 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Báo cáo dòng dõi do bộ phân tích suy ra như một sự thật, và tuyên bố danh mục cưỡng chế quyền truy cập trong khi nó chỉ lưu siêu dữ liệu | Không đạt tiêu chí hoàn thành M19 | Khắc phục tại M19 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DE-M16 | Roadmap mô-đun | `Module_16-data-ingestion-and-integration-engineering/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M17 | Roadmap mô-đun | `Module_17-elt-dbt-and-workflow-orchestration/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M18 | Roadmap mô-đun | `Module_18-data-quality-and-data-reliability-engineering/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M19 | Roadmap mô-đun | `Module_19-metadata-engineering-catalog-lineage-and-governance/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
