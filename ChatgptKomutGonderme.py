#v5 ekran koruyucuyu iptal için mouse aktifliği
import pyautogui
import threading
import tkinter as tk
import time

# Gönder simgesinin ekrandaki koordinatlarını belirleyin
gonder_simgesi_koordinat = (1200, 800)  # Örneğin, simgenin bulunduğu X ve Y koordinatları
beklenen_renk = (128, 128, 128)  # Aktif olmayan simgenin renk değeri

# İşlem kontrol değişkeni
is_running = False

def simge_durumunu_kontrol_et():
    global is_running
    if is_running:
        # Gönder simgesinin rengini al
        renk = pyautogui.pixel(gonder_simgesi_koordinat[0], gonder_simgesi_koordinat[1])
        
        # Eğer simge rengi beklenen renkten farklıysa (aktif hale gelmişse)
        if renk != beklenen_renk:
            print("'Geç' yazılıyor ve gönderiliyor...")
            pyautogui.write("gec")
            pyautogui.press("enter")
        
        # 1 saniye sonra tekrar kontrol eder
        window.after(1000, simge_durumunu_kontrol_et)  # Döngü benzeri bir kontrol sağlar

def mouse_hareketi():
    global is_running
    while is_running:
        # Mouse'u biraz hareket ettir
        x, y = pyautogui.position()  # Mevcut pozisyonu al
        pyautogui.moveTo(x + 1, y)  # 1 piksel sağa hareket ettir
        pyautogui.moveTo(x, y)  # Orijinal pozisyona geri dön
        time.sleep(10)  # 10 saniyede bir hareket ettir

def baslat():
    global is_running
    if not is_running:  # Eğer işlem zaten çalışıyorsa tekrar başlatmaz
        is_running = True
        simge_durumunu_kontrol_et()  # Simge kontrol işlevini başlat
        threading.Thread(target=mouse_hareketi, daemon=True).start()  # Mouse hareketi için yeni bir thread başlat
        print("İşlem başlatıldı.")

def durdur():
    global is_running
    is_running = False
    print("İşlem durduruldu.")

# GUI Oluşturma
window = tk.Tk()
window.title("Otomatik 'Gec' Yazma")
window.geometry("300x150")

# Başlat ve Durdur Düğmeleri
baslat_butonu = tk.Button(window, text="Başlat", command=baslat, width=15, height=2)
baslat_butonu.pack(pady=10)

durdur_butonu = tk.Button(window, text="Durdur", command=durdur, width=15, height=2)
durdur_butonu.pack(pady=10)

# GUI döngüsü
window.mainloop()





#-------------------------------------------------------------------------------------------------------------------------------------

# #v4 gui başlat durdur

# import pyautogui
# import threading
# import tkinter as tk

# # Gönder simgesinin ekrandaki koordinatlarını belirleyin
# gonder_simgesi_koordinat = (1200, 800)  # Örneğin, simgenin bulunduğu X ve Y koordinatları
# beklenen_renk = (128, 128, 128)  # Aktif olmayan simgenin renk değeri

# # İşlem kontrol değişkeni
# is_running = False

# def simge_durumunu_kontrol_et():
#     global is_running
#     if is_running:
#         # Gönder simgesinin rengini al
#         renk = pyautogui.pixel(gonder_simgesi_koordinat[0], gonder_simgesi_koordinat[1])
        
#         # Eğer simge rengi beklenen renkten farklıysa (aktif hale gelmişse)
#         if renk != beklenen_renk:
#             print("'Geç' yazılıyor ve gönderiliyor...")
#             pyautogui.write("geç")
#             pyautogui.press("enter")
        
#         # 1 saniye sonra tekrar kontrol eder
#         window.after(1000, simge_durumunu_kontrol_et)  # Döngü benzeri bir kontrol sağlar

# def baslat():
#     global is_running
#     if not is_running:  # Eğer işlem zaten çalışıyorsa tekrar başlatmaz
#         is_running = True
#         simge_durumunu_kontrol_et()
#         print("İşlem başlatıldı.")

# def durdur():
#     global is_running
#     is_running = False
#     print("İşlem durduruldu.")

# # GUI Oluşturma
# window = tk.Tk()
# window.title("Otomatik 'Geç' Yazma")
# window.geometry("300x150")

# # Başlat ve Durdur Düğmeleri
# baslat_butonu = tk.Button(window, text="Başlat", command=baslat, width=15, height=2)
# baslat_butonu.pack(pady=10)

# durdur_butonu = tk.Button(window, text="Durdur", command=durdur, width=15, height=2)
# durdur_butonu.pack(pady=10)

# # GUI döngüsü
# window.mainloop()






#----------------------------------------------------------------------------------------------------------------------------
# #v3 chatgpt de "mesaj boş" simgesini gördüğünde geç yaz
# import pyautogui
# import time

# # Gönder simgesinin ekrandaki koordinatlarını belirleyin
# # Bu koordinatlar sizin ekranınıza göre ayarlanmalıdır
# # Örneğin, gönder simgesi ekranın sağ alt köşesindeyse, ona göre ayarlayın
# gonder_simgesi_koordinat = (1200, 800)  # Örneğin, simgenin bulunduğu X ve Y koordinatları

# # Beklenen renk değerini belirtin (örneğin aktif gri rengi)
# beklenen_renk = (128, 128, 128)  # Bu rengi kendinize göre ayarlamanız gerekebilir

# def simge_durumunu_kontrol_et():
#     while True:
#         # Gönder simgesinin rengini al
#         renk = pyautogui.pixel(gonder_simgesi_koordinat[0], gonder_simgesi_koordinat[1])
        
#         # Eğer simge rengi beklenen renkten farklıysa (aktif hale gelmişse)
#         if renk != beklenen_renk:
#             print("'Geç' yazılıyor ve gönderiliyor...")
#             pyautogui.write("gec")
#             pyautogui.press("enter")
#             time.sleep(5)  # Bir süre bekleyip tekrar kontrol etmek için
            
#         time.sleep(1)  # Simgeyi her saniye kontrol et

# # İşlemi başlat
# simge_durumunu_kontrol_et()





#v2  s başlat q durdur
# import pyautogui
# import time
# import keyboard
# import threading

# # Çalıştırma ve durdurma kontrolü için bir değişken
# calisiyor = False

# def otomatik_gec_onay():
#     global calisiyor
#     while calisiyor:
#         # "geç" komutunu gönder
#         pyautogui.write("geç")
#         pyautogui.press("enter")
        
#         # Bir sonraki döngü için bekleme süresi
#         time.sleep(5)

# # Başlatma ve durdurma fonksiyonları
# def baslat():
#     global calisiyor
#     if not calisiyor:
#         calisiyor = True
#         # Yeni bir thread başlatıyoruz ki ana program kitlenmesin
#         threading.Thread(target=otomatik_gec_onay).start()
#         print("Otomatik geç gönderimi başlatıldı.")

# def durdur():
#     global calisiyor
#     calisiyor = False
#     print("Otomatik geç gönderimi durduruldu.")

# # 's' tuşuna basıldığında başlatır, 'q' tuşuna basıldığında durdurur
# keyboard.add_hotkey('ctrl+alt+s', baslat)
# keyboard.add_hotkey('ctrl+alt+q', durdur)

# # Program sonlanmadan sürekli çalışır durumda kalmasını sağlar
# print("Otomatik geç gönderimi için 's' ile başlat, 'q' ile durdur.")
# keyboard.wait('esc')  # 'esc' tuşuna basıldığında programdan çıkar



#v1
# from operator import ge
# from matplotlib.pylab import get_bit_generator
# import pyautogui
# import time

# def otomatik_gec_yanit():
#     # Belirli bir süre bekleyin, bu sürede ChatGPT onay penceresi açılabilir
#     time.sleep(2)  # Onay penceresinin açılmasını bekleyin
    
#     # "Geç" yazdırın
#     pyautogui.write("geç")
    
#     # Enter tuşuna basarak onay verin
#     pyautogui.press("enter")

# # Döngüyle sürekli kontrol
# while True:
#     # Sürekli kontrol ederek onay penceresi olduğunda otomatik "geç" yanıtı verir
#     otomatik_gec_yanit()
#     time.sleep(5)  # Bu işlemi 5 saniye arayla tekrarlayın
