import tkinter as tk
from tkinter import messagebox, simpledialog


class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Ekranı")
        self.root.configure(bg="lightblue")  # Arka plan rengi

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Lütfen Giriş Yapınız", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Admin girişi butonu
        btn_admin_login = tk.Button(root, text="Admin Girişi", command=self.admin_login, bg="navy", fg="white")
        btn_admin_login.pack(side=tk.LEFT, padx=10, pady=5)

        # Müşteri girişi butonu
        btn_customer_login = tk.Button(root, text="Müşteri Girişi", command=self.customer_login, bg="navy", fg="white")
        btn_customer_login.pack(side=tk.RIGHT, padx=10, pady=5)

    def admin_login(self):
        self.root.destroy()  # Giriş ekranını kapat
        admin_password = "1234"
        input_password = simpledialog.askstring("Admin Girişi", "Lütfen şifreyi girin:", show='*')
        if input_password == admin_password:
            self.open_admin_screen()
        else:
            messagebox.showerror("Hata", "Geçersiz şifre!")

    def open_admin_screen(self):
        root = tk.Tk()
        app = MusicShopApp(root)
        root.mainloop()

    def customer_login(self):
        self.root.destroy()  # Giriş ekranını kapat
        # Müşteri girişi için kullanıcı bilgilerini isteyen ekranı aç
        while True:
            customer_info = self.get_customer_info()
            if customer_info:
                name, surname, tc = customer_info
                root = tk.Tk()
                app = CustomerScreen(root, name, surname, tc)
                root.mainloop()
                break

    def get_customer_info(self):
        name = simpledialog.askstring("Müşteri Girişi", "Ad:")
        if name is None:
            return None
        surname = simpledialog.askstring("Müşteri Girişi", "Soyad:")
        if surname is None:
            return None
        while True:
            tc = simpledialog.askstring("Müşteri Girişi", "TC No:")
            if tc is None:
                return None
            if len(tc) == 11:
                break
            else:
                messagebox.showerror("Hata", "Geçerli TC Kimlik Numarası girin.")
        return name, surname, tc


class MusicShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Müzik Enstrümanı Dükkanı Yönetimi")
        self.root.configure(bg="lightblue")  # Arka plan rengi
        self.current_stocks = {"gitar": 10, "piyano": 5, "davul": 3, "keman": 8}

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Müzik Enstrümanı Dükkanı Yönetimi", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Enstrüman ekle butonu
        btn_add_instrument = tk.Button(root, text="Enstrüman Ekle", command=self.add_instrument_window, bg="navy", fg="white")
        btn_add_instrument.pack(pady=5)

        # Satış yap butonu
        btn_make_sale = tk.Button(root, text="Satış Yap", command=self.make_sale_window, bg="navy", fg="white")
        btn_make_sale.pack(pady=5)

        # Mevcut stoklar sekmesi
        self.current_stock_tab = tk.Frame(root, bd=1, relief=tk.SUNKEN, bg="lightblue")
        self.current_stock_tab.pack(pady=10, padx=5, fill=tk.BOTH, expand=True)
        self.populate_current_stocks()

    def populate_current_stocks(self):
        for widget in self.current_stock_tab.winfo_children():
            widget.destroy()

        lbl_current_stock = tk.Label(self.current_stock_tab, text="Mevcut Stoklar", font=("Helvetica", 12, "bold"), bg="lightblue", fg="navy")
        lbl_current_stock.pack()

        for instrument, stock in self.current_stocks.items():
            lbl_instrument_stock = tk.Label(self.current_stock_tab, text=f"{instrument.capitalize()}: {stock}", bg="lightblue", fg="navy")
            lbl_instrument_stock.pack()

    def add_instrument_window(self):
        self.add_window = tk.Toplevel()
        self.add_window.title("Enstrüman Ekle")

        # Etiketler ve giriş kutuları oluştur
        lbl_instrument = tk.Label(self.add_window, text="Enstrüman:")
        lbl_instrument.grid(row=0, column=0, padx=10, pady=5)
        self.instrument_entry = tk.Entry(self.add_window)
        self.instrument_entry.grid(row=0, column=1, padx=10, pady=5)

        lbl_quantity = tk.Label(self.add_window, text="Adet:")
        lbl_quantity.grid(row=1, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        btn_add = tk.Button(self.add_window, text="Ekle", command=self.add_instrument)
        btn_add.grid(row=2, columnspan=2, padx=10, pady=5)

    def add_instrument(self):
        instrument_name = self.instrument_entry.get().lower()  # Küçük harfe dönüştür
        quantity = int(self.quantity_entry.get())

        # Enstrüman ekleme işlemleri
        if instrument_name in self.current_stocks:
            self.current_stocks[instrument_name] += quantity
        else:
            self.current_stocks[instrument_name] = quantity

        # Başarılı ekleme mesajı
        messagebox.showinfo("Başarılı", f"{quantity} adet {instrument_name} başarıyla eklendi. Mevcut stok: {self.current_stocks[instrument_name]}")

        # İşlemler tamamlandıktan sonra pencereyi kapat
        self.add_window.destroy()

        # Mevcut stokları güncelle
        self.populate_current_stocks()

    def make_sale_window(self):
        self.sale_window = tk.Toplevel()
        self.sale_window.title("Satış Yap")

        # Satılacak enstrümanları seçmek için bir açılır menü oluştur
        lbl_select_instrument = tk.Label(self.sale_window, text="Satılacak Enstrüman:")
        lbl_select_instrument.grid(row=0, column=0, padx=10, pady=5)
        self.selected_instrument = tk.StringVar()
        self.selected_instrument.set("Gitar")  # Varsayılan olarak Gitar seçili
        instruments = list(self.current_stocks.keys())  # Güncellenmiş enstrüman listesi
        self.sale_window_instrument_menu = tk.OptionMenu(self.sale_window, self.selected_instrument, *instruments)
        self.sale_window_instrument_menu.grid(row=0, column=1, padx=10, pady=5)

        # Satılacak adet için bir giriş kutusu oluştur
        lbl_quantity = tk.Label(self.sale_window, text="Adet:")
        lbl_quantity.grid(row=1, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.sale_window)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        btn_sell = tk.Button(self.sale_window, text="Satış Yap", command=self.make_sale)
        btn_sell.grid(row=2, columnspan=2, padx=10, pady=5)

    def make_sale(self):
        instrument_name = self.selected_instrument.get().lower()  # Küçük harfe dönüştür
        quantity = int(self.quantity_entry.get())

        # Satış işlemleri
        if instrument_name in self.current_stocks:
            if self.current_stocks[instrument_name] >= quantity:
                self.current_stocks[instrument_name] -= quantity
                messagebox.showinfo("Başarılı", f"{quantity} adet {instrument_name} başarıyla satıldı. Mevcut stok: {self.current_stocks[instrument_name]}")
            else:
                messagebox.showerror("Hata", f"Stokta yeterli {instrument_name} bulunmamaktadır.")
        else:
            messagebox.showerror("Hata", f"{instrument_name} stokta bulunmamaktadır.")

        # İşlemler tamamlandıktan sonra pencereyi kapat
        self.sale_window.destroy()

        # Mevcut stokları güncelle
        self.populate_current_stocks()


class CustomerScreen:
    def __init__(self, root, name, surname, tc):
        self.root = root
        self.root.title("Müşteri Ekranı")
        self.root.configure(bg="lightblue")  # Arka plan rengi

        self.customer_name = name
        self.customer_surname = surname
        self.customer_tc = tc

        # Başlık etiketi
        lbl_title = tk.Label(self.root, text=f"Hoş Geldiniz, {self.customer_name}!", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Siparişler, Enstrümanlar, Destek Talebi Oluştur seçenekleri
        btn_show_orders = tk.Button(self.root, text="Sipariş Geçmişi", command=self.show_orders, bg="navy", fg="white")
        btn_show_orders.pack(pady=5)

        btn_show_instruments = tk.Button(self.root, text="Enstrümanlar", command=self.show_instruments, bg="navy", fg="white")
        btn_show_instruments.pack(pady=5)

        btn_create_support_request = tk.Button(self.root, text="Destek Talebi Oluştur", command=self.create_support_request, bg="navy", fg="white")
        btn_create_support_request.pack(pady=5)

        btn_back = tk.Button(self.root, text="Dön", command=self.back_to_login, bg="navy", fg="white")
        btn_back.pack(side=tk.LEFT, padx=10, pady=5)

        btn_exit = tk.Button(self.root, text="Çıkış", command=self.exit_app, bg="navy", fg="white")
        btn_exit.pack(side=tk.RIGHT, padx=10, pady=5)

    def back_to_login(self):
        self.root.destroy()  # Müşteri ekranını kapat
        root = tk.Tk()
        app = LoginScreen(root)
        root.mainloop()

    def exit_app(self):
        self.root.destroy()  # Uygulamayı kapat

    def show_orders(self):
        # Sipariş geçmişi ekranını göster
        orders = {"Gitar": 1, "Piyano": 2, "Davul": 1}  # Örnek sipariş geçmişi
        order_list = "\n".join([f"{instrument}: {quantity} adet" for instrument, quantity in orders.items()])
        messagebox.showinfo("Sipariş Geçmişi", f"Siparişleriniz:\n{order_list}")

    def show_instruments(self):
        instruments = {"Gitar": 500, "Piyano": 2000, "Davul": 300, "Keman": 400}
        self.instrument_window = tk.Toplevel()
        self.instrument_window.title("Enstrümanlar")

        for idx, (instrument, price) in enumerate(instruments.items()):
            lbl_instrument = tk.Label(self.instrument_window, text=f"{instrument}: {price}TL", bg="lightblue", fg="navy")
            lbl_instrument.grid(row=idx, column=0, padx=10, pady=5)

            btn_buy = tk.Button(self.instrument_window, text="Satın Al", command=lambda inst=instrument, prc=price: self.buy_instrument(inst, prc), bg="navy", fg="white")
            btn_buy.grid(row=idx, column=1, padx=10, pady=5)

    def buy_instrument(self, instrument, price):
        messagebox.showinfo("Satın Alma", f"{instrument} satın alındı.")
        # Sipariş geçmişi ekranında gösterilebilir

    def create_support_request(self):
        message = simpledialog.askstring("Destek Talebi Oluştur", "Destek talebinizi yazın:")
        if message:
            messagebox.showinfo("Destek Talebi", "Destek talebiniz gönderildi. Teşekkür ederiz.")
            # Admin ekranında görüntülenebilir


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()