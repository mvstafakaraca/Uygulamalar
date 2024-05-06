import tkinter as tk
from tkinter import ttk
import random

class Kitap:
    def __init__(self, ad, yazar, yayinevi):
        self.ad = ad
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.yorumlar = []

    def yorum_yap(self, yorum_metni, kullanici):
        yeni_yorum = Yorum(yorum_metni, kullanici)
        self.yorumlar.append(yeni_yorum)

class Kullanici:
    def __init__(self, ad_soyad, tc):
        self.ad_soyad = ad_soyad
        self.tc = tc
        self.okuma_listesi = []

    def kitap_ekle_okuma_listesi(self, kitap):
        self.okuma_listesi.append(kitap)

class Yorum:
    def __init__(self, yorum_metni, kullanici):
        self.yorum_metni = yorum_metni
        self.kullanici = kullanici

class Arayuz:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitap Uygulaması")
        self.okuma_listesi = []  
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Kullanıcı Adı:", background="white", foreground="black").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.kullanici_entry = ttk.Entry(self.root)
        self.kullanici_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(self.root, text="Şifre:", background="white", foreground="black").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.sifre_entry = ttk.Entry(self.root, show="*")
        self.sifre_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        self.devam_btn = ttk.Button(self.root, text="Devam", command=self.devam)
        self.devam_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def devam(self):
        kullanici_adi = self.kullanici_entry.get()
        sifre = self.sifre_entry.get()

        if kullanici_adi == "admin" and sifre == "1234":
            self.root.destroy()  
            root2 = tk.Tk()
            uygulama2 = OkumaListesiArayuz(root2, self.okuma_listesi)
            root2.mainloop()
        else:
            ttk.Label(self.root, text="Hatalı kullanıcı adı veya şifre!", foreground="red").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

class OkumaListesiArayuz:
    def __init__(self, root, okuma_listesi):
        self.root = root
        self.root.title("Okuma Listesi")
        self.okuma_listesi = okuma_listesi
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Okuma Listesi", font=("Helvetica", 14, "bold"), background="white", foreground="black").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.tree = ttk.Treeview(self.root, columns=("Ad", "Yazar", "Yayınevi"), show="headings", height=5)
        self.tree.heading("Ad", text="Ad")
        self.tree.heading("Yazar", text="Yazar")
        self.tree.heading("Yayınevi", text="Yayınevi")
        for kitap in self.okuma_listesi:
            self.tree.insert("", "end", values=(kitap.ad, kitap.yazar, kitap.yayinevi))
        self.tree.grid(row=1, column=0, padx=5, pady=5, sticky="w", columnspan=2)

        ttk.Button(self.root, text="Kitap Ekle", command=self.kitap_ekle, style="my.TButton").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Button(self.root, text="Yorum Yap", command=self.yorum_yap, style="my.TButton").grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Button(self.root, text="Yorumlarım", command=self.yorumlarim, style="my.TButton").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def kitap_ekle(self):
        self.root.destroy()  
        root3 = tk.Tk()
        uygulama3 = KitapEkleArayuz(root3, self.okuma_listesi)
        root3.mainloop()

    def yorum_yap(self):
        self.root.destroy()  
        root4 = tk.Tk()
        uygulama4 = YorumYapArayuz(root4, self.okuma_listesi)
        root4.mainloop()

    def yorumlarim(self):
        # Kullanıcının yaptığı yorumları al ve ayrı bir pencerede göster
        yorumlarim = [yorum for kitap in self.okuma_listesi for yorum in kitap.yorumlar if yorum.kullanici == "Kullanıcı"]
        if yorumlarim:
            self.root.destroy()  
            root5 = tk.Tk()
            uygulama5 = YorumlarimArayuz(root5, yorumlarim)
            root5.mainloop()
        else:
            ttk.Label(self.root, text="Henüz yaptığınız bir yorum bulunmamaktadır.", foreground="red").grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

class KitapEkleArayuz:
    def __init__(self, root, okuma_listesi):
        self.root = root
        self.root.title("Kitap Ekle")
        self.okuma_listesi = okuma_listesi
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Kitap Adı:", background="white", foreground="black").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.kitap_ad_entry = ttk.Combobox(self.root, values=[
            "Dönüşüm", "Suç ve Ceza", "Yeraltından Notlar", "Satranç", "1984", "Hayvan Çiftliği", "Simyacı", 
            "Uçurtma Avcısı", "Yüzyıllık Yalnızlık", "Kumarbaz", "Dava", "Beyaz Diş", "Sineklerin Tanrısı", 
            "Tutunamayanlar", "Sefiller", "Savaş ve Barış", "İlahi Komedya", "Monte Cristo Kontu", "Anna Karenina",
            "Göçebe", "Hamlet", "İlyada", "Othello", "Romeo ve Juliet", "Fareler ve İnsanlar", "Cesur Yeni Dünya",
            "Aylak Adam", "Madame Bovary", "Kumarbaz", "Veba", "Kör Baykuş"])
        self.kitap_ad_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(self.root, text="Yazar:", background="white", foreground="black").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.yazar_combo = ttk.Combobox(self.root, values=[
            "Mehmet Yılmaz", "Ayşe Kaya", "Ahmet Demir", "Fatma Şahin", "Mustafa Aydın", "Emine Arslan",
            "Hasan Çelik", "Zeynep Erdoğan", "Ali Yıldırım", "Hatice Kocaman", "İbrahim Aslan", "Hülya Öztürk",
            "Murat Tekin", "Şerife Tunç", "Yusuf Başaran", "Aysel Kara", "İsmail Doğan", "Gülten Yılmaz",
            "Ahmet Demir", "Ayşe Kaya", "Mehmet Yıldız", "Ayten Arslan", "İsmail Aktaş", "Fatma Gürbüz",
            "Mehmet Ali Karadeniz", "Zeliha Taş", "Selim Çelik", "Sibel Arslan", "Mustafa Kılıç", "Gamze Karagöz"])
        self.yazar_combo.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(self.root, text="Yayınevi:", background="white", foreground="black").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.yayinevi_combo = ttk.Combobox(self.root, values=[
            "Dolma Kalem", "Harper", "Simon ve Sch", "Kese", "Macmillan Yayını", "Skolastik Kor",
            "Pearson Eğitimi", "Springer Doğası", "McGraw", "John W.", "Oxford Üniversitesi", "Cambridge",
            "Blo", "Eller", "Penguen Kitapları", "Rasgele ev", "Penguen", "Vintage Kitap", "Penguen Modern Sınıfı",
            "Faber ve Faber"])
        self.yayinevi_combo.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        ttk.Button(self.root, text="Kitap Ekle", command=self.kitap_ekle, style="my.TButton").grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        ttk.Button(self.root, text="Geri", command=self.geri, style="my.TButton").grid(row=4, column=0, padx=5, pady=5, sticky="w")

    def kitap_ekle(self):
        kitap_ad = self.kitap_ad_entry.get()
        yazar = self.yazar_combo.get()
        yayinevi = self.yayinevi_combo.get()

        yeni_kitap = Kitap(kitap_ad, yazar, yayinevi)
        self.okuma_listesi.append(yeni_kitap)

        self.root.destroy()  
        root2 = tk.Tk()
        uygulama2 = OkumaListesiArayuz(root2, self.okuma_listesi)
        root2.mainloop()

    def geri(self):
        self.root.destroy()  
        root2 = tk.Tk()
        uygulama2 = OkumaListesiArayuz(root2, self.okuma_listesi)
        root2.mainloop()

class YorumYapArayuz:
    def __init__(self, root, okuma_listesi):
        self.root = root
        self.root.title("Yorum Yap")
        self.okuma_listesi = okuma_listesi
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Yorum Yapılacak Kitaplar", font=("Helvetica", 14, "bold"), background="white", foreground="black").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.kitap_combo = ttk.Combobox(self.root, values=[kitap.ad for kitap in self.okuma_listesi])
        self.kitap_combo.grid(row=1, column=0, padx=5, pady=5, sticky="we")

        ttk.Label(self.root, text="Yorumunuzu Yazın:", background="white", foreground="black").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.yorum_entry = tk.Text(self.root, width=50, height=10)
        self.yorum_entry.grid(row=3, column=0, padx=5, pady=5)

        ttk.Button(self.root, text="Yorum Yap", command=self.yorum_yap, style="my.TButton").grid(row=4, column=0, padx=5, pady=5, sticky="we")
        ttk.Button(self.root, text="Geri", command=self.geri, style="my.TButton").grid(row=5, column=0, padx=5, pady=5, sticky="w")

    def yorum_yap(self):
        yorum = self.yorum_entry.get("1.0", tk.END).strip()

        if yorum:
            secilen_kitap_ad = self.kitap_combo.get()
            secilen_kitap = next((kitap for kitap in self.okuma_listesi if kitap.ad == secilen_kitap_ad), None)

            if secilen_kitap:
                secilen_kitap.yorum_yap(yorum, "Kullanıcı")

                self.root.destroy()  
                root2 = tk.Tk()
                uygulama2 = OkumaListesiArayuz(root2, self.okuma_listesi)
                root2.mainloop()
        else:
            ttk.Label(self.root, text="Yorum alanı boş bırakılamaz!", foreground="red").grid(row=6, column=0, padx=5, pady=5, sticky="we")

    def geri(self):
        self.root.destroy()  
        root2 = tk.Tk()
        uygulama2 = OkumaListesiArayuz(root2, self.okuma_listesi)
        root2.mainloop()

class YorumlarimArayuz:
    def __init__(self, root, yorumlarim):
        self.root = root
        self.root.title("Yorumlarım")
        self.yorumlarim = yorumlarim
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg="white")
        ttk.Label(self.root, text="Yaptığınız Yorumlar", font=("Helvetica", 14, "bold"), background="white", foreground="black").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.yorumlarim_liste = tk.Text(self.root, width=50, height=10)
        self.yorumlarim_liste.grid(row=1, column=0, padx=5, pady=5)

        for yorum in self.yorumlarim:
            self.yorumlarim_liste.insert(tk.END, f"- {yorum.yorum_metni}\n\n")

        ttk.Button(self.root, text="Geri", command=self.geri, style="my.TButton").grid(row=2, column=0, padx=5, pady=5, sticky="w")

    def geri(self):
        self.root.destroy()  

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="white")
    style = ttk.Style(root)
    style.configure("my.TButton", foreground="white", background="blue", font=("Helvetica", 10, "bold"))
    uygulama = Arayuz(root)
    root.mainloop()
