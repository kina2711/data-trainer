# -*- coding: utf-8 -*-
"""DE M39 System design and distributed systems + M40 Capstone."""

M39 = ("System Design and Distributed Systems", 401, 416, """| | |
|---|---|
| **Objective cấp module** | Thiết kế một nền tảng dữ liệu từ yêu cầu mơ hồ, bảo vệ được mọi lựa chọn bằng ước lượng và đánh đổi, và giữ hoặc đổi kết luận có lý do khi ràng buộc đổi |
| **Tiền đề** | M38 |
| **Exit criterion** | Qua buổi rà soát thiết kế: ước lượng cùng bậc với thực tế, mọi lựa chọn dẫn được về một ràng buộc, và nêu được ba điều kiện làm thiết kế sai |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `DTAN` mức 4 |
| **Chế độ hỏng** | Vẽ sơ đồ đầy công cụ mà không có ước lượng nào, nên không trả lời được vì sao chọn cái này thay vì cái kia khi bị hỏi |""",
"""Module không giới thiệu công cụ mới. Nó dạy cách ghép những thứ đã học thành một hệ có lý do, và cách bảo vệ lý do đó dưới chất vấn.

Tám bài đầu là nền lý thuyết hệ phân tán ở mức đủ để lập luận; tám bài sau là thiết kế và rà soát trên tình huống thật. Mọi ước lượng đều dùng lại số đo từ các lab đã làm, theo đúng luật đặt ở lesson 261.""")

L39 = [
(401,"What distributed means, and the eight fallacies revisited","LT","Module 39: M38",
"Hệ phân tán định nghĩa bằng hệ quả chứ bằng số máy: một hệ là phân tán khi một phần của nó có thể hỏng mà phần còn lại vẫn chạy, và khi đó xuất hiện những trạng thái không có ở hệ một máy. Tám ngộ nhận kinh điển đã gặp ở M4 nay được soi lại bằng kinh nghiệm thật: mạng không đáng tin, độ trễ khác không, băng thông có hạn, mạng không an toàn, hình trạng đổi, có nhiều người quản trị, chi phí vận chuyển khác không, mạng không đồng nhất. Với mỗi ngộ nhận, nối tới một sự cố cụ thể đã tự gặp trong chương trình. Vấn đề trung tâm: **không phân biệt được một nút chết với một nút chậm**, và mọi cơ chế phát hiện hỏng đều là phỏng đoán dựa trên thời gian chờ. Hệ quả trực tiếp là mọi thiết kế đều phải chọn sẽ sai theo hướng nào khi phỏng đoán sai: coi nút còn sống thì có thể treo, coi nút đã chết thì có thể xử lý hai lần.",
"Nối mỗi ngộ nhận với một sự cố đã gặp trong chương trình, và giải thích vì sao không phân biệt được nút chết với nút chậm.",
"Tầng *hiểu*. Bài mở module, soi lại kinh nghiệm đã có bằng một khung khái niệm. Kiểm bằng bài nối có dẫn chứng; đạt khi nối đúng ít nhất sáu ngộ nhận với sự cố cụ thể kèm số bài.",
"Với mỗi ngộ nhận trong tám, tìm một sự cố đã tự gặp ở các module trước, ghi số bài và biểu hiện. Với hai ngộ nhận không tìm được sự cố tương ứng, thiết kế một thí nghiệm nhỏ để tạo ra nó.",
"Coi tám ngộ nhận là danh sách để thuộc · nghĩ mạng trong một trung tâm dữ liệu thì đáng tin · tin rằng thời gian chờ đủ dài sẽ phân biệt được chết với chậm.",
"Nối đúng ≥ 6/8 ngộ nhận với sự cố cụ thể kèm số bài, và giải thích đúng vì sao chết và chậm không phân biệt được."),

(402,"CAP, PACELC and what they do and do not tell you","LT","Lesson 401",
"Định lý CAP hay bị dùng sai nên phải phát biểu chính xác: khi có phân mảnh mạng, hệ phải chọn giữa tiếp tục phục vụ với dữ liệu có thể cũ và từ chối phục vụ để giữ nhất quán. Ba điều CAP **không** nói và đây là phần quan trọng hơn: nó không nói chọn hai trong ba như cách vẽ tam giác phổ biến, nó không áp dụng khi mạng bình thường, và nó không phải thang đo chất lượng. PACELC bổ sung phần CAP bỏ trống: khi mạng bình thường, hệ vẫn phải chọn giữa độ trễ và nhất quán, và đây mới là lựa chọn ảnh hưởng tới thiết kế hằng ngày. Áp vào hệ dữ liệu: kho phân tích thường chấp nhận dữ liệu cũ vài phút nên chọn sẵn sàng; hệ ghi giao dịch thường chọn nhất quán. Phân mảnh là chuyện hiếm nhưng xảy ra, nên câu hỏi đúng cho thiết kế là hệ sẽ hành xử ra sao trong vài phút phân mảnh, chứ có chọn CAP hay không.",
"Phát biểu đúng CAP cùng ba điều nó không nói, và với ba hệ cho trước nêu hệ đó nghiêng về phía nào khi phân mảnh và khi bình thường.",
"Tầng *hiểu*. Objective gồm cả việc bác bỏ cách hiểu sai phổ biến, vì hiểu sai dẫn tới lập luận sai trong rà soát thiết kế. Kiểm bằng bài phân tích ba hệ; đạt khi phát biểu đúng và phân loại đúng ít nhất hai hệ ở cả hai tình huống.",
"Cho ba hệ đã dùng trong chương trình gồm PostgreSQL có bản sao, Kafka, và kho đối tượng. Với mỗi hệ, nêu hành vi khi phân mảnh và lựa chọn khi mạng bình thường, dẫn bằng cấu hình cụ thể đã đặt ở các module trước. Viết ba câu bác bỏ cách hiểu chọn hai trong ba.",
"Dùng tam giác chọn hai trong ba · coi CAP là thang chất lượng · quên rằng lựa chọn khi mạng bình thường mới là lựa chọn hằng ngày.",
"Phát biểu đúng CAP kèm ba điều nó không nói, và phân loại đúng ≥ 2/3 hệ ở cả hai tình huống kèm cấu hình dẫn chứng."),

(403,"Consistency models from linearizable to eventual","LT","Lesson 402",
"Nhất quán không phải bật tắt mà là một dải, và biết mình đang ở đâu trên dải quyết định bên dùng thấy gì. Bốn mức đủ dùng, xếp từ chặt tới lỏng: tuyến tính hoá nghĩa là hệ hành xử như chỉ có một bản sao duy nhất; nhất quán tuần tự giữ thứ tự nhưng cho phép chậm; nhất quán nhân quả giữ quan hệ nguyên nhân kết quả; nhất quán cuối cùng chỉ hứa các bản sao hội tụ nếu ngừng ghi. Bốn bảo đảm phiên thường đủ cho hệ thực tế và rẻ hơn nhiều: đọc thấy thứ mình vừa ghi, đọc đơn điệu, ghi đơn điệu, và đọc sau ghi. Với hệ dữ liệu, chỗ đau thường gặp đã gặp ở lesson 120: ghi vào bản chính rồi đọc ngay ở bản sao thì không thấy, nên pipeline đọc bản sao phải chịu được điều đó hoặc phải đọc bản chính cho bước kiểm chứng. Cái giá của nhất quán chặt là độ trễ và giảm sẵn sàng, nên chọn mức chặt cho mọi thứ là cách làm hệ chậm mà không thêm giá trị.",
"Chọn mức nhất quán cần thiết cho từng phần của một hệ dữ liệu và nêu hậu quả quan sát được nếu chọn mức lỏng hơn.",
"Tầng *đánh giá*. Objective đòi cân giữa độ chặt và chi phí theo từng phần chứ áp một mức cho cả hệ. Kiểm bằng bốn phần của một hệ; đạt khi chọn đúng ít nhất ba và mỗi lần nêu hậu quả cụ thể.",
"Cho một hệ gồm bốn phần: ghi giao dịch, đọc cho bảng điều khiển, kiểm chứng đối soát, và phân tích theo lô. Chọn mức nhất quán cho từng phần. Tái hiện hiện tượng đọc không thấy thứ vừa ghi trên bản sao và đo cửa sổ thời gian xảy ra hiện tượng đó.",
"Chọn tuyến tính hoá cho mọi thứ · dùng nhất quán cuối cùng cho bước đối soát · không đo độ trễ bản sao rồi giả định nó nhỏ.",
"Chọn đúng mức cho ≥ 3/4 phần kèm hậu quả cụ thể, và có số đo cửa sổ thời gian đọc không thấy thứ vừa ghi."),

(404,"Consensus - replicated log, leader election and quorum","LT","Lesson 403",
"Đồng thuận là bài toán nhiều nút cùng thống nhất một giá trị dù có nút hỏng, và nó là nền của gần như mọi thứ đã dùng: bầu trưởng phân vùng trong Kafka ở lesson 297, hàng đợi quorum ở lesson 286, và bộ điều khiển trong Kubernetes ở lesson 366. Ý tưởng chung của các thuật toán thực dụng: bầu một trưởng, trưởng nhận mọi lệnh ghi và nhân bản thành một nhật ký có thứ tự, và một lệnh được coi là chốt khi đa số đã ghi. Vì sao đa số là ngưỡng: hai đa số bất kỳ luôn giao nhau nên không thể có hai quyết định mâu thuẫn cùng được chốt. Hệ quả thực tế cần nhớ khi thiết kế: cụm ba nút chịu được một nút chết, cụm năm nút chịu được hai, và **cụm chẵn nút không tốt hơn cụm lẻ nhỏ hơn liền kề**. Não phân đôi xảy ra khi hai phần cùng tin mình là trưởng, và cơ chế nhiệm kỳ cùng đa số là thứ ngăn nó. Cái giá: mỗi lần ghi phải chờ đa số nên độ trễ bị neo vào nút chậm thứ hai.",
"Tính số nút chịu lỗi được của một cụm cho trước, và chỉ ra trong bốn hệ đã dùng chỗ nào đang dựa vào đồng thuận.",
"Tầng *hiểu*. Objective là nắm cơ chế đủ để đọc cấu hình cụm và suy ra khả năng chịu lỗi. Kiểm bằng bài tính cộng bài định vị; đạt khi tính đúng cả bốn cấu hình và định vị đúng ít nhất ba hệ.",
"Cho bốn cấu hình cụm với số nút khác nhau, tính số nút chịu lỗi được và giải thích vì sao cụm bốn nút không hơn cụm ba nút. Trong bốn hệ đã dùng, chỉ ra chỗ nào dựa vào đồng thuận và đọc cấu hình thật để biết cụm hiện chịu được mấy nút chết.",
"Dựng cụm chẵn nút · nghĩ thêm nút luôn tăng khả năng chịu lỗi · quên rằng độ trễ ghi phụ thuộc nút chậm thứ hai · tin rằng đồng thuận loại bỏ được mọi khả năng mất dữ liệu.",
"Tính đúng khả năng chịu lỗi cả bốn cấu hình, và định vị đúng ≥ 3/4 chỗ dựa vào đồng thuận trong hệ đã dựng."),

(405,"Time, ordering and causality in a distributed system","LT","Lesson 404",
"Đồng hồ trên các máy khác nhau luôn lệch, nên dấu thời gian từ hai máy không so được một cách đáng tin, và đây là gốc của nhiều lỗi khó tìm. Hai loại đồng hồ và cách dùng đúng: đồng hồ theo giờ thật có thể nhảy lùi khi đồng bộ nên không được dùng để đo khoảng thời gian; đồng hồ đơn điệu chỉ tăng nên dùng để đo khoảng. Lỗi điển hình trong hệ dữ liệu: khử trùng hoặc chọn bản mới nhất bằng cách so dấu thời gian từ nhiều nguồn, và khi đồng hồ lệch thì chọn nhầm bản cũ. Thứ tự nhân quả và cách ghi nó mà không dựa vào đồng hồ: số thứ tự theo nguồn, hoặc đồng hồ logic. Nối lại thời gian sự kiện và thời gian xử lý ở lesson 317: đó chính là biểu hiện của vấn đề này ở tầng ứng dụng. Ba quy tắc thực dụng: không so dấu thời gian từ hai máy để quyết định thứ tự, dùng số thứ tự của nguồn khi có, và luôn lưu cả dấu thời gian nguồn lẫn dấu thời gian nhận.",
"Chỉ ra trong một thiết kế cho trước chỗ nào đang dựa vào đồng hồ để quyết định thứ tự, và đề xuất cơ chế thay thế.",
"Tầng *phân tích*. Objective là phát hiện một loại lỗi tiềm ẩn khó tái hiện, kỹ năng dùng trong rà soát thiết kế. Kiểm bằng ba thiết kế có lỗi; đạt khi chỉ đúng ít nhất hai và đề xuất cơ chế thay thế đúng.",
"Cho ba thiết kế dùng dấu thời gian để chọn bản ghi mới nhất. Với mỗi cái, chỉ ra kịch bản đồng hồ lệch làm nó chọn sai, và đề xuất thay thế. Mô phỏng lệch đồng hồ giữa hai nguồn và tái hiện một lần chọn sai trong bảng loại 2 ở lesson 314.",
"Dùng dấu thời gian giờ thật để đo khoảng · so dấu thời gian từ hai nguồn để quyết định thứ tự · giả định đồng bộ đồng hồ là đủ chính xác.",
"Chỉ đúng ≥ 2/3 thiết kế có lỗi kèm cơ chế thay thế, và tái hiện được một lần chọn sai do lệch đồng hồ."),

(406,"Partitioning and rebalancing at the system level","LT","Lesson 405",
"Chia dữ liệu ra nhiều nút là cách duy nhất vượt giới hạn một máy, và ba chiến lược chia đã gặp dưới nhiều tên: theo khoảng khoá, theo băm của khoá, và theo danh mục tra cứu. Theo khoảng giữ được truy vấn theo dải nhưng dễ tạo điểm nóng khi khoá tăng dần, ví dụ khoá là dấu thời gian thì mọi ghi mới dồn vào một phân vùng. Theo băm chia đều hơn nhưng mất khả năng truy vấn theo dải. Bài toán chung đã gặp ba lần trong chương trình: phân vùng Kafka ở lesson 293, phân vùng Spark ở lesson 351, và phân vùng bảng ở lesson 336; điểm chung là **số phân vùng cố định thì cân bằng lại tốn kém, số phân vùng linh hoạt thì phức tạp hơn**. Băm nhất quán giảm lượng dữ liệu phải di chuyển khi thêm hoặc bớt nút. Cân bằng lại nên là thao tác có kiểm soát chứ tự động hoàn toàn, vì cân bằng lại lúc hệ đang tải nặng làm mọi thứ tệ hơn.",
"Chọn chiến lược chia cho ba khối lượng công việc và nêu chi phí cân bằng lại khi thêm nút.",
"Tầng *đánh giá*. Objective đòi chọn có cân nhắc giữa khả năng truy vấn và độ đều, chứ áp một chiến lược. Kiểm bằng ba khối lượng công việc; đạt khi chọn đúng cả ba và ước lượng đúng hướng chi phí cân bằng lại.",
"Cho ba khối lượng công việc có mẫu truy vấn khác nhau. Chọn chiến lược chia cho từng cái. Mô phỏng phân bố khoá thật và đo độ đều của hai chiến lược. Tính lượng dữ liệu phải di chuyển khi thêm một nút, với băm thường và với băm nhất quán.",
"Chia theo khoá tăng dần rồi tạo điểm nóng · dùng băm khi cần truy vấn theo dải · cân bằng lại tự động lúc tải cao · quên chi phí di chuyển dữ liệu.",
"Chọn đúng chiến lược cho cả ba khối lượng công việc, và có số so lượng dữ liệu di chuyển giữa hai cách băm."),

(407,"Replication strategies and the read path","LT","Lesson 406",
"Nhân bản phục vụ ba mục đích khác nhau và trộn lẫn chúng dẫn tới thiết kế sai: chịu lỗi, tăng khả năng đọc, và đặt dữ liệu gần người dùng. Ba kiểu và hệ quả: một trưởng nhiều bản sao là kiểu phổ biến nhất và đơn giản nhất về nhất quán, ghi qua một chỗ nên trưởng là nút thắt ghi; nhiều trưởng cho phép ghi ở nhiều nơi nhưng sinh xung đột phải giải; không trưởng dùng ghi và đọc theo đa số. Nhân bản đồng bộ bảo đảm không mất dữ liệu khi trưởng chết nhưng neo độ trễ ghi vào bản sao chậm nhất; bất đồng bộ nhanh nhưng có cửa sổ mất dữ liệu, và cửa sổ đó chính là điểm khôi phục ở lesson 395. Đường đọc là nơi quyết định người dùng thấy gì: đọc từ trưởng thì luôn mới nhưng không giảm tải, đọc từ bản sao thì giảm tải nhưng có thể cũ, đọc theo đa số thì mới nhưng tốn. Ba mẫu thực dụng cho hệ dữ liệu.",
"Chọn kiểu nhân bản và đường đọc cho một yêu cầu cho trước, và nêu cửa sổ mất dữ liệu tương ứng.",
"Tầng *đánh giá*. Objective đòi nối lựa chọn kỹ thuật với hai con số mục tiêu khôi phục ở lesson 395. Kiểm bằng ba yêu cầu; đạt khi chọn đúng cả ba và nêu đúng cửa sổ mất dữ liệu của từng lựa chọn.",
"Cho ba yêu cầu khác nhau về độ mới và độ chịu lỗi. Chọn kiểu nhân bản và đường đọc cho từng cái. Trên cụm PostgreSQL đã dựng, đo độ trễ ghi ở chế độ đồng bộ và bất đồng bộ, và đo cửa sổ mất dữ liệu bằng cách giết trưởng lúc đang ghi.",
"Dùng bản sao để giảm tải mà không xét độ trễ bản sao · chọn nhân bản bất đồng bộ cho dữ liệu không được mất · nghĩ nhân bản thay được sao lưu.",
"Chọn đúng cả ba yêu cầu, và có số đo cửa sổ mất dữ liệu thực tế khi giết trưởng ở chế độ bất đồng bộ."),

(408,"Caching and invalidation in a data platform","TH","Lesson 407",
"Bộ nhớ đệm đổi độ mới lấy độ trễ và chi phí, nên câu hỏi thiết kế luôn là chấp nhận dữ liệu cũ tới mức nào. Bốn tầng đệm trong một nền tảng dữ liệu: đệm kết quả truy vấn ở tầng phục vụ, bảng tổng hợp dựng sẵn, đệm ở tầng ứng dụng, và đệm trang của hệ điều hành đã gặp ở M2. Ba chiến lược làm mới và điều kiện dùng: hết hạn theo thời gian là đơn giản nhất và đủ cho phần lớn bảng điều khiển; vô hiệu hoá theo sự kiện chính xác hơn nhưng đòi biết ai phụ thuộc vào cái gì, và đây là chỗ lineage ở M26 trả cổ tức; dựng lại theo lịch phù hợp với bảng tổng hợp. Ba vấn đề kinh điển: đệm rỗng đồng loạt khi nhiều yêu cầu cùng thấy hết hạn và cùng dựng lại, dữ liệu cũ phục vụ lâu hơn dự kiến vì quên vô hiệu hoá một nhánh, và đệm chứa dữ liệu nhạy cảm không được phân quyền. Đo tỉ lệ trúng đệm và chi phí tiết kiệm để biết đệm có đáng giữ không.",
"Thiết kế tầng đệm cho bảng điều khiển với chiến lược làm mới phù hợp, và đo tỉ lệ trúng cùng độ mới thực tế.",
"Tầng *áp dụng*. Objective là một thiết kế có hai đại lượng đo được và ràng buộc về độ mới. Kiểm bằng cặp số đo; đạt khi tỉ lệ trúng trên ngưỡng và độ mới trong cam kết ở lesson 387.",
"Thêm tầng đệm cho bảng điều khiển đọc mart. Thử cả ba chiến lược làm mới, với mỗi chiến lược đo tỉ lệ trúng, độ trễ và độ mới thực tế. Tạo tình huống đệm rỗng đồng loạt và quan sát tải lên kho. Thêm cơ chế chặn và đo lại.",
"Đặt thời gian hết hạn dài cho dữ liệu cần mới · vô hiệu hoá theo sự kiện mà không có lineage đầy đủ · đệm dữ liệu nhạy cảm không phân quyền · giữ đệm mà chưa từng đo tỉ lệ trúng.",
"Tỉ lệ trúng trên ngưỡng, độ mới nằm trong cam kết, và cơ chế chặn đệm rỗng đồng loạt giảm được đỉnh tải có số."),

(409,"Idempotency, deduplication and the outbox pattern","TH","Lesson 408",
"Bài gom một nguyên tắc đã xuất hiện ở tám module thành một bộ công cụ thiết kế. Ghi bất biến là điều kiện nền cho mọi thứ khác: thử lại an toàn, chạy bù an toàn, phát lại an toàn. Ba cách cài đặt và điều kiện áp dụng: khoá tự nhiên từ nghiệp vụ ở lesson 208 là cách bền nhất; khoá do bên gửi sinh dùng khi không có khoá nghiệp vụ; bảng đã xử lý dùng khi đích không hỗ trợ ghi đè theo khoá. Mẫu hộp thư đi giải một bài toán cụ thể và phổ biến: ghi vào cơ sở dữ liệu rồi phát một sự kiện là hai thao tác trên hai hệ, nên chết giữa chừng làm hai bên lệch nhau; giải bằng cách ghi sự kiện vào một bảng trong cùng giao dịch với dữ liệu, rồi một tiến trình riêng đọc bảng đó và phát đi, thường bằng CDC ở M31. Nhờ vậy chỉ còn một thao tác nguyên tử. Ba biến thể và chi phí của từng biến thể.",
"Cài đặt mẫu hộp thư đi cho một tuyến ghi rồi phát sự kiện, và chứng minh bằng thí nghiệm hỏng rằng cơ sở dữ liệu và luồng không lệch nhau.",
"Tầng *sáng tạo*. Objective đòi ghép giao dịch, CDC và ghi bất biến thành một mẫu giải bài toán hai hệ. Kiểm bằng thí nghiệm giết tiến trình; đạt khi qua mười lần giết mà không có sự kiện thiếu hoặc thừa so với bản ghi.",
"Cài tuyến ghi đơn hàng rồi phát sự kiện theo cách ngây thơ, giết tiến trình giữa hai thao tác và đếm mức lệch. Cài lại bằng mẫu hộp thư đi dùng CDC. Giết tiến trình mười lần ở các thời điểm khác nhau và đối soát số sự kiện với số bản ghi.",
"Ghi cơ sở dữ liệu rồi phát sự kiện trong hai thao tác rời · dùng giao dịch phân tán khi mẫu hộp thư đi đủ · quên dọn bảng hộp thư nên nó phình.",
"Bản ngây thơ định lượng được mức lệch, bản hộp thư đi qua mười lần giết mà số sự kiện khớp số bản ghi tuyệt đối."),

(410,"Backpressure and load shedding across services","TH","Lesson 409",
"Áp lực ngược trong một engine đã gặp ở lesson 326; bài này mở rộng ra giữa các dịch vụ, nơi không có cơ chế tự động nào. Khi bên nhận chậm hơn bên gửi, có đúng bốn lựa chọn và phải chọn một cách có ý thức: đệm lại và chấp nhận độ trễ tăng, làm chậm bên gửi, từ chối bớt yêu cầu, hoặc giảm chất lượng dịch vụ. Đệm vô hạn là lựa chọn tệ nhất và cũng là mặc định phổ biến nhất, vì nó biến một sự cố chậm thành một sự cố hết bộ nhớ, đúng vấn đề hàng đợi không giới hạn ở M6. Giảm tải chủ động: từ chối một phần để phần còn lại được phục vụ đúng, và tiêu chí chọn từ chối cái gì phải do nghiệp vụ quyết chứ ngẫu nhiên. Hàng đợi có giới hạn cộng chính sách khi đầy là cách cài đặt thực tế. Nối với bộ ngắt mạch ở lesson 394: ngắt mạch bảo vệ bên gọi, giảm tải bảo vệ bên bị gọi, và hệ cần cả hai.",
"Chọn và cài đặt chiến lược xử lý quá tải cho một tuyến, và chứng minh hệ suy giảm có kiểm soát thay vì sụp.",
"Tầng *áp dụng*. Objective là một cơ chế phòng vệ kiểm được bằng thí nghiệm quá tải. Kiểm bằng phép thử tải gấp năm lần công suất; đạt khi hệ vẫn phục vụ phần được ưu tiên và không có thành phần nào hết bộ nhớ.",
"Đẩy tải gấp năm lần công suất vào tuyến xử lý. Quan sát hành vi với hàng đợi không giới hạn và ghi lại điều gì hỏng trước. Thay bằng hàng đợi có giới hạn cộng chính sách giảm tải theo mức ưu tiên nghiệp vụ. Đo tỉ lệ phục vụ của phần ưu tiên cao ở cả hai cấu hình.",
"Để hàng đợi không giới hạn · giảm tải ngẫu nhiên thay vì theo ưu tiên nghiệp vụ · tăng tài nguyên thay vì đặt giới hạn · thử lại ngay khi bị từ chối.",
"Cấu hình có giới hạn giữ được tỉ lệ phục vụ của phần ưu tiên cao ở mức chấp nhận được, và không thành phần nào hết bộ nhớ."),

(411,"Estimating - back of the envelope for a data platform","TH","Lesson 410",
"Ước lượng nhanh là kỹ năng phân biệt bản thiết kế có cơ sở với bản thiết kế là danh sách công cụ, và nó được hỏi trong gần như mọi buổi phỏng vấn thiết kế. Quy trình năm bước: từ số liệu nghiệp vụ suy ra số sự kiện mỗi giây, nhân kích thước bản ghi ra thông lượng byte, nhân thời gian giữ ra dung lượng, nhân hệ số nhân bản và hệ số phình khi xử lý, rồi quy ra số máy và chi phí. Bộ số mốc cần thuộc để ước lượng mà không tra: độ trễ đọc bộ nhớ, đọc đĩa thể rắn, gọi mạng trong trung tâm dữ liệu, gọi qua Internet, và thông lượng một nút Kafka hay một trình thực thi Spark, tất cả đều đã tự đo trong chương trình nên dùng số của chính mình. Nguyên tắc: đúng bậc độ lớn là đủ, và **mọi ước lượng phải nêu giả định**, vì người rà soát kiểm giả định chứ kiểm phép nhân. Ba chỗ hay sai: quên hệ số nhân bản, quên đỉnh tải so với trung bình, và quên dữ liệu phình khi giải nén.",
"Ước lượng dung lượng, thông lượng và chi phí cho một yêu cầu nghiệp vụ cho trước, nêu rõ giả định, và cùng bậc với số đo thật.",
"Tầng *áp dụng*. Objective là một quy trình tính có kiểm chứng được bằng đối chiếu với lab. Kiểm bằng so ước lượng với thực đo; đạt khi cùng bậc độ lớn ở ít nhất bốn trong năm đại lượng và mọi giả định được nêu.",
"Cho một yêu cầu nghiệp vụ. Ước lượng năm đại lượng theo quy trình năm bước, ghi rõ giả định từng bước. Đối chiếu với số đo thật từ các lab đã làm. Lập bảng ước lượng và thực đo, giải thích mọi chỗ lệch quá một bậc.",
"Ước lượng mà không nêu giả định · dùng số trung bình cho đỉnh tải · quên hệ số nhân bản · tra số trên mạng thay vì dùng số đã tự đo.",
"Ước lượng cùng bậc với thực đo ở ≥ 4/5 đại lượng, mọi giả định được nêu, và chỗ lệch quá một bậc có giải thích."),

(412,"Designing for a read-heavy analytics workload","TH","Lesson 411",
"Bài thiết kế đầu, trên loại khối lượng công việc quen thuộc nhất. Yêu cầu: hàng trăm người dùng chạy truy vấn phân tích trên dữ liệu vài chục terabyte, độ tươi trong vài giờ là đủ, ngân sách có hạn. Quy trình thiết kế sáu bước dùng lại cho cả ba bài: làm rõ yêu cầu bằng câu hỏi, ước lượng theo lesson 411, vẽ luồng dữ liệu từ nguồn tới người dùng, chọn thành phần cho từng chặng kèm lý do, nêu chế độ hỏng và cách chặn, rồi nêu điều kiện làm thiết kế này sai. Các lựa chọn chính phải bảo vệ được: bố trí lưu trữ theo M33, tách tầng phục vụ khỏi tầng xử lý, chiến lược đệm và bảng tổng hợp theo lesson 408, và cách kiểm soát chi phí khi nhiều người chạy truy vấn nặng. Chỗ hay sai ở loại khối lượng công việc này: thiết kế cho đỉnh tải cùng lúc thay vì cho tải trung bình cộng khả năng co giãn.",
"Trình bày một thiết kế đầy đủ sáu bước cho khối lượng công việc đọc nặng, và bảo vệ được ít nhất ba lựa chọn dưới chất vấn.",
"Tầng *sáng tạo*. Objective là tổng hợp toàn chương trình thành một thiết kế có lý do. Kiểm bằng buổi trình bày có chất vấn; đạt khi sáu bước đầy đủ và ba lựa chọn được bảo vệ bằng ước lượng hoặc số đo.",
"Nhận yêu cầu, chạy sáu bước, trình bày trong 20 phút. Hai bạn cùng lớp chất vấn ba lựa chọn bất kỳ. Nộp bản thiết kế gồm sơ đồ luồng dữ liệu, bảng ước lượng, bảng chế độ hỏng, và ba điều kiện làm thiết kế sai.",
"Vẽ sơ đồ trước khi làm rõ yêu cầu · liệt kê công cụ mà không nêu lý do · thiết kế cho đỉnh tải cùng lúc · bỏ phần điều kiện làm thiết kế sai.",
"Bản thiết kế đủ sáu bước, ba lựa chọn được bảo vệ bằng ước lượng hoặc số đo, và nêu được ba điều kiện làm thiết kế sai."),

(413,"Designing a real-time pipeline under a latency budget","TH","Lesson 412",
"Bài thiết kế thứ hai, với ràng buộc độ trễ làm đổi gần như mọi lựa chọn. Yêu cầu: phát hiện giao dịch bất thường trong vòng vài giây kể từ lúc phát sinh. Kỹ thuật trung tâm là **phân bổ ngân sách độ trễ**: chia tổng ngân sách cho từng chặng gồm sinh sự kiện, vận chuyển, xử lý, tra cứu làm giàu, và ghi kết quả; rồi kiểm tổng có vừa không. Phân bổ xong thì mỗi chặng thành một ràng buộc kiểm được, và chặng nào không đạt thì phải đổi thiết kế chứ hy vọng. Các lựa chọn phải bảo vệ: engine luồng thuần hay lô vi mô theo lesson 327 và 354, cách làm giàu không tra cứu đồng bộ theo lesson 324, chu kỳ điểm kiểm tra ảnh hưởng độ trễ đầu cuối theo lesson 322, và mức ngữ nghĩa giao nhận cần thiết. Câu hỏi phải trả lời được: chuyện gì xảy ra khi một chặng vượt ngân sách, và hệ suy giảm ra sao thay vì sụp.",
"Phân bổ ngân sách độ trễ cho từng chặng, chứng minh tổng vừa ngân sách bằng số đo, và nêu hành vi suy giảm khi một chặng vượt.",
"Tầng *sáng tạo*. Objective đòi thiết kế dưới một ràng buộc định lượng cứng. Kiểm bằng bảng ngân sách đối chiếu số đo; đạt khi tổng đo được nằm trong ngân sách và có phương án suy giảm cụ thể.",
"Nhận yêu cầu có ngân sách độ trễ. Phân bổ cho năm chặng. Với mỗi chặng, dẫn một số đo từ lab đã làm để chứng minh khả thi. Trình bày và chất vấn. Nêu hành vi của hệ khi chặng làm giàu vượt ngân sách gấp ba lần.",
"Đặt ngân sách tổng mà không chia chặng · dùng tra cứu đồng bộ trong đường nóng · quên chu kỳ điểm kiểm tra khi tính độ trễ · không có phương án suy giảm.",
"Bảng ngân sách năm chặng đều có số đo hỗ trợ, tổng nằm trong ngân sách, và có phương án suy giảm cụ thể."),

(414,"Designing for multi-tenancy and isolation","TH","Lesson 413",
"Bài thiết kế thứ ba, trên ràng buộc ít được dạy nhưng gặp thường xuyên: nhiều khách hàng hoặc nhiều phòng ban dùng chung một nền tảng. Ba mức cô lập theo chi phí tăng dần: chung mọi thứ và tách bằng cột định danh, chung hạ tầng nhưng tách lược đồ hoặc cơ sở dữ liệu, và tách hoàn toàn. Bốn khía cạnh phải xét riêng chứ gộp: cô lập dữ liệu để bên này không đọc được dữ liệu bên kia, cô lập hiệu năng để một bên chạy truy vấn nặng không làm chậm bên khác, cô lập chi phí để tính được ai tốn bao nhiêu, và cô lập vận hành để nâng cấp cho một bên không ảnh hưởng bên khác. Vấn đề hàng xóm ồn ào và ba cơ chế chặn: hạn mức tài nguyên, hàng đợi riêng theo mức ưu tiên, và giới hạn tốc độ. Bảo mật mức dòng theo lesson 396 là cách rẻ nhất cho cô lập dữ liệu nhưng không cho cô lập hiệu năng, nên nói rõ nó giải được gì.",
"Chọn mức cô lập cho bốn khía cạnh theo yêu cầu cho trước, và chứng minh bằng thí nghiệm rằng hàng xóm ồn ào không làm hỏng bên còn lại.",
"Tầng *đánh giá*. Objective đòi quyết định riêng cho từng khía cạnh thay vì chọn một mức cho tất cả. Kiểm bằng bảng bốn khía cạnh cộng thí nghiệm; đạt khi bốn quyết định có lý do và thí nghiệm hàng xóm ồn ào cho kết quả trong ngưỡng.",
"Cho yêu cầu nhiều bên dùng chung. Quyết định mức cô lập cho từng khía cạnh trong bốn, kèm chi phí. Cài hạn mức tài nguyên. Chạy một truy vấn rất nặng ở bên A và đo ảnh hưởng lên độ trễ của bên B, trước và sau khi có hạn mức.",
"Chọn một mức cô lập cho cả bốn khía cạnh · dùng bảo mật mức dòng rồi tưởng đã cô lập hiệu năng · không tính được chi phí theo từng bên · bỏ qua cô lập vận hành khi nâng cấp.",
"Bốn quyết định có lý do và chi phí kèm theo, và độ trễ bên B sau khi có hạn mức nằm trong ngưỡng dù bên A chạy truy vấn nặng."),

(415,"Writing an architecture decision record that survives review","TH","Lesson 414",
"Tài liệu quyết định kiến trúc là thứ giữ lại lý do khi người ra quyết định đã rời đi, và đây là phần có giá trị dài hạn nhất của cả module. Cấu trúc năm phần: bối cảnh và ràng buộc, các phương án đã cân nhắc, quyết định, hệ quả gồm cả mặt tốt lẫn mặt xấu, và điều kiện xem lại. Phần các phương án bị loại là phần **giá trị nhất và hay bị bỏ nhất**: người đọc sau cần biết phương án kia đã được xét và loại vì lý do gì, nếu không họ sẽ đề xuất lại đúng phương án đó. Điều kiện xem lại làm tài liệu này khác một biên bản: ghi rõ mốc nào thì quyết định này nên được xét lại, ví dụ khi khối lượng vượt một ngưỡng hoặc khi đội vượt một quy mô. Viết ngắn và cụ thể; tài liệu mười trang không ai đọc. Nộp vào kho mã cùng mã nguồn, đánh số, và không sửa tài liệu cũ mà viết tài liệu mới thay thế nó.",
"Viết một tài liệu quyết định kiến trúc đủ năm phần cho một lựa chọn đã làm, và qua được rà soát chéo về phần phương án bị loại.",
"Tầng *áp dụng*. Objective là một sản phẩm viết theo chuẩn, kiểm được bằng rà soát của người không dự buổi quyết định. Kiểm bằng rà soát chéo; đạt khi người rà soát hiểu được lý do mà không cần hỏi thêm và điều kiện xem lại là kiểm được.",
"Chọn ba quyết định lớn đã làm trong các module trước. Viết tài liệu cho từng quyết định, đủ năm phần, mỗi tài liệu dưới hai trang. Đổi bài với một học viên khác: họ đọc và ghi lại mọi câu hỏi còn phải hỏi. Sửa cho tới khi không còn câu hỏi nào về lý do.",
"Bỏ phần phương án bị loại · viết hệ quả chỉ có mặt tốt · đặt điều kiện xem lại chung chung · sửa tài liệu cũ thay vì viết bản thay thế.",
"Ba tài liệu đủ năm phần và dưới hai trang, và người rà soát không còn câu hỏi nào về lý do quyết định."),

(416,"Design review - defend a design under changing constraints","KT","Lesson 415",
"Cổng của chặng 8. Bài kiểm năng lực thiết kế và bảo vệ, không có nội dung mới.",
"Bảo vệ được một thiết kế nền tảng dữ liệu dưới chất vấn, và phản ứng đúng khi hội đồng đổi một ràng buộc giữa buổi.",
"Tầng *đánh giá*. Cổng đo năng lực ra quyết định kiến trúc có bằng chứng dưới chất vấn, nên hình thức là buổi bảo vệ trực tiếp.",
"Nhận một yêu cầu nền tảng dữ liệu chưa rõ ràng, 30 phút chuẩn bị, 30 phút bảo vệ. Bài chấm năm phần: A (20đ) làm rõ yêu cầu bằng câu hỏi đúng trước khi vẽ · B (25đ) ước lượng năm đại lượng, nêu giả định, cùng bậc với số đo đã có · C (25đ) lựa chọn thành phần, mỗi lựa chọn dẫn về một ràng buộc · D (20đ) hội đồng đổi một ràng buộc giữa buổi, phản ứng có lập luận · E (10đ) ba điều kiện làm thiết kế này sai. Cả hai hướng giữ và đổi kết luận đều được điểm nếu lập luận dẫn từ ước lượng.",
"Vẽ sơ đồ trước khi hỏi · liệt kê công cụ không nêu lý do · đổi kết luận khi bị vặn mà không dẫn số nào · bỏ phần E.",
"Đạt ≥ 70/100, phần B và D đều ≥ 60%. Lựa chọn nào không dẫn được về một ràng buộc thì không tính điểm."),
]

M40 = ("Capstone - Build and Defend a Data Platform", 417, 422, """| | |
|---|---|
| **Objective cấp module** | Xây và vận hành một nền tảng dữ liệu đầu cuối trên yêu cầu nghiệp vụ thật, rồi bảo vệ nó trước hội đồng dưới sự cố gây trực tiếp |
| **Tiền đề** | M39 |
| **Exit criterion** | Nền tảng chạy đúng đầu cuối, qua được sự cố hội đồng gây ra trong buổi bảo vệ, và mọi quyết định thiết kế dẫn được về một ràng buộc hoặc một số đo |
| **Kỹ năng SFIA** | `ARCH` mức 5 · `DTAN` mức 4 · `CFMG` mức 4 |
| **Chế độ hỏng** | Dồn toàn bộ vào phần xây, bỏ phần vận hành và tài liệu, rồi không xử lý được sự cố trong buổi bảo vệ |""",
"""Sáu bài tương ứng sáu giai đoạn, mỗi giai đoạn có sản phẩm nộp riêng. Đề bài lấy từ một yêu cầu nghiệp vụ thật chứ dữ liệu mẫu có sẵn.

Trọng số chấm phản ánh trọng tâm của cả chương trình: khả năng phục hồi và vận hành chiếm 25%, ngang với phần xây. Một nền tảng chạy đúng nhưng không phục hồi được sau sự cố **không đạt**, dù kết quả đúng.""")

L40 = [
(417,"Scoping the platform and writing the contract","DA","Module 40: M39",
"Giai đoạn một: biến một yêu cầu nghiệp vụ mơ hồ thành phạm vi có biên rõ và một hợp đồng dữ liệu. Sản phẩm nộp gồm bốn thứ: danh sách câu hỏi nghiệp vụ mà nền tảng phải trả lời được, xếp theo ưu tiên; bảng ước lượng năm đại lượng theo lesson 411 kèm giả định; hợp đồng dữ liệu cho mỗi nguồn theo chuẩn M26 gồm lược đồ, ngữ nghĩa, chất lượng, độ tươi và quy trình đổi; và mục tiêu mức dịch vụ cho bốn chỉ báo theo lesson 387. Yêu cầu về phạm vi: nêu rõ cái gì **không** làm, vì phạm vi không có biên là nguyên nhân số một khiến dự án tốt nghiệp không xong. Rà soát phạm vi với giảng viên đóng vai bên nghiệp vụ, và phạm vi chỉ được chốt sau khi qua rà soát này.",
"Nộp phạm vi có biên rõ, ước lượng có giả định, hợp đồng cho mọi nguồn, và mục tiêu mức dịch vụ đo được.",
"Tầng *đánh giá*. Giai đoạn đòi phán đoán về phạm vi dưới ràng buộc thời gian có hạn. Kiểm bằng rà soát phạm vi; đạt khi bốn sản phẩm đầy đủ và phần ngoài phạm vi được nêu rõ.",
"Nhận yêu cầu nghiệp vụ. Phỏng vấn giảng viên đóng vai bên nghiệp vụ để làm rõ. Nộp bốn sản phẩm. Qua buổi rà soát phạm vi, trong đó phải bảo vệ được cả phần đã loại khỏi phạm vi.",
"Nhận mọi yêu cầu vào phạm vi · ước lượng mà không nêu giả định · bỏ phần hợp đồng vì thấy chưa cần · đặt mục tiêu mức dịch vụ bằng số tròn.",
"Bốn sản phẩm đầy đủ, phần ngoài phạm vi nêu rõ kèm lý do, và qua được buổi rà soát phạm vi."),

(418,"Build - ingestion and storage","DA","Lesson 417",
"Giai đoạn hai: đưa dữ liệu từ nguồn về và bố trí lưu trữ. Yêu cầu bắt buộc: ít nhất hai loại nguồn khác nhau trong đó một nguồn là CDC theo M31 hoặc một luồng theo M29; tầng đồng bất biến giữ nguyên bản gốc; bố trí lưu trữ có quyết định đầy đủ sáu điểm theo lesson 341; và kiểm chất lượng ở biên nhận theo M20 với vùng cách ly cho bản ghi lỗi. Ba thứ phải chứng minh được ở cuối giai đoạn: nạp lại toàn bộ cho cùng kết quả, bản ghi lỗi vào vùng cách ly chứ bị bỏ im lặng, và số byte quét của bộ truy vấn chuẩn nằm trong ngưỡng nhờ bố trí. Nộp kèm bảng quyết định bố trí và số đo hỗ trợ từng quyết định.",
"Nạp được dữ liệu từ hai loại nguồn vào bố trí lưu trữ đã thiết kế, với tính bất biến và kiểm chất lượng được chứng minh.",
"Tầng *sáng tạo*. Giai đoạn xây có ba tính chất kiểm được bằng thực nghiệm. Kiểm bằng ba phép thử; đạt khi cả ba qua và bảng quyết định bố trí có số đo hỗ trợ.",
"Xây tuyến nạp cho hai loại nguồn. Chạy lại toàn bộ và đối soát để chứng minh tính bất biến. Tiêm bản ghi lỗi và chứng minh chúng vào vùng cách ly có lý do. Chạy bộ truy vấn chuẩn và đo byte quét. Nộp bảng quyết định bố trí.",
"Bỏ tầng đồng bất biến để tiết kiệm dung lượng · nạp một loại nguồn cho nhanh · bỏ kiểm chất lượng ở biên · chọn bố trí theo thói quen mà không đo.",
"Ba phép thử đều qua, và mọi quyết định bố trí trong bảng có ít nhất một số đo hỗ trợ."),

(419,"Build - transformation, orchestration and quality","DA","Lesson 418",
"Giai đoạn ba: biến dữ liệu thô thành lớp phục vụ, có điều phối và có kiểm chất lượng. Yêu cầu bắt buộc: mô hình chiều cho lớp phục vụ theo M19 với phát biểu hạt rõ cho từng bảng; điều phối bằng một trong ba công cụ ở M22 tới M24 với lựa chọn dẫn về ma trận ở lesson 266; mọi tác vụ bất biến khi chạy lại và chạy bù được theo khoảng dữ liệu; và bộ kiểm chất lượng có ngưỡng, có cảnh báo, có vùng cách ly. Phép thử nghiệm thu của giai đoạn: chạy bù 30 ngày dữ liệu và đối soát khớp tuyệt đối với bản chạy tuần tự, đây là phép thử mà không có tính bất biến thì không qua được. Nộp kèm đồ thị phụ thuộc và một tài liệu quyết định kiến trúc theo lesson 415 cho lựa chọn bộ điều phối.",
"Xây lớp biến đổi có điều phối và kiểm chất lượng, và chạy bù 30 ngày cho kết quả khớp tuyệt đối.",
"Tầng *sáng tạo*. Giai đoạn đòi tổng hợp mô hình hoá, điều phối và chất lượng dưới ràng buộc chạy bù. Kiểm bằng phép chạy bù; đạt khi đối soát khớp tuyệt đối và tài liệu quyết định qua rà soát.",
"Xây lớp biến đổi và đồ thị điều phối. Chạy bù 30 ngày và đối soát với bản chạy tuần tự. Tiêm ba lỗi chất lượng và chứng minh cả ba bị bắt và cách ly. Nộp đồ thị phụ thuộc và tài liệu quyết định cho lựa chọn bộ điều phối.",
"Dùng thời gian chạy thay cho khoảng dữ liệu · bỏ phát biểu hạt · chọn bộ điều phối theo quen tay mà không dẫn ma trận · kiểm chất lượng không có ngưỡng.",
"Chạy bù 30 ngày đối soát khớp tuyệt đối, ba lỗi chất lượng đều bị bắt, và tài liệu quyết định qua rà soát."),

(420,"Operate - observability, failure drill and cost","DA","Lesson 419",
"Giai đoạn bốn, giai đoạn phân biệt bài đạt với bài giỏi: đưa nền tảng vào trạng thái vận hành được. Yêu cầu bắt buộc theo M38: số đo ba tầng và bảng điều khiển trả lời được năm câu hỏi chẩn đoán; cảnh báo đạt bốn tiêu chí ở lesson 390; sổ tay xử lý cho ít nhất ba sự cố hay gặp; bảng chế độ hỏng có đánh dấu điểm hỏng đơn lẻ; kế hoạch khôi phục có hai con số mục tiêu và đã diễn tập thật; và hoá đơn ước lượng chia theo thành phần kèm hai khoản cắt được. Tự chạy một buổi diễn tập sự cố trước khi bảo vệ và nộp bản phân tích sau sự cố của buổi đó, vì đội chưa từng diễn tập thì gần như chắc chắn không qua được sự cố ở buổi bảo vệ.",
"Đưa nền tảng vào trạng thái vận hành được đủ sáu yêu cầu, và tự chạy được một buổi diễn tập sự cố có phân tích sau sự cố.",
"Tầng *sáng tạo*. Giai đoạn đòi dựng một hệ vận hành hoàn chỉnh và tự kiểm chứng nó. Kiểm bằng rà soát sáu yêu cầu cộng biên bản diễn tập; đạt khi cả sáu đạt và diễn tập có khôi phục thật trong thời gian mục tiêu.",
"Dựng đủ sáu yêu cầu. Tự tổ chức một buổi diễn tập sự cố: một người gây sự cố, phần còn lại xử lý theo bảy bước. Nộp biên bản diễn tập, dòng thời gian, và bản phân tích sau sự cố có hành động khắc phục có chủ và hạn.",
"Dựng bảng điều khiển đẹp mà không trả lời được câu hỏi chẩn đoán · viết sổ tay sau khi bảo vệ · kế hoạch khôi phục chưa diễn tập · bỏ phần chi phí.",
"Sáu yêu cầu đều đạt, buổi diễn tập có khôi phục thật trong thời gian mục tiêu, và phân tích sau sự cố có hành động có chủ và hạn."),

(421,"Documentation, runbook and handover","DA","Lesson 420",
"Giai đoạn năm: làm cho người khác tiếp quản được. Bộ tài liệu tối thiểu: tài liệu kiến trúc có sơ đồ luồng dữ liệu, tập tài liệu quyết định cho mọi lựa chọn lớn theo lesson 415, hợp đồng dữ liệu cho bên dùng cuối gồm định nghĩa chỉ số và hạn chế diễn giải theo M26, sổ tay vận hành, và hướng dẫn dựng lại từ đầu. Phép thử nghiệm thu là phép thử bàn giao thật, giống phép thử ở lesson 275 nhưng ở quy mô nền tảng: một học viên khác nhận bộ tài liệu, dựng lại môi trường thử từ mã, chạy pipeline, và xử lý một sự cố có sẵn trong sổ tay; mọi câu họ phải hỏi đều được ghi lại và là điểm trừ. Nguyên tắc viết: tài liệu phục vụ người chưa biết bối cảnh, nên mọi từ viết tắt và mọi quy ước phải được định nghĩa ở chỗ người đọc gặp chúng.",
"Nộp bộ tài liệu đủ để một người khác dựng lại và vận hành được nền tảng mà không phải hỏi.",
"Tầng *đánh giá*. Giai đoạn đo chất lượng tài liệu bằng kết quả của người khác chứ bằng độ dày. Kiểm bằng phép thử bàn giao; đạt khi người nhận dựng lại được và xử lý được sự cố với số câu hỏi dưới ngưỡng.",
"Viết đủ năm loại tài liệu. Đưa cho một học viên chưa từng xem dự án của bạn. Họ dựng lại môi trường thử, chạy pipeline, và xử lý một sự cố theo sổ tay. Ghi lại mọi câu họ phải hỏi. Sửa tài liệu theo danh sách đó rồi thử lại với người thứ hai.",
"Viết tài liệu cho chính mình đọc · bỏ hướng dẫn dựng lại từ đầu · sổ tay không có ngưỡng và không có người chịu trách nhiệm · bỏ phần hạn chế diễn giải.",
"Người nhận dựng lại và vận hành được với số câu hỏi dưới ngưỡng, và lần thử thứ hai có ít câu hỏi hơn lần đầu."),

(422,"Capstone defence","KT","Lesson 421",
"Buổi bảo vệ trước hội đồng, 120 phút. Không có nội dung mới.",
"Bảo vệ được toàn bộ nền tảng: thiết kế, số đo, vận hành, và xử lý được một sự cố hội đồng gây ra ngay trong buổi.",
"Tầng *đánh giá*. Bài kiểm cuối cùng, đo năng lực tổng hợp dưới chất vấn và dưới sự cố thật, nên hình thức là bảo vệ trực tiếp có can thiệp.",
"Bài chấm bảy phần: A (15đ) bối cảnh, phạm vi và ước lượng, có giả định · B (20đ) kiến trúc và các quyết định lớn, mỗi quyết định dẫn về một ràng buộc hoặc một số đo · C (15đ) chạy đầu cuối trên dữ liệu hội đồng đưa, đối soát khớp · D (25đ) **hội đồng gây một sự cố ngay trong buổi**: phát hiện qua cảnh báo, chẩn đoán, khắc phục, thông báo · E (10đ) chi phí và hai khoản cắt được · F (10đ) bàn giao: hội đồng hỏi một câu từ sổ tay và một câu từ hợp đồng dữ liệu · G (5đ) ba điều kiện làm thiết kế này sai.",
"Dồn thời gian vào phần xây và bỏ phần vận hành · trình bày công cụ thay vì quyết định · chưa từng diễn tập sự cố trước · không biết chi phí của chính hệ mình.",
"Đạt ≥ 75/100, phần D ≥ 60%, và phần C phải đối soát khớp. Nền tảng chạy đúng nhưng không phục hồi được ở phần D thì không đạt, dù các phần khác cao."),
]
