# -*- coding: utf-8 -*-
"""DE M6 — Concurrency, parallelism and correctness under contention."""

M6 = ("Concurrency, Parallelism and Correctness Under Contention", 50, 61, """| | |
|---|---|
| **Objective cấp module** | Viết chương trình xử lý dữ liệu chạy đồng thời mà chứng minh được không mất và không nhân bản bản ghi, và định vị được tranh chấp khi nó xảy ra |
| **Tiền đề** | M3 · M5 |
| **Exit criterion** | Đạt Cổng 2 ≥ 70/100: vẽ dòng thời gian chỉ ra một tranh chấp cụ thể, và giải thích vì sao thử lại không điều kiện gây cả bão tải lẫn bản ghi trùng |
| **Kỹ năng SFIA** | `PROG` mức 4 · `TEST` mức 3 |
| **Chế độ hỏng** | Chạy thử vài lần thấy đúng rồi kết luận không có tranh chấp, trong khi tranh chấp chỉ lộ ra dưới tải và ở môi trường khác |""",
"Module khó nhất chặng 1, và là module mà lỗi tốn kém nhất về sau. Bốn bài đầu dựng khái niệm, năm bài giữa là cơ chế đồng bộ và các chế độ hỏng, ba bài cuối là mẫu hàng đợi có giới hạn, áp lực ngược và cổng 2. Mọi khẳng định về tính đúng đắn phải chứng minh bằng đối soát dưới tải, không bằng vài lần chạy thử.")

L6 = [
(50,"Concurrency, parallelism and asynchrony are three things","LT","Module 6: M3 · M5",
"Ba khái niệm bị gộp làm một trong phần lớn cách nói thông thường. Đồng thời là cấu trúc chương trình cho phép nhiều việc đang dở cùng lúc; song song là thực thi nhiều việc đúng cùng một thời điểm trên nhiều lõi; bất đồng bộ là mô hình lập trình không chặn khi chờ. Một chương trình đồng thời chạy được trên một lõi; một chương trình song song cần nhiều lõi; một chương trình bất đồng bộ có thể không song song chút nào. Định luật Amdahl: phần tuần tự đặt cận trên cho mức tăng tốc, nên 10% tuần tự thì dù bao nhiêu lõi cũng không nhanh quá 10 lần. Hệ quả cho công việc dữ liệu: nhiều pipeline có phần tuần tự lớn ở khâu ghi hoặc khâu đối soát, và thêm nhân công không cứu được. Chọn mô hình theo loại tải, nối lại lesson 12: tải nghẽn vào ra hợp với bất đồng bộ hoặc nhiều luồng, tải nghẽn tính toán cần nhiều tiến trình. Khoá thông dịch toàn cục trong một số môi trường chạy Python và hệ quả thực tế của nó.",
"Phân loại một tải rồi chọn mô hình đồng thời phù hợp, và ước lượng cận trên mức tăng tốc bằng định luật Amdahl.",
"Tầng *áp dụng*. Objective gồm một phép phân loại và một phép tính có đáp án. Kiểm bằng ba tải và ba phép tính cận trên; đạt khi chọn đúng mô hình cho cả ba và khi mức tăng tốc đo được không vượt cận trên đã tính.",
"Đo phần tuần tự của ba pipeline bằng cách đo thời gian từng giai đoạn. Tính cận trên mức tăng tốc cho từng cái. Chạy mỗi pipeline ở 1, 2, 4, 8 nhân công, đo mức tăng tốc thật, vẽ đường cong và so với cận trên.",
"Gọi mọi thứ chạy nhanh hơn là song song · thêm nhân công cho pipeline có phần tuần tự lớn · dùng nhiều luồng cho tải nghẽn tính toán trong môi trường chạy có khoá thông dịch toàn cục.",
"Chọn đúng mô hình cho cả ba tải, và mức tăng tốc đo được không vượt cận trên đã tính cho tải nào."),

(51,"Critical sections and race conditions","LT","Lesson 50",
"Vùng tới hạn là đoạn mã truy cập trạng thái dùng chung mà chỉ được một luồng vào tại một thời điểm. Tranh chấp xảy ra khi kết quả phụ thuộc thứ tự thực thi mà thứ tự đó không được bảo đảm. Vì sao một phép tăng biến đếm không phải một thao tác mà là ba: đọc, cộng, ghi, và mất cập nhật xảy ra ở khe giữa ba bước đó. Ba loại tranh chấp thường gặp trong công việc dữ liệu: hai nhân công cùng lấy một công việc trong hàng đợi, hai tiến trình cùng ghi một tệp đích, và kiểm tra rồi hành động trên hệ tệp với khe giữa hai bước. Vì sao tranh chấp không lộ ra khi chạy thử: cửa sổ rất hẹp nên xác suất thấp, và xác suất đó tăng theo tải và đổi theo máy. Vẽ dòng thời gian hai luồng để chứng minh một tranh chấp tồn tại, kỹ thuật kiểm được và là yêu cầu của cổng. Tranh chấp không phải lỗi ngẫu nhiên mà là lỗi thiết kế có thể lập luận ra trước khi chạy.",
"Vẽ dòng thời gian hai luồng chứng minh một tranh chấp trong một đoạn mã cho trước, trước khi chạy nó.",
"Tầng *phân tích*. Objective là lập luận ra lỗi từ mã, không phải quan sát lỗi khi chạy. Kiểm bằng bốn đoạn mã, ba có tranh chấp một không; đạt khi chỉ đúng cả bốn và với ba đoạn có lỗi thì vẽ được dòng thời gian cho ra kết quả sai. Chạy rồi mới biết không tính điểm.",
"Đọc bốn đoạn mã, phân loại có hay không có tranh chấp, vẽ dòng thời gian cho từng đoạn có lỗi. Sau đó chạy mỗi đoạn 100.000 lần với 8 luồng, đếm số lần kết quả sai, so với dự đoán. Chạy lại trên máy khác và so tỉ lệ.",
"Kết luận không có tranh chấp vì chạy 10 lần đều đúng · cho rằng một phép gán là thao tác nguyên tử · sửa bằng cách thêm thời gian ngủ.",
"Phân loại đúng cả bốn đoạn và vẽ được dòng thời gian cho ba đoạn có lỗi, trước khi chạy."),

(52,"Mutexes, semaphores and condition variables","TH","Lesson 51",
"Khoá loại trừ cho phép đúng một luồng vào vùng tới hạn. Chi phí của khoá: tranh chấp khoá làm luồng phải chờ, và vùng tới hạn càng dài thì mức song song càng thấp. Nguyên tắc giữ khoá ngắn nhất có thể, và cái giá khi chia nhỏ vùng tới hạn quá mức. Đèn hiệu giới hạn số luồng vào cùng lúc, dùng để giới hạn số kết nối hoặc số yêu cầu đồng thời, nối lại lesson 36. Biến điều kiện cho luồng chờ tới khi một điều kiện thành đúng mà không quay vòng tốn bộ xử lý. Đánh thức giả và vì sao phải kiểm điều kiện trong vòng lặp chứ không trong câu lệnh điều kiện. Khoá đọc ghi cho tải đọc nhiều. Thao tác nguyên tử và khi nào chúng đủ thay cho khoá. Khoá trên nhiều tiến trình: khoá tệp ở lesson 27 và khoá phân tán ở chặng 6, cùng bài toán ở ba quy mô. Khoá phân tán không đáng tin tuyệt đối vì đồng hồ và mạng, nên thiết kế vẫn phải chịu được hai bên cùng chạy.",
"Sửa một đoạn mã có tranh chấp bằng cơ chế đồng bộ phù hợp, và đo chi phí thông lượng mà cơ chế đó gây ra.",
"Tầng *áp dụng*. Objective gồm sửa lỗi và đo cái giá, vì chọn cơ chế mà không biết giá là chọn mù. Đạt khi 100.000 lần chạy 8 luồng không ra kết quả sai nào, và khi có bảng thông lượng trước và sau cho thấy chi phí đồng bộ.",
"Sửa ba đoạn mã có tranh chấp ở lesson 51 bằng ba cơ chế khác nhau. Với mỗi đoạn, chạy 100.000 lần với 8 luồng và đếm lỗi. Đo thông lượng trước và sau. Thử thu hẹp vùng tới hạn và đo lại.",
"Giữ khoá suốt cả hàm · kiểm điều kiện bằng câu lệnh điều kiện thay vì vòng lặp nên dính đánh thức giả · dùng khoá cho biến đếm trong khi thao tác nguyên tử là đủ.",
"100.000 lần chạy 8 luồng không lỗi, và có bảng thông lượng trước sau cho thấy chi phí đồng bộ."),

(53,"Deadlock, livelock and starvation","TH","Lesson 52",
"Bế tắc cần đủ bốn điều kiện đồng thời, và phá một điều kiện là đủ để ngăn. Cách phá thực tế nhất trong công việc dữ liệu: quy định thứ tự lấy khoá toàn cục, nên mọi luồng lấy khoá theo cùng một thứ tự. Bế tắc trong cơ sở dữ liệu: hai giao dịch lấy khoá hàng theo thứ tự ngược nhau, cơ chế phát hiện tự động và chọn nạn nhân, nối tới chặng 3. Khoá sống: các luồng liên tục nhường nhau và không ai tiến được, và vì sao nó khó phát hiện hơn bế tắc vì hệ thống vẫn bận. Đói: một luồng không bao giờ tới lượt do chính sách ưu tiên. Thời gian chờ khoá như một mạng an toàn: thà lỗi còn hơn treo, nối lại nguyên tắc ở lesson 34. Chẩn đoán bế tắc trên hệ thống đang chạy: đọc ngăn xếp luồng và tìm vòng chờ. Thiết kế tránh bế tắc quan trọng hơn phát hiện bế tắc.",
"Gây ra một bế tắc có chủ đích, chẩn đoán nó từ ngăn xếp luồng, và sửa bằng quy định thứ tự lấy khoá.",
"Tầng *phân tích*. Objective gồm chẩn đoán từ bằng chứng và sửa có nguyên tắc. Đạt khi định vị được vòng chờ từ ngăn xếp luồng, và khi bản sửa chạy một triệu vòng với 16 luồng không treo lần nào. Sửa bằng cách thêm thời gian chờ mà không phá vòng chờ chỉ đạt một nửa.",
"Viết chương trình hai luồng lấy hai khoá theo thứ tự ngược nhau, chạy tới khi treo. Lấy ngăn xếp luồng, định vị vòng chờ. Sửa bằng thứ tự khoá toàn cục, chạy một triệu vòng với 16 luồng. Sau đó gây bế tắc trong cơ sở dữ liệu và quan sát cơ chế chọn nạn nhân.",
"Sửa bế tắc bằng cách thêm thời gian ngủ · không đặt thời gian chờ khoá nên treo vô hạn · tăng số luồng khi thấy chậm trong khi nguyên nhân là tranh chấp khoá.",
"Định vị được vòng chờ từ ngăn xếp luồng, và bản sửa chạy một triệu vòng với 16 luồng không treo."),

(54,"Atomicity, memory visibility and why a variable looks stale","LT","Lesson 52",
"Nguyên tử nghĩa là không quan sát được trạng thái nửa chừng; khả kiến nghĩa là thay đổi của luồng này luồng kia nhìn thấy. Hai tính chất khác nhau và một chương trình có thể có cái này mà thiếu cái kia. Bộ nhớ đệm mỗi lõi và vì sao một luồng ghi biến mà luồng khác đọc ra giá trị cũ. Giao thức nhất quán bộ nhớ đệm làm việc đó cuối cùng cũng đồng bộ, nhưng cuối cùng là bao lâu thì không có bảo đảm. Sắp xếp lại lệnh bởi bộ biên dịch và bởi bộ xử lý: cả hai được phép đổi thứ tự miễn kết quả trên một luồng không đổi, nhưng trên nhiều luồng thì đổi. Hàng rào bộ nhớ và biến có đánh dấu không đệm. Vì sao một vòng lặp chờ cờ hiệu có thể chạy mãi dù cờ đã được đặt. Thao tác so sánh rồi hoán đổi và cấu trúc không khoá, cùng cảnh báo: viết cấu trúc không khoá đúng là việc khó và hiếm khi cần trong công việc dữ liệu. Nối tới chặng 6: cùng vấn đề khả kiến xuất hiện ở quy mô phân tán dưới tên nhất quán.",
"Giải thích vì sao một luồng đọc ra giá trị cũ dù luồng khác đã ghi, và chỉ ra cơ chế nào trong ba cơ chế gây ra điều đó.",
"Tầng *hiểu*. Objective là giải thích cơ chế, vì cài đặt cấu trúc không khoá vượt phạm vi module. Kiểm bằng ba đoạn mã, mỗi đoạn hỏng vì một cơ chế: bộ nhớ đệm chưa đồng bộ, sắp xếp lại lệnh, và thao tác không nguyên tử. Đạt khi chỉ đúng cơ chế cho cả ba.",
"Viết vòng lặp chờ cờ hiệu không đánh dấu, chạy với tối ưu hoá bật, quan sát nó chạy mãi. Thêm đánh dấu, quan sát nó dừng. Đọc ba đoạn mã và chỉ cơ chế gây lỗi cho từng đoạn. Đo chi phí của hàng rào bộ nhớ.",
"Gộp nguyên tử với khả kiến làm một · tin rằng ghi xong là luồng khác thấy ngay · viết cấu trúc không khoá khi một khoá là đủ.",
"Chỉ đúng cơ chế gây lỗi cho cả ba đoạn mã, và quan sát được vòng lặp chờ cờ hiệu chạy mãi rồi dừng sau khi sửa."),

(55,"Thread safety and immutable data","TH","Lesson 54",
"An toàn luồng là thuộc tính của một đoạn mã dưới truy cập đồng thời, và nó không phải thuộc tính của ngôn ngữ. Ba cách đạt được, theo thứ tự nên ưu tiên: không chia sẻ trạng thái, chia sẻ dữ liệu bất biến, và chia sẻ dữ liệu thay đổi được có đồng bộ. Cách thứ nhất và thứ hai không cần khoá nên không có tranh chấp khoá và không có bế tắc, đó là lý do chúng đứng trước. Dữ liệu bất biến trong xử lý dữ liệu: mỗi phép biến đổi sinh ra tập mới thay vì sửa tại chỗ, và đây là mô hình mà Spark dùng ở chặng 7. Cái giá là bộ nhớ và số lần sao chép. Trạng thái cục bộ theo luồng cho những thứ không chia sẻ được như kết nối cơ sở dữ liệu. Thư viện có an toàn luồng hay không là câu phải tra tài liệu chứ không đoán, và kết nối cơ sở dữ liệu gần như luôn không an toàn luồng, một lỗi rất phổ biến. Kiểm tra an toàn luồng bằng chạy tải đồng thời và đối soát, không bằng đọc mã.",
"Chuyển một đoạn xử lý dữ liệu chia sẻ trạng thái thay đổi được sang mô hình không chia sẻ hoặc bất biến, và đo chênh lệch thông lượng.",
"Tầng *áp dụng*. Objective gồm một phép tái cấu trúc và một phép đo cái giá. Đạt khi bản mới cho kết quả đúng dưới 16 luồng qua 100 lần chạy, và khi có bảng thông lượng cùng bộ nhớ đỉnh của cả hai bản để thấy đánh đổi.",
"Nhận một đoạn gộp dữ liệu dùng từ điển chia sẻ có khoá. Viết lại theo hai cách: mỗi luồng một từ điển riêng rồi gộp cuối, và dùng cấu trúc bất biến. Chạy cả ba bản với 16 luồng, 100 lần, đối soát kết quả. Đo thông lượng và bộ nhớ đỉnh.",
"Dùng chung một kết nối cơ sở dữ liệu cho nhiều luồng · giả định thư viện an toàn luồng vì nó phổ biến · kiểm an toàn luồng bằng cách đọc mã.",
"Cả ba bản cho kết quả đúng qua 100 lần chạy 16 luồng, và có bảng thông lượng cùng bộ nhớ đỉnh."),

(56,"Bounded queues and the producer-consumer pattern","TH","Lesson 55",
"Hàng đợi có giới hạn là cấu trúc trung tâm của mọi pipeline chạy đồng thời. Bên sản xuất đẩy vào, bên tiêu thụ lấy ra, hàng đợi tách nhịp hai bên. Giới hạn kích thước là phần quan trọng nhất và hay bị bỏ: hàng đợi không giới hạn biến chênh lệch tốc độ thành tăng trưởng bộ nhớ, và tiến trình chết vì cạn bộ nhớ ở lesson 14 thay vì chậm lại. Hàng đợi đầy làm bên sản xuất bị chặn, đó chính là áp lực ngược, cùng cơ chế với ống dẫn ở lesson 20 và với cửa sổ nhận ở lesson 31. Chọn kích thước hàng đợi: đủ lớn để hấp thụ dao động, đủ nhỏ để lỗi lộ ra sớm và để giới hạn dữ liệu mất khi chết. Tín hiệu kết thúc và cách đóng hàng đợi sạch sẽ để bên tiêu thụ biết dừng. Nhiều bên tiêu thụ và bảo đảm mỗi phần tử được xử lý đúng một lần. Xác nhận sau khi xử lý xong chứ không khi lấy ra, nguyên tắc quyết định giữa mất và trùng, nối thẳng tới chặng 6.",
"Cài mẫu sản xuất tiêu thụ có hàng đợi giới hạn và chứng minh bằng đối soát rằng không mất và không nhân bản bản ghi dưới tải.",
"Tầng *áp dụng*. Objective có tiêu chí đối soát tuyệt đối dưới tải. Đạt khi chạy một triệu bản ghi với 8 bên tiêu thụ, số bản ghi ra bằng đúng số vào, không trùng, lặp lại 20 lần đều đúng. Một lần lệch là không đạt vì đây chính là lỗi module tồn tại để ngăn.",
"Cài sản xuất tiêu thụ với hàng đợi giới hạn 1.000. Chạy một triệu bản ghi với 8 bên tiêu thụ, đối soát, lặp 20 lần. Đổi sang hàng đợi không giới hạn với bên tiêu thụ chậm, quan sát bộ nhớ tăng tới khi bị giết. Đo thông lượng ở bốn kích thước hàng đợi.",
"Dùng hàng đợi không giới hạn · xác nhận phần tử khi lấy ra thay vì khi xử lý xong · quên tín hiệu kết thúc nên bên tiêu thụ treo.",
"20 lần chạy một triệu bản ghi với 8 bên tiêu thụ đều đối soát khớp tuyệt đối."),

(57,"Backpressure and what to do when downstream is slow","LT","Lesson 56",
"Áp lực ngược là tín hiệu từ hạ nguồn chậm truyền ngược lên thượng nguồn. Bốn phản ứng khi hạ nguồn không theo kịp và hậu quả của từng cái: chặn thượng nguồn giữ được toàn vẹn nhưng đẩy vấn đề lên trên, đệm thêm chỉ hoãn vấn đề và đổi nó thành cạn bộ nhớ, loại bớt bản ghi làm mất dữ liệu nên chỉ chấp nhận được cho một số loại dữ liệu, và mở rộng hạ nguồn là cách đúng nhưng chậm. Tiêu chí chọn theo loại dữ liệu: dữ liệu giao dịch không được loại, dữ liệu đo lường thì loại được. Vì sao hệ thống không có áp lực ngược sụp theo kiểu thác đổ thay vì chậm dần: hàng đợi phình, bộ nhớ cạn, tiến trình chết, việc dồn sang nút còn lại, nút đó cũng chết. Phát hiện áp lực ngược qua số đo: độ sâu hàng đợi tăng đều là chỉ báo sớm nhất, và nó phải được phát ra ngoài. Nối tới chặng 6: độ trễ tiêu thụ trong hệ thống luồng là cùng chỉ báo đó.",
"Chọn phản ứng phù hợp với áp lực ngược cho ba loại dữ liệu khác nhau và nêu hậu quả của lựa chọn.",
"Tầng *đánh giá*. Objective đòi chọn giữa bốn phương án theo ràng buộc nghiệp vụ, không có đáp án chung. Kiểm bằng ba tình huống: dữ liệu thanh toán, dữ liệu đo lường, dữ liệu nhật ký gỡ lỗi. Đạt khi mỗi lựa chọn nêu được hậu quả chấp nhận và hậu quả từ chối, và khi mô phỏng xác nhận hệ thống không sụp kiểu thác đổ.",
"Dựng pipeline ba chặng, làm chặng cuối chậm đi 10 lần. Thử bốn phản ứng, đo bộ nhớ, thông lượng và số bản ghi mất cho từng cái. Với ba loại dữ liệu, chọn phản ứng và viết một đoạn nêu hậu quả. Phát độ sâu hàng đợi ra ngoài và vẽ đồ thị.",
"Tăng kích thước đệm khi thấy hàng đợi đầy · loại bản ghi giao dịch để giữ thông lượng · không phát độ sâu hàng đợi nên không có chỉ báo sớm.",
"Ba lựa chọn đều nêu được hậu quả hai chiều, và mô phỏng cho thấy hệ thống chậm dần thay vì sụp kiểu thác đổ."),

(58,"Async IO - event loop, coroutines and when it wins","TH","Lesson 50",
"Vòng lặp sự kiện chạy trên một luồng và chuyển qua lại giữa các tác vụ tại điểm chờ. Hệ quả: một tác vụ chiếm bộ xử lý mà không nhường làm đứng toàn bộ vòng lặp, và đây là chế độ hỏng đặc trưng của mô hình bất đồng bộ. Hàm đồng quy và điểm nhường. Gọi hàm chặn bên trong mã bất đồng bộ là lỗi phổ biến nhất: nó chặn cả vòng lặp chứ không chỉ tác vụ đó, và cách phát hiện là đo thời gian giữa hai vòng lặp. Đẩy việc chặn sang nhóm luồng riêng. Giới hạn số tác vụ đồng thời bằng đèn hiệu, nếu không thì mở mười nghìn kết nối cùng lúc. Huỷ tác vụ và dọn dẹp, nối lại lesson 21. Khi nào bất đồng bộ thắng nhiều luồng: rất nhiều kết nối chờ vào ra, chi phí một tác vụ thấp hơn một luồng nhiều. Khi nào không thắng: ít kết nối, hoặc tải nghẽn tính toán. Trộn hai mô hình trong một chương trình và cái giá về độ phức tạp.",
"Viết ứng dụng khách bất đồng bộ gọi 10.000 yêu cầu có giới hạn đồng thời, và phát hiện được một lời gọi chặn lọt vào vòng lặp.",
"Tầng *áp dụng*. Objective gồm một sản phẩm và một phép chẩn đoán. Đạt khi 10.000 yêu cầu hoàn tất với số kết nối đồng thời không vượt giới hạn đặt ra, và khi người học đo được thời gian đứng vòng lặp trước và sau khi đẩy lời gọi chặn ra ngoài.",
"Viết ứng dụng khách bất đồng bộ gọi 10.000 yêu cầu, đèn hiệu giới hạn 50 đồng thời. Đếm kết nối thật bằng công cụ ở lesson 38. Cố ý gọi một hàm chặn trong vòng lặp, đo thời gian đứng. Đẩy nó sang nhóm luồng, đo lại. So thông lượng với bản nhiều luồng.",
"Gọi hàm chặn trong mã bất đồng bộ · không giới hạn số tác vụ đồng thời · dùng bất đồng bộ cho tải nghẽn tính toán.",
"10.000 yêu cầu hoàn tất không vượt giới hạn đồng thời, và thời gian đứng vòng lặp giảm đo được sau khi đẩy lời gọi chặn ra."),

(59,"Processes, shared memory and multiprocessing for CPU work","TH","Lesson 58",
"Nhiều tiến trình cho tải nghẽn tính toán, vì mỗi tiến trình có bộ thông dịch riêng nên không bị khoá thông dịch toàn cục chặn. Cái giá: mỗi tiến trình tốn bộ nhớ riêng, và truyền dữ liệu giữa các tiến trình phải tuần tự hoá. Chi phí tuần tự hoá thường lớn hơn người ta tưởng và có thể nuốt hết lợi ích song song khi dữ liệu lớn mà tính toán nhẹ, nên phải đo tỉ lệ giữa hai phần. Bộ nhớ chia sẻ để tránh sao chép, và mảng chia sẻ cho dữ liệu số. Sao chép khi ghi khi tạo tiến trình con và vì sao bộ nhớ thật tăng dần chứ không tăng ngay. Nhóm tiến trình và kích thước khối khi chia việc: khối quá nhỏ thì chi phí điều phối lớn, quá lớn thì mất cân bằng tải. Truyền dữ liệu qua tệp hoặc bộ nhớ chia sẻ thay vì qua hàng đợi khi dữ liệu lớn. Tiến trình con chết và cơ chế phát hiện, nối lại lesson 21.",
"Chọn giữa nhiều luồng và nhiều tiến trình cho một tải cho trước bằng số đo, và xác định kích thước khối cho thông lượng cao nhất.",
"Tầng *đánh giá*. Objective đòi chọn có căn cứ và tinh chỉnh một tham số, không có đáp án chung. Kiểm bằng bảng thực nghiệm: hai mô hình nhân ba kích thước khối nhân hai loại tải. Đạt khi lựa chọn dẫn được về số đo, và khi chi phí tuần tự hoá được tách ra khỏi thời gian tính toán.",
"Chạy một tải tính toán trên 10 triệu bản ghi theo hai mô hình, mỗi mô hình ba kích thước khối. Đo thời gian, bộ nhớ đỉnh, và riêng phần tuần tự hoá. Lặp lại với tải nghẽn vào ra. Lập bảng và chọn cấu hình cho từng loại tải.",
"Dùng nhiều tiến trình cho tải nghẽn vào ra · truyền khung dữ liệu lớn qua hàng đợi tiến trình · chọn kích thước khối bằng cảm tính.",
"Bảng thực nghiệm đủ hai mô hình nhân ba kích thước khối nhân hai loại tải, và chi phí tuần tự hoá được tách riêng."),

(60,"Proving correctness under load - the reconciliation habit","TH","Lesson 56",
"Chạy thử vài lần không chứng minh gì, vì tranh chấp có xác suất thấp và phụ thuộc máy. Bốn kỹ thuật chứng minh tính đúng đắn dưới tải. Một là đối soát: đếm bản ghi vào và ra, tổng theo khoá nghiệp vụ, và kiểm tính duy nhất của khoá, nối lại nguyên tắc ở chặng 4. Hai là kiểm thử bất biến: phát biểu tính chất phải luôn đúng rồi sinh đầu vào ngẫu nhiên để thử phá. Ba là bơm lỗi có chủ đích: giết tiến trình, làm chậm mạng, làm đầy đĩa ở thời điểm ngẫu nhiên và lặp nhiều lần. Bốn là chạy dưới công cụ phát hiện tranh chấp. Số lần lặp cần thiết để có ý nghĩa thống kê, và vì sao 10 lần là không đủ. Chạy trên nhiều cấu hình máy vì số lõi đổi thì cửa sổ tranh chấp đổi. Ghi lại hạt giống ngẫu nhiên để tái hiện được ca hỏng. Nguyên tắc: một pipeline chưa bị bơm lỗi là một pipeline chưa biết mình hỏng thế nào.",
"Thiết kế và chạy một bộ chứng minh tính đúng đắn cho một pipeline đồng thời, dùng cả bốn kỹ thuật.",
"Tầng *sáng tạo*. Objective là thiết kế một bộ kiểm chứng dưới ràng buộc, không phải chạy một bộ có sẵn. Kiểm bằng rà soát chéo: một học viên khác dùng bộ đó trên pipeline của mình và phải tìm ra được ít nhất một lỗi đã cài sẵn. Bộ không phát hiện được lỗi cài sẵn thì chưa đủ mạnh.",
"Viết bộ chứng minh cho pipeline ở lesson 56: đối soát, kiểm thử bất biến, bơm lỗi 200 lần ở thời điểm ngẫu nhiên, và chạy dưới công cụ phát hiện tranh chấp. Nhận pipeline của học viên khác có ba lỗi cài sẵn, chạy bộ của mình, báo cáo lỗi tìm được.",
"Chạy 10 lần rồi kết luận đúng · bơm lỗi ở thời điểm cố định nên bỏ sót cửa sổ hẹp · không ghi hạt giống nên không tái hiện được ca hỏng.",
"Bộ chứng minh tìm ra ít nhất một trong ba lỗi cài sẵn trong pipeline của học viên khác."),

(61,"Gate 2 - race timeline and the retry storm","KT","Lesson 60",
"Không có nội dung mới. Cổng 2 của chương trình.",
"Định vị một tranh chấp trong mã chưa từng thấy và vẽ dòng thời gian chứng minh nó, rồi giải thích vì sao thử lại không điều kiện gây đồng thời bão tải và bản ghi trùng.",
"Tầng *đánh giá*. Cổng đo năng lực lập luận về mã đồng thời và về hệ quả hệ thống, không đo trí nhớ API. Thang điểm: A 25đ định vị tranh chấp trong ba đoạn mã lạ · B 20đ dòng thời gian chứng minh cho một tranh chấp · C 20đ sửa và chứng minh bằng đối soát dưới tải · D 20đ giải thích bão tải và bản ghi trùng bằng cơ chế · E 15đ chọn phản ứng áp lực ngược cho một tình huống cho trước. Đạt khi ≥ 70/100, phần A ≥ 50% và phần C ≥ 50%.",
"150 phút. Ba đoạn mã lạ, một pipeline có lỗi cài sẵn, và một tình huống thiết kế. Sửa xong phải chứng minh bằng 200 lần chạy có bơm lỗi, không phải bằng lập luận.",
"Sửa bằng cách thêm khoá quanh mọi thứ rồi thông lượng sụp · chứng minh bằng lập luận thay vì bằng đối soát · giải thích bão tải mà bỏ mất vế bản ghi trùng.",
"Đạt ≥ 70/100, phần A ≥ 50% và phần C ≥ 50%."),
]
