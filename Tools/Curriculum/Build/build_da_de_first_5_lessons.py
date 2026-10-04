#!/usr/bin/env python3
"""Build runnable delivery assets for DA 001-005 and DE 001-005.

The substantive note.md files are inputs and are never modified. Delivery assets are
deterministically regenerated from the lesson definitions below.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml

from humanize_portal_corpus import editorial_prose, prose_transform, remove_course_timing

ROOT = Path(__file__).resolve().parents[3]
DA_ROOT = ROOT / "Material/DA/Curriculum/Phase_01-foundations-and-role/Module_01-introduction-to-the-data-analyst-role"
DE_ROOT = ROOT / "Material/DE/Curriculum/Phase_01-engineering-foundation/Module_01-engineering-thinking-git-and-debugging"


LESSONS = [
    {
        "role": "DA", "number": 1, "slug": "what-a-data-analyst-actually-does-all-day",
        "authoring_mode": "handcrafted",
        "title": "What a Data Analyst actually does all day",
        "question": "Data Analyst tạo giá trị ở đâu trong vòng đời từ yêu cầu đến quyết định?",
        "objective": "Phân loại nhiệm vụ theo sáu vai trò dữ liệu và bảo vệ ranh giới trách nhiệm bằng outcome, artifact và consumer.",
        "prerequisites": ["Không yêu cầu kỹ thuật; người học mang theo một ví dụ về quyết định từng thấy trong công việc hoặc đời sống."],
        "hook": "Giám đốc nói doanh thu tháng 10 giảm 12% và hỏi vì sao. Một dashboard đẹp có thể vẫn hoàn toàn vô dụng nếu mốc so sánh, dữ liệu thiếu và quyết định cần hỗ trợ chưa rõ.",
        "core": "DA không được định nghĩa bởi công cụ. DA biến một câu hỏi mơ hồ thành kết luận có kiểm chứng và hành động có chủ sở hữu.",
        "mechanism": [
            "Làm rõ quyết định, population, mốc so sánh và deadline trước khi chạm dữ liệu.",
            "Kiểm chứng con số và định nghĩa trước khi giải thích biến động.",
            "Tách nhiệm vụ theo artifact: pipeline, semantic model, dashboard, phân tích, dự báo hay đặc tả quy trình.",
        ],
        "first_action": "Hỏi người nhận sẽ dùng câu trả lời để quyết định điều gì và 12% được so với mốc nào.",
        "evidence": "Bảng phân vai 15 nhiệm vụ kèm lý do dựa trên outcome và artifact, không dựa trên tên công cụ.",
        "boundary": "Ở công ty nhỏ một người có thể đội nhiều mũ; vẫn phải gọi đúng vai đang thực hiện để biết invariant và bàn giao nào thuộc trách nhiệm đó.",
        "worked": [
            "Chuẩn hóa doanh thu theo số ngày và phát hiện chi nhánh Đà Nẵng thiếu 11 ngày dữ liệu.",
            "Tách mức giảm báo cáo 12% khỏi mức giảm thật 4% sau kiểm chứng.",
            "Xác định phần giảm tập trung ở khách mới, không phải khách cũ.",
            "Khuyến nghị ngân sách có mục tiêu và mở incident dữ liệu riêng cho chi nhánh.",
        ],
        "decision_rule": "Nếu yêu cầu hỏi chuyện gì xảy ra, vì sao và nên làm gì thì DA sở hữu phân tích; nếu lỗi nằm ở ingestion, định nghĩa dùng chung, theo dõi định kỳ, dự báo hoặc quy trình thì phải có vai tương ứng đồng sở hữu.",
        "critical_failure": "Gán vai theo công cụ, hoặc gửi output không nói quyết định nào sẽ thay đổi.",
        "change": "Nếu công ty chỉ có một người dữ liệu, phạm vi thực thi rộng lên nhưng tiêu chí bàn giao của từng vai không biến mất.",
        "guided_task": "Phân loại tám thẻ việc: sửa pipeline mất dữ liệu, định nghĩa revenue, dashboard ngày, phân tích churn, dự báo churn, đặc tả hoàn tiền, đối soát hai báo cáo, trình bày khuyến nghị.",
        "guided_success": "Ít nhất 6/8 thẻ đúng và mỗi lý do gọi tên outcome hoặc artifact bàn giao.",
        "independent": "Phân loại 15 nhiệm vụ của một đội thương mại điện tử; đánh dấu ba vùng cần đồng sở hữu và viết RACI tối thiểu.",
        "transfer": "Một startup 20 người tuyển 'Data Analyst' nhưng JD gồm Airflow, dbt, Power BI và churn model. Hãy tách bốn vai, rủi ro và thứ tự tuyển/bàn giao.",
        "exit_q": "Data Analyst khác Data Engineer ở đâu, và vì sao ranh giới vẫn có thể chồng lấn?",
        "exit_a": "DA sở hữu câu trả lời và khuyến nghị; DE sở hữu dòng dữ liệu tin cậy. Chồng lấn xuất hiện ở kiểm chứng và lỗi dữ liệu, nên cần phân biệt lỗi hệ thống với logic nghiệp vụ.",
        "next": "L002 — theo dấu một con số qua vòng đời dữ liệu.",
        "sections": ["II. Bối cảnh và vấn đề đặt ra", "III. Cơ sở lý thuyết và cơ chế vận hành", "IV. Khung quyết định và tiêu chí lựa chọn", "V. Nghiên cứu tình huống: quay lại câu \"doanh thu giảm 12%\"", "VI. Giới hạn và ngộ nhận phổ biến"],
        "homework_input": "Một công ty bán lẻ có yêu cầu: sửa dữ liệu POS thiếu, thống nhất net revenue, dự báo tồn kho, dựng dashboard ngày, điều tra tỷ lệ hoàn đơn tăng và viết quy trình duyệt hoàn tiền.",
        "homework_artifact": "Ma trận nhiệm vụ × vai trò × artifact × consumer × ranh giới bàn giao, kèm memo 300-500 từ về hai vùng chồng lấn.",
        "facts": [
            ("Phần giá trị cao nhất của DA là gì?", "Biến câu hỏi thành kết luận kiểm chứng được và hành động cụ thể."),
            ("Vì sao phải kiểm chứng con số trước khi giải thích?", "Một thay đổi có thể đến từ thiếu dữ liệu hoặc khác định nghĩa, không phải hành vi kinh doanh."),
            ("Artifact điển hình của AE là gì?", "Mô hình dữ liệu và định nghĩa chỉ số dùng chung."),
            ("Khi nào một yêu cầu gần với BI Analyst?", "Khi cần theo dõi chỉ số ổn định, lặp lại và có trạng thái tương tác rõ."),
            ("Nguyên tắc phân chia lỗi dữ liệu giữa DA và DE là gì?", "Lỗi hệ thống sinh ra sửa gần pipeline; cách hiểu nghiệp vụ xử lý ở lớp phân tích/semantic."),
            ("Tỉ lệ 20/40/20/15/5 nên được hiểu thế nào?", "Là mốc định hướng có thể đổi theo tuần và tổ chức, không phải chuẩn đánh giá cá nhân."),
        ],
    },
    {
        "role": "DA", "number": 2, "slug": "where-data-comes-from-and-the-stages-it-passes-through",
        "title": "Where data comes from and the stages it passes through",
        "question": "Một con số đã bị biến đổi ở đâu từ sự kiện nghiệp vụ đến quyết định?",
        "objective": "Tái dựng vòng đời bảy chặng và định vị cơ chế sai lệch cùng bằng chứng kiểm tra tại từng boundary.",
        "prerequisites": ["DA-L001: phân biệt câu hỏi phân tích với trách nhiệm của các vai dữ liệu."],
        "hook": "Dashboard báo khách hoạt động giảm, nhưng source ghi đơn tạo, vận hành đếm đơn thanh toán còn CRM đếm phiên truy cập. Ba số đúng theo code nhưng không cùng khái niệm.",
        "core": "Con số phân tích là một chuỗi biến đổi có lineage; muốn tin kết luận phải nối event, record, storage, transform, metric, presentation và decision bằng các phép đối soát.",
        "mechanism": [
            "Tách sự kiện thật khỏi bản ghi nguồn và bảng phân tích.",
            "Khóa population, grain, event time/cutoff và định nghĩa metric ở mỗi boundary.",
            "Đối soát gần nguồn nhất còn giữ bằng chứng thay vì vá công thức cuối.",
        ],
        "first_action": "Viết event nghiệp vụ, population, grain và cutoff mà con số tuyên bố đại diện.",
        "evidence": "Bảng lineage bảy chặng với input, output, owner, failure mode và reconciliation check cho cùng một giao dịch.",
        "boundary": "Lineage mô tả đường đi và biến đổi; nó không tự chứng minh completeness nếu không có count, checksum hoặc oracle độc lập.",
        "worked": [
            "Đặt ba định nghĩa 'active customer' cạnh nhau trên cùng snapshot.",
            "Theo một khách từ click, order_created, payment_success tới mart và dashboard.",
            "So count và distinct identity sau mỗi join/filter để tìm chặng làm mất tín hiệu.",
            "Đổi câu hỏi từ 'khách giảm' thành 'conversion tạo đơn → thanh toán giảm ở thiết bị nào'.",
        ],
        "decision_rule": "Khi hai số lệch, đi ngược lineage và kiểm boundary đầu tiên chúng bắt đầu khác; chỉ sửa downstream sau khi cơ chế upstream đã được xác nhận.",
        "critical_failure": "Dùng tên bảng như bằng chứng về nghĩa dữ liệu, hoặc sửa dashboard cho khớp một tổng không độc lập.",
        "change": "Khi dữ liệu đến muộn, phải tách event time, processing time và cutoff; con số hôm nay có thể đúng theo snapshot nhưng chưa final.",
        "guided_task": "Xếp 14 thẻ artifact vào bảy chặng và nối mỗi chặng với một failure mode: missing event, duplicate, timezone, filter, join fan-out, stale cache, wrong action.",
        "guided_success": "Đúng ≥ 12/14 thẻ và nêu được một phép kiểm độc lập tại ít nhất năm boundary.",
        "independent": "Lập trace table cho một giao dịch từ checkout tới weekly revenue dashboard; ghi row count, distinct key, timestamp và owner ở mỗi chặng.",
        "transfer": "Dashboard retention giảm đúng ngày đổi SDK. Thiết kế thứ tự kiểm chứng để phân biệt hành vi thật, mất event và đổi identity.",
        "exit_q": "Vì sao lineage không đồng nghĩa dữ liệu đúng?",
        "exit_a": "Lineage chỉ nói đường đi; correctness cần invariant và reconciliation độc lập tại boundary.",
        "next": "L003 — khóa entity, record và grain trước khi đếm hoặc join.",
        "sections": ["Nỗi Đau & Động Lực", "Cơ Chế Tác Động", "Bản Đồ Quyết Định", "Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường", "Góc Khuất & Ngộ Nhận"],
        "homework_input": "Fixture gồm 12 event checkout, 10 order_created, 9 payment_success, 10 dòng raw do một event trùng, 8 dòng mart sau filter và dashboard hiển thị 7 do cache cũ.",
        "homework_artifact": "Lineage table bảy chặng, reconciliation report giải thích từng chênh lệch và memo nêu boundary đầu tiên cần sửa.",
        "facts": [
            ("Ba lớp nào dễ bị đánh đồng?", "Sự kiện nghiệp vụ, bản ghi nguồn và bảng phục vụ phân tích."),
            ("Khi hai nguồn lệch, nên bắt đầu ở đâu?", "Boundary gần nguồn nhất còn giữ được bằng chứng độc lập."),
            ("Event time khác processing time thế nào?", "Event time là lúc nghiệp vụ xảy ra; processing time là lúc hệ thống xử lý bản ghi."),
            ("Một phép reconciliation tốt cần gì?", "Oracle hoặc tổng kiểm không dùng cùng logic biến đổi đang được kiểm."),
            ("Stale dashboard cache thuộc chặng nào?", "Presentation/serving, sau khi metric có thể đã đúng ở mart."),
            ("Vì sao không vá công thức cuối?", "Nó che cơ chế upstream và khiến consumer khác tiếp tục dùng dữ liệu sai."),
        ],
    },
    {
        "role": "DA", "number": 3, "slug": "entities-attributes-records-and-grain",
        "title": "Entities, attributes, records and grain",
        "question": "Mỗi dòng đại diện cho điều gì và phép tính nào hợp lệ ở grain đó?",
        "objective": "Phát biểu và kiểm chứng grain, khóa ứng viên, rồi định lượng fan-out khi ghép hai bảng khác grain.",
        "prerequisites": ["DA-L002: nhận diện event, record và transform trong vòng đời dữ liệu."],
        "hook": "Một đơn có ba dòng sản phẩm. Join orders với order_items rồi SUM(order_total) làm doanh thu tăng gấp ba dù query chạy hoàn hảo.",
        "core": "Grain là lời cam kết mỗi dòng đại diện cho điều gì; mọi phép đếm, join và aggregate phải được chứng minh tương thích với lời cam kết đó.",
        "mechanism": [
            "Xác định entity và một câu grain đầy đủ có thời gian/trạng thái khi cần.",
            "Kiểm uniqueness của khóa ứng viên và phân phối số dòng trên mỗi key.",
            "Dự đoán cardinality trước join, đo fan-out sau join và aggregate về grain chung trước khi kết hợp.",
        ],
        "first_action": "Viết câu 'mỗi dòng đại diện cho…' và khóa ứng viên trước bất kỳ SUM hoặc JOIN nào.",
        "evidence": "Bảng kiểm grain gồm candidate key, uniqueness, row count, distinct key, join multiplicity và reconciliation total.",
        "boundary": "Khóa duy nhất về kỹ thuật chưa đủ nếu một dòng vẫn trộn nhiều trạng thái nghiệp vụ hoặc snapshot time khác nhau.",
        "worked": [
            "Orders ở grain một dòng/đơn; items ở grain một dòng/sản phẩm trong đơn.",
            "Dự đoán join one-to-many và đánh dấu order_total không additive sau join.",
            "Aggregate items về order_id hoặc chỉ lấy order_total một lần trên orders.",
            "Đối soát doanh thu và số đơn trước/sau join bằng oracle riêng.",
        ],
        "decision_rule": "Nếu hai bảng khác grain, hoặc aggregate bảng nhiều về grain một trước join, hoặc giữ measure ở bảng sở hữu; không SUM measure phía một sau join many.",
        "critical_failure": "Suy grain từ tên bảng, dùng DISTINCT để che fan-out hoặc coi primary key kỹ thuật là nghĩa nghiệp vụ.",
        "change": "Nếu yêu cầu chuyển từ đơn sang khách-tháng, phải công bố grain mới và rule phân bổ trước khi tổng hợp.",
        "guided_task": "Cho năm schema nhỏ; viết grain, candidate key, cardinality dự kiến và một query/profile chứng minh cho từng bảng.",
        "guided_success": "5/5 câu grain có entity + thời gian/trạng thái phù hợp và mỗi câu có phép kiểm uniqueness/fan-out tương ứng.",
        "independent": "Chẩn đoán workbook doanh thu bị thổi phồng 18%; tái cấu trúc phép join và lập reconciliation trước/sau.",
        "transfer": "Một bảng customer_address lưu lịch sử hiệu lực. Chọn grain và join rule để gán đúng địa chỉ tại thời điểm order.",
        "exit_q": "Tại sao DISTINCT không phải cách sửa mặc định cho fan-out?",
        "exit_a": "DISTINCT có thể xóa record hợp lệ và che mismatch grain; phải sửa cardinality hoặc aggregate về grain đúng.",
        "next": "L004 — phân rã outcome thành metric tree có driver hành động được.",
        "sections": ["Nỗi Đau & Động Lực", "Cơ Chế Tác Động", "Bản Đồ Quyết Định", "Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường", "Góc Khuất & Ngộ Nhận"],
        "homework_input": "Ba bảng orders, order_items và payments với một đơn nhiều item, một đơn trả góp hai payment và một payment hoàn một phần.",
        "homework_artifact": "Grain contract cho ba bảng, sơ đồ cardinality, hai query/pseudocode an toàn và reconciliation chứng minh không double count.",
        "facts": [
            ("Grain là gì?", "Lời cam kết một dòng đại diện cho đối tượng/sự kiện nào trong boundary đã nêu."),
            ("Dấu hiệu trực tiếp của fan-out là gì?", "Row count hoặc multiplicity trên base key tăng sau join."),
            ("Measure phía one nên xử lý thế nào trước one-to-many join?", "Giữ ở bảng sở hữu hoặc aggregate phía many về cùng grain trước khi ghép."),
            ("Candidate key cần được kiểm bằng gì?", "Count so với count distinct cùng kiểm NULL và duplicate distribution."),
            ("Primary key kỹ thuật chứng minh điều gì?", "Chỉ chứng minh định danh row, không tự chứng minh nghĩa nghiệp vụ của grain."),
            ("Khi nào COUNT(DISTINCT customer_id) hợp lệ?", "Khi population, identity, thời gian và status của customer đã được khóa."),
        ],
    },
    {
        "role": "DA", "number": 4, "slug": "three-tiers-of-questions-and-the-metric-tree",
        "title": "Three tiers of questions and the metric tree",
        "question": "Làm sao đi từ outcome biến động tới driver có owner và hành động?",
        "objective": "Dựng metric tree cân bằng số học, nối descriptive-diagnostic-prescriptive questions và bảo vệ driver bằng owner cùng lever.",
        "prerequisites": ["DA-L003: grain và additivity của measure."],
        "hook": "Revenue giảm 8%. Chia theo mọi dimension tạo 40 biểu đồ nhưng không cho biết driver nào có thể can thiệp.",
        "core": "Metric tree là mô hình giả thuyết định lượng: outcome được phân rã thành driver có thể đo, có owner và lever; ba tầng câu hỏi dẫn từ quan sát tới quyết định.",
        "mechanism": [
            "Bắt đầu từ decision/outcome và viết identity toán học hoặc quan hệ nhân quả có điều kiện.",
            "Phân rã driver đến mức đo được và can thiệp được, tránh trộn stock, flow và rate.",
            "Đi từ descriptive sang diagnostic rồi prescriptive; mỗi nhánh có owner, evidence và reversal trigger.",
        ],
        "first_action": "Xác định quyết định và công thức outcome trước khi chọn dimension để cắt lát.",
        "evidence": "Metric tree cân bằng trên fixture, mỗi lá có definition, grain, owner, lever và test cộng/nhân lại outcome.",
        "boundary": "Metric tree biểu diễn giả thuyết và identity; nó không chứng minh quan hệ nhân quả chỉ vì các nhánh cộng đúng.",
        "worked": [
            "Revenue = Orders × Average Order Value.",
            "Orders = Traffic × Conversion Rate; AOV = Items/Order × Price/Item.",
            "Đối chiếu đóng góp driver với mức giảm 8% và giữ interaction/residual.",
            "Chọn lever checkout conversion vì có owner, đủ volume và cost thử nghiệm thấp hơn giảm giá toàn site.",
        ],
        "decision_rule": "Chỉ đưa driver vào nhánh hành động khi definition và grain ổn định, có owner/lever, và contribution đủ lớn so với uncertainty và cost can thiệp.",
        "critical_failure": "Cây chỉ là taxonomy đẹp, lá không có owner, hoặc diễn giải tương quan như nguyên nhân.",
        "change": "Nếu margin thay revenue làm outcome, discount có thể đổi từ lever tích cực thành driver phá giá trị; cây phải được dựng lại theo decision.",
        "guided_task": "Dựng cây revenue cho marketplace từ GMV tới traffic, conversion, orders, AOV, take rate và refunds; đánh dấu stock/flow/rate.",
        "guided_success": "Cây cân bằng trên số mẫu, không double count, mọi lá có owner và ít nhất một lever kiểm được.",
        "independent": "Dựng ba cây cho subscription, marketplace và vận hành giao hàng; viết một câu hỏi ở mỗi tầng cho từng cây.",
        "transfer": "Conversion giảm nhưng revenue tăng do AOV. Quyết định ưu tiên driver nào khi mục tiêu đổi từ tăng trưởng sang contribution margin?",
        "exit_q": "Một metric tree cộng đúng đã đủ để kết luận nguyên nhân chưa?",
        "exit_a": "Chưa. Identity mô tả đóng góp số học; causal claim cần thiết kế bằng chứng riêng và loại trừ confounder.",
        "next": "L005 — biến yêu cầu mơ hồ thành analytical contract trả lời được.",
        "sections": ["Nỗi Đau & Động Lực", "Cơ Chế Tác Động", "Bản Đồ Quyết Định", "Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường", "Góc Khuất & Ngộ Nhận"],
        "homework_input": "Subscription có MRR giảm từ 1,00 tỷ xuống 0,94 tỷ; new MRR 0,08; expansion 0,03; contraction 0,05; churn 0,12 (tỷ đồng).",
        "homework_artifact": "Metric tree MRR có reconciliation, owner/lever cho từng lá, ba tầng câu hỏi và recommendation có uncertainty/reversal trigger.",
        "facts": [
            ("Ba tầng câu hỏi là gì?", "Descriptive: chuyện gì; diagnostic: vì sao; prescriptive: nên làm gì."),
            ("Điều kiện tối thiểu của một lá cây chỉ số?", "Definition, grain, owner, lever và bằng chứng đo."),
            ("Revenue có thể phân rã cơ bản thế nào?", "Orders nhân Average Order Value."),
            ("Vì sao phải giữ residual/interaction?", "Để không ép toàn bộ biến động vào driver khi identity hoặc tương tác không giải thích hết."),
            ("Metric tree chứng minh điều gì mạnh nhất?", "Sự nhất quán số học và cấu trúc giả thuyết, không tự chứng minh nhân quả."),
            ("Khi nào dừng phân rã?", "Khi lá đủ đo, đủ owner và đủ lever để hỗ trợ quyết định với cost hợp lý."),
        ],
    },
    {
        "role": "DA", "number": 5, "slug": "from-a-vague-request-to-an-answerable-question",
        "title": "From a vague request to an answerable question",
        "question": "Làm sao chuyển yêu cầu mơ hồ thành analytical contract có thể bác bỏ?",
        "objective": "Viết contract khóa decision, population, metric, comparison, time, slices, constraints và acceptance trước khi phân tích.",
        "prerequisites": ["DA-L002: lineage", "DA-L003: grain", "DA-L004: metric tree và ba tầng câu hỏi."],
        "hook": "Câu 'phân tích giúp vì sao khách giảm' có ít nhất năm nghĩa của khách, ba cửa sổ thời gian và nhiều quyết định khác nhau.",
        "core": "Một câu hỏi trả lời được phải nêu ai sẽ quyết định gì, trên population nào, bằng metric/comparison nào, trong time boundary nào và bằng chứng nào đủ để dừng.",
        "mechanism": [
            "Bắt đầu bằng decision và action threshold, không bắt đầu bằng danh sách biểu đồ.",
            "Khóa population, identity/grain, metric, comparison, time, segments và exclusions.",
            "Ghi assumptions, unknowns, non-goals, deliverable, deadline và acceptance check có thể bác bỏ.",
        ],
        "first_action": "Hỏi 'ai sẽ làm gì khác đi nếu kết quả cao, thấp hoặc chưa đủ chắc chắn?'.",
        "evidence": "Một analytical contract một trang và test bằng hai reviewer độc lập tạo cùng expected output từ cùng fixture.",
        "boundary": "Contract khóa nghĩa và tiêu chí; nó không bảo đảm source có đủ dữ liệu hay kết luận sẽ có causal strength mong muốn.",
        "worked": [
            "Đổi 'khách giảm' thành paid customers tháng 9 so tháng 8 theo event time ICT, chốt D+3.",
            "Định nghĩa paid customer là distinct customer_id có payment_success, loại test/refund toàn phần.",
            "Slice theo acquisition channel và device vì owner có lever tương ứng.",
            "Acceptance: reconcile với finance ±0,5%; nếu coverage <98% thì trả lời có điều kiện.",
        ],
        "decision_rule": "Unknown làm đổi semantics, blast radius hoặc acceptance phải chặn execution; unknown định lượng được có thể đi tiếp với coverage và limitation công khai.",
        "critical_failure": "Tự điền định nghĩa để kịp deadline, hoặc nhận deliverable 'dashboard' trước khi biết decision.",
        "change": "Nếu deadline từ ba ngày xuống hai giờ, co scope và strength of claim; không âm thầm hạ correctness gate.",
        "guided_task": "Phỏng vấn role-play: stakeholder chỉ nói 'campaign vừa rồi có hiệu quả không?'; nhóm có 12 phút để tạo contract và read-back.",
        "guided_success": "Contract đủ tám trường semantic, có non-goal, acceptance và ít nhất một unknown với owner.",
        "independent": "Viết contract một trang cho yêu cầu retention giảm; đổi một constraint rồi cập nhật scope, test và deliverable.",
        "transfer": "CEO muốn câu trả lời trong hai giờ nhưng identity khách đa thiết bị chưa được giải quyết. Chọn dừng, co claim hay dùng proxy và nêu điều kiện.",
        "exit_q": "Unknown nào bắt buộc phải chặn phân tích?",
        "exit_a": "Unknown có thể đổi nghĩa population/metric, blast radius hoặc tiêu chí đạt; identity chưa rõ là ví dụ điển hình.",
        "next": "DA-L006 — cấu trúc dữ liệu đúng trong Excel theo contract đã khóa.",
        "sections": ["Nỗi Đau & Động Lực", "Cơ Chế Tác Động", "Bản Đồ Quyết Định", "Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường", "Góc Khuất & Ngộ Nhận"],
        "homework_input": "Yêu cầu thô: 'Retention tháng này xấu, xem giúp và làm dashboard trước cuộc họp sáng mai'. Identity đa thiết bị chưa thống nhất; event mobile trễ tối đa 36 giờ.",
        "homework_artifact": "Analytical contract một trang, assumption ledger, read-back cho stakeholder và bản sửa khi deadline bị rút còn hai giờ.",
        "facts": [
            ("Trường đầu tiên của analytical contract là gì?", "Decision và hành động mà kết quả sẽ hỗ trợ."),
            ("Vì sao comparison phải ghi rõ?", "So với kỳ trước, cùng kỳ hay target có thể tạo kết luận trái nhau."),
            ("Một unknown khi nào là blocker?", "Khi nó làm đổi semantics, blast radius hoặc acceptance criteria."),
            ("Non-goal có tác dụng gì?", "Ngăn scope mở rộng âm thầm và làm rõ phần chưa được kết luận."),
            ("Read-back kiểm điều gì?", "Stakeholder và analyst có cùng hiểu decision, definition, deliverable và giới hạn hay không."),
            ("Deadline ngắn nên thay đổi gì?", "Thu hẹp scope/claim hoặc dùng proxy công khai, không hạ correctness gate âm thầm."),
        ],
    },
    {
        "role": "DE", "number": 1, "slug": "from-a-vague-request-to-a-testable-contract",
        "authoring_mode": "handcrafted",
        "title": "From a vague request to a testable contract",
        "question": "Làm sao biến yêu cầu kỹ thuật mơ hồ thành behavior và acceptance check có thể tái hiện?",
        "objective": "Viết testable contract khóa decision, boundary, input/output, invariants, failure behavior và evidence trước mutation.",
        "prerequisites": ["Foundation: đọc được pseudocode, bảng dữ liệu và command-line cơ bản; chưa giả định kinh nghiệm production."],
        "hook": "Yêu cầu 'đồng bộ orders nhanh và không trùng' không nói nhanh bao nhiêu, order nào, identity nào hay retry sau timeout phải quan sát gì.",
        "core": "Contract kiểm thử được mô tả behavior quan sát được trong boundary rõ, gồm precondition, input, transformation, expected output, failure semantics và acceptance evidence.",
        "mechanism": [
            "Bắt đầu từ quyết định và consumer harm, rồi khóa scope/non-goal.",
            "Viết identity, state, time, input/output và invariant đủ để reviewer dựng expected result.",
            "Gắn mỗi requirement với acceptance check và owner; unknown làm đổi semantics phải chặn mutation.",
        ],
        "first_action": "Hỏi consumer cần behavior nào và failure nào không được phép xảy ra.",
        "evidence": "Hai reviewer độc lập tạo cùng expected output từ fixture và trace mỗi failed check về requirement/owner.",
        "boundary": "Contract tốt không thay thế thiết kế hay test runtime; nó định nghĩa điều các bước đó phải chứng minh.",
        "worked": [
            "Định nghĩa order identity = source + order_id; event time và D+1 cutoff.",
            "Success: mỗi identity xuất hiện đúng một lần ở curated table trong 10 phút.",
            "Timeout có outcome unknown; retry phải idempotent và đối soát bằng run_id.",
            "Non-goal: không backfill trước ngày X; change request nếu stakeholder mở rộng.",
        ],
        "decision_rule": "Nếu thiếu identity, state transition hoặc failure semantics thì dừng; nếu chỉ thiếu threshold tối ưu có thể pilot trong bounded range và giữ reversal trigger.",
        "critical_failure": "Viết acceptance bằng từ mơ hồ như nhanh/ổn định, hoặc để implementation tự quyết semantics.",
        "change": "Khi SLO từ 10 phút xuống 30 giây, contract buộc lộ thay đổi kiến trúc thay vì coi đây là tuning nhỏ.",
        "guided_task": "Biến sáu câu requirement mơ hồ thành Given/When/Then có fixture, invariant và failure path.",
        "guided_success": "Mỗi check có input cụ thể, expected result duy nhất, oracle và requirement ID; không dùng từ định tính chưa có threshold.",
        "independent": "Viết contract cho job ingest orders có retry, late data và delete; thêm traceability matrix hai chiều.",
        "transfer": "API trả 202 nhưng commit outcome unknown. Định nghĩa behavior client, idempotency key và evidence phân biệt accepted với completed.",
        "exit_q": "Vì sao 'pipeline không được trùng dữ liệu' chưa phải acceptance criterion?",
        "exit_a": "Chưa có identity, boundary, time, trạng thái và phép đếm/oracle nên không thể tạo expected output duy nhất.",
        "next": "DE-L002 — phân rã responsibility, interface, state và failure domain.",
        "sections": ["1. Bắt đầu từ quyết định, không bắt đầu từ giải pháp", "2. Sáu phần của một phát biểu kiểm thử được", "3. Từ requirement tới acceptance check", "6. Definition of Ready và điểm dừng", "8. Failure modes và ngộ nhận"],
        "homework_input": "Requirement thô: 'Đồng bộ orders từ API sang warehouse nhanh, không mất, không trùng; API có pagination, rate limit và timeout sau khi đã nhận request'.",
        "homework_artifact": "Contract có scope/non-goal, schema/identity/time, success/failure semantics, 8 acceptance checks và traceability matrix.",
        "facts": [
            ("Một expected output tốt phải có tính chất gì?", "Hai reviewer độc lập suy ra cùng kết quả từ cùng fixture."),
            ("Identity thiếu gây rủi ro gì?", "Dedup và replay có thể xanh giả vì không biết hai record có cùng thực thể hay không."),
            ("Traceability hai chiều là gì?", "Requirement tới test/artifact và failed evidence quay về đúng requirement/owner."),
            ("Non-goal bảo vệ điều gì?", "Boundary và change control khỏi mở rộng scope âm thầm."),
            ("Outcome unknown cần xử lý thế nào?", "Dùng idempotency/reconciliation để xác định trạng thái trước retry mù."),
            ("Definition of Ready chặn khi nào?", "Khi input bắt buộc làm đổi semantics, risk hoặc acceptance chưa được giải quyết."),
        ],
    },
    {
        "role": "DE", "number": 2, "slug": "decomposition-responsibility-interface-state-and-failure-domain",
        "title": "Decomposition: responsibility, interface, state and failure domain",
        "question": "Làm sao chia hệ thành boundary thay đổi và hỏng theo cách có thể kiểm chứng?",
        "objective": "Phân rã hệ theo responsibility, interface, state, dependency direction và failure domain; kiểm bằng change/fault scenarios.",
        "prerequisites": ["DE-L001: testable contract và acceptance evidence."],
        "hook": "Tách monolith thành ba service nhưng cả ba dùng chung database và credential: network tăng, blast radius không giảm.",
        "core": "Boundary tốt gom invariant và lý do thay đổi, thu hẹp interface, có owner state rõ và làm failure propagation quan sát/kiểm soát được.",
        "mechanism": [
            "Dùng change scenario để tìm responsibility và cohesion thay vì chỉ chia theo technical layer.",
            "Thiết kế interface bằng operation, semantics, errors và invariants tối thiểu.",
            "Gắn state với authoritative writer/lifecycle; trace fault tới consumer harm và recovery.",
        ],
        "first_action": "Liệt kê invariants và các thay đổi độc lập, rồi hỏi phần nào phải đổi cùng nhau.",
        "evidence": "Context/component diagram, interface contract, state ownership table, dependency DAG và ba fault traces.",
        "boundary": "Deployment unit không tự tạo failure isolation; shared database, queue hoặc credential vẫn có thể nối blast radius.",
        "worked": [
            "Tách order intent, payment adapter và fulfillment theo invariant/lifecycle.",
            "Order là authoritative owner của state machine; payment trả outcome contract thay vì ORM object.",
            "Timeout payment không làm mất order intent; retry dựa trên idempotency key.",
            "Dependency đi từ domain policy ra ports; adapter phụ thuộc contract, không ngược lại.",
        ],
        "decision_rule": "Tách boundary khi change cadence, invariant/state ownership hoặc fault containment khác nhau và cost network/operation được biện minh.",
        "critical_failure": "Chia theo folder/service aesthetic, để nhiều writer cho cùng state hoặc public interface lộ storage detail.",
        "change": "Đổi database không được buộc domain import driver type; nếu có, dependency direction đang sai.",
        "guided_task": "Phân rã order-payment-fulfillment trên bốn trục; inject timeout payment và database outage rồi trace impact.",
        "guided_success": "Mỗi component có một responsibility, interface tối thiểu, state owner, dependencies không vòng và failure trace tới recovery.",
        "independent": "Thiết kế decomposition cho ingestion service gồm fetch, normalize, dedup, publish và checkpoint; bảo vệ quyết định trước hai fault.",
        "transfer": "Hai team cần đổi schema với cadence khác nhưng dùng chung dedup ledger. Chọn tách ở đâu và ai sở hữu migration/recovery.",
        "exit_q": "Vì sao tách process chưa chắc giảm failure domain?",
        "exit_a": "Các process có thể vẫn chung dependency/state/credential; fault ở shared resource tiếp tục ảnh hưởng tất cả.",
        "next": "DE-L003 — ghi trade-off và reversal trigger bằng ADR.",
        "sections": ["1. Ranh giới bắt đầu từ responsibility", "2. Interface là lời hứa tối thiểu", "3. State quyết định độ khó thay thế", "4. Failure domain không đồng nghĩa deployment unit", "8. Failure modes và ngộ nhận"],
        "homework_input": "Hệ ingest có API poller, parser, dedup, validator, publisher và checkpoint; hiện tất cả cùng process, cùng database, retry toàn job.",
        "homework_artifact": "Decomposition dossier gồm responsibility map, interface/state table, dependency DAG, ba failure traces và một changed-requirement analysis.",
        "facts": [
            ("Responsibility nên được tìm bằng gì?", "Invariant và lý do thay đổi nghiệp vụ/vận hành, không chỉ technical layer."),
            ("Interface tối thiểu phải nêu gì?", "Operation, input/output semantics, error contract và invariant caller được dựa vào."),
            ("Authoritative writer có tác dụng gì?", "Ngăn nhiều component cập nhật cùng state machine mà không có protocol."),
            ("Failure domain được xác định thế nào?", "Trace fault qua dependency/state tới consumer harm và recovery."),
            ("Abstraction leak là gì?", "Caller vẫn phải biết chi tiết mà boundary tuyên bố đã che."),
            ("Dependency cycle báo hiệu gì?", "Ownership/abstraction chưa rõ và thay đổi có thể lan hai chiều."),
        ],
    },
    {
        "role": "DE", "number": 3, "slug": "trade-offs-and-the-architecture-decision-record",
        "title": "Trade-offs and the architecture decision record",
        "question": "Làm sao lưu reasoning để quyết định kỹ thuật có thể được tái tạo và xét lại?",
        "objective": "Viết ADR ngắn nhưng đủ context, drivers, options, evidence, consequences, decision và revisit signal.",
        "prerequisites": ["DE-L001: contract", "DE-L002: boundary, state và failure domain."],
        "hook": "ADR chỉ ghi 'chọn Parquet' khiến đội sau không biết workload nào, option nào bị loại hay constraint nào đã đổi.",
        "core": "ADR lưu context và reasoning tại thời điểm quyết định; chất lượng nằm ở option thật, hard constraints, evidence phân biệt và điều kiện đảo quyết định.",
        "mechanism": [
            "Khóa decision drivers và hard constraints trước khi chấm option.",
            "Mô tả ít nhất hai option trong điều kiện tốt nhất, gồm failure mode và evidence có thể đảo đánh giá.",
            "Ghi consequences, owner, reversibility, confirmation và measurable revisit signal.",
        ],
        "first_action": "Viết context, decision scope và hard constraints trước khi nêu phương án yêu thích.",
        "evidence": "Reviewer tái tạo recommendation từ drivers/evidence và changed constraint làm recommendation đảo đúng rule.",
        "boundary": "ADR không thay thế benchmark, spike hay approval; nó liên kết evidence đó với quyết định phiên bản cụ thể.",
        "worked": [
            "So CSV, JSONL và Parquet cho batch analytical exchange.",
            "Hard gate: schema/type fidelity và reader compatibility; optimize scan cost sau gate.",
            "Spike đo file size, scan latency, schema evolution và operability trên fixture thật.",
            "Chọn Parquet, nhận debt inspection tooling; revisit nếu consumer không đọc được hoặc volume giảm dưới threshold.",
        ],
        "decision_rule": "Loại option vi phạm hard constraint trước; trong số option còn lại ưu tiên evidence, reversibility và total cost, không dùng weighted score để bù vi phạm cấm.",
        "critical_failure": "Viết ADR sau khi đã chọn để hợp thức hóa, dùng strawman hoặc không ghi consequence/revisit signal.",
        "change": "Nếu consumer chính chuyển sang spreadsheet không hỗ trợ Parquet, compatibility gate có thể đảo quyết định dù benchmark không đổi.",
        "guided_task": "Điền ADR one-page cho format trao đổi dữ liệu từ evidence packet; mỗi nhóm đóng vai reviewer tấn công một assumption.",
        "guided_success": "ADR dưới hai trang, có ≥2 option thật, hard constraints, evidence, consequence owner và measurable revisit signal.",
        "independent": "Viết ADR chọn scheduler cho ba workload; thiết kế spike phân biệt option và cập nhật ADR khi SLO đổi.",
        "transfer": "Option rẻ nhất vi phạm RPO nhưng có tổng điểm cao nhất. Giải thích vì sao scoring sai và sửa decision rule.",
        "exit_q": "Tại sao phương án bị loại vẫn là tài sản?",
        "exit_a": "Nó lưu constraint/evidence đã xét, tránh lặp tranh luận và cho biết khi nào option có thể hợp lệ trở lại.",
        "next": "DE-L004 — hiểu Git object graph để reasoning về thay đổi và phục hồi.",
        "sections": ["1. ADR lưu reasoning, không chỉ lưu kết luận", "2. Khóa tiêu chí trước khi so phương án", "3. Phương án bị loại là tài sản", "4. Consequence gồm cả khoản nợ được chấp nhận", "6. Revisit signal phải kiểm được"],
        "homework_input": "Chọn format lưu 500 GB/ngày, retention 90 ngày, 4 consumer gồm Spark, DuckDB, Python và spreadsheet; schema đổi hàng tuần.",
        "homework_artifact": "ADR ≤2 trang, option matrix, spike plan với expected discriminating outcomes, consequence owners và supersede/revisit procedure.",
        "facts": [
            ("ADR lưu gì quan trọng nhất?", "Context và reasoning đủ để tái tạo quyết định khi constraint thay đổi."),
            ("Hard constraint khác weighted criterion thế nào?", "Vi phạm hard constraint loại option; không được bù bằng điểm ở tiêu chí khác."),
            ("Một option tốt cần mô tả gì?", "Lợi ích, cost, failure mode và evidence có thể đảo đánh giá."),
            ("Revisit signal tốt có tính chất gì?", "Đo được, có owner và gắn với assumption/constraint cụ thể."),
            ("Spike có giá trị khi nào?", "Khi kết quả có thể phân biệt option và làm recommendation thay đổi."),
            ("Supersede ADR nghĩa là gì?", "Tạo quyết định mới thay thế nhưng giữ lịch sử và liên kết bản cũ."),
        ],
    },
    {
        "role": "DE", "number": 4, "slug": "git-as-a-content-addressed-object-database",
        "title": "Git as a content-addressed object database",
        "question": "Object graph, index và refs giải thích Git như thế nào?",
        "objective": "Dựng object graph và dự đoán thay đổi ở working tree, index, repository, HEAD và branch ref sau thao tác Git.",
        "prerequisites": ["DE-L003: reasoning bằng invariant và evidence; command-line cơ bản."],
        "hook": "Bạn git add file, sửa tiếp rồi git commit. Vì sao commit không chứa bản đang nhìn thấy trong editor?",
        "core": "Git lưu immutable content-addressed objects; working tree, index và repository là ba trạng thái khác nhau, còn refs đặt tên lên commit graph.",
        "mechanism": [
            "Blob giữ content; tree giữ name/mode → object; commit giữ tree, parents và metadata.",
            "git add chụp content vào index; diff phải luôn nêu hai trạng thái đang so.",
            "Branch là ref di chuyển; HEAD thường trỏ symbolic tới branch; reachability/reflog giải thích phục hồi.",
        ],
        "first_action": "Vẽ working tree-index-HEAD và object graph trước khi chạy lệnh thay đổi trạng thái.",
        "evidence": "Dự đoán rồi đối chiếu bằng git status, diff, diff --cached, ls-files --stage, cat-file và log --graph.",
        "boundary": "Content-addressing hỗ trợ integrity và dedup; nó không tự xác minh tác giả hay ý nghĩa nghiệp vụ của thay đổi.",
        "worked": [
            "Tạo file, hash-object để thấy blob identity, add và đọc index entry.",
            "Commit để tạo tree/commit; cat-file -p lần theo parent và tree.",
            "Sửa file sau add để quan sát index khác working tree.",
            "Xóa branch rồi dùng reflog tìm commit còn reachable và tạo rescue ref.",
        ],
        "decision_rule": "Trước reset/restore, gọi tên ref và ba trạng thái sẽ đổi; dùng mode nhỏ nhất đạt mục tiêu và bảo toàn evidence cần giữ.",
        "critical_failure": "Học thuộc lệnh reset mà không dự đoán ba cây, hoặc tin xóa branch đồng nghĩa object biến mất ngay.",
        "change": "Đổi commit message hoặc parent tạo commit ID mới dù tree giống, vì commit object content đã đổi.",
        "guided_task": "Trong repo sandbox, học viên dự đoán sáu trạng thái rồi chạy command để kiểm bằng object plumbing.",
        "guided_success": "Đúng ≥5/6 dự đoán, vẽ được blob-tree-commit graph và giải thích staged/unstaged bằng cặp trạng thái.",
        "independent": "Tạo repo ba commit, partial staging, detached HEAD và deleted branch; thu evidence và phục hồi không mất work.",
        "transfer": "Một commit 'mất' sau reset nhưng còn trong reflog. Giải thích reachability, retention và cách tạo ref cứu hộ trước thao tác khác.",
        "exit_q": "git diff và git diff --cached so những trạng thái nào?",
        "exit_a": "git diff: working tree với index; git diff --cached: index với HEAD.",
        "next": "DE-L005 — merge, rebase, revert và commit identity.",
        "sections": ["1. Git lưu snapshot qua object graph", "2. Content-addressed identity", "3. Working tree, index và repository", "4. References làm graph có tên", "5. Reset được suy từ ba cây"],
        "homework_input": "Repo sandbox có main, feature, ba file và script kiểm invariant. Học viên phải tạo partial stage, detached commit, reset mixed và xóa feature ref.",
        "homework_artifact": "Prediction log trước mỗi command, object graph có OID thực, evidence transcript và runbook phục hồi commit bằng reflog.",
        "facts": [
            ("Blob lưu gì?", "Nội dung file; tên và mode nằm trong tree."),
            ("Commit trỏ trực tiếp tới gì?", "Top-level tree, parent(s) và metadata nằm trong commit object."),
            ("git add thực sự làm gì?", "Ghi content hiện tại của path vào index cho snapshot kế tiếp."),
            ("Branch là gì?", "Một ref có thể di chuyển trỏ tới commit."),
            ("Detached HEAD nghĩa là gì?", "HEAD trỏ trực tiếp commit thay vì symbolic ref tới branch."),
            ("Vì sao cùng tree vẫn có commit ID khác?", "Parent, author/time hoặc message khác làm content commit object khác."),
        ],
    },
    {
        "role": "DE", "number": 5, "slug": "branching-merge-rebase-and-commit-identity",
        "title": "Branching, merge, rebase and commit identity",
        "question": "Chọn merge, rebase, squash, revert hay reset dựa trên graph và blast radius thế nào?",
        "objective": "Dự đoán graph/identity sau integration và chọn thao tác dựa trên history consumers, shared scope và recovery.",
        "prerequisites": ["DE-L004: object graph, refs, HEAD, index và reachability."],
        "hook": "Rebase một branch đã chia sẻ làm nội dung nhìn giống nhưng commit identity đổi; clone cũ và remote giờ kể hai lịch sử khác nhau.",
        "core": "Integration là biến đổi commit graph. Merge giữ topology, rebase replay tạo identity mới, squash nén boundary; revert tiến lịch sử còn reset di chuyển ref.",
        "mechanism": [
            "Tìm merge base và reachability để dự đoán fast-forward hay three-way merge.",
            "Rebase replay commits lên parent mới nên tạo OID mới và có blast radius với consumer đã dùng OID cũ.",
            "Chọn history shape theo audit, bisect, revert và collaboration; kiểm conflict bằng invariant/test.",
        ],
        "first_action": "Vẽ tips, parents, merge base và những người/automation đang dùng các commit trước khi chọn thao tác.",
        "evidence": "Graph trước/sau, OID mapping, clone mô phỏng consumer, invariant tests và recovery command được chạy trong sandbox.",
        "boundary": "Lịch sử thẳng không đồng nghĩa lịch sử đúng; topology bị xóa có thể làm mất thông tin vận hành.",
        "worked": [
            "Nhánh riêng chưa chia sẻ: rebase lên main để cập nhật base và giữ commits logic sạch.",
            "Nhánh shared: merge để không đổi identity mà consumer đã dùng.",
            "Bad commit đã phát hành: revert tạo inverse commit, giữ audit và tương thích clone.",
            "Conflict: đọc base/ours/theirs, dựng output theo invariant rồi chạy test; không chọn nguyên một phía theo thói quen.",
        ],
        "decision_rule": "Không rewrite identity đã chia sẻ nếu chưa có coordinated migration; dùng revert cho lịch sử công khai, reset cho ref cục bộ/recovery có containment.",
        "critical_failure": "Force-push chỉ để có graph đẹp, hoặc coi hết conflict marker là bằng chứng behavior đúng.",
        "change": "Nếu commit boundaries là deployment checkpoints, squash làm mất khả năng bisect/revert theo bước và có thể không chấp nhận được.",
        "guided_task": "Bốn scenario card: branch riêng, shared branch, bad release, noisy fixups. Chọn operation, vẽ graph và nêu affected users.",
        "guided_success": "Đúng ≥3/4 lựa chọn; mỗi lựa chọn có merge base/OID reasoning, blast radius và recovery.",
        "independent": "Dựng hai clone và remote local, tạo divergence, merge, rebase và revert; chứng minh identity/blast radius bằng log graph.",
        "transfer": "Pipeline pin commit SHA cũ trong khi team muốn rebase branch. Thiết kế migration hoặc chọn operation không phá consumer.",
        "exit_q": "Revert khác reset ở outcome lịch sử và phạm vi ảnh hưởng thế nào?",
        "exit_a": "Revert thêm commit đảo thay đổi và an toàn hơn cho lịch sử shared; reset di chuyển ref và có thể làm commit biến khỏi history hiện tại.",
        "next": "DE-L006 — phục hồi lost work bằng reflog, detached HEAD và bisect.",
        "sections": ["1. Branch là con trỏ, divergence nằm ở graph", "2. Three-way merge và conflict", "3. Rebase phát lại thay đổi lên base mới", "4. Merge, squash và thông tin bị giữ hoặc mất", "5. Revert và reset giải hai bài toán khác"],
        "homework_input": "Hai clone A/B dùng remote local; feature có ba commit, main có hotfix, CI pin OID thứ hai của feature và một bad commit đã merge vào main.",
        "homework_artifact": "Graph dự đoán/thực tế cho merge và rebase, OID map, blast-radius report từ clone B, revert evidence và decision memo.",
        "facts": [
            ("Fast-forward xảy ra khi nào?", "Tip hiện tại là ancestor của tip được hợp nhất nên ref chỉ cần di chuyển."),
            ("Three-way merge dùng ba trạng thái nào?", "Hai tips và merge base chung."),
            ("Vì sao rebase đổi commit identity?", "Commit được tạo lại trên parent mới nên object content và OID đổi."),
            ("Squash mất thông tin gì?", "Các commit boundary và topology trung gian trên history đích."),
            ("Conflict resolution hoàn thành khi nào?", "Kết quả thỏa invariant và test, không chỉ khi marker biến mất."),
            ("Khi nào ưu tiên revert?", "Khi bad change đã nằm trong lịch sử shared/công khai cần giữ audit và identity hiện có."),
        ],
    },
]


DISTRACTORS = [
    "Mở công cụ và tối ưu output ngay vì implementation sẽ làm rõ yêu cầu.",
    "Chọn một mặc định hợp lý nhưng không ghi lại để tiết kiệm thời gian.",
    "Dùng chính output đang kiểm làm oracle vì hai kết quả sẽ dễ khớp.",
    "Bỏ qua boundary và failure path nếu happy path đã chạy một lần.",
    "Thêm nhiều biểu đồ hoặc metric hơn thay cho việc khóa semantics.",
    "Coi tên bảng, folder hoặc service là bằng chứng về trách nhiệm và grain.",
]

SECOND_BRAIN_REFS = {
    "DA-L001": [
        ("wiki.da.operating-as-a-data-analyst", "Operating as a Data Analyst"),
        ("wiki.data-product.decision-first-discovery", "Decision-First Discovery"),
        ("wiki.da.revenue-and-commerce-analytics", "Revenue and commerce analytics"),
    ],
    "DA-L002": [
        ("wiki.da-foundation.data-lifecycle-seven-stages", "Data lifecycle and its seven stages"),
        ("wiki.data-product.decision-first-discovery", "Decision-First Discovery"),
        ("wiki.da.reconciliation-and-the-discipline-of-verification", "Reconciliation and the discipline of verification"),
    ],
    "DA-L003": [
        ("wiki.da-foundation.entity-attribute-record-and-grain", "Entities, attributes, records and grain"),
        ("wiki.data-modeling.fact-table-types", "Fact table types"),
        ("wiki.database.joins-duplicate-multiplication-null", "Join multiplication and NULL behavior"),
    ],
    "DA-L004": [
        ("wiki.da-foundation.three-question-tiers-and-metric-tree", "Three question tiers and the metric tree"),
        ("wiki.data-product.metric-tree", "Question decomposition and the metric tree"),
        ("wiki.data-product.decision-first-discovery", "Decision-First Discovery"),
    ],
    "DA-L005": [
        ("wiki.da-foundation.vague-request-to-answerable-question", "From a vague request to an answerable question"),
        ("wiki.semantic-layer.metric-contract", "From a business question to a metric contract"),
        ("wiki.data-product.requirements-traceability", "Requirements traceability"),
    ],
    "DE-L001": [
        ("wiki.engineering-foundation.testable-contract", "From a vague request to a testable contract"),
        ("wiki.data-product.requirements-traceability", "Requirements traceability"),
        ("wiki.data-quality.sli-slo-design", "Data SLI and SLO design"),
    ],
    "DE-L002": [
        ("wiki.engineering-foundation.decomposition-four-axes", "Decomposition across four axes"),
        ("wiki.data-product.requirements-traceability", "Requirements traceability"),
        ("wiki.backend.idempotency-keys-deduplication-state", "Idempotency keys and deduplication state"),
    ],
    "DE-L003": [
        ("wiki.engineering-foundation.adr-trade-offs", "Trade-offs and architecture decision records"),
        ("wiki.data-product.decision-first-discovery", "Decision-First Discovery"),
        ("wiki.data-product.requirements-traceability", "Requirements traceability"),
    ],
    "DE-L004": [
        ("wiki.engineering-foundation.git-object-database", "Git as a content-addressed object database"),
        ("wiki.engineering-foundation.adr-trade-offs", "Trade-offs and architecture decision records"),
        ("wiki.data-product.requirements-traceability", "Requirements traceability"),
    ],
    "DE-L005": [
        ("wiki.engineering-foundation.git-history-integration", "Branching, merge, rebase and commit identity"),
        ("wiki.engineering-foundation.git-object-database", "Git as a content-addressed object database"),
        ("wiki.engineering-foundation.adr-trade-offs", "Trade-offs and architecture decision records"),
    ],
}


def lesson_dir(item: dict) -> Path:
    base = DA_ROOT if item["role"] == "DA" else DE_ROOT
    return base / f"Lesson_{item['number']:03d}-{item['slug']}"


def note_locator(item: dict, heading: str) -> str:
    normalized = {
        "Nỗi Đau & Động Lực": "Problem Definition and Operational Relevance",
        "Cơ Chế Tác Động": "Mechanism",
        "Bản Đồ Quyết Định": "Decision Framework",
        "Case Study Thực Chiến: một chỉ số bán hàng đổi nghĩa giữa đường": "Worked Case: một chỉ số bán hàng đổi nghĩa giữa đường",
        "Góc Khuất & Ngộ Nhận": "Limits and Common Errors",
    }.get(heading, heading.strip("'"))
    return f"note.md: heading {normalized}"


def references_md(item: dict) -> str:
    lesson_id = f"{item['role']}-L{item['number']:03d}"
    links = "\n".join(f"- [[{note_id}|{label}]]" for note_id, label in SECOND_BRAIN_REFS[lesson_id])
    return f"## References\n\n{links}\n"


def public_copy(text: str) -> str:
    return prose_transform(text, lambda value: remove_course_timing(editorial_prose(value)))


def scenes(item: dict) -> list[dict]:
    sec = item["sections"]
    return [
        {"id": "S01", "type": "explain", "claim": item["hook"], "source_span": note_locator(item, sec[0]), "misconception_displaced": "Có thể bắt đầu bằng công cụ/output trước khi khóa câu hỏi và boundary."},
        {"id": "S02", "type": "explain", "claim": item["core"], "source_span": note_locator(item, sec[1]), "misconception_displaced": item["critical_failure"]},
        {"id": "S03", "type": "check", "question": item["facts"][0][0], "answer": item["facts"][0][1], "wrong_answer_reveals": "Người học nhớ từ khóa nhưng chưa nắm claim trung tâm.", "source_span": note_locator(item, sec[1])},
        {"id": "S04", "type": "practice", "task": item["guided_task"], "success_condition": item["guided_success"], "source_span": "UNSOURCED: guided practice synthesized from the lesson objective and source-backed mechanism"},
        {"id": "S05", "type": "explain", "claim": item["decision_rule"], "source_span": note_locator(item, sec[2]), "misconception_displaced": "Một rule hoặc tool luôn đúng bất kể changed constraint."},
        {"id": "S06", "type": "decide", "situation": item["change"], "trade_off": item["boundary"], "defensible_choices": "Lựa chọn phải giữ hard constraints, nêu evidence và reversal trigger.", "source_span": "UNSOURCED: changed-constraint decision scenario synthesized for transfer"},
        {"id": "S07", "type": "explain", "claim": "Worked example: " + " ".join(item["worked"]), "source_span": note_locator(item, sec[3]), "misconception_displaced": "Một case thành công tự chứng minh cơ chế tổng quát."},
        {"id": "S08", "type": "apply", "task": item["transfer"], "assumes": ["S02", "S04", "S05", "S06", "S07"], "success_condition": "Artifact nêu boundary, evidence, lựa chọn, rejected alternative và condition làm quyết định đảo.", "source_span": "UNSOURCED: curriculum transfer scenario synthesized from the lesson contract"},
        {"id": "S09", "type": "check", "question": item["exit_q"], "answer": item["exit_a"], "wrong_answer_reveals": "Người học chưa chuyển mental model sang tình huống mới.", "source_span": note_locator(item, sec[4])},
    ]


def build_yaml(item: dict) -> str:
    payload = {
        "schema_version": 2,
        "lesson_id": f"{item['role']}-L{item['number']:03d}",
        "title": item["title"],
        "status": "ready-for-owner-review",
        "lifecycle_profile": "learning",
        "risk_tier": "R2-standard",
        "target_level": "Foundation",
        "central_question": item["question"],
        "objective": item["objective"],
        "prerequisites": item["prerequisites"],
        "learner_memory": {"resolved": False, "assumption": "No prior mastery claimed; teach and assess the named prerequisites."},
        "editorial": {
            "standard": "lesson-authoring-v1",
            "humanizer": "blader/humanizer@3.1.0",
            "status": "pass",
        },
        "scenes": scenes(item),
        "assessment": {
            "formative": "quiz.md — 10 questions, pass >= 8/10; failed concepts receive targeted remediation and one retest.",
            "authentic": "homework.md — artifact scored on a 100-point analytic rubric; pass >= 75 and no critical failure.",
            "mastery_claim": "None. Package readiness and learner mastery are separate evidence states.",
        },
        "publish": {"note": True, "slides": True, "quiz": True, "homework": True, "after_note": True, "answer_key": True},
        "unused_source_spans": ["Ma trận kiểm chứng chi tiết and Source coverage remain in note.md for extension and remediation."],
    }
    return yaml.safe_dump(payload, allow_unicode=True, sort_keys=False, width=110)


def slides_md(item: dict) -> str:
    lesson_id = f"{item['role']}-L{item['number']:03d}"
    mechs = "\n".join(f"- {value}" for value in item["mechanism"])
    worked = "\n".join(f"{i}. {value}" for i, value in enumerate(item["worked"], 1))
    content = f'''---
marp: true
theme: volt
paginate: true
size: 16:9
header: '{item["role"]} · Lesson {item["number"]}'
footer: 'Foundation · runnable scene package'
---

<!-- _class: lead -->

# {item['title']}

**{lesson_id}**

> {item['question']}

---

## Chuẩn đầu ra

{item['objective']}

**Evidence:** {item['evidence']}

**Không suy ra mastery từ việc có mặt hoặc xem hết slide.**

---

<!-- scene: S01 · source: {note_locator(item, item['sections'][0])} -->
## Tình huống mở

{item['hook']}

**Independent analysis followed by peer review**

1. Bạn sẽ làm gì đầu tiên?
2. Quyết định nào có thể bị ảnh hưởng?
3. Bằng chứng nào đang thiếu?

---

<!-- scene: S02 · source: {note_locator(item, item['sections'][1])} -->
## Mental model trung tâm

> {item['core']}

{mechs}

---

## Luồng kiểm soát

| 1. Câu hỏi hoặc thay đổi | 2. Boundary | 3. Evidence | 4. Decision gate | 5. Theo dõi |
|---|---|---|---|---|
| Nêu outcome cần quyết định | Khóa scope và semantics | Dùng phép kiểm độc lập | Áp dụng có giới hạn hoặc dừng | Quan sát reversal trigger |

---

## Bước đầu tiên có tính quyết định

**{item['first_action']}**

Không làm bước này, output sau đó có thể đúng cú pháp nhưng sai đối tượng, sai thời gian hoặc sai quyết định.

---

<!-- scene: S03 · source: {note_locator(item, item['sections'][1])} -->
## Check 1 · trả lời không nhìn tài liệu

**{item['facts'][0][0]}**

<details>
<summary>Đáp án và tín hiệu chẩn đoán</summary>

{item['facts'][0][1]}

Nếu câu trả lời chỉ nêu tên công cụ, hãy quay lại mental model và nói rõ boundary + evidence + action.
</details>

---

<!-- scene: S04 · source: UNSOURCED guided practice synthesis -->
## Guided practice

{item['guided_task']}

**Definition of done:** {item['guided_success']}

Người dạy không chữa bằng đáp án ngay; yêu cầu mỗi nhóm nêu assumption và phép kiểm trước.

---

<!-- scene: S05 · source: {note_locator(item, item['sections'][2])} -->
## Quy tắc quyết định

{item['decision_rule']}

**Boundary:** {item['boundary']}

---

## Changed constraint

<!-- scene: S06 · source: UNSOURCED changed-constraint synthesis -->

{item['change']}

**Thảo luận:** lựa chọn nào còn defensible? Bằng chứng nào làm bạn đảo quyết định?

---

## Worked example · đi từng bước

<!-- scene: S07 · source: {note_locator(item, item['sections'][3])} -->

{worked}

---

## Evidence phải giữ lại

{item['evidence']}

Một output không có boundary, oracle hoặc limitation chỉ là kết quả chưa review.

---

## Failure modes

- **Critical:** {item['critical_failure']}
- Chỉ kiểm happy path và sửa expected sau khi nhìn output.
- Gộp author claim, curriculum synthesis và learner conclusion thành một giọng.
- Dùng số lượng biểu đồ/test để thay thế oracle độc lập.

---

## Independent practice · không có đáp án mẫu

{item['independent']}

**Nộp:** artifact + evidence + limitation + reversal trigger.

---

<!-- scene: S08 · source: UNSOURCED curriculum transfer scenario -->
## Transfer challenge

{item['transfer']}

Được phép có nhiều lựa chọn. Điểm nằm ở boundary, trade-off, evidence và blast radius — không nằm ở việc đoán ý người dạy.

---

<!-- scene: S09 · source: {note_locator(item, item['sections'][4])} -->
## Exit check

**{item['exit_q']}**

<details><summary>Đáp án tối thiểu</summary>

{item['exit_a']}
</details>

---

## Post-Lesson

1. Làm `quiz.md`; đạt **8/10**.
2. Nếu trượt một concept, đọc remediation trong `after-note.md` rồi retest đúng concept đó.
3. Hoàn thành `homework.md`; đạt **≥ 75/100** và không có critical failure.

**Bắc cầu:** {item['next']}

---

{references_md(item)}
'''
    return public_copy(content.replace(" — ", ": ").replace(";", ".").replace(" → ", " sang "))


def quiz_questions(item: dict) -> list[tuple[str, str, list[str]]]:
    qs = [(q, a, []) for q, a in item["facts"]]
    qs += [
        ("Trong tình huống mở bài, hành động đầu tiên tốt nhất là gì?", item["first_action"], []),
        ("Bằng chứng nào trực tiếp nhất để xác nhận năng lực của bài này?", item["evidence"], []),
        ("Khi constraint thay đổi, nguyên tắc xử lý đúng là gì?", item["change"], []),
        ("Phát biểu nào mô tả critical failure của bài?", item["critical_failure"], []),
    ]
    return qs


def quiz_md(item: dict) -> str:
    blocks = []
    questions = quiz_questions(item)
    answer_pool = [answer for _, answer, _ in questions]
    for index, (question, correct, _) in enumerate(questions, 1):
        wrongs = []
        cursor = index
        while len(wrongs) < 3:
            candidate = answer_pool[cursor % len(answer_pool)]
            cursor += 2
            if candidate != correct and candidate not in wrongs:
                wrongs.append(candidate)
        choices = [correct, *wrongs]
        rotate = index % 4
        choices = choices[rotate:] + choices[:rotate]
        answer_index = choices.index(correct)
        labels = "ABCD"
        rendered = "\n".join(f"- [ ] {labels[i]}. {choice}" for i, choice in enumerate(choices))
        blocks.append(f'''### Câu {index}

{question}

{rendered}

<details><summary>Đáp án và phản hồi</summary>

**{labels[answer_index]}. {correct}**

Đây là phát biểu trả lời đúng **boundary của câu hỏi**. Ba lựa chọn còn lại có thể là mệnh đề hợp lệ ở phần khác của bài nhưng không trả lời điều đang được hỏi — lỗi thường gặp khi nhớ nhiều thuật ngữ mà không phân biệt vai trò của chúng. Nếu chọn sai, đọc lại scene S02/S05 rồi làm novel-scenario retest trong `after-note.md`.
</details>''')
    return public_copy(f'''---
loai: formative-quiz
lesson: {item['number']}
lesson_id: {item['role']}-L{item['number']:03d}
tieu_de: "{item['title']}"
so_cau: 10
trang_thai: ready-for-owner-review
nguong_dat: 8
---

# Quiz — {item['role']} Lesson {item['number']}: {item['title']}

**Mục đích:** kiểm mental model và khả năng áp dụng, không dùng điểm danh làm bằng chứng.
**Đạt:** ≥ 8/10. Câu 7-10 là critical transfer set; sai câu nào phải remediation và retest câu tương đương.

{'\n\n---\n\n'.join(blocks)}

{references_md(item)}
''')


def homework_md(item: dict) -> str:
    return public_copy(f'''---
loai: authentic-homework
lesson: {item['number']}
lesson_id: {item['role']}-L{item['number']:03d}
tieu_de: "{item['title']}"
trang_thai: ready-for-owner-review
nguong_dat: 75
---

# Homework — {item['role']} Lesson {item['number']}: {item['title']}

**Làm cá nhân. Nộp một thư mục chứa artifact, evidence và reflection.**

## Bối cảnh và input cố định

{item['homework_input']}

Không tự bổ sung dữ kiện làm đổi semantics. Nếu cần assumption, ghi vào assumption ledger và nêu impact-if-wrong.

## Phần A — Build artifact (50 điểm)

{item['homework_artifact']}

Artifact phải đủ để một reviewer không dự buổi học tái hiện decision path. Mọi con số/command phải kèm source hoặc raw evidence.

## Phần B — Adversarial review (30 điểm)

1. Nêu hai failure mode có thể làm artifact trông đúng nhưng conclusion sai.
2. Tạo một counterexample hoặc fault injection cho mỗi failure mode.
3. Ghi expected observation **trước** khi chạy/đối chiếu.
4. Nêu oracle độc lập và kết quả sẽ khiến bạn bác bỏ recommendation.

## Phần C — Changed constraint và handoff (20 điểm)

Constraint đổi như sau: {item['change']}

Viết memo 250–400 từ: phần nào của artifact còn đúng, phần nào phải thay, affected consumer, rollback/recovery và owner tiếp theo.

## Rubric chấm điểm

| Tiêu chí | Điểm | Full-credit evidence |
|---|---:|---|
| Semantics và boundary | 20 | Population/identity/time/state hoặc responsibility được nêu đủ; không có mặc định ẩn |
| Cơ chế và correctness | 20 | Lập luận theo đúng mental model; phép tính/graph/contract tái hiện được |
| Evidence và oracle | 20 | Raw evidence, expected result, independent check và discrepancy được giữ |
| Failure/edge paths | 15 | Hai counterexample thật; không chỉ lặp happy path |
| Decision và trade-off | 15 | Chosen/rejected option, limitation và reversal trigger rõ |
| Handoff và khả năng đọc | 10 | Cấu trúc gọn, owner/next action rõ, reviewer không phải đoán |

**Ngưỡng đạt:** ≥ 75/100 và không có critical failure.

## Critical-failure rules

- {item['critical_failure']}
- Expected result được sửa sau khi nhìn output mà không ghi discrepancy.
- Không có evidence gốc hoặc dùng implementation đang kiểm làm oracle duy nhất.
- Khẳng định production/mastery vượt quá evidence của bài.

## Remediation và retest

Nếu trượt, reviewer chỉ rõ rubric row và failed invariant. Người học nộp lại phần sai cùng một changed scenario; không cần làm lại phần đã có bằng chứng đạt. Retest phải dùng fixture/scenario khác để tránh học thuộc đáp án.

{references_md(item)}
''')


def after_note_md(item: dict) -> str:
    facts = "\n".join(f"- **{q}** — {a}" for q, a in item["facts"][:4])
    return public_copy(f'''# {item['role']} Lesson {item['number']} — Practice, feedback and retest

## Thực hành có hướng dẫn

{item['guided_task']}

**Dấu hiệu đạt:** {item['guided_success']}

### Feedback protocol

1. Người học đọc boundary và expected result trước khi trình bày output.
2. Reviewer hỏi oracle nào độc lập và changed condition nào làm quyết định đảo.
3. Chỉ phản hồi vào observable artifact; không suy động cơ hoặc mastery từ độ tự tin.
4. Gắn lỗi vào một scene ID trong `lesson.yaml` để remediation có mục tiêu.

## Retrieval checks và đáp án tối thiểu

{facts}

## Novel-scenario retest

{item['transfer']}

**Pass condition:** câu trả lời nêu boundary, evidence, lựa chọn, ít nhất một alternative, blast radius/consumer harm và reversal trigger. Không chấm theo việc trùng wording của đáp án mẫu.

## Post-Lesson Work

- Làm `quiz.md`, ngưỡng 8/10.
- Làm `homework.md`, ngưỡng 75/100 và không có critical failure.
- Giữ artifact gốc, feedback, bản sửa và retest như bốn evidence riêng; không ghi đè failed attempt.

## Remediation map

| Lỗi quan sát được | Quay lại | Bài retest |
|---|---|---|
| Không gọi tên được claim trung tâm | S02 | Giải thích bằng ví dụ khác, không dùng thuật ngữ trong tiêu đề |
| Chọn action trước boundary/evidence | S01, S05 | Viết ba câu hỏi phải đóng trước mutation |
| Chỉ chạy happy path | S06, S07 | Thêm counterexample và expected failure observation |
| Không chuyển được sang scenario mới | S08 | Giải changed constraint và nêu điều kiện đảo quyết định |

## Giới hạn

Gói này chưa được dạy trên cohort thật. Điểm quiz và homework chỉ là evidence trong scope của {item['role']}-L{item['number']:03d}, không phải chứng nhận vai trò hoặc kinh nghiệm production.

## Bắc cầu

{item['next']}

{references_md(item)}
''')


def digest(paths: list[Path]) -> str:
    value = hashlib.sha256()
    for path in sorted(paths):
        value.update(path.relative_to(ROOT).as_posix().encode())
        value.update(b"\0")
        value.update(path.read_bytes())
        value.update(b"\0")
    return value.hexdigest()


def main(check: bool = False) -> int:
    stale = []
    outputs: list[Path] = []
    for item in LESSONS:
        directory = lesson_dir(item)
        note = directory / "note.md"
        if not note.exists():
            raise FileNotFoundError(note)
        if item.get("authoring_mode") == "handcrafted":
            handcrafted = [directory / name for name in ("lesson.yaml", "slides.md", "quiz.md", "homework.md", "after-note.md")]
            missing = [str(path.relative_to(ROOT)) for path in handcrafted if not path.exists()]
            if missing:
                print("MISSING HANDCRAFTED ASSETS")
                print("\n".join(missing))
                return 1
            outputs.extend(handcrafted)
            continue
        assets = {
            "lesson.yaml": build_yaml(item),
            "slides.md": slides_md(item),
            "quiz.md": quiz_md(item),
            "homework.md": homework_md(item),
            "after-note.md": after_note_md(item),
        }
        for name, content in assets.items():
            target = directory / name
            outputs.append(target)
            expected = content.rstrip() + "\n"
            if check:
                if not target.exists() or target.read_text() != expected:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.write_text(expected)
    if stale:
        print("STALE")
        print("\n".join(stale))
        return 1
    if check:
        print(f"checked lessons={len(LESSONS)} assets={len(outputs)} fingerprint={digest(outputs)}")
    else:
        print(f"built lessons={len(LESSONS)} assets={len(outputs)} fingerprint={digest(outputs)}")
    return 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.check))
