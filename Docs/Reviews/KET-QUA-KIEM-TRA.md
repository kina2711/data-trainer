# KẾT QUẢ KIỂM TRA ĐỘC LẬP GIÁO TRÌNH DỮ LIỆU

Ngày kiểm tra: 2026-09-24  
Phạm vi: trạng thái working tree tại `/home/kina2711/PROJECT/data-trainer`  
Vai trò: người soi độc lập; không sửa nội dung giáo trình, roadmap, mã web hay kho nguồn.

## Kết luận ngắn

- Không tìm thấy lỗi làm `Web/parse_curriculum.py` thất bại: lệnh chạy thành công, nhận đủ 525 bài và 1 giáo án hoàn tất.
- Cấu trúc cơ học nhìn chung rất tốt: 525/525 thư mục bài có đủ bốn tệp; front matter đúng khóa/kiểu; số bài liên tục; 40 roadmap module khớp thư mục thật; đồ thị prerequisites không có chu trình, cạnh ngược hay bài mồ côi.
- Có hai vấn đề mức **CHẶN**: sản phẩm hiện thực chỉ có hai chương trình dù tài liệu DA nói ba chương trình độc lập; và bài mẫu dạy một mô hình phân vai AE/DE sai lệch so với chính roadmap DE.
- Rủi ro lớn nhất trước khi nhân 524 bài là **hợp đồng nội dung bị trôi**: cả 85 `note.md` của DA chứa “Đặc tả từ roadmap” khác roadmap chương trình hiện tại; riêng lesson 001 đang dạy và đánh giá theo đặc tả cũ.
- Kho nguồn có đúng 1.443 PDF nhưng tổng số tệp là 1.997, không phải khoảng 1.861. Không có manifest cấp giáo trình và không có một liên kết Markdown tường minh nào từ roadmap/bài tới một tệp trong `ref/`.

---

# 1. Bảng số liệu tự đếm

| Chỉ số | Số được cung cấp | Tự đếm | Kết luận |
|---|---:|---:|---|
| Chương trình hiện hữu | 3 | **2** | Sai: chỉ có `data-analyst`, `data-engineer`; AE đang được gộp vào DE |
| Thư mục bài | 525 | **525** | Khớp: DA 85, DE 440 |
| `note.md` | 525 | **525** | Khớp |
| `quiz.md` | 525 | **525** | Khớp |
| `homework.md` | 525 | **525** | Khớp |
| `slides.md` | 525 | **525** | Khớp |
| `note.md` có `trang_thai: chua-viet` | 524/525 | **524/525** | Khớp; 1 bài `xong` |
| Bài đã soạn | 1 | **1** | Khớp: DA lesson 001 |
| Roadmap module | 40 | **40** | Khớp: DA 11, DE 29 |
| Roadmap chương trình | 3 | **2** | Sai: DA và DE |
| Tệp trong mọi `ref/` | khoảng 1.861 | **1.997** | Lệch +136 |
| PDF trong mọi `ref/` | khoảng 1.443 | **1.443** | Khớp đúng tuyệt đối |

Chi tiết loại bài theo front matter:

| Chương trình | LT | TH | DA | KT | Tổng |
|---|---:|---:|---:|---:|---:|
| Data Analyst | 18 | 59 | 4 | 4 | 85 |
| Data Engineer | 83 | 322 | 25 | 10 | 440 |

Các số trên được lấy từ lệnh vừa chạy, không suy đoán. Những lệnh chính:

```text
find material -type d -name 'lesson_*'
find material -type f \( -name note.md -o -name quiz.md -o -name homework.md -o -name slides.md \)
find material -path '*/ref/*' -type f
find material -path '*/ref/*' -type f -iname '*.pdf'
python3 Web/parse_curriculum.py
sha256sum material/data-analyst/roadmap-data-analyst.md
```

Kết quả parser:

```text
chuong trinh  2
module       40
bai         525
giao an       1 / 525
```

Mã thoát: `0`. SHA-256 của `Web/dist/data.json` trước và sau lần chạy đều là:

```text
10d20d3af852c5b086d62a17491cd42c4c0bc541c12e235c1ea7ce1b431d83eb
```

Nghĩa là parser có ghi lại tệp sinh, nhưng nội dung không đổi.

---

# 2. Danh sách phát hiện theo mức độ

## CHẶN

### C-01 — Kiến trúc sản phẩm nói “ba chương trình độc lập”, nhưng hệ thống chỉ có hai và AE bị gộp vào DE

**Bằng chứng**

- `material/data-analyst/roadmap-data-analyst.md:59-60`:

  > Data Engineer (DE) và Analytics Engineer (AE) là chương trình riêng, không phải phần mở rộng của DA.

- `material/data-engineer/roadmap-data-engineer.md:30-32`:

  > Đầu ra nghề nghiệp: Data Engineer (chính), Analytics Engineer (nhánh M12, M13, M18, M19), Platform/Data Infrastructure Engineer...
  > ...lý do của việc gộp.

- Kết quả đếm thư mục và parser đều chỉ trả về `2` chương trình.

**Vì sao là vấn đề**

Đây không chỉ là tên gọi. Roadmap DA đặt kỳ vọng ba lộ trình độc lập, trong khi roadmap DE và website triển khai mô hình hai lộ trình với AE là một nhánh. Người học không thể biết tuyên bố nào là hợp đồng sản phẩm chính thức; mọi đối chiếu DA–DE–AE cũng mất một đối tượng độc lập.

**Đề xuất sửa**

Ra một quyết định kiến trúc duy nhất: hoặc tách AE thành chương trình thứ ba có roadmap/module/bài riêng, hoặc sửa toàn bộ tuyên bố “ba chương trình độc lập” và mô tả rõ cơ chế nhánh AE trong DE. Sau đó khóa quyết định này trong ledger duyệt.

### C-02 — Bài mẫu dạy một quy tắc phân vai AE/DE sai và mâu thuẫn với roadmap DE

**Bằng chứng**

- `material/data-analyst/curriculum/module_1-Nền tảng nghề Data Analyst/curriculum/lesson_001_What a Data Analyst actually does all day/note.md:264-265`:

  > Nếu ví von: **AE viết SQL, DE viết hệ thống để SQL đó chạy, DA dùng kết quả để ra quyết định**.

- `material/data-engineer/roadmap-data-engineer.md:2425`:

  > Analytics Engineer dùng SQL để mô hình hoá, Data Engineer dùng SQL để nạp và đối soát.

**Vì sao là vấn đề**

Data Engineer cũng viết và vận hành SQL; Analytics Engineer không chỉ “viết SQL”, và hệ thống để SQL chạy không chỉ thuộc một vai duy nhất. Câu ví von tuyệt đối hóa ranh giới nghề, trái với chính roadmap DE và có thể tạo hiểu sai nền tảng ngay bài đầu tiên. Vì đây là sai kiến thức nghề nghiệp trong bài mẫu sẽ được nhân rộng, tôi xếp mức CHẶN.

**Đề xuất sửa**

Thay bằng mô tả theo trách nhiệm chính và vùng giao nhau, có ví dụ artefact của từng vai; tránh cấu trúc “vai X làm công cụ Y”. Dùng cùng một định nghĩa vai trò trong cả DA, DE và nhánh AE.

## NẶNG

### N-01 — Cả 85 đặc tả nhúng trong `note.md` của DA đã trôi khỏi roadmap hiện tại

**Bằng chứng**

So sánh tự động theo từng trường trong khối `## Đặc tả từ roadmap` cho thấy:

- 85/85 `note.md` DA có ít nhất một trường khác roadmap chương trình hiện tại.
- 450 khác biệt trường: `Prerequisites` 20, `Learn` 83, `Outcome` 77, `Lab` 79, `Pitfalls` 82, `Done when` 85, thời lượng 14, các trường kiểm tra/dự án 15.
- DE có thêm 1 sai biệt ở lesson 440, do dấu phân cách `---` bị dính vào dòng `Done when` trong note.

Ví dụ lesson 001:

- `.../lesson_001_What a Data Analyst actually does all day/note.md:25`:

  > Kể tên sáu vai trò dữ liệu và phân biệt ranh giới trách nhiệm. Tự đánh giá khoảng trống kỹ năng cá nhân.

- `material/data-analyst/roadmap-data-analyst.md:533`:

  > Phân định trách nhiệm giữa Data Analyst và các vai trò lân cận bằng một danh sách nhiệm vụ thực tế, rồi định vị khoảng cách năng lực cá nhân so với chuẩn Junior DA.

- `.../lesson_001_What a Data Analyst actually does all day/note.md:33`:

  > Xong đọc 10 tin tuyển dụng thật, ghi lại nguồn/ngày truy cập, phân loại vai trò đạt tối thiểu 8/10, và làm lại sau phản hồi để đạt chuẩn.

- `material/data-analyst/roadmap-data-analyst.md:543`:

  > Nộp bảng tự đánh giá có bằng chứng, ghi rõ nguồn/ngày truy cập và đạt tối thiểu 12/15 tình huống phân vai sau một vòng phản hồi.

**Vì sao là vấn đề**

Tác giả có thể soạn đúng phần đặc tả nằm trong note nhưng vẫn sai roadmap đã duyệt. Đây chính xác là điều đã xảy ra ở bài mẫu. `Web/parse_curriculum.py` loại khối đặc tả khỏi nội dung hiển thị nên web không vỡ, nhưng quy trình tác giả hóa và đánh giá bị vỡ.

**Đề xuất sửa**

Không sửa tay từng bản sao. Chọn một nguồn chân lý, sinh/kiểm tra khối đặc tả từ roadmap trong CI và chặn chuyển `trang_thai: xong` khi khác. Trước khi nhân mẫu, đồng bộ lại 85 bài DA và xử lý riêng DE lesson 440.

### N-02 — Bài mẫu không thực sự chứng minh Outcome/Done when hiện hành

**Bằng chứng**

Outcome hiện hành ở `material/data-analyst/roadmap-data-analyst.md:533` như trích ở N-01. Assessment cùng bài tại `:535` yêu cầu phân loại 15 nhiệm vụ và đạt `>=12/15`; Done when tại `:543` cũng yêu cầu `12/15`.

Bài mẫu có các phần đáp ứng một phần:

- `.../note.md:102-109`: mô tả sáu vai trò lân cận.
- `.../note.md:160-170`: cây quyết định phân loại.
- `.../note.md:336`: bài tự đánh giá khoảng trống năng lực.

Nhưng công cụ đánh giá lại dùng chuẩn khác:

- `.../note.md:44`: mục tiêu là phân loại đúng ít nhất `6/8` nhiệm vụ.
- `.../note.md:259`: hoạt động lớp chỉ có `8` yêu cầu công việc.
- `.../note.md:288-305`: phần tự kiểm chỉ đưa `4` tình huống, không phải 15.

**Vì sao là vấn đề**

Bài có nội dung giải thích đúng hướng, nhưng không có công cụ nào đo đúng điều roadmap hứa. Không thể kết luận người học đạt `12/15`, cũng không có bảng bằng chứng nguồn/ngày theo Done when hiện hành.

**Đề xuất sửa**

Sau khi chốt nguồn chân lý, tạo đúng bộ 15 tình huống, đáp án/rubric, vòng phản hồi và mẫu bảng tự đánh giá có bằng chứng. Kiểm thử traceability Outcome → hoạt động → đánh giá → Done when.

### N-03 — Bài mẫu chưa phải gói dạy 120 phút hoàn chỉnh

**Bằng chứng**

Điểm tốt: `.../note.md:253-260` có timeline chi tiết, tổng đúng 120 phút; 9 mục La Mã đều có nội dung.

Tuy vậy:

- `.../slides.md:1-8`: trạng thái `chua-soan`.
- `.../quiz.md:1-8`: khung 10 câu, chưa có câu hỏi/đáp án.
- `.../homework.md:1-8`: khung bài tập, chưa có đề/rubric.
- `.../note.md:259`: yêu cầu “8 yêu cầu công việc” nhưng không kèm bộ 8 tình huống.
- `.../note.md:260`: yêu cầu 10 tin tuyển dụng trực tiếp nhưng không có bộ dự phòng, ngày chụp hay hướng dẫn khi nguồn biến mất.

**Vì sao là vấn đề**

Note đủ làm xương sống bài giảng, nhưng giảng viên vẫn phải tự tạo học liệu, đáp án, tình huống và dữ liệu tại chỗ. Bài không đạt tiêu chí “dạy được mà không cần hỏi thêm”.

**Đề xuất sửa**

Hoàn tất đồng bộ cả bốn artefact; đóng gói tình huống, đáp án, rubric, nguồn dự phòng và hướng dẫn facilitator. Chỉ cho phép trạng thái bài `xong` khi tất cả artefact bắt buộc đạt trạng thái tương ứng.

### N-04 — Cổng trạng thái cho phép note `xong` trong khi ba artefact còn lại chưa soạn

**Bằng chứng**

Lesson 001 có `note.md` trạng thái `xong`, nhưng `slides.md`, `quiz.md`, `homework.md` đều còn khung/chưa soạn. Parser vẫn báo `giao an 1/525`.

`Web/parse_curriculum.py` hiện lấy trạng thái hoàn tất từ note, không kiểm chứng tính sẵn sàng của gói bốn tệp.

**Vì sao là vấn đề**

Chỉ số hoàn thành trên web có thể tạo cảm giác bài đã sẵn sàng triển khai trong khi học liệu và đánh giá chưa tồn tại.

**Đề xuất sửa**

Định nghĩa readiness ở cấp bundle: note + slides + quiz + homework, kèm validation Outcome/Assessment. Tách rõ “note đã viết” và “bài sẵn sàng dạy”.

### N-05 — Thời lượng tự học DA lệch 14 giờ; thời lượng DE lệch 17,5 giờ và bảng gate tự mâu thuẫn

**Bằng chứng DA**

- `material/data-analyst/roadmap-data-analyst.md:21-22` công bố 170 giờ trên lớp + 170 giờ tự học.
- 18 bài LT ghi “2 giờ tự học” nhưng phân bổ chi tiết chỉ cộng thành 100 phút, ví dụ `:541`.
- 4 bài KT ghi thời lượng tự học 2 giờ nhưng phần chi tiết nói không giao tự học, ví dụ lesson 16 tại `:844`.
- Tổng theo phân bổ chi tiết: **156 giờ**, thiếu **14 giờ** so với 170.

22 bài bị ảnh hưởng: 1, 2, 3, 4, 16, 17, 23, 30, 31, 33, 38, 40, 41, 46, 52, 54, 55, 64, 68, 77, 80, 85.

**Bằng chứng DE**

- `material/data-engineer/roadmap-data-engineer.md:21` công bố 1.056 giờ tự học.
- 10 bài KT ghi 2,4 giờ nhưng phần chi tiết nói không giao tự học: lessons 44, 88, 112, 148, 202, 230, 308, 360, 404, 440 (`:1035`, `:1919`, `:2409`, `:3127`, `:4207`, `:4775`, `:6329`, `:7385`, `:8275`, `:9013`).
- Tổng theo phân bổ chi tiết: **1.032 giờ**, thiếu **24 giờ**.
- Bảng gate `:101-110` cho 7 bài thời lượng 150/180 phút, nhưng đặc tả bài và front matter đều là 120 phút: lessons 44, 112, 230, 308, 360, 404, 440.
- Nếu tin bảng gate, giờ lớp là 886,5 thay vì 880; cộng tự học chi tiết thành 1.918,5 thay vì tổng công bố 1.936, lệch **17,5 giờ**.

**Vì sao là vấn đề**

Khối lượng học, lịch lớp, hợp đồng với giảng viên và năng lực đạt được không thể cùng đúng khi các tầng tài liệu cho các tổng khác nhau.

**Đề xuất sửa**

Chọn quy tắc tính thời lượng cho từng dạng bài; sinh tổng từ đặc tả bài thay vì nhập tay. Với KT, quyết định rõ có hay không có tự học. Với gate, đưa một thời lượng duy nhất vào front matter, bảng gate và timeline.

### N-06 — Kho nguồn không có truy vết cấp bài; 1.997/1.997 tệp không được tham chiếu tường minh

**Bằng chứng**

- Đếm được 1.997 tệp trong `material/**/ref/`, gồm 1.443 PDF.
- Tìm liên kết Markdown/đường dẫn `ref/` từ mọi roadmap và bài: **0**.
- Do đó, theo tiêu chí tham chiếu tường minh, **1.997/1.997** tệp chưa được roadmap hoặc bài trỏ tới.
- `material/data-engineer/ref/README.md:3` nói thư mục “intentionally empty”, nhưng thực tế có 1.995 tệp.
- `material/data-engineer/ref/README.md:7-10` mô tả cấu trúc `sach/`, `bai-viet/`, `dataset/`, `links.md`; cấu trúc thật là các cây sâu `Computer Science/` và `knowledge/`.
- Có 149 tệp mang tên README/index/manifest ở các gói con, nhưng không có manifest cấp giáo trình ánh xạ lesson → source.

**Vì sao là vấn đề**

Không thể trả lời có kiểm chứng “bài này dựa vào nguồn nào”, “nguồn này dùng ở đâu”, hoặc “nguồn nào tải về rồi bỏ”. Cây thư mục sâu tới 8 cấp và README cấp chương trình đã lỗi thời làm việc tìm nguồn phụ thuộc vào nhớ tên sách/thư mục.

**Đề xuất sửa**

Tạo manifest máy đọc được ở cấp chương trình hoặc toàn repo: `source_id`, đường dẫn, loại, tác giả/năm, license, checksum, lesson sử dụng, đoạn/trang sử dụng. Mỗi claim quan trọng trong bài tham chiếu `source_id`; CI kiểm tra nguồn tồn tại và phát hiện orphan hai chiều.

### N-07 — Roadmap và README trỏ tới nguồn nội bộ không tồn tại

**Bằng chứng**

- `material/data-analyst/roadmap-data-analyst.md:2492-2493` nói có `material/data-analyst/ref/SOURCES.md`; tệp này không tồn tại.
- `material/data-analyst/ref/README.md:8-10` liệt kê ba PDF nguồn, nhưng cả ba không có trong `ref/`.

**Vì sao là vấn đề**

Đây là liên kết nguồn đứt. Các tuyên bố thị trường trong roadmap không thể lần theo sổ nguồn được hứa hẹn.

**Đề xuất sửa**

Khôi phục đúng tệp/đường dẫn và thêm kiểm tra link tồn tại; nếu nguồn không được phép lưu trong repo, manifest cần ghi URL, ngày truy cập, bản quyền và fingerprint thay thế.

### N-08 — Nhiều khẳng định thị trường và dữ kiện trong bài mẫu không có năm/nguồn trực tiếp

**Bằng chứng roadmap DA**

- `material/data-analyst/roadmap-data-analyst.md:136-139`: Power BI là bắt buộc, Tableau/Looker chuyển đổi “trong vài ngày”, và tỷ lệ công việc 40%—không có nguồn trực tiếp hoặc năm đo.
- `:158-162`: phân bổ 40/20/20/15/5 được gọi là kết quả khảo sát, nhưng không nêu mẫu, năm hay URL.
- `:240-247`: đặc trưng công ty/ngành và ví dụ doanh nghiệp không có nguồn/năm.
- `:251-256`: mô tả kênh tuyển dụng không có bằng chứng/năm.
- `:258-275`: một JD ngân hàng được gọi là “thực tế”, nhưng thiếu tên nhà tuyển dụng, URL, ngày đăng và ngày truy cập.

Điểm làm tốt: `:235-236` có mốc Q2/2025 và nguồn ITviec; bảng lương `:291-301` có năm, nguồn thứ cấp và cảnh báo hạn chế.

**Bằng chứng bài mẫu**

- `.../note.md:84-94`: 20/40/20/15/5 không có nguồn trực tiếp.
- `:131-142`: đặc trưng các loại công ty và tên doanh nghiệp không có dẫn nguồn.
- `:148-150`: “DA là cửa vào phổ biến nhất”, Python chuyển từ điểm cộng thành yêu cầu, xu hướng self-service—không có nguồn/năm.
- `:172`: công ty dưới 50 người “thường” không có các vai trò khác—không có nguồn.
- `:202-214`: các số 12%, 11 ngày, 4% không gắn dataset hay nguồn và không được đánh dấu rõ là dữ liệu giả lập.
- `:236`: có thể học công cụ trong hai tuần—không có nguồn.
- `:247`: 80%/90% không có nguồn hoặc nhãn ví dụ giả định.

**Vì sao là vấn đề**

Các câu này có thể bị hiểu là dữ kiện thị trường có bằng chứng. Đặc biệt trong bài mở đầu nghề nghiệp, dữ kiện không truy vết làm giảm độ tin cậy và nhanh lỗi thời.

**Đề xuất sửa**

Mỗi claim thị trường phải có năm, phạm vi địa lý/mẫu và nguồn; dữ liệu minh họa phải ghi rõ “giả lập”. Claims không đủ bằng chứng nên chuyển thành giả thuyết/thảo luận, không trình bày như sự thật.

### N-09 — Ledger duyệt chỉ khóa DA; DE chưa có bằng chứng khóa roadmap

**Bằng chứng**

`.data-2026/roadmap-approved.json:3-20` chỉ có scope `material/data-analyst/roadmap-data-analyst.md` với:

```text
artifact_sha256 = 64391070c20b3ae21c5c6c5124ccd216a1987121d376b9b0f565f4f19ba14801
```

SHA-256 vừa tính của tệp DA đúng bằng giá trị này. Không có entry cho roadmap DE.

**Vì sao là vấn đề**

DA có bằng chứng bất biến sau duyệt và hiện vẫn khớp—đây là điểm làm tốt. Nhưng không thể đưa ra kết luận tương tự cho DE; thay đổi DE sau duyệt (nếu đã duyệt) sẽ không bị phát hiện bằng ledger hiện tại.

**Đề xuất sửa**

Thêm entry riêng cho DE sau khi hoàn tất review; ghi rõ scope, ngày, reviewer và hash. Nếu AE tách riêng, có entry thứ ba.

### N-10 — Đối chiếu khung ngoài cho thấy một số khoảng trống năng lực và mapping lỗi thời

**roadmap.sh Data Analyst**

Roadmap hiện hành nêu thu thập dữ liệu từ database/CSV/API/web scraping, thống kê có regression, cùng các nhánh ML/big data/deep learning. Roadmap DA nội bộ `:119-139` mô tả roadmap.sh như một lộ trình “11 bước” có “Modern Data Stack”; mô tả này không khớp bản PDF hiện hành.

- Thiếu đáng kể: thu thập dữ liệu qua API/web ở cấp analyst.
- Có thể chấp nhận do phạm vi nghề: không dạy sâu ML, big data, deep learning; roadmap nội bộ chủ ý định vị Junior DA thay vì Data Scientist.
- Có thể chấp nhận: ưu tiên Power BI thay vì buộc nhiều BI tool, nếu nói rõ nguyên tắc chuyển giao và không hứa thời gian “vài ngày” khi chưa có bằng chứng.

Nguồn: [roadmap.sh Data Analyst PDF](https://roadmap.sh/pdfs/roadmaps/data-analyst.pdf).

**roadmap.sh Backend**

DE đã phủ tốt ngôn ngữ/Git, network, relational database, API/auth/security, testing/CI-CD, broker/streaming, container/Kubernetes, scaling và observability.

- Khoảng trống đáng cân nhắc vì đầu ra có Backend/Platform: cache/Redis, NoSQL/document/graph/time-series databases, search engine operational basics.
- Khác biệt có lý do nếu giữ phạm vi Data Engineer: GraphQL, WebSockets, HATEOAS, serverless và service mesh không nhất thiết là cốt lõi.

Nguồn: [roadmap.sh Backend PDF](https://roadmap.sh/pdfs/roadmaps/backend.pdf).

**EDISON Data Science Framework**

EDISON nhóm năng lực thành analytics, engineering, data management/governance, research/project management và domain/business. Chương trình có nhiều phần engineering/governance và business framing, nhưng:

- kiến thức miền tập trung mạnh commerce/retail/product, ít cơ chế chuyển giao sang miền khác;
- research/project management chưa được đánh giá như năng lực xuyên suốt;
- ethics/privacy xuất hiện mỏng, chưa thành năng lực có đánh giá độc lập.

Việc DA không dạy ML sâu là khác biệt hợp lý: EDISON là khung Data Science rộng và cũng cho phép profile không cần mọi năng lực.

Nguồn: [EDISON CF-DS Release 2](https://edison-project.eu/sites/edison-project.eu/files/filefield_paths/edison_cf-ds-release2-v08_0.pdf).

**SFIA 9**

- Profile Data Analyst chuẩn gồm DAAN, BINT, REQM, VISL, DATM. Roadmap DA khai DAAN/BINT/VISL/DTAN nhưng bỏ REQM và DATM khỏi mapping, dù nội dung thực tế có phần yêu cầu và quản lý dữ liệu.
- Profile Data Engineer chuẩn gồm DENG, DATM, REQM, PROG, DTAN, DBDS, SINT, NFTS, TEST; roadmap DE khai một bộ khác và không hề dùng các mã DENG, REQM, DBDS, SINT, NFTS, SWDN. Nội dung có thể đã phủ nhiều năng lực, nhưng mapping không chứng minh được điều đó.

Nguồn: [SFIA 9 role-family profiles](https://sfia-online.org/en/tools-and-resources/standard-industry-skills-profiles/sfia-9-skills-for-role-families-job-titles), [SFIA Data and Analytics view](https://sfia-online.org/en/sfia-9/sfia-views/full-framework-view/development-and-implementation/data-solutions/?path=/glance).

**Đề xuất sửa chung**

Chốt ngày/version cho từng external benchmark; tạo ma trận competence → lesson → assessment. Phân biệt rõ “cố tình ngoài phạm vi” với “chưa phủ”; không chỉ liệt kê mã khung ở phần đầu.

## NHẸ

### H-01 — Một tên thư mục không khớp `tieu_de`

**Bằng chứng**

- Thư mục: `material/data-engineer/curriculum/module_5-Operating Systems, Concurrency and Linux/curriculum/lesson_066_Readiness against completion - partial I - O, cancellation and io_uring awareness`
- `note.md:5`:

  > Readiness against completion - partial I/O, cancellation and io_uring awareness

**Vì sao là vấn đề**

Parser hiện ghép bằng số bài nên build không lỗi, nhưng quy ước tên thư mục không nhất quán; liên kết thủ công, tooling và tra cứu có thể lệch.

**Đề xuất sửa**

Chọn tên canonical từ `tieu_de` và thêm validation slug/title trong CI.

### H-02 — Tài liệu tác giả hóa còn số liệu và mô hình artefact cũ

**Bằng chứng**

- `Web/docs/soan-bai-giang.md:7` nói tổng `272` bài.
- `Web/docs/soan-bai-giang.md:28` mô tả sáu thành phần, gồm cả mindmap/materials, trong khi cấu trúc bài được kiểm hiện có bốn tệp bắt buộc.
- Ví dụ output phía sau vẫn mô tả cấu trúc chương trình cũ.

**Vì sao là vấn đề**

Không làm hỏng parser, nhưng người soạn mới có thể theo sai quy trình và kỳ vọng sai số lượng.

**Đề xuất sửa**

Sinh tài liệu tác giả hóa từ schema/parser hoặc ít nhất thêm kiểm tra số liệu trong CI.

### H-03 — Ba “từ khóa không quan sát được” là false positive, không phải lỗi Outcome

Quét từ vựng tìm thấy ba Outcome chứa `hiểu/biết/nắm`, nhưng động từ chính đều quan sát được:

- DE lesson 3, `material/data-engineer/roadmap-data-engineer.md:216`: “**Viết** một chương trình... để người khác đọc hiểu được...”
- DE lesson 218, `:4539`: “**Cài đặt và benchmark**...” rồi “phân biệt giải mã được với hiểu đúng”.
- DE lesson 394, `:8077`: “**Dựng**...” cho người chưa biết hệ thống thu hẹp nguyên nhân.

Không đề xuất sửa chỉ vì từ khóa. Đây là điểm làm tốt: Outcome dùng hành vi có thể quan sát và Done when đo được.

---

# 3. Kết quả kiểm tra chi tiết theo yêu cầu

## A2. Front matter và parser

Schema kiểm tra cho 525 `note.md`:

- `chuong_trinh`: chuỗi
- `module`: chuỗi
- `lesson`: số nguyên
- `tieu_de`: chuỗi
- `dang_bai`: một trong `LT`, `TH`, `DA`, `KT`
- `thoi_luong_phut`: số nguyên
- `trang_thai`: một trong `xong`, `chua-viet`

Kết quả: **0 tệp thiếu khóa, 0 tệp sai kiểu, 0 giá trị enum ngoài tập**. Parser chạy thành công, không in lỗi.

## A3. Toàn vẹn cấu trúc

- 525/525 thư mục bài có đủ `note.md`, `quiz.md`, `homework.md`, `slides.md`.
- 0 module có số bài trùng.
- 0 module có số bài nhảy cóc.
- 0 trường hợp số lesson trong tên thư mục khác front matter.
- 1 trường hợp tên thư mục khác `tieu_de`: H-01.

## A4. Roadmap so với thực tế

| Chương trình | `so_bai` roadmap | Đặc tả trong roadmap chương trình | Bài trong roadmap module | Thư mục thật | Kết quả |
|---|---:|---:|---:|---:|---|
| Data Analyst | 85 | 85 | 85 | 85 | Khớp |
| Data Engineer | 440 | 440 | 440 | 440 | Khớp |

- 40/40 roadmap module có tập bài khớp hoàn toàn với thư mục thực tế.
- Không có bài trong module roadmap mà thiếu thư mục.
- Không có thư mục bài nằm ngoài module roadmap.
- Tiêu đề/thời lượng giữa roadmap chương trình và roadmap module khớp cho 525 bài; các mâu thuẫn thời lượng nằm ở bảng tổng/gate và phân bổ tự học, không phải giữa hai danh sách bài.

## A5. Khóa roadmap

`.data-2026/roadmap-approved.json` trỏ tới roadmap DA. Kết quả:

```text
artifact_sha256 trong ledger:
64391070c20b3ae21c5c6c5124ccd216a1987121d376b9b0f565f4f19ba14801

sha256 vừa tính:
64391070c20b3ae21c5c6c5124ccd216a1987121d376b9b0f565f4f19ba14801
```

**Khớp.** Roadmap DA không bị sửa sau trạng thái khóa được ghi. Ledger không chứa DE; xem N-09.

## B1. Chất lượng đặc tả 525 bài

| Chương trình | Tổng bài | Thiếu objective | Thiếu done-when | Thiếu prereq | Động từ chính không quan sát được |
|---|---:|---:|---:|---:|---:|
| Data Analyst | 85 | 0 | 0 | 0 | 0 |
| Data Engineer | 440 | 0 | 0 | 0 | 0 |
| **Tổng** | **525** | **0** | **0** | **0** | **0** |

Danh sách bài thiếu: **không có**. Ba lexical hit đã được đọc lại và xác nhận không phải lỗi, xem H-03.

Điểm làm tốt:

- Mỗi bài đều có Prerequisites, Learn, Outcome, Lab, Assessment, Pitfalls, In-class, Self-study và Done when.
- Outcome nhìn chung bắt đầu bằng động từ tạo artefact/hành vi: viết, dựng, phân tích, thiết kế, triển khai, benchmark, chẩn đoán.
- Roadmap module sao chép nhất quán đặc tả bài từ roadmap chương trình.

Vấn đề thời lượng: xem N-05.

## B2. Đồ thị prerequisites

| Chương trình | Nút | Cạnh phụ thuộc | Chu trình | Phụ thuộc bài phía sau | Bài mồ côi | Tham chiếu không giải được |
|---|---:|---:|---:|---:|---:|---:|
| Data Analyst | 85 | 281 | 0 | 0 | 0 | 0 |
| Data Engineer | 440 | 883 | 0 | 0 | 0 | 0 |

Quy tắc dựng đồ thị: phân giải `Lesson N`, phụ thuộc module dạng `M#`, và khoảng module như `M1–M10`; prerequisite nền tảng ngoài giáo trình không được biến thành nút giả.

Kết luận: đồ thị sạch, có thứ tự hợp lệ và không có bài hoàn toàn cô lập. Đây là điểm mạnh đáng giữ.

## B3. Trùng lặp/giao nhau

Không thể làm so sánh ba chương trình độc lập vì AE không tồn tại như chương trình; phần AE nằm trong DE M12, M13, M18, M19. Các cụm giao DA–DE/AE đáng chú ý:

### SQL NULL và logic ba trị — phân tầng có chủ ý

- DA lesson 19, `material/data-analyst/roadmap-data-analyst.md:906-910`: học `NULL` trong biểu thức, lọc, tổng hợp và ảnh hưởng đến báo cáo.
- DE lesson 114, `material/data-engineer/roadmap-data-engineer.md` đặc tả lesson 114: đặt `NULL` trong ngữ nghĩa quan hệ và kiểm thử case cạnh.

DA tập trung tránh sai báo cáo; DE tập trung semantics/hệ thống. Đây là giao nhau hợp lý.

### Subquery/CTE/window functions — phân tầng có chủ ý

- DA lessons 25–27, ví dụ `material/data-analyst/roadmap-data-analyst.md:1058-1062`: dùng window functions để tạo báo cáo và đối chiếu kết quả.
- DE lessons 121/123/124, ví dụ `material/data-engineer/roadmap-data-engineer.md:2645-2649`: thêm tính đúng, materialization/performance và case cạnh.

Không thấy bằng chứng chép nguyên khối; cùng công cụ nhưng mục đích nghề và Done when khác.

### Dimensional modeling và SCD — phân tầng có chủ ý

- DA lessons 34–35, `material/data-analyst/roadmap-data-analyst.md:1208-1231`: thiết kế star schema nhỏ và SCD Type 2 cho nhu cầu phân tích.
- DE lessons 153/157, `material/data-engineer/roadmap-data-engineer.md:3230-3234,3306-3310`: bus matrix, SCD 0–6, bất biến và kiểm thử 1.000 cập nhật.

Độ sâu và mục đích khác rõ: DA tiêu thụ/mô hình cho BI; DE/AE xây và vận hành mô hình.

### Metric tree/metric contract — giao gần nhất nhưng vẫn có phân tầng

- DA lesson 4, `material/data-analyst/roadmap-data-analyst.md:588-592`: chuyển mục tiêu thành metric tree, gán owner/lever.
- DE lesson 186, `material/data-engineer/roadmap-data-engineer.md:3893-3897`: cũng dùng metric tree nhưng thêm metric contract có schema, freshness, quality và ownership.

Khái niệm lõi lặp lại khá sát, nhưng DE mở rộng thành hợp đồng dữ liệu vận hành. Nên cross-reference để tránh dạy lại phần nhập môn.

### Reconciliation/data quality — phân tầng có chủ ý

- DA lessons 15/37, `material/data-analyst/roadmap-data-analyst.md:813-819,1265-1271`: kiểm tra kết quả phân tích và số liệu báo cáo.
- DE lesson 284, `material/data-engineer/roadmap-data-engineer.md:5845-5849`: reconciliation nhiều tầng và control point trong pipeline.

DA kiểm chứng kết quả tiêu dùng; DE thiết kế kiểm soát hệ thống.

### Requirement framing — phân tầng có chủ ý

- DA lesson 5: biến yêu cầu mơ hồ thành câu hỏi/phạm vi/metric cho phân tích.
- DE lesson 1: biến yêu cầu mơ hồ thành acceptance test/contract cho hệ thống dữ liệu.

Đây là năng lực chung cần lặp lại theo ngữ cảnh nghề, không phải chép qua lại.

## B4. Mâu thuẫn

Các mâu thuẫn đã xác nhận:

1. Ba chương trình độc lập so với AE gộp trong DE: C-01.
2. “AE viết SQL, DE viết hệ thống để SQL chạy” so với DE cũng dùng SQL để nạp/đối soát: C-02.
3. Thời lượng tổng, gate và timeline chi tiết không thể đồng thời đúng: N-05.
4. Đặc tả nhúng trong note so với roadmap đã khóa: N-01/N-02.
5. `material/data-engineer/roadmap-data-engineer.md:20` nói không yêu cầu đầu vào; phần module 1 lại yêu cầu dùng được terminal và sửa tệp văn bản. Đây có thể là chuẩn chuẩn bị chứ không phải prerequisite tuyển sinh, nhưng cần phân biệt bằng câu chữ.

Trong các cụm kỹ thuật trùng lặp đã đọc, không thấy hai roadmap đưa ra kết luận kỹ thuật đối nghịch; phần lớn là phân tầng hợp lý.

## B5. Khẳng định không dẫn nguồn

Danh sách chính và vị trí đã ghi tại N-08. Kết luận:

- Có nguồn/năm tương đối rõ: tăng trưởng tuyển dụng Q2/2025; bảng lương 2025 với cảnh báo hạn chế.
- Không đạt yêu cầu năm + nguồn: phân bổ thời gian công việc, đặc trưng ngành/công ty, kênh tuyển dụng, độ phổ biến của DA, xu hướng Python/self-service, thời gian học công cụ, và hầu hết con số case bài mẫu.
- Lesson 001 chỉ có một liên kết Markdown tới roadmap nội bộ, không có citation tới một nguồn trong `ref/`.

## B6. Đối chiếu ngoài

Chi tiết và nguồn ở N-10. Tóm tắt khoảng trống cốt lõi:

| Khung | Khoảng trống đáng kể | Khác biệt có lý do |
|---|---|---|
| roadmap.sh DA | API/web data collection; regression ở mức ứng dụng | Không dạy sâu ML/big data/deep learning vì định vị Junior DA |
| roadmap.sh Backend | cache, NoSQL, search-engine fundamentals cho nhánh Backend/Platform | Không cần phủ mọi GraphQL/WebSocket/serverless/service-mesh trong DE core |
| EDISON | domain transfer, project/research method, ethics/privacy có đánh giá | DS/ML không phải lõi của chương trình DA |
| SFIA 9 | mapping DA thiếu REQM/DATM; mapping DE thiếu nhiều mã profile chuẩn | Nội dung thực tế phủ nhiều phần, vấn đề chủ yếu là traceability/mapping |

## C1. Outcome của lesson 001

Outcome chuẩn là câu tại `material/data-analyst/roadmap-data-analyst.md:533`, không phải câu cũ trong note. Bài đáp ứng phần nhận diện vai trò và tự đánh giá qua các đoạn `note.md:102-109`, `:160-170`, `:336`; không đáp ứng bài đo 15 tình huống/12 đúng và Done when có bằng chứng. Kết luận: **đạt một phần về nội dung, không đạt về bằng chứng đánh giá**.

## C2. Chín mục La Mã

Các mục bắt đầu tại `note.md:37,54,80,156,185,220,251,272,310`. Cả 9/9 đều có nội dung; không có mục chỉ có tiêu đề. Đây là điểm làm tốt.

## C3. Dữ kiện và nguồn

Lesson 001 không chỉ ra nguồn trong `ref/` cho bất kỳ dữ kiện nào. Các nhóm không truy vết được: tỷ trọng công việc, đặc trưng loại hình doanh nghiệp, xu hướng nghề/công cụ, ngưỡng nhân sự, dữ liệu case 12%/11 ngày/4%, thời gian “hai tuần”, các tỷ lệ 80%/90%. Chi tiết dòng ở N-08.

## C4. Khả năng dạy 120 phút

**Chưa đủ để dạy mà không cần hỏi thêm.** Timeline đủ 120 phút và nội dung giảng khá đầy, nhưng thiếu bộ tình huống, quiz/đáp án, homework/rubric, slide, nguồn dự phòng và artefact đánh giá đúng chuẩn 12/15.

## C5. Khả năng nhân khuôn

Khuôn 9 mục dùng được như skeleton chung, nhưng sẽ gây khó nếu áp nguyên dạng:

- **TH:** thiếu môi trường/setup, input fixture, bước thao tác, expected output, checkpoint, lỗi dự kiến và cách khôi phục.
- **KT:** các mục lý thuyết/case/homework không thay được blueprint đề, version/security, accommodation, rubric/chấm điểm, evidence capture, remediation/retest.
- **DA:** thiếu milestone, scope, vai trò nhóm, review gate và rubric tổng hợp.
- **Mọi dạng:** thiếu mục citations/source map; trạng thái note không đại diện bundle readiness.

Lesson 16 dạng KT vẫn mang skeleton LT-centric trong `note.md:40-72`, cho thấy vấn đề đã xuất hiện ở khung chưa viết. Trước khi nhân 524 bài, cần template theo `dang_bai`, không chỉ một template chung.

## D1. Khả năng tìm nguồn

Không đạt ở cấp giáo trình. DA có hai tệp ref nhưng README trỏ nguồn thiếu; DE có 1.995 tệp trong cây sâu, README sai trạng thái, không có manifest lesson → source. Các README/index nằm trong gói con không thay thế catalog cấp curriculum.

## D2. Nguồn không được dùng

Theo tiêu chí có thể kiểm máy là **đường dẫn/liên kết tường minh**, 1.997/1.997 tệp trong `ref/` không được roadmap hoặc bài nào trỏ tới. Đây không chứng minh nội dung của chúng chưa từng được người viết đọc; nó chứng minh không có traceability để kiểm.

## D3. Tham chiếu nguồn bị thiếu

Đã xác nhận thiếu `material/data-analyst/ref/SOURCES.md` và ba PDF được DA README liệt kê. Ngoài ra không có tham chiếu tệp ref cụ thể nào từ lesson/roadmap để kiểm tồn tại.

---

# 4. Những chỗ đang làm tốt — không nên sửa nhầm

1. Parser chạy sạch và số liệu module/bài nhất quán.
2. 525/525 front matter đúng schema mà web đang đọc.
3. 525/525 bundle có đủ bốn tên tệp bắt buộc.
4. Số bài trong từng module liên tục, không trùng, không nhảy cóc.
5. Roadmap chương trình, roadmap module và thư mục bài khớp tập lesson.
6. Tất cả 525 bài có Outcome, Done when và Prerequisites.
7. Đồ thị phụ thuộc của cả hai chương trình là DAG sạch, không có cạnh đi ngược hay nút mồ côi.
8. Giao nhau DA–DE phần lớn là phân tầng theo mục đích nghề, không phải bản sao nguyên khối.
9. Lesson 001 có đủ 9 phần và timeline đúng 120 phút; vấn đề nằm ở học liệu/đánh giá/nguồn, không phải thiếu cấu trúc note.
10. Hash roadmap DA khớp ledger duyệt; không có dấu hiệu roadmap DA bị sửa sau khi khóa.

---

# 5. Tôi không kiểm được

Phần này là giới hạn bắt buộc của báo cáo:

1. **Không thể kiểm ba chương trình độc lập** vì repo chỉ có hai. Muốn kết luận chất lượng riêng của AE cần roadmap/module/bài AE độc lập, hoặc một quyết định chính thức rằng AE là nhánh của DE.
2. **Không đọc nội dung 1.443 PDF**, đúng theo yêu cầu. Vì vậy không kết luận sách/PDF có đúng, cập nhật, hợp pháp hay thực sự hỗ trợ claim nào; cần manifest lesson → source → trang/đoạn và review nội dung có chọn mẫu.
3. **Không thể khẳng định 1.997 tệp chưa từng được sử dụng về mặt ý tưởng.** Tôi chỉ chứng minh không có tham chiếu tường minh từ roadmap/bài. Muốn kết luận semantic usage cần citation hoặc provenance log.
4. **Không xác minh độc lập mọi số liệu thị trường/lương** trong nguồn gốc ngoài repo. Một số có năm/nguồn, nhưng cần URL gốc, ngày truy cập và phương pháp khảo sát để kiểm tính đúng.
5. **Không thể xác nhận license/quyền lưu trữ** của kho PDF. Cần manifest license và provenance cho từng nguồn.
6. **Không chạy `make`, không deploy**, theo quy tắc. Vì vậy chỉ xác nhận parser trực tiếp chạy thành công, không xác nhận toàn bộ pipeline build/deploy.
7. **Không chạy thử lớp 120 phút với người học thật.** Nhận định teachability dựa trên sự hiện diện của facilitator materials, assessment và timeline; cần pilot class, observation và learner evidence để kết luận hiệu quả dạy.
8. **Đối chiếu roadmap.sh là với bản hiện hành truy cập ngày kiểm tra.** Roadmap nội bộ có thể từng so với một phiên bản cũ, nhưng không ghi URL/version/date nên không thể tái tạo so sánh lịch sử.
9. **Không thể kết luận SFIA level đạt được chỉ từ mã kỹ năng.** Cần behavior statements theo level, assessment evidence và rubric; báo cáo chỉ chỉ ra mapping thiếu/không truy vết.
10. **Không đánh giá độ đúng của toàn bộ 525 Outcomes ở cấp chuyên gia miền từng chủ đề.** Tôi kiểm đủ cấu trúc, động từ, đo lường, phụ thuộc và đọc sâu các vùng giao/mâu thuẫn; việc xác nhận kiến thức chi tiết cần SME review theo module.

---

# 6. Thứ tự xử lý đề nghị

1. Quyết định chính thức mô hình 2 hay 3 chương trình và định nghĩa lại ranh giới DA/DE/AE.
2. Dừng nhân bài mẫu; đồng bộ hợp đồng lesson 001 với roadmap đã khóa và hoàn tất bundle đánh giá/học liệu.
3. Loại bỏ drift đặc tả ở 85 note DA bằng một nguồn chân lý + validator.
4. Chuẩn hóa thời lượng và readiness gate.
5. Lập source manifest/citation graph, khôi phục các tham chiếu nguồn bị thiếu.
6. Cập nhật mapping external framework có version/date và ma trận competence → assessment.

