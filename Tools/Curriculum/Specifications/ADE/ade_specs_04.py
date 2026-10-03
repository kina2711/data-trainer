# -*- coding: utf-8 -*-
"""ADE Phase 4: M9 Relational theory and SQL execution + M10 Storage engine and DB operations."""

M9 = ("Relational Theory and SQL Execution", 113, 132, """| | |
|---|---|
| **Objective cấp module** | Đi từ logic quan hệ tới kế hoạch thực thi vật lý: viết truy vấn đúng hạt và tối ưu bằng ước lượng số dòng, chi phí và bằng chứng |
| **Tiền đề** | M2 · M3 · M4 |
| **Exit criterion** | Với năm truy vấn chậm, nộp kế hoạch trước và sau, số khối đọc, số dòng ước lượng so với thực tế, và độ trễ; mọi tối ưu dẫn được về một quan sát trong kế hoạch |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `DTAN` mức 4 |
| **Chế độ hỏng** | Học cú pháp rồi tối ưu bằng cách thêm chỉ mục cho mọi cột, không đọc kế hoạch lần nào, nên truy vấn vẫn chậm và ghi thì chậm thêm |""",
"""Đây là module công cụ chính của cả hai vai gộp trong chương trình: Analytics Engineer dùng SQL để mô hình hoá, Data Engineer dùng SQL để nạp và đối soát. Mức yêu cầu vì thế cao hơn mức viết được truy vấn chạy ra kết quả.

Ba phần có thứ tự bắt buộc: nền quan hệ trước để biết truy vấn *nên* trả về gì, ngôn ngữ sau để viết ra, rồi mới tới thực thi để biết vì sao nó chậm. Học phần ba trước là học mẹo tối ưu mà không biết truy vấn có đúng hay không.

Khái niệm **hạt** đặt ở lesson 120 là khái niệm được dùng lại nhiều nhất trong toàn chương trình, tới tận M11, M11B và M14.""")

L9 = [
(113,"Relations, keys and functional dependencies","LT","Module 9: M4",
"Bảng trong cơ sở dữ liệu quan hệ không phải bảng tính: nó là một tập các bộ giá trị, nên về lý thuyết không có thứ tự và không có dòng trùng nhau. Hai tính chất đó giải thích nhiều hành vi gây ngạc nhiên, ví dụ vì sao không có thứ tự thì phải nêu rõ cách sắp khi cần. Khoá: khoá dự tuyển là tập thuộc tính xác định duy nhất một bộ, khoá chính là khoá được chọn, khoá ngoại nối hai quan hệ. Phụ thuộc hàm là công cụ để nói một thuộc tính được xác định bởi thuộc tính nào, và nó là nền của chuẩn hoá ở lesson 117. Ràng buộc là tri thức nghiệp vụ được phát biểu bằng máy kiểm được, và **ràng buộc đặt trong cơ sở dữ liệu vẫn đúng khi có đường ghi thứ hai mà ứng dụng không biết**; đây là lý do không nên dựa hoàn toàn vào kiểm tra ở tầng ứng dụng. Phân biệt khoá tự nhiên với khoá thay thế, chuẩn bị cho M11.",
"Xác định khoá dự tuyển và phụ thuộc hàm của một quan hệ cho trước, và nêu ràng buộc nào nên đặt trong cơ sở dữ liệu.",
"Tầng *hiểu*. Bài mở module, đặt từ vựng cho toàn phần nền. Kiểm bằng bài phân tích ba bảng; đạt khi tìm đúng khoá dự tuyển ở ít nhất hai và nêu đúng ràng buộc nên đặt ở tầng cơ sở dữ liệu.",
"Cho ba bảng có dữ liệu mẫu. Với mỗi bảng, tìm khoá dự tuyển bằng cách kiểm tính duy nhất trên dữ liệu thật, viết các phụ thuộc hàm quan sát được, và đề xuất ràng buộc. Thêm một đường ghi thứ hai bỏ qua ứng dụng và chứng minh ràng buộc ở cơ sở dữ liệu vẫn chặn được.",
"Coi bảng như bảng tính có thứ tự · chọn khoá chính là một cột tăng tự động mà không xác định khoá tự nhiên · để mọi ràng buộc ở tầng ứng dụng.",
"Tìm đúng khoá dự tuyển ở ≥ 2/3 bảng, và chứng minh được ràng buộc ở cơ sở dữ liệu chặn đường ghi thứ hai."),

(114,"NULL and three-valued logic","TH","Lesson 113",
"`NULL` không phải một giá trị mà là sự vắng mặt của giá trị, và nhầm hai thứ này là nguồn của những con số sai mà không báo lỗi. Logic ba trạng thái: so sánh với `NULL` cho kết quả không xác định chứ đúng hay sai, nên `WHERE cot <> 'A'` loại luôn cả dòng `NULL`, một hành vi đúng theo lý thuyết và bất ngờ với người dùng. Hành vi của `NULL` trong sáu ngữ cảnh khác nhau: số học, so sánh, nối chuỗi, danh sách giá trị, hàm tổng hợp, và sắp xếp; **hàm tổng hợp bỏ qua `NULL` nên trung bình tính trên cột có `NULL` khác trung bình người dùng nghĩ**. Ba nghĩa khác nhau bị gộp vào một ký hiệu: chưa nhập, không áp dụng, và bằng không; gộp ba nghĩa là mất thông tin và không lấy lại được. Cách xử lý đúng theo ngữ nghĩa chứ theo thói quen thay bằng số không.",
"Dự đoán đúng kết quả của biểu thức chứa `NULL` trong sáu ngữ cảnh và chọn cách xử lý theo đúng ngữ nghĩa nghiệp vụ.",
"Tầng *áp dụng*. Objective là một kỹ năng dự đoán kiểm được ngay, và là nguồn lỗi âm thầm nên phải kiểm kỹ. Kiểm bằng bài dự đoán 15 biểu thức; đạt khi đúng ≥ 13 và giải thích được bằng logic ba trạng thái.",
"Cho 15 biểu thức chứa `NULL` trong sáu ngữ cảnh. Viết dự đoán trước, chạy, đối chiếu. Trên một bảng có cột thiếu dữ liệu, tính trung bình theo ba cách xử lý khác nhau và so ba kết quả. Viết một câu cho mỗi cách nêu nó phù hợp nghĩa nghiệp vụ nào.",
"Dùng `= NULL` thay vì `IS NULL` · thay mọi `NULL` bằng số không · quên rằng điều kiện khác giá trị loại luôn dòng `NULL` · gộp ba nghĩa làm một.",
"Dự đoán đúng ≥ 13/15 biểu thức, và ba cách tính trung bình được gán đúng nghĩa nghiệp vụ."),

(115,"Relational algebra and logical equivalence","LT","Lesson 114",
"Đại số quan hệ là ngôn ngữ mà bộ tối ưu thật sự làm việc trên đó, nên hiểu nó là hiểu vì sao hai truy vấn viết khác nhau lại cho cùng kế hoạch. Sáu phép cơ bản và ý nghĩa: chọn, chiếu, kết, hợp, hiệu, gộp nhóm. Tương đương logic: đẩy phép chọn xuống sát nguồn không đổi kết quả nhưng đổi hẳn chi phí, và đó chính là phép biến đổi mà bộ tối ưu làm đầu tiên; **viết truy vấn đúng nghĩa quan trọng hơn viết truy vấn theo thứ tự mình muốn nó chạy**, vì bộ tối ưu sẽ sắp lại. Ba phép biến đổi mà bộ tối ưu không tự làm được và người viết phải tự làm: đổi truy vấn con tương quan thành phép kết, bỏ phép chọn phân biệt không cần thiết, và tránh hàm bọc quanh cột lọc. Nối tới lesson 40: ba thuật toán kết đã cài tay nay xuất hiện lại dưới dạng toán tử vật lý mà bộ tối ưu chọn.",
"Viết lại một truy vấn thành dạng tương đương có chi phí thấp hơn và giải thích bằng phép biến đổi đại số.",
"Tầng *áp dụng*. Objective là một phép biến đổi có kết quả kiểm được bằng kế hoạch và số đo. Kiểm bằng ba truy vấn; đạt khi ít nhất hai bản viết lại cho cùng kết quả và chi phí thấp hơn đo được.",
"Cho ba truy vấn viết kém. Với mỗi cái, viết lại theo một phép biến đổi tương đương, đối soát kết quả khớp tuyệt đối, và so chi phí. Với một truy vấn, viết hai cách khác nhau về hình thức và chứng minh bộ tối ưu cho cùng kế hoạch.",
"Tối ưu bằng cách đổi thứ tự mệnh đề trong truy vấn · bỏ phép chọn phân biệt mà đổi kết quả · tin rằng cách viết quyết định thứ tự thực thi.",
"≥ 2/3 bản viết lại cho kết quả khớp tuyệt đối với chi phí thấp hơn, và chứng minh được hai cách viết cho cùng kế hoạch."),

(116,"ER modelling and what the database should enforce","TH","Lesson 115",
"Mô hình thực thể quan hệ là cầu giữa từ vựng nghiệp vụ ở lesson 89 và lược đồ vật lý. Thực thể, thuộc tính, quan hệ; bản số một một, một nhiều, nhiều nhiều và cách hiện thực từng loại. Quan hệ nhiều nhiều luôn cần bảng nối, và bảng nối thường mang thêm thuộc tính riêng mà người mới hay bỏ sót. Bốn loại ràng buộc và việc mỗi loại chặn được gì: khoá chính chặn trùng, khoá ngoại chặn tham chiếu mồ côi, duy nhất chặn trùng theo khoá nghiệp vụ, và kiểm tra chặn giá trị vô lý. Câu hỏi thiết kế đi kèm: **hành vi khi xoá bản ghi cha**, vì ba lựa chọn cho ba kết quả khác nhau và chọn sai gây mất dữ liệu hoặc chặn nghiệp vụ. Ba trường hợp nên cố ý không đặt khoá ngoại và lý do, thường gặp ở kho phân tích, chuẩn bị cho M11 và M12.",
"Dựng lược đồ từ mô tả nghiệp vụ với ràng buộc đầy đủ, và chứng minh mỗi ràng buộc chặn được đúng loại dữ liệu sai.",
"Tầng *áp dụng*. Objective là một thiết kế có tiêu chí nghiệm thu bằng phép thử chèn dữ liệu sai. Kiểm bằng tám phép thử phủ định; đạt khi cả tám bị chặn và thông báo lỗi nêu đúng ràng buộc.",
"Từ mô tả nghiệp vụ một hệ đặt hàng có quan hệ nhiều nhiều, dựng lược đồ đầy đủ ràng buộc. Chèn tám bản ghi sai theo tám cách và chứng minh cả tám bị chặn. Thử ba hành vi xoá bản ghi cha khác nhau và ghi kết quả từng cái.",
"Quên bảng nối cho quan hệ nhiều nhiều · bỏ khoá ngoại vì thấy chậm mà chưa đo · đặt hành vi xoá lan toả cho bảng có dữ liệu lịch sử · không thử chèn dữ liệu sai.",
"Tám phép thử phủ định đều bị chặn với thông báo nêu đúng ràng buộc, và ba hành vi xoá được ghi kết quả rõ ràng."),

(117,"Normalization to BCNF, and deliberate denormalization","TH","Lesson 116",
"Chuẩn hoá không phải nghi thức mà là cách loại bỏ ba dị thường cụ thể, nên dạy bằng cách gặp dị thường trước rồi mới học quy tắc. Ba dị thường: thêm không được vì thiếu dữ liệu không liên quan, sửa một chỗ mà chỗ khác còn giá trị cũ, và xoá một bản ghi làm mất luôn thông tin khác. Các dạng chuẩn từ một tới Boyce-Codd, mỗi dạng chữa một loại phụ thuộc, dựa trên phụ thuộc hàm ở lesson 113. Phi chuẩn hoá có chủ đích: lặp dữ liệu để đọc nhanh hơn, đổi lại phải tự giữ đồng bộ và chấp nhận rủi ro lệch; **chỉ phi chuẩn hoá sau khi đo và sau khi biết đường ghi nào giữ đồng bộ**. Đây là chỗ hai vai trong chương trình tách nhau: hệ giao dịch nghiêng về chuẩn hoá, kho phân tích cố ý phi chuẩn hoá, và lý do sẽ rõ ở M11 và M12.",
"Chuẩn hoá một bảng phẳng tới Boyce-Codd, chỉ ra dị thường nào được chữa ở bước nào, rồi phi chuẩn hoá một đường đọc có đo.",
"Tầng *phân tích*. Objective đòi nối mỗi bước chuẩn hoá với một dị thường cụ thể, chứ áp quy tắc. Kiểm bằng bài chuẩn hoá cộng đo; đạt khi mỗi bước gắn đúng dị thường và phần phi chuẩn hoá có số đo ba chiều.",
"Từ một bảng phẳng, tự tạo ra cả ba dị thường bằng dữ liệu thật. Chuẩn hoá từng bước và chỉ ra bước nào chữa dị thường nào. Sau đó chọn một đường đọc và phi chuẩn hoá, đo tác động lên tốc độ đọc, tốc độ ghi và dung lượng. Nêu đường ghi nào chịu trách nhiệm giữ đồng bộ.",
"Học thuộc định nghĩa dạng chuẩn mà không nhận ra dị thường trong bảng thật · chuẩn hoá tới mức mọi truy vấn phải kết mười bảng · phi chuẩn hoá mà không có cơ chế giữ đồng bộ.",
"Ba dị thường được tái hiện và gắn đúng bước chữa, và phần phi chuẩn hoá có số đo cả đọc, ghi lẫn dung lượng."),

(118,"Logical query processing order","LT","Lesson 117",
"Thứ tự viết một truy vấn khác thứ tự nó được xử lý về mặt logic, và biết thứ tự đó giải thích phần lớn lỗi cú pháp khó hiểu của người mới. Thứ tự logic: nguồn, lọc dòng, gộp nhóm, lọc nhóm, chọn cột, sắp xếp, giới hạn. Từ đó suy ra ngay ba hệ quả: bí danh đặt ở bước chọn cột nên không dùng được ở bước lọc dòng nhưng dùng được ở bước sắp xếp; lọc dòng chạy trước gộp nhóm còn lọc nhóm chạy sau, nên đặt điều kiện sai chỗ vừa sai nghĩa vừa chậm; và hàm cửa sổ chạy sau gộp nhóm nên không lồng trực tiếp vào điều kiện lọc được. Phân biệt thứ tự logic với thứ tự thực thi vật lý: bộ tối ưu được phép sắp lại miễn kết quả không đổi, theo lesson 115. Phạm vi tên và cách giải quyết khi hai bảng có cột cùng tên.",
"Giải thích một lỗi cú pháp hoặc một kết quả sai bằng thứ tự xử lý logic, và sửa bằng cách đặt điều kiện đúng bước.",
"Tầng *hiểu*. Bài lý thuyết nền cho toàn phần ngôn ngữ; chưa đòi tối ưu. Kiểm bằng tám truy vấn có lỗi; đạt khi giải thích đúng ít nhất sáu bằng thứ tự xử lý chứ bằng kinh nghiệm.",
"Cho tám truy vấn: bốn cái lỗi cú pháp, bốn cái chạy được nhưng sai nghĩa do đặt điều kiện sai bước. Với mỗi cái, chỉ ra bước nào gây ra và sửa. Với hai truy vấn, chứng minh đặt điều kiện ở bước lọc dòng và bước lọc nhóm cho hai kết quả khác nhau.",
"Dùng bí danh trong mệnh đề lọc dòng · đặt điều kiện lọc dòng vào mệnh đề lọc nhóm · tin thứ tự viết là thứ tự chạy · lồng hàm cửa sổ vào điều kiện lọc.",
"Giải thích đúng ≥ 6/8 truy vấn bằng thứ tự xử lý, và chứng minh được hai kết quả khác nhau khi đặt điều kiện sai bước."),

(119,"Joins, duplicate multiplication and NULL behaviour","TH","Lesson 118",
"Phép kết giải thích bằng tích Descartes cộng điều kiện lọc: đó là định nghĩa cho phép suy ra mọi hành vi còn lại thay vì nhớ từng trường hợp. Bốn kiểu kết cơ bản cộng hai kiểu nửa và phản, cùng bài toán mỗi kiểu giải. Nhân bản dòng là chế độ hỏng nguy hiểm nhất: khi bên phải có nhiều dòng khớp, mỗi dòng bên trái nhân lên và **mọi phép tổng sau đó bị thổi phồng mà không có lỗi nào báo**. Cách phát hiện bắt buộc: đếm dòng trước và sau mỗi phép kết, và đối chiếu tổng với nguồn độc lập. Kết trái rồi đặt điều kiện bảng phải vào mệnh đề lọc dòng làm nó âm thầm thành kết trong, một lỗi kinh điển. `NULL` trong khoá kết không bao giờ khớp, theo lesson 114, nên dòng có khoá thiếu biến mất khỏi kết quả. Nối tới lesson 40: ba thuật toán kết là cách engine thực hiện, còn đây là nghĩa.",
"Viết truy vấn nhiều bảng và chứng minh không mất dòng không nhân dòng bằng phép đếm và đối soát tổng.",
"Tầng *áp dụng*. Objective là một quy trình kiểm chứng bắt buộc chứ chỉ viết đúng cú pháp. Kiểm bằng bài ghép năm bảng; đạt khi tổng khớp tuyệt đối với tổng tính trực tiếp từ bảng gốc.",
"Ghép năm bảng để ra báo cáo doanh thu theo khách và sản phẩm. Đếm dòng sau mỗi bước kết. Đối soát tổng với tổng tính thẳng từ bảng hoá đơn. Cố ý tạo nhân bản dòng và định lượng mức thổi phồng. Đặt điều kiện bảng phải vào mệnh đề lọc dòng và chứng minh kết trái thành kết trong.",
"Không đếm dòng sau khi kết · dùng phép chọn phân biệt để chữa nhân bản thay vì sửa hạt · đặt điều kiện bảng phải sai mệnh đề · quên rằng khoá `NULL` không khớp.",
"Tổng khớp tuyệt đối với bản tính trực tiếp, và định lượng được mức thổi phồng của trường hợp nhân bản cố ý."),

(120,"Aggregation, HAVING and the grain statement","TH","Lesson 119",
"Gộp nhóm là **một phép biến đổi hạt**, và cách trình bày này giải thích mọi quy tắc còn lại thay vì phải nhớ chúng rời rạc. Hạt là câu trả lời cho một dòng trong kết quả đại diện cho cái gì, phát biểu bằng một câu không mơ hồ. Từ đó suy ra: mọi cột trong danh sách chọn phải nằm trong nhóm hoặc trong hàm tổng hợp, vì cột khác không xác định ở hạt mới. Ba biến thể đếm cho ba nghĩa khác nhau và nhầm chúng là nguồn số sai. Hàm tổng hợp bỏ qua `NULL` theo lesson 114. Lọc dòng trước gộp và lọc nhóm sau gộp theo lesson 118. Gộp nhóm trên biểu thức. **Quy tắc bắt buộc của chương trình: mỗi truy vấn gộp phải kèm phát biểu hạt trước và sau, và sai hạt là sai bài dù kết quả số trông hợp lý**; quy tắc này được dùng lại nguyên vẹn ở M11 và M11B.",
"Phát biểu hạt trước và sau mỗi phép gộp và chọn đúng biến thể đếm theo nghĩa nghiệp vụ.",
"Tầng *áp dụng*. Objective là một kỷ luật phát biểu kiểm được bằng rà soát, và là nền cho toàn phần mô hình hoá sau. Kiểm bằng 20 truy vấn gộp; đạt khi mọi truy vấn có phát biểu hạt đúng và ba biến thể đếm dùng đúng chỗ.",
"Viết 20 truy vấn gộp trên dữ liệu thật, mỗi truy vấn nộp kèm phát biểu hạt trước và sau. Với ba truy vấn, dùng cả ba biến thể đếm và giải thích ba con số khác nhau. Đổi bài: người khác đọc phát biểu hạt và kiểm truy vấn có khớp phát biểu không.",
"Bỏ phát biểu hạt vì thấy hiển nhiên · dùng đếm mọi dòng khi cần đếm giá trị phân biệt · báo trung bình trên dữ liệu lệch mà không kèm phân bố · quên rằng gộp đổi hạt nên tổng không còn cộng được như trước.",
"Cả 20 truy vấn có phát biểu hạt đúng và khớp truy vấn, và ba biến thể đếm được giải thích đúng nghĩa."),

(121,"Subqueries, CTEs and the materialization caveat","TH","Lesson 120",
"Ba vị trí đặt truy vấn con và chi phí khác nhau của từng vị trí. Truy vấn con tương quan chạy lại cho mỗi dòng bên ngoài nên chi phí nhân lên, và phần lớn trường hợp viết lại được thành phép kết; bộ tối ưu đôi khi tự làm việc đó nhưng không phải lúc nào cũng làm. So sánh ba cách kiểm tồn tại và khác biệt ngữ nghĩa khi có `NULL`: dùng danh sách giá trị với truy vấn con chứa `NULL` trả về rỗng một cách bất ngờ, theo lesson 114. Biểu thức bảng chung làm truy vấn dài đọc được bằng cách đặt tên cho từng bước; **quy tắc đặt tên là đặt theo hạt chứ theo thao tác**, vì tên theo hạt cho biết một dòng là gì. Cảnh báo về vật chất hoá: ở một số hệ, biểu thức bảng chung là hàng rào tối ưu nên bộ tối ưu không đẩy điều kiện lọc xuyên qua được, và khi đó nó làm truy vấn chậm hẳn.",
"Tái cấu trúc một truy vấn lồng nhiều tầng thành chuỗi biểu thức bảng chung đặt tên theo hạt, và kiểm xem vật chất hoá có làm chậm không.",
"Tầng *áp dụng*. Objective gồm cả một cảnh báo về hiệu năng kiểm được bằng kế hoạch. Kiểm bằng bài tái cấu trúc cộng so kế hoạch; đạt khi kết quả khớp tuyệt đối và nhận ra đúng trường hợp vật chất hoá gây chậm.",
"Nhận một truy vấn 80 dòng lồng bốn tầng. Tái cấu trúc thành năm biểu thức bảng chung đặt tên theo hạt. Đối soát kết quả. So kế hoạch và thời gian hai bản. Viết một truy vấn mà biểu thức bảng chung chặn việc đẩy điều kiện lọc và chứng minh bằng kế hoạch.",
"Đặt tên biểu thức bảng chung là `t1` hay `tam2` · dùng danh sách giá trị với truy vấn con có `NULL` · giả định biểu thức bảng chung luôn miễn phí · để truy vấn con tương quan trong vòng lặp lớn.",
"Kết quả tái cấu trúc khớp tuyệt đối, tên các bước đặt theo hạt, và chỉ ra được bằng kế hoạch trường hợp vật chất hoá chặn tối ưu."),

(122,"Recursive CTEs for hierarchies and graphs","TH","Lesson 121",
"Cấu trúc phân cấp xuất hiện khắp nơi trong dữ liệu nghiệp vụ: cây tổ chức, danh mục sản phẩm, và đồ thị phụ thuộc theo lesson 38. Biểu thức bảng chung đệ quy gồm hai phần: phần neo cho mức đầu, và phần đệ quy nối tiếp cho tới khi không còn dòng mới. Ba điều kiện để nó dừng và chỉ cần thiếu một là vòng lặp vô hạn: có điều kiện dừng, dữ liệu không có chu trình, và có giới hạn độ sâu phòng khi hai điều kiện trên sai. Kỹ thuật chống chu trình bằng cách giữ đường đi đã qua, đúng ý tưởng phát hiện chu trình ở lesson 38. Ba bài toán thường giải bằng đệ quy: duyệt xuống toàn bộ con cháu, truy ngược lên tổ tiên, và tính tổng tích luỹ theo nhánh. Giới hạn hiệu năng: đệ quy trên đồ thị lớn tốn kém, nên với đồ thị rất lớn thì tính sẵn bảng đường đi là lựa chọn đúng hơn.",
"Viết truy vấn đệ quy duyệt một cấu trúc phân cấp có chống chu trình và có giới hạn độ sâu.",
"Tầng *áp dụng*. Objective là một kỹ thuật cụ thể có ba điều kiện an toàn kiểm được. Kiểm bằng ba bài toán cộng một tập dữ liệu có chu trình; đạt khi cả ba đúng và truy vấn không treo trên dữ liệu có chu trình.",
"Trên bảng cây tổ chức, viết ba truy vấn đệ quy: liệt kê toàn bộ cấp dưới, truy ngược chuỗi quản lý, và tính tổng ngân sách theo nhánh. Chèn một chu trình vào dữ liệu và chứng minh truy vấn có chống chu trình vẫn dừng còn bản không có thì treo.",
"Quên điều kiện dừng · không chống chu trình · không đặt giới hạn độ sâu · dùng đệ quy cho đồ thị rất lớn mà chưa cân nhắc bảng đường đi tính sẵn.",
"Ba truy vấn cho kết quả đúng, và bản có chống chu trình dừng được trên dữ liệu có chu trình trong khi bản không có thì treo."),

(123,"Window functions - partition, order and frame","TH","Lesson 122",
"Khác biệt cơ bản với gộp nhóm phát biểu bằng một câu: gộp nhóm **thu gọn** dòng còn hàm cửa sổ **giữ nguyên** dòng và thêm một cột tính trên một nhóm dòng lân cận. Từ đó suy ra vì sao dùng được hàm cửa sổ để lấy đứng đầu mỗi nhóm mà vẫn giữ mọi cột. Giải phẫu ba phần: phân vùng chia dòng thành nhóm, sắp xếp định thứ tự trong nhóm, khung xác định dòng nào được tính. Bốn hàm xếp hạng và khác biệt chỉ lộ ra khi có giá trị trùng, nên phải thử trên dữ liệu có trùng chứ dữ liệu sạch. Mẫu lấy N dòng đầu mỗi nhóm, giải đúng bài toán đã gặp ở lesson 37 nhưng ở tầng SQL. Vì sao không dùng hàm cửa sổ trong mệnh đề lọc dòng được, theo thứ tự xử lý ở lesson 118, và cách vòng qua bằng một tầng bọc ngoài.",
"Giải bài toán lấy N đầu mỗi nhóm và chọn đúng hàm xếp hạng theo yêu cầu xử lý giá trị trùng.",
"Tầng *áp dụng*. Objective đòi chọn đúng biến thể theo ngữ nghĩa, chỗ khác biệt chỉ lộ ra ở ca biên. Kiểm bằng ba yêu cầu trên dữ liệu có trùng; đạt khi cả ba chọn đúng hàm và kết quả đúng ở ca có trùng.",
"Trên dữ liệu cố ý có giá trị trùng, viết ba truy vấn: top ba sản phẩm mỗi chi nhánh, đơn gần nhất của mỗi khách, và chia khách thành năm nhóm theo chi tiêu. Với mỗi cái, thử cả bốn hàm xếp hạng và giải thích vì sao chọn cái đã chọn.",
"Dùng hàm xếp hạng có trùng khi cần đúng một dòng mỗi nhóm · quên phân vùng nên xếp hạng toàn bảng · đặt hàm cửa sổ vào mệnh đề lọc dòng · thử trên dữ liệu không có giá trị trùng.",
"Ba truy vấn đúng trên dữ liệu có trùng, và giải thích được vì sao chọn hàm xếp hạng đó thay vì ba hàm kia."),

(124,"Frames, running totals and period comparison","TH","Lesson 123",
"Mệnh đề khung quyết định hàm cửa sổ nhìn thấy những dòng nào, và hiểu nhầm nó là nguồn của các con số luỹ kế sai. Hai cách đếm khung: theo số dòng và theo giá trị; hai cách cho kết quả khác nhau khi có giá trị trùng, và ví dụ đối chiếu làm rõ khác biệt đó. Khung mặc định khi có mệnh đề sắp xếp không phải toàn bộ phân vùng, nên một số hàm cho kết quả bất ngờ nếu không nêu khung tường minh. So kỳ trước và cùng kỳ năm trước bằng hàm lấy giá trị dòng trước và dòng sau. **Vấn đề kỳ thiếu**: tháng không có giao dịch biến mất khỏi kết quả nên phép so kỳ trước lấy nhầm tháng, và lời giải là kết với bảng lịch đầy đủ; đây là bài học sẽ dùng lại ở M11 khi dựng bảng chiều thời gian. Chia cho không khi kỳ trước bằng không, và cách xử lý theo nghĩa nghiệp vụ.",
"Dựng báo cáo có luỹ kế, trung bình trượt và tăng trưởng so kỳ, đúng cả ở kỳ không có dữ liệu.",
"Tầng *áp dụng*. Objective có một ca biên cụ thể mà bản làm ẩu luôn sai. Kiểm bằng đối soát với bản tính độc lập; đạt khi khớp tuyệt đối kể cả ở các kỳ thiếu dữ liệu.",
"Dựng báo cáo 24 tháng có ba chỉ số trên dữ liệu cố ý thiếu ba tháng. Đối soát với bản tính độc lập. So kết quả giữa khung đếm theo dòng và khung đếm theo giá trị trên dữ liệu có trùng. Xử lý trường hợp kỳ trước bằng không và nêu nghĩa nghiệp vụ đã chọn.",
"Không dựng bảng lịch nên kỳ rỗng biến mất · dựa vào khung mặc định · nhầm hai cách đếm khung · chia cho không mà không xử lý.",
"Ba chỉ số khớp tuyệt đối với bản tính độc lập kể cả ở ba tháng thiếu, và giải thích được khác biệt giữa hai cách đếm khung."),

(125,"DML, DDL, constraints and views","TH","Lesson 124",
"Phần ngôn ngữ còn lại, gắn với ranh giới giao dịch đã học ở lesson 103. Các lệnh sửa dữ liệu và mệnh đề trả về dòng đã sửa, hữu dụng để ghi nhật ký kiểm toán trong cùng một lượt. Lệnh hợp nhất và cạm bẫy khi nguồn có dòng trùng: nó không báo lỗi mà cho kết quả không xác định. Ghi bất biến theo khoá nghiệp vụ, đúng nguyên tắc ở lesson 30 và 105, nay bằng SQL. Lệnh định nghĩa cấu trúc và ràng buộc theo lesson 116; **thêm ràng buộc lên bảng lớn có thể khoá bảng rất lâu**, nên quy trình đổi cấu trúc an toàn là thêm ở trạng thái chưa kiểm rồi kiểm sau. Khung nhìn là truy vấn đặt tên, không lưu dữ liệu; khung nhìn vật chất hoá có lưu và phải làm mới, nên nó là một dạng bộ đệm và mang mọi vấn đề của bộ đệm, chủ đề sẽ quay lại ở M12 và M14. Ba lý do khung nhìn chồng khung nhìn thành khó gỡ, chuẩn bị cho bài toán ở M14.",
"Viết lệnh ghi bất biến theo khoá nghiệp vụ và đổi cấu trúc bảng lớn mà không khoá bảng quá ngưỡng.",
"Tầng *áp dụng*. Objective gồm hai thao tác có ràng buộc vận hành kiểm được. Kiểm bằng thí nghiệm ghi lặp và thí nghiệm đổi cấu trúc có tải; đạt khi ghi lặp không sinh trùng và thời gian khoá dưới ngưỡng.",
"Viết lệnh hợp nhất theo khoá nghiệp vụ và chạy lại năm lần trên cùng dữ liệu, chứng minh không sinh trùng. Tạo nguồn có dòng trùng và quan sát kết quả không xác định. Thêm một ràng buộc lên bảng 5 triệu dòng đang có tải, đo thời gian khoá ở hai cách làm.",
"Dùng lệnh hợp nhất với nguồn chưa khử trùng · thêm ràng buộc trực tiếp lên bảng lớn đang có tải · chồng khung nhìn nhiều tầng · nhầm khung nhìn với khung nhìn vật chất hoá.",
"Ghi lặp năm lần không sinh trùng, và thời gian khoá khi thêm ràng buộc dưới ngưỡng ở cách làm hai bước."),

(126,"Inside the engine - from parser to executor","LT","Lesson 125",
"Truy vấn đi qua năm giai đoạn trước khi có kết quả, và biết giai đoạn nào làm gì là điều kiện để đọc kế hoạch ở lesson 130. Bộ phân tích cú pháp dựng cây; bộ ràng buộc tên phân giải bảng và cột, đây là nơi lỗi tên xuất hiện; bộ viết lại áp các phép biến đổi tương đương ở lesson 115; bộ lập kế hoạch liệt kê các cách thực hiện và chọn cái rẻ nhất theo mô hình chi phí; bộ thực thi chạy kế hoạch đã chọn. Điểm quan trọng: **bộ lập kế hoạch chọn dựa trên ước lượng, và ước lượng có thể sai**; phần lớn truy vấn chậm bất thường là hậu quả của ước lượng sai chứ của bộ tối ưu kém. Mô hình chi phí kết hợp chi phí đọc và chi phí tính, và nó được hiệu chỉnh theo giả định về phần cứng, nên máy có đĩa thể rắn mà cấu hình mặc định cho đĩa quay thì bộ tối ưu tránh tra chỉ mục một cách không cần thiết.",
"Nêu đúng giai đoạn nào chịu trách nhiệm cho một hiện tượng cho trước, và giải thích vì sao ước lượng sai làm kế hoạch xấu.",
"Tầng *hiểu*. Bài lý thuyết nền cho toàn phần thực thi. Kiểm bằng sáu hiện tượng cần quy về giai đoạn; đạt khi quy đúng ít nhất bốn và giải thích đúng vai trò của ước lượng.",
"Cho sáu hiện tượng gồm lỗi tên cột, truy vấn viết khác nhau ra cùng kế hoạch, kế hoạch đổi sau khi cập nhật thống kê, và ba cái khác. Quy mỗi hiện tượng về một giai đoạn. Đọc cấu hình chi phí của hệ và chỉ ra giả định nào về phần cứng đang được dùng.",
"Nghĩ bộ tối ưu luôn chọn đúng · đổ lỗi cho engine khi nguyên nhân là ước lượng sai · bỏ qua cấu hình chi phí không khớp phần cứng thật.",
"Quy đúng ≥ 4/6 hiện tượng về giai đoạn, và chỉ ra được giả định phần cứng trong cấu hình chi phí."),

(127,"Physical operators and the three join algorithms","TH","Lesson 126",
"Các toán tử vật lý là những viên gạch mà kế hoạch được ghép từ đó, và ba thuật toán kết ở đây chính là ba thứ đã tự cài ở lesson 40. Toán tử quét: quét tuần tự đọc cả bảng, quét chỉ mục đi qua cây rồi lấy dòng, quét chỉ mục có phủ không cần lấy dòng vì chỉ mục đã chứa đủ cột. Toán tử sắp xếp và toán tử gộp, cùng ngưỡng bộ nhớ: vượt ngưỡng thì tràn ra đĩa và đó chính là sắp xếp ngoài ở lesson 39, nên chi phí nhảy vọt. Ba thuật toán kết và điều kiện chọn: vòng lặp lồng nhau tốt khi bên ngoài nhỏ và bên trong có chỉ mục; kết băm tốt khi một bên vừa bộ nhớ; kết trộn tốt khi cả hai đã sắp xếp. Bộ nhớ làm việc là tham số quyết định ranh giới giữa chạy trong bộ nhớ và tràn đĩa, và đo được tác động của nó.",
"Dự đoán thuật toán kết mà bộ tối ưu sẽ chọn cho một tình huống và kiểm chứng bằng kế hoạch.",
"Tầng *phân tích*. Objective nối kiến thức tự cài ở lesson 40 với lựa chọn thật của engine. Kiểm bằng bốn tình huống; đạt khi dự đoán đúng ít nhất ba và giải thích đúng trường hợp tràn đĩa.",
"Tạo bốn tình huống khác nhau về kích thước hai bên và sự có mặt của chỉ mục. Với mỗi cái, viết dự đoán thuật toán kết trước khi chạy, rồi đọc kế hoạch để đối chiếu. Giảm bộ nhớ làm việc tới khi thấy tràn đĩa trong kế hoạch và đo mức chậm đi.",
"Nghĩ một thuật toán kết luôn nhanh hơn · bỏ qua bộ nhớ làm việc · không phân biệt quét chỉ mục với quét chỉ mục có phủ · kết luận mà không đọc kế hoạch.",
"Dự đoán đúng ≥ 3/4 tình huống, và chỉ ra được dấu hiệu tràn đĩa trong kế hoạch kèm số đo mức chậm đi."),

(128,"Statistics, selectivity and cardinality estimation","TH","Lesson 127",
"Bộ lập kế hoạch chọn dựa trên ước lượng số dòng, và ước lượng dựa trên thống kê thu thập được từ dữ liệu. Ba loại thống kê: số giá trị phân biệt, biểu đồ phân bố, và danh sách giá trị phổ biến nhất. Độ chọn lọc là tỉ lệ dòng còn lại sau một điều kiện, và ước lượng số dòng là tích của các độ chọn lọc. Từ đó lộ ra **giả định độc lập**: engine giả định các điều kiện không liên quan nhau, nên khi hai cột tương quan thì ước lượng sai nhiều bậc. Ví dụ điển hình là lọc theo thành phố và theo mã vùng: hai điều kiện thực ra nói cùng một thứ. Ba nguyên nhân ước lượng sai: thống kê cũ, dữ liệu lệch, và tương quan giữa cột. Ba cách chữa theo thứ tự nên thử: cập nhật thống kê, khai báo thống kê mở rộng cho nhóm cột tương quan, và viết lại truy vấn. So sánh số dòng ước lượng với số dòng thật là bước chẩn đoán đầu tiên.",
"Phát hiện ước lượng sai bằng cách so số dòng ước lượng với thực tế và chữa bằng đúng một trong ba cách.",
"Tầng *phân tích*. Objective là chẩn đoán nguyên nhân gốc của phần lớn truy vấn chậm. Kiểm bằng ba tình huống ước lượng sai; đạt khi phát hiện cả ba và chữa được ít nhất hai với tỉ lệ sai giảm rõ rệt.",
"Tạo ba tình huống: thống kê cũ sau khi nạp lớn, dữ liệu lệch nặng, và hai cột tương quan. Với mỗi cái, chạy kế hoạch có phân tích và so số dòng ước lượng với thực tế. Chữa bằng cách phù hợp và đo lại tỉ lệ sai. Ghi bảng trước sau.",
"Thêm chỉ mục để chữa ước lượng sai · không cập nhật thống kê sau khi nạp lớn · bỏ qua giả định độc lập · so thời gian mà không so số dòng.",
"Phát hiện đúng cả ba tình huống, và tỉ lệ sai ước lượng giảm rõ rệt ở ≥ 2/3 sau khi chữa."),

(129,"Indexes - structure, composite order and cost","TH","Lesson 128",
"Chỉ mục là cây B theo lesson 36, và mọi quy tắc dùng chỉ mục suy ra từ cấu trúc đó. Chỉ mục tổ hợp và quy tắc tiền tố trái: chỉ mục trên ba cột dùng được cho điều kiện trên cột đầu, hai cột đầu, hoặc cả ba, nhưng **không dùng được nếu điều kiện chỉ có cột thứ hai**; nên thứ tự cột trong chỉ mục là quyết định thiết kế chứ chi tiết. Chỉ mục có cột phủ thêm để tránh phải lấy dòng. Chỉ mục một phần chỉ trên tập con dòng, rất hiệu quả khi truy vấn luôn lọc theo một điều kiện cố định. Chỉ mục trên biểu thức khi điều kiện lọc bọc hàm quanh cột. Cái giá của chỉ mục và phần hay bị bỏ qua: mỗi chỉ mục làm mọi lệnh ghi chậm thêm và chiếm dung lượng, nên **thêm chỉ mục cho mọi cột là cách làm hệ ghi chậm mà đọc không nhanh hơn**. Cách tìm chỉ mục không bao giờ được dùng và bỏ chúng đi.",
"Thiết kế bộ chỉ mục cho một khối lượng truy vấn thật và định lượng cả phần đọc nhanh lên lẫn phần ghi chậm đi.",
"Tầng *đánh giá*. Objective đòi cân hai chiều đối nghịch, chứ chỉ thêm chỉ mục. Kiểm bằng bảng đo hai chiều; đạt khi đọc nhanh lên có số, ghi chậm đi được định lượng, và không chỉ mục nào thừa.",
"Nhận nhật ký 50 truy vấn thật. Thiết kế bộ chỉ mục. Đo thời gian bộ truy vấn trước và sau, và đo thông lượng ghi trước và sau. Cố ý tạo một chỉ mục sai thứ tự cột và chứng minh nó không được dùng. Tìm và bỏ các chỉ mục không bao giờ được dùng.",
"Thêm chỉ mục cho mọi cột trong điều kiện lọc · đặt sai thứ tự cột trong chỉ mục tổ hợp · bọc hàm quanh cột lọc làm chỉ mục vô hiệu · không đo tác động lên ghi.",
"Bộ truy vấn nhanh lên có số, tác động lên thông lượng ghi được định lượng, và chứng minh được chỉ mục sai thứ tự không được dùng."),

(130,"Reading EXPLAIN ANALYZE with buffers","TH","Lesson 129",
"Kế hoạch thực thi là nguồn sự thật duy nhất khi chẩn đoán truy vấn, và đọc được nó phân biệt người tối ưu có căn cứ với người thử từng cách. Đọc từ trong ra ngoài, vì nút con chạy trước nút cha. Bốn con số phải xem ở mỗi nút: số dòng ước lượng, số dòng thật, thời gian, và số khối đọc. **So ước lượng với thực tế là bước đầu tiên**, vì lệch nhiều bậc chỉ thẳng tới nguyên nhân ở lesson 128. Số khối đọc tách thành khối trong bộ đệm và khối đọc từ đĩa, và tỉ lệ đó cho biết truy vấn có được hưởng hồ đệm hay không, nối lại lesson 53. Cảnh báo về thời gian: bật đo thời gian từng nút làm truy vấn chậm đi, nên số thời gian trong kế hoạch không so trực tiếp với thời gian chạy thật được. Quy trình chẩn đoán bốn bước theo thứ tự cố định để không bỏ sót.",
"Đọc một kế hoạch và định vị nút tốn nhất cùng nguyên nhân, dẫn bằng bốn con số chứ bằng cảm nhận.",
"Tầng *phân tích*. Objective là kỹ năng đọc bằng chứng, điều kiện cho bài dự án ở lesson 132. Kiểm bằng năm kế hoạch; đạt khi định vị đúng nút tốn nhất ở ít nhất bốn và quy đúng nguyên nhân ở ít nhất ba.",
"Cho năm kế hoạch thực thi của năm truy vấn chậm vì năm nguyên nhân khác nhau. Với mỗi kế hoạch, chạy quy trình bốn bước, định vị nút tốn nhất, và quy nguyên nhân. Với một truy vấn, so thời gian trong kế hoạch với thời gian chạy thật và giải thích chênh lệch.",
"Đọc kế hoạch từ ngoài vào · chỉ nhìn thời gian mà bỏ số dòng · bỏ qua số khối đọc · so thời gian trong kế hoạch với thời gian chạy thật.",
"Định vị đúng nút tốn nhất ở ≥ 4/5 kế hoạch và quy đúng nguyên nhân ở ≥ 3/5, kèm bốn con số dẫn chứng."),

(131,"Sargability, parameters and plan stability","TH","Lesson 130",
"Ba chủ đề nhỏ nhưng gây nhiều sự cố trong hệ thật. Điều kiện dùng được chỉ mục: điều kiện phải so sánh trực tiếp với cột chứ với hàm bọc quanh cột; ba cách phá chỉ mục phổ biến là bọc hàm, ép kiểu ngầm, và khớp mẫu có ký tự đại diện ở đầu. Truy vấn tham số hoá: tách giá trị khỏi câu lệnh giúp tái dùng kế hoạch và chặn lỗ hổng chèn mã, theo nguyên tắc đã nêu ở lesson 102. Nhưng nó sinh vấn đề riêng: **kế hoạch lập cho giá trị đầu tiên có thể rất xấu cho giá trị sau**, đặc biệt khi dữ liệu lệch; đây là hiện tượng kế hoạch bị đóng băng theo tham số và là nguyên nhân của những sự cố kiểu truy vấn đột nhiên chậm mà mã không đổi. Ba cách xử lý. Ổn định kế hoạch: vì sao kế hoạch đổi sau khi cập nhật thống kê hoặc sau khi nâng cấp, và vì sao đó vừa là tính năng vừa là rủi ro.",
"Nhận ra ba cách phá chỉ mục trong truy vấn cho trước và tái hiện được hiện tượng kế hoạch bị đóng băng theo tham số.",
"Tầng *phân tích*. Objective gồm một hiện tượng khó tái hiện mà nhiều người chưa từng thấy. Kiểm bằng sáu truy vấn cộng một thí nghiệm; đạt khi tìm đúng ít nhất năm chỗ phá chỉ mục và tái hiện được hiện tượng kế hoạch xấu theo tham số.",
"Cho sáu truy vấn, mỗi cái phá chỉ mục theo một cách. Tìm và sửa từng cái, kiểm chứng bằng kế hoạch. Trên bảng có dữ liệu lệch, chạy truy vấn tham số hoá với giá trị hiếm trước rồi giá trị phổ biến sau, và chứng minh kế hoạch không đổi dù đáng lẽ phải đổi.",
"Bọc hàm quanh cột lọc · ghép chuỗi giá trị vào câu lệnh · giả định kế hoạch luôn tối ưu cho mọi tham số · đổ lỗi cho engine khi kế hoạch đóng băng.",
"Tìm đúng ≥ 5/6 chỗ phá chỉ mục và sửa được, và tái hiện được hiện tượng kế hoạch xấu theo tham số với số đo chênh lệch."),

(132,"SQL tuning project - five slow queries","DA","Lesson 131",
"Bài dự án khép module, và nó là bài chuẩn bị trực tiếp cho công việc thật của cả hai vai. Nhận năm truy vấn chậm trên một cơ sở dữ liệu có dữ liệu thật, mỗi truy vấn chậm vì một nguyên nhân khác nhau trong số đã học: ước lượng sai, thiếu chỉ mục, chỉ mục sai thứ tự, điều kiện phá chỉ mục, và tràn bộ nhớ làm việc. Quy trình bắt buộc theo đúng thứ tự: đọc kế hoạch trước, viết giả thuyết, sửa một thứ, đo lại, rồi lặp; cấm sửa nhiều thứ cùng lúc theo đúng kỷ luật ở lesson 60. Nộp cho mỗi truy vấn: kế hoạch trước và sau, số khối đọc, số dòng ước lượng so với thực tế, độ trễ, và một câu nêu tối ưu này dẫn về quan sát nào. Yêu cầu bổ sung quan trọng: **kết quả sau khi tối ưu phải khớp tuyệt đối với kết quả ban đầu**, vì tối ưu làm đổi kết quả là làm hỏng chứ tối ưu.",
"Tăng tốc năm truy vấn đạt ngưỡng, mỗi tối ưu dẫn được về một quan sát trong kế hoạch, và kết quả không đổi.",
"Tầng *sáng tạo*. Bài tổng hợp toàn module thành một quy trình tối ưu có bằng chứng. Kiểm bằng bảng trước sau cộng đối soát kết quả; đạt khi ít nhất bốn truy vấn đạt ngưỡng và mọi kết quả khớp tuyệt đối.",
"Nhận năm truy vấn chậm. Với mỗi cái, nộp kế hoạch trước và sau, bốn con số, và câu dẫn chứng. Đối soát kết quả từng truy vấn với bản gốc. Rà soát chéo: một học viên khác chọn một tối ưu bất kỳ và bạn phải chỉ ra quan sát dẫn tới nó.",
"Thêm chỉ mục cho mọi truy vấn · sửa nhiều thứ cùng lúc · tối ưu làm đổi kết quả · nộp số mà không nộp kế hoạch.",
"≥ 4/5 truy vấn đạt ngưỡng, mọi kết quả khớp tuyệt đối với bản gốc, và mọi tối ưu dẫn được về một quan sát trong kế hoạch."),
]

M10 = ("Storage Engine and Database Operations", 133, 148, """| | |
|---|---|
| **Objective cấp module** | Hiểu đường đi của một lệnh ghi và một lệnh đọc, chọn mức cô lập theo dị thường cần chặn, và vận hành được cơ sở dữ liệu gồm cả khôi phục đã kiểm chứng |
| **Tiền đề** | M4 · M5 · M9 |
| **Exit criterion** | Truy được một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục sau sự cố; thực hiện thành công một lần khôi phục thật |
| **Kỹ năng SFIA** | `DBAD` mức 4 · `SYSP` mức 4 |
| **Chế độ hỏng** | Chọn mức cô lập theo tên nghe có vẻ an toàn, và tin vào bản sao lưu chưa bao giờ khôi phục thử |""",
"""Module này đóng phần nền cơ sở dữ liệu. Nguyên tắc chấm nghiêm nhất của cả chương trình nằm ở đây: **bản sao lưu chưa khôi phục thử thì không tính là bản sao lưu**, và lesson 147 là buổi diễn tập đó.

Thạo sâu một hệ là PostgreSQL, rồi ánh xạ khác biệt sang các hệ khác; đây là quyết định của bản nguồn và được giữ nguyên, vì học nông nhiều hệ cho ra kiến thức không dùng được lúc sự cố.""")

L10 = [
(133,"Pages, heap files and the buffer pool","LT","Module 10: M9",
"Cơ sở dữ liệu không đọc ghi theo dòng mà theo trang, thường 8 KB, và mọi thứ còn lại suy ra từ đó. Bố cục một trang: phần đầu, mảng con trỏ dòng, và vùng dữ liệu lớn dần từ cuối lên; thiết kế này cho phép dòng đổi kích thước mà không phải dịch chuyển cả trang. Siêu dữ liệu về không gian trống và về khả năng nhìn thấy nằm ngay trong trang. Tệp đống là tập các trang không có thứ tự, nên tìm một dòng không có chỉ mục nghĩa là quét mọi trang. Hồ đệm là bộ đệm trang của riêng cơ sở dữ liệu, tách biệt với bộ đệm trang của hệ điều hành ở lesson 53, nên dữ liệu có thể nằm ở cả hai chỗ và điều đó gây nhầm khi đo. Chính sách loại bỏ trang, trang bẩn, và điểm kiểm tra là ba khái niệm nối trực tiếp sang lesson 137 và 138. **Tỉ lệ trúng hồ đệm là chỉ số hiệu năng hàng đầu**, đọc được từ kế hoạch ở lesson 130.",
"Đọc được bố cục một trang thật và giải thích quan hệ giữa hồ đệm với bộ đệm trang của hệ điều hành.",
"Tầng *hiểu*. Bài mở module, nối kiến thức lưu trữ ở M4 với cấu trúc bên trong cơ sở dữ liệu. Kiểm bằng bài khảo sát trang thật cộng bài giải thích; đạt khi đọc đúng ba thành phần của trang và giải thích đúng hai tầng đệm.",
"Dùng công cụ khảo sát trang của PostgreSQL để xem một trang thật: phần đầu, con trỏ dòng, và dữ liệu. Chèn thêm dòng và quan sát trang đổi. Đo tỉ lệ trúng hồ đệm cho một truy vấn ở hai trạng thái đệm nguội và đệm ấm. Giải thích vì sao đo lần hai luôn nhanh hơn.",
"Nghĩ cơ sở dữ liệu đọc theo dòng · nhầm hồ đệm với bộ đệm trang hệ điều hành · đo hiệu năng trên đệm ấm rồi kết luận · bỏ qua tỉ lệ trúng hồ đệm.",
"Đọc đúng ba thành phần của một trang thật, và giải thích đúng hai tầng đệm kèm số đo tỉ lệ trúng ở hai trạng thái."),

(134,"B-tree internals - fanout, splits and clustering","TH","Lesson 133",
"Chỉ mục ở lesson 129 nay mở ra bên trong. Độ rẽ nhánh quyết định chiều cao cây: mỗi nút là một trang chứa nhiều khoá, nên cây một triệu khoá chỉ cao ba tới bốn mức và tìm một khoá tốn ba tới bốn lần đọc trang. Chèn làm nút đầy thì tách, và tách lan lên trên có thể làm cây cao thêm một mức. Từ đó suy ra hai hiện tượng thực tế: chèn theo khoá tăng dần làm mọi lần chèn dồn vào nút cuối nên nút đó thành điểm nóng, còn chèn ngẫu nhiên thì phân bố đều nhưng làm trang bị phân mảnh. Phình chỉ mục sau nhiều lần xoá và cập nhật, cùng cách dựng lại. Gom cụm vật lý: sắp xếp dữ liệu trên đĩa theo thứ tự một chỉ mục làm truy vấn theo khoảng đọc tuần tự thay vì ngẫu nhiên, và đó là chênh lệch đã đo ở lesson 52; đổi lại chỉ gom cụm được theo một thứ tự.",
"Đo được chiều cao cây chỉ mục và chứng minh tác động của thứ tự chèn lên phân mảnh cùng điểm nóng.",
"Tầng *phân tích*. Objective đòi nối cấu trúc bên trong với hiện tượng đo được. Kiểm bằng hai thí nghiệm chèn; đạt khi đo đúng chiều cao cây và chỉ ra khác biệt giữa hai thứ tự chèn bằng số.",
"Tạo chỉ mục trên bảng một triệu dòng và đo chiều cao cây cùng kích thước. Chèn 100.000 dòng theo khoá tăng dần rồi theo khoá ngẫu nhiên vào hai bảng riêng; so thông lượng chèn và độ phân mảnh. Xoá 50% dòng và đo phình chỉ mục, rồi dựng lại và đo lại.",
"Nghĩ chỉ mục là danh sách sắp xếp · bỏ qua phình chỉ mục sau nhiều lần xoá · gom cụm theo nhiều thứ tự cùng lúc · chèn theo khoá tăng dần ở hệ ghi rất nhiều mà không lường điểm nóng.",
"Chiều cao cây đo đúng, và chênh lệch giữa hai thứ tự chèn cùng mức phình sau khi xoá đều có số chứng minh."),

(135,"LSM trees - memtable, SSTable and compaction","LT","Lesson 134",
"Cấu trúc thứ hai, tối ưu cho ghi thay vì đọc, và là cấu trúc của nhiều kho khoá giá trị cùng một số engine phân tích. Cơ chế: ghi vào bảng trong bộ nhớ và vào nhật ký, khi đầy thì đẩy xuống đĩa thành một tệp đã sắp xếp bất biến; đọc phải tra nhiều tệp nên tốn hơn. Bộ lọc Bloom ở lesson 41 dùng đúng ở đây để bỏ qua tệp chắc chắn không chứa khoá. Gộp tệp chạy nền để giảm số tệp phải tra, và đây là nguồn tải vào ra nền mà người vận hành phải biết. So với cây B bằng ba đại lượng khuếch đại ở lesson 136. Nguyên tắc rút ra: **ghi tuần tự luôn rẻ hơn ghi ngẫu nhiên**, theo lesson 52, nên cấu trúc biến mọi lần ghi thành ghi tuần tự thì thắng ở khối lượng ghi nặng, và trả giá ở đọc. Xoá bằng cách ghi thêm dấu xoá chứ xoá tại chỗ, và hệ quả là dung lượng không giảm ngay.",
"Giải thích bằng cơ chế vì sao cấu trúc này thắng ở khối lượng ghi nặng và thua ở đọc ngẫu nhiên.",
"Tầng *hiểu*. Bài lý thuyết so sánh hai cấu trúc; phần đo nằm ở lesson 136. Kiểm bằng bài giải thích cộng dự đoán; đạt khi giải thích đúng cơ chế và dự đoán đúng chiều của ba đại lượng khuếch đại.",
"Đọc cấu trúc thư mục dữ liệu của một kho dùng cấu trúc này: quan sát tệp đã sắp xếp, bộ lọc Bloom, và các mức gộp. Kích hoạt một lần gộp và quan sát tải vào ra. Viết dự đoán về ba đại lượng khuếch đại so với cây B trước khi đo ở bài sau.",
"Nghĩ cấu trúc này luôn nhanh hơn · quên rằng xoá không giải phóng dung lượng ngay · bỏ qua tải nền do gộp tệp · dùng cho khối lượng đọc ngẫu nhiên nặng.",
"Giải thích đúng cơ chế biến ghi ngẫu nhiên thành ghi tuần tự, và dự đoán đúng chiều của cả ba đại lượng khuếch đại."),

(136,"Amplification - read, write and space","TH","Lesson 135",
"Ba đại lượng để so hai cấu trúc lưu trữ một cách khách quan thay vì bằng danh tiếng. Khuếch đại đọc: một lần đọc logic tốn bao nhiêu lần đọc vật lý; cấu trúc gộp theo nhật ký cao hơn vì phải tra nhiều tệp. Khuếch đại ghi: một byte dữ liệu cuối cùng được ghi xuống đĩa bao nhiêu lần; cấu trúc gộp theo nhật ký ghi lại nhiều lần qua các mức gộp, cây B ghi lại khi tách trang và khi ghi nhật ký. Khuếch đại dung lượng: dữ liệu chiếm bao nhiêu lần kích thước logic; cả hai đều có phần dư, một bên do dấu xoá chưa gộp, một bên do trang chưa đầy. **Không có cấu trúc nào tốt cả ba**, nên chọn là chọn đại lượng nào chịu được cao. Cách đo ba đại lượng trên hệ thật, và cách dùng chúng để giải thích vì sao một hệ ghi nặng nên chọn cấu trúc nào.",
"Đo được ba đại lượng khuếch đại trên hai engine và chọn engine theo khối lượng công việc cho trước.",
"Tầng *đánh giá*. Objective đòi chọn theo ba tiêu chí đối nghịch dựa trên số tự đo. Kiểm bằng bảng ba đại lượng nhân hai engine; đạt khi cả sáu ô có số và lựa chọn dẫn được từ bảng.",
"Chạy cùng một khối lượng công việc ghi nặng trên PostgreSQL và trên một kho dùng cấu trúc gộp theo nhật ký. Đo cả ba đại lượng khuếch đại cho mỗi bên. Lặp lại với khối lượng đọc ngẫu nhiên nặng. Lập bảng và chọn engine cho hai tình huống cho trước.",
"So hai engine chỉ bằng thông lượng · bỏ qua khuếch đại dung lượng · đo trong lúc gộp tệp đang chạy nên số bị lệch · kết luận một engine tốt hơn mà không nêu khối lượng công việc.",
"Bảng ba đại lượng nhân hai engine đủ sáu ô, và lựa chọn cho hai tình huống dẫn được từ số trong bảng."),

(137,"The write-ahead log and group commit","TH","Lesson 136",
"Quy tắc nền của mọi cơ sở dữ liệu có cam kết bền vững: **ghi nhật ký trước khi ghi dữ liệu**, vì nhật ký là ghi tuần tự nên rẻ, còn ghi dữ liệu là ghi ngẫu nhiên nên đắt. Số thứ tự nhật ký định danh từng bản ghi và cho phép biết trang đã được ghi tới đâu. Một giao dịch được coi là chốt khi bản ghi chốt của nó đã nằm trên đĩa, và đó chính là một lần `fsync` theo lesson 53; đây là lý do vật lý khiến số giao dịch mỗi giây bị chặn bởi tốc độ `fsync`. Chốt theo nhóm là cách vượt giới hạn đó: gom nhiều giao dịch rồi đẩy một lần, nên thông lượng tăng mạnh trong khi độ trễ từng giao dịch tăng nhẹ; đây là đánh đổi cấu hình được. Ba mức cam kết bền vững và giá của từng mức, đo được. Nhật ký cũng là nguồn cho nhân bản ở lesson 143 và cho bắt dữ liệu thay đổi ở M17, nên hiểu nó là hiểu hai thứ sau.",
"Đo được quan hệ giữa cấu hình chốt và cặp thông lượng, độ trễ, và phát biểu đúng cam kết bền vững của từng mức.",
"Tầng *phân tích*. Objective nối một tham số cấu hình với một cam kết ngữ nghĩa và một con số. Kiểm bằng bảng ba mức cộng thí nghiệm mất điện; đạt khi ba cam kết phát biểu đúng và số đo đúng chiều.",
"Chạy tải ghi ở ba cấu hình bền vững khác nhau, đo thông lượng và độ trễ phân vị 95 cho từng cái. Giết tiến trình cơ sở dữ liệu cứng giữa lúc ghi và đếm số giao dịch đã chốt còn lại ở mỗi cấu hình. Quan sát tệp nhật ký lớn lên và điểm kiểm tra làm nó được tái sử dụng.",
"Tắt cam kết bền vững trên hệ sản xuất để tăng tốc · nghĩ chốt theo nhóm làm giảm độ trễ · không thử giết tiến trình nên không biết cam kết thật · bỏ qua quan hệ giữa nhật ký và nhân bản.",
"Bảng ba cấu hình có cả thông lượng lẫn độ trễ, số giao dịch sống sót đúng với cam kết đã phát biểu ở cả ba mức."),

(138,"Crash recovery - redo, undo and checkpoints","TH","Lesson 137",
"Sau sự cố, cơ sở dữ liệu phải đưa dữ liệu về trạng thái nhất quán, và nó làm bằng đúng hai thao tác. Làm lại: áp lại các thay đổi đã chốt nhưng chưa kịp ghi xuống trang dữ liệu. Huỷ bỏ: gỡ các thay đổi của giao dịch chưa chốt mà đã kịp ghi xuống trang. Điểm kiểm tra giới hạn lượng nhật ký phải đọc lại khi khôi phục: nó đẩy mọi trang bẩn xuống đĩa và ghi một mốc, nên khôi phục chỉ cần đọc từ mốc đó trở đi. Từ đó suy ra đánh đổi cấu hình: điểm kiểm tra dày thì khôi phục nhanh nhưng tải vào ra nền cao; thưa thì ngược lại, và **thời gian khôi phục là một cam kết vận hành chứ một hằng số**. Ba tình huống hỏng và kết quả của từng tình huống: chưa chốt thì mất, đã chốt thì còn, đang chốt thì phụ thuộc bản ghi chốt đã xuống đĩa chưa. Cách đọc nhật ký khôi phục để biết đã làm lại bao nhiêu.",
"Dự đoán đúng kết cục của ba tình huống hỏng và đo được quan hệ giữa chu kỳ điểm kiểm tra với thời gian khôi phục.",
"Tầng *phân tích*. Objective đòi suy kết cục từ cơ chế, rồi kiểm bằng thí nghiệm hỏng. Kiểm bằng ba tình huống cộng bảng hai chu kỳ; đạt khi dự đoán đúng cả ba và bảng cho thấy đúng chiều đánh đổi.",
"Chạy ba tình huống: giết cơ sở dữ liệu khi có giao dịch chưa chốt, khi vừa chốt xong, và đúng lúc đang chốt. Viết dự đoán trước, rồi khởi động lại và đối chiếu. Đo thời gian khôi phục ở hai chu kỳ điểm kiểm tra khác nhau và ghi tải vào ra nền tương ứng.",
"Nghĩ khôi phục chỉ có làm lại · đặt điểm kiểm tra rất thưa để giảm tải rồi thời gian khôi phục vượt cam kết · không đo thời gian khôi phục bao giờ.",
"Dự đoán đúng kết cục cả ba tình huống, và bảng hai chu kỳ điểm kiểm tra cho thấy đúng chiều đánh đổi có số."),

(139,"ACID and the transaction state machine","LT","Lesson 138",
"Bốn chữ cái được nhắc nhiều và hiểu sai nhiều, nên bài này định nghĩa từng chữ bằng phản ví dụ chứ bằng định nghĩa trừu tượng. Nguyên tử: giao dịch chuyển tiền đứt giữa chừng thì không được trừ mà không cộng; cơ chế là huỷ bỏ ở lesson 138. Nhất quán: các ràng buộc ở lesson 116 vẫn đúng trước và sau; đây là chữ phụ thuộc vào người thiết kế chứ vào engine. Cô lập: giao dịch chạy song song cho kết quả như thể chạy lần lượt, và đây là chữ có nhiều mức nhất, nội dung của lesson 140 tới 142. Bền vững: đã chốt thì sống sót qua sự cố; cơ chế là nhật ký ghi trước ở lesson 137. Máy trạng thái của một giao dịch và các đường chuyển. Vì sao mức cô lập là thứ duy nhất trong bốn chữ được phép hạ xuống để đổi lấy hiệu năng, và hạ tới đâu là câu hỏi của lesson 142.",
"Giải thích mỗi chữ trong bốn chữ bằng một phản ví dụ cụ thể và chỉ ra cơ chế nào bảo đảm nó.",
"Tầng *hiểu*. Bài lý thuyết nối bốn bài trước thành một khung; chuẩn bị cho ba bài sau. Kiểm bằng bài viết phản ví dụ; đạt khi cả bốn có phản ví dụ cụ thể và gắn đúng cơ chế.",
"Với mỗi chữ trong bốn chữ, viết một phản ví dụ bằng dữ liệu cụ thể và chỉ ra cơ chế nào chặn nó. Với chữ nhất quán, nêu rõ phần nào do engine bảo đảm và phần nào do người thiết kế. Vẽ máy trạng thái của một giao dịch và chỉ ra các đường chuyển quan sát được trong hệ thật.",
"Coi cả bốn chữ đều do engine bảo đảm tự động · nghĩ mức cô lập mặc định là mức cao nhất · giải thích bằng định nghĩa trừu tượng mà không có phản ví dụ.",
"Bốn phản ví dụ đều cụ thể và gắn đúng cơ chế, và phần nhất quán phân định rõ trách nhiệm engine với trách nhiệm người thiết kế."),

(140,"Locking, two-phase locking and deadlock detection","TH","Lesson 139",
"Cách thứ nhất để đạt cô lập: chặn truy cập đồng thời bằng khoá. Hai loại khoá và ma trận tương thích; mức chi tiết của khoá từ dòng tới bảng, và đánh đổi giữa mức chi tiết với chi phí quản lý khoá. Khoá hai pha: giai đoạn lấy khoá và giai đoạn nhả khoá không đan xen, và đó là điều kiện để bảo đảm kết quả tương đương chạy lần lượt. Hệ quả vận hành: khoá giữ tới cuối giao dịch, nên **giao dịch dài giữ khoá lâu và chặn người khác**, đây là nguyên nhân số một của hiện tượng cơ sở dữ liệu đột nhiên treo. Khoá chết ở tầng cơ sở dữ liệu: engine phát hiện bằng đồ thị chờ và huỷ một giao dịch làm nạn nhân, nên ứng dụng phải xử lý lỗi bị huỷ và thử lại, theo đúng lesson 104. Cách đọc bảng khoá đang giữ và đang chờ để chẩn đoán một hệ đang bị chặn.",
"Chẩn đoán một hệ bị chặn bằng cách đọc khoá đang giữ và đang chờ, và xử lý đúng khi giao dịch bị huỷ làm nạn nhân.",
"Tầng *phân tích*. Objective là chẩn đoán một sự cố hay gặp và khó đoán từ bên ngoài. Kiểm bằng hai tình huống tiêm sẵn tính giờ; đạt khi định vị đúng giao dịch chặn ở cả hai và xử lý đúng lỗi bị huỷ.",
"Mở một giao dịch dài không chốt rồi chạy tải; quan sát hệ treo và dùng khung nhìn khoá để định vị giao dịch chặn. Tạo khoá chết giữa hai giao dịch, đọc thông báo và xác định nạn nhân. Cài xử lý thử lại cho lỗi bị huỷ và chạy 1000 lần chứng minh không mất giao dịch nào.",
"Khởi động lại cơ sở dữ liệu để gỡ treo · không xử lý lỗi bị huỷ nên mất giao dịch · giữ giao dịch mở trong lúc chờ người dùng · đặt mức khoá bảng cho thao tác chỉ cần khoá dòng.",
"Định vị đúng giao dịch chặn ở cả hai tình huống, và sau khi cài thử lại thì 1000 lần chạy không mất giao dịch nào."),

(141,"MVCC, snapshots and vacuum","TH","Lesson 140",
"Cách thứ hai để đạt cô lập, và là cách PostgreSQL dùng: thay vì chặn, giữ nhiều phiên bản của một dòng để người đọc thấy ảnh chụp tại thời điểm giao dịch bắt đầu. Hệ quả lớn nhất và là lý do cách này thắng trong hệ phân tích: **người đọc không chặn người ghi và ngược lại**. Cái giá là phiên bản cũ tích tụ và phải dọn. Dọn rác cơ sở dữ liệu đánh dấu phiên bản không ai còn thấy là dùng lại được; không chạy hoặc chạy không kịp thì bảng phình và truy vấn chậm dần. Chi tiết quyết định vận hành: **một giao dịch mở rất lâu giữ ảnh chụp cũ, nên không phiên bản nào sau đó dọn được**, và đây là nguyên nhân kinh điển của bảng phình mà không ai hiểu vì sao. Quấn số giao dịch ở mức nhận biết và vì sao nó có thể buộc dừng cơ sở dữ liệu. Ba chỉ số phải theo dõi: tuổi giao dịch cũ nhất, mức phình, và tiến độ dọn.",
"Tái hiện được hiện tượng giao dịch dài chặn việc dọn rác và đo mức phình bảng gây ra.",
"Tầng *phân tích*. Objective đòi nối một hành vi ứng dụng với một hậu quả vận hành, chỗ rất khó đoán nếu không biết cơ chế. Kiểm bằng thí nghiệm có đo; đạt khi tái hiện được hiện tượng và ba chỉ số theo dõi cho thấy đúng nguyên nhân.",
"Mở một giao dịch và để nguyên không chốt. Chạy tải cập nhật liên tục trong 20 phút. Đo mức phình bảng và tuổi giao dịch cũ nhất theo thời gian. Chốt giao dịch kia rồi chạy dọn và đo lại. Dựng cảnh báo trên ba chỉ số.",
"Tin rằng dọn tự động luôn đủ · để giao dịch mở lâu trong mã ứng dụng · dùng lệnh dọn toàn phần trên bảng lớn đang có tải · chỉ theo dõi dung lượng mà không theo dõi tuổi giao dịch.",
"Tái hiện được mức phình tăng khi có giao dịch dài, và sau khi chốt thì dọn đưa mức phình về, cả hai có số đo theo thời gian."),

(142,"Isolation levels chosen by anomaly, not by name","TH","Lesson 141",
"Bài quan trọng nhất của phần giao dịch, và nguyên tắc của nó nằm ngay trong tiêu đề: **chọn mức cô lập theo dị thường cần chặn, không theo tên mức nghe có vẻ an toàn**. Năm dị thường và định nghĩa bằng kịch bản cụ thể: đọc bẩn, đọc không lặp lại, dòng ma, cập nhật mất, và lệch ghi. Hai dị thường cuối là hai dị thường mà người mới gần như không biết tới. Cập nhật mất đã gặp ở lesson 104. Lệch ghi tinh vi hơn: hai giao dịch đọc cùng một điều kiện, mỗi cái ghi một dòng khác nhau, cả hai đều hợp lệ khi xét riêng nhưng kết quả chung vi phạm một bất biến; ví dụ kinh điển là hai bác sĩ cùng xin nghỉ ca trực khi quy định phải còn ít nhất một người. Bảng ánh xạ mức cô lập với dị thường còn lại, kèm cảnh báo rằng cùng một tên mức có hành vi khác nhau giữa các engine. Ba cách chặn lệch ghi.",
"Tái hiện cập nhật mất và lệch ghi ở các mức cô lập, rồi chọn cơ chế chặn đúng theo bất biến cần giữ.",
"Tầng *đánh giá*. Objective đòi chọn theo dị thường chứ theo tên, và là chỗ nhiều hệ thật chọn sai. Kiểm bằng hai thí nghiệm tái hiện cộng bài chọn; đạt khi tái hiện được cả hai dị thường và chọn đúng cơ chế chặn cho ba bất biến cho trước.",
"Tái hiện cập nhật mất và lệch ghi bằng hai phiên chạy song song. Thử lại ở từng mức cô lập và lập bảng dị thường nào còn ở mức nào. Cho ba bất biến nghiệp vụ, chọn mức cô lập hoặc cơ chế khoá để chặn, và chứng minh bằng phép kiểm chạy song song.",
"Chọn mức cô lập theo tên · nghĩ mức cao nhất luôn là lựa chọn đúng · cho rằng cùng tên mức thì cùng hành vi giữa các engine · kiểm bằng phép chạy tuần tự.",
"Tái hiện được cả hai dị thường, bảng ánh xạ đúng, và ba bất biến đều được chặn có phép kiểm chạy song song chứng minh."),

(143,"Replication, lag, failover and split brain","TH","Lesson 142",
"Nhân bản phục vụ ba mục đích khác nhau đã nêu ở góc nhìn hệ thống, nay nhìn từ cơ sở dữ liệu. Hai cách nhân bản: theo nhật ký vật lý sao chép byte của nhật ký ghi trước ở lesson 137 nên bản sao giống hệt bản chính; theo nhật ký logic giải mã thành sự kiện có nghĩa nên nhân bản chọn lọc được và đây chính là cơ chế bắt dữ liệu thay đổi. Đồng bộ và bất đồng bộ: đồng bộ không mất dữ liệu khi bản chính chết nhưng neo độ trễ ghi vào bản sao chậm nhất; bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu, và cửa sổ đó chính là mục tiêu điểm khôi phục. Độ trễ bản sao và hệ quả đọc không thấy thứ vừa ghi. Chuyển đổi khi hỏng và hai rủi ro: não phân đôi khi hai nút cùng tin mình là bản chính, và cần cơ chế rào chặn nút cũ. Kiểm tra bản sao có thật sự bắt kịp chứ chỉ còn kết nối.",
"Đo được độ trễ bản sao dưới tải và thực hiện một lần chuyển đổi có đo lượng dữ liệu mất.",
"Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo. Kiểm bằng lần chuyển đổi thật; đạt khi đo được độ trễ dưới tải và lượng dữ liệu mất khớp với cấu hình đã chọn.",
"Dựng một bản chính và một bản sao bất đồng bộ. Chạy tải ghi và đo độ trễ bản sao. Đọc ngay sau khi ghi trên bản sao và tái hiện hiện tượng không thấy. Giết bản chính, chuyển đổi, và đếm số giao dịch mất. Lặp lại với nhân bản đồng bộ và so hai con số.",
"Đọc bản sao cho bước đối soát · nghĩ bản sao còn kết nối là còn bắt kịp · chuyển đổi mà không rào chặn nút cũ · không đo độ trễ bản sao dưới tải thật.",
"Có số đo độ trễ bản sao dưới tải, và lượng dữ liệu mất khi chuyển đổi khớp với cam kết của cấu hình ở cả hai chế độ."),

(144,"Partitioning against sharding","LT","Lesson 143",
"Hai kỹ thuật chia dữ liệu hay bị gọi lẫn nhưng khác nhau ở một điểm quyết định: phân vùng chia trong một hệ, còn phân mảnh chia sang nhiều hệ, nên phân mảnh kéo theo mọi vấn đề của hệ phân tán. Phân vùng theo khoảng, theo danh sách và theo băm; lợi ích thật là cắt bớt phân vùng khi truy vấn có điều kiện trên khoá phân vùng, và bảo trì theo phân vùng như xoá cả một tháng bằng một thao tác. Chọn khoá phân vùng theo mẫu truy vấn chứ theo trực giác, cùng nguyên tắc sẽ gặp ở M13. Phân mảnh: định tuyến yêu cầu tới mảnh đúng, cân bằng lại khi thêm mảnh, khoá nóng, và **giao dịch bắc qua nhiều mảnh là thứ tốn kém nhất và nên tránh bằng thiết kế**. Ba dấu hiệu cho thấy thật sự cần phân mảnh, và cảnh báo rằng phần lớn hệ dữ liệu ở quy mô vừa không cần, cùng lập luận sẽ gặp lại ở M15.",
"Chọn giữa phân vùng và phân mảnh cho ba tình huống và nêu khoá chia cùng hệ quả lên truy vấn.",
"Tầng *đánh giá*. Objective đòi phân biệt hai kỹ thuật và chống việc phân mảnh quá sớm. Kiểm bằng ba tình huống trong đó ít nhất hai chỉ cần phân vùng; đạt khi chọn đúng cả ba và nêu đúng khoá chia.",
"Phân vùng một bảng 50 triệu dòng theo tháng. Đo chênh lệch byte quét giữa truy vấn có và không có điều kiện trên khoá phân vùng. Xoá một tháng bằng thao tác phân vùng và so thời gian với lệnh xoá thường. Cho ba tình huống và quyết định phân vùng hay phân mảnh.",
"Phân mảnh khi phân vùng đủ · chọn khoá phân vùng không xuất hiện trong điều kiện lọc · thiết kế để mọi truy vấn phải hỏi mọi mảnh · bỏ qua chi phí cân bằng lại.",
"Có số đo chênh lệch byte quét khi cắt phân vùng, và ba tình huống được quyết định đúng kèm khoá chia."),

(145,"Backup, PITR and what a backup is not","LT","Lesson 144",
"Hai loại sao lưu và điều kiện dùng: sao lưu logic xuất ra câu lệnh nên di chuyển được giữa phiên bản và hệ, nhưng chậm và khôi phục lâu; sao lưu vật lý sao chép tệp nên nhanh, đổi lại gắn với phiên bản và kiến trúc. Khôi phục tới một thời điểm: kết hợp một bản sao lưu vật lý với chuỗi nhật ký ghi trước ở lesson 137 để đưa cơ sở dữ liệu về đúng một mốc, và đây là thứ cứu được tình huống xoá nhầm bảng lúc mười giờ sáng. Hai mục tiêu quyết định thiết kế: chịu mất bao nhiêu dữ liệu và chịu ngừng bao lâu; cả hai do nghiệp vụ quyết chứ kỹ thuật tự đặt. Bốn thứ hay bị quên khỏi kế hoạch sao lưu và đều làm nó thất bại đúng lúc cần: cấu hình, bí mật, phần mở rộng, và chính người biết quy trình. **Quy tắc không thoả hiệp: bản sao lưu chưa khôi phục thử thì chưa phải bản sao lưu**, và lesson 146 là buổi diễn tập.",
"Thiết kế kế hoạch sao lưu từ hai mục tiêu nghiệp vụ và nêu bốn thứ phải có ngoài dữ liệu.",
"Tầng *hiểu*. Bài lý thuyết chuẩn bị cho buổi diễn tập ở lesson 146. Kiểm bằng bản kế hoạch; đạt khi hai mục tiêu được nối với tần suất sao lưu cụ thể và nêu đủ bốn thứ hay quên.",
"Phỏng vấn một người đóng vai nghiệp vụ để chốt hai mục tiêu. Từ đó suy ra tần suất sao lưu đầy đủ, tần suất lưu nhật ký, và thời gian giữ. Lập danh mục mọi thứ phải sao lưu ngoài dữ liệu. Ước lượng dung lượng và chi phí lưu trữ cho ba tháng.",
"Kỹ thuật tự đặt hai mục tiêu · chỉ sao lưu dữ liệu mà quên cấu hình và bí mật · đặt thời gian giữ nhật ký ngắn hơn khoảng cách giữa hai lần sao lưu đầy đủ · chưa từng tính dung lượng.",
"Hai mục tiêu được nối với tần suất cụ thể, danh mục nêu đủ bốn thứ ngoài dữ liệu, và có ước lượng dung lượng ba tháng."),

(146,"The restore drill","TH","Lesson 145",
"Buổi diễn tập, và đây là bài mà bỏ qua thì cả module vô nghĩa. Kịch bản: mười giờ sáng có người chạy nhầm lệnh xoá một bảng quan trọng trên hệ sản xuất; nhiệm vụ là khôi phục về trạng thái ngay trước thời điểm đó, trên một máy mới, với cơ sở dữ liệu vẫn đang nhận ghi từ các bảng khác. Quy trình sáu bước và mỗi bước có điểm kiểm chứng riêng. Hai đại lượng phải đo trong lúc làm chứ ước lượng sau: thời gian từ lúc bắt đầu tới lúc phục vụ lại được, và lượng dữ liệu mất thật. So hai con số đo được với hai mục tiêu đã chốt ở lesson 145, và **nếu không đạt thì kế hoạch sai chứ buổi diễn tập sai**. Ba tình huống phát sinh hay gặp trong lúc khôi phục: thiếu phần mở rộng, sai phiên bản, và hết dung lượng đĩa. Viết lại quy trình thành sổ tay sau buổi diễn tập theo chuẩn ở lesson 10.",
"Khôi phục thành công về một mốc thời gian trên máy mới, đo hai đại lượng, và so với hai mục tiêu đã chốt.",
"Tầng *áp dụng*. Objective là một thao tác vận hành có hai số đo so với cam kết. Kiểm bằng buổi diễn tập tính giờ cộng đối soát dữ liệu; đạt khi dữ liệu khôi phục khớp trạng thái tại mốc và hai số đo được ghi lại.",
"Chạy buổi diễn tập theo kịch bản. Khôi phục về mốc ngay trước lệnh xoá nhầm, trên máy mới. Đối soát dữ liệu với bản chụp đã lưu trước đó. Đo cả hai đại lượng. So với hai mục tiêu và ghi rõ chỗ không đạt. Viết sổ tay khôi phục từ chính quy trình vừa làm.",
"Khôi phục trên chính máy đang hỏng · bỏ qua bước đối soát sau khi khôi phục · ước lượng thời gian thay vì đo · không ghi lại quy trình nên lần sau làm lại từ đầu.",
"Dữ liệu khôi phục khớp trạng thái tại mốc, hai đại lượng được đo và so với mục tiêu, và sổ tay viết ra từ quy trình thật."),

(147,"Operating a database day to day","TH","Lesson 146",
"Sáu việc vận hành định kỳ và chỉ số đi kèm từng việc. Kết nối và hồ kết nối: số kết nối tối đa là tài nguyên hữu hạn, và mỗi kết nối tốn bộ nhớ, nên hồ đặt ở phía ứng dụng theo lesson 103 là bắt buộc chứ tuỳ chọn. Truy vấn chậm: bật ghi nhật ký truy vấn vượt ngưỡng và rà định kỳ, đây là nguồn đầu vào cho việc tối ưu ở lesson 132. Phình bảng và dọn rác theo lesson 141. Thống kê theo lesson 128, và lịch cập nhật sau các đợt nạp lớn. Dung lượng: theo dõi tốc độ tăng chứ mức hiện tại, để biết trước khi đầy chứ lúc đầy. Nâng cấp: nâng cấp nhỏ và nâng cấp lớn khác nhau ở chỗ có cần chuyển đổi định dạng dữ liệu không, và nâng cấp lớn cần kế hoạch cùng đường lùi theo lesson 98. Bốn cảnh báo tối thiểu một cơ sở dữ liệu sản xuất phải có.",
"Dựng bộ theo dõi sáu việc vận hành với ngưỡng cảnh báo có căn cứ và rà được truy vấn chậm.",
"Tầng *áp dụng*. Objective là một cấu hình vận hành kiểm được bằng việc phát hiện sự cố trước khi người dùng báo. Kiểm bằng bốn sự cố tiêm sẵn; đạt khi cảnh báo phát hiện ít nhất ba trước khi tác động tới truy vấn.",
"Dựng theo dõi cho sáu việc. Đặt bốn cảnh báo tối thiểu với ngưỡng dẫn từ phân bố đo được chứ số tròn. Giảng viên tiêm bốn sự cố: cạn kết nối, phình bảng, thống kê cũ, và dung lượng tăng nhanh bất thường. Ghi cảnh báo nào phát hiện được và phát hiện trước bao lâu.",
"Đặt ngưỡng bằng số tròn · theo dõi dung lượng hiện tại mà không theo dõi tốc độ tăng · không giới hạn số kết nối ở phía ứng dụng · nâng cấp lớn mà không có đường lùi.",
"Cảnh báo phát hiện ≥ 3/4 sự cố trước khi tác động tới truy vấn, và mọi ngưỡng dẫn được từ phân bố đo được."),

(148,"Gate 4 - trace a write and defend an isolation choice","KT","Lesson 147",
"Cổng của Phase 4. Bài kiểm hai năng lực: viết và tối ưu SQL có bằng chứng ở M9, và hiểu cùng vận hành cơ sở dữ liệu ở M10. Không có nội dung mới.",
"Truy được đường đi của một lệnh ghi từ câu lệnh tới khôi phục, bảo vệ một lựa chọn mức cô lập theo dị thường, và khôi phục thành công.",
"Tầng *đánh giá*. Cổng đo năng lực tổng hợp gồm cả một thao tác vận hành có rủi ro thật, nên hình thức là bài làm cộng diễn tập.",
"Buổi 120 phút: 75 phút làm bài độc lập, 45 phút chữa bài. Bài chấm sáu phần: A (20đ) truy đường đi của một lệnh chèn từ câu lệnh tới nhật ký ghi trước, tới trang, tới điểm kiểm tra và tới khôi phục · B (20đ) tối ưu hai truy vấn chậm, mỗi tối ưu dẫn về một quan sát trong kế hoạch và kết quả khớp tuyệt đối · C (20đ) chọn mức cô lập cho hai bất biến cho trước và chứng minh bằng phép kiểm chạy song song · D (20đ) khôi phục về một mốc thời gian và đối soát khớp · E (10đ) chẩn đoán một hệ đang bị chặn bằng khung nhìn khoá · F (10đ) nêu ba chỉ số vận hành phải theo dõi và ngưỡng dẫn từ phân bố.",
"Chọn mức cô lập theo tên · tối ưu làm đổi kết quả · bỏ phần khôi phục vì tốn thời gian · chứng minh bất biến bằng phép chạy tuần tự.",
"Đạt ≥ 70/100, phần C và D đều ≥ 60%. Bất biến chỉ chứng minh bằng phép chạy tuần tự thì phần C bằng không; khôi phục không đối soát thì phần D bằng không."),
]
