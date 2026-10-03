# Knowledge Note Style Standard

## Mục đích

Quy tắc xuống dòng và công thức áp dụng cho toàn bộ Markdown trong `Docs/Second-Brain` và `Material/DE/Reference/Library/Knowledge-Notes`. Yêu cầu về chiều sâu áp dụng trực tiếp cho các knowledge note trong `2_Wiki` và bản đối ứng trong kho Reference. Note phải trình bày lại kiến thức đủ để học và tra cứu, không viết theo dạng tóm tắt chương, danh sách khẩu hiệu hoặc bản nháp bài giảng.

## Đơn vị trình bày

- Một đoạn văn xuôi là một dòng vật lý trong Markdown. Renderer tự ngắt dòng theo chiều rộng màn hình.
- Một đoạn chỉ triển khai một luận điểm chính. Chuyển luận điểm thì tạo đoạn mới bằng một dòng trống.
- Một bullet hoặc numbered item nằm trên một dòng. Không dùng bullet để thay cho phần giải thích quan hệ nhân quả.
- Bảng dùng cho so sánh theo trường cố định. Không đưa đoạn văn dài vào bảng.
- Code, cấu hình, output, Mermaid và công thức khối giữ cấu trúc nhiều dòng vốn có.

## Công thức

- Công thức inline: `$x = y + z$`.
- Công thức khối:

  ```text
  $$
  T \approx 2RTT + T_{transmit}
  $$
  ```

- Không dùng `\[` và `\]` vì renderer Obsidian hiện tại không nhận ổn định.
- Mọi ký hiệu phải được định nghĩa ngay trước hoặc sau công thức. Nêu đơn vị và giả định khi chúng ảnh hưởng cách dùng.
- Không đặt lệnh LaTeX như `\frac`, `\approx`, `\lambda` ngoài math delimiter.

## Chiều sâu bắt buộc

Tùy chủ đề, note cần bao phủ các thành phần sau bằng văn xuôi có liên kết logic:

1. Câu hỏi hoặc vấn đề trung tâm.
2. Định nghĩa và ranh giới thuật ngữ.
3. Mô hình hoặc cơ chế vận hành từng bước.
4. Điều kiện, invariant và giả định.
5. Ví dụ xuyên suốt hoặc tình huống có số liệu khi phù hợp.
6. So sánh với phương án dễ nhầm.
7. Failure modes, phản ví dụ và giới hạn.
8. Cách quan sát, kiểm chứng hoặc áp dụng.
9. Quan hệ với note trước và sau.
10. Reference có locator và qualifier.

Mỗi knowledge note phải có đúng một mục `## Source coverage`, một mục `## Key takeaways` và một mục `## Reference`. Ba tiêu đề này không đánh số để giữ tên mục ổn định giữa các note.

`## Source coverage` không phải danh sách tài liệu. Đây là ma trận kiểm soát độ phủ gồm: lát nguồn và locator, kiến thức phải giữ, vị trí đã trình bày trong note, trạng thái bao phủ, phần loại khỏi phạm vi và lý do. Mọi `source_id` trong frontmatter phải xuất hiện trong ma trận. Không được dùng số chữ, số nguồn hoặc câu “đã đọc” để thay cho đối chiếu này.

“Không bỏ sót kiến thức từ source” được hiểu trong phạm vi lát nguồn đã công bố cho note. Không mở rộng một note thành bản sao toàn bộ sách; không âm thầm bỏ một phần liên quan chỉ vì khó diễn giải. Nội dung ngoài phạm vi phải được ghi là giới hạn hoặc nguồn cần bổ sung.

Độ dài không phải tiêu chí độc lập. Note không đạt nếu dài nhưng chỉ lặp ý, hoặc ngắn đến mức bỏ qua cơ chế, điều kiện và phản ví dụ cần để sử dụng đúng kiến thức.

## Giọng văn

- Dùng tiếng Việt khoa học, câu trực tiếp, thuật ngữ nhất quán.
- Giữ tên API, protocol, pattern và identifier bằng tiếng Anh khi dịch làm giảm khả năng tra cứu.
- Không dùng khẩu hiệu, câu kết sáo rỗng, từ bơm phồng hoặc cấu trúc đối lập trang trí.
- Không gán ý kiến tổng hợp cho tác giả. Dùng callout `source-fact`, `synthesis`, `inference` và `uncertainty` đúng nghĩa.
- Không tuyên bố đã chạy lab, benchmark hoặc kiểm chứng production nếu chưa có bằng chứng thực thi.

## Kiểm tra bắt buộc

Chạy formatter ở chế độ kiểm tra trước khi đồng bộ vault:

```bash
python3 Tools/Curriculum/Build/format_knowledge_notes.py --check
```
