# Data Analytics Engineer Trainer

Data Analytics Engineer Trainer là repository nguồn dùng để thiết kế, biên soạn, kiểm chứng và
xuất bản giáo trình đào tạo nghề Data bằng tiếng Việt. Repository không chỉ chứa danh sách bài
học: nó quản lý toàn bộ quan hệ giữa lộ trình năng lực, nội dung giảng dạy, bài thực hành, tiêu chí
đánh giá, tài liệu tham khảo và bản xem trước giao diện.

Dự án hiện có hai chương trình độc lập:

| Chương trình | Giai đoạn | Mô-đun | Bài học |
|---|---:|---:|---:|
| Data Analyst | 4 | 11 | 85 |
| Data Engineer | 10 | 29 | 440 |
| **Tổng** | **14** | **40** | **525** |

Mỗi chương trình đi từ nền tảng đến năng lực nghề nghiệp của vai trò tương ứng. Data Analyst và
Data Engineer dùng cùng một quy chuẩn cấu trúc nhưng giữ roadmap, bài giảng và nguồn tham khảo
riêng. Chủ đề có thể xuất hiện ở cả hai chương trình nếu mục tiêu nghề nghiệp, độ sâu hoặc sản phẩm
đánh giá khác nhau.

## Repository có những gì

| Thành phần | Nội dung | Vai trò |
|---|---|---|
| Curriculum | `note.md`, `after-note.md`, slide, câu hỏi và tài nguyên thực hành | Nội dung dùng để học và dạy |
| Roadmap | Roadmap chương trình, giai đoạn, mô-đun và metadata bài học | Xác định thứ tự học, đầu ra và cách đánh giá |
| Reference | Thư viện nguồn cùng manifest truy vết đến từng bài | Làm căn cứ cho nội dung kỹ thuật |
| Artifact | Bản xem trước roadmap, bài giảng, sơ đồ và giao diện Rabbit Data | Duyệt nội dung và trải nghiệm trước khi xây Web |
| Apps/SecondBrain | Ứng dụng Web và Desktop đọc 645 note canonical | Tra cứu, tìm kiếm, liên kết và đọc Second Brain |
| Web | Ứng dụng học giáo trình dành cho học viên | Chưa được xây lại trong cấu trúc mới |
| Docs | Kiến trúc repository, quy chuẩn biên soạn, quyết định và báo cáo kiểm tra | Quản trị cách dự án được phát triển |
| Tools | Script kiểm tra, generator, manifest, bản đồ và snapshot chuyển đổi | Tự động hóa nhưng không thay thế nguồn Markdown |

## Ai sử dụng repository này

- Người thiết kế chương trình dùng Roadmap để quản lý năng lực, thứ tự học và cổng đánh giá.
- Người biên soạn dùng Curriculum cùng Reference để viết bài và truy vết nguồn.
- Người dạy dùng `note.md`, `after-note.md`, slide và tài nguyên đi kèm bài.
- Người rà soát dùng manifest, tiêu chí hoàn thành và bộ kiểm tra để phát hiện nội dung thiếu hoặc
  không nhất quán.
- Người phát triển sản phẩm dùng Artifact làm chuẩn đầu vào trước khi xây Web.

Đây là kho nguồn đang trong giai đoạn chuẩn hóa. Cây mới đã chứa đủ 525 gói bài học và toàn bộ
Second Brain canonical đã có ứng dụng đọc riêng; tuy nhiên phần lớn bài học vẫn ở trạng thái nháp và
Web học giáo trình dành cho học viên chưa được phát hành. Mười bài đầu tiên của DA và DE đã được
nâng thành lecture package để curriculum owner rà soát.

## Nguyên tắc tổ chức

- `Material/` là nguồn giáo trình, roadmap và tài liệu tham khảo.
- Mỗi chương trình được tổ chức theo `Giai đoạn → Mô-đun → Bài học`.
- `Curriculum/`, `Roadmap/` và `Reference/` có cây thư mục tương ứng để suy ra đường dẫn bằng quy
  tắc.
- Roadmap là hợp đồng năng lực và đánh giá; `note.md` là nội dung giáo trình; `after-note.md` chứa
  phần thực hành và kiểm tra sau bài.
- Markdown là nguồn để con người đọc và duyệt. YAML chỉ giữ định danh, trạng thái và quan hệ cấu
  trúc cần cho công cụ.
- Artifact phải được duyệt trước khi xây lại Web.
- Không suy nội dung tài liệu từ tên tệp. Mọi khẳng định kỹ thuật cần được truy về nguồn cụ thể.

## Cấu trúc repository

```text
data-trainer/
├── Apps/
│   └── SecondBrain/             Web app, desktop app và index canonical
├── Material/                  nguồn đào tạo
│   ├── DA/                    chương trình Data Analyst
│   ├── DE/                    chương trình Data Engineer
│   └── Shared/                tài nguyên kỹ thuật dùng chung, không phải bài học dùng chung
├── Artifact/                  bản xem trước để duyệt nội dung và giao diện
│   └── Rabbit-Data/
├── Web/                       ứng dụng chính thức; hiện chưa được tạo
├── Docs/                      kiến trúc, quy chuẩn, quyết định và báo cáo rà soát
├── Tools/                     mã sinh, bản đồ, snapshot, manifest và bộ kiểm tra
├── Makefile
└── package.json
```

`Web/` chỉ xuất hiện sau khi Artifact vượt qua cổng duyệt. Không tạo bản Web tạm để thay thế bước
duyệt Artifact.

## Cấu trúc đích của mỗi chương trình

Cây dưới đây là cấu trúc đã chốt cho giai đoạn chuẩn hóa roadmap. Cây hiện tại đã có đủ
`Curriculum/`, `Roadmap/` và `Reference/`; roadmap Markdown đã có ở cấp chương trình, giai đoạn và
mô-đun. YAML cấp chương trình và mô-đun chưa được tạo.

```text
Material/<DA|DE>/
├── Curriculum/
│   └── Phase_<NN>-<slug>/
│       └── Module_<NN>-<slug>/
│           └── Lesson_<NNN>-<slug>/
├── Roadmap/
│   ├── roadmap.md
│   ├── roadmap.yaml
│   └── Phase_<NN>-<slug>/
│       ├── roadmap.md
│       ├── roadmap.yaml
│       └── Module_<NN>-<slug>/
│           ├── roadmap.md
│           ├── roadmap.yaml
│           └── Lesson_<NNN>-<slug>/roadmap.yaml
└── Reference/
    ├── Library/
    └── Phase_<NN>-<slug>/
        └── Module_<NN>-<slug>/
            └── Lesson_<NNN>-<slug>/sources.yaml
```

### `Curriculum/`

Chứa nội dung được dùng để học và dạy. Mỗi thư mục bài học có cấu trúc đích:

```text
Lesson_<NNN>-<slug>/
├── lesson.yaml       trạng thái và cấu hình xuất bản
├── note.md           chương giáo trình
├── after-note.md     thực hành, kiểm tra và bài làm sau bài học
├── quiz.md           ngân hàng câu hỏi hoặc đề riêng
├── homework.md       tệp tương thích từ cấu trúc cũ; ngừng dùng sau chuyển đổi
├── slides.md         nội dung trình chiếu
├── diagrams/         sơ đồ nguồn
└── materials/        dữ liệu và tài nguyên đi kèm bài
```

### `Roadmap/`

Quy chuẩn roadmap đã chốt sử dụng ba cấp. Mỗi thông tin chỉ có một cấp sở hữu; cấp cha tóm tắt và
dẫn chiếu, không sao chép toàn bộ nội dung của cấp con. Roadmap của DA và DE đã được chuyển sang
cấu trúc này và đang chờ rà soát nội dung.

#### Cấp chương trình

Roadmap chương trình xác định:

- vai trò và năng lực đích;
- phạm vi bao gồm và không bao gồm;
- điều kiện đầu vào;
- đầu ra chương trình;
- bản đồ giai đoạn và mô-đun;
- mô hình phụ thuộc;
- hệ thống đánh giá và điều kiện hoàn thành;
- độ phủ khung năng lực, rủi ro, quyết định và tài liệu tham khảo.

#### Cấp giai đoạn

Roadmap giai đoạn xác định:

- bước chuyển năng lực của giai đoạn;
- bằng chứng đầu vào;
- thứ tự mô-đun và lý do sắp xếp;
- bài kiểm tra tích hợp cuối giai đoạn;
- ngưỡng đạt, lỗi loại trực tiếp, cách khắc phục và kiểm tra lại;
- điểm nối với năng lực trước và sau.

Mỗi roadmap giai đoạn có một sơ đồ Mermaid thể hiện thứ tự mô-đun và điểm kiểm tra cuối giai đoạn.

#### Cấp mô-đun

Roadmap mô-đun phải cho người đọc biết mô-đun dạy gì, gồm những bài nào và đánh giá bằng cách nào.
Cấu trúc bắt buộc gồm:

1. Điều kiện đầu vào.
2. Đầu ra mô-đun.
3. Tiêu chí hoàn thành và lỗi loại trực tiếp.
4. Khái niệm cùng nguyên tắc bất biến.
5. Bảng `Các bài trong mô-đun`.
6. Một sơ đồ Mermaid `Bài học → nội dung nguyên tử`.
7. `Nội dung từng bài`: vấn đề, cơ chế, công việc và bằng chứng của từng bài.
8. Lý do sắp xếp.
9. Ma trận đánh giá và hình thức kiểm tra lại.
10. Bài thực hành bắt buộc.
11. Ngộ nhận, lỗi loại trực tiếp và cách khắc phục.
12. Điểm nối với mô-đun khác.
13. Tài liệu tham khảo và giới hạn phạm vi.

Mỗi roadmap ở cả ba cấp có đúng một khối Mermaid. Ở cấp mô-đun, mỗi nội dung nguyên tử nằm trên một
dòng riêng. Artifact và Web dùng ảnh SVG render từ chính khối Mermaid, giữ phần thay thế bằng văn
bản và hỗ trợ cuộn hoặc thu phóng cho sơ đồ rộng.

Quy chuẩn đầy đủ: [Roadmap-Format-Proposal.md](Docs/Standards/Roadmap-Format-Proposal.md).

### `Reference/`

- `Library/` giữ kho nguồn gốc, bao gồm PDF và tài liệu kỹ thuật.
- `sources.yaml` ở cấp bài trỏ đến nguồn được dùng cho bài đó.
- Không nhân bản PDF xuống từng thư mục bài.
- Tên sách hoặc tên tệp chưa phải là bằng chứng. Trích dẫn cần chỉ rõ chương, mục, trang hoặc phiên
  bản tài liệu.
- Nguồn của DA và DE được quản lý trong cây chương trình tương ứng, kể cả khi hai chương trình dùng
  cùng một chủ đề.

## Định dạng bài giảng

### `note.md`

`note.md` được trình bày như một chương giáo trình kỹ thuật, không bị giới hạn bởi thời lượng đứng
lớp. Người dạy tự chọn phạm vi sử dụng trong từng buổi.

Đầu tệp có đúng ba dòng tiêu đề:

```markdown
# Phase <N>: <Tên giai đoạn>
# Module <N>: <Tên mô-đun>
# Lesson <N>: <Tên bài học>
```

Thân bài có ba mục cố định:

- `Kết quả cần đạt`;
- `Key takeaways`;
- `Reference`.

Các mục nằm giữa phải mang tên đúng theo nội dung bài. Không dùng các tiêu đề chung như “Giới
thiệu”, “Deep dive” hoặc “Nội dung chính” nếu chúng không nói được phần đó đang giải thích điều gì.

Không đặt trong `note.md`:

- YAML frontmatter;
- thời lượng và phân bổ phút;
- mô tả đối tượng học;
- trạng thái biên soạn;
- phần thực hành;
- kiểm tra cuối bài;
- bài làm sau buổi học.

### `after-note.md`

Chứa phần áp dụng sau nội dung giáo trình:

- thực hành có dữ liệu hoặc môi trường rõ ràng;
- câu hỏi kiểm tra;
- bài làm sau bài học;
- sản phẩm phải nộp;
- tiêu chí chấm, lỗi loại trực tiếp và điều kiện làm lại.

Quy chuẩn đầy đủ: [Lesson-Format.md](Docs/Standards/Lesson-Format.md).

## Artifact, Second Brain và Curriculum Web

`Artifact/Rabbit-Data/` là nơi duyệt trải nghiệm trước khi viết ứng dụng chính thức. Artifact hiện
có:

- prototype giao diện Rabbit Data;
- màn hình roadmap, bài giảng và after-note;
- bản thử roadmap DE M04 theo định dạng mới;
- gallery 56 ảnh SVG được render từ roadmap cấp chương trình, giai đoạn và mô-đun;
- manifest gắn mỗi ảnh với roadmap nguồn và mã SHA-256.

Điểm vào: [Artifact/Rabbit-Data/README.md](Artifact/Rabbit-Data/README.md).

`Apps/SecondBrain/` là ứng dụng local-first đã hoạt động trên cả Web và Desktop. Hai giao diện dùng
chung index được sinh từ 645 note canonical trong `Docs/Second-Brain/2_Wiki/`. Index không chứa PDF
nguồn, credential, đường dẫn máy cá nhân hoặc nội dung `3_Toi`.

```bash
npm run brain:index    # dựng lại index sau khi note canonical thay đổi
npm run brain:web      # mở Web app tại http://127.0.0.1:4310
npm run brain:desktop  # mở Desktop app
npm run brain:test     # dựng index và kiểm tra Web/Desktop
```

Bản Web riêng tư hiện được phát hành tại
[Rabbit Data Second Brain](https://rabbit-data-second-brain.steviekitty.chatgpt.site).

`Web/` dành cho trải nghiệm học giáo trình hiện chưa tồn tại. Khi được phép xây, Curriculum Web phải:

- đọc trực tiếp cây `Material/`;
- hiển thị roadmap ở cấp chương trình, giai đoạn, mô-đun và bài học;
- hiển thị `note.md` và `after-note.md` tách biệt;
- hiển thị SVG đã render bằng thẻ ảnh, không đưa mã Mermaid thô ra giao diện;
- dựng lại SVG bằng phiên bản Mermaid đã ghim khi roadmap nguồn thay đổi;
- không dùng CDN trong bản phát hành;
- báo lỗi build khi Mermaid hoặc metadata không hợp lệ;
- giữ nguyên ranh giới DA và DE trong điều hướng, tìm kiếm và URL.

Chạy `npm run roadmap:diagrams` để dựng lại 56 ảnh và gallery
`Artifact/Rabbit-Data/roadmaps.html`.

## Trạng thái hiện tại

Kết quả từ `make inventory`:

| Hạng mục | Số lượng |
|---|---:|
| Giai đoạn | 14 |
| Mô-đun | 40 |
| Bài học | 525 |
| `note.md` | 525 |
| `after-note.md` | 525 |
| `lesson.yaml` | 525 |
| Roadmap Markdown | 56 |
| Roadmap Draw.io | 42 |
| Tệp nguồn được bảo toàn | 2.670 |
| Manifest nguồn cấp bài | 525 |
| Note canonical trong Second Brain | 645 |
| Lecture package sẵn sàng để owner review | 10 |

Trạng thái biên soạn:

- 515 bài ở trạng thái `draft`;
- 10 bài đầu tiên, gồm DA 001–005 và DE 001–005, ở trạng thái `ready-for-owner-review`;
- 10 lecture package có tổng cộng 90 scene, 170 slide, 100 câu quiz và 10 homework rubric;
- 56 roadmap Markdown hiện tại gồm 2 roadmap chương trình, 14 roadmap giai đoạn và 40 roadmap
  mô-đun;
- toàn bộ roadmap Markdown đã dùng format phân cấp mới và đang ở trạng thái chờ rà soát nội dung;
- DE M04 trong `Artifact/` là chuẩn trình bày được dùng cho roadmap nguồn tương ứng;
- YAML hiện có ở 14 giai đoạn và 525 bài học; YAML cấp chương trình và mô-đun chưa được tạo;
- generator cũ chưa được sửa đường dẫn cho cấu trúc mới và không được chạy;
- Second Brain Web/Desktop đã được xây và kiểm tra; Curriculum Web vẫn chưa được xây.

`make test` và `make inventory` hiện báo fail vì baseline validator vẫn chờ 2.126 tệp nguồn trong khi
kho nguồn cục bộ đã có 2.670 tệp. Validator cũng báo mã băm phê duyệt roadmap DA đã cũ. Hai sai lệch
này phải được xử lý bằng một quyết định kiểm kê/phê duyệt riêng; không được che lỗi hoặc tự cập nhật
hash chỉ để làm test xanh.

## Lệnh kiểm tra

```bash
make help       # liệt kê các lệnh hiện có
make test       # kiểm tra cấu trúc, số lượng và các điều kiện bất biến hiện hành
make inventory  # in thống kê DA, DE, roadmap, reference và lesson package
npm run brain:test              # kiểm tra Second Brain Web/Desktop
npm run lectures:first10:test   # kiểm tra 10 lecture package đầu tiên
```

Không chạy các generator trong `Tools/Curriculum/Generators/` cho đến khi hoàn tất chuyển đổi
toolchain. Second Brain có quy trình build/test riêng; Curriculum Web chưa có lệnh build hoặc deploy.

## Quy trình thay đổi nội dung

1. Xác định đúng chương trình, giai đoạn, mô-đun và bài học.
2. Đọc roadmap ở cả cấp cha và cấp đang sửa.
3. Đọc `sources.yaml` và tài liệu nguồn có liên quan; không suy nội dung từ tên tài liệu.
4. Sửa đúng artifact sở hữu nội dung:
   - roadmap cho hợp đồng năng lực và đánh giá;
   - `note.md` cho nội dung giáo trình;
   - `after-note.md` cho thực hành và kiểm tra;
   - `sources.yaml` cho truy vết nguồn.
5. Dựng hoặc cập nhật bản xem trước trong `Artifact/` khi thay đổi cách trình bày.
6. Chạy `make test` và kiểm tra trực quan artifact liên quan.
7. Chỉ chuyển sang Web sau khi Artifact được duyệt.

## Quy tắc không được phá vỡ

- Không gộp nội dung DA và DE thành một bài dùng chung.
- Không xóa hoặc di chuyển nguồn trong `Reference/Library` khi chưa có manifest đối chiếu.
- Không sửa đồng thời roadmap và giáo trình nếu phạm vi công việc chỉ yêu cầu một loại artifact.
- Không coi tên bài là bằng chứng rằng nội dung đã được dạy hoặc đánh giá.
- Không dùng các từ như “toàn diện”, “tiên tiến”, “thực chiến”, “làm chủ” hoặc “chuẩn FAANG” thay
  cho thuộc tính có thể kiểm tra.
- Không đưa thời lượng, đối tượng học hoặc metadata quản trị vào phần văn của `note.md`.
- Không dùng `Docs/Archive/` làm nguồn chuẩn hiện hành.
- Không deploy Curriculum Web khi chưa có cổng duyệt và lệnh build chính thức. Second Brain dùng
  quy trình build, kiểm tra và phát hành riêng trong `Apps/SecondBrain/`.

## Tài liệu điều hành

| Tài liệu | Mục đích |
|---|---|
| [Repository-Structure.md](Docs/Architecture/Repository-Structure.md) | Ranh giới thư mục và cây nguồn |
| [ADR-0001](Docs/Decisions/ADR-0001-Repository-Structure-Migration.md) | Quyết định chuyển cấu trúc repository |
| [Roadmap-Format-Proposal.md](Docs/Standards/Roadmap-Format-Proposal.md) | Quy chuẩn roadmap ba cấp |
| [Lesson-Format.md](Docs/Standards/Lesson-Format.md) | Quy chuẩn `note.md` và `after-note.md` |
| [Artifact/Rabbit-Data/README.md](Artifact/Rabbit-Data/README.md) | Cổng duyệt giao diện Rabbit Data |
| [Tools/Curriculum/README.md](Tools/Curriculum/README.md) | Trạng thái và giới hạn của toolchain |
