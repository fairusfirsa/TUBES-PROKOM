import csv

# Data rekomendasi rumah
rumah_data = [
    {
        "nama": "Skyloft Villas",
        "lokasi": "jebres",
        "harga": "Rp 900.000.000",
        "gambar": "rumah/mewah 1.jpg",
        "ukuran": "900 m²",
        "interior":"Semi Modern",
        "bank": "Bank BNI",
        "rekening": "1764623855",
        "pemilik": "Hari Tandy",
        "nomor telp":"086482358798"
    },
    {
        "nama": "Aurora Residence",
        "lokasi": "Palur",
        "harga": "Rp 850.000.000",
        "gambar": "rumah/mewah 2.jpg",
        "ukuran": "700 m²",
        "interior":"Modern",
        "bank": "Bank BRI",
        "rekening": "7628459104",
        "pemilik": "Siti Sasmita",
        "nomor telp":"0842609984"
    },
    {
        "nama": "Vista Prime",
        "lokasi": "Mojosongo",
        "harga": "Rp 1.000.000.000",
        "gambar": "rumah/mewah 3.jpg",
        "ukuran": "900 m²",
        "interior":"Japanese",
        "bank": "Bank BSI",
        "rekening": "2571536498",
        "pemilik": "Waluyo",
        "nomor telp":"088818354612"
    },
    {
        "nama": "Metro Edge",
        "lokasi": "Solo Baru",
        "harga": "Rp 1.200.000.000",
        "gambar": "rumah/mewah 4.jpg",
        "ukuran": "900 m²",
        "interior":"Modern Futuristic",
        "bank": "Seabank",
        "rekening": "9329467193",
        "pemilik": "Tyas",
        "nomor telp":"088264510926"
    },
    {
        "nama": "Metro Edge",
        "lokasi": "Jebres",
        "harga": "Rp 900.000.000",
        "gambar": "rumah/mewah 5.jpg",
        "ukuran": "800 m²",
        "interior":"Mansion",
        "bank": "Bank BNI",
        "rekening": "2870648162",
        "pemilik": "Aji Sentosa",
        "nomor telp":"089173999472"

    },
    {
        "nama": "Amara Luxe",
        "lokasi": "Kartasura",
        "harga": "Rp 950.000.000",
        "gambar": "rumah/mewah 6.jpg",
        "ukuran": "950 m²",
        "interior":"Modern Futuristic",
        "bank": "Bank BNI",
        "rekening": "8409651098",
        "pemilik": "Tukul",
        "nomor telp":"088272289713"
    }
    
]

# Menyimpan data rumah ke file CSV
with open('data_rumah4.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=rumah_data[0].keys())
    writer.writeheader()  # Menulis header kolom
    writer.writerows(rumah_data)