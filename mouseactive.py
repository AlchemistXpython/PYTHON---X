import pyautogui
import time

def mouse_hareketi():
    global is_running
    while is_running:
        # Mouse'u biraz hareket ettir
        x, y = pyautogui.position()  # Mevcut pozisyonu al
        pyautogui.moveTo(x + 1, y)  # 1 piksel sağa hareket ettir
        pyautogui.moveTo(x, y)  # Orijinal pozisyona geri dön
        time.sleep(10)  # 10 saniyede bir hareket ettir
