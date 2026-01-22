import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF
import os

class FinanceIntelligenceSystem:
    def __init__(self, db_name="finance_expert.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.setup_db()
        print(f" System Initialized: Connected to {self.db_name}")

    def setup_db(self):
        query = '''CREATE TABLE IF NOT EXISTS expenses 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    category TEXT, amount REAL, date TEXT, notes TEXT)'''
        self.conn.execute(query)
        self.conn.commit()

    def add_transaction(self, category, amount, notes="N/A"):
        try:
            date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO expenses (category, amount, date, notes) VALUES (?, ?, ?, ?)"
            self.conn.execute(query, (category, float(amount), date_now, notes))
            self.conn.commit()
            print(f"Saved Successfully: {category} - ${amount}")
        except ValueError:
            print(" Error: Amount must be a number!")

    def generate_visuals(self):
        df = pd.read_sql_query("SELECT category, SUM(amount) as total FROM expenses GROUP BY category", self.conn)
        if df.empty:
            return
        plt.figure(figsize=(8, 6))
        plt.pie(df['total'], labels=df['category'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title("Expense Distribution by Category")
        plt.savefig("spending_chart.png")
        print(" Chart Exported: 'spending_chart.png'")

    def export_pdf_report(self):
        df = pd.read_sql_query("SELECT * FROM expenses", self.conn)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(200, 15, txt="Financial Intelligence Report", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')
        pdf.ln(10)

        pdf.set_fill_color(200, 220, 255)
        pdf.cell(30, 10, "ID", 1, 0, 'C', True)
        pdf.cell(50, 10, "Category", 1, 0, 'C', True)
        pdf.cell(40, 10, "Amount", 1, 0, 'C', True)
        pdf.cell(70, 10, "Date", 1, 1, 'C', True)

        for _, row in df.iterrows():
            pdf.cell(30, 10, str(row['id']), 1)
            pdf.cell(50, 10, str(row['category']), 1)
            pdf.cell(40, 10, f"${row['amount']:.2f}", 1)
            pdf.cell(70, 10, str(row['date']), 1, 1)

        if os.path.exists("spending_chart.png"):
            pdf.ln(10)
            pdf.image("spending_chart.png", x=50, w=110)

        pdf.output("Professional_Finance_Report.pdf")
        print(" PDF Ready: 'Professional_Finance_Report.pdf'")

# --- MAIN EXECUTION BLOCK (FIXED INDENTATION) ---
if __name__ == "__main__":
    system = FinanceIntelligenceSystem()

    print("\n--- Add New Entry ---")
    category = input("Enter Category (e.g., Food, Salary): ")
    amount = input("Enter Amount: ")

    # Adding User Data
    system.add_transaction(category, amount, notes)

    # Update Analytics & Report
    system.generate_visuals()
    system.export_pdf_report()