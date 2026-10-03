# -*- coding: utf-8 -*-
"""DE M25 Choosing an orchestrator + M26 Data contracts and handover."""

M25 = ("Choosing an Orchestrator", 261, 266, """| | |
|---|---|
| **Objective cấp module** | Chấm ba công cụ điều phối trên chín chiều, mỗi ô dẫn một quan sát từ lab của chính mình, và bảo vệ một lựa chọn cho đội có ràng buộc cho trước |
| **Tiền đề** | M22 · M23 · M24 |
| **Exit criterion** | Ma trận chín chiều đạt rà soát chéo, mọi ô truy được về lab, và giữ vững hoặc đổi kết luận có lý do khi ràng buộc bị đổi giữa buổi |
| **Kỹ năng SFIA** | `ARCH` mức 4 |
| **Chế độ hỏng** | Chấm theo cảm nhận hoặc chép bảng so sánh của nhà cung cấp, cho ra kết luận không đứng vững khi ràng buộc đổi |""",
"""Module chỉ chạy được vì ba module trước đã dựng cùng một pipeline tham chiếu và đo cùng bốn chỉ số ở lesson 226, 245 và 257. Không cùng bài toán thì đây là bài liệt kê tính năng, không phải bài so sánh, cùng ràng buộc với M18 và M31.

Bốn bài đầu dựng tiêu chí và đo, bài thứ năm xét một công cụ ở mức `C`, bài cuối là buổi bảo vệ.""")

L25 = [
(261,"Nine dimensions, and how to score each from lab evidence","LT","Module 25: M22 · M23 · M24",
"Chín chiều đánh giá và cách chuyển từng chiều thành một phép đo thực hiện được. Khả năng mô hình hoá phụ thuộc: đồ thị công cụ có diễn tả được lineage dữ liệu không, hay phải giữ cho khớp bằng tay. Chạy bù và chạy lại chọn lọc: chạy lại một ngày tốn bao nhiêu thao tác và chạy lại bao nhiêu bước, số đo đã có ở lesson 233 và 245. Kích hoạt theo sự kiện: có sẵn hay phải tự dựng, và có chiếm tài nguyên chờ không, nối lại lesson 230 và 241. Khả năng quan sát: thời gian từ lúc hỏng tới lúc biết bước nào hỏng. Công sức vận hành: số thành phần phải chạy, đường nâng cấp, ai trực. Bảo mật: thông tin xác thực đặt ở đâu và ai đọc được. Quản lý phiên bản: định nghĩa nộp vào kho mã được bao nhiêu phần. Chi phí: hạ tầng cộng thời gian người. Kỹ năng đội: mất bao lâu để người thứ hai sửa được một pipeline. Nguyên tắc chấm: mỗi ô dẫn một quan sát có số hoặc có ảnh chụp từ lab của chính mình; ba nguồn không được dùng là bảng so sánh của nhà cung cấp, bài xếp hạng, và cảm nhận về cú pháp.",
"Phát biểu cho từng chiều trong chín chiều một phép đo thực hiện được trên lab đã làm, kèm đơn vị đo.",
"Tầng *hiểu*. Bài dựng tiêu chí, chưa đo, nên objective dừng ở chỗ chuyển một chiều mơ hồ thành một phép đo lặp lại được. Kiểm bằng rà soát: mỗi phép đo phải nêu làm gì, đo cái gì, đơn vị là gì, và người khác lặp lại được. Chiều nào chỉ có tính từ mà không có phép đo thì không tính.",
"Với mỗi chiều, viết một phép đo gồm thao tác, đại lượng và đơn vị. Đối chiếu với số đo đã có ở lesson 226, 245 và 257 xem chiều nào đã có sẵn dữ liệu. Đổi bài với một học viên khác và thử thực hiện phép đo của người kia trên lab của mình; phép đo nào không lặp lại được thì viết lại.",
"Chấm bằng tính từ như mạnh, linh hoạt, dễ dùng · lấy số liệu từ tài liệu nhà cung cấp · đặt phép đo mà chỉ người viết mới thực hiện được.",
"Chín phép đo đều nêu đủ thao tác, đại lượng và đơn vị, và người khác lặp lại được trên lab của họ."),

(262,"Modelling power - task graph against asset graph on one pipeline","TH","Lesson 261",
"Trục cho khác biệt lớn nhất giữa ba công cụ, và lý do nằm ở mô hình chứ ở chất lượng cài đặt. Đồ thị tác vụ mô hình hoá việc phải làm, nên quan hệ giữa các bảng là thứ người viết phải khai báo riêng và giữ cho khớp. Đồ thị tài sản mô hình hoá thứ được tạo ra, nên quan hệ giữa các bảng chính là đồ thị. Prefect nằm ở giữa: mã Python thuần nên đồ thị suy ra từ lời gọi hàm, linh hoạt nhất nhưng không có khái niệm tài sản sẵn. Bốn câu hỏi vận hành dùng để đo trục này, và ba câu đầu đã đặt ở lesson 237: bảng nào cũ, đổi cột này hỏng cái gì, dựng lại một bảng giữa đồ thị phải dựng thêm gì, và lát nào còn thiếu. Với mỗi câu, đo số thao tác và thời gian để trả lời trên từng công cụ. Cảnh báo khi đọc số: một phần chênh lệch đến từ quyết định chia bước ở lesson 220 chứ từ công cụ, nên phải tách hai yếu tố trước khi kết luận.",
"Đo bốn câu hỏi vận hành trên ba công cụ cho cùng pipeline, và tách phần chênh lệch do mô hình khỏi phần do quyết định chia bước.",
"Tầng *phân tích*. Objective đòi phân rã khác biệt về đúng nguyên nhân, việc khó hơn thu thập số. Đạt khi bốn câu hỏi đều có số đo trên cả ba công cụ, và khi ít nhất một chênh lệch được tách rõ thành phần do mô hình và phần do cách chia bước, có lập luận kèm số.",
"Với bốn câu hỏi vận hành, đo số thao tác và thời gian trả lời trên ba công cụ. Lập bảng bốn nhân ba. Chạy lại phép đo với cách chia bước khác trên cùng công cụ, để tách hai yếu tố. Viết một đoạn nêu chênh lệch nào đến từ mô hình.",
"Gán mọi chênh lệch cho công cụ · đo trên ba pipeline khác nhau · so bằng số tính năng thay vì bằng thời gian trả lời câu hỏi vận hành.",
"Bốn câu hỏi có số đo trên cả ba công cụ, và ít nhất một chênh lệch được tách thành hai phần có lập luận."),

(263,"Backfill, replay and recovery compared under the same induced failure","TH","Lesson 262",
"Trục thứ hai và là trục quan trọng nhất về vận hành, vì chạy bù và phục hồi là việc làm thường xuyên còn dựng pipeline là việc làm một lần. Ba kịch bản chuẩn áp lên cả ba công cụ với cùng dữ liệu và cùng lỗi: thiếu một ngày ở giữa dải, thiếu 30 ngày rải rác, và sửa logic một bước ở giữa đồ thị rồi phải dựng lại hạ nguồn. Với mỗi kịch bản, ba số đo: số thao tác người vận hành phải làm, số bước hệ thống phải chạy, và thời gian tới khi dữ liệu đúng trở lại. Số đo thứ nhất đo giao diện, thứ hai đo mô hình, thứ ba đo cả hai cộng hạ tầng. Kịch bản thứ tư khó hơn và phân hoá ba công cụ rõ nhất: giết tiến trình giữa chừng một lần chạy bù dài rồi tiếp tục, đo lượng việc bị làm lại. Ràng buộc bắt buộc: kết quả cuối của cả ba công cụ phải khớp cùng một bản đối chứng, nếu không thì số đo tốc độ vô nghĩa.",
"Đo ba kịch bản chạy bù trên ba công cụ với cùng dữ liệu, và chứng minh kết quả cuối của cả ba khớp cùng một bản đối chứng.",
"Tầng *phân tích*. Objective có ràng buộc đúng đắn làm điều kiện trước khi số tốc độ có nghĩa. Đạt khi kết quả cuối của cả ba công cụ khớp bản đối chứng từng dòng, và khi bảng ba kịch bản nhân ba công cụ có đủ ba số đo mỗi ô. Nhanh mà lệch một dòng thì ô đó không tính.",
"Sinh bản đối chứng 90 ngày. Với mỗi công cụ, chạy ba kịch bản và ghi ba số đo. Đối chiếu kết quả cuối từng dòng với bản đối chứng. Thêm kịch bản thứ tư: giết tiến trình giữa chừng chạy bù, đo lượng việc bị làm lại trên từng công cụ.",
"So tốc độ trước khi đối chiếu kết quả · dùng dải ngày khác nhau cho ba công cụ · đo số thao tác người vận hành mà bỏ số bước hệ thống chạy.",
"Kết quả cuối cả ba công cụ khớp bản đối chứng từng dòng, và bảng ba nhân ba có đủ ba số đo mỗi ô."),

(264,"Operational cost - infrastructure, upgrade path and on-call load","TH","Lesson 263",
"Trục ít được đo nhất nhưng quyết định nhiều nhất sau một năm. Bốn thành phần chi phí vận hành: hạ tầng phải chạy, thời gian nâng cấp, tải trực khi hỏng, và thời gian đưa người mới vào. Hạ tầng đo bằng số tiến trình phải chạy và tài nguyên chúng chiếm ở trạng thái rỗi, số đã có từ lesson 236, 248 và 260. Nâng cấp đo bằng số bước và có phải di trú lược đồ không, dữ liệu từ ba bài vận hành đó. Tải trực đo bằng số loại sự cố đặc trưng của công cụ và thời gian chẩn đoán trung bình, lấy từ chính ba bài vận hành. Thời gian đưa người mới vào đo bằng thực nghiệm: đưa pipeline cho một học viên chưa học công cụ đó và đo thời gian tới khi họ sửa được một lỗi. Chi phí giấy phép nếu có. Nguyên tắc: chi phí vận hành phần lớn là thời gian người chứ tiền hạ tầng, nên đo bằng giờ rồi mới quy ra tiền.",
"Đo bốn thành phần chi phí vận hành cho ba công cụ, và quy chúng về cùng một đơn vị để so được.",
"Tầng *đánh giá*. Objective đòi quy nhiều loại chi phí khác đơn vị về một thước đo chung, và nêu giả định của phép quy đó. Đạt khi bốn thành phần đều có số cho cả ba công cụ, và khi phép quy về đơn vị chung nêu rõ giả định về đơn giá giờ người và chu kỳ nâng cấp.",
"Đo tài nguyên rỗi của ba cụm. Đếm số bước nâng cấp từ ghi chép lesson 236, 248, 260. Liệt kê loại sự cố đặc trưng và thời gian chẩn đoán của từng cái. Đưa pipeline cho một học viên chưa học công cụ đó, giao một lỗi, đo thời gian họ sửa được. Quy tất cả về giờ người mỗi tháng và nêu giả định.",
"Đo chi phí hạ tầng mà bỏ thời gian người · so chi phí mà không nêu giả định về đơn giá · bỏ phép thử thời gian đưa người mới vào vì tốn công.",
"Bốn thành phần có số cho cả ba công cụ, và phép quy về đơn vị chung nêu rõ giả định."),

(265,"Kestra `C` - YAML-declared flows, and when a team wants no Python","LT","Lesson 261",
"Kestra ở mức `C`: biết dùng đúng tình huống, không dựng lab. Luồng khai báo bằng YAML thay vì bằng Python, và hệ quả kéo theo. Điều kiện khiến một đội chọn hướng đó: người viết luồng không phải lập trình viên, tổ chức muốn định nghĩa rà soát được bởi người không đọc Python, hoặc muốn tránh phụ thuộc Python lan vào tầng điều phối. Giá phải trả: logic điều kiện phức tạp diễn đạt trong YAML dài dòng hơn và khó kiểm thử hơn, và tới một ngưỡng thì người ta viết Python bên trong YAML, lúc đó mất cả hai lợi thế. Nguyên tắc tổng quát áp được cho mọi công cụ khai báo: ngôn ngữ khai báo mạnh ở phần cấu trúc lặp lại, yếu ở phần logic rẽ nhánh nhiều. Cách đánh giá một công cụ ở mức `C` một cách trung thực: đọc tài liệu chính thức, xác định mô hình của nó, nêu điều kiện phù hợp, và nói rõ mình chưa chạy nên chưa biết gì về vận hành thật. Không kết luận về hiệu năng hay độ ổn định khi chưa có lab.",
"Phát biểu điều kiện khiến một đội nên cân nhắc Kestra, và nói rõ kết luận nào không đưa ra được vì chưa có lab.",
"Tầng *hiểu*. Công cụ ở mức `C` nên objective không thể là dựng hay đo. Kiểm bằng một đoạn viết: phải nêu mô hình của công cụ, điều kiện phù hợp hai chiều, và ít nhất hai kết luận cố ý không đưa ra kèm lý do thiếu bằng chứng. Đoạn viết khẳng định về hiệu năng hay độ ổn định thì không đạt, vì đó đúng là lỗi bài này dạy cách tránh.",
"Đọc tài liệu chính thức của Kestra. Viết nửa trang: mô hình của công cụ, ba điều kiện khiến đội nên cân nhắc, hai điều kiện khiến không nên, và ít nhất hai kết luận mình cố ý không đưa ra vì chưa chạy lab. Đối chiếu mô hình của nó với ba công cụ đã học.",
"Kết luận về hiệu năng từ tài liệu tiếp thị · xếp Kestra vào ma trận lesson 261 như thể đã có lab · bỏ qua ngưỡng mà YAML bắt đầu chứa Python.",
"Đoạn viết nêu đủ mô hình, điều kiện hai chiều, và ít nhất hai kết luận cố ý không đưa ra kèm lý do."),

(266,"The decision - defend one choice for a team with given constraints","KT","Lesson 265",
"Không có nội dung mới. Buổi bảo vệ quyết định chọn công cụ điều phối.",
"Chọn một công cụ điều phối cho một đội có ràng buộc cho trước, bảo vệ lựa chọn bằng ma trận bằng chứng, và điều chỉnh kết luận khi hội đồng đổi một ràng buộc giữa buổi.",
"Tầng *đánh giá*. Bài kiểm của module, đo năng lực chọn giữa các phương án và bảo vệ dưới chất vấn. Không kiểm bằng đề có đáp án đúng vì chọn công cụ nào cũng đạt nếu lập luận đứng vững. Thang điểm: A 25đ ma trận chín chiều có bằng chứng từ lab · B 20đ lập luận từ ràng buộc đội tới lựa chọn · C 20đ nêu được cái mình đánh đổi · D 15đ điều kiện khiến nên xem lại quyết định · E 20đ giữ vững hoặc đổi kết luận có lý do khi ràng buộc bị đổi. Đạt khi ≥ 70/100 và phần E ≥ 60%.",
"Nhận mô tả một đội: số người, kỹ năng Python, ngân sách hạ tầng, yêu cầu độ trễ, số pipeline, ai trực khi hỏng. Trình bày 20 phút, chất vấn 20 phút. Giữa buổi hội đồng đổi một ràng buộc, ví dụ số pipeline tăng gấp mười, người duy nhất biết Python nghỉ việc, hoặc yêu cầu tuân thủ cấm siêu dữ liệu ra ngoài.",
"Bảo vệ công cụ mình thích thay vì công cụ hợp ràng buộc · không nêu được mình đánh đổi cái gì · đổi kết luận khi bị chất vấn mà không có bằng chứng mới, hoặc giữ nguyên khi ràng buộc mới đã lật ngược lập luận.",
"Đạt ≥ 70/100 và phần E ≥ 60%."),
]

M26 = ("Data Contracts and Dataset Handover", 267, 276, """| | |
|---|---|
| **Objective cấp module** | Bàn giao một tập dữ liệu có hợp đồng thực thi được, thương lượng được với đội nguồn, và đổi được hợp đồng mà không làm vỡ hạ nguồn |
| **Tiền đề** | M25 · M20 |
| **Exit criterion** | Đạt Cổng 6 ≥ 70/100: đổi lược đồ có kiểm soát, chạy bù 30 ngày, và bàn giao ba tập dữ liệu để người khác dựng mô hình mà không hỏi lại |
| **Kỹ năng SFIA** | `DTAN` mức 4 · `RLMT` mức 3 |
| **Chế độ hỏng** | Viết hợp đồng rồi để đó, không có phép kiểm tự động và không có ai ở đội nguồn biết nó tồn tại |""",
"""Module đóng chặng 5 và nó là chỗ vai trò Data Engineer gặp phần tổ chức. Hợp đồng mười một khai báo đã dựng ở lesson 216; module này làm bốn việc mà bài đó chưa làm: đánh phiên bản, thực thi, thương lượng, và bàn giao có diễn tập.

Phần lớn khó khăn ở đây không phải kỹ thuật. Đội nguồn không có động lực giữ hợp đồng nếu họ không thấy lợi, nên thuyết phục bằng hậu quả cụ thể là kỹ năng chính của module.""")

L26 = [
(267,"From pipeline contract to data product","LT","Module 26: M25 · M20",
"Hợp đồng ở lesson 216 mô tả một pipeline; sản phẩm dữ liệu mô tả một thứ có người dùng, có chủ sở hữu, có vòng đời và có cam kết. Bốn thứ một sản phẩm dữ liệu có mà một bảng không có: giao diện ổn định được đánh phiên bản, cam kết mức dịch vụ công bố, người chịu trách nhiệm có tên, và quy trình đổi. Phân biệt tập dữ liệu nội bộ với tập dữ liệu công khai trong tổ chức: cái đầu đổi tự do, cái sau đổi theo quy trình; đánh dấu rõ cái nào là cái nào là việc rẻ và tránh được nhiều tranh chấp. Ba vai trò quanh một sản phẩm dữ liệu và trách nhiệm của từng vai: đội nguồn sinh dữ liệu, Data Engineer biến đổi và bàn giao, đội tiêu thụ dùng nó. Ranh giới trách nhiệm khi số sai: ai điều tra trước, và quy tắc điều tra ngược từ đích về nguồn. Vì sao đầu tư vào hợp đồng rẻ hơn trả lời câu hỏi lặp lại, tính bằng giờ người mỗi tháng.",
"Phân loại các tập dữ liệu hiện có thành nội bộ và công khai, và phát biểu bốn thuộc tính sản phẩm cho những cái công khai.",
"Tầng *hiểu*. Bài dựng khung cho chín bài sau. Đạt khi phân loại có tiêu chí viết ra được chứ theo cảm tính, và khi bốn thuộc tính của ít nhất hai tập dữ liệu công khai đều cụ thể: phiên bản có số, cam kết có giờ, chủ sở hữu có tên, quy trình đổi có bước.",
"Lấy các bảng đầu ra của nền tảng ở lesson 217. Phân loại nội bộ hay công khai kèm tiêu chí. Với hai bảng công khai, viết bốn thuộc tính sản phẩm. Ước lượng số giờ mỗi tháng đội đang mất vì trả lời câu hỏi lặp lại về các bảng đó.",
"Coi mọi bảng là công khai nên không đổi được gì · ghi chủ sở hữu là tên nhóm · phát biểu cam kết bằng tính từ.",
"Phân loại có tiêu chí viết ra, và bốn thuộc tính của hai tập dữ liệu công khai đều cụ thể."),

(268,"Versioning a contract and the deprecation window","TH","Lesson 267",
"Đánh phiên bản hợp đồng để hạ nguồn biết cái gì đổi và khi nào. Phân loại thay đổi theo mức ảnh hưởng, nối lại lesson 209: thêm cột tuỳ chọn tương thích ngược nên tăng phiên bản phụ; xoá cột, đổi kiểu, đổi tên phá vỡ nên tăng phiên bản chính; đổi ngữ nghĩa mà không đổi cấu trúc cũng phá vỡ và đây là loại nguy hiểm nhất vì không có tín hiệu kỹ thuật, nối lại lesson 89. Mẫu mở rộng rồi thu hẹp cho thay đổi phá vỡ, cùng bốn bước với lesson 121 và 181: thêm cái mới, ghi cả hai, chuyển người đọc, rồi bỏ cái cũ. Cửa sổ ngừng dùng là khoảng thời gian giữa bước ba và bước bốn, và nó phải công bố trước chứ không quyết định lúc sắp xoá. Cách biết ai còn dùng cột sắp bỏ: nhật ký truy vấn của kho dữ liệu, nối lại lesson 165. Chạy song song hai phiên bản và chi phí của nó. Bỏ phiên bản cũ và thủ tục xác nhận không còn ai dùng.",
"Thực hiện một thay đổi phá vỡ theo mẫu bốn bước với cửa sổ ngừng dùng công bố trước, và xác nhận không còn ai dùng phiên bản cũ trước khi bỏ.",
"Tầng *áp dụng*. Objective có quy trình nhiều bước với tiêu chí kiểm được ở từng bước. Đạt khi bốn bước đều triển khai riêng và quay lui được độc lập, và khi chứng minh được không còn truy vấn nào chạm cột cũ trong 14 ngày trước khi bỏ, bằng nhật ký truy vấn chứ bằng hỏi miệng.",
"Đổi kiểu một cột trong tập dữ liệu công khai theo bốn bước. Công bố cửa sổ ngừng dùng. Dùng nhật ký truy vấn tìm ai còn dùng cột cũ và liên hệ. Chờ tới khi không còn truy vấn nào trong 14 ngày rồi mới bỏ. Thử quay lui ở từng bước.",
"Quyết định cửa sổ ngừng dùng lúc sắp xoá · hỏi miệng xem còn ai dùng không thay vì xem nhật ký truy vấn · gộp bước chuyển người đọc với bước bỏ cột cũ vào một lần triển khai.",
"Bốn bước triển khai riêng và quay lui được, và nhật ký truy vấn xác nhận không ai dùng cột cũ trong 14 ngày."),

(269,"Enforcing a contract at the boundary","TH","Lesson 268",
"Hợp đồng không có phép kiểm tự động chỉ là lời hứa, nối lại lesson 216. Hai biên cần thực thi và cái mỗi biên bảo vệ: biên nhận kiểm nguồn có giữ đúng cam kết với mình không, biên phát kiểm mình có giữ đúng cam kết với hạ nguồn không. Nhiều đội chỉ làm biên thứ hai và bỏ biên thứ nhất, nên khi nguồn đổi thì phát hiện ở tận cuối. Ba nơi chạy phép kiểm và cái mỗi nơi bắt, nối lại lesson 213: trong tích hợp liên tục trên dữ liệu mẫu cố định, trong pipeline trên dữ liệu thật, và theo lịch riêng để phát hiện trôi khi pipeline không chạy. Hành vi khi vi phạm: chặn hay cảnh báo, và quy tắc chọn theo loại vi phạm chứ theo thói quen. Sinh phép kiểm tự động từ chính tài liệu hợp đồng thay vì viết tay hai nơi, tránh hai bản lệch nhau. Đo tỉ lệ vi phạm theo thời gian như chỉ số sức khoẻ quan hệ với đội nguồn. Báo cáo tuân thủ hợp đồng gửi định kỳ cho cả hai phía.",
"Cài thực thi hợp đồng ở cả hai biên và chứng minh vi phạm ở biên nhận được phát hiện trước khi nó lan xuống hạ nguồn.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm bằng thực nghiệm so sánh. Đạt khi bơm một vi phạm vào nguồn thì biên nhận bắt được trong lần chạy đầu tiên, còn khi tắt biên nhận thì vi phạm đó đi tới tận bảng đích rồi mới lộ, đo bằng số bước dữ liệu sai đi qua.",
"Cài phép kiểm ở cả hai biên, sinh tự động từ tài liệu hợp đồng. Bơm ba vi phạm vào nguồn: thêm cột bắt buộc, đổi kiểu, và tỉ lệ giá trị rỗng tăng vọt. Đo số bước dữ liệu sai đi qua khi có và không có biên nhận. Chạy phép kiểm theo lịch riêng khi pipeline không chạy.",
"Chỉ thực thi ở biên phát · viết phép kiểm tay tách rời tài liệu hợp đồng nên hai bản lệch · đặt mọi vi phạm là chặn.",
"Vi phạm bị bắt ở biên nhận trong lần chạy đầu, và số bước dữ liệu sai đi qua giảm rõ khi bật biên nhận."),

(270,"Negotiating with the source team","TH","Lesson 269",
"Phần khó nhất của hợp đồng dữ liệu là tổ chức chứ kỹ thuật: đội nguồn không có động lực giữ hợp đồng nếu họ không thấy lợi, và họ thường không biết ai đang phụ thuộc vào bảng của họ. Ba thứ phải chuẩn bị trước khi nói chuyện: hậu quả cụ thể đã xảy ra với số liệu, danh sách người dùng cuối bị ảnh hưởng, và đề xuất cụ thể mình muốn họ làm gì. Trình bày bằng hậu quả nghiệp vụ chứ bằng thuật ngữ kỹ thuật: báo cáo doanh thu sai ba ngày thì nói thế, không nói lược đồ thay đổi gây lỗi ép kiểu. Bốn thứ có thể đổi lại để họ dễ nhận: mình nhận thông báo trước thay vì đòi họ không đổi, mình tự viết phép kiểm thay vì đòi họ viết, mình nhận cửa sổ chuyển đổi dài hơn, và mình giúp họ thấy ai đang dùng dữ liệu của họ. Ghi lại thoả thuận thành văn bản có người ký. Leo thang khi không thoả thuận được, và khi nào chấp nhận rằng mình phải tự chịu.",
"Chuẩn bị và trình bày một đề xuất hợp đồng với đội nguồn, dùng hậu quả nghiệp vụ chứ thuật ngữ kỹ thuật, và đạt được một thoả thuận ghi thành văn bản.",
"Tầng *đánh giá*. Objective đo bằng kết quả cuộc trao đổi chứ bằng nội dung chuẩn bị. Kiểm bằng đóng vai: một học viên khác đóng vai trưởng nhóm đội nguồn có ưu tiên riêng và động lực từ chối. Đạt khi đạt được thoả thuận có ít nhất hai điều khoản cụ thể, và khi người đóng vai xác nhận lập luận dựa trên hậu quả nghiệp vụ chứ thuật ngữ.",
"Chuẩn bị ba thứ cho một bảng nguồn thật: hậu quả đã xảy ra có số, danh sách người dùng bị ảnh hưởng lấy từ nhật ký truy vấn, và đề xuất cụ thể. Đóng vai 20 phút với một học viên khác. Ghi thoả thuận thành văn bản. Đổi vai và làm lại.",
"Trình bày bằng thuật ngữ kỹ thuật · đòi đội nguồn không bao giờ đổi lược đồ · không chuẩn bị thứ gì đổi lại để họ dễ nhận.",
"Đạt thoả thuận có ít nhất hai điều khoản cụ thể, và người đóng vai xác nhận lập luận dựa trên hậu quả nghiệp vụ."),

(271,"Serving the consumer - documentation, fixtures and sample queries","TH","Lesson 270",
"Bàn giao tốt đo bằng số câu hỏi người nhận phải đặt, nối lại lesson 200. Năm thứ người tiêu thụ cần và thứ tự ưu tiên: tài liệu cột viết cho người không có ngữ cảnh, dữ liệu mẫu cố định để họ viết kiểm thử, truy vấn mẫu cho ba câu hỏi thường gặp nhất, sơ đồ lineage tới nguồn, và cách liên hệ khi có vấn đề. Dữ liệu mẫu cố định là thứ hay bị bỏ nhất và giá trị cao nhất: nó cho người nhận viết kiểm thử mà không cần chạm dữ liệu thật, nối lại lesson 84 và 87. Tài liệu cột viết thế nào để dùng được: nêu ngữ nghĩa nghiệp vụ, dải giá trị hợp lệ, và cách xử lý giá trị rỗng, chứ không chép lại tên cột. Truy vấn mẫu tiết kiệm nhiều nhất vì nó trả lời trước ba câu hỏi chắc chắn được hỏi. Đặt tài liệu ở nơi người nhận tìm thấy chứ nơi mình tiện để. Đo mức dùng tài liệu và số câu hỏi lặp lại như chỉ số chất lượng bàn giao.",
"Chuẩn bị gói bàn giao đủ năm thứ, và chứng minh bằng quan sát rằng người nhận dựng được thứ họ cần với không quá một câu hỏi.",
"Tầng *đánh giá*. Objective đo bằng người nhận thật. Kiểm bằng quan sát: hai học viên khác nhận gói bàn giao và mỗi người dựng một thứ khác nhau trên tập dữ liệu, ghi lại mọi câu phải hỏi. Đạt khi tổng số câu hỏi của cả hai không quá hai, và khi cả hai viết được kiểm thử bằng dữ liệu mẫu cố định.",
"Chuẩn bị gói bàn giao đủ năm thứ cho một tập dữ liệu. Đưa cho hai học viên khác với hai yêu cầu khác nhau. Quan sát và ghi mọi câu hỏi cùng điểm vướng. Sửa gói theo điểm vướng. Đưa cho người thứ ba và đo lại.",
"Chép tên cột vào ô mô tả · bàn giao mà không kèm dữ liệu mẫu cố định · đặt tài liệu ở kho riêng của đội mình.",
"Tổng câu hỏi của hai người nhận không quá hai, và cả hai viết được kiểm thử bằng dữ liệu mẫu cố định."),

(272,"Service level objectives for data and how to publish them","TH","Lesson 271",
"Cam kết mức dịch vụ cho dữ liệu khác cho dịch vụ trực tuyến ở chỗ nó nói về độ tươi và độ đúng chứ về thời gian phản hồi. Bốn chỉ số thường cam kết: dữ liệu sẵn sàng trước mấy giờ, độ đầy đủ tối thiểu, độ trễ tối đa của dữ liệu tới muộn, và tỉ lệ ngày đạt cam kết trong tháng. Chỉ số thứ tư là chỉ số nói thật nhất và hay bị bỏ: cam kết trước 6 giờ sáng mà đạt 70% số ngày thì cam kết đó vô nghĩa. Đo trước rồi mới cam kết: lấy phân bố 90 ngày lịch sử, cam kết ở phân vị mà mình thật sự đạt được, không cam kết ở mức mong muốn. Ngân sách vi phạm và cách dùng nó để quyết định khi nào dừng thêm tính năng mà đi sửa độ tin cậy. Công bố ở đâu để người dùng thấy: cạnh dữ liệu chứ trong tài liệu nội bộ. Báo cáo định kỳ mức đạt thật. Phân biệt cam kết với mục tiêu nội bộ: cam kết nới hơn mục tiêu để còn chỗ xoay xở.",
"Đặt cam kết mức dịch vụ từ phân bố 90 ngày lịch sử, công bố nó, và báo cáo mức đạt thật sau 30 ngày.",
"Tầng *đánh giá*. Objective đòi cam kết dựa trên số đo chứ trên mong muốn. Đạt khi bốn chỉ số đều đặt từ phân bố lịch sử có nêu phân vị chọn, và khi báo cáo 30 ngày cho thấy mức đạt thật nằm trong khoảng cam kết. Cam kết chặt hơn số liệu lịch sử là không đạt vì nó chắc chắn vi phạm.",
"Lấy phân bố 90 ngày của bốn chỉ số từ nền tảng lesson 217. Chọn phân vị và đặt cam kết cho từng chỉ số. Công bố cạnh dữ liệu. Chạy 30 ngày mô phỏng và báo cáo mức đạt thật. Tính ngân sách vi phạm còn lại. So cam kết với mục tiêu nội bộ.",
"Cam kết ở mức mong muốn thay vì mức đo được · bỏ chỉ số tỉ lệ ngày đạt · công bố cam kết trong tài liệu nội bộ mà người dùng không thấy.",
"Bốn chỉ số đặt từ phân bố lịch sử có nêu phân vị, và báo cáo 30 ngày cho mức đạt thật trong khoảng cam kết."),

(273,"Handling a contract breach - the seven-step incident process","TH","Lesson 272",
"Quy trình bảy bước khi hợp đồng bị vi phạm và dữ liệu sai đã lan ra. Bước một chặn lan rộng: dừng pipeline hoặc chặn phát hành, quyết định trong vài phút chứ không chờ hiểu hết nguyên nhân. Bước hai thông báo sớm cho người đang dùng, kể cả khi chưa biết nguyên nhân; thông báo sớm với thông tin chưa đầy đủ tốt hơn thông báo muộn với thông tin đầy đủ. Bước ba chẩn đoán. Bước bốn sửa. Bước năm chạy bù, nối lại lesson 210 và 233. Bước sáu thông báo kết quả cho đúng những người đã nhận thông báo ở bước hai, gồm cả việc nói rõ số nào đã đổi. Bước bảy phân tích nguyên nhân gốc và thêm phép kiểm để lần sau bắt sớm hơn. Bước hai và bước sáu là hai bước hay bị bỏ nhất và cũng là hai bước quyết định niềm tin, vì người dùng nhớ mình có được báo hay không hơn là nhớ sự cố kéo dài bao lâu. Ghi nhật ký sự cố và đo thời gian từng bước.",
"Xử lý một sự cố vi phạm hợp đồng theo đủ bảy bước, và đo thời gian từng bước.",
"Tầng *áp dụng*. Objective có quy trình với tiêu chí kiểm được ở từng bước. Đạt khi cả bảy bước đều có bằng chứng thời gian, khi thông báo bước hai gửi trong vòng 30 phút kể từ lúc phát hiện, và khi thông báo bước sáu gửi đúng tập người đã nhận bước hai. Sửa xong nhanh mà bỏ hai bước thông báo thì không đạt.",
"Giám khảo bơm một vi phạm hợp đồng vào nguồn. Xử lý theo bảy bước, ghi dấu thời gian từng bước. Soạn và gửi hai thông báo thật cho danh sách người dùng lấy từ nhật ký truy vấn. Chạy bù và đối chiếu. Viết phân tích nguyên nhân gốc kèm phép kiểm bổ sung.",
"Chờ hiểu hết nguyên nhân rồi mới thông báo · bỏ bước thông báo kết quả vì đã sửa xong · chạy bù mà không nói cho người dùng biết số lịch sử đã đổi.",
"Bảy bước có bằng chứng thời gian, thông báo bước hai trong 30 phút, và bước sáu gửi đúng tập người đã nhận."),

(274,"Conformed datasets - orders, payments, refunds","DA","Lesson 273",
"Không có cơ chế mới. Dự án gộp module: dựng ba tập dữ liệu đã chuẩn hoá cho ba miền nghiệp vụ liên quan nhau, mỗi tập có hợp đồng đầy đủ. Ba miền chọn có chủ đích vì chúng dùng chung chiều và phải so sánh chéo được, nối lại ma trận xe buýt ở lesson 197: một đơn hàng có thể có nhiều thanh toán và nhiều lần hoàn tiền, nên hạt của ba tập khác nhau và phép so phải qua hạt chung. Yêu cầu cho mỗi tập: hạt kiểm chứng được, khoá nghiệp vụ khai báo, hợp đồng mười một khai báo có phiên bản, phép kiểm ở hai biên, cam kết mức dịch vụ đặt từ số liệu, gói bàn giao năm thứ, và sổ tay xử lý. Tiêu chí đối soát xuyên tập: tổng tiền thanh toán trừ tổng tiền hoàn phải khớp một đại lượng tính độc lập từ đơn hàng, ở cả ba kỳ.",
"Dựng ba tập dữ liệu đã chuẩn hoá có hợp đồng đầy đủ, và chứng minh đối soát xuyên ba tập khớp ở cả ba kỳ.",
"Tầng *sáng tạo*. Objective là thiết kế một bộ sản phẩm dữ liệu dưới nhiều ràng buộc đồng thời. Chấm theo sáu mục: hạt và khoá của ba tập 20đ, đối soát xuyên tập 25đ, hợp đồng và phép kiểm hai biên 20đ, cam kết mức dịch vụ 10đ, gói bàn giao 15đ, sổ tay 10đ. Đạt khi ≥ 70/100 và mục đối soát ≥ 70% của nó.",
"Nguồn có đơn hàng, thanh toán, hoàn tiền với quan hệ một nhiều. Dựng ba tập đã chuẩn hoá. Phát biểu và kiểm chứng hạt từng tập. Viết ba hợp đồng có phiên bản. Cài phép kiểm hai biên. Đặt cam kết từ số liệu 90 ngày. Đối soát xuyên tập ở ba kỳ.",
"Đặt ba tập ở cùng một hạt cho tiện rồi mất chi tiết · đối soát từng tập riêng mà bỏ đối soát xuyên tập · viết một hợp đồng chung cho cả ba tập.",
"Đạt ≥ 70/100, mục đối soát ≥ 70%, và đối soát xuyên ba tập khớp ở cả ba kỳ."),

(275,"Handover rehearsal - someone else builds on your dataset","TH","Lesson 274",
"Không có cơ chế mới. Bài diễn tập và nó đo thứ khó giả: một tập dữ liệu người khác dùng được mà không cần mình. Quy trình diễn tập: giao gói bàn giao cho một người chưa tham gia dự án, giao họ một yêu cầu nghiệp vụ cụ thể, để họ làm trong thời gian giới hạn, và ghi lại mọi câu hỏi cùng mọi chỗ họ hiểu sai. Ba loại câu hỏi và cái mỗi loại chỉ ra: câu hỏi về ngữ nghĩa chỉ ra tài liệu cột thiếu, câu hỏi về cách dùng chỉ ra thiếu truy vấn mẫu, câu hỏi về độ tin cậy chỉ ra thiếu cam kết mức dịch vụ hoặc thiếu thông tin lineage. Hiểu sai nguy hiểm hơn câu hỏi: người hỏi thì mình biết mà sửa, người hiểu sai thì dựng ra số sai mà không ai biết, nên phần đối chiếu kết quả của họ với bản đối chứng là phần quan trọng nhất của diễn tập. Lặp diễn tập với người thứ hai sau khi sửa. Đưa diễn tập vào quy trình chuẩn trước mỗi lần công bố tập dữ liệu mới.",
"Chạy một buổi diễn tập bàn giao, phân loại mọi câu hỏi và hiểu sai, và sửa gói bàn giao rồi chứng minh cải thiện ở lần diễn tập thứ hai.",
"Tầng *đánh giá*. Objective đo bằng hai vòng quan sát nên thấy được cải thiện chứ chỉ thấy trạng thái. Đạt khi vòng hai có số câu hỏi giảm ít nhất một nửa so với vòng một, và khi kết quả người nhận dựng ra ở vòng hai khớp bản đối chứng. Vòng một nhiều câu hỏi không phải điểm trừ; không cải thiện ở vòng hai mới là.",
"Giao gói bàn giao của lesson 274 cho một người chưa tham gia, cùng một yêu cầu nghiệp vụ. Quan sát 60 phút, ghi mọi câu hỏi và mọi chỗ hiểu sai. Đối chiếu kết quả họ dựng với bản đối chứng. Phân loại câu hỏi theo ba loại. Sửa gói. Lặp với người thứ hai và so hai vòng.",
"Trả lời câu hỏi trong lúc diễn tập thay vì ghi lại rồi sửa tài liệu · bỏ phần đối chiếu kết quả vì họ không kêu gì · chỉ diễn tập một vòng.",
"Vòng hai giảm ít nhất một nửa số câu hỏi, và kết quả người nhận dựng ra khớp bản đối chứng."),

(276,"Gate 6 - controlled schema change, 30-day backfill, clean handover","KT","Lesson 275",
"Không có nội dung mới. Cổng 6 đóng chặng 5.",
"Thực hiện một thay đổi lược đồ phá vỡ có kiểm soát trên tập dữ liệu đang có người dùng, chạy bù 30 ngày, và bàn giao cho người khác dựng mô hình mà không cần hỏi lại.",
"Tầng *đánh giá*. Cổng đo ba năng lực cùng lúc: đổi có kiểm soát, phục hồi dữ liệu lịch sử, và bàn giao. Thang điểm: A 25đ thay đổi theo bốn bước với cửa sổ ngừng dùng công bố trước · B 20đ hạ nguồn không vỡ trong suốt quá trình, đo bằng số lỗi truy vấn · C 25đ chạy bù 30 ngày khớp bản đối chứng · D 20đ người nhận dựng được mô hình với không quá một câu hỏi · E 10đ thông báo gửi đúng tập người dùng ở cả hai thời điểm. Đạt khi ≥ 70/100, phần B và phần C đều ≥ 70% của chúng.",
"180 phút. Tập dữ liệu có ba người dùng mô phỏng chạy truy vấn liên tục. Đổi kiểu một cột theo bốn bước. Chạy bù 30 ngày. Bàn giao cho một học viên khác chưa biết gì về tập này, họ dựng một mô hình theo yêu cầu cho trước. Đếm lỗi truy vấn của ba người dùng suốt quá trình.",
"Gộp bước bỏ cột cũ vào cùng lần triển khai với bước chuyển người đọc · chạy bù mà không đối chiếu · bàn giao mà không kèm dữ liệu mẫu cố định.",
"Đạt ≥ 70/100, phần B và phần C đều ≥ 70%."),
]
