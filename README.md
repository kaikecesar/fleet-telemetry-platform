# 🚛 Fleet Telemetry Platform

> End-to-end data engineering platform for real-time fleet telemetry ingestion, processing, and analytics on AWS.

[![AWS](https://img.shields.io/badge/AWS-Serverless-orange)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-purple)](https://www.terraform.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 About

This project simulates a real-world **fleet telemetry platform** — the kind of system used to monitor hundreds to thousands of commercial vehicles in real time. It demonstrates data engineering patterns for high-volume time-series data: streaming ingestion, transformation, warehousing, and analytics.

**Why this project?**
Fleet telemetry is a perfect case study for modern data engineering:
- High-frequency time-series data (1 reading/second per vehicle)
- Multi-source ingestion (GPS, engine, temperature, fuel)
- Real-time analytics + historical reporting needs
- Scale challenges (thousands of active devices)
- Strict data quality and observability requirements

Built end-to-end as a portfolio piece to demonstrate production-grade engineering on AWS.

## 🎯 Technical Goals

- [ ] Ingest 10M+ telemetry records per day via Kinesis
- [ ] Sub-second query latency for real-time dashboards (up to last 24h)
- [ ] Historical queries over 90 days with <2s response time
- [ ] 99.5% pipeline availability (SLA tracking)
- [ ] 100% infrastructure as code (Terraform)
- [ ] CI/CD with automated testing and deployment

## 🏗️ Architecture

```
┌─────────────────┐      ┌──────────────┐      ┌──────────────┐
│  Simulated      │─────▶│   Kinesis    │─────▶│   Lambda     │
│  Fleet Devices  │      │  Data Stream │      │  (Ingestor)  │
└─────────────────┘      └──────────────┘      └──────┬───────┘
                                                      │
                                                      ▼
                         ┌──────────────┐      ┌──────────────┐
                         │   Redshift   │◀─────│     S3       │
                         │  (Warehouse) │      │ (Data Lake)  │
                         └──────┬───────┘      └──────┬───────┘
                                │                     │
                                ▼                     ▼
                         ┌──────────────┐      ┌──────────────┐
                         │     dbt      │      │  Glue + EMR  │
                         │ (Transform)  │      │  (Processing)│
                         └──────┬───────┘      └──────────────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   Airflow    │
                         │(Orchestration)│
                         └──────────────┘
```

## 🧰 Tech Stack

**Language:** Python 3.12
**Cloud:** AWS (Kinesis, Lambda, S3, Glue, EMR, Redshift, Athena, IAM, CloudWatch)
**IaC:** Terraform 1.12+
**Orchestration:** Apache Airflow 2.8+
**Transformation:** dbt Core
**Processing:** PySpark, Pandas, Polars
**Streaming:** Apache Kafka (local dev with Docker), Kinesis (prod)
**Observability:** CloudWatch, OpenTelemetry
**Testing:** pytest, Great Expectations (data quality)
**CI/CD:** GitHub Actions

## 📂 Repository Structure

```
fleet-telemetry-platform/
├── README.md
├── docs/
│   ├── architecture.md           # Detailed architecture decisions
│   ├── decisions/                # ADRs (Architecture Decision Records)
│   ├── performance.md            # Benchmarks and optimization notes
│   └── runbooks/                 # Operational procedures
├── infrastructure/
│   └── terraform/                # All AWS infrastructure as code
│       ├── modules/              # Reusable Terraform modules
│       ├── environments/         # dev, staging, prod
│       └── main.tf
├── ingestion/
│   ├── simulator/                # Fake fleet data generator (Python)
│   ├── lambda/                   # Kinesis → S3 ingestor
│   └── kafka/                    # Local Kafka producers (dev)
├── processing/
│   ├── glue/                     # AWS Glue ETL jobs
│   ├── spark/                    # PySpark transformations
│   └── airflow/
│       └── dags/                 # Airflow DAGs
├── warehouse/
│   └── dbt/                      # dbt project
│       ├── models/
│       │   ├── staging/          # Bronze layer (raw → clean)
│       │   ├── intermediate/     # Silver layer (joined + enriched)
│       │   └── marts/            # Gold layer (business-ready)
│       └── tests/
├── tests/                        # Integration tests
├── .github/workflows/            # CI/CD pipelines
└── Makefile                      # Common commands
```

## 🗓️ Implementation Roadmap (24 weeks)

### Phase 1 — Foundation (Weeks 1-4)

- [ ] **Week 1:** Repository setup, README, architecture docs, first ADR
- [ ] **Week 2:** Data simulator in Python (generates realistic fleet telemetry)
- [ ] **Week 3:** Terraform foundation (S3 buckets, IAM roles, VPC)
- [ ] **Week 4:** First Lambda function ingesting simulated data to S3

**Deliverable:** Simulator running locally, data landing in S3, all via Terraform.

### Phase 2 — Streaming (Weeks 5-8)

- [ ] **Week 5:** Migrate from S3 batch to Kinesis Data Streams
- [ ] **Week 6:** Kinesis Firehose + S3 partitioning strategy (year/month/day/hour)
- [ ] **Week 7:** Local Kafka setup with Docker Compose (for dev)
- [ ] **Week 8:** Schema Registry + Avro serialization + schema evolution

**Deliverable:** Real-time streaming pipeline with proper partitioning and schemas.

### Phase 3 — Processing & Warehouse (Weeks 9-12)

- [ ] **Week 9:** First Airflow DAG orchestrating daily aggregations
- [ ] **Week 10:** Advanced DAGs — dynamic task mapping, sensors, retries
- [ ] **Week 11:** dbt models — bronze/silver/gold medallion architecture
- [ ] **Week 12:** Data quality tests (dbt tests + Great Expectations)

**Deliverable:** Full end-to-end pipeline with quality checks.

### Phase 4 — Scale & Optimize (Weeks 13-16)

- [ ] **Week 13:** PySpark jobs on EMR for heavy transformations
- [ ] **Week 14:** Query optimization on Redshift (distribution, sort keys)
- [ ] **Week 15:** Delta Lake implementation for ACID guarantees
- [ ] **Week 16:** Terraform modules — reusable patterns, remote state

**Deliverable:** Production-grade performance at 10M records/day.

### Phase 5 — Advanced (Weeks 17-20)

- [ ] **Week 17:** Condensation algorithm — smart downsampling for dashboards
  (Reduces 90 days of 1-sec data to 600 plot points using MAX/MIN/AVG windows)
- [ ] **Week 18:** Observability — custom CloudWatch dashboards + alerts
- [ ] **Week 19:** Cost optimization analysis + documentation
- [ ] **Week 20:** Security audit — IAM least privilege review

**Deliverable:** Platform optimized for performance, cost, and security.

### Phase 6 — Polish (Weeks 21-24)

- [ ] **Week 21:** End-to-end CI/CD pipeline with GitHub Actions
- [ ] **Week 22:** Comprehensive documentation rewrite in English
- [ ] **Week 23:** Performance benchmarks + public blog post
- [ ] **Week 24:** v1.0 release

**Deliverable:** Production-ready open-source project.

## 🎓 Key Engineering Concepts Demonstrated

- ✅ **Streaming architecture** with Kinesis + Kafka
- ✅ **Medallion architecture** (bronze/silver/gold layers)
- ✅ **Time-series optimization** — partitioning, compression, downsampling
- ✅ **Schema evolution** — Avro + Schema Registry
- ✅ **Orchestration patterns** — DAGs, dynamic tasks, backfills
- ✅ **IaC best practices** — modules, workspaces, remote state
- ✅ **Data quality** — dbt tests + Great Expectations
- ✅ **Observability** — metrics, traces, logs
- ✅ **Cost optimization** — lifecycle policies, spot instances, query tuning
- ✅ **Security** — IAM least privilege, encryption at rest/transit

## 📊 Data Sources (All Public)

To keep this project reproducible and compliant, all data comes from public sources:

- **NYC TLC Trip Records** — https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- **OpenStreetMap GPS traces** — https://www.openstreetmap.org/traces
- **Synthetic data** — generated by the `simulator/` module using realistic distributions

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/fleet-telemetry-platform.git
cd fleet-telemetry-platform

# Install dependencies
make install

# Start local development environment (Kafka, Postgres, Redis)
make dev-up

# Run the data simulator
make simulate

# Run tests
make test
```

See [docs/getting-started.md](docs/getting-started.md) for full setup.

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [ADR Index](docs/decisions/)
- [Performance Benchmarks](docs/performance.md)
- [Operational Runbooks](docs/runbooks/)

## 📈 Current Status

**Current phase:** Phase 1 — Foundation
**Last updated:** [UPDATE WEEKLY]

### Weekly Progress

| Week | Focus | Status |
|------|-------|--------|
| 1 | Repo setup + architecture docs | ⏳ In progress |
| 2 | Data simulator | ⬜ Not started |
| ... | ... | ... |

## 👤 Author

**Kaike Oliveira** — Software Engineer specializing in distributed systems and real-time IoT architectures.

- 💼 LinkedIn: [linkedin.com/in/kaikeoliveira](https://www.linkedin.com/in/kaikeoliveira)
- 🐙 GitHub: [@kaikecesar](https://github.com/kaikecesar)

## 📝 License

MIT — see [LICENSE](LICENSE) for details.

---

> This is a learning project built in public as part of my transition from Full Stack to Data Engineering. Feedback and contributions welcome.
