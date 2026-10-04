# Giai đoạn 4: SQL và nội tại cơ sở dữ liệu

Giai đoạn này kết hợp M09-M10. Người học chuyển từ `Bằng chứng hoàn thành Giai đoạn 3` sang khả năng tạo và bảo vệ bằng chứng tích hợp ở L148.

## Điều kiện đầu vào

| Năng lực bắt buộc | Bằng chứng được chấp nhận | Cách khắc phục |
|---|---|---|
| Bằng chứng hoàn thành Giai đoạn 3 | Sản phẩm và kết quả đánh giá của giai đoạn trước | Hoàn thành lại tiêu chí chưa đạt trước khi vào bài kiểm tra tích hợp |

## Đầu ra giai đoạn

Truy được đường đi của một lệnh ghi từ câu lệnh tới khôi phục, bảo vệ một lựa chọn mức cô lập theo dị thường, và khôi phục thành công.

## Thứ tự mô-đun

| Mô-đun | Năng lực được bổ sung | Phụ thuộc | Bằng chứng hoàn thành |
|---|---|---|---|
| [DE-M09](Module_09-relational-theory-and-sql-execution/roadmap.md) | Đi từ logic quan hệ tới kế hoạch thực thi vật lý: viết truy vấn đúng hạt và tối ưu bằng ước lượng số dòng, chi phí và bằng chứng | M02 · M03 · M04 | Với năm truy vấn chậm, nộp kế hoạch trước và sau, số khối đọc, số dòng ước lượng so với thực tế, và độ trễ; mọi tối ưu dẫn được về một quan sát trong kế hoạch |
| [DE-M10](Module_10-storage-engine-and-database-operations/roadmap.md) | Hiểu đường đi của một lệnh ghi và một lệnh đọc, chọn mức cô lập theo dị thường cần chặn, và vận hành được cơ sở dữ liệu gồm cả khôi phục đã kiểm chứng | M04 · M05 · M09 | Truy được một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục sau sự cố; thực hiện thành công một lần khôi phục thật |

**Sơ đồ thứ tự:** đọc từ trái sang phải; mỗi mô-đun tạo bằng chứng đầu vào cho mô-đun kế tiếp và bài kiểm tra cuối giai đoạn.

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "wrappingWidth": 520, "nodeSpacing": 64, "rankSpacing": 160}}}%%
flowchart LR
  P04["Giai đoạn 4<br/>SQL và nội tại cơ sở dữ liệu<br/>Roadmap hiện hành"]
  M09["M09 · Lý thuyết quan hệ và thực thi SQL<br/>Bài 113–132"]
  P04 --> M09
  M10["M10 · Storage engine và vận hành cơ sở dữ liệu<br/>Bài 133–148"]
  M09 --> M10
  G04["Bài kiểm tra cuối giai đoạn<br/>Bài 148"]
  M10 --> G04

  classDef phase fill:#2b1b12,color:#fff4e8,stroke:#ff8a3d,stroke-width:2px;
  classDef module fill:#fff4e8,color:#2b1b12,stroke:#c85e16,stroke-width:1.5px;
  classDef gate fill:#fffdf8,color:#2b1b12,stroke:#2b1b12,stroke-width:2px;
  class P04 phase;
  class M09,M10 module;
  class G04 gate;
```

## Lý do sắp xếp

- M09 đứng trước M10 vì điều kiện đầu vào của M10 sử dụng bằng chứng hoặc cơ chế đã hình thành ở mô-đun trước.

## Bài kiểm tra cuối giai đoạn

### Nhiệm vụ

Bài chấm sáu phần: A (20đ) truy đường đi của một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục · B (20đ) tối ưu hai truy vấn chậm, mỗi tối ưu dẫn về một quan sát trong kế hoạch và kết quả khớp tuyệt đối · C (20đ) chọn mức cô lập cho hai bất biến cho trước và chứng minh bằng phép kiểm chạy song song · D (20đ) khôi phục về một mốc thời gian và đối soát khớp · E (10đ) chẩn đoán một hệ đang bị chặn bằng khung nhìn khoá · F (10đ) nêu ba chỉ số vận hành phải theo dõi và ngưỡng dẫn từ phân bố.

### Cách đánh giá

| Tiêu chí | Bằng chứng | Ngưỡng đạt | Lỗi loại trực tiếp |
|---|---|---|---|
| Truy được đường đi của một lệnh ghi từ câu lệnh tới khôi phục, bảo vệ một lựa chọn mức cô lập theo dị thường, và khôi phục thành công. | Bài chấm sáu phần: A (20đ) truy đường đi của một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục · B (20đ) tối ưu hai truy vấn chậm, mỗi tối ưu dẫn về một quan sát trong kế hoạch và kết quả khớp tuyệt đối · C (20đ) chọn mức cô lập cho hai bất biến cho trước và chứng minh bằng phép kiểm chạy song song · D (20đ) khôi phục về một mốc thời gian và đối soát khớp · E (10đ) chẩn đoán một hệ đang bị chặn bằng khung nhìn khoá · F (10đ) nêu ba chỉ số vận hành phải theo dõi và ngưỡng dẫn từ phân bố. | Đạt ≥ 70/100, phần C và D đều ≥ 60%. Bất biến chỉ chứng minh bằng phép chạy tuần tự thì phần C bằng không; khôi phục không đối soát thì phần D bằng không. | Chọn mức cô lập theo tên · tối ưu làm đổi kết quả · bỏ phần khôi phục vì tốn thời gian · chứng minh bất biến bằng phép chạy tuần tự. |

## Điểm tích hợp

| Năng lực trước được dùng lại | Mô-đun sử dụng | Năng lực sau được mở khóa |
|---|---|---|
| M02 · M03 · M04 | M09 | Đi từ logic quan hệ tới kế hoạch thực thi vật lý: viết truy vấn đúng hạt và tối ưu bằng ước lượng số dòng, chi phí và bằng chứng |
| M04 · M05 · M09 | M10 | Hiểu đường đi của một lệnh ghi và một lệnh đọc, chọn mức cô lập theo dị thường cần chặn, và vận hành được cơ sở dữ liệu gồm cả khôi phục đã kiểm chứng |

## Khắc phục

| Tiêu chí chưa đạt | Bằng chứng chẩn đoán | Phần phải làm lại | Cách kiểm tra lại |
|---|---|---|---|
| Chọn mức cô lập theo tên · tối ưu làm đổi kết quả · bỏ phần khôi phục vì tốn thời gian · chứng minh bất biến bằng phép chạy tuần tự. | Bài làm, nhật ký và phản hồi theo tiêu chí L148 | Bài hoặc mô-đun tạo ra bằng chứng còn thiếu | Tình huống mới, giữ nguyên đầu ra và ngưỡng đạt |

## Rủi ro của giai đoạn

| Rủi ro | Cách phát hiện | Biện pháp kiểm soát |
|---|---|---|
| Học cú pháp rồi tối ưu bằng cách thêm chỉ mục cho mọi cột, không đọc kế hoạch lần nào, nên truy vấn vẫn chậm và ghi thì chậm thêm | Không đạt tiêu chí hoàn thành M09 | Khắc phục tại M09 trước khi thực hiện bài kiểm tra cuối giai đoạn |
| Chọn mức cô lập theo tên nghe có vẻ an toàn, và tin vào bản sao lưu chưa bao giờ khôi phục thử | Không đạt tiêu chí hoàn thành M10 | Khắc phục tại M10 trước khi thực hiện bài kiểm tra cuối giai đoạn |

## Tài liệu tham khảo

| Mã | Nguồn | Vị trí | Dùng cho |
|---|---|---|---|
| DE-M09 | Roadmap mô-đun | `Module_09-relational-theory-and-sql-execution/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |
| DE-M10 | Roadmap mô-đun | `Module_10-storage-engine-and-database-operations/roadmap.md` | Đầu ra, thứ tự bài và tiêu chí đánh giá của mô-đun |

Roadmap giai đoạn không thay thế roadmap mô-đun. Khi hai cấp diễn đạt khác nhau, mã đầu ra và tiêu chí do roadmap mô-đun sở hữu được dùng để rà soát.
