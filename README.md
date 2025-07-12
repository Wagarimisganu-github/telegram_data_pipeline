
# 🏥 Telegram Medical Analytics Pipeline
This project delivers an end-to-end data pipeline for processing Telegram data into an analytical API.

**End-to-End Data Product: Scraping → ETL (dbt) → AI Enrichment (YOLOv8) → Analytics API (FastAPI) → Orchestration (Dagster)**

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI/CD](https://github.com/yourusername/telegram-med-analytics-pipeline/actions/workflows/test.yml/badge.svg)](https://github.com/yourusername/telegram-med-analytics-pipeline/actions)

<img src="docs/screenshots/pipeline_architecture.png" width="600" alt="System Architecture">

A production-ready data pipeline analyzing Ethiopian medical Telegram channels for pharmaceutical intelligence, price trends, and counterfeit detection.

## 🚀 Key Features

- **Telethon-powered scraping** of 10+ medical Telegram channels
- **Modern ELT pipeline** with dbt (star schema optimized for analytics)
- **AI-powered image recognition** using YOLOv8 (pills, syringes detection)
- **Analytical API** with FastAPI (top products, price trends, visual content stats)
- **Dagster-orchestrated** with error handling & daily schedules
- **Infra-as-Code** via Docker & Terraform

## 📂 Repository Structure

```bash
.
├── pipelines/          # Core data workflows
│   ├── extraction/     # Telegram scrapers
│   ├── transformation/ # dbt models
│   └── enrichment/     # YOLOv8 detection
├── services/           # API & orchestration
├── infra/              # Docker/Terraform configs
├── lib/                # Shared utilities
└── tests/              # Unit/integration/e2e
```
## 🛠️ Quick Start
### Prerequisites
* Python 3.11+

* Docker & Docker Compose

* Telegram API credentials

### Installation
```powershell
git clone https://github.com/yourusername/telegram-med-analytics-pipeline.git
cd telegram-med-analytics-pipeline

# Setup environment
cp .env.example .env
docker-compose up -d

# Initialize database
make migrate
```
### Running the Pipeline
```powershell
# Full pipeline run
dagster job execute -f pipelines/orchestration/jobs.py -n telegram_pipeline

# Start API
uvicorn services.api.main:app --reload
```
## 📊 Sample Analytics
```powershell
GET /api/analytics/top-products?limit=5
{
  "results": [
    {"product": "Paracetamol", "mentions": 142},
    {"product": "Amoxicillin", "mentions": 98}
  ]
}
```
<img src="docs/screenshots/api_demo.gif" width="500" alt="API Demo">

## 🤝 Contributing
1. Fork the project 
2. Create your feature branch (git checkout -b feat/ mazing-feature)

3. Commit changes (git commit -m 'Add amazing feature')

4. Push to branch (git push origin feat/amazing-feature)

5. Open a Pull Request
## ✉️ Contact
Name: Shegaw Adugna  
Email: shegamihret@gmail.com  
GitHub: https://github.com/Shegaw-21hub/telegram_data_pipeline