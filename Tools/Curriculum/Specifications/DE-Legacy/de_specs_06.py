# -*- coding: utf-8 -*-
"""DE M8 — Software engineering: Git, testing, packaging, APIs."""

M8 = ("Software Engineering - Git, Testing, Packaging", 78, 91, """| | |
|---|---|
| **Objective cấp module** | Giao một kho mã mà người khác sao về, chạy một lệnh dựng môi trường, và tái hiện đúng kết quả của mình |
| **Tiền đề** | M7 |
| **Exit criterion** | Đạt Cổng 3 ≥ 70/100: người khác sao kho, chạy một lệnh, CI xanh, và dữ liệu sau hai lần chạy bằng sau một lần |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 · `CFMG` mức 3 |
| **Chế độ hỏng** | Viết kiểm thử giả lập mọi thứ nên bộ kiểm thử xanh trong khi pipeline thật ghi sai vào cơ sở dữ liệu |""",
"Module biến mã chạy được thành mã giao được. Bốn bài đầu về Git và kho mã, hai bài giữa về môi trường và công cụ tĩnh, năm bài về kiểm thử ở bốn tầng, hai bài về phát hành và tài liệu, bài cuối là cổng 3. Nguyên tắc xuyên suốt: không giả lập thứ có thể chạy thật, vì giả lập cơ sở dữ liệu là cách chắc chắn nhất để bỏ sót lỗi cơ sở dữ liệu.")

L8 = [
(78,"Git internals - objects, commits and what a branch really is","LT","Module 8: M7",
"Bốn loại đối tượng và quan hệ giữa chúng: khối dữ liệu giữ nội dung tệp, cây giữ cấu trúc thư mục, lần nộp giữ một cây cộng con trỏ tới lần nộp cha, và thẻ. Mọi đối tượng được đặt tên bằng băm nội dung, nên nội dung giống nhau thì chỉ lưu một lần và lịch sử không sửa được mà không đổi mọi băm sau đó. Nhánh chỉ là một con trỏ tới một lần nộp, không phải một bản sao thư mục, và hiểu điều này làm phần lớn thao tác Git hết bí ẩn. Con trỏ đầu và trạng thái đầu rời. Ba vùng: thư mục làm việc, vùng chờ, kho. Vì sao dữ liệu đã nộp vẫn nằm trong lịch sử sau khi xoá tệp, nối thẳng tới bí mật ở lesson 75 và tới lý do phải quét toàn bộ lịch sử chứ không chỉ trạng thái hiện tại. Kích thước kho phình vì nộp tệp dữ liệu lớn, và vì sao không sửa được bằng cách xoá tệp. Danh sách bỏ qua và tệp lớn nên để ngoài.",
"Giải thích vì sao xoá một tệp bí mật rồi nộp lại không làm nó biến mất, và chứng minh bằng cách lấy lại nội dung đó từ lịch sử.",
"Tầng *hiểu*. Objective là giải thích cơ chế và chứng minh hệ quả của nó, không phải thao tác Git nâng cao. Kiểm bằng thực nghiệm: đạt khi lấy lại được nội dung tệp đã xoá từ lịch sử và chỉ ra được đối tượng nào còn giữ nó.",
"Tạo kho mới, nộp một tệp chứa chuỗi bí mật, xoá tệp, nộp lại. Lấy lại nội dung bí mật từ lịch sử. Liệt kê các đối tượng và chỉ ra khối dữ liệu giữ nội dung đó. Nộp một tệp 200 mê ga byte, xoá, đo kích thước kho trước và sau.",
"Tin rằng xoá tệp là xoá khỏi lịch sử · nộp tệp dữ liệu lớn vào kho mã · coi nhánh là một bản sao thư mục.",
"Lấy lại được nội dung bí mật từ lịch sử và chỉ đúng đối tượng giữ nó, kèm số đo kích thước kho trước sau."),

(79,"Branching, merging, rebasing and resolving conflicts","TH","Lesson 78",
"Gộp tạo một lần nộp có hai cha nên giữ nguyên lịch sử thật; sắp xếp lại viết lại các lần nộp lên trên đỉnh nhánh khác nên lịch sử thẳng nhưng băm đổi. Hệ quả và quy tắc: không sắp xếp lại nhánh đã đẩy lên và người khác đang dùng. Xung đột xảy ra khi hai nhánh sửa cùng vùng, và cách đọc dấu xung đột. Ba loại xung đột trong dự án dữ liệu và cách xử lý: xung đột mã thì giải bằng đọc, xung đột tệp phụ thuộc thì giải bằng dựng lại từ khai báo, xung đột tệp sinh tự động thì giải bằng sinh lại chứ không sửa tay. Chiến lược nhánh cho nhóm nhỏ: nhánh ngắn hạn từ nhánh chính, gộp qua yêu cầu kéo, xoá sau khi gộp. Vì sao nhánh sống lâu tích tụ xung đột theo cấp số nhân. Chọn lấy một lần nộp lẻ. Hoàn tác an toàn bằng lần nộp đảo ngược thay vì viết lại lịch sử. Nhật ký tham chiếu để cứu lần nộp tưởng đã mất.",
"Giải ba loại xung đột bằng ba cách khác nhau, và hoàn tác một thay đổi đã đẩy mà không viết lại lịch sử.",
"Tầng *áp dụng*. Objective gồm ba thao tác có tiêu chí đúng sai rõ. Đạt khi cả ba xung đột được giải mà bộ kiểm thử vẫn xanh, và khi thay đổi đã đẩy được hoàn tác mà băm của các lần nộp cũ không đổi.",
"Dựng ba xung đột: hai người sửa cùng hàm, hai người thêm phụ thuộc khác nhau, hai người đổi tệp khoá phụ thuộc sinh tự động. Giải từng cái bằng cách phù hợp. Đẩy một lần nộp lỗi rồi hoàn tác bằng lần nộp đảo ngược. Dùng nhật ký tham chiếu cứu một nhánh đã xoá.",
"Sửa tay tệp khoá phụ thuộc khi xung đột · sắp xếp lại nhánh người khác đang dùng · giải xung đột bằng cách giữ một bên mà không đọc bên kia.",
"Ba xung đột giải xong bộ kiểm thử vẫn xanh, và hoàn tác không làm đổi băm các lần nộp cũ."),

(80,"Pull requests, code review and what to look for in data code","TH","Lesson 79",
"Yêu cầu kéo là đơn vị rà soát, và kích thước của nó quyết định chất lượng rà soát: quá 400 dòng thì người rà soát chuyển sang đọc lướt. Mô tả yêu cầu kéo phải nêu vì sao chứ không nêu cái gì, vì cái gì đã nằm trong khác biệt mã. Danh mục rà soát riêng cho mã dữ liệu, mười điểm khác với rà soát mã ứng dụng thường: mô hình có bất biến khi chạy lại không, có đọc đồng hồ hệ thống không, bản ghi lỗi có bị loại im lặng không, có đối soát số lượng không, giao dịch có được đóng không, truy vấn có tham số hoá không, có nạp cả tệp vào bộ nhớ không, kiểu số cho tiền có đúng không, múi giờ có khai báo không, và bí mật có lọt vào không. Nhận xét rà soát nên nêu hệ quả thay vì nêu sở thích. Phân biệt điều kiện chặn với gợi ý. Tự rà soát trước khi mở yêu cầu kéo. Rà soát là nơi truyền chuẩn của nhóm, không phải nơi bắt lỗi chính tả.",
"Rà soát một yêu cầu kéo mã dữ liệu bằng danh mục mười điểm và phân loại mỗi phát hiện thành chặn hay gợi ý.",
"Tầng *đánh giá*. Objective đòi phán đoán mức nghiêm trọng, không có đáp án máy móc. Kiểm bằng một yêu cầu kéo cài sẵn bảy vấn đề thuộc bảy điểm khác nhau; đạt khi tìm được ít nhất năm trên bảy và khi phân loại chặn hay gợi ý khớp với đáp án cho ít nhất bốn phát hiện.",
"Nhận yêu cầu kéo 300 dòng cài sẵn bảy vấn đề. Rà soát theo danh mục mười điểm, viết nhận xét nêu hệ quả, phân loại chặn hay gợi ý. Đổi bài chéo: người khác rà soát yêu cầu kéo của bạn và so số phát hiện.",
"Nhận xét về sở thích định dạng thay vì về hệ quả · duyệt yêu cầu kéo 2.000 dòng · đánh dấu mọi phát hiện là chặn.",
"Tìm được ít nhất năm trên bảy vấn đề cài sẵn, và phân loại chặn hay gợi ý khớp đáp án cho ít nhất bốn."),

(81,"Repository layout for a data project","TH","Lesson 80",
"Cấu trúc thư mục là hợp đồng ngầm với người đọc tiếp theo, nên nó phải nói được ngay cái gì nằm ở đâu. Bốn thư mục lõi và trách nhiệm: mã nguồn, kiểm thử, cấu hình, tài liệu. Tách mã nguồn khỏi thư mục gốc để nhập mô đun không phụ thuộc thư mục đang đứng, nối lại lesson 68. Không để dữ liệu trong kho mã, kể cả dữ liệu mẫu lớn, nối lại lesson 78; thay bằng script sinh dữ liệu có hạt giống cố định. Tệp đầu vào duy nhất và một lệnh chạy toàn bộ, đây chính là điều kiện của cổng 3. Tách phần thuần tuý biến đổi khỏi phần vào ra để kiểm thử được không cần hạ tầng, nối tới lesson 84. Thư mục cho quyết định kiến trúc và sổ tay xử lý, nối lại lesson 4. Tệp bỏ qua đủ rộng: tệp môi trường, tệp tạm, đầu ra sinh ra, và thư mục môi trường ảo. Tệp chủ sở hữu mã khi nhóm lớn dần.",
"Tổ chức một dự án dữ liệu theo cấu trúc bốn thư mục lõi sao cho một lệnh chạy được toàn bộ và kiểm thử biến đổi không cần hạ tầng.",
"Tầng *áp dụng*. Objective có hai tiêu chí kiểm được bằng chạy thật. Đạt khi một lệnh duy nhất dựng môi trường và chạy đầu cuối trên máy sạch, và khi bộ kiểm thử phần biến đổi chạy xanh với mạng bị chặn.",
"Tổ chức lại dự án ở lesson 77. Viết tệp đầu vào duy nhất. Thay dữ liệu mẫu đính kèm bằng script sinh có hạt giống cố định. Chạy trên máy ảo sạch bằng một lệnh. Chạy kiểm thử biến đổi với mạng bị chặn.",
"Để tệp dữ liệu mẫu 500 mê ga byte trong kho · đặt mã nguồn ngay thư mục gốc nên nhập mô đun phụ thuộc chỗ đứng · quên đưa thư mục môi trường ảo vào danh sách bỏ qua.",
"Một lệnh dựng và chạy được đầu cuối trên máy sạch, và kiểm thử biến đổi xanh khi chặn mạng."),

(82,"Dependency management, pinning and reproducible environments","TH","Lesson 81",
"Phụ thuộc trực tiếp và phụ thuộc bắc cầu; phần lớn rủi ro nằm ở cái sau vì không ai đọc chúng. Khoảng phiên bản so với ghim chính xác: khoảng cho cập nhật tự động nhưng làm hai lần cài ra hai môi trường khác nhau, ghim cho tái lập được nhưng phải cập nhật bằng tay. Tệp khai báo cho phụ thuộc trực tiếp và tệp khoá cho toàn bộ cây đã giải, và cả hai đều phải nộp vào kho. Băm của gói trong tệp khoá để phát hiện gói bị thay. Môi trường ảo và cô lập giữa các dự án, nối lại lesson 24 về nhóm điều khiển và không gian tên: cùng ý tưởng cô lập ở tầng khác. Lệnh cài đặt lặp lại được từ tệp khoá thay vì từ tệp khai báo. Xung đột phụ thuộc và vì sao thêm một thư viện có thể hạ cấp một thư viện khác. Quét lỗ hổng bảo mật trong cây phụ thuộc. Quy trình nâng cấp có kiểm soát: nâng một thứ, chạy kiểm thử, nộp riêng.",
"Dựng lại đúng môi trường của người khác từ tệp khoá, và chứng minh hai lần cài trên hai máy cho cùng danh sách phiên bản.",
"Tầng *áp dụng*. Objective có tiêu chí đối chứng tuyệt đối. Đạt khi danh sách phiên bản đã giải trên hai máy khác nhau khớp từng dòng, và khi cài từ tệp khai báo không ghim cho ra khác biệt đo được để thấy lý do phải khoá.",
"Cài từ tệp khai báo không ghim trên hai máy cách nhau một tuần, so danh sách phiên bản. Sinh tệp khoá, cài lại trên cả hai, so lại. Thêm một thư viện và quan sát nó hạ cấp thư viện khác. Chạy quét lỗ hổng.",
"Chỉ nộp tệp khai báo mà không nộp tệp khoá · cập nhật hàng loạt phụ thuộc trong một lần nộp · cài thẳng vào môi trường hệ thống.",
"Danh sách phiên bản trên hai máy khớp từng dòng khi cài từ tệp khoá, và khác biệt đo được khi cài không ghim."),

(83,"Lint, format and type check in one command","TH","Lesson 82",
"Ba loại công cụ tĩnh và cái mỗi loại bắt: định dạng lo hình thức nên không tranh cãi được, kiểm tra tĩnh bắt lỗi khả nghi như biến không dùng và ngoại lệ bắt quá rộng ở lesson 65, kiểm kiểu bắt lỗi kiểu nhờ gợi ý kiểu ở lesson 67. Chúng bắt được gì và không bắt được gì: không công cụ nào bắt được lỗi logic hay lỗi dữ liệu, nên chúng là điều kiện cần chứ không phải đủ. Cấu hình tập trung ở một tệp và nộp vào kho để cả nhóm dùng chung. Chạy tự động trước mỗi lần nộp, và vì sao chạy ở máy cá nhân trước rẻ hơn chạy ở CI. Áp dụng dần cho kho mã cũ bằng cách bật từng quy tắc thay vì bật hết rồi ngập trong cảnh báo. Bỏ qua một cảnh báo phải kèm lý do viết tại chỗ, không bỏ qua toàn cục. Kiểm kiểu nghiêm ngặt dần theo mô đun. Thời gian chạy của cả ba phải dưới một ngưỡng để người ta còn chạy.",
"Cấu hình ba công cụ tĩnh chạy bằng một lệnh dưới 30 giây, và áp dụng dần cho một kho mã cũ mà không phải sửa hết cùng lúc.",
"Tầng *áp dụng*. Objective có ràng buộc thời gian và ràng buộc áp dụng dần, cả hai kiểm được. Đạt khi một lệnh chạy cả ba dưới 30 giây trên kho mã của dự án, và khi kho mã cũ đi từ hàng trăm cảnh báo xuống 0 mà mỗi bước nộp đều xanh.",
"Cấu hình ba công cụ vào một tệp và một lệnh. Đo thời gian chạy. Áp lên kho mã cũ có 400 cảnh báo: bật từng nhóm quy tắc, sửa, nộp, lặp lại cho tới 0. Cài móc chạy trước khi nộp. Thử bỏ qua một cảnh báo kèm lý do tại chỗ.",
"Bật mọi quy tắc cùng lúc rồi tắt hết vì quá nhiều · bỏ qua cảnh báo ở mức toàn cục · tin rằng ba công cụ xanh nghĩa là mã đúng.",
"Một lệnh chạy cả ba dưới 30 giây, và kho mã cũ về 0 cảnh báo với mọi bước nộp trung gian đều xanh."),

(84,"Unit tests for pure transformation functions","TH","Lesson 83",
"Hàm thuần nhận đầu vào trả đầu ra không chạm thế giới ngoài, nên kiểm thử nó nhanh và tất định. Đây là lý do tách phần biến đổi khỏi phần vào ra ở lesson 68 và 81: để phần lớn logic nằm trong hàm thuần. Cấu trúc một kiểm thử ba phần: dựng, chạy, khẳng định. Một kiểm thử kiểm một điều, và tên kiểm thử nói điều kiện cùng kết quả mong đợi. Dữ liệu cố định nhỏ và đặt ngay trong kiểm thử để đọc được, không nạp từ tệp ngoài. Sáu trường hợp biên bắt buộc cho mọi biến đổi dữ liệu: đầu vào rỗng, một bản ghi, giá trị rỗng ở mọi cột, giá trị trùng, giá trị biên của khoảng số, và ngày ở ranh giới múi giờ. Kiểm thử tham số hoá cho nhiều bộ đầu vào. Độ phủ là chỉ báo chứ không phải mục tiêu: 100% độ phủ với khẳng định yếu không chứng minh gì. Kiểm thử phải chạy nhanh để người ta còn chạy thường xuyên.",
"Viết kiểm thử đơn vị cho một biến đổi phủ đủ sáu trường hợp biên, và chứng minh chúng bắt được lỗi bằng cách cố ý làm hỏng mã.",
"Tầng *áp dụng*. Objective đòi chứng minh bộ kiểm thử có tác dụng, không chỉ đòi viết kiểm thử. Kiểm bằng kiểm thử đột biến thủ công: cài năm lỗi nhỏ vào mã biến đổi. Đạt khi bộ kiểm thử bắt được ít nhất bốn trên năm. Độ phủ cao mà không bắt được lỗi thì không đạt.",
"Viết kiểm thử đơn vị cho hàm chuẩn hoá và gộp ở lesson 77, phủ sáu trường hợp biên. Đo thời gian chạy toàn bộ. Cài năm lỗi nhỏ: đảo dấu so sánh, lệch một đơn vị, bỏ xử lý giá trị rỗng, sai múi giờ, sai thứ tự làm tròn. Chạy và đếm số lỗi bị bắt.",
"Viết kiểm thử chỉ cho đường thuận · nạp dữ liệu kiểm thử từ tệp lớn ngoài · dùng độ phủ làm mục tiêu thay vì làm chỉ báo.",
"Bộ kiểm thử bắt ít nhất bốn trên năm lỗi cài sẵn, và chạy toàn bộ dưới ngưỡng thời gian đã đặt."),

(85,"Integration tests against a real database","TH","Lesson 84",
"Kiểm thử tích hợp chạy trên hạ tầng thật vì lỗi cơ sở dữ liệu chỉ lộ ra ở cơ sở dữ liệu. Giả lập cơ sở dữ liệu là cách chắc chắn nhất để bỏ sót lỗi kiểu dữ liệu, lỗi ràng buộc, lỗi giao dịch và lỗi cú pháp riêng của hệ đó. Dựng cơ sở dữ liệu tạm cho kiểm thử bằng vùng chứa dùng một lần, khởi tạo lược đồ, chạy, rồi bỏ. Cô lập giữa các kiểm thử: mỗi kiểm thử một lược đồ riêng hoặc hoàn tác giao dịch sau mỗi kiểm thử, và đánh đổi giữa hai cách. Dữ liệu mồi tối thiểu đủ để kiểm điều đang kiểm, không mồi cả cơ sở dữ liệu. Kiểm thử phải chạy lại được nhiều lần mà cho cùng kết quả, nên không phụ thuộc thứ tự chạy và không phụ thuộc dữ liệu còn sót. Tốc độ: kiểm thử tích hợp chậm hơn đơn vị nhiều bậc nên chia hai nhóm chạy riêng, nối tới lesson 88. Điều gì nên kiểm ở tầng này và điều gì để tầng dưới.",
"Viết kiểm thử tích hợp chạy trên cơ sở dữ liệu thật dùng một lần, và chứng minh chúng chạy lại được nhiều lần cho cùng kết quả bất kể thứ tự.",
"Tầng *áp dụng*. Objective có tiêu chí kiểm được bằng chạy lặp và chạy xáo thứ tự. Đạt khi chạy bộ kiểm thử 10 lần liên tiếp và 5 lần với thứ tự ngẫu nhiên đều cho cùng kết quả, và khi ít nhất một kiểm thử bắt được lỗi mà kiểm thử đơn vị giả lập không bắt được.",
"Viết kiểm thử tích hợp cho phần ghi của dự án lesson 77, dùng vùng chứa cơ sở dữ liệu dùng một lần. Chạy 10 lần liên tiếp và 5 lần xáo thứ tự. Cài một lỗi vi phạm ràng buộc khoá và xác nhận bản giả lập không bắt được còn bản thật bắt được.",
"Giả lập cơ sở dữ liệu để chạy nhanh · dùng chung một cơ sở dữ liệu giữa các kiểm thử nên phụ thuộc thứ tự · mồi cả cơ sở dữ liệu cho mỗi kiểm thử.",
"10 lần chạy liên tiếp và 5 lần xáo thứ tự đều cùng kết quả, và ít nhất một lỗi chỉ bản thật bắt được."),

(86,"Property-based testing for data transformations","TH","Lesson 85",
"Kiểm thử theo ví dụ kiểm những trường hợp người viết nghĩ ra; kiểm thử theo tính chất phát biểu điều phải luôn đúng rồi để máy sinh đầu vào tìm phản ví dụ. Nó mạnh đúng ở chỗ con người yếu: các tổ hợp không ai nghĩ tới. Năm tính chất hay dùng cho biến đổi dữ liệu: số dòng ra có quan hệ xác định với số dòng vào, tổng theo khoá nghiệp vụ được bảo toàn, chạy hai lần bằng chạy một lần, thứ tự đầu vào không ảnh hưởng kết quả, và biến đổi rồi đảo ngược trả về bản gốc. Tính chất thứ ba chính là bất biến khi chạy lại và là tiêu chí xuyên suốt chương trình. Sinh dữ liệu có ràng buộc để đầu vào hợp lệ. Thu nhỏ phản ví dụ về trường hợp nhỏ nhất còn hỏng, tính năng làm kỹ thuật này đáng dùng. Ghi lại hạt giống để tái hiện ca hỏng, nối lại lesson 60. Khi nào kiểm thử theo tính chất không hợp: khi không phát biểu được tính chất nào rõ ràng.",
"Phát biểu năm tính chất cho một biến đổi và tìm phản ví dụ cho ít nhất một tính chất bị vi phạm.",
"Tầng *phân tích*. Objective đòi phát biểu tính chất đúng và đọc được phản ví dụ, không chỉ chạy công cụ. Đạt khi năm tính chất phát biểu được bằng mã chạy được, và khi tìm ra phản ví dụ cho lỗi cài sẵn cùng bản thu nhỏ của nó.",
"Phát biểu năm tính chất cho biến đổi ở lesson 77. Chạy với 10.000 đầu vào sinh tự nhiên. Cài một lỗi chỉ hỏng khi có giá trị rỗng trong khoá gộp. Chạy lại, đọc phản ví dụ và bản thu nhỏ. Ghi hạt giống, tái hiện.",
"Phát biểu tính chất quá yếu nên không bao giờ hỏng · sinh đầu vào không hợp lệ rồi kiểm thử hỏng vì lý do sai · không ghi hạt giống nên không tái hiện được.",
"Năm tính chất phát biểu bằng mã chạy được, và tìm ra phản ví dụ cùng bản thu nhỏ cho lỗi cài sẵn."),

(87,"Contract tests for schemas","TH","Lesson 86",
"Hợp đồng lược đồ phát biểu hình dạng dữ liệu hai bên thoả thuận, và kiểm thử hợp đồng kiểm nó tự động ở biên. Hai hướng cần kiểm và chúng khác nhau: nguồn có còn cung cấp đúng thứ mình giả định không, và mình có còn tạo ra đúng thứ hạ nguồn giả định không. Nội dung một hợp đồng: tên cột, kiểu, trường bắt buộc, dải giá trị hợp lệ, và ngữ nghĩa khoá. Thay đổi tương thích ngược so với thay đổi phá vỡ: thêm cột tuỳ chọn thì tương thích, xoá cột hay đổi kiểu thì phá vỡ. Ba phản ứng khi nguồn thêm cột và tiêu chí chọn, nối tới chặng 4. Kiểm hợp đồng chạy ở đâu: ở CI trên mẫu dữ liệu cố định, và ở thời điểm chạy thật trên dữ liệu thật, hai chỗ bắt hai loại vấn đề khác nhau. Phiên bản hoá hợp đồng và thời gian chuyển tiếp khi đổi. Vì sao phát hiện sớm rẻ hơn nhiều so với phát hiện ở bảng điều khiển.",
"Viết hợp đồng lược đồ cho một nguồn và một đích, và chứng minh kiểm thử bắt được cả thay đổi phá vỡ lẫn thay đổi tương thích, phân loại đúng từng loại.",
"Tầng *áp dụng*. Objective có tiêu chí phân loại kiểm được. Đạt khi sáu thay đổi lược đồ được phân loại đúng cả sáu, trong đó thay đổi phá vỡ làm kiểm thử đỏ còn thay đổi tương thích thì không, và khi kiểm ở thời điểm chạy bắt được một vấn đề mà kiểm ở CI không bắt được.",
"Viết hợp đồng cho nguồn và đích của dự án lesson 77. Cài sáu thay đổi: thêm cột tuỳ chọn, thêm cột bắt buộc, xoá cột, đổi kiểu, đổi ngữ nghĩa khoá, nới dải giá trị. Chạy kiểm hợp đồng ở CI và ở thời điểm chạy, so kết quả.",
"Chỉ kiểm hợp đồng ở CI nên không bắt được dữ liệu thật lệch · coi mọi thay đổi lược đồ là phá vỡ · không phiên bản hoá hợp đồng nên đổi là vỡ ngay.",
"Sáu thay đổi phân loại đúng cả sáu, và kiểm ở thời điểm chạy bắt được vấn đề mà CI không bắt."),

(88,"Continuous integration that runs in under ten minutes","TH","Lesson 87",
"CI chỉ có giá trị nếu người ta chờ nó, nên thời gian chạy là ràng buộc thiết kế chứ không phải kết quả. Bốn giai đoạn theo thứ tự chi phí tăng dần và nguyên tắc dừng sớm: công cụ tĩnh, kiểm thử đơn vị, kiểm thử tích hợp, kiểm thử hợp đồng. Chạy song song các giai đoạn độc lập. Bộ nhớ đệm phụ thuộc giữa các lần chạy và cách khoá bộ đệm theo tệp khoá ở lesson 82. Dịch vụ phụ trợ cho kiểm thử tích hợp và chờ tới khi sẵn sàng thay vì ngủ một khoảng cố định. Bí mật trong CI và nguyên tắc không in ra nhật ký, nối lại lesson 75. Kiểm thử chập chờn là thứ giết CI nhanh nhất: nguyên nhân thường gặp là phụ thuộc thời gian, phụ thuộc thứ tự, và tranh chấp ở lesson 51; quy trình xử lý là cách ly rồi sửa chứ không phải thử lại tự động. Ngân sách thời gian cho từng giai đoạn và cắt gì khi vượt. CI xanh là điều kiện gộp, không phải gợi ý.",
"Dựng CI chạy đủ bốn giai đoạn dưới 10 phút, và xử lý một kiểm thử chập chờn tới nguyên nhân gốc thay vì thử lại.",
"Tầng *áp dụng*. Objective có ràng buộc thời gian cứng và một tiêu chí về cách xử lý. Đạt khi CI chạy đủ bốn giai đoạn dưới 10 phút, và khi kiểm thử chập chờn cài sẵn được truy về nguyên nhân gốc với bằng chứng, không được xử lý bằng thử lại.",
"Dựng CI bốn giai đoạn cho dự án. Đo thời gian từng giai đoạn. Thêm bộ nhớ đệm phụ thuộc và đo lại. Cài một kiểm thử chập chờn do tranh chấp, chạy CI 30 lần, quan sát tỉ lệ đỏ, truy nguyên và sửa.",
"Thêm thử lại tự động cho kiểm thử chập chờn · chạy kiểm thử tích hợp trước kiểm thử đơn vị · ngủ một khoảng cố định để chờ dịch vụ phụ trợ.",
"CI chạy đủ bốn giai đoạn dưới 10 phút, và kiểm thử chập chờn được truy về nguyên nhân gốc có bằng chứng."),

(89,"Tags, releases and versioning a data job","TH","Lesson 88",
"Phiên bản hoá ngữ nghĩa và ba thành phần của nó, cùng câu hỏi đặc thù cho công việc dữ liệu: cái gì tính là thay đổi phá vỡ khi sản phẩm là một bảng chứ không phải một thư viện. Ba loại thay đổi phá vỡ ở tầng dữ liệu: đổi lược đồ đầu ra, đổi ngữ nghĩa một cột mà không đổi tên, và đổi hạt của bảng. Loại thứ hai nguy hiểm nhất vì không có tín hiệu kỹ thuật nào. Thẻ gắn vào một lần nộp và khác nhánh ở chỗ nó không di chuyển. Nhật ký thay đổi viết cho người dùng dữ liệu chứ không cho lập trình viên: nêu số nào đổi và đổi từ khi nào. Gắn phiên bản mã vào dữ liệu đầu ra để truy được bảng này do bản nào sinh ra, một thực hành rẻ và cứu được nhiều giờ điều tra. Quay lui mã không quay lui được dữ liệu đã ghi, nên phải có kế hoạch chạy lại. Môi trường và quy trình phát hành, chuẩn bị cho chặng 7.",
"Phát hành một phiên bản có thẻ và nhật ký thay đổi, và gắn được phiên bản mã vào dữ liệu đầu ra để truy ngược.",
"Tầng *áp dụng*. Objective có sản phẩm và một tiêu chí truy ngược kiểm được. Đạt khi từ một dòng dữ liệu bất kỳ trong bảng đích truy được về đúng lần nộp sinh ra nó, và khi nhật ký thay đổi nêu được thay đổi ngữ nghĩa bằng ngôn ngữ người dùng dữ liệu hiểu.",
"Phát hành ba phiên bản liên tiếp của công việc, trong đó một phiên bản đổi ngữ nghĩa một cột. Gắn phiên bản mã vào mỗi dòng đầu ra. Chọn ngẫu nhiên 10 dòng trong bảng và truy về lần nộp. Viết nhật ký thay đổi cho người dùng dữ liệu.",
"Coi đổi ngữ nghĩa cột là thay đổi nhỏ vì lược đồ không đổi · viết nhật ký thay đổi bằng ngôn ngữ lập trình viên · tin rằng quay lui mã là quay lui dữ liệu.",
"Truy được 10 dòng ngẫu nhiên về đúng lần nộp sinh ra chúng, và nhật ký thay đổi nêu rõ thay đổi ngữ nghĩa."),

(90,"Documentation that survives - README, ADR, runbook","TH","Lesson 89",
"Ba loại tài liệu phục vụ ba câu hỏi khác nhau và không thay thế nhau. Tài liệu giới thiệu trả lời làm sao chạy được: bảy phần gồm mục đích, yêu cầu, cài đặt, dữ liệu, cách chạy, đầu ra, và giới hạn đã biết. Bản ghi quyết định kiến trúc trả lời vì sao làm thế này: bối cảnh, các phương án đã cân nhắc, lý do loại từng phương án, và tín hiệu khiến nên xem lại. Phần phương án bị loại là phần có giá trị nhất và là phần hay bị bỏ. Sổ tay xử lý trả lời hỏng thì làm gì: triệu chứng, cách xác nhận, các bước xử lý, và cách biết đã xong. Sổ tay viết cho người trực lúc ba giờ sáng không có ngữ cảnh, nên mỗi bước phải là lệnh chạy được chứ không phải mô tả. Tiêu chí duy nhất để đánh giá tài liệu: người khác làm theo được mà không hỏi. Tài liệu chết vì không cập nhật, và cách chống là để nó gần mã và kiểm trong CI.",
"Viết ba loại tài liệu cho dự án của mình, và chứng minh bằng quan sát rằng người khác chạy được và xử lý được sự cố mà không hỏi.",
"Tầng *đánh giá*. Objective đo bằng người dùng thật, không bằng danh sách mục đã điền. Kiểm bằng quan sát: hai người chưa từng thấy dự án, một người chạy theo tài liệu giới thiệu, một người xử lý sự cố theo sổ tay. Đạt khi cả hai hoàn thành mà không đặt câu hỏi nào, có ghi chép điểm vướng.",
"Viết ba loại tài liệu. Đưa cho hai học viên khác: một người chạy dự án từ đầu, một người nhận một sự cố cài sẵn và xử lý theo sổ tay. Ghi lại mọi chỗ họ vướng hoặc phải hỏi. Sửa tài liệu theo điểm vướng rồi thử lại với người thứ ba.",
"Viết bản ghi quyết định mà bỏ phần phương án bị loại · viết sổ tay bằng mô tả thay vì lệnh chạy được · để tài liệu ở nơi khác kho mã nên nó lạc hậu.",
"Hai người chưa từng thấy dự án hoàn thành việc của mình mà không hỏi, có ghi chép điểm vướng."),

(91,"Gate 3 - clone, one command, same result","KT","Lesson 90",
"Không có nội dung mới. Cổng 3 của chương trình, và nó đo thứ khó giả: một kho mã người khác dùng được.",
"Giao một kho mã mà người chưa từng thấy sao về, chạy một lệnh dựng môi trường, chạy công việc, và thu được đúng kết quả của mình, với CI xanh và dữ liệu sau hai lần chạy bằng sau một lần.",
"Tầng *đánh giá*. Cổng đo tính giao được của một sản phẩm, nên người chấm là một học viên khác chứ không phải người viết. Thang điểm: A 25đ một lệnh dựng và chạy được trên máy sạch · B 20đ kết quả khớp đối chứng · C 20đ chạy hai lần bằng chạy một lần · D 20đ CI xanh đủ bốn giai đoạn dưới 10 phút · E 15đ ba loại tài liệu đủ để người chấm không phải hỏi. Đạt khi ≥ 70/100, phần A và phần C đều ≥ 70% của chúng.",
"Đổi kho mã chéo với một học viên khác. Người nhận chạy trên máy ảo sạch, ghi lại mọi chỗ phải hỏi hoặc phải sửa. Chạy công việc hai lần, đối soát. Mỗi câu hỏi phải đặt ra là một điểm trừ ở phần E.",
"Giả định người chấm có sẵn công cụ mình đang dùng · để bước cài đặt phải làm tay ở giữa · bộ kiểm thử xanh trên máy mình nhưng đỏ trên máy sạch.",
"Đạt ≥ 70/100, phần A và phần C đều ≥ 70%."),
]
