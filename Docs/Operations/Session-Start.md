# Bắt đầu một phiên làm việc

## Lần đầu tiên — chuẩn bị một lần rồi thôi

**1. Cài humanizer**

```bash
claude plugin install humanizer@humanizer
```

**2. Cấp quyền đọc thư mục plugin.** Bộ skill cài ngoài dự án, nên mọi tệp nó trỏ tới là lượt đọc
ngoài working directory và Claude sẽ hỏi quyền từng lần. Mở `~/.claude/settings.json`, thêm:

```json
{ "permissions": { "additionalDirectories": ["~/.claude/plugins/cache"] } }
```

**3. Kiểm tra**

```bash
cd /home/kina2711/PROJECT/data-trainer
data-agent doctor
```

Năm dòng phải xanh hết. Dòng `suite đọc được` cho biết bạn đang chạy bản nào.

---

## Mỗi lần bắt đầu phiên

### Bước 1 — Vào đúng thư mục

```bash
cd /home/kina2711/PROJECT/data-trainer
```

Sai thư mục là hỏng cả phiên: prompt trỏ tới `material/**` bằng đường dẫn tương đối.

### Bước 2 — Xem có phiên nào đang dở không

```bash
data-agent resume
```

Có phiên của chính thư mục này thì nối lại thay vì mở phiên mới:

```bash
data-agent resume --here --go
```

Làm tiếp khôi phục trí nhớ của model về công việc, **không phải** đoạn log trên màn hình.

### Bước 3 — Hỏi roadmap đã chốt chưa

```bash
P=~/.claude/plugins/cache/data-department/data-department-agent-skills
python3 $P/*/skills/data-department-orchestrator/scripts/validate_approval_record.py \
  .data-2026/roadmap-approved.json --artifact-root . --require-approved
```

| Kết quả | Nghĩa là | Chạy chặng nào |
|---|---|---|
| `PASS` | Roadmap đã chốt và chưa ai đụng vào | 3 hoặc 4 |
| `no artifact ... matches artifact_sha256` | Roadmap bị sửa sau khi chốt | Dừng, quyết định chốt lại hay hoàn nguyên |
| Không có tệp | Chưa chốt bao giờ | 1 |

### Bước 4 — Biết mình đang đứng ở đâu

```bash
# roadmap còn thiếu gì
python3 $P/*/skills/data-academy-and-curriculum/scripts/check_roadmap_rigor.py \
  material/*/roadmap/roadmap.md

# đã soạn được bao nhiêu bài
make status
```

### Bước 5 — Mở phiên và dán prompt

```bash
claude
```

Mở [PROMPT-DATA-2026.md](PROMPT-DATA-2026.md), chọn đúng ô: phạm vi lớn hay bé, chặng mấy. Sửa
dòng `Chương trình` và `Phạm vi lần này` rồi dán cả khối.

Hoặc mở app Data Agent, chọn **Data 2026**, điền 7 ô — app tự ghép prompt.

### Bước 6 — Chạy, và biết nó sẽ dừng ở đâu

| Chặng | Dừng ở |
|---|---|
| 1 | Sau khi siết roadmap tổng. Bạn đọc, chốt hoặc bảo sửa |
| 2 | Sau khi có roadmap từng module |
| 3 | Sau khi đưa danh sách nguồn. **Bạn tải, đặt vào `ref/`, quay lại nói "xong"** |
| 4 | Sau khi soạn bài. Bạn chốt nội dung |

Nó không tự đi tiếp sang chặng sau. Muốn tiếp thì mở phiên mới với prompt chặng kế.

### Bước 7 — Chốt roadmap, một lần duy nhất

Sau chặng 1 và 2, khi bạn ưng roadmap, bảo nó sinh tệp chốt:

```
Tôi chốt roadmap này. Sinh .data-2026/roadmap-approved.json theo mẫu approval-record.json:
artifact_sha256 của chính roadmap vừa chốt, approver là kina2711, decision approved,
expires_at cách một năm.
```

Từ lúc đó mọi phiên sau **tự bỏ qua chặng 1 và 2**. Muốn làm lại thì thêm vào cuối prompt:

```
TÔI YÊU CẦU LÀM LẠI ROADMAP dù đã chốt. Lý do: <lý do>.
```

---

## Thứ tự chạy lần đầu, nếu chưa có gì

```
Chặng 1 (DA)  → đọc, chốt roadmap DA
Chặng 2 (DA)  → đọc, chốt roadmap module
Chặng 3 (DA)  → nhận danh sách nguồn → tải, đặt vào ref/ → nói "xong"
Chặng 4 (DA)  → nhận bài giảng → chốt nội dung
make web      → xem thử → deploy
```

Làm hết DA rồi mới sang DE và AE. Roadmap DA 2334 dòng — nếu văn phong hoặc cách siết không hợp ý,
biết sớm ở một chương trình rẻ hơn nhiều so với biết sau ba.

## Khi phiên hết hạn mức giữa chừng

Không mất gì. Nó ghi từng bài xuống đĩa ngay khi soạn xong.

```bash
make status                    # đã tới đâu
data-agent resume --here --go  # nối lại
```

Hoặc mở phiên mới với chặng cũ, thu `Phạm vi` về đúng phần còn thiếu.

## Sau khi chốt nội dung

```bash
make status      # đã soạn bao nhiêu trên tổng số
make material    # dựng đầu ra mọi bài đã soạn
make web         # dựng trang tra cứu -> Web/dist/index.html
make preview     # xem thử tại chỗ
make deploy      # đẩy lên Vercel
```

Bài chưa có giáo án vẫn mở được và vẫn hiện nguyên đặc tả từ roadmap, nên bạn deploy được từ sớm.
