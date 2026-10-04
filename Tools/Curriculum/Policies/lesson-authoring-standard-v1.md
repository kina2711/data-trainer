# Tiêu chuẩn biên soạn bài giảng v1

Trạng thái: approved  
Owner: kina2711  
Ngày duyệt: 2026-10-04  
Mẫu chuẩn: DA-L001 và DE-L001

## Phạm vi

Tiêu chuẩn này áp dụng cho `teaching.md` của DA-L002 trở đi và DE-L002 trở đi. DA-L001 và DE-L001 là mẫu đã được owner duyệt về cấu trúc, độ sâu, cách giải thích và cách hiển thị trên web.

## Nội dung bắt buộc

Mỗi bài phải có câu hỏi trung tâm, mô hình khái niệm, ví dụ hoàn chỉnh, code hoặc artifact cụ thể, lỗi thường gặp, câu hỏi dẫn dắt, kiểm tra hiểu bài và phần kết luận ngắn. Mỗi khẳng định kỹ thuật phải có phạm vi và điều kiện áp dụng. Kết luận không được mạnh hơn bằng chứng.

Không công bố thời lượng, thời gian ước tính, lịch học hoặc áp lực hoàn thành trong nội dung dành cho người học. Metadata nội bộ phục vụ vận hành không được đưa lên giao diện bài học.

## Chuỗi tham chiếu trên web

Mỗi `teaching.md` phải có ít nhất ba liên kết theo cú pháp `[[wiki.note-id|Nhãn đọc]]` đến Second Brain.

Mỗi note được liên kết phải tồn tại trong index, có ít nhất một `source_id` thuộc sách và sách đó phải tồn tại trong Library. Giao diện phải cho phép mở note từ bài giảng và mở sách trực tiếp từ nguồn của note.

Đích liên kết không được sửa trong bước Humanizer.

## Văn phong

Văn phong phải khoa học, trung tính, trực tiếp và nghiêm khắc. Câu văn ưu tiên chủ thể, hành động, điều kiện và bằng chứng. Thuật ngữ phải được định nghĩa trước khi dùng.

Không dùng ví von, ẩn dụ trang trí, ngôn ngữ quảng cáo, câu dẫn tạo kịch tính, icon hoặc lời khen. Không dùng dấu gạch nối dài và dấu nháy cong. Hạn chế dấu nháy đơn và dấu nháy kép trong phần văn xuôi. JSON, code, lệnh, đường dẫn và dữ liệu giữ nguyên cú pháp cần thiết.

Không dùng cấu trúc đối lập giả như `không chỉ X mà còn Y` hoặc `không phải X mà là Y` khi vế phủ định không sửa một ngộ nhận có thật. Không dùng câu kết một dòng chỉ để lặp lại đoạn trước. Không dùng chữ đậm làm nhãn trang trí.

## Kiểm duyệt cuối

Sau khi nội dung hoàn tất, chạy skill `humanizer:humanizer` phiên bản 3.1.0 theo file mode. Quy trình gồm đánh dấu dấu hiệu, viết lại, đọc lại, quét lần cuối và lưu bản hoàn chỉnh.

Humanizer chỉ sửa văn xuôi. Code block, inline code, command, path, YAML metadata, dữ liệu và đích liên kết phải được giữ nguyên.

`lesson.yaml` phải ghi:

```yaml
editorial:
  standard: lesson-authoring-v1
  humanizer: blader/humanizer@3.1.0
  status: pass
```

Chạy `npm run lectures:authoring:test` sau Humanizer và trước khi rebuild web. Bài không đạt validator không được chuyển sang owner review.
