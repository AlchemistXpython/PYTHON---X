#excelde belli bir sütundaki hücreler içindeki bilgileri belirlenen yolda arama yapıyor ve bulduğunu belirlenecek bir alana kopyalıyor.

import pandas as pd
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Paneli oluştur
root = tk.Tk()
root.title("Fatura Arama Motoru")
root.geometry("350x440")

# Fonksiyonlar
def excel_dosyasi_sec():
    file_path = filedialog.askopenfilename(title="Excel Dosyasını Seçin", filetypes=[("Excel files", "*.xlsx *.xls")])
    excel_dosya_entry.delete(0, tk.END)
    excel_dosya_entry.insert(0, file_path)

def arama_klasoru_sec():
    folder_path = filedialog.askdirectory(title="PDF Dosyalarının Bulunduğu Klasörü Seçin")
    arama_klasoru_entry.delete(0, tk.END)
    arama_klasoru_entry.insert(0, folder_path)

def yapistirma_klasoru_sec():
    folder_path = filedialog.askdirectory(title="Dosyaların Kopyalanacağı Klasörü Seçin")
    yapistirma_klasoru_entry.delete(0, tk.END)
    yapistirma_klasoru_entry.insert(0, folder_path)

def islemi_baslat():
    # Giriş verilerini al
    excel_dosyasi = excel_dosya_entry.get()
    sayfa_adi = sayfa_entry.get()
    arama_klasoru = arama_klasoru_entry.get()
    yapistirma_klasoru = yapistirma_klasoru_entry.get()

    if not excel_dosyasi or not sayfa_adi or not arama_klasoru or not yapistirma_klasoru:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    # Sayaçlar
    toplam_kayit = 0
    kopyalanan_dosyalar = 0
    bulunamayan_dosyalar = 0

    try:
        df = pd.read_excel(excel_dosyasi, sheet_name=sayfa_adi, header=None)

        # B sütunundaki "S" ile başlayan hücreler üzerinde işlem yap
        for deger in df.iloc[:, 1].dropna():  # B sütunu ikinci sütun (index 1)
            if str(deger).startswith("S"):  # "S" ile başlayan hücreler
                toplam_kayit += 1
                bulunan_dosya = None
                for dosya in os.listdir(arama_klasoru):
                    if str(deger) in dosya:
                        bulunan_dosya = dosya
                        break

                if bulunan_dosya:
                    shutil.copy(os.path.join(arama_klasoru, bulunan_dosya), yapistirma_klasoru)
                    kopyalanan_dosyalar += 1
                else:
                    bulunamayan_dosyalar += 1

        # Sonuç raporu
        messagebox.showinfo("İşlem Tamamlandı", f"Toplam kayıt: {toplam_kayit}\n"
                                                f"Kopyalanan dosya: {kopyalanan_dosyalar}\n"
                                                f"Bulunamayan dosya: {bulunamayan_dosyalar}")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

# Excel dosyası seçimi
tk.Label(root, text="Excel Dosyası:").pack(pady=5)
excel_dosya_entry = tk.Entry(root, width=50)
excel_dosya_entry.pack(pady=5)
tk.Button(root, text="Dosya Seç", command=excel_dosyasi_sec).pack(pady=5)

# Sayfa adı
tk.Label(root, text="Sayfa Adı:").pack(pady=5)
sayfa_entry = tk.Entry(root, width=50)
sayfa_entry.pack(pady=5)

# PDF dosyalarının bulunduğu klasör
tk.Label(root, text="PDF Dosyalarının Bulunduğu Klasör:").pack(pady=5)
arama_klasoru_entry = tk.Entry(root, width=50)
arama_klasoru_entry.pack(pady=5)
tk.Button(root, text="Klasör Seç", command=arama_klasoru_sec).pack(pady=5)

# Dosyaların kopyalanacağı klasör
tk.Label(root, text="Dosyaların Kopyalanacağı Klasör:").pack(pady=5)
yapistirma_klasoru_entry = tk.Entry(root, width=50)
yapistirma_klasoru_entry.pack(pady=5)
tk.Button(root, text="Klasör Seç", command=yapistirma_klasoru_sec).pack(pady=5)

# İşlemi başlat düğmesi
tk.Button(root, text="İşlemi Başlat", command=islemi_baslat).pack(pady=20)
