# -*- coding: utf-8 -*-
"""ADE Phase 1: M1 Engineering thinking/Git/debugging + M2 Python production + M3 DSA."""

M1 = ("Engineering Thinking, Git and Debugging", 1, 12, """| | |
|---|---|
| **Objective cấp module** | Biến một yêu cầu mơ hồ thành hợp đồng kiểm thử được, quản lý thay đổi an toàn, và chẩn đoán lỗi bằng bằng chứng chứ bằng thử sai |
| **Tiền đề** | Không. Dùng được terminal và sửa được tệp văn bản |
| **Exit criterion** | Vẽ đúng đồ thị đối tượng của một kho Git và dự đoán đúng `HEAD` sau merge, rebase, reset; nhật ký gỡ lỗi có ít nhất ba giả thuyết bị bác bỏ bằng bằng chứng |
| **Kỹ năng SFIA** | `PROG` mức 3 · `TEST` mức 3 |
| **Chế độ hỏng** | Học thuộc lệnh Git rời rạc mà không có mô hình đối tượng, nên mất commit là mất luôn, và sửa lỗi bằng cách đổi thử tới khi hết báo lỗi |""",
"""Module mở đầu và là module đặt kỷ luật cho cả 428 bài còn lại. Ba năng lực ở đây được dùng lại ở mọi module sau: phát biểu hợp đồng trước khi viết mã, quản lý thay đổi có thể lùi, và chẩn đoán có bằng chứng.

Không dạy công cụ dữ liệu nào. Đây là chủ ý: người học vào thẳng công cụ dữ liệu mà thiếu ba năng lực này sẽ dựng được pipeline chạy nhưng không sửa được khi nó hỏng.""")

L1 = [
(1,"From a vague request to a testable contract","LT","Module 1: Không",
"Yêu cầu nghiệp vụ tới dưới dạng một câu mơ hồ, và khoảng cách giữa câu đó với một thứ kiểm thử được là nơi phần lớn công sức bị lãng phí. Sáu phần của một phát biểu bài toán dùng được: ai là người dùng, sự kiện nào kích hoạt, đầu vào gì, đầu ra gì, ràng buộc nào, và **cái gì cố ý không làm**. Phần cuối là phần hay thiếu nhất và cũng là phần cứu dự án khỏi phình. Chuyển mỗi yêu cầu thành hành vi quan sát được rồi thành một phép kiểm chấp nhận: nếu không viết được phép kiểm thì yêu cầu chưa đủ rõ để bắt đầu. Ba loại ràng buộc phải tách bạch vì chúng dẫn tới ba thiết kế khác nhau: ràng buộc về đúng đắn, về hiệu năng, và về vận hành. Phi mục tiêu viết ra thành câu chứ để ngầm hiểu.",
"Viết lại một yêu cầu mơ hồ thành phát biểu sáu phần, và cho mỗi yêu cầu một phép kiểm chấp nhận kiểm được.",
"Tầng *áp dụng*. Bài mở chương trình, người học chưa có nền kỹ thuật nào nên objective dừng ở việc áp một khuôn có sẵn vào tình huống mới. Kiểm bằng bài viết lại ba yêu cầu; đạt khi cả ba có đủ sáu phần và mọi phép kiểm chấp nhận đều nêu được đầu vào cùng kết quả mong đợi.",
"Nhận ba yêu cầu viết theo cách người nghiệp vụ thật hay nhắn. Viết lại từng cái thành phát biểu sáu phần. Với mỗi yêu cầu, viết ít nhất hai phép kiểm chấp nhận có đầu vào và kết quả mong đợi cụ thể. Đổi bài với một học viên khác: họ chỉ ra chỗ nào còn mơ hồ tới mức hai người có thể hiểu khác nhau.",
"Bỏ phần phi mục tiêu · viết phép kiểm dạng chạy không lỗi · trộn ràng buộc đúng đắn với ràng buộc hiệu năng · bắt đầu viết mã khi chưa viết được phép kiểm nào.",
"Ba yêu cầu đều có đủ sáu phần, mỗi yêu cầu có ≥ 2 phép kiểm chấp nhận cụ thể, và người đổi bài không tìm được chỗ hiểu hai nghĩa."),

(2,"Decomposition - responsibility, interface, state and failure domain","LT","Lesson 1",
"Chia một hệ thành phần là quyết định thiết kế đầu tiên và khó sửa nhất. Bốn trục để chia và mỗi trục trả lời một câu hỏi khác nhau: trách nhiệm tức phần này chịu trách nhiệm về cái gì, giao diện tức nó hứa gì với bên ngoài, trạng thái tức nó nhớ gì, và phạm vi hỏng tức nó chết thì kéo theo những gì. Độ gắn kết và độ phụ thuộc: gắn kết cao trong một phần, phụ thuộc thấp giữa các phần, và chiều phụ thuộc phải một chiều chứ vòng. Trừu tượng hoá che cái gì và bắt buộc lộ cái gì; trừu tượng rò rỉ là trừu tượng che một thứ mà người dùng vẫn phải biết, và nhận ra nó sớm tiết kiệm rất nhiều thời gian về sau. Bất biến là điều luôn đúng qua mọi lần chuyển trạng thái; bài này chỉ đặt khái niệm, còn chỗ đặt bất biến vào cơ sở dữ liệu sẽ quay lại ở M10.",
"Phân rã một hệ cho trước theo bốn trục và chỉ ra chiều phụ thuộc cùng phạm vi hỏng của từng phần.",
"Tầng *phân tích*. Objective đòi tách một chỉnh thể thành các phần có ranh giới lý giải được, chứ vẽ lại sơ đồ có sẵn. Kiểm bằng bài phân rã cộng phản biện; đạt khi bốn trục đều được trả lời và không có phụ thuộc vòng.",
"Cho mô tả một hệ bán hàng nhỏ. Phân rã thành các phần, với mỗi phần ghi bốn trục. Vẽ chiều phụ thuộc và chỉ ra phụ thuộc vòng nếu có. Với mỗi phần, trả lời: phần này chết thì cái gì còn chạy được. Hai bạn cùng lớp phản biện ranh giới bạn chọn.",
"Chia theo tầng kỹ thuật thay vì theo trách nhiệm · để phụ thuộc vòng · bỏ qua trạng thái nên không thấy phần nào khó thay thế · vẽ sơ đồ mà không nêu phạm vi hỏng.",
"Bốn trục được trả lời cho mọi phần, đồ thị phụ thuộc không có vòng, và chỉ đúng phạm vi hỏng của ít nhất ba phần."),

(3,"Trade-offs and the architecture decision record","TH","Lesson 2",
"Phần lớn quyết định kỹ thuật không có phương án đúng tuyệt đối, chỉ có phương án phù hợp ràng buộc, nên thứ cần lưu lại là **lý do** chứ kết luận. Tài liệu quyết định kiến trúc có năm phần: bối cảnh và ràng buộc, các phương án đã cân nhắc, quyết định, hệ quả gồm cả mặt xấu, và điều kiện xem lại. Phần các phương án bị loại là phần giá trị nhất: người đọc sau cần biết phương án kia đã được xét và loại vì gì, nếu không họ đề xuất lại đúng phương án đó. Điều kiện xem lại làm tài liệu này khác một biên bản: ghi mốc nào thì quyết định nên được xét lại. Tiêu chí so sánh phải nêu trước khi so, nếu không thì việc so biến thành biện minh cho lựa chọn đã có sẵn trong đầu. Khả năng đảo ngược là một tiêu chí thường bị bỏ: quyết định dễ lùi thì quyết nhanh, quyết định khó lùi thì cần bằng chứng.",
"Viết một tài liệu quyết định đủ năm phần cho một lựa chọn thật, và người không dự buổi quyết định đọc hiểu được lý do.",
"Tầng *áp dụng*. Objective là một sản phẩm viết theo chuẩn, kiểm được bằng phản ứng của người đọc chứ bằng độ dài. Kiểm bằng rà soát chéo; đạt khi người rà soát không còn câu hỏi nào về lý do và điều kiện xem lại là kiểm được.",
"Chọn định dạng tệp cho một bài toán trao đổi dữ liệu giữa hai đội: so CSV, JSON và Parquet theo lược đồ, kích thước, khả năng liên thông và mẫu quét. Nêu tiêu chí trước, rồi mới so. Viết tài liệu quyết định đủ năm phần, dưới hai trang. Đưa cho một học viên khác đọc và ghi lại mọi câu họ phải hỏi.",
"Bỏ phần phương án bị loại · viết hệ quả chỉ có mặt tốt · đặt điều kiện xem lại chung chung · chọn trước rồi mới nghĩ tiêu chí.",
"Tài liệu đủ năm phần và dưới hai trang, người rà soát không còn câu hỏi về lý do, và điều kiện xem lại nêu được mốc kiểm được."),

(4,"Git as a content-addressed object database","LT","Lesson 3",
"Học Git bằng cách nhớ lệnh thì mỗi tình huống lạ là một lần bế tắc; học bằng mô hình đối tượng thì suy ra được lệnh. Bốn loại đối tượng: blob giữ nội dung tệp, cây giữ danh sách tên trỏ tới blob và cây con, commit giữ một cây cộng danh sách cha cộng siêu dữ liệu, và thẻ có chú thích. Điểm quyết định: **commit là ảnh chụp toàn bộ cây cộng con trỏ cha, không phải một bản khác biệt**; phần khác biệt chỉ là thứ Git tính ra khi cần hiển thị. Ba vùng và ba con trỏ: cây làm việc, vùng chờ, kho; `HEAD` trỏ tới nhánh, nhánh trỏ tới commit. Từ mô hình này suy ra ngay: xoá nhánh không xoá commit, nên commit vẫn còn và phục hồi được; hai nhánh chia sẻ phần lịch sử chung vì cùng trỏ ngược về một tổ tiên. Cách tự kiểm chứng mọi khẳng định trên bằng lệnh đọc đối tượng thô, thay vì tin lời giảng.",
"Vẽ đúng đồ thị đối tượng của một kho nhỏ và dự đoán con trỏ nào thay đổi sau mỗi thao tác.",
"Tầng *hiểu*. Bài lý thuyết nền, chưa đòi xử lý sự cố. Kiểm bằng bài vẽ cộng dự đoán viết trước khi chạy; đạt khi đồ thị đúng và dự đoán khớp thực tế ở ít nhất năm trong sáu thao tác.",
"Tạo một kho mới, tạo ba commit. Dùng lệnh đọc đối tượng thô để liệt kê blob, cây và commit, rồi vẽ đồ thị. Với sáu thao tác gồm `add`, `commit`, `checkout`, `branch`, `reset --soft` và `reset --hard`, viết dự đoán con trỏ nào đổi **trước khi chạy**, rồi chạy và đối chiếu.",
"Nghĩ commit lưu phần khác biệt · nhầm nhánh với thư mục · tin rằng xoá nhánh là mất commit · học lệnh mà không đọc đối tượng lần nào.",
"Đồ thị đối tượng vẽ đúng, và dự đoán khớp thực tế ở ≥ 5/6 thao tác."),

(5,"Branching, merge, rebase and commit identity","TH","Lesson 4",
"Hợp nhất ba chiều dùng tổ tiên chung làm gốc so sánh, nên hiểu tổ tiên chung là hiểu vì sao xung đột xảy ra ở đúng chỗ đó. Xung đột không phải lỗi mà là chỗ Git không tự quyết được; giải xung đột là một quyết định nội dung chứ thao tác cơ khí. Rebase phát lại các commit lên một gốc mới, và điều quan trọng là **commit mới có mã định danh mới dù nội dung giống hệt**; từ đó suy ra quy tắc không rebase nhánh người khác đang dùng. Ba cách hợp nhất và hệ quả lên lịch sử: hợp nhất thường giữ đồ thị thật, rebase cho lịch sử thẳng nhưng viết lại định danh, và gộp thành một commit làm mất bước trung gian. Phân biệt viết lại lịch sử với commit đảo ngược: `revert` tạo một commit mới huỷ hiệu lực commit cũ và an toàn trên nhánh chung, còn `reset` viết lại và chỉ an toàn trên nhánh riêng.",
"Chọn đúng giữa hợp nhất, rebase và đảo ngược cho một tình huống cho trước, và giải thích bằng định danh commit cùng phạm vi ảnh hưởng.",
"Tầng *đánh giá*. Objective đòi cân giữa lịch sử sạch và an toàn cho người khác, chứ nhớ cú pháp. Kiểm bằng bốn tình huống; đạt khi chọn đúng ít nhất ba và mỗi lần nêu đúng ai bị ảnh hưởng.",
"Dựng hai nhánh có xung đột nội dung. Giải xung đột và giải thích vì sao Git dừng ở đúng đoạn đó, dẫn bằng tổ tiên chung. Thực hiện cả ba cách hợp nhất trên ba bản sao của cùng kho, so đồ thị kết quả. Cho bốn tình huống và chọn cách xử lý, nêu ai bị ảnh hưởng nếu chọn sai.",
"Rebase nhánh đã đẩy lên kho chung · dùng `reset --hard` trên nhánh chung · gộp commit cho một chuỗi cần giữ bước trung gian · giải xung đột bằng cách giữ một bên mà không đọc.",
"Chọn đúng ≥ 3/4 tình huống kèm phạm vi ảnh hưởng, và giải thích đúng vị trí xung đột bằng tổ tiên chung."),

(6,"Recovering lost work - reflog, detached HEAD and bisect","TH","Lesson 5",
"Hai kỹ năng cứu nguy mà phần lớn người dùng Git chỉ học sau khi đã mất việc một lần. Nhật ký tham chiếu ghi lại mọi vị trí `HEAD` từng đứng, kể cả những vị trí không còn nhánh nào trỏ tới, nên gần như mọi commit đã tạo đều tìm lại được trong thời gian giữ mặc định. Ba tình huống mất việc hay gặp và cách phục hồi từng cái: `reset --hard` nhầm, xoá nhánh chưa hợp nhất, và rebase hỏng giữa chừng. `HEAD` tách rời là trạng thái bình thường chứ lỗi, nhưng commit tạo ra trong đó không có nhánh giữ nên dễ mất. Tìm lỗi bằng chia đôi biến việc truy hồi quy thành bài toán tìm kiếm nhị phân: với một phép kiểm tự động trả đúng mã thoát thì toàn bộ quá trình tự chạy. Điều kiện để dùng được: có phép kiểm tái hiện lỗi, và lịch sử có commit nhỏ chứ commit khổng lồ.",
"Phục hồi được việc đã mất trong ba tình huống, và định vị commit gây hồi quy bằng tìm kiếm chia đôi tự động.",
"Tầng *áp dụng*. Objective là hai thao tác cứu nguy kiểm được bằng kết quả. Kiểm bằng ba tình huống mất việc cộng một lần chia đôi; đạt khi phục hồi cả ba và chia đôi chỉ đúng commit gây lỗi.",
"Tự gây cả ba tình huống mất việc rồi phục hồi từng cái bằng nhật ký tham chiếu, ghi lại ghi chú phục hồi. Tạo 8 commit, cài một hồi quy ở commit thứ tư, viết một phép kiểm trả mã thoát đúng, rồi chạy chia đôi tự động và xác nhận nó chỉ ra commit 4.",
"Không biết nhật ký tham chiếu tồn tại · chia đôi thủ công thay vì dùng phép kiểm tự động · commit quá to nên chia đôi chỉ tới một commit đổi 40 tệp · hoảng rồi clone lại kho.",
"Phục hồi thành công cả ba tình huống có ghi chú, và chia đôi tự động chỉ đúng commit 4."),

(7,"Collaboration - small commits, review and release discipline","TH","Lesson 6",
"Làm việc nhóm đặt ra ràng buộc mà làm một mình không có, và ba ràng buộc quan trọng nhất đều nằm ở kích thước và ranh giới thay đổi. Commit nhỏ và một mục đích: dễ rà soát, dễ lùi, và làm chia đôi ở lesson 6 thật sự dùng được. Thông điệp commit nói **vì sao** chứ cái gì, vì cái gì đã nằm trong phần khác biệt. Yêu cầu hợp nhất là đơn vị rà soát: kèm mô tả, phạm vi ảnh hưởng, cách kiểm chứng, và ghi chú lùi. Rà soát mã là việc tìm hiểu lầm và rủi ro chứ bắt lỗi chính tả; ba câu hỏi người rà soát phải trả lời được. Chính sách nhánh và nhánh được bảo vệ. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa thật của từng số với người dùng thư viện. Ghi chú lùi phải nói được **lùi bằng cách nào**, chứ chỉ nói có lùi được hay không; và đây là chỗ một loại thay đổi phá vỡ giả định: **thay đổi có kèm sửa cấu trúc dữ liệu thì lùi mã không đủ**, vì mã cũ không đọc được dữ liệu đã đổi. Lời giải là kế hoạch tương thích: đổi cấu trúc theo hướng cộng thêm trước, để mã cũ và mã mới cùng chạy được trong một cửa sổ, rồi mới bỏ phần cũ. Quy tắc suy ra: khả năng lùi là một thuộc tính phải thiết kế, không phải một nút bấm có sẵn. Vì sao phần này nằm ở module đầu chứ module cuối: mọi lab từ đây trở đi đều nộp qua yêu cầu hợp nhất, nên kỷ luật phải có trước.",
"Nộp một yêu cầu hợp nhất đủ bốn phần, rà soát yêu cầu của người khác bằng ba câu hỏi bắt buộc, và chỉ ra được một thay đổi mà lùi mã không đủ để lùi.",
"Tầng *áp dụng*. Objective là hai vai trong cùng một quy trình, kiểm được bằng sản phẩm của cả hai phía. Kiểm bằng một vòng nộp và rà soát chéo cộng một phép thử lùi; đạt khi yêu cầu đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi cho thấy đúng chỗ lùi mã không đủ.",
"Chia nhỏ một thay đổi lớn thành bốn commit một mục đích, mỗi commit có thông điệp nói vì sao. Nộp yêu cầu hợp nhất đủ mô tả, phạm vi ảnh hưởng, cách kiểm chứng và ghi chú lùi. Rà soát yêu cầu của một học viên khác theo ba câu hỏi bắt buộc và ghi ít nhất một rủi ro. Tạo một thay đổi có kèm sửa cấu trúc dữ liệu, lùi mã về bản trước, và ghi lại chuyện gì xảy ra với dữ liệu đã đổi. Viết kế hoạch tương thích cho phép mã cũ và mã mới cùng chạy, rồi lùi lại lần nữa và chứng minh lần này lùi được.",
"Một commit khổng lồ cho cả tính năng · thông điệp commit chép lại tên tệp đã sửa · rà soát chỉ soi phong cách · bỏ ghi chú lùi · coi lùi mã là lùi được toàn bộ khi thay đổi có kèm sửa cấu trúc dữ liệu.",
"Bốn commit đều một mục đích và có lý do, yêu cầu hợp nhất đủ bốn phần, bản rà soát nêu được ít nhất một rủi ro thật, và phép thử lùi chỉ ra đúng chỗ lùi mã không đủ với kế hoạch tương thích làm lần lùi thứ hai thành công."),

(8,"Scientific debugging - from symptom to proven cause","LT","Lesson 7",
"Sửa lỗi bằng cách đổi thử tới khi hết báo lỗi là cách tạo ra lỗi tiếp theo, vì nguyên nhân chưa từng được chứng minh. Quy trình sáu bước: ghi lại triệu chứng gồm mong đợi, thực tế, thời điểm, phiên bản, đầu vào và môi trường; tái hiện một cách xác định; thu nhỏ về trường hợp hỏng nhỏ nhất; thêm khả năng quan sát ở ranh giới; lập bảng giả thuyết; và sửa đúng nguyên nhân nhỏ nhất rồi thêm phép kiểm hồi quy. Bảng giả thuyết là công cụ trung tâm và có ba cột: dự đoán, phép thử có thể bác bỏ nó, và kết quả. **Giả thuyết không kèm phép thử bác bỏ được thì không phải giả thuyết.** Phân biệt tương quan với nguyên nhân: hai thứ cùng xảy ra không chứng minh cái này gây cái kia. Định vị theo tầng từ trên xuống: dữ liệu đầu vào, ứng dụng, phụ thuộc, hệ điều hành và mạng, nền tảng.",
"Lập bảng giả thuyết cho một lỗi cho trước, với mỗi giả thuyết nêu một phép thử bác bỏ được.",
"Tầng *hiểu*. Bài lý thuyết đặt quy trình, phần thực hành nằm ở lesson 9. Kiểm bằng bảng giả thuyết cho ba lỗi mẫu; đạt khi mọi giả thuyết đều có phép thử bác bỏ được và không có giả thuyết nào không kiểm được.",
"Cho ba mô tả lỗi. Với mỗi lỗi, viết hồ sơ triệu chứng sáu phần và lập bảng giả thuyết ít nhất ba dòng. Đổi bài: học viên khác chỉ ra giả thuyết nào không bác bỏ được bằng phép thử bạn đề ra.",
"Đoán nguyên nhân rồi tìm bằng chứng ủng hộ nó · đặt giả thuyết dạng chắc do môi trường · sửa trước khi tái hiện · bỏ bước thu nhỏ nên gỡ trên hệ đầy đủ.",
"Ba hồ sơ triệu chứng đủ sáu phần, mọi giả thuyết có phép thử bác bỏ được, và người đổi bài không tìm được giả thuyết không kiểm được."),

(9,"Reproduce, reduce and instrument at the boundary","TH","Lesson 8",
"Ba kỹ năng làm cho quy trình ở lesson 8 chạy được trong thực tế. Tái hiện xác định: cố định đầu vào, cố định thời gian và ngẫu nhiên, cố định phiên bản; lỗi chỉ xuất hiện thỉnh thoảng thì phải tìm ra biến còn thay đổi chứ kết luận là lỗi ngẫu nhiên. Thu nhỏ: cắt dần đầu vào và cắt dần mã cho tới khi bỏ thêm một thứ nữa thì lỗi biến mất; trường hợp nhỏ nhất thường tự nó chỉ ra nguyên nhân. Thêm khả năng quan sát ở **ranh giới** chứ rải khắp nơi: ghi lại đầu vào và đầu ra tại mỗi ranh giới giữa hai thành phần, vì lỗi nằm ở chỗ hai bên hiểu khác nhau về hợp đồng. Nhật ký có cấu trúc và mã theo dõi để nối các dòng thuộc cùng một lần chạy. Ba loại lỗi hay gặp với dữ liệu và cách nhận ra từng loại: dữ liệu không đúng hình dạng, tài nguyên cạn, và thiếu quyền.",
"Tái hiện xác định một lỗi, thu nhỏ về trường hợp nhỏ nhất, và chứng minh nguyên nhân bằng quan sát ở ranh giới.",
"Tầng *phân tích*. Objective là truy từ triệu chứng về nguyên nhân bằng bằng chứng, kỹ năng nền cho mọi module sau. Kiểm bằng ba lỗi tiêm sẵn; đạt khi chứng minh đúng nguyên nhân ít nhất hai và trường hợp nhỏ nhất thật sự nhỏ.",
"Nhận một chương trình xử lý CSV có ba lỗi tiêm sẵn: một dòng sai định dạng, một tình huống hết chỗ trống trên đĩa mô phỏng, và một lỗi thiếu quyền. Với mỗi lỗi, tái hiện xác định, thu nhỏ đầu vào, thêm ghi nhật ký ở ranh giới, và nộp bảng giả thuyết có ít nhất ba dòng bị bác bỏ.",
"Rải lệnh in khắp mã thay vì đặt ở ranh giới · kết luận lỗi ngẫu nhiên khi chưa cố định biến · thu nhỏ bằng cách xoá mã tới khi không chạy nữa · sửa khi chưa tái hiện được.",
"Chứng minh đúng nguyên nhân ≥ 2/3 lỗi, mỗi lần có ≥ 3 giả thuyết bị bác bỏ bằng bằng chứng, và trường hợp nhỏ nhất dưới 20 dòng."),

(10,"Technical artifacts - README, runbook and postmortem","TH","Lesson 9",
"Bốn tài liệu mà mọi thành phần chạy trong sản xuất phải có, và mỗi tài liệu phục vụ một người đọc ở một thời điểm khác nhau. README phục vụ người mới: mục đích, kiến trúc một đoạn, cách cài, cách chạy và kiểm, và giới hạn đã biết. Tài liệu quyết định ở lesson 3 phục vụ người sửa kiến trúc về sau. Sổ tay vận hành phục vụ người trực lúc ba giờ sáng, nên cấu trúc phải theo đúng trình tự họ cần: cảnh báo nào, ảnh hưởng gì, chẩn đoán ra sao, giảm nhẹ thế nào, leo thang cho ai, và xác nhận đã hồi phục bằng cách nào. Phân tích sau sự cố phục vụ cả đội về sau: dòng thời gian, điều kiện góp phần, khoảng trống trong phát hiện, và hành động khắc phục có chủ. Nguyên tắc chung: viết cho người chưa có bối cảnh, và mọi từ viết tắt được định nghĩa ở chỗ người đọc gặp nó lần đầu.",
"Viết bộ bốn tài liệu cho một thành phần nhỏ, và người khác dùng được mà không phải hỏi.",
"Tầng *áp dụng*. Objective là sản phẩm viết theo chuẩn, đo bằng kết quả của người đọc. Kiểm bằng phép thử bàn giao; đạt khi người nhận chạy được và xử lý được tình huống trong sổ tay với số câu hỏi dưới ngưỡng.",
"Viết bốn tài liệu cho công cụ CSV ở lesson 9. Đưa cho một học viên chưa xem mã: họ cài, chạy, và xử lý một tình huống lỗi chỉ dựa vào sổ tay. Ghi lại mọi câu họ phải hỏi rồi sửa tài liệu theo danh sách đó.",
"Viết README cho chính mình đọc · sổ tay không có bước xác nhận đã hồi phục · phân tích sau sự cố quy về lỗi cá nhân · dùng từ viết tắt chưa định nghĩa.",
"Người nhận cài và chạy được, xử lý được tình huống theo sổ tay, và số câu hỏi phải hỏi dưới ngưỡng."),

(11,"Putting it together - a small CLI with contract, tests and logs","DA","Lesson 10",
"Bài dự án gộp toàn module: một công cụ dòng lệnh nạp tệp CSV, kiểm tra lược đồ, và ghi ra kết quả. Yêu cầu bắt buộc và mỗi yêu cầu đến từ một bài trước: phát biểu bài toán sáu phần theo lesson 1; ranh giới thành phần rõ theo lesson 2; một tài liệu quyết định theo lesson 3; lịch sử Git gồm commit nhỏ một mục đích theo lesson 7; **mã thoát đúng** để hệ gọi biết thành công hay thất bại; nhật ký có cấu trúc ở ranh giới theo lesson 9; phép kiểm đơn vị và phép kiểm tích hợp; và bộ bốn tài liệu theo lesson 10. Phép thử nghiệm thu là phép thử tiêm lỗi: giảng viên đưa năm tệp đầu vào hỏng theo năm cách, và công cụ phải phân loại đúng, thoát đúng mã, và ghi đủ để chẩn đoán mà không cần chạy lại.",
"Nộp một công cụ đạt tám yêu cầu, xử lý đúng năm loại đầu vào hỏng, và có bộ tài liệu dùng được.",
"Tầng *sáng tạo*. Bài dự án tổng hợp, đòi ghép tám yêu cầu rời thành một sản phẩm chạy được. Kiểm bằng phép thử tiêm lỗi cộng rà soát tám yêu cầu; đạt khi cả năm đầu vào hỏng được xử lý đúng và tám yêu cầu đều có bằng chứng.",
"Xây công cụ. Nộp qua yêu cầu hợp nhất. Giảng viên đưa năm tệp hỏng: thiếu cột, sai kiểu, bảng mã sai, dòng có dấu phân cách trong trường, và tệp rỗng. Với mỗi tệp, công cụ phải phân loại, thoát đúng mã, và nhật ký đủ để một người khác chẩn đoán.",
"Nuốt ngoại lệ rồi vẫn thoát mã không · ghi nhật ký dạng chuỗi tự do · nộp một commit duy nhất · bỏ tài liệu vì thấy công cụ nhỏ.",
"Năm đầu vào hỏng đều được phân loại đúng với mã thoát đúng, tám yêu cầu đều có bằng chứng, và một học viên khác chẩn đoán được cả năm chỉ bằng nhật ký."),

(12,"Delayed recall and the evidence habit","LT","Lesson 11",
"Bài chốt module, và nó đặt một thói quen dùng cho cả 416 bài còn lại. Ôn lại có khoảng cách: kiểm tra lại sau 1 ngày, 7 ngày và 30 ngày, vì nhớ ngay sau buổi học không dự đoán được việc nhớ sau một tháng. Phân biệt nhận ra với nhớ lại: đọc lại tài liệu thấy quen thuộc là nhận ra, và nó tạo cảm giác đã học xong mà không tương ứng với năng lực; phép kiểm thật là viết lại hoặc làm lại mà không nhìn. Ghi chú chín phần dùng suốt chương trình và lý do từng phần. Nhật ký lỗi cá nhân: mỗi lỗi ghi triệu chứng, nguyên nhân thật, và dấu hiệu nhận ra sớm lần sau; đây là tài liệu người học dùng lại nhiều nhất về sau. Thói quen bằng chứng: mọi khẳng định về hệ thống của mình phải dẫn được về một số đo, một nhật ký hoặc một phép kiểm, chứ dừng ở cảm nhận. Đây chính là cổng thứ tám trong tám cổng xuyên suốt.",
"Thiết lập được hệ ôn tập có khoảng cách và nhật ký lỗi, và đạt ngưỡng nhớ lại trên nội dung của module.",
"Tầng *hiểu*. Bài chốt, đo mức giữ lại chứ mở nội dung mới. Kiểm bằng bài nhớ lại có khoảng cách sau 14 ngày; đạt khi đúng ≥ 80% và lặp lại được thao tác chia đôi mà không nhìn hướng dẫn.",
"Dựng ghi chú chín phần cho cả 11 bài trước và nhật ký lỗi từ những lỗi đã gặp trong module. Đặt lịch ôn 1, 7 và 30 ngày. Sau 14 ngày, làm bài nhớ lại gồm 20 câu và thực hiện lại quy trình chia đôi ở lesson 6 mà không nhìn hướng dẫn.",
"Đọc lại tài liệu rồi tưởng đã nhớ · bỏ nhật ký lỗi vì thấy mất thời gian · ôn dồn một lần thay vì có khoảng cách · ghi chú chép lại slide.",
"Đạt ≥ 80% bài nhớ lại sau 14 ngày, và lặp lại được quy trình chia đôi không nhìn hướng dẫn."),
]

M2 = ("Python for Production", 13, 32, """| | |
|---|---|
| **Objective cấp module** | Viết Python có hợp đồng, có kiểm thử, đóng gói được, quan sát được, và chọn đúng mô hình đồng thời theo khối lượng công việc |
| **Tiền đề** | M1 |
| **Exit criterion** | Gói cài được, có chú thích kiểu, có CI xanh, môi trường tái tạo được trên máy khác; một dịch vụ bất đồng bộ không có tác vụ mồ côi, không phát tán không giới hạn, không rò bể kết nối, và phân biệt được hết giờ cục bộ với hạn chót đầu cuối |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 |
| **Chế độ hỏng** | Viết script chạy được trên máy mình rồi gọi đó là xong: không đóng gói, không kiểm thử, không đo, và chọn mô hình đồng thời theo lời khuyên trên mạng |""",
"""Python là công cụ mức `A` của cả chương trình: mọi module sau đều dùng nó để nạp dữ liệu, biến đổi, kiểm thử và vận hành. Nên module này dạy Python như ngôn ngữ xây sản phẩm chứ ngôn ngữ viết script.

Ba phần có thứ tự bắt buộc: hiểu mô hình đối tượng và vòng đời tài nguyên trước, đóng gói và kiểm thử sau, rồi mới tới đồng thời. Học đồng thời trước khi hiểu vòng đời tài nguyên là cách tạo ra lỗi không tái hiện được.""")

L2 = [
(13,"Names, objects and mutability","LT","Module 2: M1",
"Phần lớn lỗi khó hiểu của người mới học Python bắt nguồn từ việc nhầm tên với đối tượng. Gán không sao chép giá trị mà gắn một tên vào một đối tượng, nên hai tên có thể trỏ cùng một đối tượng và sửa qua tên này thì tên kia thấy. Phân biệt đồng nhất với bằng nhau, và vì sao hai thứ này khác nhau với đối tượng thay đổi được. Đối tượng thay đổi được và không thay đổi được: hệ quả trực tiếp là **giá trị mặc định của tham số hàm được tạo một lần khi định nghĩa hàm**, nên dùng danh sách rỗng làm mặc định là một trong những bẫy kinh điển. Sao chép nông và sao chép sâu, cùng chi phí của từng loại. Phạm vi tên và bao đóng: hàm lồng nhau bắt giữ tên chứ giá trị, nên vòng lặp tạo hàm cho kết quả bất ngờ nếu không hiểu điều này. Cách tự kiểm chứng mọi khẳng định trên bằng lệnh xem đồng nhất, thay vì tin lời giảng.",
"Dự đoán đúng kết quả của các đoạn mã có chia sẻ đối tượng thay đổi được, và giải thích bằng quan hệ tên với đối tượng.",
"Tầng *hiểu*. Bài mở module, nền cho mọi bài sau; chưa đòi viết sản phẩm. Kiểm bằng bài dự đoán viết trước khi chạy; đạt khi đúng ≥ 8/10 đoạn và giải thích được bằng tên và đối tượng chứ bằng mô tả hiện tượng.",
"Cho 10 đoạn mã ngắn về chia sẻ đối tượng, mặc định thay đổi được, sao chép nông và bao đóng trong vòng lặp. Viết dự đoán trước, chạy, đối chiếu. Với mỗi đoạn sai dự đoán, vẽ lại quan hệ tên và đối tượng bằng lệnh xem đồng nhất.",
"Dùng danh sách rỗng làm giá trị mặc định · nghĩ gán là sao chép · dùng so sánh bằng cho kiểm tra đồng nhất · sao chép nông rồi tưởng đã tách hẳn.",
"Dự đoán đúng ≥ 8/10 đoạn, và mỗi đoạn sai được giải thích lại bằng quan hệ tên với đối tượng."),

(14,"Iterators, generators and lazy evaluation","TH","Lesson 13",
"Đọc cả tệp vào bộ nhớ là cách viết chạy tốt trên tệp mẫu và chết trên tệp thật, nên đánh giá lười là kỹ thuật nền của mọi module xử lý dữ liệu về sau. Phân biệt đối tượng lặp được với bộ lặp: một cái tạo ra bộ lặp, một cái giữ trạng thái đang ở đâu; từ đó suy ra vì sao duyệt một bộ lặp hai lần thì lần hai rỗng. Hàm sinh là một máy trạng thái: mỗi lần gặp lệnh nhường thì dừng lại và giữ nguyên trạng thái cục bộ, lần gọi sau chạy tiếp từ đó. Hệ quả cho dữ liệu: xử lý theo dòng chảy dùng bộ nhớ không đổi bất kể kích thước đầu vào. Áp lực ngược tự nhiên: bên tiêu thụ quyết định nhịp, nên không có chuyện bên sản xuất dồn quá nhanh. Chuỗi hàm sinh nối nhau tạo thành một đường ống trong bộ nhớ, và đây là mô hình sẽ gặp lại ở tầng lớn hơn tại M18.",
"Viết lại một đoạn xử lý nạp toàn bộ thành dạng dòng chảy, và chứng minh bằng số đo rằng bộ nhớ không tăng theo kích thước đầu vào.",
"Tầng *áp dụng*. Objective là một phép biến đổi mã có kết quả đo được bằng bộ nhớ. Kiểm bằng cặp số đo trên ba kích thước đầu vào; đạt khi bản dòng chảy giữ bộ nhớ gần như không đổi.",
"Viết bản nạp toàn bộ xử lý một tệp CSV và đo bộ nhớ đỉnh trên tệp 10 MB, 200 MB và 2 GB. Viết lại bằng hàm sinh và đo lại. Vẽ hai đường. Nối ba hàm sinh thành một chuỗi và chứng minh bộ nhớ vẫn không đổi.",
"Gọi hàm chuyển thành danh sách ngay trong chuỗi nên mất tính lười · duyệt bộ lặp hai lần · đo bộ nhớ trung bình thay vì đỉnh · kết luận từ tệp mẫu quá nhỏ.",
"Bản dòng chảy giữ bộ nhớ đỉnh gần như không đổi qua cả ba kích thước, trong khi bản nạp toàn bộ tăng tuyến tính."),

(15,"Exceptions, resource lifetime and context managers","TH","Lesson 14",
"Hai lỗi vận hành phổ biến nhất trong mã xử lý dữ liệu đều nằm ở đây: nuốt ngoại lệ, và rò rỉ tài nguyên. Phân loại ngoại lệ và nguyên tắc bắt cụ thể chứ bắt chung: bắt mọi thứ rồi bỏ qua là cách biến một lỗi rõ ràng thành dữ liệu sai âm thầm. Nối chuỗi ngoại lệ để giữ nguyên nhân gốc khi dịch lỗi sang ngôn ngữ của tầng trên. Dịch lỗi ở ranh giới: bên trong dùng ngoại lệ chi tiết, ra tới ranh giới thì dịch sang lỗi có nghĩa với người gọi. Trình quản lý ngữ cảnh bảo đảm dọn dẹp chạy kể cả khi có ngoại lệ, và đây là cách duy nhất đúng để quản lý tệp, kết nối cơ sở dữ liệu và khoá. Tự viết trình quản lý ngữ cảnh cho một tài nguyên của mình. Nguyên tắc thông báo lỗi dùng được: nêu cái gì hỏng, ở đâu, với dữ liệu nào, và người đọc nên làm gì tiếp.",
"Viết mã xử lý lỗi không nuốt ngoại lệ và không rò rỉ tài nguyên, chứng minh bằng thí nghiệm gây lỗi giữa chừng.",
"Tầng *áp dụng*. Objective là hai tính chất kiểm được bằng thực nghiệm chứ bằng đọc mã. Kiểm bằng thí nghiệm gây lỗi; đạt khi không kết nối nào còn mở sau 100 lần lỗi và mọi lỗi đều lộ ra kèm nguyên nhân gốc.",
"Viết một hàm mở kết nối, xử lý, rồi đóng. Gây lỗi giữa chừng 100 lần và đếm số kết nối còn mở. Viết lại bằng trình quản lý ngữ cảnh và đếm lại. Dịch một ngoại lệ thấp tầng sang lỗi có nghĩa ở ranh giới, giữ nguyên nhân gốc, và kiểm bằng cách đọc dấu vết.",
"Bắt mọi ngoại lệ rồi bỏ qua · đóng tài nguyên trong nhánh thành công mà quên nhánh lỗi · dịch lỗi mà mất nguyên nhân gốc · thông báo lỗi chỉ ghi thất bại.",
"Sau 100 lần gây lỗi không còn kết nối nào mở, và mọi lỗi ở ranh giới đều giữ được nguyên nhân gốc trong dấu vết."),

(16,"CPython internals that change your decisions","LT","Lesson 15",
"Bốn chi tiết bên trong máy thực thi có ảnh hưởng thật tới quyết định thiết kế, phần còn lại thì không nên bận tâm ở mức này. Đếm tham chiếu cộng bộ dọn rác chu trình: đối tượng được giải phóng ngay khi không còn tham chiếu, nên vòng tham chiếu là chỗ duy nhất cần bộ dọn chu trình; hệ quả thực tế là giữ một tham chiếu quên xoá thì bộ nhớ không về. Cấp phát bộ nhớ theo khối nhỏ và vì sao bộ nhớ trả về hệ điều hành chậm hơn người ta tưởng. Khoá thông dịch toàn cục: chỉ một luồng chạy mã Python tại một thời điểm, **nhưng phát biểu thường gặp rằng luồng vô dụng là sai**, vì khoá được nhả trong lúc chờ vào ra và trong nhiều thư viện tính toán. Từ đó rút ra quy tắc chọn ở lesson 29 chứ chọn theo cảm tính. Mã byte ở mức khái niệm, đủ để biết vì sao một số phép viết nhanh hơn phép khác.",
"Giải thích bằng cơ chế vì sao luồng vẫn hữu ích cho khối lượng công việc thiên vào ra, và đo được để chứng minh.",
"Tầng *hiểu*. Objective là bác bỏ một hiểu lầm phổ biến bằng cơ chế cộng số đo. Kiểm bằng thí nghiệm hai loại khối lượng công việc; đạt khi số đo cho thấy đúng chiều và giải thích đúng vai trò của khoá.",
"Chạy cùng một tác vụ ở ba cấu hình một luồng, nhiều luồng và nhiều tiến trình, trên hai loại khối lượng công việc: một thiên CPU và một thiên vào ra. Lập bảng sáu ô. Giải thích từng ô bằng cơ chế khoá. Tạo một vòng tham chiếu và quan sát bộ nhớ không về cho tới khi bộ dọn chu trình chạy.",
"Kết luận luồng vô dụng trong Python · dùng nhiều tiến trình cho tác vụ thiên vào ra · bỏ qua chi phí khởi động tiến trình khi so · đo một lần rồi kết luận.",
"Bảng sáu ô có số đo thật, và giải thích đúng vì sao luồng thắng ở khối lượng công việc thiên vào ra."),

(17,"Packaging - project layout, build and reproducible environments","TH","Lesson 16",
"Script chạy được trên máy mình không phải phần mềm, và ranh giới giữa hai thứ nằm ở chỗ người khác chạy lại được. Bố cục dự án và cách Python tìm mô đun: đường dẫn tìm kiếm, nhập tuyệt đối so với nhập tương đối, và nhập vòng cùng cách phá vòng. Tệp cấu hình dự án và hậu trường dựng gói: khác biệt giữa gói nguồn và gói dựng sẵn. Môi trường ảo giải bài toán xung đột phụ thuộc, còn tệp khoá phiên bản giải bài toán tái tạo: **không khoá phiên bản thì bản dựng hôm nay khác bản dựng hôm qua**, đúng vấn đề ghim phiên bản sẽ gặp lại ở M20. Đánh số phiên bản theo ngữ nghĩa và ý nghĩa với người dùng gói. Cấu hình theo thứ tự ưu tiên và ranh giới biến môi trường; bí mật không bao giờ vào kho mã hay vào nhật ký, quy tắc này lặp lại ở M19 và M21.",
"Đóng gói một công cụ thành gói cài được với môi trường khoá phiên bản, và người khác tái tạo được trên máy trống.",
"Tầng *áp dụng*. Objective là tiêu chí *clone, một lệnh, cùng kết quả* ở mức gói. Kiểm bằng phép thử tái tạo do người khác chạy; đạt khi họ cài và chạy được mà không phải sửa gì.",
"Chuyển công cụ CSV ở lesson 11 thành gói có tệp cấu hình dự án. Tạo môi trường ảo và khoá phiên bản. Dựng gói nguồn và gói dựng sẵn. Đưa cho một học viên khác cài trên máy trống từ gói dựng sẵn, chạy, và ghi lại mọi chỗ họ phải hỏi.",
"Không khoá phiên bản · để cấu hình đường dẫn tuyệt đối của máy mình · đặt bí mật trong tệp cấu hình rồi nộp vào kho · nhập tương đối lung tung gây nhập vòng.",
"Người khác cài từ gói dựng sẵn và chạy được trên máy trống mà không phải sửa gì, và môi trường tái tạo cho cùng danh sách phiên bản."),

(18,"Type hints and validation at the boundary","TH","Lesson 17",
"Chú thích kiểu không làm chương trình chạy nhanh hơn, nó làm lỗi lộ ra sớm hơn và làm mã đọc được mà không phải đoán. Cú pháp đủ dùng: kiểu hợp, kiểu tuỳ chọn, kiểu tổng quát cho vùng chứa, và giao thức cho kiểu vịt có kiểm tra. Bộ kiểm kiểu tĩnh chạy trong tích hợp liên tục và ngưỡng chặn. Ranh giới quan trọng và hay bị nhầm: **chú thích kiểu là kiểm ở thời điểm dịch, không kiểm dữ liệu lúc chạy**; dữ liệu từ tệp, từ mạng hay từ cơ sở dữ liệu phải xác thực lúc chạy tại ranh giới nhận. Xác thực ở ranh giới chứ rải khắp nơi: vào tới trong thì dữ liệu đã đúng hình dạng và mã bên trong không phải kiểm lại. Lớp dữ liệu để mô tả bản ghi có cấu trúc thay vì dùng từ điển, và vì sao điều đó quan trọng với mã xử lý dữ liệu: từ điển sai khoá chỉ lộ ra lúc chạy, còn lớp dữ liệu lộ ra lúc kiểm.",
"Thêm chú thích kiểu cho một gói tới mức bộ kiểm tĩnh sạch, và xác thực dữ liệu lúc chạy ở đúng ranh giới.",
"Tầng *áp dụng*. Objective gồm hai cơ chế khác nhau mà người học hay gộp làm một. Kiểm bằng bộ kiểm tĩnh cộng thí nghiệm dữ liệu bẩn; đạt khi bộ kiểm sạch và dữ liệu sai hình dạng bị chặn ngay tại ranh giới.",
"Thêm chú thích kiểu cho gói ở lesson 17 tới khi bộ kiểm tĩnh sạch. Thêm xác thực lúc chạy tại ranh giới đọc tệp. Đưa vào 10 bản ghi sai hình dạng và chứng minh cả 10 bị chặn ở ranh giới với thông báo nêu rõ trường nào sai. Chứng minh mã bên trong không còn kiểm lại kiểu.",
"Tưởng chú thích kiểu kiểm được dữ liệu lúc chạy · xác thực rải khắp mã · dùng từ điển cho bản ghi có cấu trúc · tắt bộ kiểm tĩnh vì nhiều cảnh báo.",
"Bộ kiểm tĩnh sạch, 10 bản ghi sai đều bị chặn tại ranh giới với thông báo nêu đúng trường, và mã bên trong không kiểm lại kiểu."),

(19,"Testing - unit, integration, property and contract","TH","Lesson 18",
"Bốn loại phép kiểm trả lời bốn câu hỏi khác nhau, và dùng một loại cho mọi việc là cách vừa chậm vừa không bắt được lỗi. Phép kiểm đơn vị kiểm một đơn vị logic, nhanh, chạy mọi lúc. Phép kiểm tích hợp kiểm hai thành phần nói chuyện đúng với nhau, và đây là nơi bắt phần lớn lỗi thật trong mã dữ liệu. Phép kiểm tính chất sinh đầu vào ngẫu nhiên và kiểm một bất biến luôn đúng, rất hợp với mã biến đổi dữ liệu vì nó tìm ra ca biên mà con người không nghĩ ra. Phép kiểm hợp đồng kiểm hai bên vẫn hiểu giống nhau về giao diện. Bộ thay thế và ranh giới đặt chúng: chỉ thay thế ở ranh giới hệ ngoài, thay thế bên trong là tự kiểm mã giả của mình. Tính xác định: cố định thời gian và ngẫu nhiên, dùng thư mục tạm; phép kiểm chạy lúc được lúc không thì tệ hơn không có. Độ phủ không đồng nghĩa chất lượng.",
"Viết đủ bốn loại phép kiểm cho một gói, và chứng minh phép kiểm tính chất bắt được ca biên mà phép kiểm đơn vị bỏ sót.",
"Tầng *áp dụng*. Objective đòi chọn đúng loại phép kiểm cho từng mục tiêu, chứ tăng độ phủ. Kiểm bằng bài tiêm lỗi; đạt khi bộ kiểm bắt được ít nhất bốn trong năm lỗi và phép kiểm tính chất bắt ít nhất một ca mà phép kiểm đơn vị bỏ sót.",
"Viết cả bốn loại phép kiểm cho gói ở lesson 18. Giảng viên tiêm năm lỗi vào mã. Chạy bộ kiểm và ghi lỗi nào bị bắt bởi loại nào. Cố định thời gian và ngẫu nhiên, chạy bộ kiểm 20 lần liên tiếp và chứng minh kết quả không đổi.",
"Thay thế cả thành phần bên trong · viết phép kiểm phụ thuộc thời gian thật · chạy theo độ phủ · bỏ phép kiểm tích hợp vì chậm.",
"Bộ kiểm bắt ≥ 4/5 lỗi tiêm, phép kiểm tính chất bắt ≥ 1 ca mà phép kiểm đơn vị bỏ sót, và 20 lần chạy cho kết quả giống nhau."),

(20,"Structured logging, correlation and actionable errors","TH","Lesson 19",
"Nhật ký là thứ duy nhất còn lại khi sự cố đã qua, nên thiết kế nhật ký là thiết kế khả năng chẩn đoán về sau. Nhật ký có cấu trúc thay vì chuỗi tự do: có cấu trúc thì truy vấn và tổng hợp được, còn chuỗi tự do thì chỉ đọc mắt được. Bốn mức và quy tắc dùng từng mức, cùng lý do để mức gỡ lỗi chạy trong sản xuất là cách làm hoá đơn tăng mà không ai đọc. Mã theo dõi nối mọi dòng thuộc cùng một lần chạy hoặc cùng một bản ghi; đây là cơ chế sẽ dùng lại xuyên suốt tới M21 để truy ngược một bản ghi sai về lô nạp sinh ra nó. Ghi cái gì ở ranh giới: đầu vào tóm tắt, quyết định đã lấy, và kết quả. Không ghi bí mật và không ghi dữ liệu cá nhân, quy tắc nối tới M21. Thông báo lỗi dùng được nêu bốn thứ: cái gì hỏng, ở đâu, với dữ liệu nào, và nên làm gì.",
"Dựng nhật ký có cấu trúc kèm mã theo dõi, và truy được toàn bộ đường đi của một bản ghi chỉ bằng mã đó.",
"Tầng *áp dụng*. Objective là một thiết kế kiểm được bằng phép truy ngược thật. Kiểm bằng bài truy ngược; đạt khi truy được đủ đường đi của bản ghi bằng một truy vấn theo mã theo dõi.",
"Thêm nhật ký có cấu trúc và mã theo dõi vào gói. Chạy trên 10.000 bản ghi trong đó có 3 bản lỗi. Với mỗi bản lỗi, truy toàn bộ đường đi chỉ bằng mã theo dõi và dựng lại chuyện đã xảy ra. Kiểm nhật ký không chứa bí mật bằng một phép quét.",
"Ghi nhật ký dạng chuỗi tự do · không có mã theo dõi · để mức gỡ lỗi trong sản xuất · ghi cả bản ghi đầy đủ vào nhật ký gồm cả dữ liệu cá nhân.",
"Truy được đủ đường đi của cả 3 bản lỗi bằng một truy vấn theo mã theo dõi, và phép quét không tìm thấy bí mật trong nhật ký."),

(21,"Profiling before optimising","TH","Lesson 20",
"Tối ưu dựa trên phỏng đoán là cách tốn thời gian vào chỗ không quan trọng, nên quy tắc không thoả hiệp là **đo trước khi sửa**. Ba loại đo cho ba loại nút thắt: đo CPU theo hàm để biết thời gian tiêu ở đâu, đo bộ nhớ theo dòng để tìm chỗ giữ dữ liệu, và đo vào ra để biết đang chờ đĩa hay chờ mạng. Đo lấy mẫu so với đo có dụng cụ: cái đầu nhẹ và dùng được trong sản xuất, cái sau chi tiết hơn nhưng làm chương trình chậm nên số đo lệch. Cách chạy so sánh đúng: có giai đoạn khởi động, lặp nhiều lần, có mốc so sánh, và cố định dữ liệu; ba cách làm số đo vô nghĩa gồm đầu vào quá nhỏ, bộ nhớ đệm đã ấm, và không lặp. Nguyên tắc rút ra và dùng lại ở M18: sửa nút thắt lớn nhất, đo lại, rồi mới sang nút thắt kế tiếp; sửa nhiều chỗ cùng lúc thì không biết chỗ nào có tác dụng.",
"Định vị nút thắt của một chương trình bằng số đo, sửa đúng nó, và định lượng phần cải thiện.",
"Tầng *phân tích*. Objective là truy từ tổng thời gian về một hàm cụ thể bằng dữ liệu đo. Kiểm bằng cặp số đo trước sau; đạt khi định vị đúng nút thắt và cải thiện đo được mà kết quả không đổi.",
"Nhận một chương trình xử lý dữ liệu chạy chậm. Đo CPU, bộ nhớ và vào ra. Viết dự đoán nút thắt trước khi đo, rồi đối chiếu. Sửa đúng một chỗ, đo lại, ghi mức cải thiện. Chạy lại bộ kiểm để chứng minh kết quả không đổi. Cố ý chạy một phép so sánh sai cách và chỉ ra nó sai ở đâu.",
"Tối ưu theo cảm giác · sửa nhiều chỗ cùng lúc · so sánh không có giai đoạn khởi động · tối ưu một hàm chiếm 2% tổng thời gian.",
"Định vị đúng nút thắt bằng số đo, cải thiện có số, bộ kiểm vẫn xanh, và chỉ ra được chỗ sai của phép so sánh sai cách."),

(22,"Threads - shared memory, races and locks","TH","Lesson 21",
"Luồng dùng chung bộ nhớ, nên nhanh khi chia sẻ dữ liệu và nguy hiểm vì hai luồng có thể sửa cùng một chỗ. Điều kiện tranh đoạt: kết quả phụ thuộc vào thứ tự thực thi, nên chương trình chạy đúng 99 lần và sai lần thứ 100, và đây là loại lỗi khó tái hiện nhất. Vùng tranh chấp và khoá; khoá chết khi hai luồng giữ chéo nhau và chờ nhau, cùng bốn điều kiện cần để nó xảy ra. Thao tác nguyên tử và vì sao một phép tăng biến đơn giản không nguyên tử. Hàng đợi có giới hạn là cách chia việc giữa các luồng an toàn hơn chia sẻ biến, vì nó gói việc đồng bộ vào một chỗ. Khi nào luồng là lựa chọn đúng: khối lượng công việc thiên vào ra, theo đúng kết luận đã đo ở lesson 16. Tắt có kiểm soát: luồng phải nhận được tín hiệu dừng và kết thúc công việc đang dở chứ bị cắt ngang.",
"Tái hiện được một điều kiện tranh đoạt một cách xác định và sửa bằng cơ chế đồng bộ đúng.",
"Tầng *phân tích*. Objective đòi biến một lỗi ngẫu nhiên thành lỗi tái hiện được, kỹ năng khó và dùng lại ở M5. Kiểm bằng bài tái hiện cộng sửa; đạt khi tái hiện được 10/10 lần trước khi sửa và 0/1000 lần sau khi sửa.",
"Viết một bộ đếm dùng chung cho 8 luồng và chứng minh kết quả sai. Tăng khả năng tái hiện bằng cách chèn điểm dừng, đạt 10/10 lần sai. Sửa bằng khoá, chạy 1000 lần và xác nhận không sai lần nào. Tạo một khoá chết có chủ ý, chẩn đoán và sửa bằng cách sắp thứ tự lấy khoá.",
"Kết luận lỗi ngẫu nhiên nên bỏ qua · thêm khoá khắp nơi rồi mất hết tác dụng của nhiều luồng · dùng luồng cho tác vụ thiên CPU · cắt ngang luồng thay vì báo dừng.",
"Tái hiện sai 10/10 lần trước khi sửa, 0/1000 lần sau khi sửa, và chẩn đoán được khoá chết bằng bốn điều kiện."),

(23,"Processes - isolation, serialization and cost","TH","Lesson 22",
"Tiến trình có bộ nhớ riêng, nên không có điều kiện tranh đoạt trên biến dùng chung, đổi lại mọi thứ truyền qua lại phải tuần tự hoá. Ba chi phí phải tính trước khi chọn: thời gian khởi động một tiến trình, bộ nhớ nhân lên theo số tiến trình, và chi phí tuần tự hoá dữ liệu qua lại. Hệ quả thực tế hay bị bất ngờ: chia một việc nhỏ cho nhiều tiến trình có thể **chậm hơn** làm tuần tự, vì chi phí truyền lớn hơn phần tiết kiệm. Khi nào tiến trình là lựa chọn đúng: khối lượng công việc thiên CPU, theo bảng đo ở lesson 16. Hồ tiến trình và cách chia việc theo khối thay vì theo từng phần tử để giảm số lần truyền. Điều gì không truyền được qua ranh giới tiến trình và cách xử lý. Tắt có kiểm soát với hồ tiến trình: tiến trình con phải được dừng sạch, nếu không thì chúng thành tiến trình mồ côi.",
"Chọn giữa tiến trình và tuần tự cho một khối lượng công việc cho trước, dẫn bằng số đo gồm cả chi phí truyền.",
"Tầng *đánh giá*. Objective đòi cân chi phí song song với phần tiết kiệm, chứ mặc định song song là nhanh. Kiểm bằng bảng ba kích thước công việc; đạt khi chỉ ra đúng điểm giao mà dưới đó tuần tự thắng.",
"Chạy cùng phép tính thiên CPU ở ba kích thước dữ liệu, mỗi kích thước ở hai chế độ tuần tự và nhiều tiến trình. Đo thời gian và bộ nhớ. Tìm điểm giao. Đổi cách chia từ từng phần tử sang theo khối và đo lại phần cải thiện. Giết tiến trình chính và kiểm tiến trình con có mồ côi không.",
"Song song hoá mọi thứ · chia theo từng phần tử · bỏ qua bộ nhớ khi tăng số tiến trình · để tiến trình con mồ côi khi tiến trình chính chết.",
"Bảng ba kích thước nhân hai chế độ đủ thời gian và bộ nhớ, chỉ ra đúng điểm giao, và không còn tiến trình mồ côi sau khi giết tiến trình chính."),

(24,"Asyncio - the event loop, cancellation and timeouts","TH","Lesson 23",
"Mô hình thứ ba, hợp nhất với khối lượng công việc có rất nhiều thao tác chờ mạng cùng lúc. Vòng lặp sự kiện chạy trên một luồng và chuyển qua lại giữa các tác vụ ở những điểm chờ; nên hàng nghìn kết nối đồng thời không tốn hàng nghìn luồng. Chi tiết quyết định thành bại: **một lời gọi chặn nằm trong hàm bất đồng bộ sẽ khoá cả vòng lặp**, nên mọi thứ khác đứng im, và đây là lỗi phổ biến nhất khi mới dùng. Cách phát hiện lời gọi chặn và cách đẩy nó sang luồng riêng. Huỷ bỏ là công dân hạng nhất: tác vụ phải xử lý được việc bị huỷ giữa chừng và dọn dẹp tài nguyên. Hết giờ đặt ở mọi lời gọi ra ngoài, không có ngoại lệ, vì không đặt là chờ vô hạn. Giới hạn đồng thời bằng cờ hiệu có giới hạn để không mở 10.000 kết nối cùng lúc và làm sập bên kia.",
"Viết một trình thu thập bất đồng bộ có giới hạn đồng thời, hết giờ và huỷ bỏ đúng, không có lời gọi chặn nào trong vòng lặp.",
"Tầng *áp dụng*. Objective gồm ba cơ chế bắt buộc kiểm được bằng thực nghiệm. Kiểm bằng ba phép thử; đạt khi không lời gọi chặn nào lọt, hết giờ kích hoạt đúng, và huỷ bỏ dọn sạch tài nguyên.",
"Viết trình thu thập gọi 500 địa chỉ với giới hạn 20 kết nối đồng thời. Cố ý chèn một lời gọi chặn và đo tác động lên toàn vòng lặp, rồi sửa bằng cách đẩy sang luồng riêng. Đặt hết giờ và kiểm nó kích hoạt. Huỷ toàn bộ giữa chừng và chứng minh mọi kết nối được đóng.",
"Gọi hàm chặn trong hàm bất đồng bộ · không đặt hết giờ · mở không giới hạn kết nối · bỏ qua việc dọn dẹp khi bị huỷ.",
"Không lời gọi chặn nào trong vòng lặp, hết giờ kích hoạt đúng ngưỡng, và sau khi huỷ thì mọi kết nối đã đóng."),

(25,"Coroutine, task and future - the state model","TH","Lesson 24",
"Bài mở phần bất đồng bộ sâu bằng việc tách bốn thứ hay bị gọi chung là tác vụ. Hàm hiệp trình là hàm được khai báo bất đồng bộ; gọi nó **không chạy gì cả**, chỉ tạo ra một đối tượng hiệp trình, và quên chờ nó là nguồn của lỗi im lặng đầu tiên mà người mới gặp. Đối tượng chờ được là bất cứ thứ gì đặt sau từ khoá chờ. Tác vụ là một hiệp trình đã được giao cho vòng lặp sự kiện chạy, nên nó có vòng đời độc lập. Tương lai là chỗ giữ kết quả chưa có. Năm trạng thái phải truy được: vừa tạo, đang chạy, đang tạm dừng, đã xong, và đã bị huỷ; phân biệt đã xong vì trả kết quả, vì ném ngoại lệ, và vì bị huỷ. Ngoại lệ trong một tác vụ không ai chờ thì bị nuốt tới lúc chương trình kết thúc mới in ra. Liệt kê tác vụ đang sống là công cụ chẩn đoán chính.",
"Truy được trạng thái của một tác vụ qua đủ năm giai đoạn và chỉ ra hai cách một lỗi bị nuốt.",
"Tầng *phân tích*. Objective đòi quan sát trạng thái thời gian chạy chứ đọc tài liệu. Kiểm bằng bài truy trạng thái; đạt khi năm trạng thái được quan sát bằng công cụ và hai ca lỗi bị nuốt được tái hiện.",
"Viết chương trình tạo bốn tác vụ: một chạy xong, một ném ngoại lệ, một bị huỷ, một treo. Sau mỗi bước, liệt kê tác vụ đang sống và ghi trạng thái từng cái. Tái hiện hai ca lỗi bị nuốt: gọi hàm hiệp trình mà không chờ, và tạo tác vụ rồi không ai lấy kết quả. Bật chế độ gỡ lỗi của thư viện bất đồng bộ và ghi lại cảnh báo nó đưa ra.",
"Gọi hàm hiệp trình mà quên chờ · tạo tác vụ rồi không giữ tham chiếu · nhầm đối tượng hiệp trình với tác vụ đang chạy · không bao giờ liệt kê tác vụ đang sống.",
"Năm trạng thái được quan sát bằng công cụ, và hai ca lỗi bị nuốt được tái hiện cùng chỉ ra cách phát hiện."),

(26,"Structured concurrency - TaskGroup, ownership and cancellation safety","TH","Lesson 25",
"Tác vụ tạo ra rồi bỏ mặc là nguồn của rò rỉ và của lỗi biến mất, nên bài này đặt ra một kỷ luật sở hữu. Đồng thời có cấu trúc buộc mọi tác vụ con thuộc một phạm vi cha, và **phạm vi cha không được rời khỏi khi còn tác vụ con đang chạy**. Bốn bảo đảm kéo theo: một tác vụ con hỏng thì các anh em bị huỷ; ngoại lệ được gom lại chứ mất; phạm vi chờ dọn dẹp xong mới thoát; và không còn tác vụ mồ côi khi tắt. Huỷ bỏ an toàn là phần khó: tín hiệu huỷ tới ở một điểm chờ bất kỳ, nên mọi tài nguyên phải nằm trong khối dọn dẹp hoặc trình quản lý ngữ cảnh bất đồng bộ; **nuốt tín hiệu huỷ để chạy nốt là lỗi nghiêm trọng** vì nó làm việc tắt treo. Dọn dẹp trong lúc bị huỷ cần được che chắn để bản thân nó không bị huỷ giữa chừng.",
"Dựng phạm vi đồng thời có cấu trúc đạt bốn bảo đảm và chứng minh không còn tác vụ mồ côi khi tắt.",
"Tầng *áp dụng*. Objective có tiêu chí nghiệm thu đếm được là số tác vụ còn sống và số tài nguyên chưa đóng. Kiểm bằng ba kịch bản tắt; đạt khi số tác vụ còn sống bằng không và số kết nối rò bằng không ở cả ba.",
"Viết một dịch vụ mở 50 tác vụ con trong một phạm vi có cấu trúc. Chạy ba kịch bản: một tác vụ con ném ngoại lệ, phạm vi bị huỷ từ ngoài, và nhận tín hiệu tắt. Sau mỗi kịch bản, đếm tác vụ còn sống và bộ mô tả tệp còn mở. Viết một bản không có cấu trúc để so và định lượng số tác vụ mồ côi.",
"Tạo tác vụ rời rồi quên · nuốt tín hiệu huỷ để chạy nốt · dọn dẹp mà không che chắn nên bị huỷ giữa chừng · rời phạm vi khi tác vụ con còn chạy.",
"Số tác vụ còn sống và số kết nối rò đều bằng không ở cả ba kịch bản, và bản không có cấu trúc được định lượng số tác vụ mồ côi."),

(27,"End-to-end deadlines and backpressure","TH","Lesson 26",
"Hai cơ chế giữ một dịch vụ bất đồng bộ không sụp dưới tải, và cả hai đều bị hiểu nhầm là hết giờ. Hết giờ cục bộ đặt cho từng lời gọi; hạn chót đầu cuối là tổng ngân sách cho cả yêu cầu. Khác biệt có hậu quả cụ thể: ba chặng mỗi chặng hết giờ 10 giây cho phép một yêu cầu chạy 30 giây, và nếu mỗi chặng còn thử lại thì con số nhân lên nữa; **hết giờ cục bộ cộng thử lại tạo ra khuếch đại thời gian chờ**. Cách đúng là truyền ngân sách còn lại xuống từng chặng, và chặng nào thấy ngân sách cạn thì bỏ sớm thay vì thử. Áp lực ngược giới hạn phía sản xuất bằng hàng đợi có giới hạn, cờ hiệu và bể kết nối có giới hạn; khi đầy thì phải chọn tường minh một trong bốn hành vi là từ chối, chờ, loại bớt, hoặc giảm chất lượng. Giữ một kết nối qua một điểm chờ dài làm cạn bể, là chế độ hỏng đặc trưng.",
"Cài truyền hạn chót đầu cuối và áp lực ngược, chứng minh yêu cầu không vượt ngân sách và bể không bị cạn.",
"Tầng *áp dụng*. Objective có hai tiêu chí nghiệm thu đo được dưới tải. Kiểm bằng phép thử tải có chặng chậm; đạt khi phân vị 99 của thời gian yêu cầu nằm trong ngân sách và không lần nào bể kết nối cạn.",
"Dựng dịch vụ ba chặng, mỗi chặng gọi một phụ thuộc có thể chậm. Cài bản chỉ có hết giờ cục bộ cộng thử lại, chạy tải với một chặng chậm, và đo phân vị 99. Cài bản truyền hạn chót và đo lại. Thêm hàng đợi có giới hạn cùng bể kết nối có giới hạn, chọn tường minh hành vi khi đầy. Tạo một đoạn giữ kết nối qua điểm chờ dài và quan sát bể cạn.",
"Chỉ đặt hết giờ cục bộ rồi tin yêu cầu có giới hạn · thử lại ở mọi chặng mà không có ngân sách chung · để hàng đợi không giới hạn · giữ kết nối qua một điểm chờ dài.",
"Phân vị 99 của thời gian yêu cầu nằm trong ngân sách hạn chót, và không lần nào bể kết nối cạn dưới tải."),

(28,"Async failure injection - six failure modes","TH","Lesson 27",
"Bài khép phần bất đồng bộ bằng cách tiêm lỗi có chủ ý, vì sáu chế độ hỏng dưới đây đều không lộ ra khi chạy thuận lợi. Vòng lặp trễ vì một lời gọi chặn hoặc một vòng tính toán dài: bằng chứng là số đo độ trễ của vòng lặp, phòng thủ là đẩy sang luồng hoặc tiến trình riêng. Tác vụ mồ côi vì tạo rồi bỏ: bằng chứng là danh sách tác vụ còn sống lúc tắt. Rò rỉ khi huỷ vì dọn dẹp không chạy: bằng chứng là số bộ mô tả tệp tăng dần. Khuếch đại thời gian chờ theo lesson 27. Cạn bể kết nối. Bão thử lại khi nhiều tác vụ cùng thử lại một lúc: bằng chứng là đỉnh tải đồng bộ, phòng thủ là ngân sách thử lại cùng nhiễu ngẫu nhiên. **Mỗi chế độ hỏng phải có một phép thử tự động tái hiện được**, nếu không nó sẽ quay lại. Sáu tình huống tiêm gồm lời gọi chặn, ổ cắm treo, ngoại lệ trong tác vụ, huỷ giữa một giao dịch, hàng đợi đầy, và tín hiệu tắt.",
"Tái hiện sáu chế độ hỏng bằng phép thử tự động và chứng minh phòng thủ tương ứng có hiệu lực.",
"Tầng *đánh giá*. Objective tổng hợp bốn bài trước thành một hệ phòng vệ có bằng chứng. Kiểm bằng sáu phép thử tiêm; đạt khi cả sáu tái hiện được tự động và ít nhất năm có phòng thủ chứng minh bằng số đo trước sau.",
"Viết sáu phép thử tiêm lỗi chạy tự động. Với mỗi cái, ghi lại bằng chứng quan sát được trước khi phòng thủ, áp phòng thủ, rồi đo lại. Chạy phép thử tắt có kiểm soát nhận tín hiệu kết thúc và chứng minh mọi giao dịch đang dở hoặc hoàn tất hoặc quay lui. Lập bảng sáu hàng gồm cơ chế, bằng chứng và phòng thủ.",
"Thử bằng tay một lần rồi coi là xong · huỷ giữa một giao dịch mà không định nghĩa ranh giới công bố · đo phòng thủ mà không đo trước · bỏ tình huống tín hiệu tắt vì khó tái hiện.",
"Sáu phép thử tiêm chạy tự động, ≥ 5 phòng thủ có số đo trước sau, và tắt có kiểm soát không để giao dịch dở dang."),

(29,"Choosing a concurrency model from the workload","LT","Lesson 28",
"Bài chốt phần đồng thời, và nó biến ba bài trước thành một quy tắc quyết định. Ba câu hỏi theo thứ tự: công việc này chờ hay tính, có cần chia sẻ trạng thái không, và quy mô đồng thời là bao nhiêu. Bảng quyết định: thiên CPU thì nhiều tiến trình; thiên vào ra với vài chục đồng thời thì luồng đủ và đơn giản hơn; thiên vào ra với hàng nghìn đồng thời thì bất đồng bộ. Lựa chọn thứ tư hay bị bỏ qua và thường đúng nhất: **không đồng thời**, vì mã tuần tự dễ đọc và dễ gỡ hơn nhiều, và phần lớn công việc dữ liệu theo lô không cần đồng thời trong tiến trình mà cần chia việc ở tầng trên, đúng cách M14 và M18 làm. Ba dấu hiệu cho thấy đã chọn sai. Mọi kết luận ở bài này phải dẫn về bảng số đo của chính mình ở lesson 16, 22, 23 và 24 chứ về lời khuyên chung.",
"Chọn mô hình đồng thời cho bốn khối lượng công việc cho trước, mỗi lần dẫn về một số đo đã tự đo.",
"Tầng *đánh giá*. Objective đòi áp một quy tắc quyết định có bằng chứng, chuẩn bị cho mọi module vận hành sau. Kiểm bằng bốn khối lượng công việc trong đó ít nhất một không nên đồng thời; đạt khi chọn đúng ít nhất ba và nhận ra trường hợp không nên đồng thời.",
"Cho bốn khối lượng công việc. Với mỗi cái, chọn mô hình và dẫn một số đo từ lesson 16, 22, 23 hoặc 24 làm căn cứ. Với khối lượng công việc không nên đồng thời, ước lượng phần phức tạp thêm vào so với phần thời gian tiết kiệm được.",
"Chọn theo mô hình đang thịnh hành · dùng bất đồng bộ cho việc thiên CPU · bỏ qua phương án không đồng thời · dẫn lời khuyên thay vì dẫn số đo.",
"Chọn đúng ≥ 3/4 khối lượng công việc với số đo dẫn chứng, và nhận ra đúng trường hợp không nên đồng thời."),

(30,"A resilient worker - retry, backoff, idempotency and shutdown","TH","Lesson 29",
"Bài ghép mọi thứ của module thành mẫu sẽ dùng lại ở M14B, M16 và M21. Bốn tính chất của một tiến trình xử lý đáng tin. Thử lại có lùi theo hàm mũ và nhiễu ngẫu nhiên: thử lại ngay lập tức làm sự cố nặng thêm vì mọi tiến trình cùng thử lại một lúc; nhiễu ngẫu nhiên phá sự đồng pha đó. Chỉ thử lại lỗi tạm thời, còn lỗi dữ liệu thì thử lại vô ích và phải tách ra. Khoá bất biến: vì thử lại nghĩa là cùng một việc chạy hai lần, nên ghi phải cho cùng kết quả khi lặp; đây là nguyên tắc nền của cả chương trình và sẽ quay lại ở M14 và M16. Hàng đợi có giới hạn giữa các giai đoạn để tạo áp lực ngược thay vì dồn vô hạn. Tắt có kiểm soát: nhận tín hiệu, ngừng nhận việc mới, hoàn tất việc đang dở trong hạn, rồi thoát với mã đúng.",
"Viết một tiến trình xử lý đạt bốn tính chất và chứng minh bằng thí nghiệm giết tiến trình rằng không mất và không trùng việc.",
"Tầng *sáng tạo*. Objective đòi ghép bốn cơ chế rời thành một mẫu chạy được dưới sự cố. Kiểm bằng thí nghiệm giết tiến trình 20 lần; đạt khi đối soát khớp tuyệt đối và tắt có kiểm soát hoàn tất trong hạn.",
"Viết tiến trình xử lý đọc từ hàng đợi có giới hạn và ghi vào tệp kết quả có khoá bất biến. Tiêm lỗi tạm thời và lỗi dữ liệu, chứng minh chỉ loại đầu được thử lại. Giết tiến trình 20 lần ở các thời điểm ngẫu nhiên, khởi động lại, và đối soát kết quả với đầu vào. Gửi tín hiệu dừng và đo thời gian tắt.",
"Thử lại mọi loại lỗi · thử lại ngay không lùi và không nhiễu · ghi không bất biến rồi sinh trùng khi thử lại · bỏ qua tín hiệu dừng.",
"Sau 20 lần giết và khởi động lại, đối soát khớp tuyệt đối; lỗi dữ liệu không bị thử lại; và tắt có kiểm soát xong trong hạn."),

(31,"Continuous integration for a Python package","TH","Lesson 30",
"Tích hợp liên tục biến kỷ luật cá nhân thành ràng buộc của cả kho, và bài này dựng bộ khung dùng cho mọi module sau. Các bước tối thiểu theo thứ tự chạy nhanh trước: định dạng và soát lỗi tĩnh, kiểm kiểu, phép kiểm đơn vị, phép kiểm tích hợp, dựng gói, và quét bí mật. Cửa chặn hợp nhất: nhánh chính chỉ nhận thay đổi khi mọi bước xanh, nếu không thì quy trình chỉ là trang trí. Chạy trên nhiều phiên bản Python nếu gói tuyên bố hỗ trợ nhiều phiên bản. Bộ nhớ đệm phụ thuộc để vòng lặp phản hồi đủ nhanh, vì quy trình chạy 20 phút là quy trình người ta tìm cách vòng qua. Quét bí mật cả lịch sử kho chứ chỉ mã hiện tại, vì xoá ở lần nộp sau không xoá được ở lần nộp trước. Mã thoát và thông báo hỏng phải nói được hỏng ở bước nào, nối lại nguyên tắc thông báo lỗi ở lesson 15.",
"Dựng quy trình tích hợp liên tục sáu bước có cửa chặn hợp nhất, với thời gian phản hồi dưới ngưỡng.",
"Tầng *áp dụng*. Objective là một cấu hình có hai ràng buộc đo được là tính chặn và thời gian. Kiểm bằng phép thử nộp mã hỏng; đạt khi mọi loại hỏng đều bị chặn và thời gian chạy dưới ngưỡng.",
"Dựng quy trình sáu bước cho gói. Bật cửa chặn hợp nhất. Nộp năm yêu cầu hợp nhất hỏng theo năm cách khác nhau, mỗi cách ứng với một bước, và xác nhận cả năm bị chặn ở đúng bước. Bật bộ nhớ đệm phụ thuộc và đo thời gian trước sau.",
"Cho phép hợp nhất khi quy trình đỏ · đặt bước chậm lên đầu · không quét lịch sử kho · thông báo hỏng không nói hỏng ở bước nào.",
"Năm yêu cầu hỏng đều bị chặn ở đúng bước, thời gian chạy dưới ngưỡng sau khi bật bộ nhớ đệm, và cửa chặn hợp nhất hoạt động."),

(32,"Python project - a packaged, tested, observable tool","DA","Lesson 31",
"Bài dự án khép module. Nâng công cụ CSV ở lesson 11 thành một gói đạt chuẩn sản xuất. Danh mục kiểm tám điểm, mỗi điểm đến từ một bài: đóng gói cài được và môi trường khoá phiên bản; chú thích kiểu sạch với bộ kiểm tĩnh; xác thực dữ liệu tại ranh giới; đủ bốn loại phép kiểm; nhật ký có cấu trúc và mã theo dõi; hồ sơ đo hiệu năng có trước và sau; mô hình đồng thời chọn có số đo; và quy trình tích hợp liên tục xanh có cửa chặn. Phép thử nghiệm thu gồm hai phần: một học viên khác cài từ gói dựng sẵn trên máy trống và chạy được; và công cụ chịu được 20 lần giết tiến trình giữa chừng mà đối soát vẫn khớp. Bằng chứng nộp kèm: bảng danh mục kiểm tám điểm, mỗi điểm dẫn tới một tệp hoặc một số đo cụ thể.",
"Nộp một gói đạt cả tám điểm danh mục kiểm, qua được phép thử cài trên máy trống và phép thử giết tiến trình.",
"Tầng *sáng tạo*. Bài tổng hợp toàn module thành một sản phẩm đạt chuẩn. Kiểm bằng hai phép thử nghiệm thu cộng rà soát danh mục; đạt khi cả tám điểm có bằng chứng và cả hai phép thử qua.",
"Nâng công cụ thành gói đạt tám điểm. Nộp bảng danh mục kiểm, mỗi điểm dẫn tới tệp hoặc số đo. Đưa cho một học viên khác cài trên máy trống. Chạy phép thử giết tiến trình 20 lần và đối soát.",
"Bỏ phần đo hiệu năng vì thấy công cụ đủ nhanh · chọn mô hình đồng thời mà không dẫn số đo · nộp khi quy trình còn đỏ · dẫn bằng chứng chung chung.",
"Tám điểm đều dẫn được tới tệp hoặc số đo, người khác cài và chạy được trên máy trống, và 20 lần giết tiến trình vẫn đối soát khớp."),
]

M3 = ("Data Structures and Algorithms for Systems", 33, 44, """| | |
|---|---|
| **Objective cấp module** | Chọn cấu trúc dữ liệu theo mẫu truy cập, tính cục bộ và tỉ lệ đọc ghi, rồi bảo vệ lựa chọn bằng số đo chứ bằng ký hiệu độ phức tạp |
| **Tiền đề** | M2 |
| **Exit criterion** | Với mỗi cấu trúc đã học, nêu được độ phức tạp thao tác, cách xếp trong bộ nhớ, khối lượng công việc phù hợp, và ca biên làm nó sụp |
| **Kỹ năng SFIA** | `PROG` mức 4 · `HPCC` mức 3 |
| **Chế độ hỏng** | Học độ phức tạp như công thức để đọc, rồi không giải thích được vì sao một phép quét tuyến tính thắng một cấu trúc có độ phức tạp tốt hơn |""",
"""Module này không phải luyện phỏng vấn thuật toán. Mục tiêu là nối cấu trúc dữ liệu với những thứ sẽ gặp ở tầng hệ thống: bảng băm nối với phép kết băm ở M9 và M18, cây B nối với chỉ mục ở M10, đồ thị nối với đồ thị phụ thuộc ở M14 và lineage ở M14D, bộ lọc Bloom nối với cấu trúc gộp theo nhật ký ở M10.

Nguyên tắc xuyên suốt: mọi kết luận về hiệu năng phải dẫn về một phép đo, vì hằng số nhân và tính cục bộ của bộ nhớ đệm thường lấn át bậc độ phức tạp ở quy mô thật.""")

L3 = [
(33,"Complexity, constant factors and benchmark bias","LT","Module 3: M2",
"Ký hiệu độ phức tạp mô tả xu hướng khi dữ liệu lớn dần, nó không nói gì về tốc độ ở quy mô cụ thể, và nhầm hai thứ này là nguồn của rất nhiều quyết định sai. Ba loại phân tích và khi nào dùng loại nào: xấu nhất cho cam kết, trung bình cho kỳ vọng, và khấu hao cho cấu trúc có thao tác đắt thỉnh thoảng như mảng động. Hằng số nhân và vì sao nó quan trọng: một thuật toán bậc tuyến tính với hằng số nhỏ thường thắng một thuật toán bậc lôgarit với hằng số lớn trong khoảng dữ liệu thực tế của phần lớn hệ. Chi phí theo bộ nhớ đệm: đọc một ô nhớ liền kề rẻ hơn nhiều so với nhảy lung tung, nên cách xếp dữ liệu trong bộ nhớ ảnh hưởng tới tốc độ không kém gì thuật toán, và điều này sẽ quay lại ở M4. Bốn cách làm phép so sánh vô nghĩa và cách tránh từng cái, nối lại kỷ luật đo ở lesson 21.",
"Dự đoán và kiểm chứng điểm giao giữa hai cách cài đặt có bậc độ phức tạp khác nhau trên dữ liệu thật.",
"Tầng *phân tích*. Objective đòi nối lý thuyết với số đo và giải thích chênh lệch, chứ tính bậc. Kiểm bằng bài đo có điểm giao; đạt khi tìm ra điểm giao và giải thích đúng bằng hằng số nhân hoặc tính cục bộ.",
"Cài hai cách tìm kiếm trên dữ liệu đã sắp xếp: quét tuyến tính và tìm nhị phân. Đo trên tám kích thước từ 8 tới 1 triệu phần tử. Vẽ đồ thị và tìm điểm giao. Giải thích vì sao quét tuyến tính thắng ở dưới điểm đó. Cố ý chạy một phép so sánh có bộ nhớ đệm đã ấm và chỉ ra nó lệch bao nhiêu.",
"Chọn cấu trúc chỉ theo bậc độ phức tạp · đo với dữ liệu quá nhỏ · không lặp lại phép đo · bỏ qua giai đoạn khởi động.",
"Tìm được điểm giao bằng số đo, và giải thích đúng nguyên nhân bằng hằng số nhân hoặc tính cục bộ."),

(34,"Arrays, dynamic arrays and memory layout","TH","Lesson 33",
"Mảng liên tục là cấu trúc nền của gần như mọi thứ nhanh, vì nó cho truy cập ngẫu nhiên theo chỉ số và cho phép đọc tuần tự với tính cục bộ tốt nhất. Mảng động thêm khả năng lớn lên: khi đầy thì cấp vùng lớn hơn và sao chép sang, và nhân đôi kích thước cho chi phí khấu hao hằng số cho mỗi lần thêm. Từ đó suy ra hai hệ quả thực tế: thêm vào cuối rẻ còn chèn vào giữa đắt vì phải dịch chuyển; và biết trước kích thước rồi cấp sẵn thì tránh được nhiều lần sao chép. Danh sách liên kết đối lập: thêm và xoá ở giữa rẻ về mặt thao tác con trỏ, nhưng mỗi nút nằm rải rác nên duyệt tốn nhiều lần nhảy bộ nhớ và chậm hơn mảng nhiều lần trong thực tế. Đây là ví dụ rõ nhất cho bài học ở lesson 33: bậc độ phức tạp giống nhau mà tốc độ thật khác nhau nhiều lần.",
"Đo được chênh lệch tốc độ duyệt giữa mảng và danh sách liên kết, và giải thích bằng cách xếp trong bộ nhớ.",
"Tầng *áp dụng*. Objective là một phép đo có giải thích cơ chế. Kiểm bằng bảng số đo; đạt khi chênh lệch đo được đúng chiều và giải thích đúng bằng tính cục bộ chứ bằng bậc độ phức tạp.",
"Cài mảng động của riêng mình có chiến lược nhân đôi, đo chi phí khấu hao cho mỗi lần thêm qua một triệu lần. So thời gian duyệt giữa mảng và danh sách liên kết cùng số phần tử. Thử cấp sẵn kích thước và đo phần tiết kiệm.",
"Giải thích chênh lệch bằng bậc độ phức tạp · dùng danh sách liên kết vì thấy thêm xoá rẻ · tăng kích thước theo hằng số thay vì nhân đôi · không cấp sẵn khi đã biết kích thước.",
"Bảng số đo cho thấy mảng duyệt nhanh hơn nhiều lần, và giải thích đúng bằng tính cục bộ bộ nhớ."),

(35,"Hash tables - collisions, load factor and resize","TH","Lesson 34",
"Bảng băm là cấu trúc được dùng nhiều nhất trong hệ dữ liệu và cũng là cấu trúc bị coi là hộp đen nhiều nhất. Cơ chế: hàm băm ánh xạ khoá sang vị trí, nhiều khoá có thể rơi cùng vị trí, nên phải có cách xử lý va chạm. Hai cách và đánh đổi: móc xích giữ danh sách tại mỗi vị trí, đơn giản và chịu được hệ số tải cao; địa chỉ mở tìm vị trí kế tiếp, tính cục bộ tốt hơn nhưng xuống cấp nhanh khi gần đầy và cần bia mộ khi xoá. Hệ số tải quyết định tốc độ: vượt ngưỡng thì phải cấp lại và băm lại toàn bộ, một thao tác đắt xảy ra thỉnh thoảng. Chất lượng hàm băm quyết định tất cả: hàm băm kém cho phân bố lệch và bảng băm suy biến về danh sách, và **kẻ tấn công cố tình tạo va chạm là một dạng tấn công có thật**. Nối tới hệ thống: phép kết băm ở M9 và M18, và phân vùng theo băm ở M16.",
"Đo được quan hệ giữa hệ số tải và tốc độ tra cứu, và chứng minh bằng thực nghiệm tác động của hàm băm kém.",
"Tầng *phân tích*. Objective đòi nối tham số cấu hình với hành vi quan sát được. Kiểm bằng bảng đo nhiều hệ số tải cộng thí nghiệm va chạm; đạt khi đường cong đúng dạng và thí nghiệm va chạm cho thấy suy biến.",
"Cài cả hai cách xử lý va chạm. Đo thời gian tra cứu ở năm mức hệ số tải. Đo chi phí của một lần cấp lại. Thay hàm băm tốt bằng một hàm băm kém có chủ ý và đo lại. Tạo một tập khoá cố tình va chạm và đo mức suy biến.",
"Coi bảng băm là hộp đen · để hệ số tải rất cao · dùng địa chỉ mở mà không xử lý bia mộ khi xoá · giả định hàm băm mặc định luôn an toàn.",
"Bảng đo năm mức hệ số tải cho đường cong đúng dạng, và tập khoá va chạm làm tra cứu suy biến có số chứng minh."),

(36,"Trees - BST, balancing and the B-tree idea","LT","Lesson 35",
"Bảng băm cho tra cứu theo khoá chính xác rất nhanh nhưng không giữ thứ tự, nên không trả lời được truy vấn theo khoảng, và đó là lý do cây tồn tại. Cây tìm kiếm nhị phân giữ thứ tự nên tra theo khoảng được, nhưng suy biến thành danh sách nếu chèn dữ liệu đã sắp xếp; cây tự cân bằng giải vấn đề đó bằng cách xoay để giữ chiều cao. Cây B là biến thể cho lưu trữ ngoài và là cấu trúc của gần như mọi chỉ mục cơ sở dữ liệu: mỗi nút chứa nhiều khoá và có nhiều con, nên cây rất thấp và số lần đọc đĩa để tìm một khoá rất nhỏ. **Lý do thiết kế đó nằm ở chỗ đọc đĩa theo khối**: đọc một khối 8 KB tốn gần bằng đọc 100 byte, nên nhồi nhiều khoá vào một nút là tối ưu đúng. Đây là bài đặt nền trực tiếp cho chỉ mục ở M10 và cho việc đọc kế hoạch thực thi ở M9.",
"Giải thích vì sao chỉ mục cơ sở dữ liệu dùng cây B thay vì cây nhị phân hay bảng băm, dẫn bằng chi phí đọc khối.",
"Tầng *hiểu*. Bài lý thuyết chuẩn bị cho M9 và M10; chưa đòi cài đặt cây B. Kiểm bằng bài giải thích cộng tính toán; đạt khi tính đúng chiều cao cây ở hai cấu hình và nêu đúng lý do liên quan tới đọc khối.",
"Cài cây tìm kiếm nhị phân, chèn dữ liệu đã sắp xếp và đo chiều cao để thấy suy biến. Tính chiều cao cây B cho một triệu khoá ở hai kích thước nút khác nhau. Viết ba câu giải thích vì sao cấu trúc này phù hợp với lưu trữ ngoài, và một câu nêu khi nào bảng băm vẫn tốt hơn.",
"Nghĩ cây B là cây nhị phân cân bằng · bỏ qua lý do đọc khối · dùng cây cho tra cứu chỉ theo khoá chính xác · chèn dữ liệu đã sắp xếp vào cây không cân bằng.",
"Chiều cao cây B tính đúng ở cả hai cấu hình, và giải thích nêu đúng vai trò của chi phí đọc khối."),

(37,"Heaps, priority queues and top-k","TH","Lesson 36",
"Đống là cấu trúc trả lời một câu hỏi rất hẹp nhưng rất hay gặp: phần tử nhỏ nhất hoặc lớn nhất hiện tại là gì. Cơ chế cây gần đầy đủ lưu trong mảng, nên không cần con trỏ và tính cục bộ tốt. Ba ứng dụng trong hệ dữ liệu: lấy N phần tử đầu mà không phải sắp xếp toàn bộ, trộn nhiều dòng đã sắp xếp trong sắp xếp ngoài ở lesson 39, và lập lịch theo độ ưu tiên. Lấy N đầu bằng đống giữ kích thước N: duyệt một lần, bộ nhớ chỉ N, so với sắp xếp toàn bộ tốn bộ nhớ theo toàn bộ dữ liệu; đây là ví dụ rõ về chọn cấu trúc theo câu hỏi thay vì theo thói quen. Dựng đống một lần rẻ hơn chèn lần lượt, và đo được chênh lệch đó. Nối tới hệ thống: bài toán lấy N đầu mỗi nhóm sẽ gặp lại ở M9 dưới dạng hàm cửa sổ.",
"Giải bài toán lấy N phần tử đầu trên dữ liệu vượt bộ nhớ bằng đống giữ kích thước N, và so bộ nhớ với cách sắp xếp toàn bộ.",
"Tầng *áp dụng*. Objective là chọn cấu trúc theo ràng buộc bộ nhớ và chứng minh bằng số đo. Kiểm bằng cặp số đo bộ nhớ; đạt khi bản dùng đống giữ bộ nhớ theo N chứ theo kích thước dữ liệu.",
"Trên tệp 5 GB, lấy 100 bản ghi lớn nhất bằng hai cách: sắp xếp toàn bộ rồi cắt, và đống giữ kích thước 100. Đo thời gian và bộ nhớ đỉnh của cả hai. So dựng đống một lần với chèn lần lượt trên một triệu phần tử.",
"Sắp xếp toàn bộ để lấy vài phần tử · dùng đống khi cần thứ tự đầy đủ · chèn lần lượt thay vì dựng một lần · bỏ qua bộ nhớ khi so.",
"Bản dùng đống giữ bộ nhớ đỉnh theo N và cho cùng kết quả, kèm số đo so với cách sắp xếp toàn bộ."),

(38,"Graphs, topological order and dependency scheduling","TH","Lesson 37",
"Đồ thị là mô hình của mọi thứ có quan hệ phụ thuộc, và trong chương trình này nó xuất hiện ba lần: đồ thị phụ thuộc của bộ điều phối ở M14, đồ thị lineage ở M14D, và đồ thị thực thi của engine phân tán ở M18. Hai cách biểu diễn và khi nào dùng cái nào: danh sách kề tiết kiệm cho đồ thị thưa, ma trận kề nhanh cho kiểm tra cạnh trên đồ thị dày. Duyệt theo chiều rộng và theo chiều sâu, cùng bài toán tương ứng. Sắp thứ tự tô pô cho đồ thị có hướng không chu trình là thuật toán trung tâm: nó trả lời câu hỏi chạy các bước theo thứ tự nào, và **thuật toán tự phát hiện chu trình** vì đồ thị có chu trình thì không sắp được. Từ đó suy ra cách bộ điều phối báo lỗi phụ thuộc vòng. Chạy song song có giới hạn trên đồ thị: các nút không phụ thuộc nhau chạy đồng thời được, và đó là cách một đồ thị phụ thuộc được thực thi nhanh.",
"Cài bộ thực thi đồ thị phụ thuộc có phát hiện chu trình và chạy song song có giới hạn, và chứng minh thứ tự chạy đúng.",
"Tầng *sáng tạo*. Objective đòi ghép sắp thứ tự tô pô với giới hạn đồng thời ở lesson 29 thành một bộ thực thi. Kiểm bằng ba đồ thị thử trong đó một có chu trình; đạt khi thứ tự chạy hợp lệ, chu trình bị phát hiện, và giới hạn đồng thời được tôn trọng.",
"Cài bộ thực thi nhận một đồ thị nhiệm vụ. Chạy trên ba đồ thị: một chuỗi thẳng, một đồ thị có nhánh song song, và một đồ thị có chu trình. Chứng minh thứ tự chạy hợp lệ bằng nhật ký, chu trình bị báo lỗi rõ ràng, và số nhiệm vụ chạy đồng thời không vượt giới hạn. Thêm trạng thái thử lại cho nhiệm vụ hỏng.",
"Không phát hiện chu trình nên chạy vô hạn · chạy song song không giới hạn · bắt đầu một nhiệm vụ khi phụ thuộc chưa xong · không giữ trạng thái nên chạy lại từ đầu.",
"Thứ tự chạy hợp lệ trên cả ba đồ thị, chu trình bị báo lỗi rõ, và số nhiệm vụ đồng thời không vượt giới hạn."),

(39,"External merge sort and IO amplification","TH","Lesson 38",
"Bài toán nền của mọi xử lý dữ liệu vượt bộ nhớ, và cũng là thứ engine phân tán ở M18 làm bên trong khi sắp xếp và khi xáo trộn. Cơ chế hai pha: pha một chia dữ liệu thành các đoạn vừa bộ nhớ, sắp xếp từng đoạn và ghi ra đĩa; pha hai trộn các đoạn đã sắp xếp bằng một đống theo lesson 37. Số đoạn trộn cùng lúc bị giới hạn bởi bộ nhớ, nên dữ liệu rất lớn cần nhiều vòng trộn, và **số vòng trộn nhân lên lượng đọc ghi đĩa**; đại lượng này gọi là hệ số khuếch đại vào ra và là thứ quyết định thời gian chạy thật. Đánh đổi bộ nhớ và số vòng: cho nhiều bộ nhớ hơn thì ít vòng hơn và ít đọc ghi hơn. Đây là lý do một công việc sắp xếp được cấp thêm bộ nhớ có thể nhanh lên nhiều lần chứ tuyến tính, và là bài học sẽ dùng lại khi chỉnh bộ nhớ ở M18.",
"Cài sắp xếp ngoài với ngân sách bộ nhớ nhỏ hơn dữ liệu, và đo được quan hệ giữa bộ nhớ cấp và hệ số khuếch đại vào ra.",
"Tầng *áp dụng*. Objective là một cài đặt có số đo giải thích được bằng cơ chế hai pha. Kiểm bằng bảng ba mức bộ nhớ; đạt khi sắp xếp đúng ở mọi mức và hệ số khuếch đại đo được giảm khi tăng bộ nhớ.",
"Cài sắp xếp ngoài cho tệp 2 GB với ngân sách bộ nhớ 100 MB. Kiểm kết quả đã sắp xếp đúng. Chạy lại ở ba mức bộ nhớ và đo tổng byte đọc cùng ghi. Tính hệ số khuếch đại vào ra cho từng mức và vẽ quan hệ.",
"Đọc cả tệp vào bộ nhớ · dùng số đoạn trộn quá lớn so với bộ nhớ · chỉ đo thời gian mà không đo byte đọc ghi · không kiểm kết quả đã sắp xếp đúng.",
"Kết quả sắp xếp đúng ở cả ba mức bộ nhớ, và hệ số khuếch đại vào ra giảm khi tăng bộ nhớ có số chứng minh."),

(40,"Hash join against sort-merge join","TH","Lesson 39",
"Hai cách ghép hai tập dữ liệu theo khoá, và đây là bài nối trực tiếp tới M9 và M18 vì mọi engine đều chọn giữa hai cách này. Phép kết băm dựng bảng băm từ bên nhỏ rồi quét bên lớn để dò; nhanh khi bên nhỏ vừa bộ nhớ, và suy giảm khi không vừa vì phải chia thành phân vùng rồi làm từng phần. Phép kết sắp xếp trộn sắp cả hai bên theo khoá rồi trộn; tốn hơn khi dữ liệu chưa sắp xếp, nhưng **miễn phí nếu dữ liệu đã sắp xếp sẵn**, và đây là lý do bố trí dữ liệu ở M13 ảnh hưởng tới tốc độ kết. Điểm giao phụ thuộc ba yếu tố: kích thước hai bên, bộ nhớ có sẵn, và dữ liệu đã sắp xếp chưa. Khoá lệch làm phép kết băm suy giảm vì một phân vùng quá lớn, đúng hiện tượng sẽ gặp lại ở M18. Cách đo để tìm điểm giao trên dữ liệu của chính mình thay vì tin quy tắc chung.",
"Cài cả hai phép kết và tìm được điểm giao theo kích thước dữ liệu, bộ nhớ và độ lệch khoá.",
"Tầng *đánh giá*. Objective đòi xác định điều kiện áp dụng của hai thuật toán bằng thực nghiệm, chuẩn bị trực tiếp cho M9. Kiểm bằng bảng ba yếu tố; đạt khi tìm ra điểm giao theo ít nhất hai yếu tố và giải thích đúng cơ chế suy giảm.",
"Cài phép kết băm và phép kết sắp xếp trộn. Đo thời gian trên lưới gồm ba kích thước dữ liệu nhân hai mức bộ nhớ. Thêm một khoá chiếm 60% dữ liệu và đo lại cả hai. Chạy lại phép kết sắp xếp trộn trên dữ liệu đã sắp xếp sẵn và ghi phần chênh.",
"Kết luận một cách luôn nhanh hơn · bỏ qua bộ nhớ khi so · không thử dữ liệu lệch khoá · quên rằng dữ liệu đã sắp xếp đổi hẳn kết luận.",
"Tìm được điểm giao theo ≥ 2 yếu tố kèm số đo, và giải thích đúng vì sao phép kết băm suy giảm khi khoá lệch."),

(41,"Bloom filters and probabilistic membership","TH","Lesson 40",
"Cấu trúc trả lời câu hỏi khoá này có thể có trong tập không, với một đánh đổi rất cụ thể: nó có thể trả lời nhầm là có, nhưng **không bao giờ trả lời nhầm là không**. Tính chất một chiều đó là thứ làm nó hữu dụng: dùng làm bộ lọc trước để tránh một phép tìm đắt, và trả lời nhầm là có chỉ tốn thêm một lần tìm chứ cho kết quả sai. Cơ chế: một dãy bit và k hàm băm; thêm phần tử thì bật k bit, hỏi thì kiểm k bit. Tỉ lệ trả lời nhầm phụ thuộc số bit trên mỗi phần tử và số hàm băm, và có công thức để chọn hai tham số theo tỉ lệ mong muốn. Không xoá được phần tử, và đó là giới hạn phải biết trước khi dùng. Nối tới hệ thống: cấu trúc gộp theo nhật ký ở M10 dùng nó để tránh đọc các tệp không chứa khoá, và engine truy vấn dùng nó để bỏ qua tệp ở M13.",
"Chọn số bit trên mỗi phần tử và số hàm băm cho một tỉ lệ nhầm mục tiêu, và kiểm chứng tỉ lệ thật bằng thực nghiệm.",
"Tầng *áp dụng*. Objective là chọn tham số có công thức rồi xác nhận bằng đo. Kiểm bằng bảng quét tham số; đạt khi tỉ lệ nhầm đo được bám sát lý thuyết và không có lần nào trả lời nhầm là không.",
"Cài bộ lọc Bloom. Quét số bit trên mỗi phần tử từ 4 tới 16 và số hàm băm từ 1 tới 8. Với mỗi tổ hợp, đo tỉ lệ trả lời nhầm thật trên một triệu phép hỏi và so với giá trị lý thuyết. Chứng minh bằng thực nghiệm không có trường hợp nào trả lời nhầm là không. Đo phần tiết kiệm khi dùng nó làm bộ lọc trước một phép tìm trên đĩa.",
"Dùng bộ lọc Bloom khi cần câu trả lời chắc chắn · chọn tham số theo cảm tính · quên rằng không xoá được · bỏ qua chi phí tính k hàm băm.",
"Tỉ lệ nhầm đo được bám sát lý thuyết trên lưới tham số, không có lần nào trả lời nhầm là không, và có số đo phần tiết kiệm."),

(42,"Choosing a structure from the access pattern","LT","Lesson 41",
"Bài chốt phần cấu trúc, biến bảy bài trước thành một quy tắc quyết định. Bốn câu hỏi theo thứ tự: truy cập theo khoá chính xác hay theo khoảng, tỉ lệ đọc so với ghi ra sao, dữ liệu có vừa bộ nhớ không, và có cần giữ thứ tự không. Bảng quyết định nối bốn câu đó với các cấu trúc đã học. Ba cặp đối lập cần thuộc: bảng băm cho tra chính xác còn cây cho tra khoảng; mảng cho duyệt tuần tự còn danh sách liên kết gần như không bao giờ đúng trong mã dữ liệu; đống cho câu hỏi cực trị còn sắp xếp cho thứ tự đầy đủ. Nguyên tắc cuối và quan trọng nhất: **ở quy mô thật, đo quyết định chứ bậc độ phức tạp quyết định**, và mọi lựa chọn trong bài này phải dẫn về một số đo đã tự đo ở lesson 33 tới 41. Ba tình huống mà cấu trúc đơn giản nhất là lựa chọn đúng dù có cấu trúc tốt hơn về lý thuyết.",
"Chọn cấu trúc cho năm mẫu truy cập cho trước, mỗi lần dẫn về một số đo đã tự đo.",
"Tầng *đánh giá*. Objective đòi áp một quy tắc quyết định có bằng chứng. Kiểm bằng năm mẫu truy cập trong đó ít nhất một nên dùng cấu trúc đơn giản nhất; đạt khi chọn đúng ít nhất bốn và nhận ra trường hợp đó.",
"Cho năm mẫu truy cập mô tả bằng ngôn ngữ nghiệp vụ. Với mỗi mẫu, trả lời bốn câu hỏi, chọn cấu trúc, và dẫn một số đo từ các bài trước. Với mẫu mà cấu trúc đơn giản là đúng, ước lượng phần phức tạp thêm nếu chọn cấu trúc tinh vi hơn.",
"Chọn cấu trúc tinh vi vì nghe hay hơn · bỏ qua tỉ lệ đọc ghi · quên hỏi dữ liệu có vừa bộ nhớ không · dẫn lý thuyết thay vì dẫn số đo.",
"Chọn đúng ≥ 4/5 mẫu truy cập với số đo dẫn chứng, và nhận ra đúng trường hợp nên dùng cấu trúc đơn giản nhất."),

(43,"Failure drills - adversarial input and measurement traps","TH","Lesson 42",
"Bài diễn tập hỏng, và nó kiểm tra xem người học có thật sự hiểu cơ chế hay chỉ chạy được lab. Năm tình huống hỏng, mỗi tình huống nhắm vào một hiểu lầm cụ thể. Một là tập khoá cố tình va chạm làm bảng băm suy biến, theo lesson 35. Hai là đồ thị có chu trình làm bộ thực thi chạy vô hạn, theo lesson 38. Ba là đệ quy quá sâu làm tràn ngăn xếp, và cách chuyển sang vòng lặp có ngăn xếp tường minh. Bốn là tràn số khi cộng dồn kích thước, một lỗi ít gặp trong Python nhưng phải hiểu vì sẽ gặp ở M4. Năm là phép so sánh cho kết quả ngược vì đầu vào quá nhỏ hoặc bộ nhớ đệm đã ấm, theo lesson 33. Với mỗi tình huống, yêu cầu không phải chỉ sửa mà là **dựng một phép kiểm hồi quy bắt được nó lần sau**, đúng kỷ luật đã đặt ở lesson 9.",
"Chẩn đoán năm tình huống hỏng về đúng cơ chế và viết phép kiểm hồi quy bắt được từng cái.",
"Tầng *phân tích*. Objective đòi truy từ triệu chứng về cơ chế đã học và biến nó thành một phép kiểm lâu dài. Kiểm bằng năm tình huống tính giờ; đạt khi chẩn đoán đúng ít nhất bốn và mỗi cái có phép kiểm hồi quy chạy được.",
"Giảng viên đưa năm chương trình hỏng theo năm cách trên, mỗi cái 10 phút. Với mỗi cái, chẩn đoán cơ chế, sửa, và viết một phép kiểm hồi quy. Chạy toàn bộ phép kiểm trên bản chưa sửa để chứng minh chúng thật sự bắt được lỗi.",
"Sửa mà không viết phép kiểm hồi quy · tăng giới hạn đệ quy thay vì đổi cách · kết luận từ một lần đo · viết phép kiểm không chạy trên bản chưa sửa.",
"Chẩn đoán đúng ≥ 4/5 tình huống, và mọi phép kiểm hồi quy đều báo đỏ trên bản chưa sửa và xanh trên bản đã sửa."),

(44,"Gate 1 - explain a structure choice and prove it by measurement","KT","Lesson 43",
"Cổng của Phase 1. Bài kiểm ba năng lực nền của cả chương trình: kỷ luật kỹ thuật ở M1, Python có chất lượng sản phẩm ở M2, và chọn cấu trúc có bằng chứng ở M3. Không có nội dung mới.",
"Nộp lời giải cho một bài toán dữ liệu cho trước, bảo vệ lựa chọn cấu trúc bằng số đo của chính mình, và chẩn đoán được một lỗi tiêm sẵn.",
"Tầng *đánh giá*. Cổng đo năng lực tổng hợp dưới chất vấn, nên hình thức là bài làm cộng bảo vệ chứ trắc nghiệm.",
"Buổi 145 phút: 100 phút làm bài độc lập, 45 phút chữa bài. Nhận một bài toán xử lý tệp 3 GB với ngân sách bộ nhớ 200 MB. Bài chấm sáu phần: A (15đ) phát biểu bài toán sáu phần và phép kiểm chấp nhận · B (20đ) chương trình chạy đúng trong ngân sách bộ nhớ · C (20đ) lựa chọn cấu trúc dẫn bằng số đo của chính mình, không dẫn lý thuyết suông · D (15đ) bộ kiểm đủ bốn loại và quy trình tích hợp xanh · E (20đ) chẩn đoán một lỗi tiêm sẵn bằng bảng giả thuyết có ít nhất ba dòng bị bác bỏ · F (10đ) nhật ký có cấu trúc đủ để người khác chẩn đoán lại.",
"Nạp cả tệp vào bộ nhớ · chọn cấu trúc rồi mới tìm lý do · bỏ phần chẩn đoán vì hết giờ · dẫn bậc độ phức tạp thay vì số đo.",
"Đạt ≥ 70/100, phần B và C đều ≥ 60%. Lựa chọn cấu trúc không dẫn được về số đo của chính mình thì phần C bằng không."),
]
