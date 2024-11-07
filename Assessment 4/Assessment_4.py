import tkinter as tk
from tkinter import messagebox
import pyodbc

class app:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        
        self.conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\database.accdb;'
        )
        
        self.create_widgets
        
    def create_widgets(self):
        btn_all_records = tk.Button(self.root, text="Print All Records", 
                                  command=self.print_all_records,
                                  width=25, pady=10)
        btn_all_records.pack(pady=5)
        
        btn_positive_growth = tk.Button(self.root, text="Print Positive Growth",
                                      command=self.print_positive_growth,
                                      width=25, pady=10)
        btn_positive_growth.pack(pady=5)
        
        btn_query_by_date = tk.Button(self.root, text="Query Record by Date",
                                    command=self.query_record_by_date,
                                    width=25, pady=10)
        btn_query_by_date.pack(pady=5)
        
        btn_count_between_dates = tk.Button(self.root, text="Count Companies Between Dates",
                                          command=self.count_companies_between_dates,
                                          width=25, pady=10)
        btn_count_between_dates.pack(pady=5)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()