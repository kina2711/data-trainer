# Data 2026 — chạy trong Claude Code tại VSCode

Nâng chuẩn ba chương trình DA, DE, AE đang nằm trong `material/`. Không làm lại từ đầu: bắt đầu từ
roadmap đã có, viết lại ngôn từ, chi tiết hoá, viết objective từng tầng — rồi mới đi tìm nguồn.

## Chuẩn bị một lần

```bash
cd /home/kina2711/PROJECT/data-trainer
claude plugin install humanizer@humanizer     # nếu chưa có
data-agent doctor                             # kiểm tra bộ skill nhìn thấy được từ đây
```

Plugin cài ngoài thư mục này, nên các tệp nó trỏ tới là lượt đọc ngoài working directory. Cấp một
lần trong `~/.claude/settings.json`:

```json
{ "permissions": { "additionalDirectories": ["~/.claude/plugins/cache"] } }
```

## Tám bước, và hai chỗ dừng chờ bạn

| Bước | Việc | Skill |
|---|---|---|
| 1 | Bắt đầu từ roadmap, viết lại ngôn từ | `humanizer` · `core-review-ai-prose` |
| 2 | Roadmap chi tiết → objective role → module → buổi | `academy-build-skill-track-map` · `academy-define-role-learning-outcomes` · `academy-design-learning-module` · `academy-map-questions-to-learning-objectives` |
| 3 | Từ tên + objective mới đi tìm nguồn | `content-research-technical-topic` |
| 3b | Nêu tên nguồn và cách lấy | cùng task trên |
| 3c | **Dừng — bạn tải về, đặt vào `ref/`, xác nhận** | `core-request-human-approval` → `book-assess-source-rights` |
| 4 | Trích note từ sách, tài liệu, video | `book-extract-source-text` · `brain-transcribe-audio-video-source` |
| 5 | Soạn bài, đo theo objective ở bước 2 | `academy-outline-lesson-from-source` · `academy-write-theory-lesson` |
| 6 | Index, audit, ba cổng kiểm duyệt AI | `academy-audit-note-corpus` · `core-review-ai-*` |
| 7 | **Dừng — bạn chốt nội dung** | `orchestrator-manage-approval-ledger` |
| 8 | Chốt → đóng gói + hướng dẫn build web | `content-package-technical-series-repository` |

38 task, 32 đợt, chín cổng cần bạn duyệt. Con số nằm trong
`harnesses/data-2026.harness.json` của bộ skill; validator đối chiếu chứ không để ai gõ tay.

Hai bất biến được kiểm bằng code mỗi lần build: **tìm nguồn phải sau khi có objective**, và **đọc
nguồn phải sau khi bạn xác nhận**.

## Chạy

```bash
cd /home/kina2711/PROJECT/data-trainer
claude
```

Rồi dán prompt bên dưới, sửa bốn dòng đầu. Hoặc mở app Data Agent, chọn **Data 2026**, điền 6 ô.

## Thứ luồng cố ý không tự làm

**Không tự tải sách.** Bước 3b nêu tên nguồn và cách lấy; bạn tải, đặt vào `material/<chương
trình>/**/ref/`, rồi báo. Trong lúc chờ nó không được đoán nội dung sách từ tên sách. Sách từ site
chia sẻ lậu nằm ngoài luồng — `book-assess-source-rights` là cổng chạy trước mọi thao tác đọc sâu,
nên đây là chỗ luồng dừng chứ không phải lời khuyên.

**Không tự deploy.** Bước 8 hướng dẫn bạn chạy `make`. Một luồng có bước deploy là luồng sẽ có lúc
nói "đã deploy" mà không ai cầm bằng chứng.

**Không tự sinh dataset.** Nó đề xuất ý tưởng và nói rõ cần dữ liệu hình dạng gì. Bạn đưa dữ liệu.

## Prompt đầy đủ

Sửa bốn dòng đầu rồi dán nguyên khối:

```
Chạy workflow `data-2026` trong workflows/, điều phối qua data-department-orchestrator.
Thư mục làm việc là repo data-trainer.

Chương trình: Data Analyst (DA)
Phạm vi lần này: DA/Module 3
Chạy tới: gợi ý nguồn và cách lấy, rồi dừng chờ tôi tải
Đường tôi lấy nguồn ngoài: <O'Reilly learning / sách giấy đã mua / chỉ nguồn mở và docs chính thức>

BƯỚC 1 — BẮT ĐẦU TỪ ROADMAP, viết lại ngôn từ. Đọc roadmap.md hiện có trong phạm vi rồi rà văn
phong bằng skill humanizer nếu nó có mặt; không có thì dùng authored-prose-voice.md của bộ này và
nói rõ đã dùng cái nào. Nó chỉ sửa văn xuôi: giữ nguyên code, câu lệnh, đường dẫn, bảng, YAML
front matter và link. Và nó KHÔNG được thêm hay bớt một dữ kiện, con số, tên hay trích dẫn nào —
mất một claim khi viết lại là lỗi, không phải gọn hơn. Số bài, số module, thời lượng trong bảng
phải khớp y như trước.

BƯỚC 2 — ROADMAP CHI TIẾT rồi OBJECTIVE TỪNG TẦNG, từ trên xuống: (a) role/skill — học xong
chương trình làm được gì; (b) từng module; (c) từng buổi học. Objective phải quan sát được và
kiểm chứng được, không phải "hiểu về X". Mỗi module kèm exit criterion. Đây là thứ mọi bước sau đo
theo, nên viết xong objective mới được đi tiếp.

BƯỚC 3 — TỪ TÊN VÀ OBJECTIVE mới đi tìm nguồn, không phải ngược lại. Dùng chính tên và objective
vừa viết làm câu tìm:
"The best book/document/video to learn <tên và objective>"
Tìm trước khi có objective là gom tài liệu cho một câu hỏi chưa ai đặt.

BƯỚC 3b — NÊU TÊN NGUỒN VÀ CÁCH LẤY. Với mỗi nguồn: tên và tác giả, phiên bản hoặc năm, nó phục
vụ objective nào, và lấy ở đâu — link nhà xuất bản, bản open-access, docs chính thức, arXiv, khoá
học, hoặc ghi rõ "cần mua" / "mượn thư viện". Không tải sách từ site chia sẻ lậu và không đưa link
tới những site đó. Nguồn ngoài theo technical-content-quality-standard: tài liệu chính thức đang
hiện hành, standard, nghiên cứu gốc, hoặc bằng chứng chạy thật. Blog cá nhân, nội dung tổng hợp
lại và bài do AI viết không tính là nguồn.

BƯỚC 3c — DỪNG, CHỜ TÔI TẢI VỀ. Sau khi nêu danh sách thì dừng. Tôi tự tải và đặt vào
material/<chương-trình>/**/ref/ rồi báo bạn. Đừng đọc sâu, đừng trích, đừng suy nội dung sách từ
tên sách trong lúc chờ. Tôi xác nhận xong thì book-assess-source-rights chạy trước tiên và chốt
ngưỡng trích dẫn ngay ở đó.

BƯỚC 4 — TRÍCH NOTE. PDF và sách qua book-extract-source-text; video qua
brain-transcribe-audio-video-source có timestamp và ghi rõ chỗ nghe không rõ; slide và ảnh qua
brain-process-image-and-diagram-source. Note ref đầy đủ chứ không tóm tắt, tách rõ bốn phần: nguồn
nói gì / tổng hợp / suy luận chưa có trong nguồn / còn chưa chắc. Mỗi mục kiến thức phải chỉ ra
được nó nằm ở đâu trong nguồn. Thứ không đọc được thì nói là không đọc được.

BƯỚC 5 — SOẠN BÀI, đo theo objective ở bước 2. Giữ nguyên cấu trúc ba tầng của repo: Chương trình
→ Module → Bài giảng, ghi vào
material/<chương-trình>/curriculum/module_<N>-<tên>/curriculum/lesson_<NNN>_<tên>/note.md
cùng quiz.md, homework.md, slides.md. Giữ đúng front matter mà Web/parse_curriculum.py đang đọc —
đổi khoá là làm hỏng trang web.

BƯỚC 6 — Index corpus, audit corpus, cổng bản quyền, cổng riêng tư, và ba cổng kiểm duyệt nội dung
AI (code, văn bản, phương tiện). Số liệu in ra phải từ chạy thật; chưa chạy được thì ghi là chưa
chạy được.

BƯỚC 7 — DỪNG CHO TÔI CHỐT NỘI DUNG. Trình ra: file nào đã viết lại, objective nào đã viết, nguồn
nào đã dùng, bài nào đã soạn, cổng nào đã qua và cổng nào đang chờ. Ghi quyết định vào approval
ledger. Đừng build web ở bước này.

BƯỚC 8 — TÔI CHỐT thì đóng gói bằng content-package-technical-series-repository, rồi HƯỚNG DẪN TÔI
BUILD WEB: nói rõ lệnh nào sinh ra file gì và chạy theo thứ tự nào; nếu parse_curriculum.py báo
lỗi front matter thì chỉ ra bài nào sai khoá nào. Tôi tự chạy — đừng tự deploy và đừng bao giờ nói
là đã deploy.

TÔI KHÔNG CHỐT thì hỏi ngược tôi từng điểm: chỗ nào sai, sai vì nội dung hay vì văn phong, sửa ở
tầng role / module / hay buổi — rồi mới sửa đúng chỗ đó. Đừng viết lại cả bài khi tôi chỉ chê một
đoạn.

DATASET: tôi sẽ tự đưa dữ liệu khi cần. Bạn chỉ đề xuất ý tưởng dataset và nói rõ cần dữ liệu hình
dạng gì; đừng tự sinh dataset rồi coi như đã có.
```

## Build web — bước 8

Chạy theo thứ tự này. Mỗi lệnh phụ thuộc đầu ra của lệnh trước.

```bash
make status      # đã soạn bao nhiêu bài trên tổng số
make material    # dựng đầu ra mọi bài đã soạn (bỏ qua bài trang_thai: chua-viet)
make web         # dựng trang tra cứu   -> Web/dist/index.html + data.json
make preview     # xem thử tại chỗ, mô phỏng URL sạch của Vercel
make deploy      # đẩy lên Vercel
```

`make web` đọc hai lớp nội dung tách rời: **đặc tả bài** lấy từ `roadmap.md` nên có sẵn cho cả 272
bài, và **giáo án chi tiết** lấy từ `note.md` của từng bài nên dựng dần. Bài chưa có giáo án vẫn
mở được và vẫn hiện nguyên đặc tả — người học không gặp trang trống, nên bạn deploy được từ sớm.

Nếu `make web` báo lỗi khi đọc front matter, bài đó sai khoá YAML. Xem bài nào:

```bash
python3 Web/parse_curriculum.py 2>&1 | head -20
```

Deploy nháp trước khi đẩy bản chính:

```bash
make deploy-preview   # URL tạm, không động vào bản đang chạy
```

## Nếu phiên đứt giữa chừng

```bash
data-agent resume            # phiên nào đang dở
data-agent resume --here --go
```

Làm tiếp khôi phục trí nhớ của model về công việc, không phải đoạn log trên màn hình.
