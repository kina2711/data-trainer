# -*- coding: utf-8 -*-
"""DE M17 Elasticsearch + M18 Choosing a database."""

M17 = ("Elasticsearch", 175, 182, """| | |
|---|---|
| **Objective cấp module** | Thiết kế ánh xạ và bộ phân tích cho một tải tìm kiếm, và chẩn đoán được ba sự cố vận hành đặc trưng: quá nhiều mảnh, áp lực bộ nhớ, và độ trễ làm mới |
| **Tiền đề** | M11 |
| **Exit criterion** | Tìm kiếm nhật ký tiếng Việt cho kết quả đúng, đổi được ánh xạ bằng lập chỉ mục lại không ngừng phục vụ, và sửa được một cụm quá nhiều mảnh |
| **Kỹ năng SFIA** | `DBAD` mức 3 · `SYSP` mức 3 |
| **Chế độ hỏng** | Dùng Elasticsearch làm nguồn dữ liệu gốc hoặc làm kho phân tích chung, rồi gặp mất dữ liệu và chi phí bộ nhớ không kiểm soát |""",
"Mức `B`. Elasticsearch giải một bài toán hẹp là tìm kiếm toàn văn và lọc trên dữ liệu bán cấu trúc, và mọi đặc tính vận hành của nó suy ra từ chỉ mục ngược cùng mô hình phân đoạn bất biến. Module bám hai thứ đó. Ba bài cuối là vận hành, vì đây là hệ mà sự cố vận hành hay gặp nhất trong bảy hệ.")

L17 = [
(175,"The inverted index and why search is a different problem","LT","Module 17: M11",
"Chỉ mục ngược ánh xạ từ khoá tới danh sách tài liệu chứa nó, ngược với chỉ mục cây B ánh xạ khoá tới vị trí dòng, nối lại lesson 111. Hệ quả: tìm tài liệu chứa một từ là tra một lần rồi đọc danh sách, chi phí tỉ lệ số tài liệu khớp chứ không tỉ lệ kích thước tập. Đây là lý do tìm kiếm toàn văn trên hệ quan hệ bằng khớp mẫu có ký tự đại diện ở đầu luôn chậm, nối lại lesson 94. Từ điển từ khoá và danh sách vị trí, cùng dung lượng chúng chiếm. Chấm điểm liên quan và ba yếu tố của nó: tần suất từ trong tài liệu, độ hiếm của từ trong tập, và độ dài tài liệu. Hệ quả quan trọng cho công việc dữ liệu: kết quả có thứ tự theo điểm chứ không theo giá trị, nên nó trả lời câu hỏi cái nào liên quan nhất chứ không trả lời câu hỏi có bao nhiêu cái. Phân biệt ngữ cảnh truy vấn có chấm điểm với ngữ cảnh lọc không chấm điểm và được đệm.",
"Giải thích vì sao chỉ mục ngược nhanh cho tìm kiếm mà chậm cho gộp nhóm, và phân biệt ngữ cảnh truy vấn với ngữ cảnh lọc bằng số đo.",
"Tầng *hiểu*. Bài lý thuyết nối cấu trúc với hành vi. Đạt khi giải thích đúng hai chiều của chỉ mục ngược, và khi thực nghiệm cho thấy cùng một điều kiện đặt trong ngữ cảnh lọc nhanh hơn rõ rệt so với đặt trong ngữ cảnh truy vấn khi chạy lặp.",
"Nạp 5 triệu bản ghi nhật ký. Chạy một tìm kiếm toàn văn và so với khớp mẫu tương đương trên PostgreSQL. Chạy cùng một điều kiện lọc trong hai ngữ cảnh, mỗi cái 100 lần, so độ trễ. Chạy một phép gộp nhóm trên 5 triệu tài liệu và so với ClickHouse.",
"Dùng Elasticsearch làm kho phân tích chung · đặt điều kiện lọc vào ngữ cảnh truy vấn nên mất bộ đệm · trông chờ thứ tự kết quả theo giá trị.",
"Hai chiều của chỉ mục ngược được giải thích đúng, và thực nghiệm cho thấy chênh lệch giữa hai ngữ cảnh."),

(176,"Analyzers, tokenizers and Vietnamese text","TH","Lesson 175",
"Bộ phân tích biến văn bản thành từ khoá và nó chạy ở hai thời điểm: lúc lập chỉ mục và lúc truy vấn. Hai lần phải dùng cùng một bộ phân tích, nếu không thì từ khoá sinh ra không khớp và tìm không ra, một lỗi âm thầm vì không có thông báo. Ba thành phần: bộ lọc ký tự, bộ tách từ, và bộ lọc từ khoá. Bộ tách từ theo khoảng trắng hợp tiếng Anh nhưng không hợp tiếng Việt vì tiếng Việt có từ ghép nhiều âm tiết, nên tách theo khoảng trắng cho ra âm tiết chứ không cho ra từ. Ba cách xử lý tiếng Việt và đánh đổi: giữ nguyên âm tiết rồi dựa vào truy vấn cụm từ, dùng ghép n âm tiết, hoặc dùng bộ tách từ tiếng Việt chuyên dụng. Chuẩn hoá dấu và chữ hoa chữ thường, nối lại lesson 8 về chuẩn hoá Unicode. Từ dừng và vì sao loại chúng có hại cho một số truy vấn. Kiểm bộ phân tích bằng giao diện phân tích thử trước khi lập chỉ mục.",
"Thiết kế bộ phân tích cho nhật ký tiếng Việt và chứng minh nó tìm đúng bằng một tập kiểm chứng có đáp án.",
"Tầng *áp dụng*. Objective có tiêu chí đối chứng bằng tập kiểm chứng. Đạt khi đạt ít nhất 90% độ chính xác trên 50 truy vấn có đáp án, và khi chứng minh được trường hợp dùng khác bộ phân tích ở hai thời điểm làm tìm không ra.",
"Dựng tập 50 truy vấn tiếng Việt có đáp án trên 1 triệu bản ghi. Thử ba cách xử lý tiếng Việt, đo độ chính xác từng cách. Dùng giao diện phân tích thử xem từ khoá sinh ra cho ba câu mẫu. Cố ý đặt bộ phân tích truy vấn khác bộ phân tích lập chỉ mục và quan sát kết quả rỗng.",
"Tách tiếng Việt theo khoảng trắng rồi tìm cụm từ không ra · đổi bộ phân tích mà không lập chỉ mục lại · loại từ dừng rồi mất truy vấn cụm từ chứa chúng.",
"Đạt ít nhất 90% độ chính xác trên 50 truy vấn có đáp án, và chứng minh được ca lệch bộ phân tích."),

(177,"Mapping, dynamic mapping and field explosion","TH","Lesson 176",
"Ánh xạ khai báo kiểu của từng trường, và ánh xạ động tự suy kiểu từ tài liệu đầu tiên chứa trường đó. Ánh xạ động tiện lúc thử nghiệm nhưng nguy hiểm trong sản xuất vì hai lý do: kiểu suy sai từ một tài liệu bất thường rồi cố định mãi, và trường mới tự động thêm làm số trường tăng không kiểm soát. Nổ số trường là sự cố kinh điển: nhật ký có trường tên động theo dữ liệu tạo ra hàng nghìn trường, làm siêu dữ liệu cụm phình và cụm chậm. Cách chặn: tắt ánh xạ động, đặt giới hạn số trường, và dùng kiểu đối tượng phẳng cho dữ liệu không biết trước hình dạng. Hai kiểu cho chuỗi và khác biệt quyết định: kiểu văn bản được phân tích nên tìm kiếm được nhưng không gộp nhóm và không sắp xếp được; kiểu từ khoá không phân tích nên khớp chính xác, gộp nhóm và sắp xếp được. Khai báo cả hai cho một trường bằng trường con là mẫu mặc định. Ánh xạ không sửa được sau khi lập chỉ mục, chỉ thêm trường mới được.",
"Thiết kế ánh xạ tường minh cho nhật ký ứng dụng và chứng minh nó chặn được nổ số trường, so với ánh xạ động.",
"Tầng *áp dụng*. Objective có tiêu chí đếm được. Đạt khi nạp cùng tập dữ liệu vào hai chỉ mục, chỉ mục động vượt 1.000 trường còn chỉ mục tường minh giữ dưới 50, và khi giải thích đúng vì sao một trường kiểu văn bản không gộp nhóm được.",
"Nạp 2 triệu bản ghi nhật ký có trường động vào hai chỉ mục: một ánh xạ động, một ánh xạ tường minh có giới hạn trường. Đếm số trường mỗi bên. Thử gộp nhóm trên trường kiểu văn bản và quan sát lỗi, rồi dùng trường con kiểu từ khoá. Thử sửa kiểu một trường đã có và quan sát nó không làm được.",
"Để ánh xạ động trong sản xuất · dùng kiểu văn bản cho trường cần gộp nhóm · trông chờ sửa được kiểu trường sau khi đã lập chỉ mục.",
"Chỉ mục động vượt 1.000 trường còn tường minh dưới 50, và ca gộp nhóm trên kiểu văn bản được giải thích đúng."),

(178,"Segments, refresh and the near-real-time illusion","TH","Lesson 177",
"Phân đoạn là đơn vị lưu trữ bất biến: ghi mới vào bộ đệm trong bộ nhớ, định kỳ tạo phân đoạn mới, và phân đoạn nhỏ được trộn thành lớn, cấu trúc cùng họ với lesson 167. Làm mới là thao tác biến bộ đệm thành phân đoạn tìm kiếm được, mặc định mỗi một giây, nên dữ liệu vừa ghi không tìm thấy ngay; đây là nghĩa chính xác của gần thời gian thực và là nguồn hiểu nhầm phổ biến khi kiểm thử. Nhật ký giao dịch bảo đảm bền vững giữa hai lần làm mới, cùng vai trò với nhật ký ghi trước ở lesson 118. Xoá là đánh dấu chứ không xoá thật, và không gian chỉ thu hồi khi trộn, nên tỉ lệ tài liệu đã xoá là một chỉ số cần theo dõi. Cập nhật là xoá cộng chèn lại cả tài liệu, nên cập nhật một trường vẫn ghi lại toàn bộ. Tăng khoảng làm mới cho tải nạp lớn và tắt hẳn khi nạp một lần, một đòn bẩy nạp nhanh hay bị bỏ qua.",
"Đo độ trễ giữa lúc ghi và lúc tìm thấy, và tăng thông lượng nạp bằng cách chỉnh khoảng làm mới.",
"Tầng *áp dụng*. Objective có hai số đo cụ thể. Đạt khi đo được độ trễ ghi tới tìm thấy ở ba cấu hình làm mới, và khi thông lượng nạp tăng ít nhất 50% khi tắt làm mới trong lúc nạp lô lớn.",
"Ghi một tài liệu rồi truy vấn ngay trong vòng lặp, đo độ trễ tới khi tìm thấy, lặp 100 lần ở ba khoảng làm mới. Nạp 10 triệu tài liệu với làm mới mặc định, rồi với làm mới tắt, so thông lượng. Cập nhật một trường của 1 triệu tài liệu và đo tỉ lệ tài liệu đã xoá.",
"Kiểm thử ghi rồi đọc ngay mà không tính khoảng làm mới · để làm mới mặc định khi nạp khối lượng lớn · cập nhật một trường thường xuyên như với hệ quan hệ.",
"Độ trễ ghi tới tìm thấy đo được ở ba cấu hình, và thông lượng nạp tăng ít nhất 50% khi tắt làm mới."),

(179,"Shards, replicas and the too-many-shards problem","TH","Lesson 178",
"Chỉ mục chia thành mảnh chính, mỗi mảnh là một chỉ mục Lucene độc lập, và mảnh sao là bản sao của mảnh chính. Số mảnh chính cố định khi tạo chỉ mục và không đổi được, nên đây là quyết định khó đảo ngược thứ hai sau ánh xạ. Quá nhiều mảnh là sự cố phổ biến nhất của Elasticsearch: mỗi mảnh tốn bộ nhớ cho siêu dữ liệu và tốn tài nguyên cho trộn, nên một cụm hàng chục nghìn mảnh nhỏ chậm hơn hẳn cụm ít mảnh lớn dù cùng dữ liệu. Quy tắc kích thước mảnh hợp lý và cách tính số mảnh từ tổng dung lượng dự kiến. Nguyên nhân gốc thường là tạo chỉ mục theo ngày cho dữ liệu ít, cùng sai lầm với phân vùng theo ngày ở lesson 168. Vòng đời chỉ mục và chính sách cuộn theo kích thước thay vì theo thời gian, cách chữa đúng. Phân bổ mảnh và cân bằng lại. Mảnh sao tăng khả năng đọc và tăng dung lượng gấp đôi.",
"Tính số mảnh hợp lý cho một khối lượng dữ liệu dự kiến, và sửa một cụm quá nhiều mảnh bằng chính sách cuộn theo kích thước.",
"Tầng *đánh giá*. Objective đòi một phép tính và một quyết định vận hành. Đạt khi số mảnh tính ra nằm trong khoảng hợp lý theo quy tắc kích thước, và khi sau khi áp chính sách cuộn thì số mảnh giảm ít nhất 10 lần với cùng khối lượng dữ liệu, kèm số đo độ trễ truy vấn trước sau.",
"Dựng cụm có 5.000 mảnh nhỏ bằng cách tạo chỉ mục theo ngày cho dữ liệu ít. Đo bộ nhớ cụm và độ trễ truy vấn. Tính số mảnh hợp lý cho khối lượng đó. Áp chính sách cuộn theo kích thước, lập chỉ mục lại, đo lại. Thử đổi số mảnh chính của một chỉ mục đã có và quan sát nó không làm được.",
"Tạo chỉ mục theo ngày cho dữ liệu vài trăm mê ga byte mỗi ngày · đặt số mảnh cao để phòng xa · thêm mảnh sao khi nút cổ chai là bộ nhớ chứ không phải đọc.",
"Số mảnh tính ra nằm trong khoảng hợp lý, và sau khi áp chính sách cuộn số mảnh giảm ít nhất 10 lần kèm số đo độ trễ."),

(180,"Heap pressure, circuit breakers and cluster health","TH","Lesson 179",
"Elasticsearch chạy trên máy ảo có thu gom rác, nên bộ nhớ vùng đống là tài nguyên khan hiếm nhất và phần lớn sự cố quy về nó, nối lại lesson 13. Quy tắc kích thước vùng đống và lý do không đặt quá ngưỡng nén con trỏ. Phần bộ nhớ còn lại dành cho bộ đệm trang của hệ điều hành mà Lucene dựa vào, nối lại lesson 22, nên đặt vùng đống bằng toàn bộ RAM là sai theo hai hướng cùng lúc. Bốn thứ chiếm vùng đống nhiều nhất: siêu dữ liệu mảnh, dữ liệu trường cho gộp nhóm trên trường kiểu văn bản, bộ đệm truy vấn, và kết quả trung gian của gộp nhóm sâu. Cầu dao chặn thao tác dự kiến vượt ngưỡng bộ nhớ và trả lỗi thay vì để tiến trình chết, và đọc thông báo cầu dao là cách chẩn đoán trực tiếp. Tạm dừng do thu gom rác kéo dài làm nút bị coi là chết và bị loại khỏi cụm, gây cân bằng lại và làm mọi thứ tệ hơn. Ba trạng thái sức khoẻ cụm và nghĩa của từng cái.",
"Chẩn đoán một cụm áp lực bộ nhớ về đúng một trong bốn nguyên nhân, và chỉnh cấu hình để cầu dao chặn thay vì nút chết.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt bốn nguyên nhân cùng triệu chứng. Kiểm bằng ba ca dựng sẵn; đạt khi định vị đúng ít nhất hai và mỗi lần dẫn được số đo bộ nhớ theo thành phần, và khi sau khi chỉnh thì thao tác nặng bị cầu dao chặn thay vì làm nút chết.",
"Dựng ba ca: gộp nhóm trên trường kiểu văn bản, gộp nhóm sâu nhiều tầng, và quá nhiều mảnh. Với mỗi ca đọc phân bố bộ nhớ vùng đống theo thành phần. Chỉnh ngưỡng cầu dao và chạy lại ca nặng nhất, xác nhận bị chặn. Đặt vùng đống bằng toàn bộ RAM và quan sát hiệu năng giảm.",
"Đặt vùng đống bằng toàn bộ RAM · gộp nhóm trên trường kiểu văn bản · tăng vùng đống để chữa khi nguyên nhân là quá nhiều mảnh.",
"Định vị đúng ít nhất hai trên ba ca có số đo bộ nhớ theo thành phần, và cầu dao chặn được thao tác nặng."),

(181,"Reindexing and changing a mapping without downtime","TH","Lesson 180",
"Ánh xạ không sửa được nên đổi kiểu một trường đòi lập chỉ mục lại toàn bộ, thao tác tốn thời gian tỉ lệ khối lượng dữ liệu. Bí danh chỉ mục là lớp gián tiếp giữa ứng dụng và chỉ mục vật lý, và nó là thứ cho phép làm việc này không ngừng phục vụ: ứng dụng luôn trỏ vào bí danh, còn bí danh chuyển từ chỉ mục cũ sang chỉ mục mới bằng một thao tác nguyên tử. Quy trình bốn bước: tạo chỉ mục mới với ánh xạ mới, lập chỉ mục lại dữ liệu cũ, bắt kịp phần ghi mới phát sinh trong lúc lập lại, rồi chuyển bí danh. Bước ba là bước khó và có hai cách: ghi đôi vào cả hai chỉ mục, hoặc lập lại theo khoảng thời gian rồi chạy bù phần chênh. Đây cùng mẫu mở rộng rồi thu hẹp với lesson 121. Tăng tốc lập chỉ mục lại bằng tắt làm mới và bỏ mảnh sao tạm thời, nối lại lesson 178. Theo dõi tiến độ và khôi phục khi thất bại giữa chừng.",
"Đổi kiểu một trường trên chỉ mục 20 triệu tài liệu đang có tải, không ngừng phục vụ và không mất tài liệu nào.",
"Tầng *sáng tạo*. Objective là thiết kế một quy trình nhiều bước dưới ràng buộc không ngừng phục vụ. Đạt khi số tài liệu chỉ mục mới bằng số cũ cộng số ghi phát sinh trong lúc chuyển, không lệch một tài liệu, và khi truy vấn qua bí danh không lỗi lần nào suốt quá trình.",
"Chỉ mục 20 triệu tài liệu có tải ghi 500 tài liệu mỗi giây và tải đọc liên tục. Đổi kiểu một trường theo quy trình bốn bước qua bí danh. Đếm tài liệu ở cả hai chỉ mục và đối soát. Ghi lại số lỗi truy vấn suốt quá trình. Đo thời gian lập chỉ mục lại có và không tắt làm mới.",
"Cho ứng dụng trỏ thẳng vào tên chỉ mục thay vì bí danh · bỏ qua phần ghi phát sinh trong lúc lập lại · để mảnh sao bật trong suốt quá trình lập lại.",
"Số tài liệu đối soát khớp tuyệt đối, và không lỗi truy vấn nào qua bí danh suốt quá trình."),

(182,"Log search at scale - a working system","TH","Lesson 181",
"Không có cơ chế mới. Bài gộp module: dựng một hệ tìm kiếm nhật ký hoàn chỉnh dùng mọi thứ đã học. Yêu cầu: ánh xạ tường minh có giới hạn trường từ lesson 177, bộ phân tích tiếng Việt đạt ngưỡng chính xác từ lesson 176, chính sách vòng đời cuộn theo kích thước từ lesson 179, khoảng làm mới chỉnh theo tải nạp từ lesson 178, và giám sát bộ nhớ vùng đống theo thành phần từ lesson 180. Tiêu chí vận hành: số mảnh giữ trong ngưỡng khi dữ liệu tăng qua ba tháng mô phỏng, và độ trễ truy vấn phân vị 95 dưới ngưỡng đặt trước. Phần kết luận bắt buộc: nêu rõ ba loại truy vấn nên chuyển sang hệ khác thay vì cố làm ở đây, thường là gộp nhóm lớn, kết nhiều nguồn, và báo cáo chính xác tuyệt đối. Báo cáo là một trong bảy đầu vào của M18.",
"Dựng hệ tìm kiếm nhật ký đạt ngưỡng độ chính xác và độ trễ, và nêu ba loại truy vấn nên chuyển sang hệ khác kèm lý do.",
"Tầng *sáng tạo*. Objective là thiết kế một hệ dưới nhiều ràng buộc cùng lúc, cộng một phán đoán về ranh giới áp dụng. Chấm theo bốn mục: độ chính xác tìm kiếm 30đ, chỉ số vận hành 30đ, quy trình đổi ánh xạ 20đ, và phần nêu ranh giới 20đ. Đạt khi ≥ 70/100 và phần nêu ranh giới ≥ 50%, vì biết khi nào không dùng là một nửa giá trị của module.",
"Dựng hệ tìm kiếm cho 200 triệu dòng nhật ký tiếng Việt mô phỏng ba tháng. Đo độ chính xác trên tập 50 truy vấn có đáp án, số mảnh theo thời gian, và độ trễ phân vị 95. Chạy một lần đổi ánh xạ qua bí danh. Viết phần nêu ba loại truy vấn nên chuyển sang hệ khác kèm số đo so sánh.",
"Mở rộng dần sang làm cả báo cáo phân tích trên cùng cụm · bỏ phần nêu ranh giới vì hệ đang chạy tốt · đo độ trễ lúc cụm rỗi.",
"Đạt ≥ 70/100 và phần nêu ranh giới ≥ 50%, với ba loại truy vấn có số đo so sánh."),
]

M18 = ("Choosing a Database - Polyglot Design and Defence", 183, 188, """| | |
|---|---|
| **Objective cấp module** | Thiết kế một sơ đồ dữ liệu nhiều hệ cho một ứng dụng thật và bảo vệ mọi lựa chọn bằng số đo từ bảy module trước |
| **Tiền đề** | M11 · M12 · M13 · M14 · M15 · M16 · M17 |
| **Exit criterion** | Đạt Cổng 4 ≥ 70/100: bảo vệ sơ đồ đa hệ trước hội đồng, giữ vững hoặc đổi kết luận có lý do khi một ràng buộc bị thay giữa buổi |
| **Kỹ năng SFIA** | `ARCH` mức 4 · `DBAD` mức 4 |
| **Chế độ hỏng** | Chọn hệ theo công nghệ đang thịnh hành hoặc theo một bài so sánh trên mạng, rồi không bảo vệ được khi bị hỏi về tải cụ thể |""",
"Module chỉ chạy được vì bảy module trước đã đo trên cùng một use case. Không cùng bài toán thì đây là bài liệt kê tính năng, không phải bài so sánh, cùng ràng buộc với M25 và M31. Năm bài dựng tiêu chí và đối soát, bài cuối là Cổng 4.")

L18 = [
(183,"Seven systems, one use case - assembling the evidence","TH","Module 18: M11 · M12 · M13 · M14 · M15 · M16 · M17",
"Tập hợp số đo từ bảy module thành một bảng duy nhất, và đây là bước lộ ra chỗ đo không so được: khác phần cứng, khác khối lượng dữ liệu, khác định nghĩa chỉ số. Chín trục đo và cách chuẩn hoá từng trục để so được: mô hình dữ liệu tự nhiên cho miền nghiệp vụ, thông lượng ghi, độ trễ đọc theo khoá, độ trễ truy vấn phân tích, khả năng kết nhiều nguồn, bảo đảm giao dịch, điểm phục hồi và thời lượng phục hồi, công sức vận hành, và chi phí. Nguyên tắc chuẩn hoá: cùng khối lượng dữ liệu, cùng phần cứng hoặc quy về đơn vị tài nguyên, và cùng định nghĩa chỉ số, nhất là phân vị. Ô nào chưa đo được thì ghi là chưa đo, không ghi là tương đương. Ba trục không đo được bằng lab ngắn và phải ghi rõ giới hạn: độ ổn định dài hạn, chất lượng hệ sinh thái công cụ, và chi phí nhân sự.",
"Lập bảng chín trục nhân bảy hệ từ số đo của chính mình, và đánh dấu rõ ô nào chưa đo được cùng lý do.",
"Tầng *phân tích*. Objective đòi chuẩn hoá số đo để chúng so được, việc khó hơn thu thập. Đạt khi ít nhất 45 trên 63 ô có số đo từ lab, khi mọi ô còn lại được đánh dấu chưa đo kèm lý do, và khi ba trục không đo được bằng lab ngắn được nêu rõ.",
"Thu số đo từ bảy module. Với mỗi trục, kiểm ba điều kiện chuẩn hoá và ghi lại ô nào vi phạm. Đo bổ sung cho ô thiếu khi chi phí chấp nhận được. Lập bảng chín nhân bảy. Đổi bảng chéo với một học viên khác và rà soát điều kiện chuẩn hoá.",
"Điền ô bằng con số từ tài liệu nhà cung cấp · ghi tương đương cho ô chưa đo · so độ trễ trung bình của hệ này với phân vị 95 của hệ kia.",
"Ít nhất 45 trên 63 ô có số đo từ lab, ô còn lại đánh dấu chưa đo kèm lý do, và ba trục ngoài tầm lab được nêu."),

(184,"The decision matrix - workload shapes, not system rankings","LT","Lesson 183",
"Câu hỏi đúng không phải hệ nào tốt hơn mà là tải nào hợp hệ nào, và đổi cách hỏi là nội dung chính của bài. Sáu hình dạng tải và hệ hợp với từng cái: giao dịch nhiều ghi nhỏ cần ràng buộc, đọc theo khoá độ trễ thấp, phân tích quét lớn, tìm kiếm toàn văn, dữ liệu hình dạng thay đổi, và chuỗi sự kiện chỉ chèn thêm. Bảy yếu tố phải cân trước khi chọn, theo thứ tự tôi đề nghị: hình dạng dữ liệu và mẫu truy cập, yêu cầu nhất quán, khối lượng và tốc độ tăng, điểm phục hồi và thời lượng phục hồi, kỹ năng đội, chi phí vận hành, và cuối cùng mới là hiệu năng thô. Đặt hiệu năng cuối là có chủ đích: nó là yếu tố dễ đo nhất nên hay bị cân nặng quá mức, trong khi kỹ năng đội và chi phí vận hành quyết định thành bại nhiều hơn. Ba dấu hiệu một lựa chọn sai: phải viết nhiều mã để bù thiếu sót của hệ, phải đồng bộ thủ công giữa hai hệ, và không ai trong đội chẩn đoán được khi hỏng.",
"Ánh xạ sáu hình dạng tải sang hệ phù hợp, và giải thích vì sao hiệu năng thô đặt cuối trong bảy yếu tố.",
"Tầng *hiểu*. Bài lý thuyết dựng khung quyết định cho ba bài sau. Đạt khi ánh xạ đúng ít nhất năm trên sáu hình dạng kèm lý do từ bảng ở lesson 183, và khi lập luận về thứ tự bảy yếu tố nêu được ít nhất hai hậu quả cụ thể của việc cân hiệu năng quá mức.",
"Nhận sáu mô tả tải thật. Ánh xạ từng cái sang một hoặc hai hệ, dẫn ô cụ thể trong bảng lesson 183. Với hai tải, viết kịch bản chọn theo hiệu năng thô và chỉ ra hậu quả sau một năm. Thảo luận nhóm ba dấu hiệu lựa chọn sai từ kinh nghiệm lab.",
"Xếp hạng bảy hệ từ tốt tới tệ · chọn theo công nghệ đang thịnh hành · bỏ qua kỹ năng đội vì nghĩ có thể học.",
"Ánh xạ đúng ít nhất năm trên sáu hình dạng có dẫn chứng, và lập luận về thứ tự nêu hai hậu quả cụ thể."),

(185,"Polyglot architecture - synchronising two systems","TH","Lesson 184",
"Dùng nhiều hệ là chuyện bình thường, nhưng mỗi hệ thêm vào là một bài toán đồng bộ, và chi phí đó thường bị bỏ qua lúc thiết kế. Ba cách đồng bộ và đánh đổi: ghi đôi từ ứng dụng đơn giản nhưng không nguyên tử nên hai hệ lệch khi một bên lỗi, bắt thay đổi dữ liệu từ nguồn gốc đáng tin hơn và là nội dung chặng 6, và đồng bộ theo lô định kỳ rẻ nhất nhưng độ trễ cao. Mẫu hộp thư đi để ghi đôi trở nên đáng tin: ghi dữ liệu và ghi bản tin vào cùng một giao dịch, rồi một tiến trình riêng đọc bản tin và đẩy sang hệ thứ hai. Nguồn sự thật phải chỉ định rõ một hệ duy nhất, và mọi hệ khác là bản dẫn xuất dựng lại được; không có quy tắc này thì khi hai bên lệch không ai biết bên nào đúng. Đối soát định kỳ giữa hai hệ như một phép kiểm bắt buộc, nối lại lesson 104. Ba câu hỏi phải trả lời trước khi thêm hệ thứ hai.",
"Thiết kế đường đồng bộ giữa hai hệ cho một use case, chỉ định nguồn sự thật, và cài phép đối soát phát hiện được lệch.",
"Tầng *áp dụng*. Objective có sản phẩm và một phép kiểm chứng. Đạt khi đường đồng bộ chạy và phép đối soát phát hiện được lệch do lỗi bơm vào, và khi tài liệu chỉ rõ nguồn sự thật cùng cách dựng lại hệ dẫn xuất từ nó.",
"Đồng bộ đơn hàng từ PostgreSQL sang Elasticsearch để tìm kiếm. Cài ghi đôi trần, bơm lỗi ở bên thứ hai, đo số bản ghi lệch. Cài lại bằng mẫu hộp thư đi, lặp thí nghiệm. Viết phép đối soát chạy hằng giờ. Xoá sạch hệ dẫn xuất và dựng lại từ nguồn sự thật, đo thời gian.",
"Ghi đôi trực tiếp từ ứng dụng cho dữ liệu quan trọng · không chỉ định nguồn sự thật · thêm hệ thứ ba trước khi giải xong bài toán đồng bộ giữa hai hệ đầu.",
"Đường đồng bộ chạy và phép đối soát phát hiện được lệch bơm vào, và hệ dẫn xuất dựng lại được từ nguồn sự thật."),

(186,"Designing the schema for an e-commerce platform","TH","Lesson 185",
"Không có cơ chế mới. Bài thiết kế: nhận mô tả một nền tảng thương mại điện tử có sáu nhóm yêu cầu khác nhau về hình dạng tải, và thiết kế sơ đồ dữ liệu cho nó. Sáu nhóm chọn có chủ đích để không một hệ nào phủ hết: đặt hàng và thanh toán cần giao dịch, danh mục sản phẩm hình dạng thay đổi, tìm kiếm sản phẩm bằng tiếng Việt, phiên người dùng độ trễ thấp, sự kiện hành vi khối lượng lớn, và báo cáo doanh thu quét lớn. Đầu ra gồm bốn phần: sơ đồ các hệ và dữ liệu nào ở đâu, đường đồng bộ giữa chúng theo lesson 185, phát biểu nguồn sự thật, và phép tính chi phí vận hành ước lượng. Ràng buộc bắt buộc: mỗi hệ đưa vào phải dẫn được ít nhất hai ô trong bảng lesson 183 làm lý do, và phải nêu phương án một hệ duy nhất cùng lý do loại nó.",
"Thiết kế sơ đồ dữ liệu đa hệ cho sáu nhóm yêu cầu, mỗi hệ dẫn được hai ô số đo làm lý do, kèm phương án một hệ bị loại.",
"Tầng *sáng tạo*. Objective là thiết kế dưới ràng buộc nhiều chiều. Chấm theo năm mục: ánh xạ tải sang hệ 25đ, đường đồng bộ và nguồn sự thật 25đ, dẫn chứng số đo 20đ, phép tính chi phí vận hành 15đ, và phương án bị loại 15đ. Đạt khi ≥ 70/100 và mục dẫn chứng ≥ 50%.",
"Nhận mô tả nền tảng kèm số liệu: 50.000 đơn mỗi ngày, 2 triệu sản phẩm, 100 triệu sự kiện mỗi ngày, đội 4 người. Thiết kế sơ đồ đủ bốn phần. Viết phương án một hệ duy nhất và lý do loại. Đổi bài chéo và rà soát dẫn chứng từng hệ.",
"Đưa cả bảy hệ vào sơ đồ vì đã học cả bảy · bỏ phần chi phí vận hành vì khó ước lượng · không xét phương án một hệ duy nhất.",
"Đạt ≥ 70/100 và mục dẫn chứng ≥ 50%, với mỗi hệ dẫn được hai ô số đo."),

(187,"Preparing the defence - assumptions and what would change them","TH","Lesson 186",
"Bảo vệ một thiết kế không phải chứng minh nó đúng mà là nêu rõ nó đúng trong điều kiện nào. Ba loại phát biểu phải tách bạch: số đo, giả định, và suy luận. Số đo là thứ đã chạy; giả định là thứ nhận từ đề bài hoặc tự đặt; suy luận là thứ rút ra từ hai cái kia. Lẫn lộn ba loại là lỗi bảo vệ phổ biến nhất. Với mỗi giả định, phát biểu tín hiệu khiến phải xem lại: khối lượng vượt ngưỡng nào, độ trễ yêu cầu xuống mức nào, đội mất người nào. Đây là nội dung của một bản ghi quyết định kiến trúc ở lesson 90, và phần phương án bị loại là phần có giá trị nhất. Chuẩn bị cho ba câu hỏi chắc chắn bị hỏi: vì sao không dùng một hệ cho tất cả, vì sao không dùng hệ đang thịnh hành, và nếu khối lượng gấp mười thì sao. Tập trả lời bằng số chứ bằng lập luận chung. Nhượng bộ đúng phần chưa đủ bằng chứng là dấu hiệu bảo vệ tốt, không phải dấu hiệu yếu.",
"Viết bản ghi quyết định kiến trúc cho sơ đồ của mình, tách bạch ba loại phát biểu và nêu tín hiệu xem lại cho từng giả định.",
"Tầng *đánh giá*. Objective đòi phân loại độ chắc chắn của chính lập luận mình. Kiểm bằng rà soát chéo: một học viên khác đọc và phải phân loại lại được ba loại phát biểu. Đạt khi ít nhất 80% phát biểu được phân loại khớp giữa hai người, và khi mọi giả định đều có tín hiệu xem lại phát biểu bằng số.",
"Viết bản ghi quyết định cho sơ đồ ở lesson 186. Gắn nhãn từng phát biểu là số đo, giả định, hay suy luận. Với mỗi giả định, viết tín hiệu xem lại bằng số. Đổi bài chéo để người khác phân loại lại. Tập trả lời ba câu hỏi chắc chắn bị hỏi, mỗi câu dưới hai phút.",
"Trình bày giả định như số đo · viết tín hiệu xem lại bằng tính từ · chuẩn bị bảo vệ mọi thứ thay vì chuẩn bị nhượng bộ phần chưa đủ bằng chứng.",
"Ít nhất 80% phát biểu được phân loại khớp giữa hai người, và mọi giả định có tín hiệu xem lại bằng số."),

(188,"Gate 4 - defend a polyglot schema under changing constraints","KT","Lesson 187",
"Không có nội dung mới. Cổng 4 của chương trình, đóng chặng 3.",
"Bảo vệ một sơ đồ dữ liệu đa hệ trước hội đồng, và điều chỉnh hoặc giữ vững kết luận có lý do khi hội đồng thay một ràng buộc giữa buổi.",
"Tầng *đánh giá*. Cổng đo năng lực thiết kế và bảo vệ dưới chất vấn, không đo trí nhớ về bảy hệ. Thang điểm: A 20đ sơ đồ và ánh xạ tải sang hệ · B 20đ dẫn chứng số đo từ lab của chính mình · C 15đ đường đồng bộ và nguồn sự thật · D 15đ giả định và tín hiệu xem lại · E 30đ phản ứng khi ràng buộc bị đổi. Đạt khi ≥ 70/100 và phần E ≥ 50%. Phần E nặng nhất vì thiết kế đúng trong một điều kiện là dễ, còn biết điều kiện nào lật ngược nó mới là năng lực kiến trúc.",
"Trình bày 20 phút, chất vấn 25 phút. Hội đồng gồm một kỹ sư dữ liệu đi làm, một người đóng vai chủ sản phẩm, và một người đóng vai vận hành. Giữa buổi hội đồng đổi một ràng buộc: khối lượng gấp mười, hoặc yêu cầu điểm phục hồi xuống 5 phút, hoặc đội mất người duy nhất biết một hệ.",
"Bảo vệ hệ mình thích thay vì hệ hợp ràng buộc · giữ nguyên kết luận khi ràng buộc mới đã lật ngược lập luận · đổi kết luận khi bị chất vấn mà không có bằng chứng mới.",
"Đạt ≥ 70/100 và phần E ≥ 50%."),
]
