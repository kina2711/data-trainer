# -*- coding: utf-8 -*-
"""DE M1 + M2 — đặc tả bài. (n, title, type, prereq, learn, outcome, danhgia, lab, pitfalls, done)"""

M1 = ("Introduction to the Data Engineer Role and the Learning System", 1, 5, """| | |
|---|---|
| **Objective cấp module** | Vẽ được đường đi của một bản ghi từ hệ thống nguồn tới bảng điều khiển, và chỉ ra năm chỗ nó hỏng được cùng phép đo phát hiện từng chỗ |
| **Tiền đề** | Không |
| **Exit criterion** | Giải thích đường đi đó cho một người mới trong 5 phút, và trả lời được vì sao phải có chất lượng, quyền sở hữu, giám sát và bảo mật |
| **Kỹ năng SFIA** | `DTAN` mức 2 |
| **Chế độ hỏng** | Coi đây là module dẫn nhập rồi học lướt, nên tới chặng 4 không phát biểu được hợp đồng của một pipeline |""",
"Module không cài công cụ nào. Nó dựng bản đồ để 417 bài sau có chỗ neo, và dựng hệ thống ghi chép mà cả chương trình dựa vào. Bốn bài đầu đi từ ranh giới nghề tới cách học; bài cuối là cổng 0.")

L1 = [
(1,"What a Data Engineer does and where the boundary sits","LT","Module 1: Không",
"Sáu vai trò trong tổ chức dữ liệu và ranh giới trách nhiệm: Data Engineer, Analytics Engineer, Data Analyst, Data Scientist, Platform Engineer, Data Architect. Ba vùng chồng lấn hay gây tranh chấp phạm vi và cách các tổ chức thật chia chúng: ai sở hữu bảng thô, ai sở hữu bảng phục vụ, ai sở hữu định nghĩa chỉ số. Sản phẩm bàn giao của Data Engineer là một tập dữ liệu có hợp đồng, không phải một bảng điều khiển. Ba loại tổ chức tuyển Data Engineer và khác biệt về nội dung công việc: công ty sản phẩm có dữ liệu sự kiện lớn, doanh nghiệp truyền thống có nhiều hệ thống giao dịch cũ, và công ty dịch vụ làm dự án cho khách. Phân bổ thời gian thực tế của nghề theo bản nguồn: phần lớn thời gian nằm ở làm cho pipeline chạy đúng lại sau khi hỏng, không nằm ở viết pipeline mới.",
"Phân định trách nhiệm của sáu vai trò cho một danh sách nhiệm vụ cho trước, và định vị khoảng cách giữa năng lực hiện có của bản thân và ma trận năng lực ở mục 4.",
"Tầng *hiểu*. Bài mở chương trình, người học chưa có dữ liệu để thao tác, nên objective dừng ở phân định và giải thích. Kiểm bằng bài gán 18 nhiệm vụ cho sáu vai trò kèm một câu lý do mỗi nhiệm vụ; chấm theo bảng ranh giới ở phụ lục, đạt khi đúng ≥ 14/18 và lý do không mâu thuẫn với bảng.",
"Đọc 10 tin tuyển dụng Data Engineer đang mở tại Việt Nam trên ITViec hoặc TopDev. Lập bảng tần suất công nghệ: mỗi công nghệ xuất hiện trong bao nhiêu tin. Đối chiếu với bản đồ 40 module ở mục 9 và chỉ ra công nghệ nào chương trình không phủ, công nghệ nào chương trình phủ mà tin không nhắc.",
"Quy vai trò Data Engineer về viết pipeline · giả định thành thạo công cụ là điều kiện đủ · bỏ qua phần vận hành vì nó không có trong tiêu đề tin tuyển dụng.",
"Nộp bảng tần suất từ 10 tin có ghi nguồn và ngày truy cập, và bài gán nhiệm vụ đạt ≥ 14/18."),

(2,"The path of one record - source to dashboard","LT","Lesson 1",
"Bảy chặng của một bản ghi: sự kiện nghiệp vụ, hệ thống nguồn, thu thập, lưu trữ thô, biến đổi, lớp phục vụ, và ứng dụng tiêu thụ. Với mỗi chặng, cơ chế mất mát, cơ chế nhân bản, và cơ chế diễn giải sai đặc trưng của chặng đó. Phân biệt ba cặp khái niệm mà người mới hay gộp: ETL với ELT theo chỗ đặt phép biến đổi, theo lô với theo luồng theo đơn vị xử lý chứ không theo tốc độ, và hệ thống giao dịch với hệ thống phân tích theo mẫu truy cập. Ba lớp dữ liệu thường gặp và trách nhiệm của từng lớp: thô giữ nguyên như nguồn để tái tạo được, lớp giữa làm sạch và chuẩn hoá, lớp phục vụ hướng người dùng. Vì sao một con số trên bảng điều khiển là kết quả của một chuỗi quyết định thiết kế, không phải một quan sát trực tiếp.",
"Tái dựng đường đi bảy chặng từ trí nhớ và chỉ ra ít nhất một cơ chế sai lệch cụ thể tại mỗi chặng.",
"Tầng *hiểu*. Objective là tái dựng và giải thích cơ chế, chưa thao tác trên hệ thống nào. Kiểm bằng bài vẽ lại sơ đồ và điền cơ chế sai lệch; đạt khi đủ bảy chặng và ít nhất năm chặng có cơ chế đúng, chấm theo bảng đối chiếu.",
"Vẽ đường đi của một đơn hàng từ lúc khách bấm đặt tới lúc con số doanh thu hiện trên bảng điều khiển. Nêu 5 nơi dữ liệu có thể sai và với mỗi nơi, một phép đo phát hiện được nó. Đổi bài với một học viên khác và tìm chặng người kia bỏ sót.",
"Vẽ đường đi tuyến tính mà bỏ qua chỗ dữ liệu bị ghi lại nhiều lần · nhầm theo luồng với nhanh · cho rằng lớp thô là bản sao y hệt nguồn.",
"Sơ đồ đủ bảy chặng, ít nhất năm chặng có cơ chế sai lệch đúng, và 5 phép đo phát hiện đều thực hiện được."),

(3,"Declaring a use case - owner, grain, consumer, freshness","TH","Lesson 2",
"Chín thuộc tính phải khai báo trước khi xây bất cứ thứ gì: chủ dữ liệu, hệ thống nguồn, hạt dữ liệu, người tiêu thụ, độ tươi yêu cầu, mức đúng đắn yêu cầu, quyền truy cập, thời gian lưu giữ, và người chịu trách nhiệm khi hỏng. Hạt dữ liệu là thuộc tính chặn: phát biểu bằng một câu có dạng một dòng là một gì, và kiểm chứng bằng phép đếm. Phân biệt độ tươi với độ trễ và với tần suất chạy, ba thứ hay bị gộp. Mức đúng đắn phát biểu được bằng ngưỡng chứ không bằng tính từ: sai lệch cho phép là bao nhiêu phần trăm, đo bằng cách nào, đối chiếu với nguồn nào. Thủ tục từ chối một yêu cầu không trả lời được bằng dữ liệu hiện có, và vì sao từ chối sớm rẻ hơn xây rồi bỏ. Ba use case mẫu dùng xuyên suốt chương trình: đơn hàng, thanh toán, tồn kho.",
"Viết bản khai báo đủ chín thuộc tính cho một yêu cầu phát biểu mơ hồ, sao cho người thứ hai triển khai được không cần hỏi lại.",
"Tầng *áp dụng*. Sản phẩm là một tài liệu có tiêu chí kiểm được. Kiểm bằng rà soát chéo: một học viên khác đọc bản khai báo và viết ra hiểu biết của mình về hạt và người tiêu thụ; đạt khi hai bên khớp và không có câu hỏi làm rõ nào phát sinh.",
"Nhận ba yêu cầu phát biểu mơ hồ cho ba use case mẫu. Viết ba bản khai báo đủ chín thuộc tính. Đổi bài chéo, người nhận viết lại hạt và người tiêu thụ theo cách mình hiểu. Mọi chênh lệch phải sửa vào bản khai báo.",
"Phát biểu hạt bằng tên bảng thay vì bằng một câu · để mức đúng đắn ở dạng tính từ · bỏ trống người chịu trách nhiệm khi hỏng vì chưa có ai.",
"Ba bản khai báo đạt rà soát chéo, không phát sinh câu hỏi làm rõ nào."),

(4,"How to learn this - evidence, recall and a knowledge repo","TH","Lesson 3",
"Chương trình dài hơn hai năm, nên cách ghi chép quyết định phần lớn kết quả. Cấu trúc kho kiến thức sáu thư mục và việc của từng thư mục: khái niệm, lab, dự án, quyết định kiến trúc, sổ tay xử lý, và rà soát. Khuôn một ghi chú chín phần theo bản nguồn: định nghĩa, vấn đề nó giải, cơ chế bên trong, đường đi của một yêu cầu hoặc một bản ghi, lựa chọn và đánh đổi, lỗi thường gặp, cách quan sát, lab, câu hỏi kiểm tra. Bốn câu tự hỏi sau mỗi khái niệm: nó tồn tại để làm gì, nó sai theo cách nào, làm sao biết nó sai, khi nào dùng thứ khác. Ôn lại sau 1, 7 và 30 ngày. Thang sáu mức theo dõi năng lực: chưa học, giải thích được, làm theo hướng dẫn, tự làm, xử lý ca lạ, áp dụng thực tế. Nguyên tắc không suy ra mức thành thạo từ việc đã đọc: mỗi mức phải có bằng chứng kèm ngày. Cảnh báo từ bản nguồn: không tạo 150 kho rỗng.",
"Dựng kho kiến thức sáu thư mục và viết một ghi chú chín phần hoàn chỉnh cho một khái niệm đã học ở lesson 2 hoặc 3.",
"Tầng *áp dụng*. Objective là một sản phẩm có khuôn kiểm được. Kiểm bằng rà soát: ghi chú phải đủ chín phần, phần đường đi phải có một ví dụ cụ thể, và phần lab phải chạy lại được bởi người khác. Ghi chú đủ chín tiêu đề nhưng phần cơ chế chỉ chép lại định nghĩa thì không đạt.",
"Dựng kho kiến thức sáu thư mục có quản lý phiên bản. Viết một ghi chú chín phần cho khái niệm hạt dữ liệu hoặc đường đi bảy chặng. Lập bảng theo dõi năng lực sáu mức cho 40 module, đánh dấu mức hiện tại và để trống cột bằng chứng.",
"Tạo cấu trúc thư mục rỗng rồi không viết gì · chép định nghĩa vào phần cơ chế · đánh dấu đã hiểu mà không có bằng chứng kèm ngày.",
"Kho có đủ sáu thư mục, một ghi chú chín phần đạt rà soát, và bảng theo dõi năng lực có cột bằng chứng."),

(5,"Gate 0 - explain the data path and defend the four disciplines","KT","Lesson 4",
"Không có nội dung mới. Cổng 0 của chương trình.",
"Giải thích đường đi của dữ liệu cho một người không làm kỹ thuật trong 5 phút, và bảo vệ được vì sao cần chất lượng, quyền sở hữu, giám sát và bảo mật, bằng hậu quả cụ thể chứ bằng nguyên tắc chung.",
"Tầng *đánh giá*. Cổng đo năng lực giải thích và bảo vệ, không đo trí nhớ, nên không kiểm bằng đề trắc nghiệm. Thang điểm: A 25đ đường đi bảy chặng · B 20đ năm chỗ hỏng và phép đo · C 20đ bốn kỷ luật, mỗi kỷ luật một hậu quả cụ thể khi thiếu · D 15đ bản khai báo use case · E 20đ trả lời chất vấn. Đạt khi ≥ 70/100 và phần E ≥ 50%.",
"Trình bày 5 phút cho một người đóng vai quản lý không làm kỹ thuật, hỏi đáp 10 phút. Người nghe được phép hỏi vì sao không làm đơn giản hơn ở bất kỳ chặng nào.",
"Dùng thuật ngữ mà người nghe không có · bảo vệ bốn kỷ luật bằng nguyên tắc chung thay vì bằng hậu quả · không trả lời được câu vì sao không làm đơn giản hơn.",
"Đạt ≥ 70/100 và phần E ≥ 50%."),
]

M2 = ("Computers - CPU, Memory, Storage and the Cost of a Computation", 6, 17, """| | |
|---|---|
| **Objective cấp module** | Ước lượng bậc độ lớn thời gian của một thao tác dữ liệu trước khi chạy, rồi đo và giải thích chênh lệch bằng cơ chế phần cứng |
| **Tiền đề** | M1 |
| **Exit criterion** | Tự giải thích vì sao một phép kết có thể tràn ra đĩa, vì sao nhiều chỉ mục làm ghi chậm, và vì sao thêm RAM không cứu được một truy vấn tệ |
| **Kỹ năng SFIA** | `HPCC` mức 2 · `SYSP` mức 2 |
| **Chế độ hỏng** | Học thuộc tên các tầng bộ nhớ đệm mà không bao giờ đo, nên tới chặng 7 không chẩn đoán được nút cổ chai của một công việc Spark |""",
"Module đo là chính. Mọi khẳng định về hiệu năng trong 12 bài đều phải kiểm bằng một phép đo chạy trên máy người học. Bốn bài đầu về biểu diễn dữ liệu là nơi sinh ra lỗi âm thầm; ba bài giữa về bộ xử lý; năm bài cuối về bộ nhớ, đĩa và phép đo.")

L2 = [
(6,"Bits, bytes, integers and the overflow that does not announce itself","LT","Module 2: M1",
"Nhị phân và thập lục phân, bit và byte, và cách đọc một dãy byte thô. Số nguyên có dấu và không dấu, biểu diễn bù hai, và dải giá trị của từng độ rộng. Tràn số: cơ chế một phép cộng cho ra số âm, và vì sao phần lớn ngôn ngữ không báo lỗi khi việc đó xảy ra. Ba chỗ tràn số gặp thật trong công việc dữ liệu: khoá tự tăng 32 bit chạm trần, tổng luỹ kế theo giây trong bảng số nguyên, và dấu thời gian Unix 32 bit. Chuyển kiểu thu hẹp và mất dữ liệu âm thầm khi ép từ 64 bit xuống 32 bit. Đọc kích thước dữ liệu theo bậc: một triệu dòng nhân một trăm byte là bao nhiêu, và vì sao ước lượng bậc độ lớn quan trọng hơn con số chính xác khi quyết định kiến trúc.",
"Ước lượng kích thước một tập dữ liệu từ số dòng và lược đồ, và định vị chỗ tràn số trong ba đoạn mã cho trước.",
"Tầng *áp dụng*. Objective gồm một phép ước lượng và một phép định vị lỗi, cả hai kiểm được bằng đáp án. Kiểm bằng bài ước lượng ba tập dữ liệu, đạt khi sai trong phạm vi một bậc độ lớn, cộng bài định vị tràn số đúng cả ba đoạn.",
"Viết chương trình gây tràn số nguyên 32 bit rồi quan sát kết quả. Ước lượng kích thước ba tập dữ liệu từ lược đồ, sau đó sinh dữ liệu thật và đo, so với ước lượng. Đọc ba đoạn mã và chỉ dòng nào tràn được cùng điều kiện gây tràn.",
"Giả định số nguyên luôn đủ rộng · ước lượng bằng cách nhân số dòng với số cột mà quên độ rộng kiểu · coi cảnh báo ép kiểu là nhiễu.",
"Ba ước lượng đều sai trong phạm vi một bậc độ lớn, và định vị đúng chỗ tràn ở cả ba đoạn mã."),

(7,"Floating point, decimal, and why money is never a float","TH","Lesson 6",
"Biểu diễn dấu phẩy động theo chuẩn IEEE 754: dấu, số mũ, phần định trị. Vì sao 0,1 cộng 0,2 không bằng 0,3, và vì sao đây không phải lỗi của ngôn ngữ mà là hệ quả của biểu diễn nhị phân. Sai số tích luỹ khi cộng một triệu giá trị nhỏ, và cơ chế khiến thứ tự cộng đổi thì kết quả đổi, nên phép tổng trên hệ phân tán không tất định nếu dùng dấu phẩy động. Kiểu thập phân có độ chính xác xác định và chi phí của nó. Quy tắc cho tiền: lưu bằng số nguyên đơn vị nhỏ nhất hoặc bằng kiểu thập phân có khai báo độ chính xác, không bao giờ bằng dấu phẩy động. So sánh hai số thực bằng ngưỡng sai số thay vì bằng dấu bằng. Ba chỗ sai số lọt vào báo cáo tài chính: tổng theo nhóm, tỉ lệ phần trăm, và làm tròn trước khi cộng thay vì sau khi cộng.",
"Chứng minh bằng thực nghiệm rằng một phép tổng dấu phẩy động cho kết quả khác nhau theo thứ tự cộng, và sửa nó bằng kiểu thập phân.",
"Tầng *áp dụng*. Objective có tiêu chí đúng sai tuyệt đối, kiểm bằng chạy thật. Đạt khi bản thực nghiệm cho ra hai kết quả khác nhau trên cùng tập số, và bản sửa bằng kiểu thập phân cho cùng một kết quả ở mọi thứ tự cộng. Giải thích đúng mà không chạy được thì chưa đạt.",
"Sinh một triệu giá trị tiền nhỏ. Cộng theo thứ tự tăng dần, giảm dần và ngẫu nhiên bằng dấu phẩy động, ghi ba kết quả. Đổi sang kiểu thập phân, lặp lại, xác nhận ba kết quả bằng nhau. Đo chênh lệch thời gian chạy giữa hai kiểu.",
"Dùng dấu phẩy động cho tiền vì nó nhanh hơn · so sánh hai số thực bằng dấu bằng · làm tròn từng dòng trước khi cộng.",
"Ba thứ tự cộng cho ba kết quả khác nhau ở dấu phẩy động và một kết quả duy nhất ở kiểu thập phân, có số đo thời gian kèm theo."),

(8,"Text encoding, UTF-8 and endianness","TH","Lesson 6",
"Bảng mã và điểm mã: khác biệt giữa ký tự, điểm mã và byte. UTF-8 là mã hoá độ dài thay đổi: một ký tự tiếng Việt có dấu chiếm nhiều byte hơn một ký tự ASCII, nên độ dài chuỗi tính theo ký tự khác độ dài tính theo byte, và cắt chuỗi theo byte làm hỏng ký tự. Chuẩn hoá Unicode và vì sao hai chuỗi trông giống hệt nhau lại không bằng nhau: cùng một chữ có dấu biểu diễn được bằng một điểm mã hoặc bằng hai điểm mã ghép. Hậu quả trực tiếp cho công việc dữ liệu: khoá kết không khớp, phép đếm giá trị phân biệt ra sai số. Ký tự đầu tệp đánh dấu thứ tự byte và cách nó làm hỏng cột đầu tiên khi đọc CSV. Thứ tự byte lớn nhỏ và chỗ nó xuất hiện: định dạng tệp nhị phân và giao thức mạng. Phát hiện bảng mã của một tệp lạ và vì sao việc đó chỉ là phỏng đoán.",
"Định vị nguyên nhân khi hai chuỗi tiếng Việt trông giống nhau nhưng không khớp khi kết, và sửa bằng chuẩn hoá Unicode.",
"Tầng *phân tích*. Objective là truy nguyên một lỗi có nhiều nguyên nhân khả dĩ, không phải làm theo hướng dẫn. Kiểm bằng ba tệp mỗi tệp hỏng vì một nguyên nhân khác nhau: bảng mã sai, chuẩn hoá khác nhau, ký tự đánh dấu đầu tệp. Đạt khi định vị đúng cả ba và dẫn được bằng chứng ở mức byte.",
"Nhận ba tệp CSV tiếng Việt hỏng theo ba cách. Với mỗi tệp, xem nội dung ở mức byte, định vị nguyên nhân, sửa, và chứng minh phép kết khớp sau khi sửa. Đo số cặp khớp thêm sau chuẩn hoá.",
"Đếm độ dài chuỗi bằng byte rồi cắt giữa ký tự · giả định mọi tệp là UTF-8 · bỏ qua ký tự đánh dấu đầu tệp rồi tên cột đầu có ký tự lạ.",
"Định vị đúng nguyên nhân cả ba tệp với bằng chứng ở mức byte, và phép kết khớp sau khi sửa."),

(9,"Dates, times and timezones as a source of silent error","TH","Lesson 6",
"Dấu thời gian Unix, múi giờ, và độ lệch múi giờ không phải là múi giờ. Giờ mùa hè tạo ra hai bất thường mỗi năm: một giờ không tồn tại và một giờ xuất hiện hai lần, nên dấu thời gian cục bộ không phải khoá duy nhất. Quy tắc vận hành: lưu bằng UTC, chuyển sang giờ địa phương ở tầng hiển thị, và luôn ghi rõ múi giờ trong lược đồ. Bốn chỗ lệch múi giờ lọt vào báo cáo: ranh giới ngày khác nhau giữa hai hệ thống, phép gộp theo ngày trên dữ liệu UTC cho một tổ chức ở múi giờ khác, phép so cùng kỳ năm trước khi năm nhuận, và tuần ISO khác tuần lịch thường. Định dạng ngày mơ hồ giữa kiểu ngày trước tháng và tháng trước ngày: cơ chế sai không phát tín hiệu, nên tồn tại được qua nhiều kỳ báo cáo. Độ phân giải dấu thời gian và mất mát khi ép từ micro giây xuống giây. Đặc thù Việt Nam: Tết âm lịch dịch chuyển giữa tháng dương lịch làm phép so cùng kỳ lệch.",
"Chuyển một cột ngày trộn nhiều định dạng và nhiều múi giờ về một chuẩn thống nhất, và chứng minh không bản ghi nào bị hoán đổi ngày với tháng.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm chứng được bằng đối chứng. Đạt khi bảng sau chuẩn hoá khớp từng dòng với bảng đối chứng, và khi người học chỉ ra được số bản ghi từng mơ hồ cùng cách phân giải. Không kiểm bằng câu hỏi vì lỗi này chỉ lộ ra trên dữ liệu thật.",
"Nhận một tệp có cột ngày trộn ba định dạng và hai múi giờ, trong đó 40 bản ghi rơi vào vùng mơ hồ ngày tháng. Chuẩn hoá về UTC. Đếm và phân giải từng bản ghi mơ hồ có nêu căn cứ. So với bảng đối chứng.",
"Ép kiểu ngày bằng thư viện tự đoán định dạng rồi tin kết quả · lưu giờ địa phương không kèm múi giờ · gộp theo ngày trên dữ liệu UTC cho tổ chức ở múi giờ khác.",
"Bảng sau chuẩn hoá khớp từng dòng với đối chứng, và 40 bản ghi mơ hồ đều có căn cứ phân giải."),

(10,"The CPU instruction cycle, registers and pipelines","LT","Lesson 6",
"Chu kỳ lệnh: nạp, giải mã, thực thi, ghi lại. Thanh ghi là mức lưu trữ nhanh nhất và ít nhất. Đường ống lệnh cho phép nhiều lệnh ở các chặng khác nhau cùng lúc, và điều kiện đường ống bị xả. Dự đoán nhánh: cơ chế, và vì sao một vòng lặp có nhánh khó đoán chạy chậm hơn hẳn vòng lặp có nhánh dễ đoán trên cùng số phép tính. Tập lệnh đơn dòng nhiều dữ liệu và lý do các công cụ phân tích hiện đại cố sắp dữ liệu sao cho dùng được nó, đây là một phần lý do lưu trữ theo cột thắng cho tải phân tích. Xung nhịp và số lệnh mỗi chu kỳ, và vì sao so sánh xung nhịp giữa hai bộ xử lý khác kiến trúc là vô nghĩa. Thang bậc độ lớn cần thuộc: một lệnh, một lần truy cập bộ nhớ đệm cấp một, một lần truy cập bộ nhớ chính, một lần đọc đĩa thể rắn, một lần đi mạng trong trung tâm dữ liệu.",
"Sắp xếp năm thao tác theo bậc độ lớn thời gian và dùng thang đó để ước lượng thời gian một vòng lặp trước khi chạy.",
"Tầng *hiểu*. Bài lý thuyết, chưa có công cụ đo sâu, nên objective dừng ở chỗ dùng được thang bậc. Kiểm bằng bài sắp xếp và bài ước lượng; đạt khi sắp đúng thứ tự năm thao tác và ước lượng vòng lặp sai trong phạm vi một bậc so với số đo thật.",
"Học thuộc thang bậc độ lớn năm mức. Viết hai vòng lặp cùng số phép tính, một có nhánh dễ đoán một có nhánh khó đoán, ước lượng trước rồi đo. Giải thích chênh lệch bằng dự đoán nhánh.",
"So sánh hai bộ xử lý bằng xung nhịp · cho rằng số phép tính bằng nhau thì thời gian bằng nhau · bỏ qua chi phí nạp dữ liệu khi đếm phép tính.",
"Sắp đúng thứ tự năm thao tác, và ước lượng vòng lặp sai trong phạm vi một bậc so với số đo."),

(11,"Cache hierarchy, cache lines and locality","TH","Lesson 10",
"Ba cấp bộ nhớ đệm và tỉ lệ dung lượng với độ trễ giữa chúng. Dòng bộ nhớ đệm là đơn vị nạp: đọc một byte thì nạp cả dòng, nên truy cập tuần tự rẻ hơn truy cập ngẫu nhiên rất nhiều dù cùng số byte. Cục bộ theo không gian và cục bộ theo thời gian. Hệ quả trực tiếp cho công việc dữ liệu: duyệt mảng theo thứ tự lưu nhanh hơn duyệt ngược thứ tự, và đây là một phần lý do lưu trữ theo cột nhanh hơn lưu trữ theo dòng cho phép gộp trên một cột. Chia sẻ giả: hai luồng ghi vào hai biến khác nhau nằm cùng một dòng bộ nhớ đệm làm chậm nhau, một lỗi hiệu năng không nhìn thấy trong mã. Đo tỉ lệ trượt bộ nhớ đệm bằng công cụ đếm sự kiện phần cứng. Vì sao cấu trúc dữ liệu liên kết bằng con trỏ chậm hơn mảng dù cùng độ phức tạp tiệm cận.",
"Đo chênh lệch thời gian giữa duyệt tuần tự và duyệt ngẫu nhiên trên cùng lượng dữ liệu, và giải thích chênh lệch bằng dòng bộ nhớ đệm.",
"Tầng *phân tích*. Objective đòi giải thích một số đo bằng cơ chế, không chỉ tạo ra số đo. Kiểm bằng báo cáo: phải có số đo cho ít nhất ba kích thước dữ liệu bắc qua ranh giới bộ nhớ đệm, và phải chỉ ra chỗ đường cong thời gian gãy cùng lý do. Có số mà không giải thích được chỗ gãy thì chưa đạt.",
"Viết chương trình duyệt mảng theo ba cách: tuần tự, nhảy bước bằng kích thước dòng bộ nhớ đệm, và ngẫu nhiên. Chạy ở năm kích thước dữ liệu từ nhỏ hơn bộ nhớ đệm cấp một tới lớn hơn cấp ba. Vẽ đường cong thời gian và chỉ chỗ gãy.",
"Đo một kích thước dữ liệu rồi kết luận chung · quên làm nóng bộ nhớ đệm trước khi đo · so sánh hai chương trình khác nhau về số phép tính rồi quy hết cho bộ nhớ đệm.",
"Có số đo ở năm kích thước, đường cong có chỗ gãy rõ, và chỗ gãy giải thích được bằng ranh giới cấp bộ nhớ đệm."),

(12,"Core against thread, context switch and the cost of switching","LT","Lesson 10",
"Lõi vật lý, luồng phần cứng và luồng phần mềm là ba thứ khác nhau và thường bị gộp làm một. Đa luồng đồng thời cho phép một lõi chạy hai luồng phần cứng, và vì sao nó tăng thông lượng cho tải chờ bộ nhớ nhưng không tăng cho tải tính toán thuần. Bộ lập lịch của hệ điều hành và lát thời gian. Chuyển ngữ cảnh: những gì phải lưu và khôi phục, chi phí trực tiếp và chi phí gián tiếp do bộ nhớ đệm bị làm nguội. Hệ quả vận hành: số luồng lớn hơn số lõi rất nhiều làm giảm thông lượng chứ không tăng, và đây là lỗi cấu hình phổ biến của tiến trình thực thi trong công cụ điều phối. Tải nghẽn tính toán so với tải nghẽn vào ra, cách phân biệt bằng số đo, và vì sao hai loại này cần số luồng khác nhau. Mối liên hệ tới chặng sau: số phân vùng trong Spark và số tiến trình thực thi trong công cụ điều phối đều là cùng một bài toán.",
"Phân loại một tải là nghẽn tính toán hay nghẽn vào ra bằng số đo, và chọn số luồng phù hợp với loại tải đó.",
"Tầng *phân tích*. Objective là phân loại có bằng chứng rồi suy ra quyết định cấu hình. Kiểm bằng hai tải dựng sẵn, một loại mỗi tải; đạt khi phân loại đúng cả hai, dẫn được số đo làm bằng chứng, và số luồng chọn ra cho thông lượng cao nhất trong bảng thực nghiệm của chính mình.",
"Dựng hai tải: một tính toán thuần, một đọc tệp nhiều. Chạy mỗi tải ở 1, 2, 4, 8, 16, 64 luồng. Đo thông lượng và mức dùng bộ xử lý. Vẽ hai đường cong, chỉ điểm cực đại của từng cái và giải thích vì sao hai điểm khác nhau.",
"Đặt số luồng bằng số lõi cho mọi loại tải · tăng số luồng tới khi máy đứng rồi kết luận máy yếu · đo thông lượng mà không đo mức dùng bộ xử lý.",
"Phân loại đúng cả hai tải có số đo kèm theo, và hai đường cong có điểm cực đại khác nhau được giải thích."),

(13,"RAM - latency, bandwidth, heap and stack","LT","Lesson 11",
"Độ trễ và băng thông là hai đại lượng khác nhau và tối ưu cho cái này thường đánh đổi cái kia. Ngăn xếp và vùng nhớ động: cách cấp phát, cách thu hồi, và vì sao cấp phát trên ngăn xếp gần như miễn phí còn trên vùng nhớ động thì không. Phân mảnh vùng nhớ động và cơ chế khiến một tiến trình còn nhiều bộ nhớ trống vẫn không cấp phát được khối lớn. Thu gom rác và tạm dừng do nó gây ra, cùng lý do một công việc xử lý dữ liệu lớn trong ngôn ngữ có thu gom rác có thể đứng vài giây không rõ nguyên nhân. Chi phí bộ nhớ thật của một cấu trúc dữ liệu so với kích thước dữ liệu thuần: phần đầu của đối tượng, con trỏ, và hệ số phình của từ điển băm. Ước lượng bộ nhớ cần cho một bảng trong bộ nhớ từ số dòng và lược đồ, và vì sao ước lượng đó luôn phải nhân hệ số an toàn.",
"Ước lượng bộ nhớ cần cho một bảng trong bộ nhớ từ lược đồ, rồi đo thật và giải thích hệ số phình.",
"Tầng *áp dụng*. Objective gồm ước lượng và đối chiếu với số đo. Kiểm bằng ba cấu trúc dữ liệu khác nhau chứa cùng dữ liệu; đạt khi ước lượng sai trong phạm vi hệ số hai và khi người học chỉ ra được nguồn gốc phần phình cho ít nhất hai trong ba cấu trúc.",
"Nạp cùng một triệu bản ghi vào ba cấu trúc: danh sách các từ điển, mảng theo cột, và khung dữ liệu. Ước lượng trước, đo bộ nhớ thật sau. Giải thích chênh lệch. Gây phân mảnh bằng cách cấp phát rồi giải phóng xen kẽ, quan sát.",
"Ước lượng bằng số byte dữ liệu thuần · bỏ qua phần đầu của đối tượng trong ngôn ngữ động · coi bộ nhớ trống theo báo cáo hệ điều hành là bộ nhớ cấp phát được.",
"Ba ước lượng sai trong phạm vi hệ số hai, và nguồn gốc phần phình giải thích được cho ít nhất hai cấu trúc."),

(14,"Virtual memory, paging, page faults, swap and OOM","TH","Lesson 13",
"Bộ nhớ ảo tách địa chỉ chương trình nhìn thấy khỏi địa chỉ vật lý. Trang, bảng trang và bộ đệm tra cứu địa chỉ. Lỗi trang nhẹ và lỗi trang nặng: cái đầu rẻ, cái sau phải đọc đĩa nên đắt gấp nhiều bậc. Vùng hoán đổi: khi nào hệ điều hành dùng nó, và vì sao một tiến trình rơi vào hoán đổi thì thà chết còn hơn chạy tiếp, bởi thông lượng sụt xuống mức không dùng được. Cơ chế giết tiến trình khi cạn bộ nhớ: tiến trình nào bị chọn và vì sao nó thường không phải tiến trình gây ra vấn đề. Đọc dấu vết trong nhật ký hệ thống để xác nhận một tiến trình bị giết vì cạn bộ nhớ chứ không phải vì lỗi mã. Giới hạn bộ nhớ theo nhóm tiến trình và mối liên hệ tới giới hạn tài nguyên của vùng chứa ở chặng 7. Ánh xạ tệp vào bộ nhớ và khi nào nó có lợi.",
"Phân biệt một tiến trình bị giết vì cạn bộ nhớ với một tiến trình chết vì lỗi mã, bằng bằng chứng trong nhật ký hệ thống.",
"Tầng *phân tích*. Objective là chẩn đoán phân biệt hai nguyên nhân giống nhau ở bề mặt. Kiểm bằng ba ca dựng sẵn: một cạn bộ nhớ, một lỗi mã, một rơi vào hoán đổi và chậm chứ chưa chết. Đạt khi phân loại đúng cả ba và dẫn được dòng nhật ký hoặc số đo cho từng ca.",
"Dựng ba ca trong máy ảo có giới hạn bộ nhớ. Ca một cấp phát tới khi bị giết. Ca hai lỗi mã. Ca ba nạp tập dữ liệu lớn hơn bộ nhớ và quan sát hoán đổi. Với mỗi ca, thu nhật ký hệ thống và số đo lỗi trang nặng.",
"Kết luận hết bộ nhớ chỉ vì tiến trình chết · bỏ qua trạng thái hoán đổi rồi tưởng máy chậm do bộ xử lý · tăng bộ nhớ mà không xem tiến trình nào thật sự chiếm.",
"Phân loại đúng cả ba ca với dòng nhật ký hoặc số đo lỗi trang nặng làm bằng chứng."),

(15,"Disks - HDD, SSD, NVMe and the sequential against random gap","TH","Lesson 13",
"Đĩa từ có bộ phận cơ nên thời gian tìm kiếm chi phối, còn ổ thể rắn không có nên khoảng cách giữa đọc tuần tự và đọc ngẫu nhiên hẹp lại nhưng không biến mất. Ba đại lượng và quan hệ giữa chúng: số thao tác vào ra mỗi giây, thông lượng, và độ trễ. Vì sao tối ưu một đại lượng thường làm xấu đại lượng khác. Độ sâu hàng đợi và cơ chế ổ thể rắn chỉ đạt thông lượng công bố khi có đủ yêu cầu song song. Kích thước khối và chi phí của việc đọc một dòng nhỏ trong một khối lớn. Hệ quả trực tiếp cho công việc dữ liệu: vấn đề nhiều tệp nhỏ, và vì sao đọc một nghìn tệp một mê ga byte chậm hơn nhiều so với đọc một tệp một ghi ga byte dù cùng tổng dung lượng. Ba loại lưu trữ và mẫu truy cập của từng loại: lưu trữ khối, lưu trữ tệp, lưu trữ đối tượng. Độ trễ của lưu trữ đối tượng so với đĩa cục bộ và hệ quả lên thiết kế ở chặng 7.",
"Đo khoảng cách giữa đọc tuần tự và đọc ngẫu nhiên trên máy của mình, và ước lượng thời gian đọc một tập dữ liệu chia thành nhiều tệp nhỏ trước khi chạy.",
"Tầng *áp dụng*. Objective gồm một phép đo và một phép ước lượng dùng kết quả đo. Kiểm bằng bài dự đoán rồi đối chứng: đạt khi ước lượng thời gian đọc một nghìn tệp nhỏ sai trong phạm vi hệ số hai so với số đo thật.",
"Đo đọc tuần tự và đọc ngẫu nhiên ở bốn độ sâu hàng đợi. Chia một tập dữ liệu một ghi ga byte thành một tệp, một trăm tệp, và mười nghìn tệp. Ước lượng thời gian đọc từng cách trước khi chạy, rồi đo.",
"Đo mà không vô hiệu hoá bộ đệm trang nên đo lại tốc độ bộ nhớ · so sánh số thao tác vào ra mỗi giây giữa hai ổ mà bỏ qua độ sâu hàng đợi · chia nhỏ tệp để chạy song song mà không tính chi phí mở tệp.",
"Có số đo ở bốn độ sâu hàng đợi, và ước lượng thời gian đọc mười nghìn tệp nhỏ sai trong phạm vi hệ số hai."),

(16,"Durability - fsync, write amplification and filesystems","TH","Lesson 15",
"Ghi thành công không có nghĩa dữ liệu đã nằm trên đĩa. Chuỗi bộ đệm giữa lời gọi ghi và mặt đĩa: bộ đệm của ứng dụng, bộ đệm trang của hệ điều hành, bộ đệm của thiết bị. Lời gọi đồng bộ hoá ép xuống tới đâu, chi phí của nó, và vì sao một cơ sở dữ liệu gọi nó ở mỗi lần xác nhận giao dịch. Mất dữ liệu khi mất điện ở từng mức bộ đệm. Khuếch đại ghi: ghi một byte làm thiết bị ghi nhiều hơn một byte, cơ chế ở ổ thể rắn do xoá theo khối, và cơ chế ở cơ sở dữ liệu do nhật ký ghi trước cộng với ghi dữ liệu. Hệ quả: nhiều chỉ mục làm mỗi lần chèn tốn nhiều lần ghi hơn, đây là vế thứ hai của tiêu chí ra module. Hệ tệp và nhật ký của nó. Ghi nguyên tử bằng ghi tệp tạm rồi đổi tên, mẫu dùng lại suốt chương trình. Không gian đĩa đầy và bốn triệu chứng nó gây ra ở tầng ứng dụng.",
"Chứng minh bằng thực nghiệm chi phí của lời gọi đồng bộ hoá, và cài đặt ghi nguyên tử bằng mẫu ghi tệp tạm rồi đổi tên.",
"Tầng *áp dụng*. Objective gồm một số đo và một sản phẩm mã. Đạt khi bảng số đo cho thấy chênh lệch thông lượng giữa có và không có đồng bộ hoá, và khi cài đặt ghi nguyên tử sống sót qua thực nghiệm giết tiến trình giữa chừng mà không để lại tệp dở.",
"Ghi một trăm nghìn bản ghi theo ba chế độ: không đồng bộ, đồng bộ mỗi bản ghi, đồng bộ mỗi một nghìn bản ghi. Đo thông lượng. Cài đặt ghi nguyên tử bằng tệp tạm và đổi tên, rồi giết tiến trình giữa chừng 10 lần và xác nhận không lần nào để lại tệp dở.",
"Tin rằng ghi xong là an toàn · gọi đồng bộ hoá mỗi bản ghi rồi kết luận đĩa chậm · ghi đè trực tiếp lên tệp đích nên mất cả bản cũ khi hỏng giữa chừng.",
"Bảng ba chế độ có số thông lượng, và 10 lần giết tiến trình không để lại tệp dở nào."),

(17,"Measuring - benchmark a computation and locate the bottleneck","TH","Lesson 16",
"Phép đo sai còn tệ hơn không đo, vì nó cho kết luận sai mà có vẻ có căn cứ. Sáu nguồn nhiễu phải kiểm soát: bộ đệm nóng hay nguội, tải nền, điều chỉnh xung nhịp theo nhiệt, thời gian khởi động của môi trường chạy, biến thiên giữa các lần chạy, và kích thước dữ liệu không đại diện. Đo nhiều lần và báo trung vị cùng phân vị 95, không báo trung bình, vì phân bố thời gian chạy lệch phải. Bốn số đo tối thiểu cho mọi phép đo hiệu năng: thời gian, mức dùng bộ xử lý, bộ nhớ đỉnh, và lượng vào ra. Quy trình định vị nút cổ chai theo bốn bước: đo bốn số trên, tìm tài nguyên bão hoà, đổi một biến duy nhất, đo lại. Vì sao đổi hai biến cùng lúc làm phép đo mất giá trị. Ghi lại phép đo sao cho lặp lại được: lệnh chạy, dữ liệu, phần cứng, phiên bản, và kết quả thô.",
"Thiết kế và chạy một phép đo có kiểm soát nhiễu cho một thao tác dữ liệu, rồi định vị tài nguyên bão hoà bằng bốn số đo.",
"Tầng *đánh giá*. Objective đòi thiết kế một phép đo và biện minh các lựa chọn kiểm soát nhiễu, không có một đáp án duy nhất. Kiểm bằng rà soát chéo: một học viên khác chạy lại theo tài liệu và phải ra kết quả trong phạm vi sai số mà người thiết kế công bố. Chạy lại không ra thì phép đo chưa đủ tài liệu.",
"Thiết kế phép đo cho một thao tác gộp trên năm triệu dòng. Kiểm soát đủ sáu nguồn nhiễu, nêu rõ cách kiểm soát từng nguồn. Chạy 10 lần, báo trung vị và phân vị 95 cùng bốn số đo. Đưa tài liệu cho người khác chạy lại.",
"Báo trung bình thay vì trung vị · chạy một lần rồi kết luận · đổi cả kích thước dữ liệu lẫn số luồng trong cùng một lần thử.",
"Người khác chạy lại theo tài liệu ra kết quả trong phạm vi sai số đã công bố, và tài nguyên bão hoà được chỉ ra có bằng chứng."),
]
