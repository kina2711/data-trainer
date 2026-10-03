# Prompt kiểm tra chéo tại Codex

Mục đích: Codex **soi độc lập**, không dựng lại. Một bộ kiểm mà tự sửa thì thôi là bộ kiểm.

Mở Codex trong thư mục `data-trainer` rồi dán khối dưới.

---

```
Bạn đang kiểm tra chéo một dự án giáo trình dữ liệu. Vai của bạn là NGƯỜI SOI ĐỘC LẬP, không
phải người xây. Tuyệt đối không sửa file nào. Chỉ báo cáo.

BỐI CẢNH ĐÃ ĐO ĐƯỢC (bạn hãy tự kiểm lại, đừng tin số này):
- 3 chương trình: Data Analyst, Data Engineer, Analytics Engineer
- 525 thư mục bài, mỗi thư mục có note.md, quiz.md, homework.md, slides.md
- 524/525 note.md ở trạng thái `trang_thai: chua-viet` — mới là khung, chưa có nội dung
- 1 bài đã soạn: material/data-analyst/.../lesson_001_What a Data Analyst actually does all day/
- 40 roadmap cấp module, 3 roadmap cấp chương trình
- material/**/ref/ chứa ~1861 tệp nguồn (1443 PDF)
- .data-2026/roadmap-approved.json khoá bản roadmap đã được duyệt

Chạy theo đúng thứ tự dưới. Cái rẻ chạy trước, cái tốn token chạy sau.

═══ PHẦN A — KIỂM CƠ HỌC (chạy lệnh, không cần đọc hiểu) ═══

A1. Đếm lại toàn bộ số liệu ở trên. Số nào tôi ghi sai thì nói rõ đúng là bao nhiêu.

A2. Front matter. Mọi note.md phải có đủ và đúng kiểu: chuong_trinh, module, lesson, tieu_de,
    dang_bai, thoi_luong_phut, trang_thai. Web/parse_curriculum.py đọc đúng các khoá này — sai
    một khoá là hỏng trang web. Chạy `python3 Web/parse_curriculum.py` và báo mọi lỗi.
    Liệt kê file sai khoá nào, sai thế nào.

A3. Toàn vẹn cấu trúc. Thư mục bài nào thiếu một trong bốn tệp? Số thứ tự bài có bị trùng hoặc
    nhảy cóc trong một module không? Tên thư mục có khớp `tieu_de` trong front matter không?

A4. Đối chiếu roadmap với thực tế. Mỗi roadmap chương trình khai số bài trong front matter
    (`so_bai`). Con số đó có khớp số thư mục bài thật không? Roadmap module khai bài nào thì
    thư mục đó có tồn tại không, và ngược lại — có thư mục bài nào không nằm trong roadmap nào?

A5. Khoá roadmap. Đọc .data-2026/roadmap-approved.json, tính sha256 của file roadmap nó trỏ tới,
    so với artifact_sha256. Khớp hay lệch? Lệch nghĩa là roadmap đã bị sửa sau khi duyệt.

═══ PHẦN B — KIỂM ROADMAP (đây là phần có nội dung thật, soi kỹ nhất) ═══

B1. Với từng roadmap chương trình và 40 roadmap module, kiểm bốn thứ cho MỖI bài:
    - Có Outcome (objective) không, và động từ có quan sát được không? "Hiểu", "biết",
      "nắm được" là không quan sát được — không đánh giá được thì không hứa được gì.
    - Có Done when (tiêu chí xong) không?
    - Có Prerequisites không?
    - Thời lượng có nhất quán với roadmap chương trình không?
    Báo dạng bảng: chương trình | tổng bài | thiếu objective | thiếu done-when | thiếu prereq |
    động từ không quan sát được. Kèm danh sách tên bài cụ thể.

B2. Đồ thị phụ thuộc. Gom toàn bộ Prerequisites thành một đồ thị. Có chu trình không? Có bài nào
    phụ thuộc vào bài nằm SAU nó trong thứ tự dạy không? Có bài nào bị mồ côi — không ai cần nó
    và nó không cần ai?

B3. Trùng lặp giữa ba chương trình. DA, DE, AE chắc chắn có phần giao nhau (SQL, mô hình dữ liệu).
    Chỉ ra chỗ giao. Với mỗi chỗ: là phân tầng có chủ ý (cùng chủ đề, khác độ sâu, khác mục đích
    nghề) hay là chép qua lại? Trích cả hai đoạn để tôi tự so.

B4. Mâu thuẫn. Có chỗ nào hai roadmap nói ngược nhau về cùng một khái niệm, công cụ, hay thứ tự
    học không? Trích nguyên văn cả hai phía.

B5. Khẳng định không dẫn nguồn. Mọi câu nói về thị trường, lương, thứ công ty đang dùng, tỉ lệ
    phần trăm — có kèm năm và nguồn không? Liệt kê câu nào không có.

B6. Đối chiếu ngoài. So cấu trúc với roadmap.sh (data-analyst / backend), EDISON Data Science
    Framework, SFIA. Chương trình này thiếu năng lực nào mà các khung kia coi là cốt lõi? Và
    chỗ nào nó cố tình khác — khác có lý do chính đáng hay là bỏ sót?

═══ PHẦN C — KIỂM BÀI MẪU (chỉ 1 bài, nhưng quan trọng nhất) ═══

lesson_001 là bài duy nhất đã soạn. 524 bài còn lại sẽ được nhân theo khuôn của nó, nên một
khiếm khuyết ở đây sẽ nhân lên 524 lần.

C1. Đọc kỹ note.md của lesson_001. Nội dung có thật sự đạt Outcome mà roadmap hứa cho bài đó
    không? Trích câu Outcome, rồi chỉ ra chỗ nào trong bài đáp ứng, chỗ nào không.

C2. Chín mục La Mã (I–IX) có mục nào rỗng hoặc chỉ có tiêu đề không?

C3. Mọi dữ kiện, con số, tên riêng trong bài — có dẫn được về nguồn trong ref/ không? Cái nào
    không dẫn được thì nêu ra. Đừng đọc hết PDF; chỉ cần kiểm bài có CHỈ RA nguồn hay không.

C4. Bài này có đủ để một người dạy được 120 phút mà không cần hỏi thêm không? Thiếu gì?

C5. Khuôn này có nhân được cho 524 bài còn lại không? Chỗ nào trong khuôn sẽ gây khó khi áp cho
    bài dạng TH (thực hành) hay KT (kiểm tra) thay vì LT (lý thuyết)?

═══ PHẦN D — KIỂM KHO NGUỒN ═══

D1. ref/ có ~1443 PDF. ĐỪNG đọc nội dung chúng. Chỉ kiểm: cách tổ chức thư mục có cho phép một
    người tìm được nguồn cho một bài cụ thể không? Có manifest hay index nào không?

D2. Có nguồn nào nằm trong ref/ mà không roadmap hay bài nào trỏ tới không — tức là tải về rồi
    bỏ đó?

D3. Ngược lại: roadmap hay bài có trỏ tới nguồn nào không tồn tại trong ref/ không?

═══ CÁCH BÁO CÁO ═══

Ghi ra file KET-QUA-KIEM-TRA.md ở thư mục gốc, theo thứ tự:

1. Bảng số liệu bạn tự đếm, đặt cạnh số tôi đưa ở đầu prompt. Lệch chỗ nào nói chỗ đó.
2. Danh sách phát hiện, xếp theo mức: CHẶN (làm hỏng web build hoặc sai kiến thức) → NẶNG
   (ảnh hưởng chất lượng dạy) → NHẸ (nhất quán, hình thức).
3. Mỗi phát hiện: file + dòng, trích nguyên văn, vì sao là vấn đề, đề xuất sửa. KHÔNG tự sửa.
4. Phần "tôi không kiểm được" — nói rõ cái gì bạn không đủ dữ kiện để kết luận, và cần gì để
   kết luận được. Phần này bắt buộc có; một báo cáo không có giới hạn là một báo cáo chưa đủ
   trung thực.

QUY TẮC:
- Không sửa file nào. Không chạy make. Không deploy.
- Không đoán nội dung sách từ tên sách.
- Số nào bạn in ra phải từ lệnh bạn vừa chạy. Chưa chạy được thì ghi là chưa chạy được.
- Chỗ nào bạn thấy làm tốt thì cũng nói — tôi cần biết chỗ nào đang đúng để đừng sửa nhầm.
```

---

## Ghi chú

Codex có thể không có sẵn các script kiểm của bộ skill. Nếu có, dùng luôn:

```bash
python3 <đường-dẫn-skills>/data-academy-and-curriculum/scripts/check_roadmap_rigor.py \
  material/*/roadmap/roadmap.md material/*/curriculum/*/roadmap/roadmap.md

python3 <đường-dẫn-skills>/data-department-orchestrator/scripts/validate_approval_record.py \
  .data-2026/roadmap-approved.json --artifact-root . --require-approved
```

Không có thì Phần A và B trong prompt đã mô tả đủ để Codex tự viết lệnh kiểm tương đương.
