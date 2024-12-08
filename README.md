# APLIKASI CICILAMAN (SISTEM ANGSURAN RUMAH)
# DAFTAR ANGGOTA KELOMPOK
1. I0324088 - Muhammad Fairuz Firza
2. I0324070 - Vito Abrianda Robin	
3. I0324051 - Kholid Ardian
# Penjelasan Sistem Angsuran Rumah
Aplikasi ini adalah sebuah system dengan dua fitur utama, yaitu menghitung angsuran rumah dan rekomendasi rumah. Fitur angsuran rumah dimulai dengan memasukkan harga rumah, uang muka, jangka waktu (tahun) dan bunga dari informasi pengguna. Kemudian data tersebut di proses hingga menghasilkan angsuran bulanan yang harus dibayar oleh pengguna. Data tersebut lalu dikirim ke Email yang sudah terdaftar di aplikasi. Fitur kedua adalah rekomendasi rumah, fitur tersebut memberikan opsi kepada pengguna yang ingin membeli rumah. Fitur ini memberikan informasi tentang berbagai penjual rumah dengan range harga yang berbeda, sehingga memberikan banyak pilihan kepada pengguna. Fitur ini juga menyediakan fasilitas pembayaran bagi pengguna yang ingin langsung membeli rumah dengan berbagai pilihan pembayaran. Aplikasi ini memberikan banyak fitur yang berguna, sehingga memberi pengguna kemudahan dalam melakukan aktivitas baik angsuran ataupun membeli rumah.
# Fitur-fitur Aplikasi
1. Aplikasi ini menggunakan akun untuk setiap pengguna
2. Aplikasi ini dapat menghitung pembayaran angsuran
3. Aplikasi ini dapat mengirim data hasil perhitungan angsuran ke Email pengguna
4. Aplikasi ini dapat memberikan rekomendasi rumah dengan berbagai varian harga dan informasi yang lengkap
5. Aplikasi ini menyediakan pembayaran rumah dari rekomendasi yang diberikan dengan berbagai pilihan pembayaran
6. Aplikasi ini dapat mengirim data hasil pembayaran rumah ke Email pengguna

#Libary
1. Tkinter
2. Costumtkinter
3. tkinter.messagebox
4. tkinter.filedialog
5. smtplib
6. Email
7. email.mime
8. email.encoders
9. PIL
10. os
11. csv
12. Reportlab
    
# Flowchart
![flowchart cicilaman kelompok 13 drawio](https://github.com/user-attachments/assets/6d90a027-dc89-4a9e-9526-d55ce4bcaa42)

Flowchart atau diagram alir diatas menjelaskan mekanisme proses berjalannya sistem CicilAman. Program dimulai dengan memasukkan email pengguna yang sudah terdaftar, lalu masuk ke bagian menu utama. Pengguna bisa memilih fitur yang akan digunakan yaitu antara fitur angsuran rumah dan fitur rekomendasi rumah. Fitur angsuran diawali dengan menginput harga rumah, uang muka, jangka waktu, dan bunga. Kemudian data diproses sehingga menghasilkan angsuran bulanan yang harus dibayar oleh pengguna. Data kemudian disimpan di JSON dan dikirim ke Email yang Sudah diinput di awal oleh pengguna. Pengguna kemudian dapat memilih apakah ingin melanjutkan ke fitur rekomendasi atau keluar dari aplikasi. Sedangkan tahap awal dari fitur rekomendasi rumah adalah memilih rentang harga rumah. Pengguna kemudian diarahkan ke berbagai pilihan rumah yang sesuai dengan rentang harga yang dipilih. Jika sudah mendapatkan rumah yang pas, pengguna kemudian disuguhi informasi yang lebih lengkap dari rumah tersebut. Pengguna kemudian dapat langsung membeli rumah tersebut dengan fitur pembayaran yang sudah disediakan. Sebelum memilih metode pembayaran, pengguna harus memasukkan email yang akan digunakan untuk membeli rumah. Pengguna dapat memilih metode pembayaran, apakah ingin lunas atau cicilan. Jika sudah memilih, pengguna kemudian harus membayar sesuai ketentuan dan harus menyertakan bukti pembayaran yang dapat did upload di aplikasi. Jika sudah selesai, data pembayaran akan dikirim ke email pengguna, lalu halaman akan diarahkan Kembali ke halaman pemilihan rumah. Pengguna dapat memilih Kembali rumah atau keluar dari aplikasi.
# SiteMap
![Sitemap CicilAman Kelompok 13](https://github.com/user-attachments/assets/2da604dc-801d-4ac1-a9af-6227e859d611)

Sitemap di atas menjelaskan gambaran kasar tentang proses berjalannya aplikasi CicilAman. Sistem dimulai dari halaman utama atau home page, kemudian masuk ke halaman login atau login page. Selanjutnya sistem masuk ke daftar menu terdiri dari 2 fitur, yaitu rekomendasi rumah dan angsuran rumah. Di angsuran rumah, pengguna bisa menghitung angsurannya dengan memasukkan data yang dibutuhkan. Sedangkan di fitur rekomendasi rumah, pertama-tama pengguna memilih rentang harga untuk rumah yang ingin dituju, lalu pengguna memilih rumah yang sesuai dengan keinginannya. Pengguna dapat melakukan pembayaran setelah memasukkan data yang dibutuhkan.
