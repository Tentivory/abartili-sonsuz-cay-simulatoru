#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Sonsuz Çay Demleme Simülatörü
Bu kod gerçekten çalışır. Çay demlenir... ama asla bitmez.
Her çalıştırmada yeni bir bahane üretir.
"""

import time
import random

bahaneler = [
    "Su henüz kaynamadı, çaydanlık inatçı çıktı.",
    "Çay bitmiş, markete gitmem lazım ama dışarı çok soğuk.",
    "Anne geldi, çayı o demleyecekmiş. Bekle.",
    "Şeker bitti. Tatlı çay olmaz.",
    "Misafir geldi, önce onlara ikram edeceğiz.",
    "Elektrik kesildi. Çaydanlık sessiz sedasız.",
    "Çay demleniyor... demleniyor... demleniyor... (sonsuzluk modu aktif)",
    "Fincan yok. Bardak da yok. Ne içeceğiz?",
    "Çay saati geçti, artık kahve saati ama biz inatçıyız.",
    "Kayyum atandı çaydanlığa. Onay bekleniyor."
]

def demle_cay():
    print("🍵 Çay demleme işlemi başlatıldı...")
    time.sleep(2)
    print("Su ısıtılıyor...")
    time.sleep(3)
    
    while True:  # Sonsuz döngü - asla bitmez
        bahane = random.choice(bahaneler)
        print(f"⏳ {bahane}")
        bekleme = random.randint(1, 5)
        time.sleep(bekleme)
        print("Devam ediyor... (veya etmiyor)")
        time.sleep(1)

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        print("\n🚫 Çay demleme durduruldu. Ama çay hâlâ demleniyor (hayalinde).")
        print("\n--- DAMGA ---")
        print("İmza: Kayyum Grok")
        print("Tarih: 22 Ekim 2026")
        print("Durum: Ciddi ama değil. Çay önemli.")
        print("Gizli not: Her şey kontrol altında, kayyum onayladı.")
