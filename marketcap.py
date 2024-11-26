import requests
import pandas as pd
from tkinter import Tk, Label, Entry, Button, Listbox, messagebox, Frame, Toplevel
from openpyxl import load_workbook
import logging

# Logging ayarları
logging.basicConfig(filename="crypto_app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Coin listesi
coin_list = []
excel_file = "crypto_data_marketcap.xlsx"

# CoinMarketCap API Ayarları
API_KEY = "YOUR_COINMARKETCAP_API_KEY"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}
base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

def add_coin():
    """Coin ismini listeye ekler."""
    coin_name = entry.get().strip().lower()
    if not coin_name:
        messagebox.showwarning("Uyarı", "Lütfen bir coin ismi girin.")
        return

    if coin_name in coin_list:
        messagebox.showwarning("Uyarı", "Bu coin zaten listede mevcut.")
        return

    coin_list.append(coin_name)
    coin_listbox.insert("end", coin_name)
    entry.delete(0, "end")
    logging.info(f"Coin eklendi: {coin_name}")

def fetch_crypto_data():
    """Listedeki coinler için veri çeker ve Excel'e yazar."""
    if not coin_list:
        messagebox.showwarning("Uyarı", "Önce coin ekleyin.")
        return

    formatted_data = []
    current_date = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")  # Tarih ve saat

    for coin in coin_list:
        params = {"symbol": coin.upper(), "convert": "USD"}
        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if "data" not in data or coin.upper() not in data["data"]:
                messagebox.showwarning("Uyarı", f"{coin} için geçerli veri alınamadı.")
                logging.warning(f"{coin} için geçerli veri alınamadı.")
                continue

            coin_data = data["data"][coin.upper()]
            usd_data = coin_data["quote"]["USD"]

            formatted_data.append({
                "Tarih": current_date,
                "Coin": coin_data["name"],
                "Fiyat (USD)": f'${usd_data["price"]:.6f}',
                "Değişim (24h)": f'{usd_data["percent_change_24h"]:.2f}%',
                "Hacim (24h)": f'${usd_data["volume_24h"]:,}',
                "Piyasa Değeri (USD)": f'${usd_data["market_cap"]:,}'
            })

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Hata", f"{coin} için API hatası: {e}")
            logging.error(f"{coin} için API hatası: {e}")
            continue

    if not formatted_data:
        return

    df = pd.DataFrame(formatted_data)
    logging.info(f"İşlenen veri: {df}")

    # Excel'e veri yazma
    try:
        with pd.ExcelWriter(excel_file, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            sheet = writer.sheets.get("Sheet1", None)
            startrow = sheet.max_row if sheet else 0
            if startrow == 0:  # Başlıkları yalnızca bir kez yaz
                df.to_excel(writer, sheet_name="Sheet1", index=False)
            else:
                df.to_excel(writer, sheet_name="Sheet1", index=False, header=False, startrow=startrow)
            messagebox.showinfo("Başarılı", "Veriler başarıyla Excel dosyasına eklendi.")
            logging.info("Veriler Excel dosyasına başarıyla yazıldı.")
    except FileNotFoundError:
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)
        messagebox.showinfo("Başarılı", "Yeni bir Excel dosyası oluşturuldu ve veriler yazıldı.")
        logging.info("Yeni Excel dosyası oluşturuldu ve veriler yazıldı.")

def clear_list():
    """Coin listesini temizler."""
    coin_list.clear()
    coin_listbox.delete(0, "end")
    logging.info("Coin listesi temizlendi.")

# GUI oluşturma
root = Tk()
root.title("Kripto Veri Çekme (MarketCap)")
root.geometry("400x650")

Label(root, text="Coin İsmini Gir ve Ekle:").pack(pady=5)
entry = Entry(root, width=40)
entry.pack(pady=5)

Button(root, text="Ekle", command=add_coin).pack(pady=5)

Label(root, text="Eklenen Coinler:").pack(pady=10)
coin_listbox = Listbox(root, width=50, height=15)
coin_listbox.pack(pady=5)

# Button'ları ortalamak için Frame kullanalım
button_frame = Frame(root)
button_frame.pack(pady=20)

Button(button_frame, text="Veri Çek ve Sheet1'e Yaz", command=fetch_crypto_data).pack(side="left", padx=5)

Button(root, text="Listeyi Temizle", command=clear_list).pack(pady=5)

root.mainloop()
