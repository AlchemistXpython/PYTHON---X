import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Yeni veriler eklenip saklanacak DataFrame
data = pd.DataFrame(columns=["S.NO", "VADE", "VADE GÜN", "TUTAR", "F SÜTUNU"])

def format_tarih(tarih):
    return tarih.strftime("%d/%m/%Y")

def format_binlik_ayirac(sayi):
    return "{:,.2f}".format(sayi)

def hesapla_ortalama_vade(df):
    try:
        # Vade günleri ve tutarların çarpımıyla toplam F sütununu hesapla
        toplam_f = (df["VADE GÜN"] * df["TUTAR"]).sum()
        toplam_tutar = df["TUTAR"].sum()

        if toplam_tutar > 0:
            # Ağırlıklı ortalama vade hesapla
            ortalama_vade = toplam_f / toplam_tutar
        else:
            ortalama_vade = 0

        # Ortalama vadeyi virgülden sonra 2 basamak olacak şekilde formatla
        ortalama_vade_gun = round(ortalama_vade, 2)

        # Ortalama vade gününe göre yeni tarih hesapla
        ortalama_vade_tarih = pd.Timestamp.today() + pd.Timedelta(days=int(ortalama_vade))

        # Ekranda görünmesi için değerleri güncelle
        lbl_ortalama_vade_val.config(text=f"{ortalama_vade_gun}")
        lbl_ortalama_tarih_val.config(text=f"{format_tarih(ortalama_vade_tarih)}")
        lbl_toplam_tutar_val.config(text=f"{format_binlik_ayirac(toplam_tutar)}")

        # Ortalama vade 180 günü aşarsa kırmızı renkli uyarı yap
        if ortalama_vade_gun > 180:
            lbl_ortalama_vade_val.config(bg="red", fg="white")
        else:
            lbl_ortalama_vade_val.config(bg=root.cget("bg"), fg="black")

    except Exception as e:
        messagebox.showerror("Hata", f"Hesaplama sırasında bir hata oluştu: {e}")

# Yeni veri ekleme veya seçilen satırı güncelleme
def veri_ekle():
    global data, selected_item
    try:
        vade = pd.to_datetime(entry_vade.get(), format='%d/%m/%Y')
        tutar = float(entry_tutar.get())
        # Tarihi normalize ederek saatleri hariç tut
        vade_gun = (vade.normalize() - pd.Timestamp.today().normalize()).days
        f_sutun = vade_gun * tutar

        if selected_item:
            index = int(tree.item(selected_item)['values'][0]) - 1
            data.loc[index, "VADE"] = vade
            data.loc[index, "VADE GÜN"] = vade_gun
            data.loc[index, "TUTAR"] = tutar
            data.loc[index, "F SÜTUNU"] = f_sutun
        else:
            yeni_veri = pd.DataFrame([[len(data) + 1, vade, vade_gun, tutar, f_sutun]],
                                     columns=["S.NO", "VADE", "VADE GÜN", "TUTAR", "F SÜTUNU"])
            data = pd.concat([data, yeni_veri], ignore_index=True)

        hesapla_ortalama_vade(data)
        tabloyu_guncelle(data)

        # Giriş kutularını temizle
        entry_vade.delete(0, tk.END)
        entry_tutar.delete(0, tk.END)
        selected_item = None

        # Veri ekleme işleminden sonra imleci vade tarihine geçir
        entry_vade.focus_set()

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı ve tarih giriniz. Tarih formatı gg/aa/yyyy olmalıdır.")


def tabloyu_guncelle(df):
    for row in tree.get_children():
        tree.delete(row)

    for i, row in df.iterrows():
        tree.insert('', tk.END, values=(row["S.NO"], format_tarih(row["VADE"]), row["VADE GÜN"], format_binlik_ayirac(row["TUTAR"])))

# Seçilen satırları silme
def secili_satiri_sil():
    global data
    selected_items = tree.selection()  # Treeview'de seçilen satırlar
    for item in selected_items:
        try:
            # Treeview'deki S.NO sütununu kullanarak DataFrame'deki doğru indeksi alıyoruz
            index = int(tree.item(item)['values'][0]) - 1  # S.NO 1'den başlıyor, indeks ise 0'dan
            if index in data.index:  # Bu indeksin DataFrame'de olup olmadığını kontrol ediyoruz
                data = data.drop(index).reset_index(drop=True)
                
                # Treeview'deki S.NO'yu güncelle (DataFrame sıfırdan indeksleniyor)
                for i in range(len(data)):
                    data.at[i, 'S.NO'] = i + 1
            else:
                messagebox.showerror("Hata", "Seçilen satır DataFrame'de bulunamadı.")
        except KeyError:
            messagebox.showerror("Hata", "Satır silinirken bir sorun oluştu.")

    tabloyu_guncelle(data)
    hesapla_ortalama_vade(data)

# Treeview'de bir satır seçildiğinde ilgili verileri giriş alanlarına getirme
def satiri_duzenle(event):
    global selected_item
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, 'values')
        entry_vade.delete(0, tk.END)
        entry_vade.insert(0, values[1])
        entry_tutar.delete(0, tk.END)
        entry_tutar.insert(0, values[3].replace(',', ''))

# Tkinter genel alana tıklanıldığında vade ve tutar alanlarını temizle
def bosluklari_temizle(event):
    global selected_item
    widget = event.widget  # Tıklanan widget
    if widget not in [tree, entry_vade, entry_tutar, btn_ekle, btn_sil, btn_yeniden_hesapla, btn_kilavuz]:
        entry_vade.delete(0, tk.END)
        entry_tutar.delete(0, tk.END)
        selected_item = None

# Tutar alanında space tuşuna basıldığında "000" ekle ve boşluk eklemeyi engelle
def space_tusuna_basildi(event):
    current_text = entry_tutar.get()
    entry_tutar.delete(0, tk.END)
    entry_tutar.insert(0, current_text + "000")
    return "break"

# Tarih giriş alanında gg/aa/yyyy formatını otomatikleştir
def tarih_giris(event):
    current_text = entry_vade.get()
    
    # Günü tamamladığında '/' ekle
    if len(current_text) == 2:
        entry_vade.insert(tk.END, "/")
    
    # Ayı tamamladığında '/' ekle
    elif len(current_text) == 5:
        entry_vade.insert(tk.END, "/")
    
    # Eğer giriş 10 karakteri aştıysa (gg/aa/yyyy) daha fazla giriş yapılmasını engelle
    elif len(current_text) > 10:
        entry_vade.delete(10, tk.END)

def kilavuz_ac():
    kilavuz_pencere = tk.Toplevel(root)
    kilavuz_pencere.title("Kılavuz")
    
    # Pencerenin genişlemesine izin verelim
    kilavuz_pencere.geometry("800x300")

    kilavuz_text = tk.Text(kilavuz_pencere)
    kilavuz_text.insert(tk.END, """Kılavuz:
1- Vade tarihini yazarken / basmanıza gerek yok, otomatik olarak ekler.

2- Tutar kısmında space "boşluk" tuşuna basıldığında "000" atar.

3- Veriler girildikten sonra, veri ekle tuşuna basılır ve imleç otomatik vade gün bölümüne gider.

4- Veri Ekle/Düzenle; tuşu ile seçimi yapılmış satırda düzeltmeleri yapıp tekra veri Ekle/Düzenle ye basılır.

5- Seçili Satırı Sil tuşu; silinmesini istediğiniz satırı siler.

6- Yeniden Hesapla tuşu ile istediğiniz satırı Ctrl + Sol Mouse ile seçip ortalamaları hesaplayabilirsiniz.

7- 180 günü geçtiğinde kırmızı ile boyanır, dikkati artırmak için.
""")
    
    kilavuz_text.config(state=tk.DISABLED)  # Text alanı sadece okunabilir olsun
    
    # Text widget'ını genişletilebilir hale getirelim
    kilavuz_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Alt kısma ek bilgiler
    alt_bilgi = tk.Label(kilavuz_pencere, text="\nVersion : 0.0.9\n\nYazılım: Bu program Mücahit Bayrak tarafından yazılmış ve geliştirilmiştir.\n\nUyarı: Bu bilgisayar programı telif hakkı yasaları ve uluslararası anlaşmalarla korunmaktadır. Bu programın tamamının veya bir bölümünü izinsiz olarak çoğaltılması veya dağıtılması ciddi yaptırımlarla karşılaşılmasına neden olabilir.", justify="left", wraplength=350)
    alt_bilgi.pack(pady=10, expand=True, fill=tk.BOTH)



# Ctrl + Sol Mouse tuşu ile seçilen satırları yeniden hesapla
def yeniden_hesapla():
    selected_items = tree.selection()
    secili_veriler = pd.DataFrame(columns=["S.NO", "VADE", "VADE GÜN", "TUTAR", "F SÜTUNU"])

    for item in selected_items:
        index = int(tree.item(item)['values'][0]) - 1
        secili_veriler = pd.concat([secili_veriler, data.loc[[index]]])

    hesapla_ortalama_vade(secili_veriler)

# Satır seçimi için global değişken
selected_item = None

root = tk.Tk()
root.title("Vade Hesaplama")
root.geometry("400x500")  # Pencere genişletildi

lbl_vade = tk.Label(root, text="Vade Tarihi (gg/aa/yyyy):")
lbl_vade.pack()
entry_vade = tk.Entry(root)
entry_vade.pack()

# Tarih girişine otomatik '/' eklemek için bind
entry_vade.bind("<KeyRelease>", tarih_giris)

lbl_tutar = tk.Label(root, text="Tutar:")
lbl_tutar.pack()
entry_tutar = tk.Entry(root)
entry_tutar.pack()

# Tutar kısmında space tuşuna basıldığında "000" ekle ve boşluk bırakmayı engelle
entry_tutar.bind("<space>", space_tusuna_basildi)

btn_ekle = tk.Button(root, text="Veri Ekle/Düzenle", command=veri_ekle)
btn_ekle.pack()

tree = ttk.Treeview(root, columns=("S.NO", "Vade", "Vade Gün", "Tutar"), show='headings')
tree.heading("S.NO", text="S.NO")
tree.heading("Vade", text="Vade")
tree.heading("Vade Gün", text="Vade Gün")
tree.heading("Tutar", text="Tutar")

tree.column("S.NO", width=50)
tree.column("Vade", width=100)
tree.column("Vade Gün", width=100)
tree.column("Tutar", width=150)

tree.pack()

tree.bind("<ButtonRelease-1>", satiri_duzenle)

btn_sil = tk.Button(root, text="Seçili Satırları Sil", command=secili_satiri_sil)
btn_sil.pack()

btn_yeniden_hesapla = tk.Button(root, text="Yeniden Hesapla (Seçilen)", command=yeniden_hesapla)
btn_yeniden_hesapla.pack()

info_frame = tk.Frame(root)
info_frame.pack(pady=10)

lbl_ortalama_vade = tk.Label(info_frame, text="ORTALAMA VADE:", font=("Arial", 12), anchor="e")
lbl_ortalama_vade.grid(row=0, column=0, padx=10, sticky="e")

lbl_ortalama_tarih = tk.Label(info_frame, text="ORTALAMA TARİH:", font=("Arial", 12), anchor="e")
lbl_ortalama_tarih.grid(row=1, column=0, padx=10, sticky="e")

lbl_toplam_tutar = tk.Label(info_frame, text="TOPLAM TUTAR:", font=("Arial", 12), anchor="e")
lbl_toplam_tutar.grid(row=2, column=0, padx=10, sticky="e")

lbl_ortalama_vade_val = tk.Label(info_frame, text="", font=("Arial", 12), anchor="w")
lbl_ortalama_vade_val.grid(row=0, column=1, padx=10, sticky="w")

lbl_ortalama_tarih_val = tk.Label(info_frame, text="", font=("Arial", 12), anchor="w")
lbl_ortalama_tarih_val.grid(row=1, column=1, padx=10, sticky="w")

lbl_toplam_tutar_val = tk.Label(info_frame, text="", font=("Arial", 12), anchor="w")
lbl_toplam_tutar_val.grid(row=2, column=1, padx=10, sticky="w")

# Kılavuz butonu, tıklanınca yeni bir pencere açacak
btn_kilavuz = tk.Button(root, text="Kılavuz", command=kilavuz_ac)
btn_kilavuz.pack(side=tk.RIGHT)

# Tkinter'ın herhangi bir yerine tıklanırsa boşlukları temizle
root.bind("<Button-1>", bosluklari_temizle)

root.mainloop()


