import tkinter as tk
from tkinter import messagebox

sales = []
customers = []
support_requests = []

class StartScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Ekranı")
        self.root.configure(bg="lightblue")  # Arka plan rengi

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Hoş Geldiniz!", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Giriş türü seçim düğmeleri
        btn_customer_login = tk.Button(root, text="Müşteri Girişi", command=self.customer_login, bg="navy", fg="white")
        btn_customer_login.pack(pady=5)

        btn_admin_login = tk.Button(root, text="Admin Girişi", command=self.admin_login, bg="navy", fg="white")
        btn_admin_login.pack(pady=5)

    def admin_login(self):
        self.root.withdraw()  # Giriş ekranını gizle
        admin_login_screen = tk.Toplevel(self.root)  # Yeni bir ana pencere oluştur
        admin_login_screen.title("Admin Girişi")
        admin_login_screen.configure(bg="lightblue")  # Arka plan rengi
        app = AdminLoginScreen(admin_login_screen)

    def customer_login(self):
        self.root.withdraw()  # Giriş ekranını gizle
        customer_login_screen = tk.Toplevel(self.root)  # Yeni bir ana pencere oluştur
        customer_login_screen.title("Müşteri Girişi")
        customer_login_screen.configure(bg="lightblue")  # Arka plan rengi
        app = CustomerLoginScreen(customer_login_screen)

class CustomerLoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Müşteri Girişi")
        self.root.configure(bg="lightblue")

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Müşteri Girişi", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Müşteri bilgileri giriş alanları
        lbl_name = tk.Label(root, text="Ad:", bg="lightblue", fg="navy")
        lbl_name.pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        lbl_surname = tk.Label(root, text="Soyad:", bg="lightblue", fg="navy")
        lbl_surname.pack(pady=5)
        self.surname_entry = tk.Entry(root)
        self.surname_entry.pack()

        lbl_email = tk.Label(root, text="Email:", bg="lightblue", fg="navy")
        lbl_email.pack(pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        lbl_phone = tk.Label(root, text="Telefon No:", bg="lightblue", fg="navy")
        lbl_phone.pack(pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # "Devam" düğmesi
        btn_continue = tk.Button(root, text="Devam", command=self.show_options, bg="navy", fg="white")
        btn_continue.pack(pady=5)

    def show_options(self):
        # İki yeni seçeneği göster
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Girdi alanlarını temizle
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        # Önceki ekranı gizle
        self.root.withdraw()

        # İki yeni seçenek: Ürünleri görüntüle ve destek talebi
        options_window = tk.Toplevel(self.root)
        options_window.title("Seçenekler")
        options_window.configure(bg="lightblue")

        btn_products = tk.Button(options_window, text="Ürünleri Görüntüle ve Satın Al", command=self.view_products, bg="navy", fg="white")
        btn_products.pack(pady=5)

        btn_support = tk.Button(options_window, text="Destek", command=self.request_support, bg="navy", fg="white")
        btn_support.pack(pady=5)

        btn_back = tk.Button(options_window, text="Geri Dön", command=self.back_to_start, bg="navy", fg="white")
        btn_back.pack(pady=5)

    def view_products(self):
        # Ürünler ekranını göstermek için yeni pencere oluştur
        products_window = tk.Toplevel(self.root)
        products_window.title("Ürünler")
        products_window.configure(bg="lightblue")

        lbl_products_title = tk.Label(products_window, text="Ürünler", font=("Helvetica", 12, "bold"), bg="lightblue", fg="navy")
        lbl_products_title.pack()

        products = {"Bilgisayar": 3000, "Tablet": 1500, "Telefon": 2000}
        for product, price in products.items():
            lbl_product = tk.Label(products_window, text=f"{product}: {price}TL", bg="lightblue", fg="navy")
            lbl_product.pack()

            btn_buy = tk.Button(products_window, text="Satın Al", command=lambda prod=product: self.buy_product(prod), bg="navy", fg="white")
            btn_buy.pack()

    def buy_product(self, product):
        # Müşteri tarafından satın alınan ürünleri kaydet
        sales.append({"Müşteri": f"{self.name_entry.get()} {self.surname_entry.get()}", "Ürün": product})
        messagebox.showinfo("Satın Alma", f"{product} satın alındı.")

    def request_support(self):
        # Destek talebi için yeni pencere oluştur
        support_window = tk.Toplevel(self.root)
        support_window.title("Destek Talebi")
        support_window.configure(bg="lightblue")

        lbl_support = tk.Label(support_window, text="Sorununuzu Açıklayın:", bg="lightblue", fg="navy")
        lbl_support.pack(pady=10)

        self.support_entry = tk.Text(support_window, height=5, width=40)
        self.support_entry.pack(pady=5)

        btn_submit = tk.Button(support_window, text="Gönder", command=self.submit_support, bg="navy", fg="white")
        btn_submit.pack(pady=5)

        btn_back = tk.Button(support_window, text="Geri Dön", command=self.back_to_options, bg="navy", fg="white")
        btn_back.pack(pady=5)

    def submit_support(self):
        # Destek talebini kaydet
        support_text = self.support_entry.get("1.0", tk.END)  # Metin kutusundaki girdiyi al
        support_requests.append({"Müşteri": f"{self.name_entry.get()} {self.surname_entry.get()}", "Talep": support_text})

        # İşlem tamamlandıktan sonra metin kutusunu temizle
        self.support_entry.delete("1.0", tk.END)

    def back_to_start(self):
        self.root.destroy()
        root = tk.Tk()
        root.configure(bg="lightblue")  # Ana pencere arka plan rengi
        app = StartScreen(root)
        root.mainloop()

    def back_to_options(self):
        self.support_entry.delete("1.0", tk.END)
        self.root.deiconify()

class AdminLoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Girişi")
        self.root.configure(bg="lightblue")

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Admin Girişi", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Kullanıcı adı ve şifre giriş alanları
        lbl_username = tk.Label(root, text="Kullanıcı Adı:", bg="lightblue", fg="navy")
        lbl_username.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        lbl_password = tk.Label(root, text="Şifre:", bg="lightblue", fg="navy")
        lbl_password.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Giriş butonu
        btn_login = tk.Button(root, text="Giriş", command=self.login, bg="navy", fg="white")
        btn_login.pack(pady=5)

    def login(self):
        # Kullanıcı adı ve şifreyi al
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Admin kimlik doğrulaması
        if username == "admin" and password == "1234":
            self.root.withdraw()  # Giriş ekranını gizle
            admin_login_screen = tk.Toplevel(self.root)  # Yeni bir ana pencere oluştur
            admin_login_screen.title("Admin Ekranı")
            admin_login_screen.configure(bg="lightblue")  # Arka plan rengi
            app = AdminScreen(admin_login_screen)
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

class AdminScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Ekranı")
        self.root.configure(bg="lightblue")

        # Başlık etiketi
        lbl_title = tk.Label(root, text="Admin Ekranı", font=("Helvetica", 16), bg="lightblue", fg="navy")
        lbl_title.pack(pady=10)

        # Satın alınan ürünlerin ve destek taleplerinin listelerini gösteren seçenekler
        btn_show_sales = tk.Button(root, text="Satın Alınan Ürünler", command=self.show_sales, bg="navy", fg="white")
        btn_show_sales.pack(pady=5)

        btn_show_support = tk.Button(root, text="Destek Talepleri", command=self.show_support_requests, bg="navy", fg="white")
        btn_show_support.pack(pady=5)

        # Geri Dön ve Çıkış düğmeleri
        btn_back = tk.Button(root, text="Geri Dön", command=self.back_to_start, bg="navy", fg="white")
        btn_back.pack(pady=5)

        btn_exit = tk.Button(root, text="Çıkış", command=self.root.quit, bg="navy", fg="white")
        btn_exit.pack(pady=5)

    def show_sales(self):
        # Satın alınan ürünlerin listesi
        sales_window = tk.Toplevel(self.root)
        sales_window.title("Satın Alınan Ürünler")
        sales_window.configure(bg="lightblue")

        lbl_sales_title = tk.Label(sales_window, text="Satın Alınan Ürünler", font=("Helvetica", 12, "bold"), bg="lightblue", fg="navy")
        lbl_sales_title.pack()

        for sale in sales:
            lbl_sale = tk.Label(sales_window, text=f"{sale['Müşteri']} - {sale['Ürün']}", bg="lightblue", fg="navy")
            lbl_sale.pack()

    def show_support_requests(self):
        # Destek taleplerinin listesi
        support_window = tk.Toplevel(self.root)
        support_window.title("Destek Talepleri")
        support_window.configure(bg="lightblue")

        lbl_support_title = tk.Label(support_window, text="Destek Talepleri", font=("Helvetica", 12, "bold"), bg="lightblue", fg="navy")
        lbl_support_title.pack()

        for request in support_requests:
            lbl_request = tk.Label(support_window, text=f"{request['Müşteri']} - {request['Talep']}", bg="lightblue", fg="navy")
            lbl_request.pack()

    def back_to_start(self):
        self.root.destroy()
        root = tk.Tk()
        root.configure(bg="lightblue")  # Ana pencere arka plan rengi
        app = StartScreen(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightblue")  # Ana pencere arka plan rengi
    app = StartScreen(root)

    # Pencere kapatılacağı zaman gerçekleşecek işlemi tanımla
    root.protocol("WM_DELETE_WINDOW", root.quit)

    root.mainloop()
