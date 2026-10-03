# TÁI KIỂM ROADMAP DATA ENGINEER SAU SỬA LỖI

Ngày kiểm: 2026-09-25  
Commit được kiểm: `41a0a60`  
Phạm vi: roadmap tổng, 29 roadmap module và 440 cây bài của Data Engineer; Data Analyst chỉ được kiểm không hỏng lây trong vòng này.  
Nguyên tắc: chỉ đọc; không chạy scaffold/diagram/assemble; không sửa curriculum hay nguồn sinh.

`make test` tại commit trên: **PASS toàn bộ**. Audit độc lập: `/tmp/audit_recheck_curricula.py` (SHA-256 `410c84b415ec69639e6888fdb369d52ba9ee2c363001d0433863fedfe329cb5f`), kết quả `/tmp/audit_recheck_curricula.json` (SHA-256 `0c4c41b8167869b52a55d0813ed193a615f433d1741ed153acbf5fd1a61558d6`). Hai tệp tạm không thuộc repo.

---

# Phần 1 — Lỗi phải sửa

## 1. Hai bài cổng vẫn tự mâu thuẫn về thời gian làm bài

**Mức nghiêm trọng: NẶNG.**

Roadmap đã sửa thời lượng cổng về 120/150/180 phút và tổng giờ đã khớp. Tuy nhiên:

- Lesson 44 ghi `In-class (120 phút)` gồm **75 phút làm bài + 45 phút chữa**, nhưng Lab lại cho **100 phút làm bài**.
- Lesson 112 cũng ghi 75 + 45 phút, nhưng Lab lại cho **110 phút làm bài**.

Hai mô tả không thể cùng thực hiện trong một buổi 120 phút.

**File và dòng.** `material/data-engineer/roadmap/roadmap.md:1024,1032,2398,2406`. Hai mâu thuẫn được sao nguyên vào roadmap module và `note.md` tương ứng.

**Bằng chứng tái hiện.**

```bash
rg -n -A12 '^### Lesson (44|112) ' material/data-engineer/roadmap/roadmap.md
```

**Đề xuất sửa.** Chọn một ngân sách độc lập duy nhất cho từng cổng, rồi đồng bộ ba nơi: `In-class`, `Lab`, và note sinh ra.

## 2. Các khẳng định định lượng về hiệu năng/khả năng vận hành vẫn không có nguồn hoặc điều kiện áp dụng

**Mức nghiêm trọng: VỪA.**

Các câu sau được viết như sự thật tổng quát nhưng roadmap không có citation và không nêu đủ điều kiện đo:

| Dòng | Khẳng định |
|---:|---|
| 1061 | Truy cập dữ liệu từ một tới hàng triệu nhịp; mỗi bậc chậm hơn 1–3 bậc độ lớn |
| 1080 | Cache line thường 64 byte; tuần tự nhanh hơn ngẫu nhiên hàng chục lần |
| 1099 | Bố trí cột có thể nhanh hơn hàng chục lần |
| 1194 | HDD random chậm hơn tuần tự hàng trăm lần |
| 1232 | Một triệu lần đọc một byte chậm hơn đọc khối 64 KB hàng trăm lần |
| 4254 | Đọc 3/100 cột chỉ tốn 3% byte, bỏ qua kích thước cột, encoding, metadata và compression |
| 5562 | Ngày 23/25 giờ “hai lần mỗi năm”, không giới hạn theo múi giờ/quy tắc DST |
| 8114 | Burn-rate alert thay được “hàng chục” cảnh báo và là cách giảm ồn hiệu quả nhất |

**File.** `material/data-engineer/roadmap/roadmap.md` tại các dòng trong bảng.

**Bằng chứng tái hiện.**

```bash
rg -n 'hàng (chục|trăm|triệu)|ba phần trăm|23 hoặc 25 giờ|64 byte|một tới ba bậc' \
  material/data-engineer/roadmap/roadmap.md
rg -n 'https?://' material/data-engineer/roadmap/roadmap.md
```

Lệnh thứ hai không trả URL nào. Đây không phải kết luận rằng các mệnh đề đều sai; lỗi là không thể truy vết và không biết miền áp dụng.

**Đề xuất sửa.** Gắn nguồn có phiên bản/ngày truy cập, hoặc đổi thành giả thuyết lab và bắt học viên đo trên phần cứng cụ thể.

---

# Phần 2 — Nội dung bị mất so với hợp đồng gốc

Tái kiểm đúng sáu module của vòng trước: M1, M12, M16, M18, M23, M29. **Không còn tìm thấy mục bị mất đã báo ở vòng trước.**

| Hợp đồng gốc / lỗi cũ | Trạng thái hiện tại | Bằng chứng hiện tại |
|---|---|---|
| M1: rollback qua schema change cần compatibility plan | ĐÃ KHÔI PHỤC | Lesson 97/98 nối rollback với tương thích hai chiều; roadmap `:2040,2116` |
| M12: 15+ metric, ít nhất 5 loại | ĐÃ KHÔI PHỤC | Lesson 184 capstone, roadmap `:3838-3850` |
| M12: sáu fixture NULL/duplicate/refund/late/SCD/fiscal | ĐÃ KHÔI PHỤC | Cùng block capstone `:3838-3850` |
| M12: two-consumer serving và cache isolation | ĐÃ KHÔI PHỤC | Lesson 179 và capstone `:3745-3755,3838-3850` |
| M12: dual-run, reconciliation, deprecation record | ĐÃ KHÔI PHỤC | Lesson 182/capstone `:3794-3811,3838-3850` |
| M12: hai critical failure về overwrite và cache context/version | ĐÃ KHÔI PHỤC | Lesson 183/capstone `:3819-3850` |
| M23: chọn Spark/Flink/Polars/DuckDB | ĐÃ KHÔI PHỤC | Lesson 358 mở rộng bốn lớp engine `:7338-7350` |
| M29: ba RFC, một RFC triển khai và đo adoption | ĐÃ KHÔI PHỤC | Lessons 433–439, đặc biệt `:8865-8991` |
| M29: hai người/two teams tự dùng paved road | ĐÃ KHÔI PHỤC | Lesson 436 `:8932-8940` |
| M29: cost/SLO và game day | ĐÃ KHÔI PHỤC | Lessons 439 và 403, `:8985-8991,8242-8275` |

M16 và M18 không có regression mới trong Outcomes/Labs/Exit Criteria/Critical failures đã đối chiếu ở vòng trước.

---

# Phần 3 — Không nhất quán nhưng chưa chắc sai

## Ngưỡng phụ thuộc môi trường

Các Done-when ở lessons 10, 31, 72, 125, 179, 238, 283, 292, 368, 393, 429 và 436 vẫn không chứa con số ngay tại bài. Khác vòng trước, roadmap nay có quy ước ở `material/data-engineer/roadmap/roadmap.md:9033-9038`: người dạy phải chốt và ghi ngưỡng vào đề **trước** buổi học.

Hai cách hiểu:

- Hợp lệ nếu đề giảng viên là artefact có phiên bản, được lưu cùng kết quả chấm.
- Chưa tái lập được nếu đề chỉ truyền miệng hoặc không được lưu; khi đó cùng sản phẩm có thể đạt ở lớp này và trượt ở lớp khác mà không có audit trail.

Không xếp đây là lỗi sau khi quy ước mới đã được thêm, nhưng việc triển khai quy ước chưa kiểm được vì đề chi tiết được roadmap tự ghi là “Chưa” tại `:9028-9031`.

---

# Phần 4 — Loại lỗi mà `make test` không phủ

1. **Mâu thuẫn ngữ nghĩa trong cùng bài.** Test thấy `In-class (120 phút)` hợp lệ nhưng không cộng `75 + 45` rồi đối chiếu với “100/110 phút làm bài” trong Lab. Nên parse tất cả số phút của KT và kiểm ngân sách.
2. **Độ đúng nội dung của tham chiếu.** Test chỉ kiểm `lesson N` tồn tại; không biết cụm danh từ quanh tham chiếu có đúng chủ đề bài N. Giữ một fixture tối thiểu cho các reference quan trọng sau renumber và duyệt nghĩa thủ công theo mẫu.
3. **Tính đầy đủ hợp đồng nguồn.** Test không ánh xạ Exit Criteria, Labs, Critical failures sang bài đích. Nên có manifest machine-readable `source_item -> lesson/field` và fail nếu item mất.
4. **Claim bên ngoài không có citation.** Test không phát hiện con số/từ tuyệt đối như “hàng trăm lần”, “hiệu quả nhất”. Nên lint câu định lượng yêu cầu citation hoặc nhãn `ước lượng/lab hypothesis`.
5. **Ngưỡng chấm runtime.** Test không kiểm đề lớp có ghi ngưỡng trước buổi học. Nên validate artefact đề theo schema và lưu timestamp/version.

---

# Phần 5 — Những gì đã kiểm và ĐẠT

- 440 lesson liên tục 1–440; 29 module liên tục 1–29; range liền, không hở/chồng; số bài từng module khớp `ade-module-map.md`.
- Tổng thời lượng module và tổng nhãn `In-class`: **884,5 giờ**. Tự học thực tế: **430 × 2,4 = 1.032 giờ**; header và module map đều đã sửa đúng.
- 440/440 bài có đúng chín trường và đúng một nhãn loại: 82 LT, 323 TH, 25 DA, 10 KT.
- 10 KT đúng cuối 10 phase và khớp bảng gate; phase/range khớp module map.
- 454 tham chiếu lesson trong văn xuôi đều thuộc 1–440; mọi prerequisite `Lesson N` đều lùi; 208 tham chiếu module đều thuộc 1–29.
- Mẫu tất định 40 tham chiếu lesson rải toàn chương trình đã đọc ngữ cảnh: không còn tham chiếu sai nghĩa; lỗi `lesson 140 tới 132` đã được sửa.
- Ánh xạ “Hợp đồng nguồn” của 29 module đã kiểm; mã module cũ trong prerequisite M12–M29 đã được sửa.
- Refresh SIMD/MIMD/async và hierarchy `MIMD workers → vectorized operators → SIMD lanes` còn hiện diện ở đúng M14/M23; không thấy regression.
- 29 thư mục module, 440 thư mục bài; đủ `note.md`, `quiz.md`, `homework.md`, `slides.md`, đúng một drawio mỗi bài. Cả 469 drawio (gồm drawio cấp module) parse XML thành công.
- Frontmatter 440 note khớp roadmap; 440 khối “Đặc tả từ roadmap” khớp từng chữ; 29 roadmap module có đúng tập bài và payload.
- Data Analyst không bị hỏng lây về cấu trúc: 11 module, 85 bài, tất cả drawio parse và frontmatter chính khớp. Các lỗi nội dung DA được báo riêng trong `REVIEW_CODEX_DA.md`.

## Giới hạn của vòng tái kiểm

- Chỉ 40/454 tham chiếu lesson được đọc nghĩa thủ công; phần còn lại được kiểm tồn tại/range.
- Chỉ sáu module được đối chiếu sâu với hợp đồng nguồn, theo phạm vi vòng trước.
- Không chạy generator, scaffold, diagram hay dựng web; vì vậy không kiểm tính tái lập của quá trình sinh.
- Không có đề giảng viên, kết quả chạy lab, rubric đã dùng hoặc biên bản phê duyệt của owner; không thể xác nhận ngưỡng runtime và chất lượng giảng dạy thực tế.
- Đây là audit độc lập, chưa phải phê duyệt của owner.
