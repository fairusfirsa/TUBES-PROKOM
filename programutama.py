import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkEntry
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from range11 import halaman_rumah

# Fungsi Halaman 1
def halaman1(main):
    global utama, gambar_next2, gambar_quit2

    for widget in main.winfo_children():
        widget.destroy()

    frame1 = tk.Frame(main, bg='black')
    frame1.pack(expand=True, ipadx=1920, ipady=1080)

    utama = ImageTk.PhotoImage(Image.open('1.png'))
    label = tk.Label(frame1, image=utama)
    label.pack(fill=tk.BOTH, expand=tk.YES)

    # Tombol Quit
    gambar_quit = Image.open('quit.png').resize((300, 60), Image.LANCZOS)
    gambar_quit2 = ImageTk.PhotoImage(gambar_quit)
    tombolquit = CTkButton(
        label, text="", image=gambar_quit2, cursor='hand2',
        border_spacing=0, command=main.quit, fg_color="transparent"
    )
    tombolquit.pack(padx=240, pady=170, anchor='s', side='left')

    # Tombol Next
    gambar_next = Image.open('next.png').resize((300, 60), Image.LANCZOS)
    gambar_next2 = ImageTk.PhotoImage(gambar_next)
    tombolnext = CTkButton(
        label, text="", image=gambar_next2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_login(main),
        fg_color="transparent"
    )
    tombolnext.pack(padx=180, pady=170, anchor='s', side='right')

# buat file csv
if not os.path.exists('abc.csv'):
    with open('abc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Email', 'Name', 'Password'])  
        
def toggle_password():
    if pw_user.cget("show") == "*":
        pw_user.config(show="")
        toggle_button.config(image=hide_img) 
    else:
        pw_user.config(show="*") 
        toggle_button.config(image=show_img)  
 
# halaman 2
def halaman_login(main):
    global bg_login, pw_user, toggle_button, show_img, hide_img, label_bg  
    
    for widget in main.winfo_children():
        widget.destroy()

    frame_login = tk.Frame(main)
    frame_login.pack(expand=True, fill=tk.BOTH)

    bg_login = ImageTk.PhotoImage(Image.open('3.png')) 
    label_bg = tk.Label(frame_login, image=bg_login)
    label_bg.place(relwidth=1, relheight=1)  

    # Entry untuk email
    email_user = tk.Entry(frame_login, width=30, font=("Helvetica", 20), relief="flat", bg="#ffffff")
    email_user.place(relx=0.5, rely=0.4, anchor="center")

    # Entry untuk password
    pw_user = tk.Entry(frame_login, show="*", width=30, font=("Helvetica", 20), relief="flat", bg="#ffffff")
    pw_user.place(relx=0.5, rely=0.5, anchor="center")
    
    show_img = Image.open('oeye.png')  
    hide_img = Image.open('heye.png')
    
    show_img = ImageTk.PhotoImage(show_img.resize((25, 25)))  
    hide_img = ImageTk.PhotoImage(hide_img.resize((25, 25))) 
    
    # Tombol Show/Hide Password
    toggle_button = tk.Button(
        frame_login, image=show_img, command=toggle_password, bg="#ffffff", relief="flat"
    )
    toggle_button.place(relx=0.62, rely=0.50, anchor="center")  # Tempatkan tombol di sebelah kanan entry password

    # Tombol Login
    login_button = tk.Button(
        frame_login, text="Login", command=lambda: signin(email_user, pw_user, main),
        font=("Helvetica", 14), bg="#57a689", fg="white", relief="flat"
    )
    login_button.place(relx=0.627, rely=0.57, anchor="center")

    # Tombol Sign Up
    signup_button = tk.Button(
        frame_login, text="Belum punya Akun? Daftar", command=lambda: halaman_signup(main),cursor='hand2',
        font=("Helvetica", 14), bg="#2a729c", fg="white", relief="flat"
    )
    signup_button.place(relx=0.43, rely=0.57, anchor="center")


def signin(email_user, pw_user, main):
    email = email_user.get()
    password = pw_user.get()

    if not email or not password:
        messagebox.showerror('Error', 'Mohon isi semua bidang!')
        return

    try:
        with open('abc.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader) 

            for row in reader:
                if row[1] == email:
                    if row[3] == password:
                        halaman3(main, email) 
                        return
                    else:
                        messagebox.showerror('Sign In Error', 'Password tidak valid!')
                        return
            messagebox.showerror('Sign In Error', 'Email tidak ditemukan!')
    except FileNotFoundError:
        messagebox.showerror('Error', 'File abc.csv tidak ditemukan!')
    except Exception as e:
        messagebox.showerror('Error', f'Terjadi kesalahan: {e}')


#halaman pendaftaran
def halaman_signup(main):
    global bg_signup, pw_user, toggle_button, show_img, hide_img, label_bg

    for widget in main.winfo_children():
        widget.destroy()

    frame_signup = tk.Frame(main)
    frame_signup.pack(expand=True, fill=tk.BOTH)

    bg_signup = ImageTk.PhotoImage(Image.open('4.png'))  
    label_bg = tk.Label(frame_signup, image=bg_signup)
    label_bg.place(relwidth=1, relheight=1)
    
    name_user = tk.Entry(frame_signup, width=30, font=("Helvetica", 20), relief="flat", bg="#ffffff")
    name_user.place(relx=0.5, rely=0.4, anchor="center")

    email_user = tk.Entry(frame_signup, width=30, font=("Helvetica", 20), relief="flat", bg="#ffffff")
    email_user.place(relx=0.5, rely=0.5, anchor="center")

    pw_user = tk.Entry(frame_signup, show="*", width=30, font=("Helvetica", 20), relief="flat", bg="#ffffff")
    pw_user.place(relx=0.5, rely=0.6, anchor="center")
    
    show_img = Image.open('oeye.png')  
    hide_img = Image.open('heye.png')
    
    show_img = ImageTk.PhotoImage(show_img.resize((25, 25)))  
    hide_img = ImageTk.PhotoImage(hide_img.resize((25, 25))) 
    
    toggle_button = tk.Button(
        frame_signup, image=show_img, command=toggle_password, bg="#ffffff", relief="flat"
    )
    toggle_button.place(relx=0.62, rely=0.6, anchor="center") 


    signup_button = tk.Button(
        frame_signup,
        text="Sign Up",
        command=lambda: signup(email_user, pw_user, name_user, main),
        font=("Helvetica", 14), bg="#57a689", fg="white", relief="flat"
    )
    signup_button.place(relx=0.62, rely=0.67, anchor="center")

    login_button = tk.Button(
        frame_signup,
        text="Back to Login",
        command=lambda: halaman_login(main),
        font=("Helvetica", 14), bg="#2a729c", fg="white", relief="flat"
    )
    login_button.place(relx=0.396, rely=0.67, anchor="center")
    
def signup(email_user, pw_user, name_user, main):
    email = email_user.get()
    password = pw_user.get()
    name = name_user.get()

    if not email or not password or not name:
        messagebox.showerror('Error', 'Mohon isi semua bidang!')
        return

    try:
        with open('abc.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)

            for row in reader:
                if row[1] == email:
                    messagebox.showerror('Error', 'Email sudah terdaftar!')
                    return

        with open('abc.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([None, email, name, password])
            messagebox.showinfo('Success', 'Pendaftaran berhasil! Silakan login.')

        halaman_login(main)
    except Exception as e:
        messagebox.showerror('Error', f'Terjadi kesalahan: {e}')


# Halaman 3
def halaman3(main, user_email):
    global utama, hitung2, rekomen2, frame3

    for widget in main.winfo_children():
        widget.destroy()

    frame3 = tk.Frame(main, bg='black')
    frame3.pack(expand=True, ipadx=1920, ipady=1080)

    utama = ImageTk.PhotoImage(Image.open('2.png'))
    label = tk.Label(frame3, image=utama)
    label.pack(fill=tk.BOTH, expand=tk.YES)

    rekomen = Image.open('rekomen.png').resize((300, 60), Image.LANCZOS)
    rekomen2 = ImageTk.PhotoImage(rekomen)
    tombolrekomen = CTkButton(
        label, text="", image=rekomen2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_rekomen(main),
        fg_color="transparent"
    )
    tombolrekomen.pack(padx=240, pady=300, anchor='s', side='left')

    # Tombol Hitung
    hitung = Image.open('hitung.png').resize((300, 60), Image.LANCZOS)
    hitung2 = ImageTk.PhotoImage(hitung)
    tombolhitung = CTkButton(
        label, text="", image=hitung2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_hitung(main, user_email),
        fg_color="transparent"
    )
    tombolhitung.pack(padx=180, pady=300, anchor='s', side='right')


def kirim_email_peserta(email_penerima, nama_file_pdf):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_pengirim = "cicilamann@gmail.com"  
    password_pengirim = "ukkg flhj harg uvov"  

    try:
        pesan = MIMEMultipart()
        pesan["From"] = email_pengirim
        pesan["To"] = email_penerima
        pesan["Subject"] = "Hasil Perhitungan Angsuran Rumah"

        body = "Berikut adalah hasil perhitungan angsuran rumah Anda. PDF terlampir."
        pesan.attach(MIMEText(body, "plain"))

        with open(nama_file_pdf, "rb") as lampiran:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(lampiran.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(nama_file_pdf)}")
            pesan.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_pengirim, password_pengirim)
        server.send_message(pesan)
        server.quit()

        print("Email berhasil dikirim.")
        messagebox.showinfo("Sukses", f"PDF berhasil dikirim ke {email_penerima}")
    except Exception as e:
        print(f"Error saat mengirim email: {e}")  
        messagebox.showerror("Error", f"Gagal mengirim email: {e}")


# simpan pdf
def simpan_pdf(harga, dp, waktu, bunga, angsuran, email):
    try:
        filename = "Hasil_Angsuran.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        logo_path = "logo.png" 
        if os.path.exists(logo_path):
            c.drawImage(logo_path, 50, height - 100, width=50, height=50, mask='auto')

        c.setFont("Helvetica-Bold", 16)
        c.drawString(170, height - 70, "PT CicilAman")
        c.setFont("Helvetica", 10)
        c.drawString(170, height - 85, "Jalan Kebahagiaan No. 123, Jakarta, Indonesia")
        c.drawString(170, height - 100, "Telepon: +62 333 222 111 | Email: cicilamann@gmail.com")

        c.setStrokeColor(colors.black)
        c.line(50, height - 110, width - 50, height - 110)

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, height - 140, "Laporan Hasil Perhitungan Angsuran Rumah")

        data = [
            ["Deskripsi", "Nilai"],
            ["Harga Rumah", f"Rp {harga:,.2f}"],
            ["DP (Down Payment)", f"Rp {dp:,.2f}"],
            ["Jangka Waktu", f"{waktu} tahun"],
            ["Bunga Tahunan", f"{bunga}%"],
            ["Angsuran Bulanan", f"Rp {angsuran:,.2f}"]
        ]

        table = Table(data, colWidths=[200, 250], hAlign='LEFT')
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        table.setStyle(style)
        table.wrapOn(c, width, height)
        table.drawOn(c, 50, height - 300)

        c.setFont("Helvetica-Oblique", 10)
        c.drawString(50, 50, "Dokumen ini dihasilkan oleh sistem PT CicilAman.")
        c.drawString(50, 35, "Harap tidak membagikan dokumen ini tanpa izin.")
        
        c.save()
        messagebox.showinfo("Sukses", f"Hasil perhitungan berhasil disimpan ke {filename}!")

        kirim_email_peserta(email, filename)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan file PDF: {e}")



# Halaman hitung
def halaman_hitung(main, user_email):
    for widget in main.winfo_children():
        widget.destroy()

    frame_hitung = tk.Frame(main)
    frame_hitung.pack(expand=True, fill=tk.BOTH)

    bg_hitung_img = Image.open('5.png')  
    bg_hitung = ImageTk.PhotoImage(bg_hitung_img)
    label_bg = tk.Label(frame_hitung, image=bg_hitung)
    label_bg.image = bg_hitung  
    label_bg.place(relwidth=1, relheight=1)

    harga_var = tk.StringVar()
    dp_var = tk.StringVar()
    waktu_var = tk.StringVar()
    bunga_var = tk.StringVar()
    hasil_var = tk.StringVar()

    tk.Entry(frame_hitung, textvariable=harga_var, font=("Helvetica", 20), width=20, relief="flat", bg=None).place(relx=0.5, rely=0.3, anchor="w")
    tk.Entry(frame_hitung, textvariable=dp_var, font=("Helvetica", 20), width=20, relief="flat", bg=None).place(relx=0.5, rely=0.37, anchor="w")
    tk.Entry(frame_hitung, textvariable=waktu_var, font=("Helvetica", 20), width=20, relief="flat", bg=None).place(relx=0.5, rely=0.44, anchor="w")
    tk.Entry(frame_hitung, textvariable=bunga_var, font=("Helvetica", 20), width=20, relief="flat", bg=None).place(relx=0.5, rely=0.51, anchor="w")

    def hitung_angsuran():
        try:
            harga = float(harga_var.get())
            dp = float(dp_var.get())
            waktu = int(waktu_var.get())
            bunga = float(bunga_var.get())
            pinjaman = harga - dp
            bunga_tahunan = pinjaman * (bunga / 100)
            total_pinjaman = pinjaman + (bunga_tahunan * waktu)
            angsuran_bulanan = total_pinjaman / (waktu * 12)
            hasil_var.set(f"Rp {angsuran_bulanan:,.2f}")

            simpan_pdf(harga, dp, waktu, bunga, angsuran_bulanan, user_email)
        except ValueError:
            messagebox.showerror("Error", "Masukkan semua nilai dengan benar!")

    tk.Button(
        frame_hitung, text="Hitung Angsuran Anda", font=("Helvetica", 14), bg="#57a689", fg="white",
        command=hitung_angsuran, relief="flat"
    ).place(relx=0.5, rely=0.58, anchor="w")

    tk.Label(frame_hitung, textvariable=hasil_var, font=("Helvetica", 20), fg="black", bg="white").place(relx=0.5, rely=0.65, anchor="w")

    tk.Button(
        frame_hitung, text="Kirim Hasil ke Email", font=("Helvetica", 14), bg="#2a729c", fg="white",
        command=lambda: kirim_email_peserta(user_email, "Hasil_Angsuran.pdf"), relief="flat"
    ).place(relx=0.5, rely=0.72, anchor="w")
    
    # Tombol Quit
    gambar_quit = Image.open('quit.png').resize((300, 60), Image.LANCZOS)
    gambar_quit2 = ImageTk.PhotoImage(gambar_quit)
    tombolquit = CTkButton(
        frame_hitung, text="", image=gambar_quit2, cursor='hand2',
        border_spacing=0, command=main.quit, fg_color="transparent"
    )
    tombolquit.pack(padx=150, pady=100, anchor='s', side='right')
    
    # halaman rekomen
    gambar_next = Image.open('rekomen.png').resize((300, 60), Image.LANCZOS)
    gambar_next2 = ImageTk.PhotoImage(gambar_next)
    tombolnext = CTkButton(
        frame_hitung, text="", image=gambar_next2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_rekomen(main),
        fg_color="transparent"
    )
    tombolnext.pack(padx=150, pady=100, anchor='s', side='left')
    
    
#halaman rekomen
def halaman_rekomen(main):
    global gambar_rek, frame_rek

    for widget in main.winfo_children():
        widget.destroy()

    frame_rekomen = tk.Frame(main, bg='black')
    frame_rekomen.pack(expand=True, fill=tk.BOTH)

    gambar_rek = ImageTk.PhotoImage(Image.open('8.png').resize((1920, 1080), Image.LANCZOS))
    label_rek = tk.Label(frame_rekomen, image=gambar_rek)
    label_rek.pack(fill=tk.BOTH, expand=tk.YES)
    
    tombol_100_250 = CTkButton(
        label_rek, text="100 - 250 Juta",
        command=lambda:halaman_rumah(main),
        font=("Helvetica", 30),
        fg_color="#57a689",  
        text_color="white",
        hover_color="#333333",
        width=500
    )
    tombol_100_250.place(relx=0.5, rely=0.3, anchor="center")

    tombol_250_500 = CTkButton(
        label_rek, text="250 - 500 Juta",
        command=lambda: (250, 500),
        font=("Helvetica", 30),
        fg_color="#57a689",
        text_color="white",
        hover_color="#333333",
        width=500
    )
    tombol_250_500.place(relx=0.5, rely=0.4, anchor="center")

    tombol_500_750 = CTkButton(
        label_rek, text="500 - 750 Juta",
        command=lambda: (500, 750),
        font=("Helvetica", 30),
        fg_color="#57a689",
        text_color="white",
        hover_color="#333333",
        width=500
    )
    tombol_500_750.place(relx=0.5, rely=0.5, anchor="center")

    tombol_750_1m = CTkButton(
        label_rek, text="750 Juta - 1 Miliar",
        command=lambda: (750, 1000),
        font=("Helvetica", 30),
        fg_color="#57a689",
        text_color="white",
        hover_color="#333333",
        width=500
    )
    tombol_750_1m.place(relx=0.5, rely=0.6, anchor="center")
    
    

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistem Angsuran Rumah")
    root.geometry("1920x1080")
    halaman1(root)
    root.mainloop()