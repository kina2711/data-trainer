# Quy trình xây dựng Data Analytics Engineer Trainer

## Nguyên tắc vận hành

Quy trình có ba chặng theo thứ tự cố định:

1. Chuẩn bị học thuật cho toàn bộ DA và DE.
2. Xây và duyệt Web.
3. Sản xuất nội dung bài giảng.

Không viết bài giảng khi nguồn chưa qua đọc sâu. Không dùng tên tệp hoặc mục lục để suy diễn nội
dung tài liệu. Không chuyển sang chặng Web khi năm bước chuẩn bị học thuật chưa hoàn tất.

## Chặng I — Chuẩn bị học thuật một lần cho toàn dự án

### Bước 1 — Khóa objective

Objective được quản lý ở bốn tầng:

```text
Programme → Phase → Module → Lesson
```

Data Analyst và Data Engineer giữ nguyên nội dung riêng, kể cả nơi có chủ đề giao nhau. Tầng dưới
phải tạo bằng chứng đóng góp được cho tầng trên. Mỗi objective bài phải có:

- hành động quan sát được;
- sản phẩm hoặc bằng chứng;
- ngưỡng đạt;
- điều kiện tiên quyết;
- tầng Bloom khớp cách đánh giá;
- phương án đánh giá lại;
- critical failure khi có;
- đường dẫn và SHA-256 của roadmap nguồn.

Roadmap là nguồn sự thật. Registry là chỉ mục dẫn xuất, không thay thế roadmap và không được chép
objective vào `note.md` ở bước này.

Lệnh:

```bash
make objectives
```

Đầu ra:

- `Tools/Curriculum/Manifests/Academic/objectives.json`
- `Tools/Curriculum/Manifests/Academic/objective-options.yaml`
- `Tools/Curriculum/Manifests/Academic/objective-success-contract.yaml`
- `Tools/Curriculum/Manifests/Academic/objective-change-scope.json`

### Bước 2 — Chọn nguồn

Nguồn được chọn theo thứ tự:

1. chuẩn, specification và tài liệu chính thức;
2. nghiên cứu gốc hoặc giáo trình mở từ tác giả/tổ chức;
3. sách có tác giả, nhà xuất bản và đường lấy hợp pháp;
4. tệp đang có trong Library sau khi xác minh phiên bản, nguồn gốc và quyền sử dụng.

Mỗi objective ở bốn tầng phải truy được tới ít nhất một source ID. Việc gắn nguồn ở bước này chỉ
xác nhận độ phù hợp phạm vi; không có nghĩa là nguồn đã được đọc. Chương, trang và đoạn trích chỉ
được khóa ở Bước 4.

Lệnh:

```bash
make source-plan
```

Đầu ra:

- `Tools/Curriculum/Manifests/Academic/reference-inventory.json`
- `Tools/Curriculum/Manifests/Academic/source-catalog.json`
- `Tools/Curriculum/Manifests/Academic/source-plan.json`
- `Docs/Operations/SOURCE-REQUEST.md`

### Bước 3 — Owner chuẩn bị nguồn

Codex báo đúng một danh sách gom theo nguồn tại `Docs/Operations/SOURCE-REQUEST.md`, sau đó dừng.
Owner thực hiện ba việc:

1. mua hoặc mượn các sách thương mại;
2. xác nhận quyền sử dụng đối với tệp local được đánh dấu cần rà soát;
3. tải bản mở từ trang chính thức khi cần bản cố định để trích dẫn.

Docs/spec sống có thể đọc trực tuyến. Khi đọc phải ghi phiên bản hoặc ngày truy cập. Không dùng
tệp bị inventory đánh dấu nguồn gốc cần rà soát. Bước 4 chỉ mở khi owner trả lời `done`; nếu thiếu
nguồn, owner phải nêu source ID và phương án thay thế.

### Bước 4 — Đọc sâu và tạo source note

Mỗi nguồn được đọc theo phạm vi objective đã gắn. Source note phải tách rõ:

- dữ kiện hoặc lập luận của nguồn;
- trích dẫn nguyên văn ngắn khi cần;
- diễn giải của biên soạn viên;
- giới hạn, giả định và điểm còn tranh luận;
- locator ổn định: chương, mục, trang hoặc URL anchor;
- phiên bản, ngày truy cập và SHA-256 đối với tệp cục bộ.

Không ghi một khẳng định vào source note nếu không truy ngược được về locator. Không tự lấp phần
nguồn thiếu bằng kiến thức nhớ lại.

### Bước 5 — Phân rã Reference theo cấp sở hữu

Source note được phân phối vào cây Reference mà không nhân bản văn bản. Tầng dưới trỏ tới đoạn
nguồn chi tiết; tầng trên tổng hợp phạm vi và quan hệ.

```text
Material/<DA|DE>/Reference/
├── Programme/
├── Phase_<NN>-<slug>/
│   └── Reference/
└── Library/

Material/<DA|DE>/Curriculum/Phase_<NN>-<slug>/
└── Module_<NN>-<slug>/
    ├── Reference/
    └── Lesson_<NNN>-<slug>/
        └── Reference/
```

Data Analyst vẫn có phase cấu trúc trong roadmap hiện hành; không quay lại bố cục cũ không phase.
Mỗi reference fragment phải mang source ID, locator, objective ID và quan hệ `supports`,
`qualifies`, `contradicts` hoặc `example`.

## Chặng II — Xây Web

Chỉ bắt đầu sau khi Bước 1–5 hoàn tất và owner duyệt cổng chuẩn bị học thuật. Web hiển thị:

- roadmap Programme → Phase → Module → Lesson;
- sơ đồ đã render thành ảnh;
- bài giảng và `after-note.md` khi các tệp này được sản xuất;
- truy vết Reference mà không công khai tài liệu không có quyền phân phối.

`Artifact/` là bản xem trước thiết kế và luồng sử dụng. Web chỉ được triển khai sau khi Artifact
được duyệt.

## Chặng III — Sản xuất nội dung

Thứ tự sản xuất cho từng bài:

1. `note.md` — giáo trình sâu, không giới hạn theo thời lượng buổi học;
2. `after-note.md` — thực hành, kiểm tra cuối bài và bài làm sau buổi học;
3. slide và sơ đồ;
4. trang bài giảng trên Web.

Đầu `note.md` dùng ba heading:

```markdown
# Phase x: <Tên phase>
# Module x: <Tên module>
# Lesson x: <Tên lesson>
```

Không có front matter, phần giới thiệu metadata, mô tả đối tượng hoặc thời lượng. Phần nguồn mang
tên `## Reference`, không có cột trạng thái. Bài kết thúc bằng `## Key takeaways`. Nội dung chỉ
được viết từ Reference đã xử lý và phải giữ locator tới nguồn gốc.

## Cổng kiểm định

| Cổng | Điều kiện tối thiểu |
|---|---|
| Objective | `make objectives` đạt; đủ 2 programme, 14 phase, 40 module, 525 lesson |
| Source selection | `make source-plan` đạt; mỗi module và mỗi bài có ít nhất 3 sách, 3 document/spec, 3 website, 3 video và 1 Coursera course có module/week path; không nguồn nào bị ghi là đã đọc |
| Acquisition | Owner xác nhận `done` và giải quyết từng nguồn còn thiếu hoặc quyền sử dụng chưa rõ |
| Deep reading | Mọi khẳng định có locator; không còn locator ở trạng thái `pending-deep-reading` |
| Reference | Mọi fragment có source ID và objective ID; không sao chép tài liệu vượt quyền sử dụng |
| Web | Artifact được duyệt trước khi build/deploy |
| Lesson | Note, after-note, slide và trang Web truy được về Reference đã duyệt |

## Lệnh kiểm tra hiện hành

```bash
make test
make inventory
make objectives
make reference-inventory
make source-plan
make roadmap-diagrams
```

`make test` kiểm cấu trúc; nó không chứng minh nội dung đúng. `make objectives` kiểm hợp đồng đầu
ra. `make source-plan` kiểm độ phủ và tính toàn vẹn của kế hoạch nguồn. Việc đọc sâu và đánh giá
học thuật vẫn cần bằng chứng locator ở Bước 4.
