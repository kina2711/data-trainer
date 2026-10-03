---
source_id: src.web.dbt-semantic-models
source_type: web
title: Semantic models
publisher: dbt Labs
canonical_url: https://docs.getdbt.com/docs/build/semantic-models
captured: 2026-10-01
status: active-public-source
rights: public-web-documentation
authority: official-product-documentation
tags: [source/web, semantic-layer, metrics, entities, dimensions]
---

# dbt Semantic Models — hồ sơ nguồn

## Phạm vi sử dụng

Tài liệu chính thức được đọc lại ngày 2026-10-01. Phần dùng trong note là semantic graph, entities, dimensions, simple/ratio/derived/cumulative metrics, time spine, aggregation time dimension và dependency giữa metrics. Chi tiết cú pháp là version-sensitive; note dùng dbt/MetricFlow làm một ví dụ triển khai, không đồng nhất sản phẩm này với khái niệm semantic layer nói chung.

Tài liệu hiện hành cho dbt v1.12+ và đặc tả mới đã thay đổi đáng kể so với legacy spec. Ở authoring spec mới, simple metric mang aggregation/expression và `measure` không còn là node khai báo độc lập như legacy implementation. Giáo trình vẫn tách measure và metric ở mức khái niệm để phân tích aggregation contract; mọi ví dụ YAML phải gắn rõ version.

## Tài liệu liên quan đã đọc

- Staging project structure: https://docs.getdbt.com/best-practices/how-we-structure/2-staging
- Semantic structure: https://docs.getdbt.com/best-practices/how-we-build-our-metrics/semantic-layer-7-semantic-structure
- About MetricFlow: https://docs.getdbt.com/docs/build/about-metricflow
- Semantic models: https://docs.getdbt.com/docs/build/semantic-models
- Derived metrics: https://docs.getdbt.com/docs/build/derived
- Cumulative metrics and time spine: https://docs.getdbt.com/docs/build/cumulative
- Migrate to the latest YAML spec: https://docs.getdbt.com/docs/build/latest-metrics-spec
- MetricFlow concepts and join behavior: https://docs.getdbt.com/docs/build/about-metricflow
- MetricFlow commands, validation and generated SQL: https://docs.getdbt.com/docs/build/metricflow-commands
- dbt Semantic Layer overview and serving paths: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl?version=2
- Result and declarative caching: https://docs.getdbt.com/docs/use-dbt-semantic-layer/sl-cache
- Semantic Layer credentials, tokens and access boundary: https://docs.getdbt.com/docs/use-dbt-semantic-layer/setup-sl
- Semantic Layer APIs: https://docs.getdbt.com/docs/dbt-apis/sl-api-overview

Tài liệu commands hiện hành phân biệt môi trường dbt platform và self-hosted, đồng thời phân biệt cờ `--compile` với `--explain` tùy engine/version. Note chỉ mô tả workflow `parse → validate → query → inspect generated SQL/dataflow plan`; câu lệnh cụ thể phải đối chiếu đúng môi trường trước khi chạy.

Tài liệu caching hiện hành phân biệt result caching của data platform và declarative caching qua saved query/export. Trang này cũng nêu cached tables chưa áp security context ở query time; vì vậy note L179–L180 coi cache authorization isolation là điều kiện thiết kế bắt buộc, không suy rằng cache sản phẩm tự động an toàn. Tài liệu quản trị xác nhận service token được gắn với credential, policy ở data platform của credential được tôn trọng và credential nên có quyền tối thiểu.

## Note dẫn xuất

- [[Modelling for Handover - What the Consumer Needs]]
- [[The Layers That Must Be Distinguished]]
- [[From a Business Question to a Metric Contract]]
- [[The Semantic Graph - Entities, Dimensions, Measures and Metrics]]
- [[Metric Types - Simple, Ratio, Derived and Cumulative]]
- [[Additivity and Aggregation in the Semantic Layer]]
- [[Time Semantics - Grain, Offsets and Period Comparison]]
- [[Ambiguous Joins and the Chasm Trap]]
- [[Fanout - Proving a Metric Is Not Double Counted]]
- [[The Compatibility Matrix - Which Dimension Goes with Which Metric]]
- [[Semantic Models in MetricFlow]]
- [[Defining Metrics and Reading the Generated SQL]]
- [[Query Compilation Internals]]
- [[Testing a Semantic Layer - Definition and Static Tests]]
- [[Correctness Tests and Reconciliation Against Hand-Written SQL]]
- [[Serving, Caching and Performance]]
- [[Access Control at the Semantic Layer]]
- [[Architecture Alternatives - Headless, BI-Native or Curated Marts]]
- [[Metric Lifecycle - Propose, Certify, Version, Deprecate]]
- [[Capstone - A Governed Revenue Semantic Product]]
- [[Capstone - A Governed Customer Health Data Product]]
- [[Gate 5 - Defend a Metric Definition and Prove Self-Service]]
