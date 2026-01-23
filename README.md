# Enterprise Finance Automation System
**A professional Python-driven pipeline for SQL data management and automated business reporting.**

### Project Overview
This project automates the lifecycle of financial data. It replaces manual spreadsheets with a Pythonic workflow that captures transactions, secures them in a SQL database, analyzes patterns with Pandas, and generates executive-level PDF reports.

### Technical Details & Logic
The system is built using a modular architecture in `tracker.py`:

* **Data Persistence (SQL):** Utilizes **SQLite3** to manage a relational database ("D:\Finance_SQL_Automation\Professional_Finance_Report.pdf"). It ensures that transaction history is structured and persistent.
* **Algorithmic Analysis:** Leverages **Pandas** to aggregate raw data from SQL queries, calculating category-wise spending totals for real-time insights.
* **Visual Intelligence:** Uses **Matplotlib** to generate dynamic pie charts (`spending_chart.png`), providing a visual breakdown of expenses.
* **Automated Documentation:** Integrates the **FPDF library** to translate database records and charts into a formatted, professional PDF Executive Report.
* **Robust Engineering:** Implemented using **Object-Oriented Programming (OOP)** and error handling to ensure code scalability and reliability.

### Tech Stack
* **Core:** Python 3.x, SQL (SQLite3)
* **Data Science:** Pandas, Matplotlib
* **Reporting:** FPDF

### 📊 Project Output
<img width="640" height="480" alt="analytics_chart" src="https://github.com/user-attachments/assets/134845de-7532-49d9-96da-2b02d6b41ae1" />
