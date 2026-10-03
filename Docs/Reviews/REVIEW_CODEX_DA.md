# RÀ SOÁT PHẢN BIỆN ROADMAP DATA ANALYST

Ngày kiểm: 2026-09-25  
Commit được kiểm: `41a0a60`  
Phạm vi: `material/data-analyst/roadmap/roadmap.md`, 11 roadmap module và 85 cây bài trong `material/data-analyst/curriculum/`.  
Đối chiếu đọc-only: workbook gốc trong `/home/kina2711/PROJECT/data-analyst/roadmap/`, `material/data-analyst/ref/`, bộ dữ liệu dùng chung và generator. Không sửa các nguồn này.

`make test`: **PASS toàn bộ**. Audit độc lập dùng cùng script `/tmp/audit_recheck_curricula.py` (SHA-256 `410c84b415ec69639e6888fdb369d52ba9ee2c363001d0433863fedfe329cb5f`), kết quả `/tmp/audit_recheck_curricula.json` (SHA-256 `0c4c41b8167869b52a55d0813ed193a615f433d1741ed153acbf5fd1a61558d6`).

---

# Phần 1 — Lỗi phải sửa

## 1. Hợp đồng DS1 yêu cầu 8 bảng/42.000 dòng nhưng artefact chỉ có 6 bảng/41.861 dòng

**Mức nghiêm trọng: CHẶN — đáp án nghiệm thu không thể đạt bằng dữ liệu được cấp.**

Roadmap mô tả `DS1 · SalesDB — 8 bảng chuẩn hoá · 42.000 dòng` tại `material/data-analyst/roadmap/roadmap.md:2351`. Lesson 17 yêu cầu học viên xác nhận đúng số bảng/số dòng (`:870-874`), và lesson 29 tiếp tục yêu cầu tái dựng tám bảng.

Nguồn dữ liệu thực ghi **41.861 dòng** và chỉ liệt kê sáu bảng tại `material/_shared/datasets/README.md:8,19-22`; DDL PostgreSQL cũng chỉ có sáu `CREATE TABLE`.

**Bằng chứng tái hiện.**

```bash
rg -n '^CREATE TABLE' material/_shared/datasets/ddl/ds1_postgres.sql
rg -n 'DS1|41.861|ChiNhanh.*KhachHang' material/_shared/datasets/README.md
rg -n '8 bảng|42.000|số bảng và số dòng' material/data-analyst/roadmap/roadmap.md
```

**Đề xuất sửa.** Chọn dữ liệu hay roadmap làm chuẩn, rồi đồng bộ số bảng, số dòng, đáp án lesson 17/29 và fixture test.

## 2. Hợp đồng DS4 trộn hai tệp thành một phương trình sai

**Mức nghiêm trọng: CHẶN — phép đối soát công bố không đúng với bất kỳ tệp nào.**

Roadmap gọi DS4 là `orders.csv`, 50.000 dòng, 15 bản ghi lỗi tại `material/data-analyst/roadmap/roadmap.md:2354`; các bài 36–37 dùng phép đối soát 49.985 + 15 = 50.000.

Artefact thực tế:

- `orders.csv`: 50.000 dòng, chứa bốn **bẫy định dạng**, không phải 15 bản ghi bị reject (`material/_shared/datasets/README.md:55-64`).
- `orders_dirty.csv`: 50.005 dòng; 20 lỗi ép kiểu, 49.985 qua ép kiểu, thêm 5 mã trùng và 3 tên thiếu (`:66-83`). Phép kiểm chuẩn là **49.985 + 20 = 50.005**.
- Catalog dùng chung còn định nghĩa DS4 là “Dữ liệu của bạn”, không phải `orders.csv` (`:11`), nên mã DS4 cũng xung đột.

**Bằng chứng tái hiện.**

```bash
python3 material/_shared/datasets/tests/verify_orders_dirty.py
rg -n '49\.985|50\.005|DS4' material/_shared/datasets/README.md \
  material/data-analyst/roadmap/roadmap.md
```

**Đề xuất sửa.** Tách tên/mã của `orders.csv` và `orders_dirty.csv`; dùng identity do verifier sinh, không chép tay.

## 3. Roadmap hứa DS3 5 triệu event nhưng lệnh chuẩn chỉ sinh 2 triệu

**Mức nghiêm trọng: NẶNG.**

Roadmap ghi DS3 có 5 triệu event tại `material/data-analyst/roadmap/roadmap.md:2353` và dùng con số đó ở M5/M7. Generator đặt mặc định 2.000.000 tại `material/_shared/datasets/generators/ds3_appevents.py:4,9`; `make data` gọi script không truyền `--rows` tại `Makefile:38-42`. README artefact cũng ghi 2.000.000 tại `material/_shared/datasets/README.md:10,95,132`.

**Bằng chứng tái hiện.**

```bash
rg -n '5 triệu|5\.000\.000' material/data-analyst/roadmap/roadmap.md
rg -n 'default=2_000_000|ds3_appevents.py' \
  material/_shared/datasets/generators/ds3_appevents.py Makefile
```

**Đề xuất sửa.** Công bố 2 triệu hoặc truyền `--rows 5000000` trong lệnh build chính thức và kiểm đúng row count.

## 4. 75/85 note chứa “Đặc tả từ roadmap” đã cũ hoặc mất trường

**Mức nghiêm trọng: CHẶN — người học/web có thể nhận hợp đồng khác roadmap được duyệt.**

So sánh từng chữ chín trường của 85 bài cho kết quả chỉ **10 bài khớp**, **75 bài lệch**. Các bài khớp: 5, 16, 30, 37, 45, 54, 63, 68, 76, 82. Mọi note lệch đều thiếu `Đánh giá`; lessons 84–85 mất gần toàn bộ đặc tả.

Phân bố lệch: M1 4, M2 10, M3 13, M4 6, M5 7, M6 8, M7 8, M8 4, M9 7, M10 5, M11 3.

Ví dụ lesson 1, note tại `material/data-analyst/curriculum/module_1-Introduction to the Data Analyst Role/curriculum/lesson_001_What a Data Analyst actually does all day/note.md:19-33` vẫn dùng Learn/Outcome/Lab/Done-when cũ và không có `Đánh giá`, trong khi roadmap chuẩn nằm ở `material/data-analyst/roadmap/roadmap.md:527-543`. Đây là bài duy nhất có `trang_thai: xong`; sai lệch vì thế đã đi vào bài có nội dung thật, không chỉ scaffold.

Lessons 84–85: các note chỉ còn một phần nhỏ ở dòng 22 trở đi, trong khi roadmap tổng có đủ đặc tả tại `material/data-analyst/roadmap/roadmap.md:2257-2314`.

**Bằng chứng tái hiện.**

```bash
python3 /tmp/audit_recheck_curricula.py
python3 - <<'PY'
import json
p=json.load(open('/tmp/audit_recheck_curricula.json'))['data-analyst']['material']
print(len(p['spec_mismatches']))
print([x[0] for x in p['spec_mismatches']])
PY
```

**Đề xuất sửa.** Sửa generator/serialization trước, rồi sinh lại có kiểm soát; không ghi đè phần nội dung đã soạn của lesson 1. Thêm test exact-match như DE.

## 5. Bốn bài KT vi phạm chính quy ước “chín trường” của roadmap

**Mức nghiêm trọng: NẶNG — schema đặc tả không nhất quán.**

Mục 11 tuyên bố mọi bài có đúng chín trường, gồm `Lab`, tại `material/data-analyst/roadmap/roadmap.md:421-435`. Lessons 16, 30, 54 và 85 không có `Lab`; ba bài dùng `Đề gồm`, bài 85 dùng `Hình thức` (`:827-846,1110-1129,1614-1633,2285-2314`).

**Bằng chứng tái hiện.**

```bash
python3 /tmp/audit_recheck_curricula.py
# Kết quả data-analyst.structure.field_errors: lessons 16,30,54,85; missing Lab
```

**Đề xuất sửa.** Giữ `Lab` là field máy đọc, đưa `Đề gồm/Hình thức` vào nội dung của field đó hoặc sửa schema công khai và mọi consumer.

## 6. Tổng tự học bị cộng dư 8 giờ

**Mức nghiêm trọng: NẶNG — sai tải lượng chương trình.**

Header ghi 170 giờ tự học và 340 giờ tổng tại `material/data-analyst/roadmap/roadmap.md:13,20`; phụ lục còn nói mỗi bài có hai giờ tự học tại `:2551-2554`. Nhưng bốn bài KT 16, 30, 54, 85 đều ghi “Không có bài tự học” (`:844,1127,1631,2312`). Theo đặc tả bài, tổng đúng là **81 × 2 = 162 giờ**, tổng chương trình **332 giờ**.

**Bằng chứng tái hiện.**

```bash
rg -n '^\*\*Self-study \(2 giờ\)\.\*\* Không có bài tự học' \
  material/data-analyst/roadmap/roadmap.md
python3 -c 'print((85-4)*2, 170+(85-4)*2)'
```

**Đề xuất sửa.** Chọn cách tính công bố; nếu KT thật sự không tự học, sửa header và phụ lục.

## 7. Đồ thị phụ thuộc, bảng “phụ thuộc cứng” và prerequisite bài không mô tả cùng một DAG

**Mức nghiêm trọng: NẶNG — người lập lịch nhận các điều kiện khác nhau.**

- ASCII graph có `M7 → M8` (`material/data-analyst/roadmap/roadmap.md:385-391`) nhưng chính mục 10.2 nói M8 chỉ cần M5, không cần M7 (`:412`); lesson 64 cũng chỉ yêu cầu M5 (`:1838`).
- Lesson 46 yêu cầu M2 và M3 (`:1463`), nhưng bảng chỉ liệt kê M2 → M6 (`:400`), thiếu M3 → M6.
- M7 yêu cầu M3 và M5 (`:1643-1651`), bảng chỉ có M3 → M7 (`:401`), thiếu M5 → M7.
- Lesson đầu M5 yêu cầu M4 (`:1296`); bảng “phụ thuộc cứng” bỏ M4 → M5 dù ASCII có cạnh đó.
- ASCII vẽ M9 → M10, còn M10 và bảng chỉ yêu cầu M7 (`:2108-2116,404`).

**Bằng chứng tái hiện.**

```bash
sed -n '381,417p' material/data-analyst/roadmap/roadmap.md
rg -n '^\*\*Prerequisites\.\*\* Module (5|6|7|8|10):' \
  material/data-analyst/roadmap/roadmap.md
```

**Đề xuất sửa.** Chọn một DAG chuẩn machine-readable và sinh ASCII, bảng, prerequisite từ đó.

## 8. Roadmap trỏ tới manifest nguồn không tồn tại; index hiện có trỏ tới file/path không tồn tại

**Mức nghiêm trọng: NẶNG — mất traceability nguồn bài.**

Roadmap khẳng định danh sách nguồn từng bài nằm tại `material/data-analyst/ref/SOURCES.md` (`material/data-analyst/roadmap/roadmap.md:2492-2493`), nhưng file không tồn tại. Thư mục ref chỉ có `README.md` và `roadmap-v1-goc.md`. README lại liệt kê ba PDF và các path `curriculum/lessons/...` không tồn tại (`material/data-analyst/ref/README.md:3-11`). Các ref folder cấp module được để trống có chủ ý.

**Bằng chứng tái hiện.**

```bash
find material/data-analyst/ref -maxdepth 2 -type f -printf '%p\n' | sort
test -f material/data-analyst/ref/SOURCES.md; echo $?
```

**Đề xuất sửa.** Tạo manifest thật có `lesson -> source -> locator/version`, hoặc bỏ lời khẳng định và ghi rõ chưa có nguồn.

## 9. Ba lab bắt buộc đã được roadmap thừa nhận là chưa có dữ liệu

**Mức nghiêm trọng: NẶNG — lesson 60, 62, 68 chưa chạy được theo mô tả.**

Roadmap tự ghi tại `material/data-analyst/roadmap/roadmap.md:2359-2362`: thiếu dữ liệu đa kênh có touchpoints cho attribution, chuỗi ít nhất 36 tháng phủ hai Tết, và tập can thiệp/đối chứng cho difference-in-differences.

**Bằng chứng tái hiện.**

```bash
sed -n '2359,2362p' material/data-analyst/roadmap/roadmap.md
```

**Đề xuất sửa.** Chặn trạng thái “sẵn sàng dạy” của ba bài cho tới khi dataset, generator và đáp án kiểm chứng tồn tại. Việc roadmap công khai thiếu hụt này là điểm làm tốt về tính trung thực.

## 10. Hai kết luận về thị trường viện dẫn một “khảo sát” không tồn tại trong tài liệu

**Mức nghiêm trọng: VỪA.**

Roadmap nói Power BI là bắt buộc trong các tin tuyển dụng khảo sát tại §5.4 (`material/data-analyst/roadmap/roadmap.md:136`) và SQL xuất hiện ở mọi tin khảo sát (`:861`). Nhưng §5.4 chỉ đưa một JD mẫu, không có công ty, URL, ngày thu thập hay bảng mẫu. Các mô tả loại công ty/vị trí tại `:238-247` cũng không có nguồn và năm.

**Bằng chứng tái hiện.**

```bash
rg -n 'khảo sát ở mục 5\.4|mọi tin tuyển dụng|^### 5\.4' \
  material/data-analyst/roadmap/roadmap.md
sed -n '238,287p' material/data-analyst/roadmap/roadmap.md
```

**Đề xuất sửa.** Lưu mẫu khảo sát với tiêu chí chọn, ngày, URL và bảng đếm; nếu không có, bỏ lượng từ “mọi” và không dùng nó để biện minh thứ tự học.

## 11. Hai tài nguyên trả phí không được ghi rõ chi phí

**Mức nghiêm trọng: NHẸ.**

Danh sách tài nguyên tại `material/data-analyst/roadmap/roadmap.md:2495-2501` ghi Khan Academy là miễn phí nhưng không nói Google Professional Certificate thu phí theo thuê bao và kỳ thi PL-300 có lệ phí theo vùng. Link chính thức còn hoạt động khi kiểm ngày 2026-09-25; không tìm thấy link chia sẻ lậu.

**Đề xuất sửa.** Gắn nhãn “trả phí/giá phụ thuộc khu vực; kiểm trang chính thức” và ngày kiểm.

---

# Phần 2 — Nội dung bị mất so với nguồn gốc

Không thể lập bảng Exit Criteria/Critical failures như DE vì nguồn gốc DA **không phải hợp đồng học tập**. Workbook `/home/kina2711/PROJECT/data-analyst/roadmap/ROAD MAP 66 NGÀY TRỞ THÀNH DATA ANALYST.xlsx` có 1 sheet, 69 hàng, là danh sách chủ đề 66 ngày; không có Outcomes, Labs, Exit Criteria, Critical failures hay failure matrix.

Hai bản workbook ở `.roadmap/` và `roadmap/` có hash file khác nhau nhưng 69 hàng ô giải mã giống nhau. Nội dung gốc có các dải chủ đề sau mà roadmap DA hiện tại không ánh xạ truy vết:

| Nhóm trong workbook gốc | Hiện trạng roadmap mới | Kết luận có thể đưa ra |
|---|---|---|
| Cấu trúc dữ liệu, DBMS internals, NoSQL/MongoDB | Không còn hoặc giảm mạnh | Chưa thể gọi là “mất”: có thể là thu hẹp đúng vai DA |
| Tableau | Không dạy, roadmap công khai lý do tại `:131-139` | Khác có chủ ý; lý do “chuyển trong vài ngày/9 bài không thêm năng lực” chưa có bằng chứng |
| Python/OOP, NumPy | Python thu hẹp cho automation/analysis | Khác có chủ ý theo role boundary |
| Thống kê/hồi quy/dự án | Còn và được tái cấu trúc | Có phủ chủ đề, nhưng không có ID nguồn để chứng minh completeness từng mục |

`material/data-analyst/ref/roadmap-v1-goc.md` là lộ trình “Full-stack Data Professional” 72 buổi, gồm cả DE/big-data; nó cũng không phải hợp đồng DA-only đã duyệt. Vì vậy báo cáo không gắn nhãn “bịa thêm” hay “mất” cho các chênh lệch nội dung khi không có chuẩn có thẩm quyền.

---

# Phần 3 — Không nhất quán nhưng chưa chắc sai

1. **Done-when “chọn đúng”.** Lessons 38, 42, 68 dùng đáp án/rubric ngầm; có thể đo được nếu answer key tồn tại, nhưng answer key không nằm trong phạm vi repo. Lesson 8 dùng “công thức đạt rà soát chéo” (`material/data-analyst/roadmap/roadmap.md:692`) mà không có rubric, nên yếu hơn ba trường hợp còn lại.
2. **So sánh roadmap.sh.** Roadmap ghi snapshot ngày 2026-09-17 và 11 bước (`:112-129`). Trang hiện tại dùng nội dung động; kiểm web ngày 2026-09-25 không tái tạo đáng tin toàn bộ danh sách trong ảnh/graph, nên chưa kết luận snapshot sai.
3. **DS2 “có tháng khuyết giao dịch”.** Roadmap hứa đặc tính này tại `:2352`; generator/README không công bố phép kiểm tương ứng. Chưa chạy sinh toàn bộ DS2 nên chưa kết luận dữ liệu chắc chắn không có tháng khuyết.
4. **Văn phong AI.** Chỉ tìm thấy hai cấu trúc gần “không phải X mà là Y”; 48 em-dash chủ yếu nằm trong bảng/định dạng. Không có bằng chứng tái hiện đủ để kết luận roadmap được viết bằng AI hoặc văn phong vi phạm có hệ thống.

---

# Phần 4 — Loại lỗi mà `make test` không phủ

`material/_shared/tools/check_curriculum.py:102-111` chỉ đếm một tập field cũ/field thay thế và coi bài hợp lệ khi có ít nhất hai field; vì vậy bốn KT thiếu `Lab` vẫn pass. `:113-145` chủ yếu kiểm file tồn tại, không so exact note với roadmap.

Các khoảng trống cần test bổ sung:

1. **Schema chính xác chín trường.** Fail nếu thiếu/thừa/đổi tên field; không dùng `Đề gồm`, `Hình thức` làm alias âm thầm.
2. **Đồng bộ generator.** So từng chữ roadmap tổng ↔ roadmap module ↔ note; hiện test bỏ lọt 75/85 note lệch.
3. **Hợp đồng dataset.** Chạy generator/verifier trong fixture nhỏ và kiểm row/table/error counts cùng công thức đối soát.
4. **DAG thống nhất.** So graph machine-readable với bảng edge và prerequisite ở bài đầu module.
5. **Tổng giờ theo nội dung bài.** Loại bài “Không có bài tự học” khỏi phép cộng.
6. **Source manifest.** Fail nếu file được viện dẫn không tồn tại hoặc source locator không resolve.
7. **Claim thị trường.** Lint câu định lượng/tuyệt đối yêu cầu năm, nguồn và sample method.
8. **Paid-link disclosure và link health.** Kiểm định kỳ, phân biệt miễn phí/trả phí; không chỉ kiểm URL có cú pháp.

---

# Phần 5 — Những gì đã kiểm và ĐẠT

- 85 lesson liên tục 1–85; 11 module liên tục 1–11; range liền, không trùng/hở; module map khớp số bài và 170 giờ lớp.
- Đúng một nhãn dạng bài cho mọi bài: 18 LT, 59 TH, 4 DA, 4 KT. Bốn KT ở lessons 16, 30, 54, 85 và đúng cuối các phase/cổng đã công bố.
- 66 tham chiếu lesson trong văn xuôi đều nằm trong 1–85; 37 tham chiếu module đều trong 1–11; mọi prerequisite `Lesson N` đều trỏ lùi.
- Mẫu tất định 40 tham chiếu lesson được đọc ngữ cảnh; không tìm thấy renumber làm tham chiếu trỏ sai chủ đề.
- 11 module dir, 85 lesson dir; mỗi bài đủ note/quiz/homework/slides và đúng một drawio. Tổng 96 drawio gồm cấp module đều parse XML thành công.
- Frontmatter `module`, `lesson`, `tieu_de`, `dang_bai` của 85 note khớp roadmap tổng.
- 11 roadmap module liệt kê đúng tập bài và đặc tả khớp roadmap tổng.
- 85 Outcome bắt đầu bằng động từ quan sát được; không tìm thấy “hiểu/biết/nắm được” làm động từ objective.
- 19/20 URL được mở hoặc redirect bình thường. URL VietnamWorks không trả ổn định từ môi trường kiểm nhưng tìm kiếm xác nhận domain thương hiệu; vì vậy ghi **chưa xác minh**, không gắn nhãn link chết. Không tìm thấy link piracy.
- Hai số 64%/70% về tuyển dụng được dẫn tới bài ITviec có năm và trang chính thức còn truy cập được. Phân bổ 40/20/20/15/5 tự ghi là ước lượng không đại diện; đây là cách trình bày trung thực.
- Roadmap tự công khai ba dataset còn thiếu (`:2359-2362`) và các phần chưa hoàn tất; điểm này nên giữ.

## Giới hạn bắt buộc

- Nguồn DA hiện có không cung cấp hợp đồng chuẩn như DE, nên không thể kết luận completeness của Outcomes/Labs/Exit Criteria/Critical failures hay nội dung “bịa thêm”. Cần một hợp đồng DA được owner phê duyệt, có ID từng requirement.
- Không chạy `make data` vì nó sinh hàng triệu dòng và không cần để chứng minh ba mismatch mặc định; các số thực tế được lấy từ generator, verifier và README hiện hành. DS2 missing-month vì thế là **chưa kiểm**.
- Chỉ so exact phần “Đặc tả từ roadmap” của toàn bộ note; không đọc sâu nội dung giảng dạy của 84 scaffold. Lesson 1 có nội dung thật được đọc đại diện.
- Kiểm link là snapshot ngày 2026-09-25; không bảo đảm trạng thái tương lai. Nội dung động của roadmap.sh và VietnamWorks chưa xác minh đầy đủ.
- Không có answer key, rubric runtime, bài nộp học viên hay kết quả dạy thử; chưa thể xác nhận Done-when thực thi được trong lớp.
- Không có owner approval. Đây là báo cáo audit độc lập, không phải quyết định phát hành.

## Dấu vết task contract

- Skill task đã dùng: `academy-audit-curriculum-quality`.
- Bằng chứng: roadmap/material/dataset/generator/source workbook và các lệnh tái hiện trong từng phát hiện.
- Validation: `make test` cộng audit độc lập và mẫu nghĩa 40 reference.
- Residual risk/owner kế tiếp: owner DA cần chốt chuẩn dataset, chọn DAG chuẩn, xác nhận workbook nào là authority và cung cấp hợp đồng requirement có ID trước khi sửa generator/scaffold.
