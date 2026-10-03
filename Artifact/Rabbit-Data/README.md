# Rabbit Data interface artifact

Thư mục này là cổng duyệt trải nghiệm trước khi xây lại `Web/`.

## Bản đang duyệt

- `index.html`: prototype tương tác cho roadmap, bài giảng và sau bài giảng.
- `Previews/DE/Phase_02/Module_04/roadmap.md`: bản thử định dạng roadmap cấp mô-đun cho DE M04.
- `Previews/DE/Phase_02/Module_04/diagram.html`: bản render Mermaid của quan hệ bài học → nội dung nguyên tử.
- `roadmaps.html`: gallery ảnh của toàn bộ roadmap DA và DE.
- `Roadmaps/`: 56 ảnh SVG cùng manifest truy vết roadmap nguồn và mã SHA-256.
- `screenshots/desktop/lesson-reader.png`: mốc kiểm tra desktop 1440 × 1100.
- `screenshots/mobile/lesson-reader.png`: mốc kiểm tra mobile 390 × 844.

Mở trực tiếp `index.html` để thử ba tab. Đây là prototype thiết kế, chưa đọc dữ liệu thật từ
`Material/` và chưa phải web application.

Artifact phải cho xem được tối thiểu:

- trang tổng quan roadmap;
- điều hướng Programme → Phase → Module → Lesson;
- trang đọc `note.md`;
- vùng riêng cho `after-note.md`;
- responsive desktop và mobile;
- visual language Rabbit Data có chủ ý, không dùng giao diện dashboard/template mặc định.

Ảnh được dựng lại bằng `npm run roadmap:diagrams`. `Web/` chỉ được tạo sau khi artifact này được
owner duyệt; khi xây, Web dùng các SVG đã render làm ảnh và không hiển thị mã Mermaid thô.
