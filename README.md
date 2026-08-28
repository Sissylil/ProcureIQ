# ProcureIQ

**Procurement & Supplier Decision Intelligence Platform**  
**采购与供应商决策智能平台**

ProcureIQ is a bilingual procurement and supply-chain decision-support application built with Python and Streamlit. It is designed to help users evaluate suppliers, analyse procurement spend, monitor supply risk, plan inventory, forecast demand and test operational scenarios.

ProcureIQ 是一个使用 Python 与 Streamlit 开发的中英双语采购与供应链决策支持平台，用于供应商评估、采购支出分析、供应风险监控、库存规划、需求预测与情景分析。

---

## Project Motivation / 项目动机

The project is based on a simple procurement principle: **the lowest quotation is not always the best sourcing decision**.

A sourcing decision should consider multiple factors together, including:

- Unit cost / 单位成本
- Minimum order quantity (MOQ) / 最低订购量
- Lead time / 交期
- On-time delivery / 准时交付
- Quality performance / 质量表现
- Supplier risk / 供应商风险
- Price variance / 价格波动
- Demand and inventory requirements / 需求与库存需求

ProcureIQ converts these inputs into structured dashboards, supplier rankings and operational recommendations.

---

## Main Features / 主要功能

### 1. Overview / 总览
Provides a high-level view of procurement performance, including:

- Annual procurement spend
- Average supplier lead time
- On-time delivery rate
- Average supplier risk
- Supplier spend distribution
- Supplier overall scores

### 2. Supplier Scorecard / 供应商评分
Evaluates suppliers using five key dimensions:

- Cost
- Lead time
- Delivery
- Quality
- Risk

The platform generates an overall score and supplier grade.

### 3. Supplier Comparison / 供应商比较
Allows users to adjust decision weights for:

- Cost
- Lead time
- Delivery
- Quality
- Risk

The system then calculates a weighted supplier ranking and recommends the strongest sourcing alternative.

### 4. Spend Analysis / 采购支出分析
Analyses:

- Total procurement spend
- Spend by category
- Spend by supplier
- Supplier concentration
- Price variance

### 5. Risk Monitor / 风险监控
Creates an operational risk index using:

- Supplier risk score
- On-time delivery
- Quality
- Late orders
- Price variance

Suppliers are classified into low, medium or high-risk groups.

### 6. Inventory Planning / 库存规划
Supports operational inventory decisions through:

- Safety stock
- Reorder point
- Days of cover
- Target inventory
- Suggested replenishment quantity

The module uses supplier lead time together with user-defined demand and service-level assumptions.

### 7. Scenario Analysis / 情景分析
Allows users to simulate changes in:

- Demand
- Supplier lead time
- Service level

The system compares baseline and scenario results for:

- Safety stock
- Reorder point
- Target inventory
- Suggested order quantity

### 8. Demand Forecasting / 需求预测
Supports historical demand analysis using:

- Moving Average
- Exponential Smoothing

Users may upload their own demand-history CSV or use the built-in synthetic demonstration data.

### 9. Decision Assistant / 决策助手
Translates supplier metrics into simple business recommendations, highlighting:

- Supplier strengths
- Areas of concern
- Suggested sourcing action

### 10. CSV Templates & Export / 模板与结果导出
Users can:

- Download a procurement-data template
- Upload their own procurement dataset
- Download a demand-history template
- Upload historical demand
- Export supplier-comparison results
- Export inventory-planning results
- Export scenario-analysis results

---

## Data Structure / 数据结构

### Procurement Data Template / 采购数据模板

The following column names must remain unchanged:

| Column | Meaning |
|---|---|
| `PO_ID` | Purchase order identifier |
| `Supplier` | Supplier name |
| `Category` | Procurement category |
| `Unit_Cost` | Unit purchase cost |
| `MOQ` | Minimum order quantity |
| `Lead_Time_Days` | Supplier lead time in days |
| `On_Time_Delivery_Pct` | On-time delivery percentage |
| `Quality_Score` | Supplier quality score |
| `Risk_Score` | Supplier risk score |
| `Annual_Quantity` | Annual purchase quantity |
| `Price_Variance_Pct` | Price variance |
| `Late_Orders` | Number of late orders |

`Annual_Spend` is calculated automatically by ProcureIQ.

### Demand History Template / 需求历史模板

Required columns:

| Column | Meaning |
|---|---|
| `Date` | Demand period/date |
| `Demand` | Historical demand quantity |

---

## Default Demo Data / 默认演示数据

When no procurement file is uploaded, ProcureIQ uses:

`sample_procurement_data.csv`

This file contains **synthetic demonstration data only** and does not contain confidential company information.

用户没有上传采购 CSV 时，系统会读取 `sample_procurement_data.csv` 作为默认演示数据。该数据完全为模拟数据，不包含任何真实企业机密信息。

---

## Technology Stack / 技术栈

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

---

## Run Locally / 本地运行

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## Project Structure / 项目结构

```text
ProcureIQ/
├── app.py
├── sample_procurement_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Deployment / 部署

The application can be deployed using **Streamlit Community Cloud**.

Basic deployment flow:

1. Upload the project to a public GitHub repository.
2. Open Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the main application file.
5. Deploy.

---

## Portfolio Note / 项目说明

ProcureIQ is an independent portfolio project created for learning and demonstration purposes. The application focuses on the design of procurement and supply-chain decision logic rather than reproducing any confidential internal company system.

ProcureIQ 是一个独立开发的学习与作品集项目，重点在于采购与供应链决策逻辑的设计，不复制任何真实企业的内部系统或机密数据。

---

## Future Extensions / 可扩展方向

Possible future improvements include:

- Database persistence
- User authentication
- Advanced demand forecasting
- Supplier anomaly detection
- AI-assisted recommendation generation
- ERP/API integration
