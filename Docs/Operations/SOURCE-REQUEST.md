# Danh sách nguồn cần chuẩn bị

> Cổng dừng của Bước 3. Danh sách này chọn nguồn cho toàn bộ DA và DE; chưa có nguồn nào được coi là đã đọc. Sau khi chuẩn bị xong, owner trả lời `done` để bắt đầu đọc sâu.

## Phạm vi và nguyên tắc

- Registry được phủ: **2 chương trình · 14 phase · 40 module · 525 bài**.
- Mỗi module và bài có tối thiểu **3 sách · 3 document/spec · 3 website · 3 video · 1 Coursera course có path cụ thể**.
- Bài kế thừa gói nguồn của module để bảo đảm baseline; ánh xạ đủ 525 bài nằm trong `Tools/Curriculum/Manifests/Academic/source-plan.json`.
- Khi đọc sâu, từng bài sẽ khóa chapter/page/section/timestamp riêng và thay nguồn nếu gói module không đủ sát nội dung bài.
- Docs/spec sống được đọc tại nguồn chính thức; không cần tải thủ công nếu chấp nhận đọc trực tuyến.
- Sách thương mại chỉ lấy qua nhà xuất bản, thư viện hoặc bản đã mua hợp pháp.
- Tệp local có nguồn gốc chưa xác nhận không được dùng làm căn cứ xuất bản.
- Chương/trang chính xác được khóa sau khi đọc; bước này chỉ khóa nguồn và phạm vi chủ đề.

## Việc owner cần làm

### 1. Mua hoặc mượn thư viện

| Mã | Nguồn | Phạm vi dùng | Đường lấy hợp pháp |
|---|---|---|---|
| `SRC-KIMBALL` | The Data Warehouse Toolkit — Wiley | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 | [Nhà xuất bản](https://www.wiley.com/en-us/The+Data+Warehouse+Toolkit%3A+The+Definitive+Guide+to+Dimensional+Modeling%2C+3rd+Edition-p-9781118530801) |
| `SRC-STORY` | Storytelling with Data — Wiley | DA-M01, DA-M06, DA-M07, DA-M10, DA-M11 | [Nhà xuất bản](https://www.wiley.com/en-us/Storytelling+with+Data%3A+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253) |
| `SRC-TOCE` | Trustworthy Online Controlled Experiments — Cambridge University Press | DA-M05, DA-M07, DA-M08 | [Nhà xuất bản](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) |
| `SRC-DDIA` | Designing Data-Intensive Applications, Second Edition — O'Reilly Media | DE-M11, DE-M13, DE-M14, DE-M15, DE-M20, DE-M21, DE-M22, DE-M23, DE-M27 | [Nhà xuất bản](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) |
| `PACK-DA_FOUNDATIONS-BOOK-01` | Data Science for Business — O'Reilly Media | DA-M01, DA-M10, DA-M11 | [Nhà xuất bản](https://www.oreilly.com/library/view/data-science-for/9781449374273/) |
| `PACK-DA_FOUNDATIONS-BOOK-02` | The Truthful Art — New Riders | DA-M01, DA-M10, DA-M11 | [Nhà xuất bản](https://www.pearson.com/en-us/subject-catalog/p/truthful-art-the-data-charts-and-maps-for-communication/P200000009761) |
| `PACK-PRODUCT_ANALYTICS-BOOK-01` | Lean Analytics — O'Reilly Media | DA-M07 | [Nhà xuất bản](https://www.oreilly.com/library/view/lean-analytics/9781449335687/) |
| `PACK-PRODUCT_ANALYTICS-BOOK-02` | Product Analytics — O'Reilly Media | DA-M07 | [Nhà xuất bản](https://www.oreilly.com/library/view/product-analytics/9781492026433/) |
| `PACK-EXCEL_BI-BOOK-01` | M Is for (Data) Monkey — Apress | DA-M02, DA-M06 | [Nhà xuất bản](https://link.springer.com/book/10.1007/978-1-4842-6383-9) |
| `PACK-EXCEL_BI-BOOK-02` | The Definitive Guide to DAX — Microsoft Press | DA-M02, DA-M06 | [Nhà xuất bản](https://www.microsoftpressstore.com/store/definitive-guide-to-dax-business-intelligence-for-9780134865867) |
| `PACK-EXCEL_BI-BOOK-03` | The Big Book of Dashboards — Wiley | DA-M02, DA-M06 | [Nhà xuất bản](https://www.wiley.com/en-us/The+Big+Book+of+Dashboards%3A+Visualizing+Your+Data+Using+Real+World+Business+Scenarios-p-9781119282716) |
| `PACK-STATS_EXPERIMENT-BOOK-02` | Practical Statistics for Data Scientists — O'Reilly Media | DA-M05, DA-M08 | [Nhà xuất bản](https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/) |
| `PACK-PYTHON_ENGINEERING-BOOK-01` | Fluent Python, Second Edition — O'Reilly Media | DA-M09, DE-M01, DE-M02 | [Nhà xuất bản](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) |
| `PACK-PYTHON_ENGINEERING-BOOK-02` | Effective Python, Third Edition — Addison-Wesley | DA-M09, DE-M01, DE-M02 | [Nhà xuất bản](https://www.pearson.com/en-us/subject-catalog/p/effective-python-125-specific-ways-to-write-better-python/P200000011759) |
| `PACK-PYTHON_ENGINEERING-BOOK-03` | Python Concurrency with asyncio — Manning | DA-M09, DE-M01, DE-M02 | [Nhà xuất bản](https://www.manning.com/books/python-concurrency-with-asyncio) |
| `PACK-ALGORITHMS_ARCH-BOOK-01` | Algorithms, Fourth Edition — Addison-Wesley | DE-M03, DE-M04 | [Nhà xuất bản](https://algs4.cs.princeton.edu/home/) |
| `PACK-OS_NETWORK-BOOK-02` | The Linux Programming Interface — No Starch Press | DE-M05, DE-M06 | [Nhà xuất bản](https://nostarch.com/tlpi) |
| `PACK-OS_NETWORK-BOOK-03` | Computer Networking: A Top-Down Approach — Pearson | DE-M05, DE-M06 | [Nhà xuất bản](https://gaia.cs.umass.edu/kurose_ross/index.php) |
| `PACK-SOFTWARE_API-BOOK-02` | API Design Patterns — Manning | DE-M07, DE-M08 | [Nhà xuất bản](https://www.manning.com/books/api-design-patterns) |
| `PACK-SOFTWARE_API-BOOK-03` | The Pragmatic Programmer, 20th Anniversary Edition — Addison-Wesley | DE-M07, DE-M08 | [Nhà xuất bản](https://www.pearson.com/en-us/subject-catalog/p/the-pragmatic-programmer-your-journey-to-mastery-20th-anniversary-edition-2nd-edition/P200000000184) |
| `PACK-DATABASE_MODELING-BOOK-01` | Database System Concepts — McGraw Hill | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 | [Nhà xuất bản](https://www.db-book.com/) |
| `PACK-DATABASE_MODELING-BOOK-02` | Database Internals — O'Reilly Media | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13, DE-M14, DE-M15 | [Nhà xuất bản](https://www.oreilly.com/library/view/database-internals/9781492040330/) |
| `PACK-OLAP_FORMATS-BOOK-03` | Fundamentals of Data Engineering — O'Reilly Media | DE-M14, DE-M15, DE-M16, DE-M17, DE-M18, DE-M19 | [Nhà xuất bản](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) |
| `PACK-PIPELINE_GOV-BOOK-02` | Data Pipelines Pocket Reference — O'Reilly Media | DE-M16, DE-M17, DE-M18, DE-M19 | [Nhà xuất bản](https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/) |
| `PACK-PIPELINE_GOV-BOOK-03` | Data Quality Fundamentals — O'Reilly Media | DE-M16, DE-M17, DE-M18, DE-M19 | [Nhà xuất bản](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) |
| `PACK-DISTRIBUTED_STREAM-BOOK-02` | Kafka: The Definitive Guide, Second Edition — O'Reilly Media | DE-M20, DE-M21, DE-M22, DE-M23 | [Nhà xuất bản](https://www.oreilly.com/library/view/kafka-the-definitive/9781492043072/) |
| `PACK-DISTRIBUTED_STREAM-BOOK-03` | Streaming Systems — O'Reilly Media | DE-M20, DE-M21, DE-M22, DE-M23 | [Nhà xuất bản](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) |
| `PACK-AI_ENGINEERING-BOOK-01` | AI Engineering — O'Reilly Media | DE-M28 | [Nhà xuất bản](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) |
| `PACK-AI_ENGINEERING-BOOK-02` | Designing Machine Learning Systems — O'Reilly Media | DE-M28 | [Nhà xuất bản](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) |
| `PACK-AI_ENGINEERING-BOOK-03` | Hands-On Large Language Models — O'Reilly Media | DE-M28 | [Nhà xuất bản](https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/) |
| `PACK-LEADERSHIP-BOOK-02` | The Staff Engineer's Path — O'Reilly Media | DE-M29 | [Nhà xuất bản](https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/) |
| `PACK-LEADERSHIP-BOOK-03` | Accelerate — IT Revolution | DE-M29 | [Nhà xuất bản](https://itrevolution.com/product/accelerate/) |

### 2. Xác nhận quyền sử dụng tệp đang có

| Mã | Tệp | Phạm vi dùng | Yêu cầu |
|---|---|---|---|
| `SRC-COD` | `Material/DE/Reference/Library/knowledge/hardware/Computer Organization and Design 5E - Patterson Hennessy - 0124077269.pdf` | DE-M03, DE-M04, DE-M14, DE-M23 | Xác nhận bản được mua/cấp phép; nếu không, lấy qua [nhà xuất bản](https://www.elsevier.com/books/computer-organization-and-design-mips-edition/patterson/978-0-12-407726-3). |

### 3. Tải bản mở từ trang chính thức

| Mã | Nguồn | Phạm vi dùng | Link chính thức |
|---|---|---|---|
| `SRC-OPENINTRO` | OpenIntro Statistics — OpenIntro | DA-M05, DA-M08, DA-M11 | [Tải/đọc](https://www.openintro.org/book/os/) |
| `SRC-NIST-STAT` | NIST/SEMATECH e-Handbook of Statistical Methods — NIST | DA-M05, DA-M07, DA-M08 | [Tải/đọc](https://www.itl.nist.gov/div898/handbook/) |
| `SRC-PROGIT` | Pro Git — Git project / Apress | DE-M01, DE-M07 | [Tải/đọc](https://git-scm.com/book/en/v2) |
| `SRC-ODS` | Open Data Structures — Pat Morin | DE-M03, DE-M04 | [Tải/đọc](https://opendatastructures.org/) |
| `SRC-N2T` | Nand2Tetris — Nand2Tetris project | DE-M04 | [Tải/đọc](https://www.nand2tetris.org/course) |
| `SRC-OSTEP` | Operating Systems: Three Easy Pieces — Arpaci-Dusseau & Arpaci-Dusseau | DE-M05, DE-M06, DE-M10, DE-M20 | [Tải/đọc](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| `SRC-RFC9293` | RFC 9293: Transmission Control Protocol — IETF | DE-M06 | [Tải/đọc](https://www.rfc-editor.org/rfc/rfc9293.html) |
| `SRC-RFC9110` | RFC 9110: HTTP Semantics — IETF | DE-M05, DE-M06, DE-M08, DE-M16 | [Tải/đọc](https://www.rfc-editor.org/rfc/rfc9110.html) |
| `SRC-RFC8446` | RFC 8446: TLS 1.3 — IETF | DE-M06 | [Tải/đọc](https://www.rfc-editor.org/rfc/rfc8446.html) |
| `SRC-W3C-PROV` | W3C PROV Family — W3C | DE-M19 | [Tải/đọc](https://www.w3.org/TR/prov-overview/) |
| `SRC-AWS-WAF` | AWS Well-Architected Framework — Amazon Web Services | DE-M24 | [Tải/đọc](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) |
| `SRC-NIST-CSF` | Cybersecurity Framework 2.0 — NIST | DE-M26 | [Tải/đọc](https://www.nist.gov/cyberframework) |
| `SRC-NIST-AIRMF` | Artificial Intelligence Risk Management Framework — NIST | DE-M28 | [Tải/đọc](https://www.nist.gov/itl/ai-risk-management-framework) |
| `PACK-STATS_EXPERIMENT-DOCUMENT-02` | ASA statement on p-values — American Statistical Association | DA-M05, DA-M08 | [Tải/đọc](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) |

## Course Coursera theo module

| Module | Course | Path bắt buộc |
|---|---|---|
| `DA-M01` | [Introducing Data Analytics and Analytical Thinking](https://www.coursera.org/learn/google-introducing-data-analytics-and-analytical-thinking) | Module 1 — Transform data into insights |
| `DA-M02` | [Excel Skills for Business: Essentials](https://www.coursera.org/learn/excel-essentials) | Modules 1–7 — Excel core, formulas, data and charts |
| `DA-M03` | [SQL for Data Science](https://www.coursera.org/learn/sql-for-data-science) | Modules 1–4 — retrieval, filtering, joins and analysis |
| `DA-M04` | [Data Warehousing and Business Intelligence](https://www.coursera.org/learn/data-warehousing-business-intelligence) | Modules 1–2 — warehouse architecture and multidimensional modeling |
| `DA-M05` | [Statistics with Python](https://www.coursera.org/specializations/statistics-with-python) | Course 1 Modules 1–4; Course 2 Modules 1–4 |
| `DA-M06` | [Data Visualization Fundamentals](https://www.coursera.org/learn/data-visualization-fundamentals) | Module 1 onward — visualization foundations with Power BI |
| `DA-M07` | [Ask Questions to Make Data-Driven Decisions](https://www.coursera.org/learn/ask-questions-make-decisions) | Modules 1–4 — questions, decisions and stakeholders |
| `DA-M08` | [Statistics with Python](https://www.coursera.org/specializations/statistics-with-python) | Course 1 Modules 1–4; Course 2 Modules 1–4 |
| `DA-M09` | [Python for Data Science, AI & Development](https://www.coursera.org/learn/python-for-applied-data-science-ai) | Modules 1–5 — Python, structures, APIs and data |
| `DA-M10` | [Ask Questions to Make Data-Driven Decisions](https://www.coursera.org/learn/ask-questions-make-decisions) | Modules 1–4 — questions, decisions and stakeholders |
| `DA-M11` | [Google Data Analytics Capstone](https://www.coursera.org/learn/google-data-analytics-capstone) | Modules 1–4 — case study and portfolio |
| `DE-M01` | [Using Python to Interact with the Operating System](https://www.coursera.org/learn/python-operating-system) | Modules 1–7 — OS, files, processes, testing and automation |
| `DE-M02` | [Using Python to Interact with the Operating System](https://www.coursera.org/learn/python-operating-system) | Modules 1–7 — OS, files, processes, testing and automation |
| `DE-M03` | [Algorithms, Part I](https://www.coursera.org/learn/algorithms-part1) | Modules 2–13 — analysis, structures, sorting and searching |
| `DE-M04` | [Build a Modern Computer from First Principles](https://www.coursera.org/learn/build-a-computer) | Modules 2 and 4–8 — logic, arithmetic, memory, machine language, architecture and assembler |
| `DE-M05` | [Using Python to Interact with the Operating System](https://www.coursera.org/learn/python-operating-system) | Modules 1–7 — OS, files, processes, testing and automation |
| `DE-M06` | [The Bits and Bytes of Computer Networking](https://www.coursera.org/learn/computer-networking) | Modules 1–6 — layers, networking, transport and services |
| `DE-M07` | [Software Design and Architecture](https://www.coursera.org/specializations/software-design-architecture) | Courses 1–4 — design, patterns, architecture and capstone |
| `DE-M08` | [Back-End Developer Capstone](https://www.coursera.org/learn/back-end-developer-capstone) | Modules 1–4 — backend, database, API, auth and tests |
| `DE-M09` | [Database Management Essentials](https://www.coursera.org/learn/database-management) | Modules 4–12 — SQL, ERD, normalization and advanced queries |
| `DE-M10` | [Database Management Essentials](https://www.coursera.org/learn/database-management) | Modules 4–12 — SQL, ERD, normalization and advanced queries |
| `DE-M11` | [Data Warehousing and Business Intelligence](https://www.coursera.org/learn/data-warehousing-business-intelligence) | Modules 1–2 — warehouse architecture and multidimensional modeling |
| `DE-M12` | [Data Warehousing and Business Intelligence](https://www.coursera.org/learn/data-warehousing-business-intelligence) | Modules 1–2 — warehouse architecture and multidimensional modeling |
| `DE-M13` | [Introduction to Data Engineering](https://www.coursera.org/learn/introduction-to-data-engineering) | Modules 1–4 — role, ecosystem, lifecycle and platform |
| `DE-M14` | [Introduction to Big Data with Spark and Hadoop](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop) | Modules 1–7 — distributed processing, Spark and Hadoop |
| `DE-M15` | [Introduction to Data Engineering](https://www.coursera.org/learn/introduction-to-data-engineering) | Modules 1–4 — role, ecosystem, lifecycle and platform |
| `DE-M16` | [ETL and Data Pipelines with Shell, Airflow and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka) | Modules 1–5 — ETL, pipelines, Airflow and Kafka |
| `DE-M17` | [ETL and Data Pipelines with Shell, Airflow and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka) | Modules 1–5 — ETL, pipelines, Airflow and Kafka |
| `DE-M18` | [Introduction to Data Engineering](https://www.coursera.org/learn/introduction-to-data-engineering) | Modules 1–4 — role, ecosystem, lifecycle and platform |
| `DE-M19` | [Introduction to Data Engineering](https://www.coursera.org/learn/introduction-to-data-engineering) | Modules 1–4 — role, ecosystem, lifecycle and platform |
| `DE-M20` | [Introduction to Big Data with Spark and Hadoop](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop) | Modules 1–7 — distributed processing, Spark and Hadoop |
| `DE-M21` | [ETL and Data Pipelines with Shell, Airflow and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka) | Modules 1–5 — ETL, pipelines, Airflow and Kafka |
| `DE-M22` | [ETL and Data Pipelines with Shell, Airflow and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka) | Modules 1–5 — ETL, pipelines, Airflow and Kafka |
| `DE-M23` | [Introduction to Big Data with Spark and Hadoop](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop) | Modules 1–7 — distributed processing, Spark and Hadoop |
| `DE-M24` | [Reliable Google Cloud Infrastructure: Design and Process](https://www.coursera.org/learn/cloud-infrastructure-design-process) | Modules 2–10 — services, architecture, reliability and security |
| `DE-M25` | [Introduction to Containers w/ Docker, Kubernetes & OpenShift](https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift) | Modules 1–5 — containers, Kubernetes and operations |
| `DE-M26` | [Reliable Google Cloud Infrastructure: Design and Process](https://www.coursera.org/learn/cloud-infrastructure-design-process) | Modules 2–10 — services, architecture, reliability and security |
| `DE-M27` | [Reliable Google Cloud Infrastructure: Design and Process](https://www.coursera.org/learn/cloud-infrastructure-design-process) | Modules 2–10 — services, architecture, reliability and security |
| `DE-M28` | [Generative AI Engineering and Fine-Tuning Transformers](https://www.coursera.org/learn/generative-ai-engineering-and-fine-tuning-transformers) | Modules 1–2 — transformers, fine-tuning and PEFT |
| `DE-M29` | [Leading Teams: Developing as a Leader](https://www.coursera.org/learn/leading-teams-developing-as-a-leader) | Modules 1–4 — leadership, self, others and growth |

## Kiểm tra định lượng theo module

| Module | Book | Document | Website | Video | Coursera |
|---|---:|---:|---:|---:|---:|
| `DA-M01` | 3 | 3 | 5 | 3 | 1 |
| `DA-M02` | 3 | 4 | 3 | 3 | 1 |
| `DA-M03` | 3 | 3 | 3 | 3 | 1 |
| `DA-M04` | 3 | 4 | 3 | 3 | 1 |
| `DA-M05` | 3 | 4 | 3 | 3 | 1 |
| `DA-M06` | 4 | 3 | 3 | 3 | 1 |
| `DA-M07` | 4 | 5 | 3 | 3 | 1 |
| `DA-M08` | 3 | 4 | 3 | 3 | 1 |
| `DA-M09` | 3 | 4 | 3 | 3 | 1 |
| `DA-M10` | 3 | 4 | 4 | 3 | 1 |
| `DA-M11` | 4 | 4 | 5 | 3 | 1 |
| `DE-M01` | 4 | 4 | 3 | 3 | 1 |
| `DE-M02` | 3 | 4 | 3 | 3 | 1 |
| `DE-M03` | 3 | 4 | 3 | 3 | 1 |
| `DE-M04` | 3 | 3 | 4 | 3 | 1 |
| `DE-M05` | 3 | 6 | 3 | 3 | 1 |
| `DE-M06` | 3 | 6 | 3 | 3 | 1 |
| `DE-M07` | 4 | 4 | 3 | 3 | 1 |
| `DE-M08` | 3 | 5 | 3 | 3 | 1 |
| `DE-M09` | 3 | 3 | 3 | 3 | 1 |
| `DE-M10` | 4 | 3 | 3 | 3 | 1 |
| `DE-M11` | 4 | 3 | 3 | 3 | 1 |
| `DE-M12` | 3 | 3 | 3 | 3 | 1 |
| `DE-M13` | 4 | 3 | 4 | 3 | 1 |
| `DE-M14` | 4 | 5 | 3 | 3 | 1 |
| `DE-M15` | 3 | 6 | 3 | 3 | 1 |
| `DE-M16` | 3 | 7 | 3 | 3 | 1 |
| `DE-M17` | 3 | 4 | 3 | 3 | 1 |
| `DE-M18` | 3 | 6 | 3 | 3 | 1 |
| `DE-M19` | 3 | 6 | 3 | 3 | 1 |
| `DE-M20` | 4 | 3 | 3 | 3 | 1 |
| `DE-M21` | 4 | 3 | 3 | 3 | 1 |
| `DE-M22` | 4 | 4 | 3 | 3 | 1 |
| `DE-M23` | 4 | 4 | 3 | 3 | 1 |
| `DE-M24` | 3 | 6 | 3 | 3 | 1 |
| `DE-M25` | 3 | 5 | 3 | 3 | 1 |
| `DE-M26` | 3 | 6 | 3 | 3 | 1 |
| `DE-M27` | 6 | 3 | 3 | 3 | 1 |
| `DE-M28` | 3 | 4 | 3 | 3 | 1 |
| `DE-M29` | 5 | 4 | 3 | 3 | 1 |

## Nguồn đọc trực tuyến, không cần tải thủ công

Khi bước đọc sâu bắt đầu, locator sẽ ghi phiên bản hoặc ngày truy cập để tránh nội dung trôi theo thời gian.

| Mã | Loại | Nguồn | Phạm vi dùng |
|---|---|---|---|
| `SRC-MSL-DA` | website | [Training for Data Analysts](https://learn.microsoft.com/en-us/training/career-paths/data-analyst) — Microsoft Learn | DA-M01 |
| `SRC-MS-EXCEL` | document | [Excel help & learning](https://support.microsoft.com/en-us/excel) — Microsoft Support | DA-M02 |
| `SRC-MS-PQ` | document | [Power Query documentation](https://learn.microsoft.com/en-us/power-query/) — Microsoft Learn | DA-M02, DA-M04, DA-M06 |
| `SRC-MS-PBI` | website | [Power BI learning path directory](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-learning-path-directory) — Microsoft Learn | DA-M02, DA-M06, DA-M11, DE-M13 |
| `SRC-PG17` | document | [PostgreSQL 17 Documentation](https://www.postgresql.org/docs/17/) — PostgreSQL Global Development Group | DA-M03, DA-M04, DA-M11, DE-M08, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13, DE-M22 |
| `SRC-PANDAS` | document | [pandas User Guide](https://pandas.pydata.org/docs/user_guide/) — pandas project | DA-M09 |
| `SRC-PYTHON` | document | [Python 3 Documentation](https://docs.python.org/3/) — Python Software Foundation | DA-M09, DE-M01, DE-M02, DE-M03 |
| `SRC-GOOGLE-TW` | website | [Technical Writing Courses](https://developers.google.com/tech-writing) — Google for Developers | DA-M01, DA-M10, DA-M11 |
| `SRC-AMPLITUDE` | document | [Product Analytics documentation](https://www.amplitude.com/docs/analytics/product-analytics) — Amplitude | DA-M07 |
| `SRC-SEGOOGLE` | book | [Software Engineering at Google](https://abseil.io/resources/swe-book) — Google / O'Reilly | DE-M07, DE-M08, DE-M27, DE-M29 |
| `SRC-LINUX-MAN` | document | [Linux man-pages project](https://www.kernel.org/doc/man-pages/) — Linux man-pages project | DE-M05, DE-M06 |
| `SRC-PY-ASYNC` | document | [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html) — Python Software Foundation | DE-M02, DE-M05, DE-M16 |
| `SRC-IOURING` | document | [io_uring(7)](https://man7.org/linux/man-pages/man7/io_uring.7.html) — Linux man-pages / liburing | DE-M05 |
| `SRC-OPENAPI` | document | [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — OpenAPI Initiative | DE-M07, DE-M08 |
| `SRC-OWASP-API` | document | [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) — OWASP | DE-M07, DE-M08, DE-M26 |
| `SRC-DBT` | document | [dbt Developer Hub](https://docs.getdbt.com/) — dbt Labs | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13, DE-M17, DE-M18, DE-M19 |
| `SRC-DUCKDB` | document | [DuckDB documentation and publications](https://duckdb.org/why_duckdb) — DuckDB Foundation | DE-M14 |
| `SRC-CLICKHOUSE` | document | [ClickHouse Documentation](https://clickhouse.com/docs) — ClickHouse | DE-M14 |
| `SRC-PARQUET` | document | [Apache Parquet documentation and format](https://parquet.apache.org/docs/) — Apache Software Foundation | DE-M15 |
| `SRC-AVRO` | document | [Apache Avro Specification](https://avro.apache.org/docs/current/specification/) — Apache Software Foundation | DE-M15 |
| `SRC-ICEBERG` | document | [Apache Iceberg Table Specification](https://iceberg.apache.org/spec/) — Apache Software Foundation | DE-M15 |
| `SRC-DELTA` | document | [Delta Lake Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md) — Delta Lake project | DE-M14, DE-M15 |
| `SRC-AIRBYTE` | document | [Airbyte Documentation](https://docs.airbyte.com/) — Airbyte | DE-M16 |
| `SRC-SINGER` | document | [Singer Specification](https://hub.meltano.com/singer/spec/) — Singer / Meltano | DE-M16 |
| `SRC-AIRFLOW` | document | [Apache Airflow Core Concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/) — Apache Software Foundation | DE-M16, DE-M17, DE-M18, DE-M19 |
| `SRC-GX` | document | [Great Expectations Documentation](https://docs.greatexpectations.io/docs/) — Great Expectations | DE-M18 |
| `SRC-OPENLINEAGE` | document | [OpenLineage Specification](https://openlineage.io/docs/spec/object-model/) — OpenLineage project | DE-M19 |
| `SRC-KAFKA` | document | [Apache Kafka Documentation](https://kafka.apache.org/documentation/) — Apache Software Foundation | DE-M20, DE-M21, DE-M22, DE-M23 |
| `SRC-DEBEZIUM` | document | [Debezium Documentation](https://debezium.io/documentation/reference/stable/) — Debezium project | DE-M20, DE-M21, DE-M22, DE-M23 |
| `SRC-SPARK` | document | [Apache Spark Documentation](https://spark.apache.org/docs/latest/) — Apache Software Foundation | DE-M23 |
| `SRC-FLINK` | document | [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/) — Apache Software Foundation | DE-M20, DE-M21, DE-M22, DE-M23 |
| `SRC-GCP-WAF` | document | [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) — Google Cloud | DE-M24 |
| `SRC-AZURE-WAF` | document | [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) — Microsoft | DE-M24 |
| `SRC-DOCKER` | document | [Docker Documentation](https://docs.docker.com/) — Docker | DE-M25 |
| `SRC-TERRAFORM` | document | [Terraform Documentation](https://developer.hashicorp.com/terraform/docs) — HashiCorp | DE-M25 |
| `SRC-K8S` | document | [Kubernetes Documentation](https://kubernetes.io/docs/home/) — Kubernetes project / CNCF | DE-M24, DE-M25, DE-M26, DE-M27 |
| `SRC-SRE` | book | [Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/) — Google | DE-M24, DE-M25, DE-M26, DE-M27, DE-M29 |
| `SRC-OTEL` | document | [OpenTelemetry Documentation and Specification](https://opentelemetry.io/docs/concepts/) — OpenTelemetry / CNCF | DE-M18, DE-M26 |
| `SRC-OWASP-LLM` | document | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — OWASP | DE-M28 |
| `SRC-OPENAI` | document | [OpenAI API Documentation](https://developers.openai.com/api/docs) — OpenAI | DE-M28 |
| `PACK-DA_FOUNDATIONS-DOCUMENT-01` | document | [Data Analyst career path](https://learn.microsoft.com/en-us/training/career-paths/data-analyst) — Microsoft Learn | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-DOCUMENT-02` | document | [Technical Writing Courses](https://developers.google.com/tech-writing) — Google for Developers | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-DOCUMENT-03` | document | [Google Engineering Practices](https://google.github.io/eng-practices/) — Google | DA-M01, DA-M10, DA-M11, DE-M07, DE-M08, DE-M29 |
| `PACK-DA_FOUNDATIONS-WEBSITE-01` | website | [Google Data Analytics Certificate](https://www.coursera.org/professional-certificates/google-data-analytics) — Google / Coursera | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-WEBSITE-02` | website | [Data-to-Viz](https://www.data-to-viz.com/) — Yan Holtz | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-WEBSITE-03` | website | [Storytelling with Data resources](https://www.storytellingwithdata.com/resources) — Storytelling with Data | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-VIDEO-01` | video | [Google Career Certificates video library](https://www.youtube.com/@GoogleCareerCertificates) — Google | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-VIDEO-02` | video | [Storytelling with Data video library](https://www.youtube.com/@storytellingwithdata) — Storytelling with Data | DA-M01, DA-M10, DA-M11 |
| `PACK-DA_FOUNDATIONS-VIDEO-03` | video | [Google Developers technical writing videos](https://developers.google.com/tech-writing/videos) — Google for Developers | DA-M01, DA-M10, DA-M11 |
| `PACK-PRODUCT_ANALYTICS-DOCUMENT-01` | document | [Google Analytics measurement documentation](https://developers.google.com/analytics) — Google | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-DOCUMENT-02` | document | [Amplitude Analytics documentation](https://www.amplitude.com/docs/analytics) — Amplitude | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-DOCUMENT-03` | document | [Microsoft experimentation platform papers](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/publications/) — Microsoft Research | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-WEBSITE-01` | website | [Amplitude Academy](https://academy.amplitude.com/) — Amplitude | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-WEBSITE-02` | website | [Mixpanel learning resources](https://mixpanel.com/content/guide-to-product-analytics/) — Mixpanel | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-WEBSITE-03` | website | [Microsoft Research experimentation group](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/) — Microsoft Research | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-VIDEO-01` | video | [Amplitude video library](https://www.youtube.com/@Amplitude) — Amplitude | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-VIDEO-02` | video | [Google Analytics video library](https://www.youtube.com/@GoogleAnalytics) — Google Analytics | DA-M07 |
| `PACK-PRODUCT_ANALYTICS-VIDEO-03` | video | [Microsoft Research experimentation talks](https://www.youtube.com/@MicrosoftResearch) — Microsoft Research | DA-M05, DA-M07, DA-M08 |
| `PACK-EXCEL_BI-DOCUMENT-01` | document | [Excel documentation](https://support.microsoft.com/en-us/excel) — Microsoft Support | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-DOCUMENT-03` | document | [Power BI guidance](https://learn.microsoft.com/en-us/power-bi/guidance/) — Microsoft Learn | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-WEBSITE-01` | website | [Excel learning templates](https://create.microsoft.com/en-us/excel-templates) — Microsoft | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-WEBSITE-02` | website | [DAX Guide](https://dax.guide/) — SQLBI | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-VIDEO-01` | video | [Microsoft Power BI video library](https://www.youtube.com/@MicrosoftPowerBI) — Microsoft Power BI | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-VIDEO-02` | video | [Guy in a Cube](https://www.youtube.com/@GuyInACube) — Microsoft-affiliated educators | DA-M02, DA-M06 |
| `PACK-EXCEL_BI-VIDEO-03` | video | [Excel video training](https://support.microsoft.com/en-us/office/excel-video-training-9bc05390-e94c-46af-a5b3-d7c22f6990bb) — Microsoft Support | DA-M02, DA-M06 |
| `PACK-STATS_EXPERIMENT-DOCUMENT-01` | document | [NIST/SEMATECH Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — NIST | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-DOCUMENT-03` | document | [Microsoft experimentation publications](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/publications/) — Microsoft Research | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-WEBSITE-01` | website | [Seeing Theory](https://seeing-theory.brown.edu/) — Brown University | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-WEBSITE-02` | website | [OpenIntro resources](https://www.openintro.org/) — OpenIntro | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-WEBSITE-03` | website | [Evan Miller A/B testing tools](https://www.evanmiller.org/ab-testing/) — Evan Miller | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-VIDEO-01` | video | [StatQuest](https://www.youtube.com/@statquest) — StatQuest | DA-M05, DA-M08 |
| `PACK-STATS_EXPERIMENT-VIDEO-02` | video | [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability) — Khan Academy | DA-M05, DA-M08 |
| `PACK-PYTHON_ENGINEERING-DOCUMENT-02` | document | [Python Packaging User Guide](https://packaging.python.org/) — Python Packaging Authority | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-DOCUMENT-03` | document | [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) — Python Software Foundation | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-WEBSITE-01` | website | [Python Developer's Guide](https://devguide.python.org/) — Python core developers | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-WEBSITE-02` | website | [Real Python](https://realpython.com/) — Real Python | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-WEBSITE-03` | website | [PyPI](https://pypi.org/) — Python Packaging Authority | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-VIDEO-01` | video | [PyCon US video library](https://www.youtube.com/@PyConUS) — Python Software Foundation | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-VIDEO-02` | video | [PyData video library](https://www.youtube.com/@PyDataTV) — PyData | DA-M09, DE-M01, DE-M02 |
| `PACK-PYTHON_ENGINEERING-VIDEO-03` | video | [Python official video library](https://www.youtube.com/@Python) — Python Software Foundation | DA-M09, DE-M01, DE-M02 |
| `PACK-ALGORITHMS_ARCH-DOCUMENT-01` | document | [Nand2Tetris project specifications](https://www.nand2tetris.org/course) — Nand2Tetris | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-DOCUMENT-02` | document | [Intel 64 and IA-32 optimization manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) — Intel | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-DOCUMENT-03` | document | [GCC vectorization documentation](https://gcc.gnu.org/projects/tree-ssa/vectorization.html) — GNU Project | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-WEBSITE-01` | website | [Algorithms, 4th edition site](https://algs4.cs.princeton.edu/home/) — Princeton | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-WEBSITE-02` | website | [VisuAlgo](https://visualgo.net/en) — National University of Singapore | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-WEBSITE-03` | website | [Nand2Tetris](https://www.nand2tetris.org/) — Nand2Tetris | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-VIDEO-01` | video | [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/video_galleries/lecture-videos/) — MIT OpenCourseWare | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-VIDEO-02` | video | [Nand2Tetris lectures](https://www.nand2tetris.org/course) — Nand2Tetris | DE-M03, DE-M04 |
| `PACK-ALGORITHMS_ARCH-VIDEO-03` | video | [Princeton Algorithms lectures](https://www.coursera.org/learn/algorithms-part1) — Princeton / Coursera | DE-M03, DE-M04 |
| `PACK-OS_NETWORK-DOCUMENT-01` | document | [Linux man-pages](https://www.kernel.org/doc/man-pages/) — Linux man-pages project | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-DOCUMENT-02` | document | [RFC 9293: TCP](https://www.rfc-editor.org/rfc/rfc9293.html) — IETF | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-WEBSITE-01` | website | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) — University of Wisconsin–Madison | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-WEBSITE-02` | website | [Linux Kernel documentation](https://docs.kernel.org/) — Linux kernel project | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-WEBSITE-03` | website | [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — Cloudflare | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-VIDEO-01` | video | [MIT 6.S081 Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2021/schedule.html) — MIT | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-VIDEO-02` | video | [Stanford CS144 Computer Networking](https://www.youtube.com/@stanfordonline) — Stanford | DE-M05, DE-M06 |
| `PACK-OS_NETWORK-VIDEO-03` | video | [Linux Plumbers Conference](https://www.youtube.com/@LinuxfoundationOrg) — Linux Foundation | DE-M05, DE-M06 |
| `PACK-SOFTWARE_API-WEBSITE-01` | website | [Martin Fowler](https://martinfowler.com/) — Martin Fowler | DE-M07, DE-M08 |
| `PACK-SOFTWARE_API-WEBSITE-02` | website | [Google Testing Blog](https://testing.googleblog.com/) — Google | DE-M07, DE-M08 |
| `PACK-SOFTWARE_API-WEBSITE-03` | website | [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) — Mozilla | DE-M07, DE-M08 |
| `PACK-SOFTWARE_API-VIDEO-01` | video | [Google for Developers](https://www.youtube.com/@GoogleDevelopers) — Google | DE-M07, DE-M08 |
| `PACK-SOFTWARE_API-VIDEO-02` | video | [InfoQ architecture talks](https://www.youtube.com/@infoq) — InfoQ | DE-M07, DE-M08 |
| `PACK-SOFTWARE_API-VIDEO-03` | video | [OWASP video library](https://www.youtube.com/@OWASPGLOBAL) — OWASP | DE-M07, DE-M08 |
| `PACK-DATABASE_MODELING-DOCUMENT-03` | document | [SQL standard information](https://www.iso.org/standard/76583.html) — ISO | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-WEBSITE-01` | website | [Use The Index, Luke](https://use-the-index-luke.com/) — Markus Winand | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-WEBSITE-02` | website | [CMU Database Group](https://db.cs.cmu.edu/) — Carnegie Mellon University | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-WEBSITE-03` | website | [Kimball Group techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/) — Kimball Group | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-VIDEO-01` | video | [CMU 15-445 Database Systems](https://www.youtube.com/@CMUDatabaseGroup) — Carnegie Mellon University | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-VIDEO-02` | video | [PostgreSQL Conference video library](https://www.youtube.com/@PostgresConference) — PostgreSQL Conference | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-DATABASE_MODELING-VIDEO-03` | video | [dbt Labs video library](https://www.youtube.com/@dbt-labs) — dbt Labs | DA-M03, DA-M04, DE-M09, DE-M10, DE-M11, DE-M12, DE-M13 |
| `PACK-OLAP_FORMATS-DOCUMENT-01` | document | [Apache Parquet format](https://parquet.apache.org/docs/) — Apache Software Foundation | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-DOCUMENT-02` | document | [Apache Iceberg specification](https://iceberg.apache.org/spec/) — Apache Software Foundation | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-WEBSITE-01` | website | [DuckDB publications](https://duckdb.org/science/) — DuckDB Foundation | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-WEBSITE-02` | website | [ClickHouse Academy](https://learn.clickhouse.com/) — ClickHouse | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-WEBSITE-03` | website | [Apache Arrow](https://arrow.apache.org/) — Apache Software Foundation | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-VIDEO-01` | video | [DuckDB video library](https://www.youtube.com/@DuckDB) — DuckDB | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-VIDEO-02` | video | [ClickHouse video library](https://www.youtube.com/@ClickHouseDB) — ClickHouse | DE-M14, DE-M15 |
| `PACK-OLAP_FORMATS-VIDEO-03` | video | [Apache Arrow video library](https://www.youtube.com/@ApacheArrow) — Apache Arrow | DE-M14, DE-M15 |
| `PACK-PIPELINE_GOV-DOCUMENT-02` | document | [OpenLineage object model](https://openlineage.io/docs/spec/object-model/) — OpenLineage | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-DOCUMENT-03` | document | [W3C PROV](https://www.w3.org/TR/prov-overview/) — W3C | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-WEBSITE-01` | website | [Astronomer Academy](https://academy.astronomer.io/) — Astronomer | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-WEBSITE-02` | website | [Airbyte tutorials](https://docs.airbyte.com/using-airbyte/getting-started/) — Airbyte | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-WEBSITE-03` | website | [Great Expectations learning](https://docs.greatexpectations.io/docs/tutorials/) — Great Expectations | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-VIDEO-01` | video | [Apache Airflow video library](https://www.youtube.com/@ApacheAirflow) — Apache Airflow | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-VIDEO-02` | video | [Data Council video library](https://www.youtube.com/@DataCouncil) — Data Council | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-PIPELINE_GOV-VIDEO-03` | video | [OpenLineage video library](https://www.youtube.com/@OpenLineage) — OpenLineage | DE-M16, DE-M17, DE-M18, DE-M19 |
| `PACK-DISTRIBUTED_STREAM-WEBSITE-01` | website | [Distributed Systems course](https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/) — Martin Kleppmann / University of Cambridge | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-DISTRIBUTED_STREAM-WEBSITE-02` | website | [Confluent Developer](https://developer.confluent.io/) — Confluent | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-DISTRIBUTED_STREAM-WEBSITE-03` | website | [Databricks learning](https://www.databricks.com/learn) — Databricks | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-DISTRIBUTED_STREAM-VIDEO-01` | video | [Distributed Systems lectures](https://www.youtube.com/@kleppmann) — Martin Kleppmann | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-DISTRIBUTED_STREAM-VIDEO-02` | video | [Confluent video library](https://www.youtube.com/@Confluent) — Confluent | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-DISTRIBUTED_STREAM-VIDEO-03` | video | [Databricks video library](https://www.youtube.com/@Databricks) — Databricks | DE-M20, DE-M21, DE-M22, DE-M23 |
| `PACK-CLOUD_SRE-DOCUMENT-02` | document | [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otel/) — OpenTelemetry / CNCF | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-DOCUMENT-03` | document | [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — NIST | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-WEBSITE-01` | website | [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) — Google Cloud | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-WEBSITE-02` | website | [CNCF Landscape](https://landscape.cncf.io/) — CNCF | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-WEBSITE-03` | website | [Killercoda Kubernetes scenarios](https://killercoda.com/kubernetes) — Killercoda | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-VIDEO-01` | video | [Google Cloud Tech](https://www.youtube.com/@googlecloudtech) — Google Cloud | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-VIDEO-02` | video | [CNCF video library](https://www.youtube.com/@cncf) — CNCF | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-VIDEO-03` | video | [HashiCorp video library](https://www.youtube.com/@HashiCorp) — HashiCorp | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-AI_ENGINEERING-DOCUMENT-01` | document | [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) — NIST | DE-M28 |
| `PACK-AI_ENGINEERING-WEBSITE-01` | website | [Hugging Face Course](https://huggingface.co/learn/llm-course/chapter1/1) — Hugging Face | DE-M28 |
| `PACK-AI_ENGINEERING-WEBSITE-02` | website | [NIST Trustworthy AI resources](https://www.nist.gov/artificial-intelligence) — NIST | DE-M28 |
| `PACK-AI_ENGINEERING-WEBSITE-03` | website | [OpenAI Cookbook](https://cookbook.openai.com/) — OpenAI | DE-M28 |
| `PACK-AI_ENGINEERING-VIDEO-01` | video | [DeepLearning.AI video library](https://www.youtube.com/@Deeplearningai) — DeepLearning.AI | DE-M28 |
| `PACK-AI_ENGINEERING-VIDEO-02` | video | [Hugging Face video library](https://www.youtube.com/@HuggingFace) — Hugging Face | DE-M28 |
| `PACK-AI_ENGINEERING-VIDEO-03` | video | [NIST video library](https://www.youtube.com/@NIST) — NIST | DE-M28 |
| `PACK-LEADERSHIP-DOCUMENT-02` | document | [SFIA skills framework 9](https://sfia-online.org/en/sfia-9) — SFIA Foundation | DE-M29 |
| `PACK-LEADERSHIP-DOCUMENT-03` | document | [ACM Code of Ethics](https://www.acm.org/code-of-ethics) — ACM | DE-M29 |
| `PACK-LEADERSHIP-WEBSITE-01` | website | [StaffEng stories](https://staffeng.com/stories) — StaffEng | DE-M29 |
| `PACK-LEADERSHIP-WEBSITE-02` | website | [LeadDev resources](https://leaddev.com/) — LeadDev | DE-M29 |
| `PACK-LEADERSHIP-WEBSITE-03` | website | [Google re:Work](https://rework.withgoogle.com/) — Google | DE-M29 |
| `PACK-LEADERSHIP-VIDEO-01` | video | [LeadDev video library](https://www.youtube.com/@LeadDev) — LeadDev | DE-M29 |
| `PACK-LEADERSHIP-VIDEO-02` | video | [InfoQ leadership talks](https://www.youtube.com/@infoq) — InfoQ | DE-M29 |
| `PACK-LEADERSHIP-VIDEO-03` | video | [Google re:Work video library](https://www.youtube.com/@Google) — Google | DE-M29 |
| `SRC-GOOGLE-ENG` | document | [Google Engineering Practices Documentation](https://google.github.io/eng-practices/) — Google | DA-M10, DE-M01, DE-M07, DE-M29 |
| `SRC-EVENT-SYSTEMS` | book | [Designing Event-Driven Systems](https://forum.confluent.io/t/free-book-designing-event-driven-systems/72) — Ben Stopford / Confluent | DE-M21, DE-M22, DE-M27 |
| `PACK-CLOUD_SRE-BOOK-02` | book | [The Site Reliability Workbook](https://sre.google/workbook/table-of-contents/) — Google | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-CLOUD_SRE-BOOK-03` | book | [Building Secure and Reliable Systems](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html) — Google | DE-M24, DE-M25, DE-M26, DE-M27 |
| `PACK-LEADERSHIP-BOOK-01` | book | [Staff Engineer](https://staffeng.com/book) — Will Larson | DE-M29 |

## Không dùng ở vòng đọc sâu

- Mọi tệp mà `reference-inventory.json` ghi `provenance_status: review-required`.
- Bản DDIA có chuỗi `z-lib` trong tên tệp local: không dùng; thay bằng bản mua/mượn hợp pháp `SRC-DDIA`.
- Tài liệu tổng hợp trong `Computer Science/` vẫn là kho ứng viên cho tới khi xác minh tác giả, phiên bản và quyền sử dụng.

## Điều kiện mở Bước 4

Owner xác nhận đủ ba nhóm việc trên bằng từ khóa `done`. Nếu một sách chưa lấy được, ghi mã nguồn và phương án thay thế; không mặc nhiên coi là đã có.
