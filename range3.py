import tkinter as tk
from PIL import Image, ImageTk
from customtkinter import CTkButton, CTkEntry
from tkinter import messagebox, filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

# Membaca data rumah dari file CSV
def load_rumah_data():
    rumah_data = []
    with open('data_rumah3.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rumah_data.append(row)
    return rumah_data

# Global untuk menyimpan data rumah
rumah_data = load_rumah_data()
current_index = 0 

def halaman_rumah(main):
    global bg_rekomen1, bg_rekomen2, current_index

    from programutama import halaman_rekomen
    
    for widget in main.winfo_children():
        widget.destroy()

    frame_rumah = tk.Frame(main, bg='black')
    frame_rumah.pack(expand=True, fill=tk.BOTH)

    utama = ImageTk.PhotoImage(Image.open('bg/7.png'))
    label_rum = tk.Label(frame_rumah, image=utama )
    label_rum.image = utama  
    label_rum.pack(fill=tk.BOTH, expand=tk.YES)

    rumah1 = rumah_data[current_index]
    rumah2 = rumah_data[(current_index + 1) % len(rumah_data)] 

    try:
        gambar_rumah1 = Image.open(rumah1["gambar"]).resize((250, 250), Image.LANCZOS)
        bg_rekomen1 = ImageTk.PhotoImage(gambar_rumah1)
        label_gambar1 = tk.Label(label_rum, image=bg_rekomen1, bg="#57a689", borderwidth=0)
        label_gambar1.image = bg_rekomen1
        label_gambar1.place(relx=0.3, rely=0.38, anchor="center")
    except FileNotFoundError:
        tk.Label(label_rum, text="Gambar 1 tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="#57a689").place(relx=0.3, rely=0.4, anchor="center")

    info_rumah1 = f"""Nama: {rumah1['nama']}
Lokasi: {rumah1['lokasi']}
Ukuran: {rumah1['ukuran']}
Interior: {rumah1['interior']}
Harga: {rumah1['harga']}"""
    tk.Label(label_rum, text=info_rumah1, font=("Helvetica", 14), bg="#57a689", fg="white").place(relx=0.3, rely=0.61, anchor="center")
    CTkButton(
        label_rum, text="",
        image=ImageTk.PhotoImage(Image.open("bg/pilih.png").resize((300, 50), Image.LANCZOS)),  
        cursor='hand2', command=lambda: halaman_pembayaran(main, rumah1),
        fg_color="transparent", border_spacing=0
    ).place(relx=0.3, rely=0.78, anchor="center")

    try:
        gambar_rumah2 = Image.open(rumah2["gambar"]).resize((250, 250), Image.LANCZOS)
        bg_rekomen2 = ImageTk.PhotoImage(gambar_rumah2)
        label_gambar2 = tk.Label(label_rum, image=bg_rekomen2, bg="#57a689", borderwidth=0)
        label_gambar2.image = bg_rekomen2
        label_gambar2.place(relx=0.7, rely=0.38, anchor="center")
    except FileNotFoundError:
        tk.Label(label_rum, text="Gambar 2 tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="#57a689").place(relx=0.7, rely=0.4, anchor="center")

    info_rumah2 = f"""Nama: {rumah2['nama']}
Lokasi: {rumah2['lokasi']}
Ukuran: {rumah2['ukuran']}
Interior: {rumah2['interior']}
Harga: {rumah2['harga']}"""
    tk.Label(label_rum, text=info_rumah2, font=("Helvetica", 14), bg="#57a689", fg="white", relief="flat").place(relx=0.7, rely=0.61, anchor="center")
    CTkButton(
        label_rum, text="",  
        image=ImageTk.PhotoImage(Image.open("bg/pilih.png").resize((300, 50), Image.LANCZOS)),  
        cursor='hand2', command=lambda: halaman_pembayaran(main, rumah2),
        fg_color="transparent", border_spacing=0
    ).place(relx=0.7, rely=0.78, anchor="center")

    CTkButton(
        label_rum, text="",  
        image=ImageTk.PhotoImage(Image.open("bg/kir.png").resize((50, 50), Image.LANCZOS)),  
        cursor='hand2', command=lambda: next_rumah(-2),
        fg_color="transparent", border_spacing=0
    ).place(relx=0.1, rely=0.45, anchor="center")

    CTkButton(
        label_rum, text="", 
        image=ImageTk.PhotoImage(Image.open("bg/kan.png").resize((50, 50), Image.LANCZOS)),  
        cursor='hand2', command=lambda: next_rumah(2),
        fg_color="transparent", border_spacing=0
    ).place(relx=0.9, rely=0.45, anchor="center")
    
    def next_rumah(step):
        global current_index
        current_index = (current_index + step) % len(rumah_data)
        halaman_rumah(main)
        
            # Tombol Quit
    gambar_quit = Image.open('bg/quit.png').resize((300, 60), Image.LANCZOS)
    gambar_quit2 = ImageTk.PhotoImage(gambar_quit)
    tombolquit = CTkButton(
        label_rum, text="", image=gambar_quit2, cursor='hand2',
        border_spacing=0, command=main.quit, fg_color="transparent"
    )
    tombolquit.place(relx=0.85, rely=0.1, anchor="center")
    
    gambar_back = Image.open('bg/kembali.png').resize((300, 60), Image.LANCZOS)
    gambar_back2 = ImageTk.PhotoImage(gambar_back)
    tombolback = CTkButton(
        label_rum, text="", image=gambar_back2, cursor='hand2',
        border_spacing=0, command=lambda:halaman_rekomen(main), fg_color="transparent"
    )
    tombolback.place(relx=0.15, rely=0.1, anchor="center")

        
def halaman_pembayaran(main, rumah):
    global bg_rumah, bg_latar

    for widget in main.winfo_children():
        widget.destroy()

    frame_pembayaran = tk.Frame(main)
    frame_pembayaran.pack(expand=True, fill=tk.BOTH)
    
    try:
        background_image = Image.open("bg/9.png")  
        bg_image_resized = background_image.resize((main.winfo_width(), main.winfo_height()), Image.LANCZOS)
        bg_latar = ImageTk.PhotoImage(bg_image_resized)
        label_bg = tk.Label(frame_pembayaran, image=bg_latar)
        label_bg.place(relx=0, rely=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Gambar latar belakang tidak ditemukan!")

    try:
        gambar_rumah = Image.open(rumah["gambar"]).resize((500, 500), Image.LANCZOS)
        bg_rumah = ImageTk.PhotoImage(gambar_rumah)
        label_gambar_rumah = tk.Label(frame_pembayaran, image=bg_rumah, border=0)
        label_gambar_rumah.image = bg_rumah
        label_gambar_rumah.place(relx=0.25, rely=0.46, anchor="center") 
    except FileNotFoundError:
        tk.Label(frame_pembayaran, text="Gambar tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="white").place(x=50, y=50)

    info_rumah = f"""Nama: {rumah['nama']}
Lokasi: {rumah['lokasi']}
Ukuran: {rumah['ukuran']}
Interior: {rumah['interior']}
Harga: {rumah['harga']}
Bank Tujuan: {rumah['bank']}
Nomor Rekening: {rumah['rekening']}
Pemilik Rekening: {rumah['pemilik']}"""
    info_label = tk.Label(frame_pembayaran, text=info_rumah, font=("Helvetica", 20, "bold"), bg="#d6e4e4", fg="#545454", justify="left")
    info_label.place(relx=0.66, rely=0.43, anchor="center") 

    confirm_button = CTkButton(
        frame_pembayaran, 
        text="Konfirmasi Pembayaran", 
        font=("Helvetica", 25), 
        fg_color="#57a689",  
        hover_color="#333333", 
        text_color="white",
        command=lambda: halaman_pilihan_pembayaran(main, rumah)
    )
    confirm_button.place(relx=0.84, rely=0.68, anchor="center") 

    back_button = CTkButton(
        frame_pembayaran, 
        text="Kembali", 
        font=("Helvetica", 25), 
        fg_color="#2a729c",  
        hover_color="#333333",  
        text_color="white",
        command=lambda: halaman_rumah(main)
    )
    back_button.place(relx=0.55, rely=0.68, anchor="center")  
    
def halaman_pilihan_pembayaran(main, rumah):
    global bg_belakang

    for widget in main.winfo_children():
        widget.destroy()

    frame_pilihan = tk.Frame(main)
    frame_pilihan.pack(expand=True, fill=tk.BOTH)

    try:
        bayar_bg = Image.open("bg/10.png") 
        bayar_bg_resize = bayar_bg.resize((main.winfo_width(), main.winfo_height()), Image.LANCZOS)
        bg_belakang = ImageTk.PhotoImage(bayar_bg_resize)
        label_buy = tk.Label(frame_pilihan, image=bg_belakang)
        label_buy.place(relx=0, rely=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Gambar latar belakang tidak ditemukan!")

    entry_email = CTkEntry(frame_pilihan, font=("Helvetica", 20), width=400, justify="center")
    entry_email.place(relx=0.5, rely=0.35, anchor="center")
    
    
    def go_to_lunas():
        email = entry_email.get()
        if not email:
            messagebox.showerror("Error", "Email harus diisi!")
            return
        halaman_lunas(main, rumah, email)

    def go_to_cicilan():
        email = entry_email.get()
        if not email:
            messagebox.showerror("Error", "Email harus diisi!")
            return
        halaman_cicilan(main, rumah, email)

    # Tombol cicil
    gambar_cicil = Image.open('bg/cicil.png').resize((300, 60), Image.LANCZOS)
    gambar_cicil2 = ImageTk.PhotoImage(gambar_cicil)
    tombolcicil = CTkButton(
        frame_pilihan, text="", image=gambar_cicil2, cursor='hand2',
        border_spacing=0, command=go_to_cicilan, fg_color="transparent"
    )
    tombolcicil.place(relx=0.5, rely=0.55, anchor="center")
    
    # Tombol lunas
    gambar_lunas = Image.open('bg/lunas.png').resize((300, 60), Image.LANCZOS)
    gambar_lunas2= ImageTk.PhotoImage(gambar_lunas)
    tombollunas = CTkButton(
        frame_pilihan, text="", image=gambar_lunas2, cursor='hand2',
        border_spacing=0, command=go_to_lunas,
        fg_color="transparent"
    )
    tombollunas.place(relx=0.5, rely=0.65, anchor="center")
    
    gambar_backk = Image.open('bg/kembali.png').resize((300, 60), Image.LANCZOS)
    gambar_backk2 = ImageTk.PhotoImage(gambar_backk)
    tombolback = CTkButton(
        frame_pilihan, text="", image=gambar_backk2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_pembayaran(main, rumah), fg_color="transparent"
    )
    tombolback.place(relx=0.15, rely=0.1, anchor="center")

def create_pdf_report_with_proof(data, payment_type, filename):
    
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    table_data = [
        ['Detail', 'Informasi'],
        ['Tipe Pembayaran', payment_type],
        ['Nominal Pembayaran', data.get('nominal', 'N/A')],
        ['Bank Tujuan', data.get('bank_tujuan', 'N/A')],
        ['Nomor Rekening Tujuan', data.get('rekening_tujuan', 'N/A')]
    ]
    
    table = Table(table_data, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    
    content = []
    content.append(Paragraph(f"Laporan Pembayaran {payment_type}", styles['Title']))
    content.append(table)
    
    try:
        proof_image = Image(data.get('bukti_pembayaran', ''), width=4*inch, height=3*inch)
        content.append(Paragraph("Bukti Pembayaran:", styles['Heading2']))
        content.append(proof_image)
    except Exception as e:
        content.append(Paragraph(f"Gagal memuat bukti pembayaran: {e}", styles['BodyText']))

    doc.build(content) 

def send_email_with_attachment(recipient_email, filename):
    try:
       
        sender_email = "cicilamann@gmail.com"  
        sender_password = "ukkg flhj harg uvov"  

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Laporan Pembayaran Rumah"
        
        body = "Terlampir laporan pembayaran rumah Anda."
        msg.attach(MIMEText(body, 'plain'))
        
        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {filename}")
        msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        messagebox.showinfo("Email", "Laporan berhasil dikirim!")
    
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengirim email: {str(e)}")
        

def halaman_lunas(main, rumah, email):
    global lunas_bel

    for widget in main.winfo_children():
        widget.destroy()

    frame_lunas = tk.Frame(main)
    frame_lunas.pack(expand=True, fill=tk.BOTH)
    
    try:
        lunas_bg = Image.open("bg/11.png") 
        lunas_bg_resize = lunas_bg.resize((main.winfo_width(), main.winfo_height()), Image.LANCZOS)
        lunas_bel = ImageTk.PhotoImage(lunas_bg_resize)
        label_lun = tk.Label(frame_lunas, image=lunas_bel)
        label_lun.place(relx=0, rely=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Gambar latar belakang tidak ditemukan!")
        
    try:
        gamb_rumah = Image.open(rumah["gambar"]).resize((220, 220), Image.LANCZOS)
        bg_rum = ImageTk.PhotoImage(gamb_rumah)
        label_gam_rum = tk.Label(frame_lunas, image=bg_rum, border=0)
        label_gam_rum.image = bg_rum
        label_gam_rum.place(relx=0.235, rely=0.415, anchor="center") 
    except FileNotFoundError:
        tk.Label(frame_lunas, text="Gambar tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="white").place(x=50, y=50)

    uploaded_proof_path = [None]

    info_rumah = f"""Nama: {rumah['nama']}
Bank Tujuan: {rumah['bank']}
Nomor Rekening: {rumah['rekening']}
Pemilik Rekening: {rumah['pemilik']}
Harga Rumah: {rumah['harga']}"""
    tk.Label(frame_lunas, text=info_rumah, font=("Helvetica", 18,"bold"), bg="#d6e4e4", fg="#545454", justify="left").place(relx=0.24, rely=0.726,anchor="center")

    def upload_proof():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            uploaded_proof_path[0] = file_path
            
            try:
                img = Image.open(file_path)
                img.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(img)
                proof_preview.configure(image=photo)
                proof_preview.image = photo
                upload_button.configure(text="Ganti Bukti Pembayaran")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat gambar: {e}")

    upload_button = CTkButton(frame_lunas, text="Upload Bukti Pembayaran", 
                               font=("Helvetica", 25),
                               fg_color="#57a689",
                               hover_color= "#333333",
                               text_color="white",
                               command=upload_proof)
    upload_button.place(relx=0.772, rely=0.32, anchor="center")

    proof_preview = tk.Label(frame_lunas)
    proof_preview.place(relx=0.77, rely=0.48, anchor="center")

    entry_nama_pemilik = CTkEntry(frame_lunas, font=("Helvetica", 20), width=400, justify="center")
    entry_nama_pemilik.place(relx=0.505, rely=0.36, anchor="center")

    entry_nominal = CTkEntry(frame_lunas, font=("Helvetica", 20), width=400, justify="center")
    entry_nominal.place(relx=0.505, rely=0.5, anchor="center")

    def konfirmasi_lunas():
      
        if uploaded_proof_path[0] is None:
            messagebox.showerror("Error", "Harap upload bukti pembayaran!")
            return

        if not entry_nama_pemilik.get():
            messagebox.showerror("Error", "Nama Pemilik Pembayar harus diisi!")
            return

        if not entry_nominal.get() or not entry_nominal.get().isdigit():
            messagebox.showerror("Error", "Nominal Pembayaran harus diisi dan berupa angka!")
            return

        nominal = entry_nominal.get()
        
        payment_data = {
            'nama_pemilik': entry_nama_pemilik.get(),
            'nominal': nominal,
            'bukti_pembayaran': uploaded_proof_path[0],
            'bank_tujuan': rumah['bank'],
            'rekening_tujuan': rumah['rekening']
        }

        pdf_filename = f"Pembayaran_Lunas_{rumah['nama']}.pdf"
        create_pdf_report_with_proof(payment_data, "Lunas", pdf_filename)

        send_email_with_attachment(email, pdf_filename)

        messagebox.showinfo("Success", "Pembayaran lunas berhasil dan email telah dikirim!")
        halaman_rumah(main)  


    CTkButton(frame_lunas, text="Konfirmasi Pembayaran Lunas", 
              font=("Helvetica", 25), 
              fg_color="#57a689",
              hover_color="#333333",
              text_color="white",
              command=konfirmasi_lunas).place(relx=0.5, rely=0.58, anchor="center")
    
    gambar_backkkk = Image.open('bg/kembali.png').resize((300, 60), Image.LANCZOS)
    gambar_backkkk2 = ImageTk.PhotoImage(gambar_backkkk)
    tombolback = CTkButton(
        frame_lunas, text="", image=gambar_backkkk2, cursor='hand2',
        border_spacing=0, command=lambda:halaman_pilihan_pembayaran(main, rumah), fg_color="transparent"
    )
    tombolback.pack(padx=150, pady=50, anchor='s', side='left')   

    # Tombol Quit
    gambar_quit = Image.open('bg/quit.png').resize((300, 60), Image.LANCZOS)
    gambar_quit2 = ImageTk.PhotoImage(gambar_quit)
    tombolquit = CTkButton(
        frame_lunas, text="", image=gambar_quit2, cursor='hand2',
        border_spacing=0, command=main.quit, fg_color="transparent"
    )
    tombolquit.pack(padx=150, pady=50, anchor='s', side='right')    

def halaman_cicilan(main, rumah, email):
    global cic

    for widget in main.winfo_children():
        widget.destroy()
    
    try:
        total_harga = float(str(rumah['harga']).replace('Rp ', '').replace('.', '').replace(',', '.'))
    except ValueError:
        messagebox.showerror("Error", "Format harga rumah tidak valid!")
        return
    
    frame_perhitungan = tk.Frame(main)
    frame_perhitungan.pack(expand=True, fill=tk.BOTH)
    
    try:
        cicil_bg = Image.open("bg/12.png") 
        cicil_bg_resize = cicil_bg.resize((main.winfo_width(), main.winfo_height()), Image.LANCZOS)
        cic = ImageTk.PhotoImage(cicil_bg_resize)
        cicil_cil = tk.Label(frame_perhitungan, image=cic)
        cicil_cil.place(relx=0, rely=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Gambar latar belakang tidak ditemukan!")
        
    try:
        gamb_rumah = Image.open(rumah["gambar"]).resize((220, 220), Image.LANCZOS)
        bg_rum = ImageTk.PhotoImage(gamb_rumah)
        label_gam_rum = tk.Label(frame_perhitungan, image=bg_rum, border=0)
        label_gam_rum.image = bg_rum
        label_gam_rum.place(relx=0.305, rely=0.405, anchor="center")  
    except FileNotFoundError:
        tk.Label(frame_perhitungan, text="Gambar tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="white").place(x=50, y=50)
    
    
    tk.Label(frame_perhitungan, text=f"Harga Rumah: Rp {total_harga:,.2f}", 
             font=("Helvetica", 18, "bold"), bg="#d6e4e4", fg="#545454").place(relx=0.305, rely=0.666, anchor="center")
    
    entry_dp = CTkEntry(frame_perhitungan, font=("Helvetica", 25), width=400, justify="center")
    entry_dp.place(relx=0.685, rely=0.33, anchor="center")
    
    entry_tenor = CTkEntry(frame_perhitungan, font=("Helvetica", 25), width=400, justify="center")
    entry_tenor.place(relx=0.685, rely=0.47, anchor="center")
    
    entry_suku_bunga = CTkEntry(frame_perhitungan, font=("Helvetica", 25), width=400, justify="center")
    entry_suku_bunga.place(relx=0.685, rely=0.6, anchor="center")
    
    cicilan_result = [None]
    
    def hitung_cicilan():
        try:
            dp = float(entry_dp.get())
            tenor = int(entry_tenor.get())
            suku_bunga = float(entry_suku_bunga.get())
            
            sisa_pinjaman = total_harga - dp
            bunga_bulanan = suku_bunga / 12 / 100
            cicilan_bulanan = sisa_pinjaman * (bunga_bulanan * (1 + bunga_bulanan)**tenor) / ((1 + bunga_bulanan)**tenor - 1)
            
            cicilan_result[0] = round(cicilan_bulanan, 2)
            
            halaman_cicilan2(main, rumah, email, cicilan_result[0])
        
        except ValueError:
            messagebox.showerror("Error", "Masukkan data dengan benar!")
    
    btn_hitung = CTkButton(frame_perhitungan, 
                           text="Hitung Cicilan", 
                           font=("Helvetica", 25), 
                           fg_color="#57a689",
                           hover_color="#333333",
                           text_color="white",
                           command=hitung_cicilan)
    btn_hitung.place(relx=0.685, rely=0.67, anchor="center")
    
    gambar_backkk = Image.open('bg/kembali.png').resize((300, 60), Image.LANCZOS)
    gambar_backkk2 = ImageTk.PhotoImage(gambar_backkk)
    tombolback = CTkButton(
        frame_perhitungan, text="", image=gambar_backkk2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_pilihan_pembayaran(main, rumah), fg_color="transparent"
    )
    tombolback.pack(padx=150, pady=50, anchor='s', side='left')   

def halaman_cicilan2(main, rumah, email, nominal_cicilan=None):
    global cica
    
    for widget in main.winfo_children():
        widget.destroy()
    
    uploaded_proof_path = [None]
    
    info_rumah = f"""Nama: {rumah['nama']} 
Bank Tujuan: {rumah['bank']} 
Nomor Rekening: {rumah['rekening']} 
Pemilik Rekening: {rumah['pemilik']}"""
    
    frame_cici = tk.Frame(main)
    frame_cici.pack(expand=True, fill=tk.BOTH)
    
    try:
        cicilan2_bg = Image.open("bg/13.png")  
        cicilan2_bg_resize = cicilan2_bg.resize((main.winfo_width(), main.winfo_height()), Image.LANCZOS)
        cica = ImageTk.PhotoImage(cicilan2_bg_resize)
        cicilan_cil = tk.Label(frame_cici, image=cica)
        cicilan_cil.place(relx=0, rely=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Gambar latar belakang tidak ditemukan!")
        
    try:
        ga_rumah = Image.open(rumah["gambar"]).resize((220, 220), Image.LANCZOS)
        rum_bg = ImageTk.PhotoImage(ga_rumah)
        label_ga_rum = tk.Label(frame_cici, image=rum_bg, border=0)
        label_ga_rum.image = rum_bg
        label_ga_rum.place(relx=0.236, rely=0.418, anchor="center") 
    except FileNotFoundError:
        tk.Label(frame_cici, text="Gambar tidak ditemukan!", font=("Helvetica", 16), fg="red", bg="white").place(x=50, y=50)
    
    tk.Label(frame_cici, text=info_rumah, font=("Helvetica", 18, "bold"), 
             bg="#d6e4e4", fg="#545454", justify="left").place(relx=0.123, rely=0.79, anchor="sw")
    
    
    if nominal_cicilan:
        tk.Label(frame_cici, text=f"Rp {nominal_cicilan:,.2f}", 
                 font=("Helvetica", 27, "bold"), bg="#d6e4e4", fg="#545454").place(relx=0.5, rely=0.37, anchor="center")

        entry_nominal = CTkEntry(frame_cici, font=("Helvetica", 20, "bold"), justify="center",width=400)
        entry_nominal.insert(0, f"{nominal_cicilan:.2f}")
        entry_nominal.place(relx=0.508, rely=0.53, anchor="center")
    
    def upload_proof():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            uploaded_proof_path[0] = file_path
            # Display thumbnail of uploaded image
            try:
                img = Image.open(file_path)
                img.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(img)
                proof_preview.configure(image=photo)
                proof_preview.image = photo
                upload_button.configure(text="Ganti Bukti Pembayaran")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat gambar: {e}")
    
    # tombol upload
    upload_button = CTkButton(frame_cici, text="Upload Bukti Pembayaran", 
                               font=("Helvetica", 25),
                               fg_color="#57a689",
                               hover_color= "#333333",
                               text_color="white",
                               command=upload_proof)
    upload_button.place(relx=0.772, rely=0.32, anchor="center")
    
    proof_preview = tk.Label(frame_cici, bg="white")
    proof_preview.place(relx=0.77, rely=0.48, anchor="center")
    
    def konfirmasi_cicilan():
        rekening = None  
        nominal = entry_nominal.get()

        if not nominal:
            messagebox.showerror("Error", "Nominal harus diisi!")
            return

        if uploaded_proof_path[0] is None:
            messagebox.showerror("Error", "Harap upload bukti pembayaran!")
            return

        try:
            nominal = float(nominal)
            total_harga = float(rumah['harga'].replace('Rp ', '').replace('.', ''))
            
            if nominal <= 0 or nominal > total_harga:
                messagebox.showerror("Error", "Nominal tidak valid!")
                return
        except ValueError:
            messagebox.showerror("Error", "Nominal harus berupa angka!")
            return
        
        payment_data = {
            'nama_pemilik': 'Pembayaran Cicilan',
            'bukti_pembayaran': uploaded_proof_path[0],
            'nominal': f"Rp {nominal:,}",
            'bank_tujuan': rumah['bank'],
            'rekening_tujuan': rumah['rekening']
        }

        pdf_filename = f"Pembayaran_Cicilan_{rumah['nama']}.pdf"
        create_pdf_report_with_proof(payment_data, "Cicilan", pdf_filename)

        send_email_with_attachment(email, pdf_filename)

        halaman_rumah(main)

    CTkButton(frame_cici, text="Konfirmasi Pembayaran", 
              font=("Helvetica", 25), 
              fg_color="#57a689",
              hover_color="#333333",
              text_color="white",
              command=konfirmasi_cicilan).place(relx=0.508, rely=0.6, anchor="center")
    
    gambar_backkkk = Image.open('bg/kembali.png').resize((300, 60), Image.LANCZOS)
    gambar_backkkk2 = ImageTk.PhotoImage(gambar_backkkk)
    tombolback = CTkButton(
        frame_cici, text="", image=gambar_backkkk2, cursor='hand2',
        border_spacing=0, command=lambda: halaman_cicilan(main, rumah, email), fg_color="transparent"
    )
    tombolback.pack(padx=150, pady=50, anchor='s', side='left')   

    # Tombol Quit
    gambar_quit = Image.open('bg/quit.png').resize((300, 60), Image.LANCZOS)
    gambar_quit2 = ImageTk.PhotoImage(gambar_quit)
    tombolquit = CTkButton(
        frame_cici, text="", image=gambar_quit2, cursor='hand2',
        border_spacing=0, command=main.quit, fg_color="transparent"
    )
    tombolquit.pack(padx=150, pady=50, anchor='s', side='right')            