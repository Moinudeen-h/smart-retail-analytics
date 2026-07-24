# 🛒 Smart Retail Analytics AI Copilot

An end-to-end **AI-powered retail analytics platform** combining Data Engineering, Business Intelligence, and Large Language Models (LLMs).

The system ingests retail transaction data, builds a PostgreSQL data warehouse using a star schema, provides interactive Power BI dashboards, and enables users to ask business questions in natural language through an LLM-powered analytics assistant.

The AI assistant automatically converts natural language questions into SQL queries, executes them against the warehouse, and generates business insights.

---

## 🏗️ System Architecture

```text
Raw Retail Data
       │
       ▼
Python ETL Pipeline
       │
       ▼
PostgreSQL Data Warehouse (Star Schema)
       │
       ├─────────────────────────┐
       ▼                         ▼
Power BI Dashboard     AI Analytics Copilot
                                 │
                                 ▼
                     Natural Language Query
                                 │
                                 ▼
                             Text-to-SQL
                                 │
                                 ▼
                        SQL Execution Engine
                                 │
                                 ▼
                    Business Insight Generation

```

---

## 🚀 Key Features

### Data Engineering Pipeline

* Automated data ingestion using Python
* Data cleaning and validation
* Dimensional modeling using Star Schema
* PostgreSQL data warehouse implementation
* Fact and dimension table management

### Business Intelligence

* Interactive Power BI dashboard
* Sales performance analysis
* Customer analytics
* Product performance tracking
* Regional revenue insights

### AI Analytics Copilot

* Natural language business queries
* LLM-powered Text-to-SQL generation
* Automatic SQL execution
* AI-generated executive summaries
* Business recommendations from database insights

> **Example Interaction:**
> * **User:** What are the top 5 best-selling products by revenue?
> * **AI Summary:** Based on the data, the top 5 best-selling products by revenue are Laptop (LKR 345,000), Smartphone (LKR 277,000), Smart Watch (LKR 165,000), Tablet (LKR 63,000), and Headphones (LKR 49,000).
> * **AI Recommendation:** Allocate more marketing resources to promote high-margin items like Laptops to maximize overall profitability.
> 

---

## 🛠️ Technology Stack

* **Data Engineering:** Python, PostgreSQL, SQLAlchemy, Pandas
* **Business Intelligence:** Microsoft Power BI
* **Artificial Intelligence:** Large Language Models (LLMs), Groq API, Text-to-SQL, Prompt Engineering
* **Application Layer:** Streamlit
* **Development Tools:** Git, GitHub, VS Code

---

## 📂 Project Structure

```text
smart-retail-analytics/
│
├── data/
│
├── dashboard/
│   └── Smart_Retail_Analytics_Dashboard.pbix
│
├── src/
│   │
│   ├── ai/
│   │   ├── llm_client.py
│   │   ├── sql_generator.py
│   │   ├── sql_executor.py
│   │   ├── insight_generator.py
│   │   └── retail_assistant.py
│   │
│   ├── database/
│   ├── transformation/
│   ├── validation/
│   │
│   └── app/
│       └── ai_dashboard.py
│
└── README.md

```

---

## 💡 Example AI Questions

The AI assistant can seamlessly handle queries such as:

* *Which city generated the highest sales revenue?*
* *Which products generate the most revenue?*
* *Who are the highest spending customers?*
* *What are the main sales trends by quarter?*

---

## 🎯 Project Objective

This project demonstrates the integration of modern **Data Engineering and Generative AI technologies** to build an enterprise-style analytics platform capable of transforming raw business data into actionable intelligence.

```