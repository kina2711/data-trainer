# -*- coding: utf-8 -*-
"""Sinh roadmap từng module cho chương trình Data Analyst từ roadmap tổng v5.0.

Nguồn duy nhất của đặc tả bài là material/data-analyst/roadmap/roadmap.md.
Script không viết lại một chữ nào trong đặc tả đó; nó cắt khối module ra,
rồi chèn thêm phần đồ thị phụ thuộc trong module do người soạn tự suy.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC  = os.path.join(ROOT, "material", "data-analyst", "roadmap", "roadmap.md")
CUR  = os.path.join(ROOT, "material", "data-analyst", "curriculum")

# (bài chặn, bài bị chặn, lý do kỹ thuật)
EDGES = {
1: [(3,4,"Lá của cây chỉ số là một độ đo trên một hạt; thang đo ở lesson 3 quyết định phép tính nào hợp lệ trên lá đó"),
    (3,5,"Bước 3 của đặc tả là khai báo hạt"),
    (4,5,"Bước 2 của đặc tả là chọn chỉ số, và sáu thành phần của một định nghĩa chỉ số nối tiếp cây chỉ số"),
    (2,5,"Thủ tục từ chối một yêu cầu đòi biết dữ liệu mất ở chặng nào trong vòng đời bảy chặng")],
2: [(6,7,"Tham chiếu theo tên cột và vùng đặt tên chỉ tồn tại sau khi dữ liệu ở dạng Table"),
    (7,8,"`IF` lồng nhau là công thức; cần cơ chế tham chiếu trước"),
    (7,9,"Vùng tra cứu phải khoá bằng tham chiếu tuyệt đối"),
    (8,9,"`#N/A` xử lý bằng `IFERROR` và `IFNA`, cả hai giới thiệu ở lesson 8"),
    (7,10,"Hàm chuỗi dùng cùng cơ chế công thức và sao chép công thức"),
    (7,11,"Hàm ngày dùng cùng cơ chế công thức"),
    (6,12,"Table là nguồn hợp lệ duy nhất cho PivotTable tự mở rộng"),
    (11,12,"Nhóm theo ngày, tháng, quý chỉ chạy khi cột ngày đã ở đúng kiểu"),
    (12,13,"Biểu đồ dựng trên kết quả tổng hợp; Show Values As cung cấp chuỗi số để vẽ"),
    (6,14,"Unpivot chuyển bảng rộng thành dạng dài, nên cần định nghĩa dạng dài ở lesson 6"),
    (10,14,"Các bước làm sạch trong Power Query lặp lại đúng thao tác chuỗi ở lesson 10"),
    (11,14,"Bước đổi kiểu sang ngày là chỗ hỏng thường gặp nhất của một truy vấn"),
    (7,15,"Chiều đầy đủ đo bằng `COUNT` so với `COUNTA`, hai hàm đếm hai tập khác nhau"),
    (9,15,"Chiều nhất quán đo bằng tỉ lệ mã không khớp khi ghép hai bảng"),
    (12,15,"Đối chiếu chéo hai nguồn và tổng kiểm tra đều dựng bằng PivotTable"),
    (15,16,"Cổng đòi nộp báo cáo có đối soát")],
3: [(17,18,"Không có môi trường chạy thì không viết được truy vấn nào"),
    (18,19,"`NULL` biểu hiện trước hết ở `WHERE`, nên cần thứ tự thực thi logic"),
    (18,20,"Hàm đặt trong `SELECT` và `WHERE`"),
    (19,21,"Thiếu `ELSE` sinh ra `NULL`, và hệ quả của nó chỉ hiểu được sau logic ba trạng thái"),
    (20,21,"Nhánh `CASE` thường chứa biểu thức chuỗi hoặc ngày"),
    (18,22,"Quy tắc `WHERE` lọc trước gộp và `HAVING` lọc sau gộp suy trực tiếp từ thứ tự thực thi logic"),
    (19,22,"`COUNT(cot)`, `SUM` và `AVG` đều bỏ qua `NULL`; không biết điều đó thì đọc sai mọi kết quả gộp"),
    (21,22,"Gộp nhóm trên biểu thức `CASE`"),
    (18,23,"`JOIN` là tích Descartes cộng một điều kiện lọc, nên cần `WHERE`"),
    (23,24,"Nhân bản dòng là hệ quả của bản số quan hệ nêu ở lesson 23"),
    (22,24,"Cách xử lý nhân dòng là gộp trước khi ghép"),
    (19,25,"`EXISTS`, `IN` và `JOIN` cho kết quả khác nhau khi tập con chứa `NULL`"),
    (24,25,"CTE đặt tên theo hạt của kết quả ghép"),
    (22,26,"`OVER` dạy bằng cách đối chiếu với `GROUP BY`: một bên giữ nguyên số dòng, một bên thu gọn"),
    (25,26,"Hàm cửa sổ không dùng được trong `WHERE`; đường vòng là CTE"),
    (26,27,"Mệnh đề khung và `LAG`, `LEAD` mở rộng cú pháp `OVER`"),
    (22,28,"Ba loại trùng lặp phát hiện bằng đếm theo nhóm"),
    (24,28,"Bản ghi mồ côi là một phát biểu về toàn vẹn tham chiếu giữa hai bảng"),
    (26,28,"Khử trùng cài bằng `ROW_NUMBER` trên phân vùng khoá nghiệp vụ"),
    (22,29,"Kiểm chứng hạt bằng phép đếm là bước bắt buộc của quy trình khảo sát"),
    (28,29,"Bộ truy vấn kiểm chất lượng dùng lại được trên bảng bất kỳ"),
    (29,30,"Cổng khảo sát một cơ sở dữ liệu lạ không có tài liệu")],
4: [(31,32,"Khoá chính, khoá ngoại và bảng trung gian cho quan hệ nhiều–nhiều đều là sản phẩm của chuẩn hoá"),
    (31,34,"Lược đồ sao là phi chuẩn hoá có chủ đích; không có chuẩn hoá thì không phát biểu được nó phi chuẩn hoá cái gì"),
    (32,34,"Đầu vào của bài là một lược đồ chuẩn hoá cho trước, đọc bằng ERD"),
    (33,34,"Lý do lược đồ sao tồn tại là mẫu truy cập của hệ thống phân tích"),
    (34,35,"Chiều thay đổi chậm là một thuộc tính của bảng chiều"),
    (31,36,"Bước 2 của quy trình nạp là định nghĩa lược đồ đích"),
    (36,37,"Phép cộng đối soát tổng đầu vào bằng bản ghi sạch cộng bản ghi lỗi chạy trên kết quả nạp ở lesson 36")],
5: [(38,39,"Phương sai và độ lệch chuẩn là cách định lượng chiều độ trải"),
    (39,40,"Sai số chuẩn phân biệt được với độ lệch chuẩn chỉ sau khi độ lệch chuẩn đã rõ"),
    (40,41,"Kiểm định giả thuyết dựng trên phân phối mẫu và sai số chuẩn"),
    (41,42,"Chọn kiểm định là chọn cách tính trị số p cho một thiết kế cụ thể"),
    (38,43,"Hệ số tương quan bằng 0 trên hai biến phụ thuộc nhau chỉ đọc được khi đã biết hình dạng phân bố"),
    (38,44,"Bước phân tích đơn biến của quy trình bảy bước là mô tả phân bố trên bốn chiều"),
    (39,44,"Phân biệt dao động thường và bất thường quyết định giả thuyết nào đáng theo"),
    (43,44,"Bất thường ở giao hai chiều là dạng thường gặp của nghịch lý Simpson"),
    (42,45,"Dự án đòi kết luận định lượng có kiểm định đã kiểm giả định"),
    (44,45,"Dự án đòi nhật ký giả thuyết từ quy trình bảy bước")],
6: [(46,47,"Sáu cơ chế bóp méo đều phát biểu bằng kênh mã hoá bị dùng sai"),
    (46,48,"Thang màu là một kênh mã hoá; chọn sai loại thang là chọn sai kênh"),
    (49,50,"Độ đo tính trên mô hình; không có quan hệ và hướng lọc thì ngữ cảnh lọc không có nghĩa"),
    (50,51,"Hàm thông minh thời gian là `CALCULATE` cộng bảng lịch"),
    (46,52,"Quy trình thiết kế đi ngược kết thúc ở bước chọn biểu đồ"),
    (47,52,"Dashboard không được chứa biểu đồ bóp méo"),
    (48,52,"Bố cục và phân cấp thị giác dựng trên nguyên tắc màu và nhãn"),
    (52,53,"Bài dựng đúng bản phác thảo vẽ ở lesson 52"),
    (51,53,"Trực quan hoá hiển thị độ đo, gồm cả bộ chỉ số so sánh theo thời gian"),
    (53,54,"Cổng kiểm thử trên dashboard dựng ở lesson 53")],
7: [(55,56,"Phễu định nghĩa trên chuỗi sự kiện; ba tham số của phễu đều là phát biểu về sự kiện"),
    (55,57,"Cohort đòi một định nghĩa danh tính người dùng ổn định qua phiên"),
    (58,59,"Phân rã doanh thu thành số khách × tần suất × giá trị đơn dùng lại đúng ba chiều của RFM"),
    (55,60,"Quy kết kênh đòi sự kiện có ghi nguồn"),
    (56,60,"Phễu tiếp thị là phễu chuyển đổi mở rộng lên các tầng trước sản phẩm"),
    (55,61,"Bước 0 của điều tra là loại trừ sự kiện hỏng và định nghĩa chỉ số vừa đổi"),
    (56,61,"Cắt lát theo bước phễu là một trong các chiều điều tra"),
    (57,61,"Phân biệt thay đổi thành phần với thay đổi hành vi kiểm bằng so sánh cohort"),
    (62,63,"Chuẩn cơ sở ngây thơ theo mùa đòi thành phần mùa vụ đã tách")],
8: [(64,65,"Giả thuyết và chỉ số phát biểu trước khi chạy vì ngẫu nhiên hoá chỉ có giá trị khi thiết kế cố định trước"),
    (65,66,"Cỡ mẫu tính cho một chỉ số chính và một đơn vị ngẫu nhiên hoá đã chọn"),
    (65,67,"Bất cân xứng tỉ lệ mẫu là phép kiểm trên cơ chế ngẫu nhiên hoá dựng ở lesson 65"),
    (66,67,"Nhìn lén và dừng sớm chỉ nêu được thành vấn đề khi lực kiểm định và cỡ mẫu đã rõ"),
    (64,68,"Ba điều kiện khiến ngẫu nhiên hoá bất khả thi nêu ngay ở lesson 64")],
9: [(69,70,"`DataFrame` là một đối tượng Python; cần kiểu dữ liệu và cấu trúc dữ liệu trước"),
    (70,71,"`groupby` và `merge` là phương thức trên `DataFrame`"),
    (70,72,"Mọi thao tác làm sạch chạy trên `DataFrame` đã nạp"),
    (70,73,"`seaborn` nhận `DataFrame` làm đầu vào"),
    (69,74,"Script kéo dữ liệu là một chương trình Python có hàm và xử lý lỗi"),
    (71,74,"Quy tắc đẩy phép lọc và phép gộp xuống cơ sở dữ liệu đòi biết pandas làm được gì tương đương"),
    (72,75,"Bốn phép kiểm chất lượng đặt vào quy trình là các phép đã làm bằng tay ở lesson 72"),
    (74,75,"Kiểm thử và nhật ký bổ sung cho quy trình dựng ở lesson 74"),
    (75,76,"Dự án đòi kho mã có kiểm thử và chạy lại được")],
10:[(77,78,"Tóm tắt điều hành là đỉnh của kim tự tháp"),
    (78,79,"Slide 15 phút rút từ báo cáo đã viết"),
    (78,81,"README dự án mở đầu bằng bài toán nghiệp vụ, theo đúng quy ước viết của báo cáo"),
    (79,82,"Vòng case study là bảo vệ một kết luận dưới chất vấn"),
    (80,82,"Nguyên liệu cho phỏng vấn hành vi theo cấu trúc STAR lấy từ nhật ký lỗi"),
    (81,82,"Portfolio là thứ nhà tuyển dụng đọc trước vòng sàng lọc")],
11:[(83,84,"Không rà soát được tiến độ của một dự án chưa có đặc tả được duyệt"),
    (84,85,"Bảo vệ diễn ra sau khi phạm vi đã chốt ở buổi rà soát giữa kỳ")],
}


ORDER = {
1: "Ba bài đầu không phải một chuỗi. Lesson 1, lesson 2 và lesson 3 không bài nào cần bài nào, nên dạy theo thứ tự nào cũng được. Thứ tự đang đánh số đi từ rộng vào hẹp cho dễ theo, chứ không phải vì phụ thuộc. Chỗ thật sự cố định nằm ở hai bài cuối: lesson 4 phải sau lesson 3 vì lá của cây chỉ số là một độ đo trên một hạt, và lesson 5 phải sau cả hai vì đặc tả sáu bước gọi tên cả hạt lẫn chỉ số.",
2: "Lesson 6 chặn cả module vì ba thứ sau nó đều đòi dữ liệu ở dạng Table. Sau lesson 7 đồ thị tách thành ba nhánh không liên quan nhau: nhánh logic và tra cứu, nhánh chuỗi, nhánh ngày. Hai chỗ hợp nhánh là lesson 12 và lesson 14, và cả hai đều hợp vì cùng một lý do kỹ thuật: PivotTable nhóm theo ngày và Power Query đổi kiểu sang ngày đều hỏng nếu cột ngày chưa đúng kiểu. Lesson 15 đứng cuối vì đối soát cần cả ba nhánh: đếm từ lesson 7, mã không khớp từ lesson 9, tổng kiểm tra từ lesson 12.",
3: "Lesson 18 là gốc thật của module: thứ tự thực thi logic suy ra được phần lớn quy tắc còn lại, gồm quy tắc mọi cột trong `SELECT` phải nằm trong `GROUP BY` hoặc trong một hàm tổng hợp. Sau đó đồ thị chia hai nhánh chạy song song: nhánh biến đổi một bảng (lesson 19 tới 22) và nhánh ghép nhiều bảng (lesson 23 tới 24). Hai nhánh gặp nhau ở lesson 24, vì cách xử lý nhân bản dòng là gộp trước khi ghép. Lesson 26 đặt sau lesson 22 không phải vì hàm cửa sổ khó hơn, mà vì nó dạy bằng phép đối chiếu: `GROUP BY` thu gọn số dòng còn `OVER` giữ nguyên. Không có vế thứ nhất thì vế thứ hai không có nội dung.",
4: "Module có hai gốc. Lesson 33 không cần lesson 31 và lesson 32: nó so sánh hai loại hệ thống, không thao tác trên lược đồ nào. Ba bài đầu đổ vào lesson 34 vì thiết kế lược đồ sao cần đủ ba thứ: biết chuẩn hoá để phát biểu mình đang phi chuẩn hoá cái gì, đọc được ERD của lược đồ nguồn, và biết mẫu truy cập phân tích để biện minh lựa chọn. Nhánh lesson 36 và 37 chạy độc lập với nhánh mô hình hoá, nên xếp cuối là do lịch chứ không do phụ thuộc.",
5: "Chuỗi lesson 38 tới 42 là chuỗi suy diễn thật: mỗi bài định nghĩa đại lượng mà bài sau dùng. Lesson 43 không nằm trong chuỗi đó — nó chỉ cần lesson 38, và dạy một loại sai lầm khác hẳn: sai vì thiết kế nghiên cứu, không sai vì tính toán. Đặt nó sau lesson 42 là theo lịch, không theo phụ thuộc. Lesson 44 là chỗ hợp nhánh, vì quy trình bảy bước gọi tới cả mô tả phân bố, phân biệt dao động, lẫn nhận diện thiên lệch.",
6: "Module có hai gốc độc lập hoàn toàn, và đây là điều thứ tự đánh số che mất. Nhánh nguyên lý thị giác (lesson 46, 47, 48) không đụng tới Power BI. Nhánh công cụ (lesson 49, 50, 51) không đụng tới nguyên lý thị giác. Hai nhánh gặp nhau lần đầu ở lesson 53, khi một bản phác thảo đã có phải dựng bằng độ đo đã viết. Lesson 52 chỉ cần nhánh nguyên lý, nên nó dạy được trước khi học viên mở Power BI lần nào — và nên như thế, vì bài đòi phác thảo trên giấy trước khi mở công cụ.",
7: "Module có ba gốc, không phải một chuỗi chín bài. Lesson 55 mở nhánh phân tích hành vi; lesson 58 mở nhánh thương mại, chạy trên dữ liệu giao dịch chứ không trên dữ liệu sự kiện; lesson 62 mở nhánh chuỗi thời gian, không cần cả hai nhánh kia. Lesson 61 là đỉnh của nhánh hành vi vì điều tra một chỉ số sụt giảm phải cắt lát theo đúng những chiều mà lesson 56 và 57 dựng ra. Ba nhánh chỉ hội tụ ở dự án cuối chương trình, không hội tụ trong module.",
8: "Bốn bài lesson 64 tới 67 theo đúng trình tự vòng đời một thí nghiệm, và trình tự đó cũng là trình tự phụ thuộc: không tính được cỡ mẫu khi chưa chốt chỉ số chính, và không nêu được tác hại của việc dừng sớm khi chưa có khái niệm lực kiểm định. Lesson 68 nằm ngoài chuỗi: nó chỉ cần lesson 64, nên dạy được ngay sau bài mở đầu. Xếp nó cuối là để không cắt ngang mạch thí nghiệm.",
9: "Lesson 70 chặn trực tiếp nhiều bài nhất trong module: ba bài ngay sau nó đều thao tác trên `DataFrame`. Sau đó ba nhánh tách ra và không nhánh nào cần nhánh nào — biến đổi, làm sạch, trực quan hoá. Lesson 74 là ngoại lệ đáng chú ý: nó cần lesson 69 cho phần script và lesson 71 cho quy tắc phân công tính toán, nhưng không cần lesson 72 và 73. Lesson 75 hợp nhánh vì kiểm tra chất lượng trong quy trình chính là các phép đã làm tay ở lesson 72, đặt vào đường chạy dựng ở lesson 74.",
10:"Nhánh trình bày (lesson 77 tới 79) và nhánh vận hành (lesson 80) độc lập nhau. Lesson 80 dạy quản lý dòng yêu cầu và ranh giới nghề nghiệp, không cần kỹ năng viết báo cáo. Lesson 82 là chỗ mọi nhánh đổ về, vì bốn vòng phỏng vấn lấy nguyên liệu từ cả ba: vòng case study cần kỹ năng bảo vệ, vòng hành vi cần nhật ký lỗi, vòng sàng lọc cần portfolio.",
11:"Đây là module duy nhất mà thứ tự tuyến tính thật. Ba bài không phụ thuộc nhau về khái niệm — chúng là ba mốc của cùng một dự án theo thời gian. Lesson 84 sau lesson 83 vì không rà soát được tiến độ khi chưa có đặc tả duyệt; lesson 85 sau lesson 84 vì phạm vi phải chốt trước khi bảo vệ. Không có chỗ nào đảo hay học song song được.",
}

PARALLEL = {
1: "Lesson 1, 2 và 3 học song song hoặc đảo thứ tự tuỳ ý. Lesson 4 và 5 thì không.",
2: "Sau lesson 7, ba nhánh {lesson 8, 9}, {lesson 10} và {lesson 11} chạy song song được. Lớp thiếu thời gian có thể giao lesson 10 làm bài tự học mà không ảnh hưởng nhánh còn lại, miễn nộp trước lesson 14.",
3: "Sau lesson 18, nhánh {lesson 19, 20, 21, 22} và nhánh {lesson 23, 24} chạy song song được tới điểm hợp ở lesson 24. Lesson 27 và lesson 28 không chặn nhau, dạy thứ tự nào cũng được.",
4: "Lesson 33 học song song với lesson 31 và 32. Nhánh {lesson 36, 37} học song song với nhánh {lesson 34, 35}; nếu lớp cần bộ dữ liệu sạch sớm thì đẩy lesson 36 lên trước lesson 34.",
5: "Lesson 43 học song song với chuỗi lesson 40, 41, 42 — nó chỉ cần lesson 38.",
6: "Nhánh {lesson 46, 47, 48, 52} và nhánh {lesson 49, 50, 51} chạy song song được trọn vẹn. Lớp có hai giảng viên nên chia đôi, rút module từ 9 buổi nối tiếp xuống 5.",
7: "Ba nhánh {lesson 55, 56, 57, 60, 61}, {lesson 58, 59} và {lesson 62, 63} chạy song song được hoàn toàn.",
8: "Lesson 68 học song song với lesson 65, 66, 67.",
9: "Lesson 73 học song song với nhánh {lesson 71, 74, 75} — nó chỉ cần lesson 70.",
10:"Lesson 80 học song song với lesson 77, 78, 79.",
11:"Không có bài nào học song song được.",
}

CROSS = {
1: ("Không", "M2 — lesson 6 dùng khái niệm hạt dữ liệu phát biểu ở lesson 3", "Không module nào; M1 là gốc của cả chương trình"),
2: ("M1", "M3 — lesson 22 đối chiếu `GROUP BY` với PivotTable ở lesson 12 · M6 — lesson 49 nối tiếp trực tiếp Power Query ở lesson 14", "Không"),
3: ("M2", "M4 — lesson 34 đòi `JOIN` nhiều bảng và phát biểu hạt · M7 — phễu, cohort, RFM đều cài bằng hàm cửa sổ ở lesson 26–27 · M9 — lesson 71 đối chiếu từng thao tác pandas với truy vấn SQL", "Không"),
4: ("M3", "M5", "M6 — với điều kiện M6 dùng lược đồ sao cho sẵn thay vì lược đồ tự dựng ở lesson 34. Rút ~3 tuần"),
5: ("M4", "M7 · M8 — lesson 66 đòi lực kiểm định và sai lầm loại I, II ở lesson 41", "Không"),
6: ("M2 · M3", "M7", "M4 — với điều kiện dùng lược đồ sao cho sẵn. Rút ~3 tuần"),
7: ("M3 · M5 · M6", "M8 · M10 — lesson 78 viết báo cáo cho kết quả điều tra ở lesson 61", "M9 — người đã biết lập trình nên đẩy M9 lên trước để dùng pandas trong M7. Rút ~2 tuần"),
8: ("M5", "M11", "Xếp được ngay sau M5, không cần chờ M6 và M7"),
9: ("M3", "M10", "M7 — người đã biết lập trình nên học M9 trước. Rút ~2 tuần"),
10:("M7 · M9", "M11", "Không"),
11:("Toàn bộ M1–M10", "Không", "Không"),
}


def main():
    src = open(SRC, encoding="utf-8").read()
    blocks = re.split(r"^(?=# MODULE \d+ ·)", src, flags=re.M)[1:]
    # bo phan phu luc dinh o cuoi khoi cuoi cung
    blocks[-1] = re.split(r"^(?=# PHỤ LỤC)", blocks[-1], flags=re.M)[0]

    dirs = {}
    for d in os.listdir(CUR):
        m = re.match(r"module_(\d+)-(.+)", d)
        if m:
            dirs[int(m.group(1))] = d

    written = []
    for b in blocks:
        mh = re.match(r"# MODULE (\d+) · (.+)", b)
        n = int(mh.group(1))
        d = dirs[n]
        title = d.split("-", 1)[1]
        rng = re.search(r"^\*\*(Lessons .+?)\*\*", b, re.M).group(1)
        tbl = re.search(r"^(\| \|.*?)\n\n", b, re.M | re.S).group(1)
        intro = re.search(r"^\| \*\*Chế độ hỏng\*\*.*?\n\n(.+?)\n\n", b, re.M | re.S).group(1)

        lessons = re.findall(r"^### Lesson (\d+) · (.+?) `(\w+)`\s*$", b, re.M)
        specs = b[b.index("### Lesson"):].rstrip()

        edges = EDGES[n]
        blockers = {}
        for a, c, _ in edges:
            blockers.setdefault(c, []).append(a)

        out = []
        out.append(f"# MODULE {n} · {title}\n")
        out.append(f"**{rng}**\n")
        out.append(tbl + "\n")
        out.append(intro + "\n")
        out.append("---\n")
        out.append("## Đồ thị phụ thuộc trong module\n")
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
        out.append(
            f"{len(lessons)} bài, {len(edges)} cạnh phụ thuộc, sâu {depth} tầng. "
            f"Mọi cạnh đi từ số bài nhỏ tới số bài lớn, nên đồ thị phi chu trình và không có tham chiếu tiến. "
            f"Bảng tầng tính trực tiếp từ bảng cạnh bên dưới: bài cùng một tầng không bài nào chặn bài nào, "
            f"nên dạy song song hoặc đảo thứ tự trong tầng đều được. "
            f"Module cần ít nhất {depth} khe thời gian nối tiếp, so với {len(lessons)} nếu dạy tuần tự.\n")
        out.append("| Tầng | Bài | Dạy được sau khi xong |\n|---|---|---|")
        for l in sorted(groups):
            ls_ = " · ".join("Lesson %d" % x for x in sorted(groups[l]))
            prev = "Không có bài nào chặn" if l == 0 else "tầng %d" % (l - 1)
            out.append(f"| {l} | {ls_} | {prev} |")
        out.append("")
        out.append("### Cạnh phụ thuộc\n")
        out.append("| Bài chặn | Bài bị chặn | Lý do kỹ thuật |\n|---|---|---|")
        for a, c, why in edges:
            out.append(f"| Lesson {a} | Lesson {c} | {why} |")
        out.append("")
        out.append("### Vì sao thứ tự này\n")
        out.append(ORDER[n] + "\n")
        out.append("### Học song song trong module\n")
        out.append(PARALLEL[n] + "\n")
        out.append("---\n")
        out.append("## Vị trí trong đồ thị chương trình\n")
        cb, cbs, cp = CROSS[n]
        out.append("| | |\n|---|---|")
        out.append(f"| **Module chặn module này** | {cb} |")
        out.append(f"| **Module này chặn** | {cbs} |")
        out.append(f"| **Học song song được với** | {cp} |")
        out.append("")
        out.append("---\n")
        out.append("## Lesson list\n")
        out.append("| Lesson | Title | Type | Chặn bởi |\n|---|---|---|---|")
        for ln, lt, ty in lessons:
            bl = blockers.get(int(ln), [])
            bls = " · ".join(f"L{x}" for x in bl) if bl else "—"
            out.append(f"| {ln} | {lt} | `{ty}` | {bls} |")
        out.append("")
        out.append("---\n")
        out.append("## Lesson specifications\n")
        out.append(specs + "\n")

        path = os.path.join(CUR, d, "roadmap", "roadmap.md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write("\n".join(out))
        written.append((n, path, len(lessons), len(edges)))

    for n, p, nl, ne in written:
        print(f"M{n:<3} {nl:>2} bài · {ne:>2} cạnh  →  {os.path.relpath(p, ROOT)}")


if __name__ == "__main__":
    main()
