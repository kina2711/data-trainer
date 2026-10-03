# Repository structure

## Source boundaries

```text
Material/   nguồn đào tạo
Artifact/   prototype được duyệt trước khi xây ứng dụng
Web/        ứng dụng chính thức, chỉ xuất hiện sau cổng duyệt Artifact
Docs/       quy chuẩn và quyết định của repository
Tools/      mã sinh, kiểm tra và provenance của curriculum
```

## Material hierarchy

`DA` và `DE` cùng dùng một cấu trúc:

```text
<Programme>/
├── Curriculum/
│   └── Phase_<NN>-<slug>/
│       └── Module_<NN>-<slug>/
│           └── Lesson_<NNN>-<slug>/
├── Roadmap/
│   ├── roadmap.md
│   └── Phase_<NN>-<slug>/Module_<NN>-<slug>/Lesson_<NNN>-<slug>/
└── Reference/
    ├── Library/
    └── Phase_<NN>-<slug>/Module_<NN>-<slug>/Lesson_<NNN>-<slug>/
```

Roadmap và Reference mirror Curriculum để đường dẫn giữa ba loại artifact có thể suy ra bằng
quy tắc, không cần bảng ánh xạ thủ công.

## DA phase mapping

Bốn phase cấu trúc bám vào bốn mốc đã có trong roadmap DA; đây chưa phải lần biên tập roadmap:

| Phase | Module | Mốc kết thúc |
|---|---|---:|
| 01 · Foundations and role | M1–M2 | Lesson 16 |
| 02 · SQL and data access | M3 | Lesson 30 |
| 03 · Analytical foundations and BI | M4–M6 | Lesson 54 |
| 04 · Applied analytics and capstone | M7–M11 | Lesson 85 |

DE dùng nguyên ánh xạ 10 phase trong module map đã duyệt.
