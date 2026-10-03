#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

from format_knowledge_notes import normalize_markdown

ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT / "Material/DE/Curriculum/Phase_01-engineering-foundation/Module_01-engineering-thinking-git-and-debugging"
PACK = ROOT / "Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01"
WIKI = ROOT / "Docs/Second-Brain/2_Wiki/Software-Engineering"
MANIFEST = ROOT / "Docs/Second-Brain/second-brain-manifest.json"

SOM = "src.book.sommerville-software-engineering.10e"
PP = "src.book.hunt-thomas-pragmatic-programmer.20ae"
MADR = "src.web.madr-templates"
PROGIT = "src.book.chacon-straub-pro-git.2e"

SOURCE_LABELS = {
    SOM: "SRC-SOMMERVILLE-SOFTWARE-ENGINEERING-10E",
    PP: "SRC-HUNT-THOMAS-PRAGMATIC-PROGRAMMER-20AE",
    MADR: "SRC-MADR-TEMPLATES",
    PROGIT: "SRC-CHACON-STRAUB-PRO-GIT-2E",
}


@dataclass(frozen=True)
class Lesson:
    number: int
    directory: str
    title: str
    slug: str
    note_id: str
    question: str
    sources: tuple[str, ...]
    sections: tuple[tuple[str, str, str], ...]
    case: str
    failure_modes: tuple[str, ...]
    probes: tuple[str, ...]
    takeaway: str

    @property
    def filename(self) -> str:
        return f"{self.number:03d}-{self.slug}.md"

    @property
    def folder(self) -> Path:
        return MODULE / self.directory


LESSONS = (
    Lesson(
        1,
        "Lesson_001-from-a-vague-request-to-a-testable-contract",
        "From a vague request to a testable contract",
        "vague-request-to-testable-contract",
        "wiki.engineering-foundation.testable-contract",
        "Làm sao biến một yêu cầu mơ hồ thành contract đủ rõ để hai người độc lập tạo cùng một phép kiểm chấp nhận?",
        (SOM,),
        (
            ("Bắt đầu từ quyết định, không bắt đầu từ giải pháp", "Câu ‘làm dashboard doanh thu’ chưa nói ai sẽ dùng kết quả để quyết định điều gì. Trước khi chọn dữ liệu hay công cụ, người viết contract phải xác định actor, trigger và quyết định cần hỗ trợ. Nếu bỏ ba điểm này, đội kỹ thuật có thể giao đúng màn hình nhưng sai công việc.", "Một contract tốt không cố đoán mọi chi tiết ngay từ đầu. Nó khóa phần có thể quan sát: ai kích hoạt, input nào được chấp nhận, output nào xuất hiện, ràng buộc nào bắt buộc và điều gì nằm ngoài phạm vi. Phần chưa biết được ghi thành câu hỏi có owner, không được ngụy trang thành mặc định."),
            ("Sáu phần của một phát biểu kiểm thử được", "Sáu phần gồm user, trigger, input, output, constraints và non-goals. User là vai trò chịu hậu quả, không nhất thiết là người bấm nút. Trigger là sự kiện hoặc lịch chạy. Input phải có boundary và nguồn thẩm quyền. Output mô tả hành vi nhìn thấy được, không chỉ tên artifact.", "Constraints cần tách correctness, performance và operability. ‘Đúng số tiền theo sổ cái’, ‘trả trong 10 giây’ và ‘replay không tạo bản ghi kép’ dẫn tới ba loại bằng chứng khác nhau. Non-goal chặn việc phạm vi nở âm thầm; nó phải viết thành câu có thể phản biện, không nằm trong trí nhớ của người họp."),
            ("Từ requirement tới acceptance check", "Acceptance check gồm trạng thái đầu, hành động, dữ liệu cụ thể và kết quả mong đợi. ‘Chạy không lỗi’ chỉ chứng minh process trả exit code thuận lợi; nó không chứng minh đúng population, đúng số tiền hay đúng thời điểm. Một check tốt sẽ thất bại khi một mệnh đề nghiệp vụ bị vi phạm.", "Mỗi requirement cần cả positive case và boundary hoặc negative case. Nếu yêu cầu nói hỗ trợ đơn hàng hợp lệ, hãy đưa thêm đơn thiếu currency hoặc trùng identity. Hai người đọc contract phải có thể dựng cùng oracle mà không hỏi tác giả kết quả đúng là gì."),
            ("Assumption ledger và câu hỏi chưa đóng", "Mọi contract đều dựa trên assumption: timezone nào, duplicate được nhận diện ra sao, dữ liệu sửa muộn đến khi nào, ai có quyền phê duyệt. Ghi assumption cùng impact-if-wrong giúp đội biết điểm nào cần xác minh trước khi code và điểm nào có thể chấp nhận tạm thời.", "Một unknown có thể không chặn thiết kế nếu đã có giới hạn an toàn. Ngược lại, identity key chưa rõ thường chặn deduplication vì mọi test phía sau đều có thể xanh giả. Quy tắc dừng là: nếu unknown làm thay đổi semantics, blast radius hoặc tiêu chí đạt, phải giải quyết trước mutation."),
            ("Traceability hai chiều", "Requirement nối tới acceptance check; check nối tới fixture và kết quả; thay đổi code nối ngược về requirement. Chuỗi này cho phép trả lời vì sao một test tồn tại và requirement nào chưa có phép kiểm. Traceability không phải bảng quản trị trang trí mà là công cụ phát hiện lỗ hổng.", "Khi requirement đổi, đừng sửa test cho xanh trước rồi mới cập nhật contract. Hãy ghi thay đổi semantics, xem lại non-goal và boundary, sau đó cập nhật oracle. Nếu không, test chỉ chứng minh implementation mới khớp chính nó."),
            ("Definition of Ready và điểm dừng", "Một yêu cầu sẵn sàng khi actor, trigger, input, output, constraints, non-goals và acceptance checks đều đủ để bắt đầu một increment nhỏ. Ready không có nghĩa mọi câu hỏi tương lai đã biến mất; nó có nghĩa phần việc sắp làm có boundary và bằng chứng hoàn thành rõ.", "Nếu reviewer vẫn tạo được hai kết quả trái nhau nhưng đều hợp văn bản, contract chưa sẵn sàng. Phản biện cần tập trung vào counterexample chứ không tranh câu chữ: đưa một input sát biên, hỏi output nào đúng và ai chịu trách nhiệm khi không đủ dữ liệu."),
        ),
        "Một quản lý nhắn ‘mỗi sáng gửi doanh thu hôm qua’. Sau khi hỏi lại, đội xác định finance analyst là consumer, 07:00 Asia/Ho_Chi_Minh là trigger, ledger đã posted là nguồn, output là tổng gross/refund/net theo currency, dữ liệu chưa posted là non-goal, và gửi trễ hơn 07:10 là vi phạm vận hành. Hai acceptance checks dùng một fixture bình thường và một refund tới sát cutoff.",
        ("Dùng động từ mơ hồ như nhanh, đầy đủ hoặc realtime mà không có ngưỡng.", "Đưa tên công cụ vào requirement khiến một lựa chọn implementation biến thành nhu cầu giả.", "Viết happy path nhưng không viết duplicate, missing hoặc boundary time.", "Không ghi non-goal nên mọi ý tưởng hợp lý đều bị xem là cam kết."),
        ("Hai reviewer độc lập viết cùng expected output từ một fixture.", "Một input ở đúng cutoff và một input sau cutoff cho kết quả khác đúng policy.", "Bỏ trường identity phải làm contract bị chặn thay vì tự chọn mặc định.", "Đổi SLO từ 10 phút xuống 30 giây phải lộ thay đổi thiết kế.", "Một non-goal bị yêu cầu lại phải tạo change request, không lén mở rộng scope.", "Trace một failed check về đúng requirement và owner."),
        "Yêu cầu chỉ sẵn sàng để xây khi hành vi quan sát được, boundary và oracle đều rõ hơn tên giải pháp.",
    ),
    Lesson(
        2,
        "Lesson_002-decomposition-responsibility-interface-state-and-failure-domain",
        "Decomposition - responsibility, interface, state and failure domain",
        "decomposition-responsibility-interface-state-failure-domain",
        "wiki.engineering-foundation.decomposition-four-axes",
        "Làm sao chia một hệ thành các boundary có trách nhiệm, interface, state và failure domain nhất quán?",
        (SOM, PP),
        (
            ("Ranh giới bắt đầu từ responsibility", "Một component nên có một lý do nghiệp vụ hoặc vận hành rõ để thay đổi. Chia theo controller, service và repository có thể hữu ích cho tổ chức mã nhưng chưa nói ai sở hữu invariant. Nếu cùng quy tắc order bị kiểm ở API, worker và SQL script, responsibility đang bị phân tán.", "Cách kiểm thực dụng là đặt một change scenario: đổi policy refund hoặc đổi storage engine thì phần nào phải sửa? Nếu diff lan qua nhiều boundary không liên quan, decomposition chưa cô lập được quyết định volatile."),
            ("Interface là lời hứa tối thiểu", "Interface cần nêu operation, input/output semantics, error contract và invariants mà caller được dựa vào. Nó không nên lộ ORM entity, table layout hoặc exception của driver nếu những thứ đó không thuộc domain contract. Public surface càng rộng thì số assumption bên ngoài càng nhiều.", "Một abstraction rò rỉ khi caller vẫn phải biết chi tiết bị tuyên bố là đã che. Ví dụ repository trả SQLAlchemy Session buộc domain biết transaction mechanism. Không phải mọi leak đều tránh được, nhưng leak phải được gọi tên và kiểm soát thay vì ẩn dưới một interface đẹp."),
            ("State quyết định độ khó thay thế", "Stateless function dễ nhân bản vì kết quả chỉ phụ thuộc input. Component giữ state cần nói state nào là authoritative, lifecycle ra sao, ai được mutate và phục hồi thế nào. Cache, checkpoint và dedup ledger là ba state có semantics khác nhau; gom chúng vào một hộp ‘storage’ che mất recovery contract.", "Invariant phải sống gần owner của state. Nếu hai component cùng có quyền cập nhật một state machine mà không có protocol, failure giữa hai write tạo trạng thái trung gian. Decomposition cần làm rõ transaction boundary hoặc compensation, không chỉ vẽ mũi tên gọi hàm."),
            ("Failure domain không đồng nghĩa deployment unit", "Failure domain trả lời một phần hỏng kéo theo phần nào mất chức năng hoặc mất dữ liệu. Hai module cùng process có thể lỗi độc lập ở semantics nhưng crash cùng process. Hai service khác nhau vẫn có chung failure domain nếu đều phụ thuộc một database hoặc credential.", "Hãy trace từ fault tới consumer harm: timeout, retry, queue growth, stale output và recovery. Boundary tốt giúp khoanh blast radius hoặc ít nhất làm nó quan sát được. Tách service mà không tách dependency và state đôi khi chỉ tăng network failure mà không giảm blast radius."),
            ("Cohesion, coupling và chiều phụ thuộc", "Cohesion hỏi code bên trong có phục vụ cùng capability; coupling hỏi boundary này đặt assumption gì lên boundary kia; dependency direction hỏi policy có biết mechanism hay ngược lại. Ba khái niệm liên quan nhưng một biểu đồ import không chứng minh đủ runtime, temporal và data coupling.", "Orthogonality là phép thử thay đổi: thay một quyết định thì bao nhiêu module không liên quan bị chạm. Đây là heuristic chẩn đoán, không phải mục tiêu tuyệt đối. Một contract ổn định vẫn tạo coupling có chủ ý; vấn đề là coupling có được công bố, version và kiểm thử hay không."),
            ("Đồ thị phụ thuộc và vòng lặp", "Một vòng A→B→C→A khiến không boundary nào đứng độc lập để kiểm thử hoặc thay thế. Phá vòng bằng cách chuyển policy về owner, tách protocol hoặc đảo dependency qua port. Không nên tạo package ‘common’ chỉ để giấu vòng; shared package vẫn là một node có ownership và release contract.", "Sau khi vẽ source graph, bổ sung data owner, runtime call và failure dependency. Một cạnh phải ghi assumption cụ thể: schema, ordering, availability hay identity. Danh sách cạnh có ý nghĩa hơn số lượng hộp vì nó cho biết điều gì thực sự phải phối hợp khi thay đổi."),
        ),
        "Hệ bán hàng được chia thành order policy, payment adapter, inventory adapter và fulfillment workflow. Order policy sở hữu state transition; adapters cài port do application sở hữu; workflow điều phối nhưng không cập nhật trực tiếp bảng của adapters. Nhóm inject payment timeout và chứng minh order vẫn ở trạng thái recoverable trong khi catalog read tiếp tục phục vụ.",
        ("Chia theo công nghệ rồi gọi đó là domain boundary.", "Vẽ component nhưng không ghi state owner hoặc invariant.", "Chỉ đọc import graph rồi kết luận không có coupling.", "Tách deployment nhưng giữ shared database và shared credential nên failure domain không đổi."),
        ("Đổi database không buộc domain model import type mới.", "Kill payment adapter không làm mất order intent.", "Một state transition chỉ có một authoritative writer.", "Mỗi public field đều gắn với một consumer assumption hợp lệ.", "Đồ thị source dependency không có vòng.", "Changed-requirement exercise chạm đúng owner và test contract."),
        "Decomposition có giá trị khi cô lập decision, state và failure; số lượng component tự nó không chứng minh điều đó.",
    ),
    Lesson(
        3,
        "Lesson_003-trade-offs-and-the-architecture-decision-record",
        "Trade-offs and the architecture decision record",
        "trade-offs-and-architecture-decision-record",
        "wiki.engineering-foundation.adr-trade-offs",
        "Làm sao ghi một quyết định kỹ thuật để người đến sau hiểu constraint, phương án bị loại và thời điểm cần xét lại?",
        (MADR, PP),
        (
            ("ADR lưu reasoning, không chỉ lưu kết luận", "Dòng ‘chọn Parquet’ không giải thích workload, consumers hay constraint. ADR phải giữ context tại thời điểm quyết định để người đọc phân biệt quyết định sai với constraint đã đổi. Nếu chỉ còn kết luận, đội sau thường lặp lại tranh luận cũ hoặc áp lựa chọn vào bối cảnh khác.", "Một ADR ngắn vẫn cần status, context, decision drivers, options, outcome, consequences và confirmation. Độ dài dưới hai trang buộc người viết chọn evidence quyết định thay vì chép toàn bộ cuộc họp."),
            ("Khóa tiêu chí trước khi so phương án", "Nếu tiêu chí xuất hiện sau lựa chọn, bảng so sánh dễ trở thành biện minh. Hãy nêu trước population, volume, latency, compatibility, operability, cost và reversibility. Mỗi tiêu chí cần unit hoặc ordinal rule đủ rõ để reviewer phản bác.", "Không phải mọi tiêu chí có trọng số bằng nhau. Correctness và compliance có thể là hard constraint; cost là biến tối ưu sau khi qua gate. Gộp chúng thành một điểm tổng duy nhất có thể che việc phương án thắng nhờ bù một vi phạm không được phép."),
            ("Phương án bị loại là tài sản", "Ít nhất hai phương án thực phải được mô tả trong điều kiện tốt nhất của chúng. Strawman làm ADR trông chắc chắn nhưng không giúp quyết định. Với mỗi option, ghi lợi ích, chi phí, failure mode và evidence nào có thể đảo đánh giá.", "Phương án ‘không làm gì’ hoặc trì hoãn cũng là option nếu nó hợp lệ. Nó làm lộ cost of change và urgency. Tuy nhiên, không dùng nó để né quyết định khi risk đang tích lũy; consequence phải ghi cả chi phí của việc chờ."),
            ("Consequence gồm cả khoản nợ được chấp nhận", "Mỗi quyết định tạo thuận lợi và giới hạn. Chọn CSV tăng interoperability nhưng làm schema và type ambiguity khó kiểm soát; chọn Parquet giảm scan cost nhưng tăng yêu cầu reader compatibility và inspection tooling. ADR phải ghi phần xấu bằng ngôn ngữ vận hành.", "Consequence cần owner và hành động khi có thể: ai giữ compatibility suite, ai theo dõi file size, ai chịu migration. Nếu không có owner, consequence chỉ là lời cảnh báo không tạo thay đổi hành vi."),
            ("Reversibility và option value", "Quyết định dễ rollback nên được timebox để học nhanh. Quyết định thay identifier, public schema hoặc storage layout khó đảo cần evidence và migration path mạnh hơn. Reversibility không phải nhãn yes/no; nó gồm thời gian, dữ liệu phải chuyển, số consumer và khả năng dual-run.", "Một spike có giá trị khi giảm uncertainty quyết định. Nó phải nêu hypothesis, fixture, expected discriminating observation và stop condition. Demo thành công nhưng không phân biệt hai options thì không tạo evidence cho ADR."),
            ("Revisit signal phải kiểm được", "‘Xem lại khi cần’ không phải signal. Signal tốt có metric hoặc sự kiện: median file vượt 1 GB, có consumer cần random row update, scan cost vượt ngưỡng hoặc library mất support. Khi signal xảy ra, ADR chuyển sang review chứ không tự động đảo quyết định.", "ADR mới supersede ADR cũ thay vì sửa lịch sử như chưa từng có lựa chọn trước. Chuỗi quyết định giúp thấy constraint tiến hóa và tránh gán logic mới cho evidence cũ."),
        ),
        "Hai đội trao đổi 200 GB sự kiện mỗi ngày. Nhóm so CSV, JSON và Parquet theo schema enforcement, interoperability, scan pattern, compression và debugging. Parquet thắng cho batch analytics; CSV giữ làm export nhỏ cho đối tác. ADR ghi reader compatibility suite, ngưỡng file nhỏ cần compaction và signal xét lại nếu workload chuyển sang point update.",
        ("Chọn phương án trước rồi mới tạo tiêu chí.", "Chỉ ghi mặt tốt của lựa chọn thắng.", "Dùng option giả yếu để tránh phản biện.", "Không có revisit signal hoặc confirmation test."),
        ("Reviewer tái tạo được recommendation từ drivers và evidence.", "Changed constraint đủ lớn làm recommendation đảo theo rule đã ghi.", "Mỗi option có ít nhất một failure mode thật.", "Consequence có owner hoặc được đánh dấu risk được chấp nhận.", "Spike phân biệt hai option thay vì chỉ chứng minh một demo chạy.", "ADR mới supersede bản cũ mà giữ nguyên lịch sử."),
        "ADR tốt làm reasoning có thể kiểm tra lại; nó không biến lựa chọn phụ thuộc bối cảnh thành chân lý lâu dài.",
    ),
    Lesson(
        4,
        "Lesson_004-git-as-a-content-addressed-object-database",
        "Git as a content-addressed object database",
        "git-content-addressed-object-database",
        "wiki.engineering-foundation.git-object-database",
        "Mô hình object, snapshot, index và references giải thích các thao tác Git như thế nào?",
        (PROGIT,),
        (
            ("Git lưu snapshot qua object graph", "Blob giữ nội dung file, tree ánh xạ tên và mode tới blob hoặc tree con, commit trỏ tới top-level tree cùng parent và metadata. Commit vì thế là node trong graph của snapshot, không phải một patch được lưu như đơn vị gốc. Diff là phép so sánh Git tính ra giữa hai trạng thái.", "Hai file có cùng content có thể dùng cùng blob dù tên khác, vì tên nằm trong tree. Hai commit có tree giống nhau vẫn có identity khác nếu parent, author, timestamp hoặc message khác. Điều này giải thích vì sao cherry-pick hoặc rebase tạo commit mới dù patch trông giống."),
            ("Content-addressed identity", "Object ID được suy từ type, size và content theo object format của repository. Thay một byte trong blob tạo identity khác; tree trỏ blob mới nên tree đổi; commit trỏ tree mới nên commit đổi. Chuỗi ảnh hưởng này tạo integrity có thể kiểm tra bằng traversal.", "Không nên dạy SHA-1 như bản chất duy nhất của Git. Bản chất là object được gọi bằng digest của nội dung đã canonicalize; repository có thể dùng object format khác. Lab phải hỏi Git bằng `git hash-object` và `git cat-file`, không hard-code độ dài hash."),
            ("Working tree, index và repository", "Working tree là bản checkout có thể sửa; index là snapshot dự kiến cho commit kế tiếp; repository giữ object và refs. `git add` cập nhật index bằng content hiện tại, không đơn giản đặt cờ ‘đã theo dõi’. Sửa file lần nữa sau add tạo hai phiên bản: index giữ bản đã stage, working tree giữ bản mới hơn.", "`git status` và `git diff` chỉ có nghĩa khi biết hai trạng thái đang được so. `git diff` mặc định so working tree với index; `git diff --cached` so index với `HEAD`. Học thuộc output mà không nêu cặp trạng thái dẫn tới dự đoán sai khi partial staging."),
            ("References làm graph có tên", "Branch là ref có thể di chuyển tới commit. `HEAD` thường là symbolic ref trỏ tới branch hiện tại; branch lại trỏ tới commit. Commit mới dùng commit hiện tại làm parent rồi cập nhật branch. Detached HEAD bỏ lớp branch nhưng không phá object graph.", "Xóa branch chỉ xóa một ref, không xóa object ngay lập tức. Commit còn reachable từ ref khác hoặc reflog vẫn có thể tìm và phục hồi. Sau khi không còn reachable và hết retention, garbage collection mới có thể loại object; vì vậy ‘xóa nhánh luôn an toàn’ cũng là kết luận quá rộng."),
            ("Reset được suy từ ba cây", "Để hiểu reset, theo dõi `HEAD`, index và working tree riêng. `--soft` di chuyển ref/HEAD nhưng giữ index và working tree; mixed reset còn cập nhật index; hard reset cập nhật cả working tree và có thể làm mất thay đổi chưa lưu. Cú pháp nguy hiểm vì phạm vi mutation khác nhau, không phải vì tên lệnh khó nhớ.", "Trước reset, ghi bảng trạng thái của ba vùng và dự đoán từng cột sau lệnh. Nếu mục tiêu chỉ bỏ stage hoặc khôi phục file, dùng command hẹp hơn giúp giảm blast radius. Không chạy hard reset dựa trên trực giác ‘quay lại commit’."),
            ("Đọc object thô để kiểm mô hình", "Một repository ba commit đủ để kiểm mọi mệnh đề nền. Dùng `git rev-parse`, `git cat-file -t/-p`, `git ls-tree`, `git show-ref` và `git symbolic-ref HEAD` để dựng graph từ evidence. Dự đoán trước mỗi command rồi so output, tránh biến lab thành chép lệnh.", "Bằng chứng cần ghi Git version, object format, commit IDs trước–sau và trạng thái ba vùng. Nếu command hiện đại thay output so với sách 2014, giữ cơ chế ổn định và ghi khác biệt phiên bản thay vì ép output cũ."),
        ),
        "Một file `orders.csv` được commit ba lần, lần hai thêm dòng và lần ba đổi tên. Học viên chứng minh blob của content không đổi được tái dùng, tree đổi khi tên đổi, commit đổi theo tree/parent, rồi tạo và xóa một branch để thấy ref biến mất trong khi commit còn trong reflog.",
        ("Nghĩ commit lưu patch thay vì snapshot graph.", "Nghĩ staging area chỉ là danh sách tên file.", "Đồng nhất `HEAD` với commit thay vì symbolic ref trong trường hợp thường.", "Tin rằng xóa branch lập tức xóa commit hoặc hard reset luôn phục hồi được."),
        ("Dựng đúng blob-tree-commit graph từ `cat-file`.", "Stage rồi sửa tiếp phải quan sát được hai phiên bản file.", "Xóa branch nhưng tìm lại commit qua reflog.", "Soft, mixed và hard reset tạo đúng ba trạng thái đã dự đoán.", "Đổi message nhưng giữ tree vẫn tạo commit identity mới.", "Clone sandbox và tái dựng graph trên Git version đã ghi."),
        "Khi coi Git là object graph cộng refs và ba vùng, command trở thành hệ quả có thể dự đoán thay vì danh sách phải học thuộc.",
    ),
    Lesson(
        5,
        "Lesson_005-branching-merge-rebase-and-commit-identity",
        "Branching, merge, rebase and commit identity",
        "branching-merge-rebase-commit-identity",
        "wiki.engineering-foundation.git-history-integration",
        "Khi nào nên merge, rebase, squash hoặc revert, và lựa chọn đó thay đổi graph cùng người dùng khác ra sao?",
        (PROGIT,),
        (
            ("Branch là con trỏ, divergence nằm ở graph", "Tạo branch chỉ tạo ref tới commit hiện có. Khi hai branch nhận commit riêng, graph phân kỳ từ common ancestor. Work không được sao chép thành thư mục thứ hai; working tree được materialize theo commit mà `HEAD` chọn.", "Trước integration, vẽ tips, parents và merge base. Nếu một tip reachable từ tip kia, merge có thể fast-forward bằng cách di chuyển ref. Nếu histories đã diverge, Git cần kết hợp snapshots và thường tạo merge commit hai parent."),
            ("Three-way merge và conflict", "Three-way merge so hai tips với merge base. Thay đổi chỉ ở một phía thường được lấy tự động; thay đổi tương thích ở hai phía có thể kết hợp; thay đổi cạnh tranh trên cùng vùng khiến Git dừng. Conflict là bằng chứng thiếu quyết định nội dung, không phải lỗi engine.", "Giải conflict cần đọc base, ours và theirs rồi xây kết quả thỏa invariant hiện tại. Chọn nguyên một phía có thể xóa thay đổi hợp lệ của phía kia. Sau resolution, test phải kiểm behavior chứ không chỉ kiểm marker conflict đã biến mất."),
            ("Rebase phát lại thay đổi lên base mới", "Rebase tìm commits thuộc nhánh hiện tại nhưng không thuộc upstream, tính patch tương ứng rồi tạo commit mới trên base mới. Parent thay đổi nên commit identity thay đổi; author có thể được giữ nhưng committer metadata và graph không còn giống lịch sử cũ.", "Lịch sử thẳng giúp đọc tuyến tính nhưng đổi lấy việc viết lại identity. Nó phù hợp cho branch riêng trước khi chia sẻ. Khi commit cũ đã được người khác dùng, force update bắt họ reconcile hai histories tương đương về nội dung nhưng khác identity."),
            ("Merge, squash và thông tin bị giữ hoặc mất", "Merge commit giữ topology và parent của hai nhánh. Rebase giữ các bước logic theo tuyến nhưng thay identity. Squash tạo một commit tổng hợp và bỏ các boundary trung gian khỏi history đích. Không có lựa chọn luôn tốt; cần hỏi history được dùng để audit, bisect, revert hay chỉ để review kết quả.", "Nếu chuỗi commit biểu diễn migration theo bước có deploy checkpoint, squash có thể xóa thông tin vận hành cần thiết. Nếu branch chứa nhiều fixup noise không có giá trị độc lập, squash có thể giảm chi phí đọc. Quyết định phải dựa vào consumer của history."),
            ("Revert và reset giải hai bài toán khác", "Revert tạo commit mới có patch đảo tác dụng của commit đích; lịch sử công khai vẫn tiến về trước và collaborators không phải thay refs đã biết. Reset di chuyển ref và có thể cập nhật index/working tree; nó phù hợp cho lịch sử riêng hoặc phục hồi có kiểm soát.", "Revert merge cần chọn mainline parent và không đồng nghĩa Git quên merge cũ. Một revert sau đó có thể ảnh hưởng merge lại. Vì vậy incident trên shared branch cần rehearsal trong clone và graph review, không chạy lệnh theo tên gọi."),
            ("Quy tắc quyết định dựa trên phạm vi ảnh hưởng", "Hỏi ba câu: commit đã public chưa, topology có giá trị không, và cần giữ từng bước hay chỉ kết quả? Public history ưu tiên merge hoặc revert. Private history có thể rebase để sắp xếp. Squash phù hợp khi intermediate commits không phải đơn vị audit hoặc rollback.", "Mọi rewrite cần backup ref, kiểm remote state và dùng lease khi force push được policy cho phép. `--force-with-lease` giảm nguy cơ ghi đè cập nhật chưa thấy nhưng không thay thế phối hợp con người; lease đúng vẫn có thể phá consumer dùng commit cũ."),
        ),
        "Ba bản sao của cùng repository tích hợp một feature và hotfix. Bản A merge giữ topology, bản B rebase feature lên hotfix, bản C squash feature. Nhóm so `git log --graph`, commit IDs, khả năng revert từng bước và hành vi của một clone đã fetch lịch sử cũ. Sau đó họ xử lý một conflict bằng cách kiểm invariant thay vì chọn ours/theirs nguyên khối.",
        ("Rebase branch đã chia sẻ mà không phối hợp.", "Dùng `reset --hard` để sửa shared branch.", "Giải conflict bằng giữ một phía mà không đọc base.", "Squash chuỗi migration cần rollback theo từng bước."),
        ("Dự đoán merge base và loại merge trước khi chạy.", "Chứng minh rebase tạo identity mới cho commits được replay.", "Một clone cũ minh họa blast radius của force update.", "Revert giữ lịch sử tiến tới và tạo commit mới.", "Conflict resolution qua test invariant chứ không qua absence of markers.", "Bốn scenario đạt ít nhất ba lựa chọn đúng kèm affected users."),
        "Lựa chọn integration là quyết định về graph, identity và collaborators; lịch sử ‘đẹp’ không được đánh đổi bằng blast radius không được công bố.",
    ),
)


def contract(lesson: Lesson) -> tuple[str, str, str, str, str, str]:
    text = (lesson.folder / "note.md").read_text()
    after_path = lesson.folder / "after-note.md"
    after = after_path.read_text() if after_path.exists() else ""

    def field(body: str, name: str) -> str:
        match = re.search(rf"(?m)^\*\*{re.escape(name)}\.\*\*\s*(.+)$", body)
        return match.group(1).strip() if match else ""

    legacy = tuple(field(text, name) for name in ("Outcome", "Đánh giá", "Lab", "Pitfalls", "Self-study (2,4 giờ)", "Done when"))
    if all(legacy):
        return legacy  # type: ignore[return-value]
    tasks = re.findall(r"(?m)^\*\*Nhiệm vụ\.\*\*\s*(.+)$", after)
    restored = (
        field(text, "Năng lực cần chứng minh"),
        field(after, "Cách đánh giá"),
        tasks[0] if tasks else "",
        field(after, "Lỗi cần chủ động loại trừ"),
        tasks[1] if len(tasks) > 1 else "",
        field(text, "Điều kiện hoàn thành"),
    )
    if not all(restored):
        raise ValueError(f"L{lesson.number}: cannot recover curriculum contract")
    return restored


def frontmatter(lesson: Lesson) -> str:
    source_lines = "\n".join(f"  - {source}" for source in lesson.sources)
    return f"""---
note_id: {lesson.note_id}
note_type: concept-deep-dive
status: review
language: vi
created: 2026-10-02
last_verified: 2026-10-02
review_after: 2027-04-02
editorial_pass: humanized-v3
primary_question: {lesson.question}
source_ids:
{source_lines}
aliases: [{lesson.title}]
tags: [wiki/software-engineering, engineering-foundation]
reference_path: Material/DE/Reference/Library/Knowledge-Notes/PACK-ENGINEERING-FOUNDATION-01/{lesson.filename}
---
"""


def knowledge_note(lesson: Lesson) -> str:
    parts = [frontmatter(lesson), f"\n# {lesson.title}\n\n> [!abstract] Câu hỏi trung tâm\n> {lesson.question}\n"]
    for index, (heading, first, second) in enumerate(lesson.sections, 1):
        parts.append(f"\n## {index}. {heading}\n\n{first}\n\n{second}\n")
        if index == 2:
            parts.append(f"\n> [!synthesis]\n> Phần này ghép contract của roadmap DE-L{lesson.number:03d} với các lát nguồn đã khai báo. Mọi threshold và tình huống cụ thể là thiết kế giáo trình, không phải lời trích nguyên văn của tác giả.\n")
    parts.append(f"\n## 7. Tình huống xuyên suốt\n\n{lesson.case}\n\nTình huống của `{lesson.note_id}` phải được chạy trong sandbox hoặc fixture có version. Nếu chưa chạy, các kết quả mong đợi chỉ là protocol đánh giá; không được ghi thành observation. Người học giữ input, command, state trước–sau, raw output và một oracle độc lập đủ để reviewer tái hiện câu hỏi riêng của bài `{lesson.title}`.\n")
    parts.append("\n## 8. Failure modes và ngộ nhận\n")
    for item in lesson.failure_modes:
        parts.append(f"\n- **Failure mode.** {item} Cần đưa một counterexample nhỏ nhất để chứng minh hậu quả, sau đó ghi owner và cách phục hồi thay vì chỉ sửa câu chữ.\n")
    parts.append("\n## 9. Ma trận kiểm chứng\n\nMỗi probe dưới đây bắt đầu bằng dự đoán viết trước. Kết quả đạt chỉ được ghi khi artifact thực tế khớp oracle; exit code thành công không thay thế kiểm tra semantics.\n")
    for index, probe in enumerate(lesson.probes, 1):
        parts.append(f"\n### 9.{index}. {probe}\n\n**Mệnh đề.** {probe}\n\n**Thiết kế phép thử.** Tạo positive control và một boundary hoặc changed-constraint case chỉ khác đúng biến cần kiểm. Khóa fixture, phiên bản, identity và state ban đầu; ghi expected result trước khi chạy.\n\n**Bằng chứng.** Giữ command, raw output, state transition và reconciliation với oracle không dùng chung assumption. Nếu evidence không phân biệt được mệnh đề đúng và sai, probe chưa có giá trị quyết định.\n")
    parts.append("\n## 10. Câu hỏi tự kiểm tra\n\n1. Boundary nào làm mệnh đề trung tâm không còn đúng?\n2. Artifact nào là nguồn thẩm quyền và artifact nào chỉ là tín hiệu?\n3. Counterexample nhỏ nhất cần những state nào?\n4. Một kiểm tra xanh giả có thể xuất hiện theo đường nào?\n5. Constraint nào khiến quyết định phải đảo?\n6. Phần nào hiện mới là protocol, chưa phải observation?\n")
    parts.append("\n## 11. Giới hạn và điều chưa cho phép kết luận\n\n- Nội dung là giáo trình và expected evidence; không tuyên bố đã kiểm chứng trên production.\n- Hành vi phụ thuộc phiên bản phải được chạy lại với version ghi trong evidence package.\n- Threshold, case study và decision rule tổng hợp cho curriculum không được gán nguyên văn cho nguồn.\n- Note giữ trạng thái `review` cho tới khi owner duyệt semantics và learner artifact.\n")
    refs = "\n".join(f"{i}. [[{SOURCE_LABELS[source]}]]" for i, source in enumerate(lesson.sources, 1))
    rows = []
    for source in lesson.sources:
        if source == SOM:
            locator = "Chapter 4 PDF 103–132; Chapter 7 PDF 169–212"
            kept = "requirement validation, interface, decomposition và information hiding"
        elif source == PP:
            locator = "Topic 10 PDF 76–83"
            kept = "orthogonality, change isolation và decision discipline"
        elif source == MADR:
            locator = "ADR core và MADR additions; accessed 2026-10-01"
            kept = "context, drivers, options, decision, consequences và confirmation"
        else:
            locator = "Chapter 1 PDF 42–43; Chapter 3 PDF 129–174; Chapter 7 PDF 422–434; Chapter 10 PDF 762–790"
            kept = "object graph, refs, merge, rebase, reset và identity"
        rows.append(f"| [[{SOURCE_LABELS[source]}]] — `{source}` | {locator} | {kept} | §§1–9 | Đã phủ | Nội dung ngoài objective DE-L{lesson.number:03d} |")
    coverage = "\n".join(rows)
    parts.append(f"\n## Reference\n\n{refs}\n\n## Source coverage\n\n| Source slice | Locator | Kiến thức phải giữ | Vị trí | Trạng thái | Ngoài phạm vi |\n|---|---|---|---|---|---|\n{coverage}\n\n## Key takeaways\n\n- {lesson.takeaway}\n- Một kết luận chỉ có giá trị trong scope, version và state đã ghi.\n- Counterexample và changed-constraint test mạnh hơn việc lặp lại định nghĩa.\n- Trước khi lab chạy, note này đã có provenance và protocol nhưng chưa phải chứng nhận production.\n")
    return normalize_markdown("".join(parts))


def curriculum_files(lesson: Lesson, knowledge: str) -> tuple[str, str]:
    outcome, assessment, lab, pitfalls, homework, done = contract(lesson)
    header = f"# Phase 1: Engineering Foundation\n# Module 1: Engineering Thinking, Git and Debugging\n# Lesson {lesson.number}: {lesson.title}"
    body = re.sub(r"^---\n.*?\n---\n", "", knowledge, flags=re.S)
    body = re.sub(r"^# .+\n+", "", body, count=1)
    note = f"{header}\n\n## Mục tiêu bài học\n\n**Năng lực cần chứng minh.** {outcome}\n\n**Điều kiện hoàn thành.** {done}\n\n{body}"
    after = f"""{header}

## Thực hành

**Nhiệm vụ.** {lab}

Chỉ dùng fixture hoặc sandbox được phép. Viết dự đoán trước khi chạy; giữ input, versions, commands, state trước–sau, raw failures, reconciliation và limitations.

## Kiểm tra cuối bài

1. Nêu invariant, identity, state và boundary.
2. Vẽ hoặc mô tả transition trước khi thao tác.
3. Tái hiện một failure hoặc changed-constraint case.
4. Đối soát bằng oracle độc lập và công bố phần chưa kiểm.

## Tiêu chí hoàn thành

**Cách đánh giá.** {assessment}

**Điều kiện đạt.** {done}

## Bài làm sau buổi học

**Nhiệm vụ.** {homework}

**Lỗi cần chủ động loại trừ.** {pitfalls}

## Reference

- Knowledge note: `{(PACK / lesson.filename).relative_to(ROOT)}`
- Nội dung học thuật: `note.md` cùng thư mục.
"""
    return note, after


def update_manifest(check: bool) -> list[str]:
    data = json.loads(MANIFEST.read_text())
    failures: list[str] = []
    source_expected = {
        "source_id": PROGIT,
        "record_path": "1_Nguon/Books/SRC-CHACON-STRAUB-PRO-GIT-2E.md",
        "canonical_path": str(ROOT / "Material/Reference_temp/Pro_Git_-_Scott_Chacon.pdf"),
        "sha256": "fe6c23508d76a5e31a2022dd34bbb21005e194f168a4608f273099f3c3b4b3ab",
        "captured": "2026-10-02",
        "rights": "copyrighted-private-owner-provided",
    }
    source_by_id = {item.get("source_id"): item for item in data["source_registry"]}
    if check:
        actual = source_by_id.get(PROGIT)
        if actual != source_expected:
            failures.append("manifest source drift: Pro Git")
    else:
        data["source_registry"] = [item for item in data["source_registry"] if item.get("source_id") != PROGIT]
        data["source_registry"].append(source_expected)
    note_ids = {lesson.note_id for lesson in LESSONS}
    if not check:
        data["note_registry"] = [item for item in data["note_registry"] if item.get("note_id") not in note_ids]
        data["retrieval_test_set"] = [item for item in data["retrieval_test_set"] if item.get("expected_note_id") not in note_ids]
    note_by_id = {item.get("note_id"): item for item in data["note_registry"]}
    retrieval = {(item.get("query"), item.get("expected_note_id")) for item in data["retrieval_test_set"]}
    for lesson in LESSONS:
        expected = {"note_id": lesson.note_id, "path": f"2_Wiki/Software-Engineering/{lesson.title}.md", "status": "review", "source_ids": list(lesson.sources), "last_verified": "2026-10-02"}
        queries = (f"L{lesson.number} decision boundary nào?", f"L{lesson.number} counterexample nào?", f"L{lesson.number} evidence nào quyết định?")
        if check:
            if note_by_id.get(lesson.note_id) != expected:
                failures.append(f"manifest note drift: {lesson.note_id}")
            for query in queries:
                if (query, lesson.note_id) not in retrieval:
                    failures.append(f"missing retrieval: {query}")
        else:
            data["note_registry"].append(expected)
            data["retrieval_test_set"].extend({"query": query, "expected_note_id": lesson.note_id} for query in queries)
    if not check:
        data["version"] = "1.0.88"
        data["updated_at"] = "2026-10-03T00:20:00+07:00"
        data["layers"]["1_Nguon"]["source_count"] = len(data["source_registry"])
        data["layers"]["2_Wiki"]["note_count"] = len(data["note_registry"])
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale: list[str] = []
    digest = hashlib.sha256()
    for lesson in LESSONS:
        knowledge = knowledge_note(lesson)
        note, after = curriculum_files(lesson, knowledge)
        targets = ((PACK / lesson.filename, knowledge), (WIKI / f"{lesson.title}.md", knowledge), (lesson.folder / "note.md", note), (lesson.folder / "after-note.md", after))
        for target, content in targets:
            if args.check:
                if not target.exists() or target.read_text() != content:
                    stale.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
        digest.update(note.encode())
        digest.update(after.encode())
    stale.extend(update_manifest(args.check))
    if stale:
        print("STALE\n" + "\n".join(stale))
        return 1
    print(("checked" if args.check else "written") + f"=20 stale=0 fingerprint={digest.hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
