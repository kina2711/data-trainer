# -*- coding: utf-8 -*-
"""Sinh roadmap từng module cho Analytics Engineer từ roadmap tổng.
Đặc tả bài lấy nguyên văn; phần thêm là đồ thị phụ thuộc trong module."""
import os, re

ROOT = "/home/kina2711/PROJECT/data-trainer"
SRC  = os.path.join(ROOT, "material/analytics-engineer/roadmap/roadmap.md")
CUR  = os.path.join(ROOT, "material/analytics-engineer/curriculum")

EDGES = {
1:[(3,4,"Một trong sáu thành phần của định nghĩa chỉ số là hạt nguồn, khái niệm phát biểu ở lesson 3"),
   (2,4,"Chi phí của chỉ số phân mảnh chỉ thuyết phục sau khi người học tự gánh nó ở tầng 40 view")],
2:[(5,6,"Không có môi trường chạy thì không dự đoán rồi kiểm chứng được số dòng"),
   (6,7,"`NULL` biểu hiện trước hết ở `WHERE`, nên cần thứ tự thực thi logic"),
   (6,8,"Hàm đặt trong `SELECT` và `WHERE`"),
   (7,9,"Thiếu `ELSE` sinh `NULL`; hệ quả chỉ hiểu được sau logic ba trạng thái"),
   (8,9,"Nhánh `CASE` thường chứa biểu thức chuỗi hoặc ngày"),
   (6,10,"Quy tắc `WHERE` lọc trước gộp và `HAVING` lọc sau gộp suy từ thứ tự thực thi logic"),
   (7,10,"`COUNT(cot)`, `SUM`, `AVG` đều bỏ qua `NULL`"),
   (9,10,"`SUM(CASE WHEN ...)` là mẫu gộp có điều kiện"),
   (6,11,"`JOIN` trình bày bằng tích Descartes cộng điều kiện lọc"),
   (11,12,"Nhân bản dòng là hệ quả của bản số quan hệ nêu ở lesson 11"),
   (10,12,"Cách xử lý nhân dòng là gộp trước khi kết"),
   (7,13,"`EXISTS`, `IN` và `JOIN` cho kết quả khác nhau khi tập con chứa `NULL`"),
   (12,13,"CTE đặt tên theo hạt của kết quả kết"),
   (10,14,"`OVER` dạy bằng đối chiếu: `GROUP BY` thu gọn dòng, `OVER` giữ nguyên"),
   (13,14,"Hàm cửa sổ không dùng được trong `WHERE`; đường vòng là CTE"),
   (14,15,"Mệnh đề khung và `LAG`, `LEAD` mở rộng cú pháp `OVER`"),
   (12,16,"Cổng đòi chứng minh số dòng không mất không nhân"),
   (15,16,"Cổng có phần hàm cửa sổ")],
3:[(17,22,"Tải gia tăng chỉ an toàn khi mô hình bất biến khi chạy lại"),
   (20,21,"Ba loại trùng lặp phát hiện bằng mẫu khử trùng có quy tắc chọn dòng"),
   (21,22,"Dữ liệu tới muộn xử lý bằng chính các phép kiểm chất lượng của lesson 21"),
   (21,23,"Bảy truy vấn khảo sát dùng lại bộ kiểm chất lượng sáu chiều"),
   (18,24,"Dự án chấm chéo tính đọc được theo quy ước của lesson 18"),
   (21,24,"Dự án đòi báo cáo chất lượng sáu chiều"),
   (22,24,"Dự án đòi chứng minh tính bất biến khi chạy lại")],
4:[(25,27,"Bước một của Kimball xuất phát từ một lược đồ chuẩn hoá"),
   (26,27,"Lý do lược đồ chiều tồn tại là mẫu truy cập của hệ thống phân tích"),
   (27,28,"Độ đo được xác định ở bước bốn của quy trình"),
   (27,29,"Chiều được xác định ở bước ba của quy trình"),
   (28,30,"Lược đồ sao xếp bảng sự kiện quanh các chiều"),
   (29,30,"Lược đồ sao đòi chiều đã thiết kế xong"),
   (29,31,"Chiều thay đổi chậm là một thuộc tính của bảng chiều"),
   (29,32,"Bảng lịch là một bảng chiều, và chiều vai trò là biến thể của nó"),
   (30,33,"Cổng đòi lược đồ sao đầy đủ"),
   (31,33,"Cổng có phần xác định chiều nào cần Type 2"),
   (32,33,"Cổng đòi dữ liệu mẫu có trục thời gian")],
5:[(34,35,"Git thao tác qua dòng lệnh"),
   (35,36,"Nhánh và gộp dựng trên vòng lặp add, commit, push"),
   (34,37,"Môi trường ảo tạo và kích hoạt bằng dòng lệnh"),
   (37,38,"Đóng gói đòi môi trường tái tạo được trước"),
   (36,38,"Điểm vào duy nhất và README được rà soát qua pull request")],
6:[(39,40,"Cài công cụ sau khi biết nó giải vấn đề gì"),
   (40,41,"Mô hình là tệp trong dự án đã dựng"),
   (41,42,"Kiến trúc phân lớp phát biểu bằng chiều của cạnh `ref()`"),
   (42,43,"Tầng staging là tầng đầu của kiến trúc"),
   (42,44,"Tầng intermediate là tầng giữa"),
   (43,44,"Intermediate đọc từ staging"),
   (44,45,"Mart đọc từ intermediate"),
   (41,46,"Vật chất hoá là cấu hình của mô hình"),
   (41,47,"Tài liệu và đồ thị sinh từ `ref()`"),
   (45,48,"Dự án đòi mart hoàn chỉnh"),
   (46,48,"Dự án đòi chọn vật chất hoá có lý giải"),
   (47,48,"Dự án đòi tài liệu đạt chuẩn người mới đọc hiểu")],
7:[(51,52,"Gói cộng đồng phần lớn là tập hợp macro"),
   (51,53,"Cấu hình theo môi trường dùng ngôn ngữ khuôn mẫu"),
   (49,54,"Chuyển sang gia tăng là một trong bốn đòn bẩy giảm chi phí"),
   (51,55,"Dự án lớn dựa vào macro để không lặp lại"),
   (53,55,"Dự án lớn cần cấu hình tách theo môi trường"),
   (49,56,"Dự án đòi hai mô hình gia tăng có cửa sổ nhìn lại"),
   (50,56,"Dự án đòi một snapshot"),
   (51,56,"Dự án đòi hai macro có kiểm thử"),
   (53,56,"Dự án đòi ba môi trường")],
8:[(57,58,"Kiểm thử nghiệp vụ là tầng bốn trong bốn tầng"),
   (57,59,"Kiểm thử đơn vị phân biệt được với kiểm thử dữ liệu sau khi bốn tầng đã rõ"),
   (57,60,"Giám sát mở rộng kiểm thử từ một lần chạy sang theo thời gian"),
   (57,61,"Kiểm thử lược đồ nguồn là tầng một áp lên biên nhận dữ liệu"),
   (61,62,"Data contract ra đời từ chính nỗi đau nguồn đổi lược đồ"),
   (60,63,"Xử lý sự cố bắt đầu bằng tín hiệu từ giám sát"),
   (62,63,"Thực thi là vế sau của một contract đã đàm phán"),
   (59,64,"Cổng có phần bộ kiểm thử bốn tầng"),
   (60,64,"Cổng có phần thiết lập giám sát có ngưỡng"),
   (63,64,"Cổng có phần xử lý sự cố đủ bảy bước")],
9:[(65,66,"Semantic layer là một trong ba cách giải bài toán phân mảnh"),
   (66,67,"Khai báo thực thể và chiều là cấu phần của semantic layer"),
   (67,68,"Chỉ số định nghĩa trên độ đo và thực thể đã khai báo"),
   (68,69,"Người dùng cuối tiêu thụ chính các chỉ số đã định nghĩa"),
   (68,70,"Quản trị vòng đời áp lên định nghĩa chỉ số")],
10:[(71,72,"Đồ thị và máy trạng thái là từ vựng để phát biểu sáu tình huống cron không làm được"),
    (72,73,"Ngày logic là thuộc tính của một lần chạy trong máy trạng thái"),
    (73,74,"Chạy lại an toàn đòi mô hình lọc theo ngày logic")],
11:[(75,76,"Bẫy mã ở tầng ngoài là hệ quả trực tiếp của chu kỳ phân tích tệp của bộ lập lịch"),
    (76,77,"Phải có đồ thị chạy được rồi mới truy được lỗi của nó"),
    (76,78,"Kết nối thay cho thông tin xác thực viết trong chính tệp đồ thị"),
    (76,79,"Quyết định chia task áp lên đồ thị đã dựng"),
    (77,79,"Một trong bốn chỉ số so sánh là thời gian từ lúc hỏng tới lúc biết mô hình nào hỏng"),
    (79,80,"Đặt thử lại khác nhau cho từng loại task chỉ có nghĩa khi đồ thị đã chia task"),
    (80,81,"Chạy bù 30 ngày dựa vào thử lại và thời gian chờ đã cấu hình"),
    (81,82,"Giới hạn song song kiểm chứng bằng chính bài chạy bù")],
12:[(83,84,"Nạp dự án dbt thành đồ thị tài sản đòi khái niệm tài sản trước"),
    (84,85,"Tác vụ và công việc là phần bù cho thứ đồ thị tài sản không biểu diễn được"),
    (84,86,"Phân mảnh là thuộc tính của tài sản"),
    (86,87,"Kiểm tra độ tươi và kiểm tra lát thiếu phát biểu trên phân mảnh"),
    (84,88,"Danh mục hiển thị chính các tài sản đã nạp"),
    (87,88,"Kết quả kiểm tra hiển thị ngay trên đồ thị tài sản")],
13:[(89,90,"Bọc dbt đòi biết trạng thái là giá trị trả về"),
    (90,91,"Bản triển khai tách luồng đã viết khỏi nơi chạy nó"),
    (91,92,"Lịch gắn vào bản triển khai chứ không gắn vào luồng"),
    (91,93,"Khối nạp lúc chạy trong hạ tầng do bản triển khai chỉ định"),
    (90,94,"Hiện vật sinh từ tệp kết quả chạy của dbt đã đọc ở lesson 90")],
14:[(95,96,"Không có phép đo thì ma trận chỉ còn tính từ"),
    (95,97,"Đánh giá một công cụ mức `C` vẫn phải theo cùng bộ tiêu chí"),
    (96,98,"Bảo vệ dựa trên ma trận đã có bằng chứng"),
    (97,98,"Quyết định phải nêu cả phương án không làm lab")],
15:[(99,100,"Quy trình phát hành dựng trên CI đã chạy được"),
    (100,101,"Cam kết mức dịch vụ phát biểu được sau khi có môi trường tách bạch"),
    (100,102,"Chạy lại lịch sử thực hiện qua quy trình phát hành"),
    (101,103,"Đàm phán với người dùng dựa trên cam kết đã công bố"),
    (101,104,"Dự án đòi cam kết mức dịch vụ công bố"),
    (102,104,"Dự án đòi một lần quay lui diễn tập thành công")],
16:[(105,106,"Danh mục lấy quan hệ giữa bảng từ lineage"),
    (105,107,"Thẻ phân loại lan truyền theo lineage cấp cột"),
    (106,107,"Ma trận truy cập gắn vào tài sản đã có trong danh mục")],
17:[(110,111,"Không rà soát tiến độ được khi chưa có kiến trúc được duyệt"),
    (111,112,"Bảo vệ diễn ra sau khi phạm vi đã chốt ở buổi rà soát giữa kỳ")],
}

ORDER = {
1:"Lesson 1, 2 và 3 không bài nào chặn bài nào, nên đảo thứ tự tuỳ ý. Thứ tự đang đánh số đi từ bối cảnh nghề tới khái niệm nền cho dễ theo, không phải vì phụ thuộc. Chỗ cố định duy nhất là lesson 4: nó cần hạt dữ liệu từ lesson 3 để phát biểu thành phần thứ hai của một định nghĩa chỉ số, và cần nỗi đau tự gánh ở lesson 2 để chi phí phân mảnh có nghĩa.",
2:"Lesson 6 là gốc thật: thứ tự thực thi logic suy ra phần lớn quy tắc còn lại, gồm quy tắc mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong hàm tổng hợp. Sau đó đồ thị chia hai nhánh chạy song song được: nhánh biến đổi một bảng (7, 8, 9, 10) và nhánh kết nhiều bảng (11, 12). Hai nhánh gặp ở lesson 12, vì cách chữa nhân bản dòng là gộp trước khi kết. Lesson 14 đặt sau lesson 10 không vì hàm cửa sổ khó hơn, mà vì nó dạy bằng phép đối chiếu với `GROUP BY`; thiếu vế thứ nhất thì vế thứ hai không có nội dung.",
3:"Lesson 19 không chặn bài nào trong module. Nó dạy đọc kế hoạch thực thi, và chỗ dùng thật nằm ở M7 lesson 54 khi cắt chi phí tầng biến đổi. Đặt nó ở đây là vì nó thuộc nhóm kỷ luật mã, không phải vì bài sau cần nó. Ba bài thật sự nối nhau là 20, 21, 22: mẫu khử trùng cho ra ba loại trùng lặp, ba loại trùng lặp cho ra phép xử lý dữ liệu tới muộn. Lesson 24 hội tụ ba nhánh vì dự án chấm cả tính đọc được, báo cáo chất lượng lẫn tính bất biến.",
4:"Module có hai gốc. Lesson 26 không cần lesson 25: nó so sánh hai loại hệ thống, không thao tác trên lược đồ nào. Hai bài đầu đổ vào lesson 27 vì bốn bước Kimball cần cả hai thứ: một lược đồ chuẩn hoá làm đầu vào, và lý do mẫu truy cập phân tích đòi cấu trúc khác. Lesson 27 là nút thắt của module: ba bài sau nó đều lấy đầu ra của một bước trong bốn bước. Lesson 31 và 32 không chặn nhau nên đảo được.",
5:"Lesson 34 chặn cả module vì hai nhánh sau nó đều thao tác qua dòng lệnh. Sau đó nhánh Git (35, 36) và nhánh môi trường (37) chạy song song được, không nhánh nào cần nhánh nào. Hai nhánh hợp ở lesson 38 vì đóng gói cần cả kho mã có nhánh lẫn môi trường tái tạo được.",
6:"Lesson 41 là nút thắt của module: ba nhánh sau nó đều là hệ quả của đồ thị `ref()`. Nhánh kiến trúc (42 tới 45) là chuỗi thật vì mỗi tầng đọc từ tầng trước. Nhánh vật chất hoá (46) và nhánh tài liệu (47) độc lập với nhau và với nhánh kiến trúc, nên dạy song song được. Ba nhánh hội tụ ở lesson 48 vì dự án chấm cả ba.",
7:"Module có ba gốc độc lập: gia tăng, snapshot, và macro. Lesson 50 không cần lesson 49 dù cả hai nói về dữ liệu thay đổi theo thời gian, vì snapshot cài đặt chiều Type 2 còn mô hình gia tăng xử lý khối lượng. Lesson 51 mở nhánh dài nhất: gói cộng đồng và cấu hình theo môi trường đều dựng trên ngôn ngữ khuôn mẫu. Lesson 54 chỉ cần lesson 49, nên dạy được sớm hơn vị trí đánh số.",
8:"Lesson 57 chặn bốn bài kế tiếp vì bốn tầng kiểm thử là từ vựng cho tất cả. Sau đó có hai nhánh: nhánh kiểm thử (58, 59) và nhánh vận hành theo thời gian (60, 61, 62, 63). Nhánh thứ hai là chuỗi nhân quả thật: thay đổi lược đồ nguồn sinh ra nhu cầu contract, contract sinh ra nhu cầu thực thi, thực thi sinh ra quy trình xử lý sự cố. Lesson 64 hội tụ ba nhánh vì cổng chấm cả ba.",
9:"Module gần như tuyến tính, và ở đây tuyến tính là thật chứ không phải thói quen: mỗi bài định nghĩa vật mà bài sau thao tác lên. Thực thể và chiều có trước thì mới khai báo được độ đo; độ đo có trước thì mới định nghĩa được chỉ số; chỉ số có trước thì mới nói được chuyện tiêu thụ và quản trị vòng đời. Chỗ rẽ duy nhất là lesson 69 và lesson 70, hai bài không chặn nhau.",
10:"Bốn bài là một chuỗi thật. Lesson 71 dựng danh sách sáu tình huống cron không biểu diễn được; lesson 72 cấp từ vựng đồ thị và máy trạng thái để phát biểu chúng cho chính xác; lesson 73 lấy một trạng thái cụ thể trong máy đó là ngày logic; lesson 74 dùng ngày logic để phát biểu điều kiện chạy lại an toàn. Không bài nào đảo được mà vẫn giữ nghĩa.",
11:"Lesson 76 là nút thắt: bốn bài sau đều thao tác trên đồ thị đã dựng ở đó. Lesson 77 và 78 không chặn nhau nên đảo được. Lesson 79 là bài nặng nhất module và nó cần hai đầu vào: đồ thị chạy được từ lesson 76, và phép đo thời gian truy lỗi từ lesson 77, vì một trong bốn chỉ số so sánh chính là con số đó. Ba bài cuối là chuỗi vận hành: chia task xong mới đặt được thử lại theo loại task, có thử lại mới chạy bù được, chạy bù mới lộ ra giới hạn tài nguyên.",
12:"Lesson 84 là nút thắt: ba bài sau đều thao tác trên đồ thị tài sản đã nạp. Lesson 85 nằm riêng một nhánh vì nó nói về thứ đồ thị tài sản không biểu diễn được, nên nó không chặn bài nào và không bài nào chặn nó ngoài lesson 84. Nhánh chính là 86 rồi 87: phân mảnh có trước thì kiểm tra lát thiếu và độ tươi mới phát biểu được. Lesson 88 hội tụ vì danh mục hiển thị cả tài sản lẫn kết quả kiểm tra.",
13:"Lesson 90 và lesson 91 là hai nút liên tiếp, và đây là chỗ Prefect khác hai công cụ trước: bản triển khai là một tầng riêng giữa mã luồng và hạ tầng, nên mọi thứ về lịch và khối đều treo vào nó chứ không treo vào luồng. Lesson 92 và 93 không chặn nhau nên đảo được. Lesson 94 chỉ cần lesson 90, vì hiện vật sinh từ tệp kết quả chạy đã đọc ở đó, nên dạy được sớm hơn vị trí đánh số.",
14:"Lesson 95 chặn cả module vì không có phép đo thì ba bài sau chỉ còn tính từ. Lesson 96 và 97 không chặn nhau: một bài đo ba công cụ đã có lab, một bài đánh giá một công cụ chưa có lab, và chúng dùng chung bộ tiêu chí chứ không dùng chung dữ liệu. Lesson 98 hội tụ vì buổi bảo vệ phải nêu cả phương án đã đo lẫn phương án chỉ đọc tài liệu.",
15:"Lesson 100 là nút thắt: ba bài sau đều cần môi trường tách bạch. Nhánh cam kết dịch vụ (101, 103) và nhánh chạy lại lịch sử (102) độc lập với nhau. Lesson 103 nói về quan hệ hai chiều với đội nguồn và người dùng, và nó chỉ cần cam kết đã công bố ở lesson 101 làm cơ sở đàm phán, nên nó không nằm trên đường găng của module.",
16:"Lesson 108 và lesson 109 không chặn bài nào và không bài nào chặn chúng. Kinh tế của tầng biến đổi dựa vào M7 lesson 54 chứ không dựa vào lineage; bài nghề nghiệp thì độc lập hoàn toàn. Ba bài còn lại là chuỗi thật: lineage sinh ra danh mục, danh mục cộng lineage sinh ra khả năng gắn thẻ và lan truyền phân loại.",
17:"Ba bài không phụ thuộc nhau về khái niệm; chúng là ba mốc của cùng một dự án theo thời gian. Lesson 111 sau lesson 110 vì không rà soát tiến độ được khi kiến trúc chưa duyệt; lesson 112 sau lesson 111 vì phạm vi phải chốt trước khi bảo vệ. Không chỗ nào đảo hay học song song được.",
}

PARALLEL = {
1:"Lesson 1, 2 và 3 học song song hoặc đảo thứ tự tuỳ ý. Lesson 4 thì không.",
2:"Sau lesson 6, nhánh {7, 8, 9, 10} và nhánh {11, 12} chạy song song được tới điểm hợp ở lesson 12.",
3:"Lesson 19 học song song với mọi bài khác trong module, hoặc dời hẳn sang trước M7 lesson 54. Lesson 23 học song song với lesson 22.",
4:"Lesson 26 học song song với lesson 25. Lesson 31 và lesson 32 học song song được sau lesson 29.",
5:"Sau lesson 34, nhánh {35, 36} và nhánh {37} chạy song song được.",
6:"Sau lesson 41, ba nhánh {42, 43, 44, 45}, {46} và {47} chạy song song được. Lớp thiếu thời gian giao lesson 47 làm bài tự học, miễn nộp trước lesson 48.",
7:"Ba nhánh {49, 54}, {50} và {51, 52, 53, 55} chạy song song được hoàn toàn.",
8:"Sau lesson 57, nhánh {58, 59} và nhánh {60, 61, 62, 63} chạy song song được.",
9:"Lesson 69 và lesson 70 học song song được sau lesson 68. Các bài còn lại không.",
10:"Không có bài nào học song song được trong module này.",
11:"Lesson 77 và lesson 78 học song song được sau lesson 76.",
12:"Lesson 85 học song song với nhánh {86, 87}. Nó chỉ cần lesson 84.",
13:"Lesson 92, 93 và 94 học song song được: 92 và 93 cần lesson 91, còn 94 chỉ cần lesson 90.",
14:"Lesson 96 và lesson 97 học song song được sau lesson 95.",
15:"Sau lesson 100, nhánh {101, 103} và nhánh {102} chạy song song được.",
16:"Lesson 108 và lesson 109 học song song với mọi bài khác trong module.",
17:"Không có bài nào học song song được.",
}

CROSS = {
1:("Không","M2 — lesson 6 đòi khái niệm hạt dữ liệu ở lesson 3 · M6 — lesson 39 đối chiếu với tám vấn đề tự rút ra ở lesson 2","Không; M1 là gốc của chương trình"),
2:("M1","M3 · M4","M5 — M5 là nhánh công cụ, không cần SQL"),
3:("M2","M4 · M6","M5"),
4:("M3","M6 — lesson 45 áp mô hình chiều vào công cụ · M7 — lesson 50 cài chiều Type 2 của lesson 31","M5"),
5:("M1","M6 — dbt chạy qua dòng lệnh và dự án nằm trong kho Git","M2 · M3 · M4 — cả ba học song song được với M5"),
6:("M3 · M4 · M5","M7 · M8 · M9 · M10","Không"),
7:("M6","M15 — lesson 108 dựa vào phép đo chi phí ở lesson 54","M8 — hai module không chặn nhau"),
8:("M6","M15 — lesson 99 chạy chính bộ kiểm thử của M8 trong CI","M7"),
9:("M6 · M7","M16 — lesson 105 truy nguyên tới cột nguồn của chỉ số","M10 — M9 và khối điều phối không chặn nhau"),
10:("M6 · M7","M11 · M12 · M13","M9"),
11:("M10","M12 · M13 · M14 · M15","Không"),
12:("M11","M14","M13 — hai module công cụ không chặn nhau, chia hai giảng viên được"),
13:("M11","M14","M12"),
14:("M11 · M12 · M13","Không","Không"),
15:("M8 · M11","M17","M16"),
16:("M6 · M9","M17","M15"),
17:("Toàn bộ M1–M16","Không","Không"),
}


def main():
    src = open(SRC, encoding="utf-8").read()
    blocks = re.split(r"^(?=# MODULE \d+ ·)", src, flags=re.M)[1:]
    blocks[-1] = re.split(r"^(?=## A · )", blocks[-1], flags=re.M)[0]

    dirs = {}
    for d in os.listdir(CUR):
        m = re.match(r"module_(\d+)-(.+)", d)
        if m:
            dirs[int(m.group(1))] = d

    out_rows = []
    for b in blocks:
        n = int(re.match(r"# MODULE (\d+) ·", b).group(1))
        d = dirs[n]
        title = d.split("-", 1)[1]
        rng = re.search(r"^\*\*(Lessons .+?)\*\*", b, re.M).group(1)
        tbl = re.search(r"^(\| \|.*?)\n\n", b, re.M | re.S).group(1)
        after = b[b.index(tbl) + len(tbl):]
        intro = after.strip().split("\n\n")[0].strip()
        if intro.startswith("### Lesson"):
            intro = ""
        specs = b[b.index("### Lesson"):].rstrip()
        lessons = re.findall(r"^### Lesson (\d+) · (.+?) `(\w+)`\s*$", b, re.M)

        edges = EDGES[n]
        preds = {int(x): [] for x, _, _ in lessons}
        for a, c, _ in edges:
            preds[c].append(a)
        lay = {}
        for x in sorted(preds):
            lay[x] = 0 if not preds[x] else 1 + max(lay[p] for p in preds[x])
        groups = {}
        for x, l in lay.items():
            groups.setdefault(l, []).append(x)
        depth = max(lay.values()) + 1

        o = []
        o.append(f"# MODULE {n} · {title}\n")
        o.append(f"**{rng}**\n")
        o.append(tbl + "\n")
        if intro:
            o.append(intro + "\n")
        o.append("---\n")
        o.append("## Đồ thị phụ thuộc trong module\n")
        o.append(f"{len(lessons)} bài, {len(edges)} cạnh phụ thuộc, sâu {depth} tầng. "
                 f"Mọi cạnh đi từ số bài nhỏ tới số bài lớn, nên đồ thị phi chu trình và không có tham chiếu tiến. "
                 f"Bảng tầng tính trực tiếp từ bảng cạnh bên dưới: bài cùng một tầng không bài nào chặn bài nào. "
                 f"Module cần ít nhất {depth} khe thời gian nối tiếp, so với {len(lessons)} nếu dạy tuần tự.\n")
        o.append("| Tầng | Bài | Dạy được sau khi xong |\n|---|---|---|")
        for l in sorted(groups):
            ls_ = " · ".join("Lesson %d" % x for x in sorted(groups[l]))
            o.append(f"| {l} | {ls_} | {'Không có bài nào chặn' if l == 0 else 'tầng %d' % (l-1)} |")
        o.append("")
        o.append("### Cạnh phụ thuộc\n")
        o.append("| Bài chặn | Bài bị chặn | Lý do kỹ thuật |\n|---|---|---|")
        for a, c, why in edges:
            o.append(f"| Lesson {a} | Lesson {c} | {why} |")
        o.append("")
        o.append("### Vì sao thứ tự này\n")
        o.append(ORDER[n] + "\n")
        o.append("### Học song song trong module\n")
        o.append(PARALLEL[n] + "\n")
        o.append("---\n")
        o.append("## Vị trí trong đồ thị chương trình\n")
        cb, cbs, cp = CROSS[n]
        o.append("| | |\n|---|---|")
        o.append(f"| **Module chặn module này** | {cb} |")
        o.append(f"| **Module này chặn** | {cbs} |")
        o.append(f"| **Học song song được với** | {cp} |")
        o.append("")
        o.append("---\n")
        o.append("## Lesson list\n")
        o.append("| Lesson | Title | Type | Chặn bởi |\n|---|---|---|---|")
        for ln, lt, ty in lessons:
            bl = preds.get(int(ln), [])
            o.append(f"| {ln} | {lt} | `{ty}` | {' · '.join('L%d' % x for x in bl) if bl else '—'} |")
        o.append("")
        o.append("---\n")
        o.append("## Lesson specifications\n")
        o.append(specs + "\n")

        path = os.path.join(CUR, d, "roadmap", "roadmap.md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write("\n".join(o))
        out_rows.append((n, len(lessons), len(edges), depth))

    for n, nl, ne, dp in out_rows:
        print(f"M{n:<3} {nl:>2} bài · {ne:>2} cạnh · {dp:>2} tầng")
    print(f"tổng: {sum(r[1] for r in out_rows)} bài, {sum(r[2] for r in out_rows)} cạnh")


if __name__ == "__main__":
    main()
