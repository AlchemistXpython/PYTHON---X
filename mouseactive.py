#v4 tuş kombinasyonu---------------------------------------------------------------------------------------------------------------------

import pyautogui
import time

def prevent_screen_saver(interval):
    try:
        while True:
            # Mevcut fare konumunu al
            current_position = pyautogui.position()

            # Fareyi hareket ettir (bir adım sağa ve eski yerine)
            pyautogui.moveTo(current_position[0] + 1, current_position[1])
            pyautogui.moveTo(current_position[0], current_position[1])

            # Klavye girişi simüle et (örneğin 'Shift' tuşuna bas)
            pyautogui.press('shift')

            # Belirtilen süre kadar bekle (2 dakika)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından durduruldu.")

# 2 dakika (120 saniye) interval ile çalıştır
prevent_screen_saver(120)



#v3---------------------------------------------------------------------------------------------------------------------------------------

# import pyautogui
# import time

# def move_mouse_periodically(interval):
#     try:
#         while True:
#             # Mevcut fare konumunu al
#             current_position = pyautogui.position()

#             # Fareyi bir adım sağa hareket ettir ve eski yerine getir
#             pyautogui.moveTo(current_position[0] + 1, current_position[1])
#             pyautogui.moveTo(current_position[0], current_position[1])

#             # Belirtilen süre kadar bekle (2 dakika)
#             time.sleep(interval)
#     except KeyboardInterrupt:
#         print("\nİşlem kullanıcı tarafından durduruldu.")

# # 2 dakika (120 saniye) interval ile çalıştır
# move_mouse_periodically(120)



#v2---------------------------------------------------------------------------------------------------------------------------------------

# import pyautogui
# import time
# import threading

# # Global değişken
# is_running = False

# def mouse_hareketi():
#     global is_running
#     while is_running:
#         # Mevcut pozisyonu al
#         x, y = pyautogui.position()  
#         # Mouse'u biraz hareket ettir
#         pyautogui.moveTo(x + 1, y)  # 1 piksel sağa hareket ettir
#         time.sleep(1)  # Her 1 saniyede bir hareket ettir
#         pyautogui.moveTo(x, y)  # Mouse'u orijinal pozisyona geri döndür

# def start_mouse_movement():
#     global is_running
#     is_running = True
#     thread = threading.Thread(target=mouse_hareketi)
#     thread.start()

# def stop_mouse_movement():
#     global is_running
#     is_running = False

# # Test için basit bir arayüz
# if __name__ == "__main__":
#     print("Mouse hareketini başlatmak için 'start' yazın, durdurmak için 'stop' yazın.")
#     while True:
#         command = input().strip().lower()
#         if command == "start":
#             start_mouse_movement()
#             print("Mouse hareketi başlatıldı.")
#         elif command == "stop":
#             stop_mouse_movement()
#             print("Mouse hareketi durduruldu.")
#         elif command == "exit":
#             stop_mouse_movement()  # Durdurulmuşsa çık
#             break
#         else:
#             print("Geçersiz komut. Lütfen 'start', 'stop' veya 'exit' yazın.")




# import pyautogui
# import time
# import threading

# # Global değişken
# is_running = False

# def mouse_hareketi():
#     global is_running
#     while is_running:
#         # Mouse'u biraz hareket ettir
#         x, y = pyautogui.position()  # Mevcut pozisyonu al
#         pyautogui.moveTo(x + 1, y)  # 1 piksel sağa hareket ettir
#         time.sleep(10)  # 10 saniyede bir hareket ettir

# def start_mouse_movement():
#     global is_running
#     is_running = True
#     thread = threading.Thread(target=mouse_hareketi)
#     thread.start()

# def stop_mouse_movement():
#     global is_running
#     is_running = False

# # Test için basit bir arayüz
# if __name__ == "__main__":
#     print("Mouse hareketini başlatmak için 'start' yazın, durdurmak için 'stop' yazın.")
#     while True:
#         command = input().strip().lower()
#         if command == "start":
#             start_mouse_movement()
#             print("Mouse hareketi başlatıldı.")
#         elif command == "stop":
#             stop_mouse_movement()
#             print("Mouse hareketi durduruldu.")
#         elif command == "exit":
#             break
#         else:
#             print("Geçersiz komut. Lütfen 'start', 'stop' veya 'exit' yazın.")
