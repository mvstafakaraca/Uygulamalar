import tkinter as tk
from tkinter import ttk, simpledialog

class Seyahat:
    def __init__(self):
        self.rotalar = []
        self.konaklamalar = []
        self.ucak_biletleri = []

    def rota_ekle(self, rota):
        self.rotalar.append(rota)

    def konaklama_sec(self, konaklama):
        self.konaklamalar.append(konaklama)

    def ucak_bileti_ekle(self, bilet):
        self.ucak_biletleri.append(bilet)

    def plan_duzenle(self):
        # Seyahat planını düzenle
        pass

class Konaklama:
    def __init__(self, isim, fiyat_araligi):
        self.isim = isim
        self.fiyat_araligi = fiyat_araligi

class Rota:
    def __init__(self, detaylar):
        self.detaylar = detaylar

class UcakBileti:
    def __init__(self, havayolu, fiyat):
        self.havayolu = havayolu
        self.fiyat = fiyat

class SeyahatPlanlamaUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Seyahat Planlama Uygulaması")

        # Stil oluştur
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#e6f7ff")  # Açık mavi renk
        self.style.configure("TLabel", background="#e6f7ff", foreground="red", font=('Arial', 12, 'bold'))

        self.seyahat = Seyahat()
        self.kisi_sayisi = 0
        self.kisiler = []
        self.toplam_fiyat = 0

        self.create_kisi_bilgileri_ekranı()

    def create_kisi_bilgileri_ekranı(self):
        self.kisi_bilgileri_frame = ttk.Frame(self.root, style="TFrame")
        self.kisi_bilgileri_frame.pack(padx=10, pady=10)

        ttk.Label(self.kisi_bilgileri_frame, text="Kişi Bilgileri", style="TLabel").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.kisi_sayisi_label = ttk.Label(self.kisi_bilgileri_frame, text="Kaç kişi seyahat edecek?", style="TLabel")
        self.kisi_sayisi_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.kisi_sayisi_combobox = ttk.Combobox(self.kisi_bilgileri_frame, values=[1, 2, 3, 4, 5, 6])
        self.kisi_sayisi_combobox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.devam_button = ttk.Button(self.kisi_bilgileri_frame, text="Devam", command=self.kisi_sayisini_onayla)
        self.devam_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def kisi_sayisini_onayla(self):
        self.kisi_sayisi = int(self.kisi_sayisi_combobox.get())
        self.kisi_bilgileri_frame.destroy()
        self.kisi_bilgilerini_al()

    def kisi_bilgilerini_al(self):
        self.kisiler = []

        for i in range(self.kisi_sayisi):
            # Kişi bilgilerini tek seferde al
            isim_soyisim_yas = simpledialog.askstring(
                "Kişi Bilgileri",
                f"Lütfen {i+1}. kişinin ad, soyad ve yaşını girin (örn: Ahmet Yılmaz 30):"
            )

            if isim_soyisim_yas is None:
                self.root.destroy()  # Kullanıcı iptal etti, uygulamayı kapat
                return

            isim_soyisim_yas = isim_soyisim_yas.split()
            isim, soyisim, yas = isim_soyisim_yas if len(isim_soyisim_yas) == 3 else ["Bilgi Yok", "Bilgi Yok", 0]  # Eğer bilgi eksikse varsayılan değerler
            yas = int(yas)
            self.kisiler.append((isim, soyisim, yas))

            # Öğrenci ve tam fiyat seçeneklerini sormak için bir alt pencere oluştur
            ogrenci_tam_fiyat_penceresi = tk.Toplevel(self.root)
            ogrenci_tam_fiyat_penceresi.title("Öğrenci ve Tam Fiyat Seçimi")

            # Seçenekleri tutmak için değişkenler
            ogrenci_variable = tk.BooleanVar(value=False)
            tam_fiyat_variable = tk.BooleanVar(value=False)

            # Eğer kişi 18 yaşından küçükse öğrenci seçeneğini aktif et
            if yas < 18:
                ogrenci_variable.set(True)

            # Etiketler ve seçim kutuları oluştur
            ttk.Label(ogrenci_tam_fiyat_penceresi, text="Öğrenci Fiyatı").grid(row=0, column=0, padx=5, pady=5)
            ogrenci_checkbox = ttk.Checkbutton(ogrenci_tam_fiyat_penceresi, variable=ogrenci_variable, state='disabled' if yas >= 18 else 'normal')
            ogrenci_checkbox.grid(row=0, column=1, padx=5, pady=5)
            ttk.Label(ogrenci_tam_fiyat_penceresi, text="Tam Fiyat").grid(row=1, column=0, padx=5, pady=5)
            ttk.Checkbutton(ogrenci_tam_fiyat_penceresi, variable=tam_fiyat_variable).grid(row=1, column=1, padx=5, pady=5)

            # Devam butonu
            ttk.Button(
                ogrenci_tam_fiyat_penceresi,
                text="Devam",
                command=lambda: self.ogrenci_tam_fiyat_secildi(ogrenci_variable, tam_fiyat_variable, ogrenci_tam_fiyat_penceresi)
            ).grid(row=2, columnspan=2, padx=5, pady=5)

            # Öğrenci ve tam fiyat seçeneklerinin belirgin olması için ana pencereyi dondur
            self.root.wait_window(ogrenci_tam_fiyat_penceresi)

    def ogrenci_tam_fiyat_secildi(self, ogrenci_variable, tam_fiyat_variable, ogrenci_tam_fiyat_penceresi):
        # Öğrenci ve tam fiyat seçeneklerini kaydet
        ogrenci_mi = ogrenci_variable.get()
        tam_fiyat_mi = tam_fiyat_variable.get()

        # Kullanıcı seçimini tuple'a ekleyelim
        self.kisiler[-1] += (ogrenci_mi, tam_fiyat_mi)

        # Alt pencereyi kapat
        ogrenci_tam_fiyat_penceresi.destroy()

        # Eğer tüm kişilerin bilgileri alındıysa, rota seçim sekmesini göster
        if len(self.kisiler) == self.kisi_sayisi:
            self.rota_sekmesini_goster()

    def rota_sekmesini_goster(self):
        # Rota seçim sekmesini göster
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.rota_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.rota_frame, text="Rota Seç")

        ttk.Label(self.rota_frame, text="Rota Seç", style="TLabel").pack()
        rota_secenekler = ["İstanbul İzmir", "İstanbul Ankara", "İstanbul Balıkesir"]
        self.rota_variable = tk.StringVar(value=rota_secenekler[0])  # Varsayılan olarak ilk seçeneği seç

        for rota in rota_secenekler:
            tk.Radiobutton(self.rota_frame, text=rota, variable=self.rota_variable, value=rota, command=self.konaklama_sekmesini_goster).pack()

    def konaklama_sekmesini_goster(self):
        secilen_rota = self.rota_variable.get()

        # Eğer varsa eski konaklama sekmesini sil
        if hasattr(self, "konaklama_frame"):
            self.konaklama_frame.destroy()

        # Eğer Balıkesir veya Ankara seçildiyse, konaklama seçim sekmesini gösterme
        if secilen_rota in ["İstanbul Balıkesir", "İstanbul Ankara"]:
            return

        # Yeni konaklama seçim sekmesini oluştur
        self.konaklama_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.konaklama_frame, text="Konaklama Seç")

        ttk.Label(self.konaklama_frame, text="Konaklama Seç", style="TLabel").pack()

        if secilen_rota == "İstanbul İzmir":
            konaklama_secenekleri = ["Lüks bir otelde suit oda (1000TL-4000TL)", "Orta seviye bir otelde standart oda (300TL-1200TL)", "Daha ekonomik bir otelde standart oda (150TL-600TL)"]
        else:
            konaklama_secenekleri = []

        self.konaklama_variable = tk.StringVar(value=konaklama_secenekleri[0])  # Varsayılan olarak ilk seçeneği seç

        for secenek in konaklama_secenekleri:
            tk.Radiobutton(self.konaklama_frame, text=secenek, variable=self.konaklama_variable, value=secenek, command=self.otel_fiyatlari_goster).pack()

    def otel_fiyatlari_goster(self):
        secilen_konaklama = self.konaklama_variable.get()

        # Eğer varsa eski otel fiyatları sekmesini sil
        if hasattr(self, "otel_fiyatlari_frame"):
            self.otel_fiyatlari_frame.destroy()

        # Yeni otel fiyatları sekmesini oluştur
        self.otel_fiyatlari_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.otel_fiyatlari_frame, text="Otel Fiyatları")

        ttk.Label(self.otel_fiyatlari_frame, text="Otel Fiyatları", style="TLabel").pack()

        # Balıkesir ve İzmir'e özel oteller ve fiyatlar
        otel_fiyatlari = {}
        if secilen_konaklama.startswith("Lüks bir otelde suit oda"):
            otel_fiyatlari = {
                "Ayvalık Palas Hotel": 2500,
                "Altınoluk Hotel": 2000,
                "Burhaniye Hotel": 1800,
                "Edremit Resort": 3000
            }
        elif secilen_konaklama.startswith("Orta seviye bir otelde standart oda"):
            otel_fiyatlari = {
                "Ayvalık Palas Hotel": 1000,
                "Altınoluk Hotel": 800,
                "Burhaniye Hotel": 700,
                "Edremit Resort": 1200
            }
        elif secilen_konaklama.startswith("Daha ekonomik bir otelde standart oda"):
            otel_fiyatlari = {
                "Ayvalık Palas Hotel": 500,
                "Altınoluk Hotel": 400,
                "Burhaniye Hotel": 300,
                "Edremit Resort": 600
            }

        self.secilen_otel_fiyati = tk.IntVar()  # Seçilen otel fiyatını tutacak değişken

        for otel, fiyat in otel_fiyatlari.items():
            tk.Radiobutton(self.otel_fiyatlari_frame, text=f"{otel} - {fiyat} TL", variable=self.secilen_otel_fiyati, value=fiyat, command=self.toplam_fiyati_guncelle).pack()

        # Eğer uçak bileti seçme ekranı daha önce açılmadıysa aç
        if not hasattr(self, "ucak_bileti_acildi"):
            self.ucak_bileti_acildi = False
        if not self.ucak_bileti_acildi:
            self.ucak_biletleri_goster()

    def ucak_biletleri_goster(self):
        # Uçak bileti fiyatları sekmesi
        self.ucak_biletleri_frame = ttk.Frame(self.notebook, style="TFrame")
        self.notebook.add(self.ucak_biletleri_frame, text="Uçak Bileti Seç")

        ttk.Label(self.ucak_biletleri_frame, text="Uçak Bileti Seç", style="TLabel").pack()

        # Uçak biletlerini göster
        ucak_bilet_fiyatlari = {
            "Türk Hava Yolları": 900,
            "Pegasus Havayolları": 750,
            "AnadoluJet": 600
        }

        self.secilen_ucak_bileti_fiyati = tk.IntVar()  # Seçilen uçak bileti fiyatını tutacak değişken

        for havayolu, fiyat in ucak_bilet_fiyatlari.items():
            tk.Radiobutton(self.ucak_biletleri_frame, text=f"{havayolu} - {fiyat} TL", variable=self.secilen_ucak_bileti_fiyati, value=fiyat, command=self.toplam_fiyati_guncelle).pack()

        self.ucak_bileti_acildi = True

    def toplam_fiyati_guncelle(self):
        # Seçilen uçak biletinin ve otelin fiyatlarını al
        ucak_bileti_fiyati = self.secilen_ucak_bileti_fiyati.get()
        otel_fiyati = self.secilen_otel_fiyati.get()

        # Toplam fiyatı hesapla
        self.toplam_fiyat = (ucak_bileti_fiyati + otel_fiyati) * self.kisi_sayisi

        # Eğer varsa eski toplam fiyat etiketini sil
        if hasattr(self, "toplam_fiyat_label"):
            self.toplam_fiyat_label.destroy()

        # Yeni toplam fiyat etiketini oluştur
        self.toplam_fiyat_label = ttk.Label(self.root, text=f"Toplam Fiyat: {self.toplam_fiyat} TL", style="TLabel")
        self.toplam_fiyat_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = SeyahatPlanlamaUygulamasi(root)
    root.mainloop()
