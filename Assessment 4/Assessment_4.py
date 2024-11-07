import tkinter as tk
from tkinter import messagebox, ttk
import pyodbc
from datetime import datetime

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Company Database App")
        
        # Database connection settings
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:/Users/2024002133/Documents/Company.accdb;'
        )
        
        # Create main buttons
        self.create_widgets()

    def create_widgets(self):
        # Create buttons with some padding and width
        btn_all_records = tk.Button(self.root, text="Print All Records", command=self.print_all_records, width=25, pady=10)
        btn_all_records.pack(pady=5)
        
        btn_positive_growth = tk.Button(self.root, text="Print Positive Growth", command=self.print_positive_growth, width=25, pady=10)
        btn_positive_growth.pack(pady=5)
        
        btn_query_by_date = tk.Button(self.root, text="Query Record by Date", command=self.query_record_by_date, width=25, pady=10)
        btn_query_by_date.pack(pady=5)
        
        btn_count_between_dates = tk.Button(self.root, text="Count Companies Between Dates", command=self.count_companies_between_dates, width=25, pady=10)
        btn_count_between_dates.pack(pady=5)

    def print_all_records(self):
        try:
            # Create a new window for displaying records
            records_window = tk.Toplevel(self.root)
            records_window.title("All Company Records")
            records_window.geometry("800x400")

            # Create a treeview widget
            tree = ttk.Treeview(records_window)
            tree["columns"] = ("company_name", "industry", "year_revenue", "revenue_growth", "number_of_employees", "headquarter", "company_found_date")
            
            # Format columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("company_name", anchor=tk.W, width=120)
            tree.column("industry", anchor=tk.W, width=100)
            tree.column("year_revenue", anchor=tk.E, width=100)
            tree.column("revenue_growth", anchor=tk.E, width=100)
            tree.column("number_of_employees", anchor=tk.E, width=120)
            tree.column("headquarter", anchor=tk.W, width=100)
            tree.column("company_found_date", anchor=tk.W, width=120)

            # Create headings
            tree.heading("company_name", text="Company Name")
            tree.heading("industry", text="Industry")
            tree.heading("year_revenue", text="Revenue (B)")
            tree.heading("revenue_growth", text="Growth (%)")
            tree.heading("number_of_employees", text="Employees")
            tree.heading("headquarter", text="Headquarter")
            tree.heading("company_found_date", text="Found Date")

            # Add scrollbar
            scrollbar = ttk.Scrollbar(records_window, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            # Pack the treeview and scrollbar
            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Connect to database and fetch records
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Company_Data")
                records = cursor.fetchall()

                # Insert records into treeview
                for record in records:
                    tree.insert("", "end", values=record)

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch records: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def print_positive_growth(self):
        pass

    def query_record_by_date(self):
        pass

    def count_companies_between_dates(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
