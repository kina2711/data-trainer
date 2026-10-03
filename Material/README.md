# Material

Mỗi chương trình có ba cây song song:

- `Curriculum`: nội dung học và scaffold của lesson.
- `Roadmap`: hợp đồng chương trình và module; nội dung hiện tại chưa được biên tập lại.
- `Reference`: thư viện nguồn cùng ghi chú tham chiếu theo phase, module và lesson.

```text
Material/<DA|DE>/
├── Curriculum/Phase/Module/Lesson/
├── Roadmap/Phase/Module/Lesson/
└── Reference/Phase/Module/Lesson/
```

Nguồn gốc dung lượng lớn nằm trong `Reference/Library`. Không nhân bản PDF xuống từng lesson;
lesson sẽ dùng `sources.yaml` để trỏ tới nguồn khi bước chuẩn hóa reference bắt đầu.
