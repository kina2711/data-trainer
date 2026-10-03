"""Curated source packs for academic source-plan v2.

Entries are selection metadata only. A locator here names the relevant region; page-level
locators remain pending until the source is acquired and read.
"""

from __future__ import annotations


def r(title, authority, url, locator, access="online-official"):
    return {"title": title, "authority": authority, "url": url,
            "locator": locator, "access": access}


PACKS = {
"DA_FOUNDATIONS": {
 "book": [
  r("Data Science for Business", "O'Reilly Media", "https://www.oreilly.com/library/view/data-science-for/9781449374273/", "Problem framing; data-analytic thinking", "purchase-or-library"),
  r("The Truthful Art", "New Riders", "https://www.pearson.com/en-us/subject-catalog/p/truthful-art-the-data-charts-and-maps-for-communication/P200000009761", "Evidence, uncertainty and communication", "purchase-or-library"),
  r("Storytelling with Data", "Wiley", "https://www.wiley.com/en-us/Storytelling+with+Data%3A+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253", "Context, focus, narrative and delivery", "purchase-or-library")],
 "document": [
  r("Data Analyst career path", "Microsoft Learn", "https://learn.microsoft.com/en-us/training/career-paths/data-analyst", "Role tasks and learning paths"),
  r("Technical Writing Courses", "Google for Developers", "https://developers.google.com/tech-writing", "Technical Writing One and Two"),
  r("Google Engineering Practices", "Google", "https://google.github.io/eng-practices/", "Review, change descriptions and communication")],
 "website": [
  r("Google Data Analytics Certificate", "Google / Coursera", "https://www.coursera.org/professional-certificates/google-data-analytics", "Ask–prepare–process–analyze–share–act"),
  r("Data-to-Viz", "Yan Holtz", "https://www.data-to-viz.com/", "Chart selection decision tree"),
  r("Storytelling with Data resources", "Storytelling with Data", "https://www.storytellingwithdata.com/resources", "Exercises and examples")],
 "video": [
  r("Google Career Certificates video library", "Google", "https://www.youtube.com/@GoogleCareerCertificates", "Data Analytics series"),
  r("Storytelling with Data video library", "Storytelling with Data", "https://www.youtube.com/@storytellingwithdata", "Lessons and chart makeovers"),
  r("Google Developers technical writing videos", "Google for Developers", "https://developers.google.com/tech-writing/videos", "Technical writing video lessons")],
},
"PRODUCT_ANALYTICS": {
 "book": [
  r("Lean Analytics", "O'Reilly Media", "https://www.oreilly.com/library/view/lean-analytics/9781449335687/", "Metrics, business models and stages", "purchase-or-library"),
  r("Product Analytics", "O'Reilly Media", "https://www.oreilly.com/library/view/product-analytics/9781492026433/", "Instrumentation, funnels, cohorts and retention", "purchase-or-library"),
  r("Trustworthy Online Controlled Experiments", "Cambridge University Press", "https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59", "Metrics and experimentation pitfalls", "purchase-or-library")],
 "document": [
  r("Google Analytics measurement documentation", "Google", "https://developers.google.com/analytics", "Events, dimensions and metrics"),
  r("Amplitude Analytics documentation", "Amplitude", "https://www.amplitude.com/docs/analytics", "Funnels, retention, cohorts and journeys"),
  r("Microsoft experimentation platform papers", "Microsoft Research", "https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/publications/", "Experiment design and platform evidence")],
 "website": [
  r("Amplitude Academy", "Amplitude", "https://academy.amplitude.com/", "Product analytics learning paths"),
  r("Mixpanel learning resources", "Mixpanel", "https://mixpanel.com/content/guide-to-product-analytics/", "Product measurement patterns"),
  r("Microsoft Research experimentation group", "Microsoft Research", "https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/", "Controlled experiment research")],
 "video": [
  r("Amplitude video library", "Amplitude", "https://www.youtube.com/@Amplitude", "Product analytics tutorials"),
  r("Google Analytics video library", "Google Analytics", "https://www.youtube.com/@GoogleAnalytics", "Measurement and reporting series"),
  r("Microsoft Research experimentation talks", "Microsoft Research", "https://www.youtube.com/@MicrosoftResearch", "Online controlled experiments talks")],
},
"EXCEL_BI": {
 "book": [
  r("M Is for (Data) Monkey", "Apress", "https://link.springer.com/book/10.1007/978-1-4842-6383-9", "Power Query and repeatable transformation", "purchase-or-library"),
  r("The Definitive Guide to DAX", "Microsoft Press", "https://www.microsoftpressstore.com/store/definitive-guide-to-dax-business-intelligence-for-9780134865867", "DAX evaluation and modeling", "purchase-or-library"),
  r("The Big Book of Dashboards", "Wiley", "https://www.wiley.com/en-us/The+Big+Book+of+Dashboards%3A+Visualizing+Your+Data+Using+Real+World+Business+Scenarios-p-9781119282716", "Dashboard patterns and scenarios", "purchase-or-library")],
 "document": [
  r("Excel documentation", "Microsoft Support", "https://support.microsoft.com/en-us/excel", "Tables, formulas, PivotTables and charts"),
  r("Power Query documentation", "Microsoft Learn", "https://learn.microsoft.com/en-us/power-query/", "M, transformations and query folding"),
  r("Power BI guidance", "Microsoft Learn", "https://learn.microsoft.com/en-us/power-bi/guidance/", "Modeling, report design, performance and security")],
 "website": [
  r("Excel learning templates", "Microsoft", "https://create.microsoft.com/en-us/excel-templates", "Practice workbooks"),
  r("DAX Guide", "SQLBI", "https://dax.guide/", "DAX reference and compatibility"),
  r("Power BI learning path directory", "Microsoft Learn", "https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-learning-path-directory", "Scenario-based learning paths")],
 "video": [
  r("Microsoft Power BI video library", "Microsoft Power BI", "https://www.youtube.com/@MicrosoftPowerBI", "Modeling, DAX and report design"),
  r("Guy in a Cube", "Microsoft-affiliated educators", "https://www.youtube.com/@GuyInACube", "Power BI operations and performance"),
  r("Excel video training", "Microsoft Support", "https://support.microsoft.com/en-us/office/excel-video-training-9bc05390-e94c-46af-a5b3-d7c22f6990bb", "Excel foundations, functions and analysis")],
},
"STATS_EXPERIMENT": {
 "book": [
  r("OpenIntro Statistics", "OpenIntro", "https://www.openintro.org/book/os/", "Probability, inference and regression", "download-open"),
  r("Practical Statistics for Data Scientists", "O'Reilly Media", "https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/", "Applied inference and experimentation", "purchase-or-library"),
  r("Trustworthy Online Controlled Experiments", "Cambridge University Press", "https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59", "Experiment design, metrics and pitfalls", "purchase-or-library")],
 "document": [
  r("NIST/SEMATECH Statistics Handbook", "NIST", "https://www.itl.nist.gov/div898/handbook/", "EDA, estimation, testing and process modeling"),
  r("ASA statement on p-values", "American Statistical Association", "https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf", "Principles for interpreting statistical significance", "download-open"),
  r("Microsoft experimentation publications", "Microsoft Research", "https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/publications/", "Online experiment methods and failure modes")],
 "website": [
  r("Seeing Theory", "Brown University", "https://seeing-theory.brown.edu/", "Interactive probability and inference"),
  r("OpenIntro resources", "OpenIntro", "https://www.openintro.org/", "Datasets, labs and books"),
  r("Evan Miller A/B testing tools", "Evan Miller", "https://www.evanmiller.org/ab-testing/", "Power and test calculators")],
 "video": [
  r("StatQuest", "StatQuest", "https://www.youtube.com/@statquest", "Statistics Fundamentals playlist"),
  r("Khan Academy Statistics", "Khan Academy", "https://www.khanacademy.org/math/statistics-probability", "Probability and statistics video units"),
  r("Microsoft Research experimentation talks", "Microsoft Research", "https://www.youtube.com/@MicrosoftResearch", "Experimentation platform talks")],
},
"PYTHON_ENGINEERING": {
 "book": [
  r("Fluent Python, Second Edition", "O'Reilly Media", "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/", "Data model, functions, typing, concurrency", "purchase-or-library"),
  r("Effective Python, Third Edition", "Addison-Wesley", "https://www.pearson.com/en-us/subject-catalog/p/effective-python-125-specific-ways-to-write-better-python/P200000011759", "Idioms, robustness and maintainability", "purchase-or-library"),
  r("Python Concurrency with asyncio", "Manning", "https://www.manning.com/books/python-concurrency-with-asyncio", "asyncio, task groups and I/O", "purchase-or-library")],
 "document": [
  r("Python 3 documentation", "Python Software Foundation", "https://docs.python.org/3/", "Language, library and tutorial"),
  r("Python Packaging User Guide", "Python Packaging Authority", "https://packaging.python.org/", "Projects, builds, dependencies and distribution"),
  r("Python asyncio tasks", "Python Software Foundation", "https://docs.python.org/3/library/asyncio-task.html", "TaskGroup, cancellation and timeouts")],
 "website": [
  r("Python Developer's Guide", "Python core developers", "https://devguide.python.org/", "Workflow, testing and contribution"),
  r("Real Python", "Real Python", "https://realpython.com/", "Applied Python tutorials"),
  r("PyPI", "Python Packaging Authority", "https://pypi.org/", "Package discovery and release metadata")],
 "video": [
  r("PyCon US video library", "Python Software Foundation", "https://www.youtube.com/@PyConUS", "Python language and engineering talks"),
  r("PyData video library", "PyData", "https://www.youtube.com/@PyDataTV", "Python data tooling talks"),
  r("Python official video library", "Python Software Foundation", "https://www.youtube.com/@Python", "Conference and language talks")],
},
"ALGORITHMS_ARCH": {
 "book": [
  r("Algorithms, Fourth Edition", "Addison-Wesley", "https://algs4.cs.princeton.edu/home/", "Data structures, sorting, searching and graphs", "purchase-or-library"),
  r("Open Data Structures", "Pat Morin", "https://opendatastructures.org/", "Lists, queues, hashes, trees and graphs", "download-open"),
  r("Computer Organization and Design", "Morgan Kaufmann", "https://www.elsevier.com/books/computer-organization-and-design-mips-edition/patterson/978-0-12-407726-3", "ISA, memory hierarchy and parallelism", "purchase-or-library")],
 "document": [
  r("Nand2Tetris project specifications", "Nand2Tetris", "https://www.nand2tetris.org/course", "Projects 1–6 and lecture slides"),
  r("Intel 64 and IA-32 optimization manual", "Intel", "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html", "Optimization and SIMD manuals"),
  r("GCC vectorization documentation", "GNU Project", "https://gcc.gnu.org/projects/tree-ssa/vectorization.html", "Auto-vectorization capabilities and diagnostics")],
 "website": [
  r("Algorithms, 4th edition site", "Princeton", "https://algs4.cs.princeton.edu/home/", "Code, exercises and visualizations"),
  r("VisuAlgo", "National University of Singapore", "https://visualgo.net/en", "Interactive data structures and algorithms"),
  r("Nand2Tetris", "Nand2Tetris", "https://www.nand2tetris.org/", "Hardware/software construction path")],
 "video": [
  r("MIT 6.006 Introduction to Algorithms", "MIT OpenCourseWare", "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/video_galleries/lecture-videos/", "Lecture video series"),
  r("Nand2Tetris lectures", "Nand2Tetris", "https://www.nand2tetris.org/course", "Official hardware lecture videos"),
  r("Princeton Algorithms lectures", "Princeton / Coursera", "https://www.coursera.org/learn/algorithms-part1", "Modules 2–13 lecture videos")],
},
"OS_NETWORK": {
 "book": [
  r("Operating Systems: Three Easy Pieces", "Arpaci-Dusseau", "https://pages.cs.wisc.edu/~remzi/OSTEP/", "Virtualization, concurrency and persistence", "download-open"),
  r("The Linux Programming Interface", "No Starch Press", "https://nostarch.com/tlpi", "Processes, files, signals, IPC and sockets", "purchase-or-library"),
  r("Computer Networking: A Top-Down Approach", "Pearson", "https://gaia.cs.umass.edu/kurose_ross/index.php", "Application, transport and network layers", "purchase-or-library")],
 "document": [
  r("Linux man-pages", "Linux man-pages project", "https://www.kernel.org/doc/man-pages/", "System calls and interfaces"),
  r("RFC 9293: TCP", "IETF", "https://www.rfc-editor.org/rfc/rfc9293.html", "TCP specification"),
  r("RFC 9110: HTTP Semantics", "IETF", "https://www.rfc-editor.org/rfc/rfc9110.html", "HTTP semantics")],
 "website": [
  r("OSTEP", "University of Wisconsin–Madison", "https://pages.cs.wisc.edu/~remzi/OSTEP/", "Book chapters, homework and projects"),
  r("Linux Kernel documentation", "Linux kernel project", "https://docs.kernel.org/", "Kernel subsystems and APIs"),
  r("Cloudflare Learning Center", "Cloudflare", "https://www.cloudflare.com/learning/", "Networking and web protocol explainers")],
 "video": [
  r("MIT 6.S081 Operating System Engineering", "MIT", "https://pdos.csail.mit.edu/6.S081/2021/schedule.html", "Lecture recordings and labs"),
  r("Stanford CS144 Computer Networking", "Stanford", "https://www.youtube.com/@stanfordonline", "CS144 lecture series"),
  r("Linux Plumbers Conference", "Linux Foundation", "https://www.youtube.com/@LinuxfoundationOrg", "Kernel, I/O and networking talks")],
},
"SOFTWARE_API": {
 "book": [
  r("Software Engineering at Google", "Google / O'Reilly", "https://abseil.io/resources/swe-book", "Team-scale software practices", "online-open"),
  r("API Design Patterns", "Manning", "https://www.manning.com/books/api-design-patterns", "Resource-oriented APIs, consistency and evolution", "purchase-or-library"),
  r("The Pragmatic Programmer, 20th Anniversary Edition", "Addison-Wesley", "https://www.pearson.com/en-us/subject-catalog/p/the-pragmatic-programmer-your-journey-to-mastery-20th-anniversary-edition-2nd-edition/P200000000184", "Engineering workflow and maintainability", "purchase-or-library")],
 "document": [
  r("OpenAPI Specification", "OpenAPI Initiative", "https://spec.openapis.org/oas/latest.html", "API contracts and schemas"),
  r("OWASP API Security Top 10", "OWASP", "https://owasp.org/API-Security/editions/2023/en/0x11-t10/", "API risks and mitigations"),
  r("Google Engineering Practices", "Google", "https://google.github.io/eng-practices/", "Code review and change quality")],
 "website": [
  r("Martin Fowler", "Martin Fowler", "https://martinfowler.com/", "Architecture and delivery patterns"),
  r("Google Testing Blog", "Google", "https://testing.googleblog.com/", "Testing practices and case studies"),
  r("MDN HTTP", "Mozilla", "https://developer.mozilla.org/en-US/docs/Web/HTTP", "HTTP guides and reference")],
 "video": [
  r("Google for Developers", "Google", "https://www.youtube.com/@GoogleDevelopers", "Software engineering and API talks"),
  r("InfoQ architecture talks", "InfoQ", "https://www.youtube.com/@infoq", "Architecture and engineering talks"),
  r("OWASP video library", "OWASP", "https://www.youtube.com/@OWASPGLOBAL", "API and application security talks")],
},
"DATABASE_MODELING": {
 "book": [
  r("Database System Concepts", "McGraw Hill", "https://www.db-book.com/", "Relational model, transactions, storage and query processing", "purchase-or-library"),
  r("Database Internals", "O'Reilly Media", "https://www.oreilly.com/library/view/database-internals/9781492040330/", "Storage engines and distributed databases", "purchase-or-library"),
  r("The Data Warehouse Toolkit", "Wiley", "https://www.wiley.com/en-us/The+Data+Warehouse+Toolkit%3A+The+Definitive+Guide+to+Dimensional+Modeling%2C+3rd+Edition-p-9781118530801", "Dimensional modeling patterns", "purchase-or-library")],
 "document": [
  r("PostgreSQL 17 Documentation", "PostgreSQL Global Development Group", "https://www.postgresql.org/docs/17/", "SQL, indexes, concurrency, internals and administration"),
  r("dbt Developer Hub", "dbt Labs", "https://docs.getdbt.com/", "Models, tests, documentation and semantic layer"),
  r("SQL standard information", "ISO", "https://www.iso.org/standard/76583.html", "SQL language standard record")],
 "website": [
  r("Use The Index, Luke", "Markus Winand", "https://use-the-index-luke.com/", "SQL indexing and execution"),
  r("CMU Database Group", "Carnegie Mellon University", "https://db.cs.cmu.edu/", "Database systems research and courses"),
  r("Kimball Group techniques", "Kimball Group", "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/", "Dimensional modeling techniques")],
 "video": [
  r("CMU 15-445 Database Systems", "Carnegie Mellon University", "https://www.youtube.com/@CMUDatabaseGroup", "15-445 lecture series"),
  r("PostgreSQL Conference video library", "PostgreSQL Conference", "https://www.youtube.com/@PostgresConference", "Query, storage and operations talks"),
  r("dbt Labs video library", "dbt Labs", "https://www.youtube.com/@dbt-labs", "Analytics engineering and semantic layer talks")],
},
"OLAP_FORMATS": {
 "book": [
  r("Designing Data-Intensive Applications, Second Edition", "O'Reilly Media", "https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/", "Storage, encoding and derived data", "purchase-or-library"),
  r("Database Internals", "O'Reilly Media", "https://www.oreilly.com/library/view/database-internals/9781492040330/", "Storage layouts and database architecture", "purchase-or-library"),
  r("Fundamentals of Data Engineering", "O'Reilly Media", "https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/", "Storage and data engineering lifecycle", "purchase-or-library")],
 "document": [
  r("Apache Parquet format", "Apache Software Foundation", "https://parquet.apache.org/docs/", "File format, encoding and metadata"),
  r("Apache Iceberg specification", "Apache Software Foundation", "https://iceberg.apache.org/spec/", "Snapshots, manifests and evolution"),
  r("Delta Lake protocol", "Delta Lake project", "https://github.com/delta-io/delta/blob/master/PROTOCOL.md", "Transaction log and table features")],
 "website": [
  r("DuckDB publications", "DuckDB Foundation", "https://duckdb.org/science/", "OLAP engine research"),
  r("ClickHouse Academy", "ClickHouse", "https://learn.clickhouse.com/", "Columnar analytics learning paths"),
  r("Apache Arrow", "Apache Software Foundation", "https://arrow.apache.org/", "Columnar memory format ecosystem")],
 "video": [
  r("DuckDB video library", "DuckDB", "https://www.youtube.com/@DuckDB", "Engine internals and research talks"),
  r("ClickHouse video library", "ClickHouse", "https://www.youtube.com/@ClickHouseDB", "OLAP architecture and operations"),
  r("Apache Arrow video library", "Apache Arrow", "https://www.youtube.com/@ApacheArrow", "Columnar format and execution talks")],
},
"PIPELINE_GOV": {
 "book": [
  r("Fundamentals of Data Engineering", "O'Reilly Media", "https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/", "Lifecycle, ingestion, orchestration and governance", "purchase-or-library"),
  r("Data Pipelines Pocket Reference", "O'Reilly Media", "https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/", "Pipeline patterns and orchestration", "purchase-or-library"),
  r("Data Quality Fundamentals", "O'Reilly Media", "https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/", "Quality dimensions and operating practices", "purchase-or-library")],
 "document": [
  r("Apache Airflow core concepts", "Apache Software Foundation", "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/", "DAGs, tasks, scheduling and backfill"),
  r("OpenLineage object model", "OpenLineage", "https://openlineage.io/docs/spec/object-model/", "Jobs, runs, datasets and facets"),
  r("W3C PROV", "W3C", "https://www.w3.org/TR/prov-overview/", "Provenance model family")],
 "website": [
  r("Astronomer Academy", "Astronomer", "https://academy.astronomer.io/", "Airflow learning paths"),
  r("Airbyte tutorials", "Airbyte", "https://docs.airbyte.com/using-airbyte/getting-started/", "Replication and connector tutorials"),
  r("Great Expectations learning", "Great Expectations", "https://docs.greatexpectations.io/docs/tutorials/", "Data quality tutorials")],
 "video": [
  r("Apache Airflow video library", "Apache Airflow", "https://www.youtube.com/@ApacheAirflow", "Airflow Summit and tutorials"),
  r("Data Council video library", "Data Council", "https://www.youtube.com/@DataCouncil", "Data platform, quality and metadata talks"),
  r("OpenLineage video library", "OpenLineage", "https://www.youtube.com/@OpenLineage", "Lineage specification and integrations")],
},
"DISTRIBUTED_STREAM": {
 "book": [
  r("Designing Data-Intensive Applications, Second Edition", "O'Reilly Media", "https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/", "Distributed data, batch and stream processing", "purchase-or-library"),
  r("Kafka: The Definitive Guide, Second Edition", "O'Reilly Media", "https://www.oreilly.com/library/view/kafka-the-definitive/9781492043072/", "Kafka architecture and operations", "purchase-or-library"),
  r("Streaming Systems", "O'Reilly Media", "https://www.oreilly.com/library/view/streaming-systems/9781491983867/", "Time, state and correctness in streaming", "purchase-or-library")],
 "document": [
  r("Apache Kafka documentation", "Apache Software Foundation", "https://kafka.apache.org/documentation/", "Design, protocol and operations"),
  r("Debezium documentation", "Debezium", "https://debezium.io/documentation/reference/stable/", "CDC snapshots, offsets and delivery"),
  r("Apache Flink documentation", "Apache Software Foundation", "https://nightlies.apache.org/flink/flink-docs-stable/", "State, time, checkpoints and backpressure")],
 "website": [
  r("Distributed Systems course", "Martin Kleppmann / University of Cambridge", "https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/", "Distributed systems lectures and notes"),
  r("Confluent Developer", "Confluent", "https://developer.confluent.io/", "Kafka and stream processing courses"),
  r("Databricks learning", "Databricks", "https://www.databricks.com/learn", "Spark and data engineering learning")],
 "video": [
  r("Distributed Systems lectures", "Martin Kleppmann", "https://www.youtube.com/@kleppmann", "Distributed systems lecture series"),
  r("Confluent video library", "Confluent", "https://www.youtube.com/@Confluent", "Kafka and event streaming talks"),
  r("Databricks video library", "Databricks", "https://www.youtube.com/@Databricks", "Spark and lakehouse talks")],
},
"CLOUD_SRE": {
 "book": [
  r("Site Reliability Engineering", "Google", "https://sre.google/sre-book/table-of-contents/", "SLOs, monitoring, toil and incidents", "online-open"),
  r("The Site Reliability Workbook", "Google", "https://sre.google/workbook/table-of-contents/", "Applied SRE practices", "online-open"),
  r("Building Secure and Reliable Systems", "Google", "https://google.github.io/building-secure-and-reliable-systems/raw/toc.html", "Security and reliability engineering", "online-open")],
 "document": [
  r("Kubernetes documentation", "Kubernetes / CNCF", "https://kubernetes.io/docs/home/", "Workloads, networking, storage and security"),
  r("OpenTelemetry specification", "OpenTelemetry / CNCF", "https://opentelemetry.io/docs/specs/otel/", "Signals, SDKs, propagation and semantic conventions"),
  r("NIST Cybersecurity Framework 2.0", "NIST", "https://www.nist.gov/cyberframework", "Govern, identify, protect, detect, respond, recover")],
 "website": [
  r("Google Cloud Architecture Framework", "Google Cloud", "https://cloud.google.com/architecture/framework", "Cloud architecture pillars"),
  r("CNCF Landscape", "CNCF", "https://landscape.cncf.io/", "Cloud-native ecosystem map"),
  r("Killercoda Kubernetes scenarios", "Killercoda", "https://killercoda.com/kubernetes", "Interactive Kubernetes practice")],
 "video": [
  r("Google Cloud Tech", "Google Cloud", "https://www.youtube.com/@googlecloudtech", "Cloud architecture and SRE talks"),
  r("CNCF video library", "CNCF", "https://www.youtube.com/@cncf", "Kubernetes, observability and platform talks"),
  r("HashiCorp video library", "HashiCorp", "https://www.youtube.com/@HashiCorp", "Terraform and infrastructure automation")],
},
"AI_ENGINEERING": {
 "book": [
  r("AI Engineering", "O'Reilly Media", "https://www.oreilly.com/library/view/ai-engineering/9781098166298/", "Foundation models, evaluation and production systems", "purchase-or-library"),
  r("Designing Machine Learning Systems", "O'Reilly Media", "https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/", "ML system lifecycle and monitoring", "purchase-or-library"),
  r("Hands-On Large Language Models", "O'Reilly Media", "https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/", "LLM internals and applications", "purchase-or-library")],
 "document": [
  r("NIST AI RMF 1.0", "NIST", "https://www.nist.gov/itl/ai-risk-management-framework", "Govern, map, measure and manage"),
  r("OWASP Top 10 for LLM Applications", "OWASP", "https://genai.owasp.org/llm-top-10/", "LLM application risks"),
  r("OpenAI API documentation", "OpenAI", "https://developers.openai.com/api/docs", "Models, tools, evals and production practices")],
 "website": [
  r("Hugging Face Course", "Hugging Face", "https://huggingface.co/learn/llm-course/chapter1/1", "Transformers and LLM engineering"),
  r("NIST Trustworthy AI resources", "NIST", "https://www.nist.gov/artificial-intelligence", "Standards and risk resources"),
  r("OpenAI Cookbook", "OpenAI", "https://cookbook.openai.com/", "Implementation examples and eval patterns")],
 "video": [
  r("DeepLearning.AI video library", "DeepLearning.AI", "https://www.youtube.com/@Deeplearningai", "LLM engineering and evaluation"),
  r("Hugging Face video library", "Hugging Face", "https://www.youtube.com/@HuggingFace", "Transformers and open models"),
  r("NIST video library", "NIST", "https://www.youtube.com/@NIST", "AI risk management talks")],
},
"LEADERSHIP": {
 "book": [
  r("Staff Engineer", "Will Larson", "https://staffeng.com/book", "Staff archetypes, scope and influence", "online-open"),
  r("The Staff Engineer's Path", "O'Reilly Media", "https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/", "Technical leadership and operating at staff level", "purchase-or-library"),
  r("Accelerate", "IT Revolution", "https://itrevolution.com/product/accelerate/", "Delivery performance and organizational capabilities", "purchase-or-library")],
 "document": [
  r("Google Engineering Practices", "Google", "https://google.github.io/eng-practices/", "Review and engineering collaboration"),
  r("SFIA skills framework 9", "SFIA Foundation", "https://sfia-online.org/en/sfia-9", "Responsibility levels and skills"),
  r("ACM Code of Ethics", "ACM", "https://www.acm.org/code-of-ethics", "Professional and leadership obligations")],
 "website": [
  r("StaffEng stories", "StaffEng", "https://staffeng.com/stories", "Staff-plus practitioner interviews"),
  r("LeadDev resources", "LeadDev", "https://leaddev.com/", "Engineering leadership practices"),
  r("Google re:Work", "Google", "https://rework.withgoogle.com/", "Team and management research")],
 "video": [
  r("LeadDev video library", "LeadDev", "https://www.youtube.com/@LeadDev", "Engineering leadership talks"),
  r("InfoQ leadership talks", "InfoQ", "https://www.youtube.com/@infoq", "Staff-plus and architecture leadership"),
  r("Google re:Work video library", "Google", "https://www.youtube.com/@Google", "Team effectiveness and leadership talks")],
},
}


MODULE_PACK = {
 "DA-M01":"DA_FOUNDATIONS", "DA-M02":"EXCEL_BI", "DA-M03":"DATABASE_MODELING",
 "DA-M04":"DATABASE_MODELING", "DA-M05":"STATS_EXPERIMENT", "DA-M06":"EXCEL_BI",
 "DA-M07":"PRODUCT_ANALYTICS", "DA-M08":"STATS_EXPERIMENT", "DA-M09":"PYTHON_ENGINEERING",
 "DA-M10":"DA_FOUNDATIONS", "DA-M11":"DA_FOUNDATIONS",
 "DE-M01":"PYTHON_ENGINEERING", "DE-M02":"PYTHON_ENGINEERING", "DE-M03":"ALGORITHMS_ARCH",
 "DE-M04":"ALGORITHMS_ARCH", "DE-M05":"OS_NETWORK", "DE-M06":"OS_NETWORK",
 "DE-M07":"SOFTWARE_API", "DE-M08":"SOFTWARE_API", "DE-M09":"DATABASE_MODELING",
 "DE-M10":"DATABASE_MODELING", "DE-M11":"DATABASE_MODELING", "DE-M12":"DATABASE_MODELING",
 "DE-M13":"DATABASE_MODELING", "DE-M14":"OLAP_FORMATS", "DE-M15":"OLAP_FORMATS",
 "DE-M16":"PIPELINE_GOV", "DE-M17":"PIPELINE_GOV", "DE-M18":"PIPELINE_GOV",
 "DE-M19":"PIPELINE_GOV", "DE-M20":"DISTRIBUTED_STREAM", "DE-M21":"DISTRIBUTED_STREAM",
 "DE-M22":"DISTRIBUTED_STREAM", "DE-M23":"DISTRIBUTED_STREAM", "DE-M24":"CLOUD_SRE",
 "DE-M25":"CLOUD_SRE", "DE-M26":"CLOUD_SRE", "DE-M27":"CLOUD_SRE",
 "DE-M28":"AI_ENGINEERING", "DE-M29":"LEADERSHIP",
}


COURSES = {
 "C-DA-INTRO": r("Introducing Data Analytics and Analytical Thinking", "Google / Coursera", "https://www.coursera.org/learn/google-introducing-data-analytics-and-analytical-thinking", "Module 1 — Transform data into insights"),
 "C-EXCEL": r("Excel Skills for Business: Essentials", "Macquarie University / Coursera", "https://www.coursera.org/learn/excel-essentials", "Modules 1–7 — Excel core, formulas, data and charts"),
 "C-SQL": r("SQL for Data Science", "UC Davis / Coursera", "https://www.coursera.org/learn/sql-for-data-science", "Modules 1–4 — retrieval, filtering, joins and analysis"),
 "C-DW": r("Data Warehousing and Business Intelligence", "University of California Irvine / Coursera", "https://www.coursera.org/learn/data-warehousing-business-intelligence", "Modules 1–2 — warehouse architecture and multidimensional modeling"),
 "C-STATS": r("Statistics with Python", "University of Michigan / Coursera", "https://www.coursera.org/specializations/statistics-with-python", "Course 1 Modules 1–4; Course 2 Modules 1–4"),
 "C-PBI": r("Data Visualization Fundamentals", "Microsoft / Coursera", "https://www.coursera.org/learn/data-visualization-fundamentals", "Module 1 onward — visualization foundations with Power BI"),
 "C-PRODUCT": r("Ask Questions to Make Data-Driven Decisions", "Google / Coursera", "https://www.coursera.org/learn/ask-questions-make-decisions", "Modules 1–4 — questions, decisions and stakeholders"),
 "C-PYDATA": r("Python for Data Science, AI & Development", "IBM / Coursera", "https://www.coursera.org/learn/python-for-applied-data-science-ai", "Modules 1–5 — Python, structures, APIs and data"),
 "C-DA-CAP": r("Google Data Analytics Capstone", "Google / Coursera", "https://www.coursera.org/learn/google-data-analytics-capstone", "Modules 1–4 — case study and portfolio"),
 "C-PYOS": r("Using Python to Interact with the Operating System", "Google / Coursera", "https://www.coursera.org/learn/python-operating-system", "Modules 1–7 — OS, files, processes, testing and automation"),
 "C-ALGO": r("Algorithms, Part I", "Princeton University / Coursera", "https://www.coursera.org/learn/algorithms-part1", "Modules 2–13 — analysis, structures, sorting and searching"),
 "C-N2T": r("Build a Modern Computer from First Principles", "Hebrew University / Coursera", "https://www.coursera.org/learn/build-a-computer", "Modules 2 and 4–8 — logic, arithmetic, memory, machine language, architecture and assembler"),
 "C-NET": r("The Bits and Bytes of Computer Networking", "Google / Coursera", "https://www.coursera.org/learn/computer-networking", "Modules 1–6 — layers, networking, transport and services"),
 "C-SWARCH": r("Software Design and Architecture", "University of Alberta / Coursera", "https://www.coursera.org/specializations/software-design-architecture", "Courses 1–4 — design, patterns, architecture and capstone"),
 "C-BACKEND": r("Back-End Developer Capstone", "Meta / Coursera", "https://www.coursera.org/learn/back-end-developer-capstone", "Modules 1–4 — backend, database, API, auth and tests"),
 "C-DB": r("Database Management Essentials", "University of Colorado / Coursera", "https://www.coursera.org/learn/database-management", "Modules 4–12 — SQL, ERD, normalization and advanced queries"),
 "C-DE-INTRO": r("Introduction to Data Engineering", "IBM / Coursera", "https://www.coursera.org/learn/introduction-to-data-engineering", "Modules 1–4 — role, ecosystem, lifecycle and platform"),
 "C-ETL": r("ETL and Data Pipelines with Shell, Airflow and Kafka", "IBM / Coursera", "https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka", "Modules 1–5 — ETL, pipelines, Airflow and Kafka"),
 "C-SPARK": r("Introduction to Big Data with Spark and Hadoop", "IBM / Coursera", "https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop", "Modules 1–7 — distributed processing, Spark and Hadoop"),
 "C-CLOUD": r("Reliable Google Cloud Infrastructure: Design and Process", "Google Cloud / Coursera", "https://www.coursera.org/learn/cloud-infrastructure-design-process", "Modules 2–10 — services, architecture, reliability and security"),
 "C-K8S": r("Introduction to Containers w/ Docker, Kubernetes & OpenShift", "IBM / Coursera", "https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift", "Modules 1–5 — containers, Kubernetes and operations"),
 "C-GENAI": r("Generative AI Engineering and Fine-Tuning Transformers", "IBM / Coursera", "https://www.coursera.org/learn/generative-ai-engineering-and-fine-tuning-transformers", "Modules 1–2 — transformers, fine-tuning and PEFT"),
 "C-LEAD": r("Leading Teams: Developing as a Leader", "University of Illinois / Coursera", "https://www.coursera.org/learn/leading-teams-developing-as-a-leader", "Modules 1–4 — leadership, self, others and growth"),
}


MODULE_COURSE = {
 "DA-M01":"C-DA-INTRO", "DA-M02":"C-EXCEL", "DA-M03":"C-SQL", "DA-M04":"C-DW",
 "DA-M05":"C-STATS", "DA-M06":"C-PBI", "DA-M07":"C-PRODUCT", "DA-M08":"C-STATS",
 "DA-M09":"C-PYDATA", "DA-M10":"C-PRODUCT", "DA-M11":"C-DA-CAP",
 "DE-M01":"C-PYOS", "DE-M02":"C-PYOS", "DE-M03":"C-ALGO", "DE-M04":"C-N2T",
 "DE-M05":"C-PYOS", "DE-M06":"C-NET", "DE-M07":"C-SWARCH", "DE-M08":"C-BACKEND",
 "DE-M09":"C-DB", "DE-M10":"C-DB", "DE-M11":"C-DW", "DE-M12":"C-DW",
 "DE-M13":"C-DE-INTRO", "DE-M14":"C-SPARK", "DE-M15":"C-DE-INTRO",
 "DE-M16":"C-ETL", "DE-M17":"C-ETL", "DE-M18":"C-DE-INTRO", "DE-M19":"C-DE-INTRO",
 "DE-M20":"C-SPARK", "DE-M21":"C-ETL", "DE-M22":"C-ETL", "DE-M23":"C-SPARK",
 "DE-M24":"C-CLOUD", "DE-M25":"C-K8S", "DE-M26":"C-CLOUD", "DE-M27":"C-CLOUD",
 "DE-M28":"C-GENAI", "DE-M29":"C-LEAD",
}
