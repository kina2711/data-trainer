# -*- coding: utf-8 -*-
"""DE M10 — The life of a query: database internals."""

M10 = ("The Life of a Query - Database Internals", 108, 121, """| | |
|---|---|
| **Objective cấp module** | Truy một truy vấn chậm hoặc một sự cố cơ sở dữ liệu về đúng chặng trong vòng đời truy vấn, bằng kế hoạch thực thi và số đo chứ bằng phỏng đoán |
| **Tiền đề** | M9 · M2 |
| **Exit criterion** | Chẩn đoán sáu ca dựng sẵn về đúng chặng, và diễn tập một lần khôi phục từ bản sao lưu có đo thời điểm phục hồi và thời lượng phục hồi |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 3 |
| **Chế độ hỏng** | Tối ưu bằng cách sửa cú pháp truy vấn hoặc thêm chỉ mục theo cảm tính, vì chưa bao giờ đọc kế hoạch thực thi |""",
"""Module lấy một sơ đồ làm trục và mười bốn bài đi dọc nó:

```text
Ứng dụng khách → xác thực và nhóm kết nối → phân tích cú pháp → kiểm tra và gắn tham số
→ viết lại → bộ tối ưu hoá (thống kê, ước lượng bản số, chi phí) → kế hoạch vật lý
→ bộ thực thi (quét, lọc, kết, gộp, sắp) → bộ đệm ↔ đĩa
→ trả kết quả qua mạng → xác nhận hoặc hoàn tác → nhật ký ghi trước và điểm kiểm tra
→ bản sao và sao lưu
```

Mọi khẳng định về hiệu năng trong module phải kèm kế hoạch thực thi và số đo, không kèm lập luận về cú pháp.""")

L10 = [
(108,"The life of a query - twelve stages end to end","LT","Module 10: M9 · M2",
"Đi dọc sơ đồ một lần, mỗi chặng nêu việc nó làm và chế độ hỏng đặc trưng của nó. Chặng kết nối: hết kết nối, nối lại lesson 36. Phân tích cú pháp: lỗi cú pháp, và chi phí phân tích lại khi truy vấn không tham số hoá nên mỗi lần là một chuỗi khác. Gắn tham số: truy vấn chuẩn bị sẵn dùng lại kế hoạch, và trường hợp kế hoạch dùng lại không còn tối ưu khi tham số đổi phân bố. Viết lại: bộ tối ưu hoá biến đổi truy vấn theo luật tương đương của đại số quan hệ ở lesson 92, nên truy vấn viết cách nào thường không quan trọng bằng dữ liệu trông thế nào. Bộ tối ưu hoá chọn kế hoạch theo chi phí ước lượng, và mọi sai lầm của nó bắt nguồn từ ước lượng bản số sai. Bộ thực thi và các toán tử vật lý. Bộ đệm và đĩa. Trả kết quả và chi phí mạng. Xác nhận, nhật ký ghi trước, điểm kiểm tra, bản sao. Phân biệt kế hoạch logic với kế hoạch vật lý.",
"Định vị một sự cố cơ sở dữ liệu về đúng chặng trong mười hai chặng, và nêu phép đo xác nhận cho chặng đó.",
"Tầng *phân tích*. Objective là phân loại có bằng chứng, đặt nền cho mười ba bài sau. Kiểm bằng sáu mô tả sự cố; đạt khi định vị đúng ít nhất năm và mỗi lần nêu được một phép đo xác nhận thực hiện được, không chấp nhận phép đo chung chung như xem nhật ký.",
"Vẽ lại sơ đồ mười hai chặng từ trí nhớ. Nhận sáu mô tả sự cố: hết kết nối, truy vấn chậm dần theo thời gian, một truy vấn chậm hẳn sau khi nạp dữ liệu mới, kết quả trả về chậm dù truy vấn nhanh, ghi chậm sau khi thêm chỉ mục, và cơ sở dữ liệu đứng sau khi mất điện. Định vị từng cái và nêu phép đo.",
"Kết luận truy vấn chậm mà chưa loại trừ chặng mạng và chặng kết nối · quy mọi thứ về thiếu chỉ mục · dùng xem nhật ký làm phép đo.",
"Định vị đúng ít nhất năm trên sáu sự cố, mỗi lần kèm một phép đo xác nhận thực hiện được."),

(109,"Pages, tuples and how a row is stored","LT","Lesson 108",
"Trang là đơn vị đọc ghi của cơ sở dữ liệu, thường vài ki lô byte, và mọi thao tác quy về đọc ghi trang chứ không quy về đọc ghi dòng. Cấu trúc một trang: phần đầu, mảng con trỏ dòng, vùng trống, và dữ liệu dòng mọc ngược từ cuối. Hệ quả: cập nhật một dòng nhỏ vẫn phải ghi cả trang, nối lại khuếch đại ghi ở lesson 16. Bố trí một dòng: phần đầu dòng, bản đồ giá trị rỗng, rồi các cột theo thứ tự lưu. Thứ tự cột ảnh hưởng dung lượng do căn lề, nên sắp cột theo độ rộng giảm dần tiết kiệm được vài phần trăm trên bảng lớn. Giá trị quá lớn không vừa trang được lưu ngoài dòng, và chi phí đọc thêm khi truy cập chúng. Hệ số lấp đầy trang và chỗ trống để lại cho cập nhật tại chỗ. Bảng phình do dòng chết chưa được thu hồi, chuẩn bị cho lesson 118. Lưu theo dòng so với lưu theo cột, nối lại lesson 41 và 70.",
"Ước lượng số trang một bảng chiếm từ lược đồ và số dòng, rồi đo thật và giải thích chênh lệch.",
"Tầng *áp dụng*. Objective gồm ước lượng và đối chứng bằng số đo hệ thống. Đạt khi ước lượng sai trong phạm vi 30% so với số trang thật, và khi người học chỉ ra được nguồn gốc của phần chênh, thường là căn lề và phần đầu trang.",
"Tạo ba bảng 5 triệu dòng cùng dữ liệu nhưng khác thứ tự cột. Ước lượng số trang từ lược đồ. Đo số trang thật bằng khung nhìn hệ thống. So ba bảng và giải thích chênh lệch bằng căn lề. Cập nhật 10% số dòng và đo lại kích thước.",
"Ước lượng dung lượng bằng tổng độ rộng cột nhân số dòng · giả định cập nhật một cột chỉ ghi một cột · bỏ qua giá trị lưu ngoài dòng khi tính.",
"Ước lượng sai trong phạm vi 30% so với số trang thật, và nguồn gốc phần chênh được chỉ ra."),

(110,"The buffer pool and the two-tier cache problem","TH","Lesson 109",
"Bộ đệm giữ trang vừa dùng trong bộ nhớ, và tỉ lệ trúng là chỉ số quan trọng nhất của nó. Chính sách thay thế và vì sao một lần quét toàn bảng lớn có thể đẩy mọi trang nóng ra ngoài, hiện tượng gọi là làm ô nhiễm bộ đệm, cùng cách các hệ quản trị chống lại nó. Trang bẩn và thời điểm ghi xuống đĩa, chuẩn bị cho điểm kiểm tra ở lesson 118. Hai tầng đệm chồng nhau: bộ đệm của cơ sở dữ liệu và bộ đệm trang của hệ điều hành ở lesson 22, nên cùng một trang có thể nằm hai nơi và tốn gấp đôi bộ nhớ. Hệ quả cấu hình: đặt bộ đệm bằng toàn bộ RAM là sai, phải chừa cho hệ điều hành và cho bộ nhớ làm việc của truy vấn. Bộ nhớ làm việc cho phép sắp và phép kết, và điều gì xảy ra khi không đủ: tràn ra đĩa, đây chính là vế thứ nhất của tiêu chí ra M2. Đọc tỉ lệ trúng và số trang đọc từ đĩa trên hệ thống đang chạy.",
"Đo tỉ lệ trúng bộ đệm trước và sau một lần quét toàn bảng lớn, và chỉ ra ngưỡng bộ nhớ làm việc mà phép sắp bắt đầu tràn ra đĩa.",
"Tầng *phân tích*. Objective đòi nối số đo với cơ chế và tìm một ngưỡng. Đạt khi có số đo tỉ lệ trúng ở ba thời điểm cho thấy hiện tượng ô nhiễm, và khi ngưỡng tràn đĩa được xác định bằng thực nghiệm ở ít nhất bốn giá trị bộ nhớ làm việc.",
"Làm nóng bộ đệm bằng tải truy vấn thường. Đo tỉ lệ trúng. Quét toàn bảng lớn hơn bộ đệm. Đo lại ngay sau và sau khi chạy tải thường 10 phút. Chạy một phép sắp ở bốn giá trị bộ nhớ làm việc, tìm ngưỡng tràn đĩa bằng kế hoạch thực thi.",
"Đặt bộ đệm bằng toàn bộ RAM · đọc tỉ lệ trúng ngay sau khi khởi động rồi kết luận · bỏ qua bộ nhớ làm việc khi tính dung lượng.",
"Số đo tỉ lệ trúng ở ba thời điểm cho thấy ô nhiễm bộ đệm, và ngưỡng tràn đĩa xác định được ở bốn giá trị."),

(111,"Index structures - B-tree, LSM and inverted","LT","Lesson 110",
"Cây B cộng và ba tính chất làm nó thành chỉ mục mặc định: chiều cao thấp nên ít lần chạm đĩa, lá nối nhau nên quét khoảng rẻ, và cân bằng tự động, nối lại lesson 46. Chỉ mục phủ và quét chỉ mục thuần khi mọi cột cần đều nằm trong chỉ mục. Chỉ mục phức hợp và quy tắc tiền tố trái: thứ tự cột quyết định truy vấn nào dùng được, nên một chỉ mục ba cột không thay thế được ba chỉ mục một cột. Chọn lọc của cột và vì sao chỉ mục trên cột ít giá trị phân biệt thường vô dụng. Cây trộn có cấu trúc nhật ký: ghi vào bộ nhớ rồi xả ra đĩa theo tầng, tối ưu cho ghi nhiều, đổi khuếch đại ghi thấp lấy khuếch đại đọc cao, nối tới ClickHouse ở M16. Chỉ mục ngược cho tìm kiếm toàn văn, nối tới Elasticsearch ở M17. Chi phí ghi của chỉ mục: mỗi chỉ mục thêm một cây phải cập nhật, đây là vế thứ hai của tiêu chí ra M2.",
"Chọn cấu trúc chỉ mục và thứ tự cột cho năm mẫu truy vấn, và dự đoán truy vấn nào dùng được chỉ mục nào trước khi chạy.",
"Tầng *đánh giá*. Objective đòi thiết kế chỉ mục có đánh đổi đọc ghi, không có đáp án chung. Đạt khi dự đoán đúng ít nhất bốn trên năm truy vấn về việc chỉ mục có được dùng không, xác nhận bằng kế hoạch thực thi, và khi chi phí ghi được đo trước sau khi thêm chỉ mục.",
"Tạo bảng 10 triệu dòng. Thiết kế chỉ mục cho năm mẫu truy vấn. Dự đoán truy vấn nào dùng chỉ mục nào, rồi đọc kế hoạch thực thi để xác nhận. Đo thời gian chèn 1 triệu dòng khi có 0, 2, 5 chỉ mục. Thử một chỉ mục trên cột giới tính và quan sát nó không được dùng.",
"Tạo chỉ mục cho mọi cột trong mệnh đề lọc · đảo thứ tự cột trong chỉ mục phức hợp · thêm chỉ mục mà không đo chi phí ghi.",
"Dự đoán đúng ít nhất bốn trên năm truy vấn xác nhận bằng kế hoạch, và có số đo chi phí ghi theo số chỉ mục."),

(112,"Statistics, cardinality estimation and why plans go wrong","TH","Lesson 111",
"Bộ tối ưu hoá chọn kế hoạch theo chi phí ước lượng, và chi phí ước lượng dựa trên ước lượng số dòng, nên mọi kế hoạch tồi đều truy về một ước lượng bản số sai. Thống kê gồm gì: số dòng, số giá trị phân biệt, biểu đồ phân bố, tỉ lệ giá trị rỗng, và các giá trị xuất hiện nhiều nhất. Thu thập thống kê tự động và điều kiện kích hoạt, cùng lý do thống kê lạc hậu sau một lần nạp lớn. Bốn nguyên nhân ước lượng sai: thống kê cũ, dữ liệu lệch mà biểu đồ không đủ chi tiết, tương quan giữa hai cột mà bộ tối ưu hoá giả định độc lập, và hàm bọc quanh cột làm mất thống kê. Nguyên nhân thứ ba là nguyên nhân khó nhất: lọc theo tỉnh và theo quận là hai điều kiện tương quan, nhân hai chọn lọc ra con số nhỏ hơn thực tế nhiều lần. So ước lượng với số dòng thật trong kế hoạch là cách chẩn đoán trực tiếp nhất.",
"So ước lượng số dòng với số dòng thật trong kế hoạch thực thi, và truy sai lệch lớn về đúng một trong bốn nguyên nhân.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân có cùng triệu chứng. Kiểm bằng bốn ca dựng sẵn; đạt khi truy đúng ít nhất ba, mỗi lần dẫn được con số ước lượng và con số thật từ kế hoạch.",
"Dựng bốn ca: nạp 5 triệu dòng rồi chạy ngay khi thống kê chưa cập nhật, bảng có một giá trị chiếm 80%, hai cột tương quan chặt, và mệnh đề lọc bọc hàm quanh cột. Với mỗi ca, đọc kế hoạch, so ước lượng với thật, truy nguyên. Cập nhật thống kê và đo lại.",
"Ép bộ tối ưu hoá dùng kế hoạch mình muốn thay vì sửa thống kê · đọc chi phí ước lượng mà không đọc số dòng · cập nhật thống kê rồi không đo lại.",
"Truy đúng ít nhất ba trên bốn nguyên nhân, mỗi lần dẫn được ước lượng và số thật từ kế hoạch."),

(113,"Reading an execution plan - logical against physical","TH","Lesson 112",
"Kế hoạch logic nói làm gì, kế hoạch vật lý nói làm thế nào, và chỉ cái sau mới nói được truy vấn sẽ chạy bao lâu. Đọc kế hoạch từ trong ra ngoài và từ dưới lên. Bốn nhóm toán tử và ý nghĩa vận hành: truy cập dữ liệu gồm quét toàn bảng, quét chỉ mục, tra chỉ mục rồi lấy dòng; kết; gộp; và sắp. Quét toàn bảng không phải luôn xấu: khi lấy phần lớn bảng thì nó rẻ hơn tra chỉ mục từng dòng, và ngưỡng đó tính được. Chế độ phân tích thật so với chế độ chỉ ước lượng: cái đầu chạy truy vấn nên cho số dòng thật và thời gian thật, cái sau không chạy nên chỉ có ước lượng. Bốn con số phải đọc trong mỗi nút: số dòng ước lượng, số dòng thật, số lần lặp, và thời gian. Số lần lặp nhân thời gian là chi phí thật của nút, và bỏ qua nó là lỗi đọc kế hoạch phổ biến nhất. Bộ đệm chia sẻ đọc được và đọc từ đĩa. Chỗ tràn ra đĩa hiện trong kế hoạch.",
"Đọc một kế hoạch thực thi và chỉ ra nút tốn nhất cùng lý do, phân biệt được nút chậm với nút chạy nhiều lần.",
"Tầng *phân tích*. Objective đòi định vị chi phí thật, và bẫy chính là nhầm thời gian một lần với tổng chi phí. Kiểm bằng bốn kế hoạch, trong đó hai kế hoạch có nút tốn nhất là nút chạy nhiều lần chứ không phải nút chậm nhất. Đạt khi chỉ đúng cả bốn.",
"Chạy bốn truy vấn ở chế độ phân tích thật. Với mỗi kế hoạch, lập bảng bốn con số cho từng nút, tính chi phí thật, chỉ nút tốn nhất. Hai kế hoạch có nút chạy 10.000 lần mỗi lần 0,1 mili giây. Xác định ngưỡng mà quét toàn bảng rẻ hơn tra chỉ mục.",
"Đọc kế hoạch ước lượng rồi kết luận về thời gian thật · chọn nút có thời gian một lần lớn nhất làm nút tốn nhất · coi quét toàn bảng luôn là lỗi.",
"Chỉ đúng nút tốn nhất ở cả bốn kế hoạch, gồm hai ca nút tốn nhất là nút chạy nhiều lần."),

(114,"Join execution - which algorithm the planner picks and why","TH","Lesson 113",
"Ba thuật toán kết ở lesson 44 xuất hiện trong kế hoạch dưới tên toán tử vật lý, và bài này nối lý thuyết đó với thực tế. Điều kiện bộ tối ưu hoá chọn từng cái: vòng lặp lồng khi bảng ngoài nhỏ và bảng trong có chỉ mục, kết băm khi không có chỉ mục phù hợp và bảng dựng vừa bộ nhớ làm việc, kết trộn sắp khi cả hai bên đã sắp theo khoá kết. Thứ tự kết khi có nhiều bảng: số cách sắp xếp tăng theo giai thừa nên bộ tối ưu hoá cắt tỉa không gian tìm kiếm, và với truy vấn nhiều bảng nó có thể bỏ lỡ kế hoạch tốt nhất. Kết băm tràn ra đĩa khi bảng dựng lớn hơn bộ nhớ làm việc, nối lại lesson 110: đây là câu trả lời đầy đủ cho vế thứ nhất của tiêu chí ra M2. Lệch khoá kết làm một nhóm băm nhận phần lớn dòng, nối lại lesson 48. Kết lồng nhau trên bảng lớn là triệu chứng của ước lượng bản số sai chứ không phải lựa chọn của bộ tối ưu hoá.",
"Giải thích vì sao bộ tối ưu hoá chọn một thuật toán kết cụ thể trong một kế hoạch, và làm nó đổi lựa chọn bằng cách đổi một điều kiện.",
"Tầng *phân tích*. Objective đòi hiểu quy luật chọn đủ để tác động vào nó có chủ đích. Đạt khi giải thích đúng lựa chọn ở ba kế hoạch, và khi làm bộ tối ưu hoá đổi sang thuật toán khác bằng cách đổi đúng một điều kiện, ba lần với ba điều kiện khác nhau.",
"Dựng ba truy vấn kết cho ra ba thuật toán khác nhau. Giải thích từng lựa chọn. Với mỗi cái, đổi đúng một điều kiện để bộ tối ưu hoá chọn thuật toán khác: thêm chỉ mục, đổi bộ nhớ làm việc, và sắp sẵn dữ liệu. Ép kết băm tràn ra đĩa và quan sát trong kế hoạch.",
"Ép thuật toán kết bằng gợi ý thay vì sửa nguyên nhân · tăng bộ nhớ làm việc toàn cục để chữa một truy vấn · bỏ qua lệch khoá khi kết băm chậm bất thường.",
"Giải thích đúng lựa chọn ở ba kế hoạch, và ba lần làm bộ tối ưu hoá đổi thuật toán bằng một điều kiện."),

(115,"Partition pruning and predicate pushdown","TH","Lesson 114",
"Phân vùng chia một bảng logic thành nhiều bảng vật lý theo một khoá, và lợi ích chính không phải tốc độ đọc mà là cắt tỉa: bộ tối ưu hoá bỏ qua cả phân vùng không thoả điều kiện, nên chi phí tỉ lệ với dữ liệu cần chứ không với dữ liệu có. Ba kiểu phân vùng và mẫu truy cập hợp với từng kiểu, nối lại lesson 48. Điều kiện cắt tỉa hoạt động: mệnh đề lọc phải nằm trên chính khoá phân vùng và không bị bọc hàm, nối lại lesson 96, nên phân vùng theo ngày mà lọc theo hàm trích tháng thì cắt tỉa vô hiệu. Đẩy vị từ xuống: đưa điều kiện lọc xuống càng sớm càng tốt trong cây kế hoạch để giảm dòng đi lên trên. Hai chỗ nó không đẩy được: qua hàm cửa sổ và qua một số dạng truy vấn con. Xoá phân vùng cũ bằng thao tác siêu dữ liệu thay vì xoá dòng, nhanh hơn nhiều bậc. Quá nhiều phân vùng làm lập kế hoạch chậm, nên có giới hạn trên hợp lý.",
"Chứng minh cắt tỉa phân vùng có hiệu lực bằng số phân vùng được quét, và tìm một truy vấn làm cắt tỉa vô hiệu rồi sửa.",
"Tầng *phân tích*. Objective đòi chứng minh bằng số đo trong kế hoạch chứ không bằng thời gian. Đạt khi chỉ ra được số phân vùng quét trong kế hoạch cho ba truy vấn, và khi định vị đúng nguyên nhân cắt tỉa vô hiệu rồi sửa cho nó hoạt động trở lại.",
"Tạo bảng phân vùng theo ngày 36 phân vùng, 50 triệu dòng. Chạy ba truy vấn và đọc số phân vùng quét trong kế hoạch. Viết một truy vấn bọc hàm quanh khoá phân vùng, quan sát quét hết, rồi sửa. Xoá một phân vùng bằng thao tác siêu dữ liệu và so thời gian với xoá dòng.",
"Đánh giá cắt tỉa bằng thời gian chạy thay vì bằng số phân vùng quét · bọc hàm quanh khoá phân vùng · tạo phân vùng theo ngày cho bảng giữ 10 năm mà không gộp.",
"Số phân vùng quét đọc được từ kế hoạch cho ba truy vấn, và ca cắt tỉa vô hiệu được định vị và sửa."),

(116,"MVCC, locking and what isolation costs","LT","Lesson 115",
"Điều khiển đồng thời nhiều phiên bản cho người đọc thấy một ảnh chụp nhất quán mà không chặn người ghi, và ngược lại. Cơ chế: mỗi dòng có nhiều phiên bản kèm dấu giao dịch, và mỗi giao dịch thấy phiên bản hợp lệ với ảnh chụp của nó. Hệ quả vận hành quan trọng nhất: cập nhật không sửa tại chỗ mà tạo phiên bản mới, nên bảng phình và cần thu hồi dòng chết, nối lại lesson 109. Giao dịch mở lâu chặn việc thu hồi mọi dòng chết sinh ra sau khi nó bắt đầu, nên một phiên quên đóng làm cả cơ sở dữ liệu phình. Khoá ở ba mức: hàng, trang, bảng; và leo thang khoá khi số khoá hàng vượt ngưỡng. Khoá chia sẻ và khoá độc quyền, ma trận tương thích. Chờ khoá và hàng đợi chờ. Bốn mức cô lập ở lesson 105 cài đặt bằng gì: mức thấp dùng ảnh chụp, mức cao dùng khoá hoặc phát hiện xung đột rồi huỷ. Cô lập cao đổi bằng tỉ lệ huỷ chứ không bằng thời gian chờ.",
"Giải thích vì sao một giao dịch mở lâu làm cơ sở dữ liệu phình, và chỉ ra giao dịch đó bằng khung nhìn hệ thống.",
"Tầng *hiểu*. Bài lý thuyết nối cơ chế với một triệu chứng vận hành cụ thể. Đạt khi giải thích đúng chuỗi nhân quả từ giao dịch mở tới phình bảng, và khi định vị được giao dịch cũ nhất đang mở cùng thời lượng của nó trên một hệ thống có tải.",
"Mở một giao dịch và để đó. Chạy tải cập nhật 30 phút. Đo kích thước bảng và số dòng chết theo thời gian. Định vị giao dịch cũ nhất bằng khung nhìn hệ thống. Đóng nó, chạy thu hồi, đo lại. Quan sát leo thang khoá khi cập nhật số dòng lớn trong một giao dịch.",
"Để phiên mở trong công cụ khách rồi đi ăn trưa · tăng ngưỡng leo thang khoá để chữa tranh chấp · kết luận phình bảng do dữ liệu tăng mà không xem dòng chết.",
"Giải thích đúng chuỗi nhân quả, và định vị được giao dịch cũ nhất đang mở cùng thời lượng."),

(117,"Deadlocks - detection, victims and prevention","TH","Lesson 116",
"Bế tắc trong cơ sở dữ liệu là trường hợp cụ thể của bế tắc ở lesson 53, với bốn điều kiện giống hệt. Khác biệt: hệ quản trị có bộ phát hiện chạy định kỳ, tìm vòng chờ trong đồ thị chờ khoá, rồi chọn một giao dịch làm nạn nhân và huỷ nó. Tiêu chí chọn nạn nhân khác nhau giữa các hệ, thường là giao dịch làm ít việc nhất. Hệ quả cho ứng dụng: giao dịch bị huỷ là chuyện bình thường phải xử lý bằng thử lại, không phải lỗi hệ thống, nên mã ghi phải có vòng thử lại; nhưng thử lại chỉ đúng khi giao dịch bất biến, nối lại lesson 106. Ba nguyên nhân bế tắc phổ biến trong công việc dữ liệu: cập nhật nhiều dòng theo thứ tự khác nhau ở hai tiến trình, nâng cấp khoá chia sẻ thành độc quyền, và khoá khoảng khi chèn. Phòng ngừa: quy định thứ tự cập nhật toàn cục, giữ giao dịch ngắn, và gom cập nhật thành một câu lệnh. Đọc nhật ký bế tắc để biết hai giao dịch đang chờ khoá nào.",
"Gây bế tắc cơ sở dữ liệu có chủ đích, đọc nhật ký bế tắc để xác định hai khoá gây vòng chờ, và phòng ngừa bằng thứ tự cập nhật.",
"Tầng *phân tích*. Objective gồm chẩn đoán từ nhật ký và một bản sửa có nguyên tắc. Đạt khi xác định đúng hai khoá gây vòng chờ từ nhật ký, và khi bản sửa chạy 10.000 giao dịch song song không sinh bế tắc nào. Sửa bằng cách chỉ thêm thử lại thì chỉ đạt một nửa.",
"Dựng hai tiến trình cập nhật hai bảng theo thứ tự ngược nhau. Chạy tới khi có bế tắc. Bật nhật ký bế tắc, đọc, xác định hai khoá. Sửa bằng thứ tự cập nhật toàn cục, chạy 10.000 giao dịch song song. Thêm vòng thử lại cho phần còn lại và xác nhận nó bất biến.",
"Coi giao dịch bị huỷ là lỗi hệ thống · chỉ thêm thử lại mà không phá vòng chờ · thử lại một giao dịch không bất biến.",
"Xác định đúng hai khoá gây vòng chờ từ nhật ký, và bản sửa chạy 10.000 giao dịch song song không bế tắc."),

(118,"Write-ahead log, checkpoints and crash recovery","TH","Lesson 117",
"Nguyên tắc ghi trước: mọi thay đổi ghi vào nhật ký và đồng bộ xuống đĩa trước khi trang dữ liệu được ghi, nên sau sự cố có đủ thông tin để dựng lại. Đây là cách cơ sở dữ liệu đạt được tính bền vững mà không phải đồng bộ mọi trang dữ liệu ở mỗi lần xác nhận, nối lại lesson 16. Nội dung một bản ghi nhật ký và số thứ tự. Điểm kiểm tra: ghi mọi trang bẩn xuống đĩa và đánh dấu một mốc, để phục hồi chỉ phải chạy lại từ mốc đó thay vì từ đầu. Đánh đổi: điểm kiểm tra thưa thì phục hồi lâu, dày thì tốn vào ra lúc chạy bình thường, và đây là tham số phải chọn theo thời lượng phục hồi mục tiêu. Ba pha phục hồi sau sự cố: phân tích, chạy lại, hoàn tác. Nhật ký cũng là nguồn cho bản sao ở lesson 120 và cho bắt thay đổi dữ liệu ở chặng 6. Nhật ký đầy đĩa làm cơ sở dữ liệu dừng ghi, một sự cố vận hành phổ biến.",
"Đo thời gian phục hồi sau sự cố ở ba cấu hình điểm kiểm tra, và giải thích đánh đổi bằng số đo vào ra lúc chạy bình thường.",
"Tầng *đánh giá*. Objective đòi chọn một tham số có đánh đổi hai chiều và biện minh bằng số. Đạt khi có bảng ba cấu hình kèm cả thời gian phục hồi lẫn vào ra lúc chạy bình thường, và khi lựa chọn cuối dẫn được về một thời lượng phục hồi mục tiêu cho trước.",
"Chạy tải ghi liên tục. Với ba khoảng điểm kiểm tra khác nhau, đo vào ra lúc chạy bình thường, rồi ngắt điện máy ảo và đo thời gian phục hồi. Lập bảng. Chọn cấu hình cho thời lượng phục hồi mục tiêu 2 phút. Làm đầy phân vùng nhật ký và quan sát hệ thống dừng ghi.",
"Đặt điểm kiểm tra thưa để giảm vào ra mà không đo thời gian phục hồi · để nhật ký chung phân vùng với dữ liệu · tin rằng xác nhận thành công nghĩa là trang dữ liệu đã xuống đĩa.",
"Bảng ba cấu hình có cả thời gian phục hồi lẫn vào ra, và lựa chọn cuối dẫn được về thời lượng mục tiêu."),

(119,"Backup, point-in-time restore and measuring RPO and RTO","TH","Lesson 118",
"Hai đại lượng quyết định thiết kế sao lưu và chúng thường bị nhầm: điểm phục hồi là lượng dữ liệu chấp nhận mất tính bằng thời gian, thời lượng phục hồi là thời gian chấp nhận hệ thống ngừng. Hai con số này do nghiệp vụ quyết định chứ không do kỹ thuật, và mọi lựa chọn kỹ thuật suy ra từ chúng. Sao lưu logic so với sao lưu vật lý: cái đầu di chuyển được giữa phiên bản, cái sau nhanh hơn nhiều trên dữ liệu lớn. Sao lưu toàn phần, vi sai và tăng dần. Phục hồi tới một thời điểm bằng bản sao lưu nền cộng nhật ký ghi trước từ lesson 118, và đây là lý do phải giữ nhật ký chứ không chỉ giữ bản sao lưu. Nguyên tắc duy nhất về sao lưu: một bản sao lưu chưa phục hồi thử không phải là bản sao lưu. Diễn tập phục hồi định kỳ và đo thời gian thật. Ba lỗi làm bản sao lưu vô dụng: cùng đĩa với dữ liệu, không mã hoá, và không ai biết mật khẩu giải mã.",
"Phục hồi cơ sở dữ liệu tới một thời điểm cụ thể trong quá khứ, và đo điểm phục hồi cùng thời lượng phục hồi đạt được thật.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm bằng diễn tập thật, không bằng lập luận. Đạt khi phục hồi tới đúng thời điểm chỉ định và dữ liệu khớp ảnh chụp đối chứng tại thời điểm đó, và khi nộp hai con số đo được chứ không phải hai con số cam kết.",
"Chạy tải ghi và chụp ảnh đối chứng ở ba mốc thời gian. Lấy sao lưu nền, giữ nhật ký. Xoá cơ sở dữ liệu. Phục hồi tới mốc thứ hai. So từng dòng với ảnh chụp mốc đó. Đo thời gian từ lúc bắt đầu tới lúc phục vụ được. Lặp lại một lần nữa và so hai lần đo.",
"Lấy sao lưu mà không bao giờ phục hồi thử · để bản sao lưu cùng đĩa với dữ liệu · báo cáo điểm phục hồi cam kết thay vì đo được.",
"Dữ liệu sau phục hồi khớp ảnh chụp đối chứng tại mốc chỉ định, và hai con số là số đo được từ diễn tập."),

(120,"Replication, replica lag and read-after-write","TH","Lesson 119",
"Bản sao vật lý truyền nhật ký ghi trước từ lesson 118, bản sao logic truyền thay đổi ở mức dòng; cái đầu giống hệt bản chính, cái sau chọn được bảng và chuyển được giữa phiên bản, và nó chính là nền của bắt thay đổi dữ liệu ở chặng 6. Đồng bộ so với bất đồng bộ: đồng bộ không mất dữ liệu khi bản chính chết nhưng mỗi lần xác nhận phải chờ bản sao, bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu bằng đúng độ trễ. Độ trễ bản sao: nguyên nhân, cách đo, và vì sao nó tăng vọt khi có giao dịch ghi lớn. Đọc sau ghi: ứng dụng ghi vào bản chính rồi đọc ngay từ bản sao có thể không thấy dữ liệu vừa ghi, một lỗi khó tái hiện vì nó phụ thuộc thời điểm. Ba cách xử lý và đánh đổi. Chuyển đổi dự phòng thủ công và tự động, cùng rủi ro hai bản cùng nhận ghi. Tách tải đọc sang bản sao và điều kiện an toàn.",
"Đo độ trễ bản sao dưới ba mức tải và tái hiện được lỗi đọc sau ghi, rồi sửa bằng một trong ba cách.",
"Tầng *phân tích*. Objective gồm đo và tái hiện một lỗi phụ thuộc thời điểm, việc khó hơn đọc tài liệu. Đạt khi tái hiện được lỗi đọc sau ghi ít nhất 5 lần trong 100 lần thử, và khi bản sửa cho 0 lần trong 1.000 lần thử.",
"Dựng bản chính và một bản sao bất đồng bộ. Đo độ trễ ở ba mức tải ghi. Chạy một giao dịch ghi lớn và quan sát độ trễ tăng vọt. Viết kịch bản ghi rồi đọc ngay từ bản sao, chạy 100 lần, đếm số lần không thấy dữ liệu. Sửa và chạy 1.000 lần.",
"Tách tải đọc sang bản sao mà không xét đọc sau ghi · dùng bản sao bất đồng bộ khi nghiệp vụ không chấp nhận mất dữ liệu · đo độ trễ lúc không có tải.",
"Tái hiện lỗi đọc sau ghi ít nhất 5 lần trong 100 thử, và bản sửa cho 0 lần trong 1.000 thử."),

(121,"Schema migrations without downtime","TH","Lesson 120",
"Thay đổi lược đồ trên bảng lớn đang phục vụ là thao tác rủi ro nhất trong vận hành cơ sở dữ liệu, vì một số thao tác giữ khoá bảng và chặn mọi truy cập. Phân loại thao tác theo mức khoá: thao tác chỉ đổi siêu dữ liệu chạy tức thì, thao tác phải viết lại bảng mất thời gian tỉ lệ kích thước, và thao tác giữ khoá độc quyền chặn cả đọc. Cùng một lệnh có thể rơi vào nhóm khác nhau tuỳ phiên bản, nên phải kiểm trên bản sao trước. Tạo chỉ mục không chặn ghi và chi phí kèm theo. Mẫu mở rộng rồi thu hẹp cho thay đổi phá vỡ: thêm cột mới, ghi cả hai, chuyển dữ liệu nền, chuyển đọc, rồi mới bỏ cột cũ; bốn bước này triển khai riêng và mỗi bước quay lui được. Thời gian chờ khoá cho lệnh đổi lược đồ để nó thất bại thay vì chặn cả hệ thống. Quay lui một di trú đã chạy: mã quay lui được còn dữ liệu thì không, nối lại lesson 89.",
"Thực hiện một thay đổi lược đồ phá vỡ trên bảng 50 triệu dòng đang có tải, không gây ngừng phục vụ, theo mẫu mở rộng rồi thu hẹp.",
"Tầng *sáng tạo*. Objective là thiết kế một quy trình nhiều bước dưới ràng buộc không ngừng phục vụ, không phải chạy một lệnh. Đạt khi tải đọc ghi chạy suốt quá trình không có lỗi nào và độ trễ phân vị 95 không vượt hai lần mức nền, và khi mỗi trong bốn bước quay lui được độc lập.",
"Bảng 50 triệu dòng có tải đọc ghi liên tục. Đổi kiểu một cột từ số nguyên sang chuỗi theo mẫu bốn bước. Đo lỗi và độ trễ phân vị 95 suốt quá trình. Thử quay lui ở từng bước. Trước đó, chạy lệnh đổi kiểu trực tiếp trên bản sao và đo thời gian khoá.",
"Chạy lệnh đổi lược đồ trực tiếp trên bảng lớn giờ cao điểm · bỏ thời gian chờ khoá nên lệnh chặn cả hệ thống · bỏ cột cũ ở cùng lần triển khai với chuyển đọc.",
"Tải chạy suốt không lỗi và độ trễ phân vị 95 không vượt hai lần mức nền, và cả bốn bước đều quay lui được."),
]
