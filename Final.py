import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

class SistemAngsuranRumah:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Angsuran Rumah")
        self.root.geometry("800x600")

        self.data_file = "angsuran_data.json"
        self.load_data()
        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.main_frame, text="Nama Pembeli:").grid(row=0, column=0, sticky=tk.W)
        self.nama_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.nama_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.main_frame, text="Harga Rumah:").grid(row=1, column=0, sticky=tk.W)
        self.harga_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.harga_var).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.main_frame, text="Uang Muka:").grid(row=2, column=0, sticky=tk.W)
        self.uang_muka_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.uang_muka_var).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.main_frame, text="Jangka Waktu (tahun):").grid(row=3, column=0, sticky=tk.W)
        self.jangka_waktu_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.jangka_waktu_var).grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(self.main_frame, text="Bunga (%):").grid(row=4, column=0, sticky=tk.W)
        self.bunga_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.bunga_var).grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(self.main_frame, text="Hitung Angsuran Anda", command=self.hitung_angsuran).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Simpan Data Anda", command=self.simpan_data).grid(row=6, column=0, columnspan=2, pady=5)
        
        self.create_treeview()
        self.update_treeview()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        else:
            self.data = []
    
    def create_treeview(self):
        columns = ('nama', 'harga', 'uang_muka', 'jangka_waktu', 'bunga', 'angsuran', 'tanggal')
        self.tree = ttk.Treeview(self.main_frame, columns=columns, show='headings')
        
        self.tree.heading('nama', text='Nama')
        self.tree.heading('harga', text='Harga Rumah')
        self.tree.heading('uang_muka', text='Uang Muka')
        self.tree.heading('jangka_waktu', text='Jangka Waktu')
        self.tree.heading('bunga', text='Bunga')
        self.tree.heading('angsuran', text='Angsuran/bulan')
        self.tree.heading('tanggal', text='Tanggal')
   
        for col in columns:
            self.tree.column(col, width=100)
        
        self.tree.grid(row=7, column=0, columnspan=2, pady=10)
        
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=2, sticky='ns')
    
    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for item in self.data:
            self.tree.insert('', tk.END, values=(
                item['nama'],
                f"Rp {float(item['harga']):,.0f}",
                f"Rp {float(item['uang_muka']):,.0f}",
                f"{item['jangka_waktu']} tahun",
                f"{item['bunga']}%",
                f"Rp {float(item['angsuran']):,.0f}",
                item['tanggal']
            ))
    
    def hitung_angsuran(self):
        try:
            harga = float(self.harga_var.get())
            uang_muka = float(self.uang_muka_var.get())
            jangka_waktu = float(self.jangka_waktu_var.get())
            bunga = float(self.bunga_var.get())
            
            pinjaman = harga - uang_muka
            
            bunga_tahunan = pinjaman * (bunga / 100)
       
            total_pinjaman = pinjaman + (bunga_tahunan * jangka_waktu)
            
            angsuran_bulanan = total_pinjaman / (jangka_waktu * 12)
            
            messagebox.showinfo("Hasil Perhitungan", 
                              f"Angsuran per bulan: Rp {angsuran_bulanan:,.2f}")
            
            return angsuran_bulanan
            
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan angka yang valid")
            return None
    
    def simpan_data(self):
        angsuran = self.hitung_angsuran()
        if angsuran:
            data_baru = {
                'nama': self.nama_var.get(),
                'harga': self.harga_var.get(),
                'uang_muka': self.uang_muka_var.get(),
                'jangka_waktu': self.jangka_waktu_var.get(),
                'bunga': self.bunga_var.get(),
                'angsuran': str(angsuran),
                'tanggal': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.data.append(data_baru)
            
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
            
            self.update_treeview()
            messagebox.showinfo("Sukses", "Data berhasil disimpan!")
        
            self.nama_var.set("")
            self.harga_var.set("")
            self.uang_muka_var.set("")
            self.jangka_waktu_var.set("")
            self.bunga_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemAngsuranRumah(root)
    root.mainloop()