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
        # Create frame for centering buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, padx=20, pady=20)

        # Create buttons with specific styling
        btn_all_records = tk.Button(button_frame, text="Print All Records", command=self.print_all_records, width=25)
        btn_all_records.pack(pady=5)
        
        btn_positive_growth = tk.Button(button_frame, text="Print Positive Growth", command=self.print_positive_growth, width=25)
        btn_positive_growth.pack(pady=5)
        
        btn_query_by_date = tk.Button(button_frame, text="Query Record by Date", command=self.query_record_by_date, width=25)
        btn_query_by_date.pack(pady=5)
        
        btn_count_between_dates = tk.Button(button_frame, text="Count Companies Between Dates", command=self.count_companies_between_dates, width=25)
        btn_count_between_dates.pack(pady=5)

    def print_all_records(self):
        try:
            # Create a new window for displaying records
            records_window = tk.Toplevel(self.root)
            records_window.title("All Company Records")
            records_window.geometry("800x300")

            # Create a frame for the header
            header_frame = tk.Frame(records_window)
            header_frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(header_frame, text="All Company Records", font=('Arial', 10, 'bold')).pack()

            # Create text widget for displaying records
            text_widget = tk.Text(records_window, wrap=tk.NONE, height=15)
            
            # Add horizontal scrollbar
            h_scrollbar = tk.Scrollbar(records_window, orient=tk.HORIZONTAL, command=text_widget.xview)
            text_widget.configure(xscrollcommand=h_scrollbar.set)
            
            # Add vertical scrollbar
            v_scrollbar = tk.Scrollbar(records_window, orient=tk.VERTICAL, command=text_widget.yview)
            text_widget.configure(yscrollcommand=v_scrollbar.set)

            # Pack the widgets
            text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Connect to database and fetch records
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Company_Data")
                records = cursor.fetchall()

                # Create headers
                headers = ["Company Name", "Industry", "Revenue (B)", "Growth (%)", "Employees", "Headquarter", "Found Date"]
                header_format = "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}\n"
                record_format = "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}\n"

                # Insert headers
                text_widget.insert(tk.END, header_format.format(*headers))
                text_widget.insert(tk.END, "-" * 110 + "\n")

                # Insert records
                for record in records:
                    formatted_record = [
                        str(record[0]),  # Company Name
                        str(record[1]),  # Industry
                        str(record[2]),  # Revenue
                        str(record[3]),  # Growth
                        str(record[4]),  # Employees
                        str(record[5]),  # Headquarter
                        str(record[6])   # Found Date
                    ]
                    text_widget.insert(tk.END, record_format.format(*formatted_record))

                # Make text widget read-only
                text_widget.configure(state='disabled')

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch records: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def print_positive_growth(self):
        try:
            # Create a new window for displaying records
            growth_window = tk.Toplevel(self.root)
            growth_window.title("Companies with Positive Growth")
            growth_window.geometry("800x300")

            # Create a frame for the header
            header_frame = tk.Frame(growth_window)
            header_frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(header_frame, text="Companies with Positive Growth", font=('Arial', 10, 'bold')).pack()

            # Create text widget for displaying records
            text_widget = tk.Text(growth_window, wrap=tk.NONE, height=15)
            
            # Add horizontal scrollbar
            h_scrollbar = tk.Scrollbar(growth_window, orient=tk.HORIZONTAL, command=text_widget.xview)
            text_widget.configure(xscrollcommand=h_scrollbar.set)
            
            # Add vertical scrollbar
            v_scrollbar = tk.Scrollbar(growth_window, orient=tk.VERTICAL, command=text_widget.yview)
            text_widget.configure(yscrollcommand=v_scrollbar.set)

            # Pack the widgets
            text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Connect to database and fetch records with positive growth
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Company_Data WHERE revenue_growth > 0")
                records = cursor.fetchall()

                # Create headers
                headers = ["Company Name", "Industry", "Revenue (B)", "Growth (%)", "Employees", "Headquarter", "Found Date"]
                header_format = "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}\n"
                record_format = "{:<20} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}\n"

                # Insert headers
                text_widget.insert(tk.END, header_format.format(*headers))
                text_widget.insert(tk.END, "-" * 110 + "\n")

                # Insert records
                for record in records:
                    formatted_record = [
                        str(record[0]),  # Company Name
                        str(record[1]),  # Industry
                        str(record[2]),  # Revenue
                        str(record[3]),  # Growth
                        str(record[4]),  # Employees
                        str(record[5]),  # Headquarter
                        str(record[6])   # Found Date
                    ]
                    text_widget.insert(tk.END, record_format.format(*formatted_record))

                # Make text widget read-only
                text_widget.configure(state='disabled')

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch records: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def query_record_by_date(self):
        pass

    def count_companies_between_dates(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
