import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class Product:
    def __init__(self, name, stock_quantity):
        self.name = name
        self.stock_quantity = stock_quantity
    
    def update_stock(self, quantity):
        # Stok güncellemek için gerekli işlemler
        self.stock_quantity += quantity

    def sell_product(self, quantity):
        # Ürün satışı işlemleri
        if quantity > self.stock_quantity:
            return False  # Stoktan fazla satış yapmaya çalışıldığında False döndür
        else:
            self.stock_quantity -= quantity
            return True

    def remove_stock(self, quantity):
        # Stoktan miktar düşme işlemi
        if quantity > self.stock_quantity:
            return False  # Stoktan fazla düşürme yapmaya çalışıldığında False döndür
        else:
            self.stock_quantity -= quantity
            return True

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ürün Yönetim Sistemi")
        self.geometry("600x500")
        self.products = {}  # Eklenen ürünleri ve adetlerini tutmak için bir sözlük
        self.order_counter = 1  # Sipariş numarası sayacı
        self.configure(background="#2C3E50")  # Arka plan rengini ayarla
        self.create_widgets()

    def create_widgets(self):
        # Başlık etiketi
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self, text="Ürün Yönetim Sistemi", font=title_font, bg="#2C3E50", fg="#FFFFFF")
        self.title_label.pack(pady=10)

        # Ürün adı etiketi ve giriş kutusu
        self.product_name_label = tk.Label(self, text="Ürün Adı:", bg="#2C3E50", fg="#FFFFFF")
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.pack()

        # Miktar etiketi ve giriş kutusu
        self.quantity_label = tk.Label(self, text="Miktar:", bg="#2C3E50", fg="#FFFFFF")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        # Ürün ekleme, satış ve stok silme düğmeleri
        self.button_frame = tk.Frame(self, bg="#2C3E50")
        self.button_frame.pack(pady=10)

        self.add_product_button = tk.Button(self.button_frame, text="Ürün Ekle", command=self.add_product, bg="#16A085", fg="#000000", padx=10, pady=5)
        self.add_product_button.grid(row=0, column=0, padx=5)

        self.sell_product_button = tk.Button(self.button_frame, text="Ürün Sat", command=self.sell_product, bg="#E74C3C", fg="#000000", padx=10, pady=5)
        self.sell_product_button.grid(row=0, column=1, padx=5)

        self.remove_stock_button = tk.Button(self.button_frame, text="Stok Sil", command=self.remove_stock, bg="#3498DB", fg="#000000", padx=10, pady=5)
        self.remove_stock_button.grid(row=0, column=2, padx=5)

        # Sipariş geçmişi başlığı
        self.history_label = tk.Label(self, text="Sipariş Geçmişi", bg="#2C3E50", fg="#FFFFFF")
        self.history_label.pack(pady=10)

        # Sipariş geçmişi listesi
        self.history_listbox = tk.Listbox(self, width=50, bg="#34495E", fg="#FFFFFF")
        self.history_listbox.pack()

        # Stok bilgisi başlığı
        self.stock_label = tk.Label(self, text="Stok Bilgisi", bg="#2C3E50", fg="#FFFFFF")
        self.stock_label.pack(pady=10)

        # Stok bilgisi listesi
        self.stock_listbox = tk.Listbox(self, width=50, bg="#34495E", fg="#FFFFFF")
        self.stock_listbox.pack()

    def add_product(self):
        # Ürün ekleme işlevi
        product_name = self.product_name_entry.get()
        quantity_str = self.quantity_entry.get()

        if not product_name or not quantity_str:
            messagebox.showerror("Hata", "Ürün adı ve miktar alanları boş olamaz!")
            return

        quantity = int(quantity_str)

        if product_name in self.products:
            # Ürün zaten eklenmişse, stok miktarını güncelle
            self.products[product_name].update_stock(quantity)
        else:
            # Yeni ürün eklenirse, sözlüğe ekleyin
            self.products[product_name] = Product(product_name, quantity)
        
        self.update_product_list()

    def sell_product(self):
        # Ürün satışı işlevi
        product_name = self.product_name_entry.get()
        quantity_str = self.quantity_entry.get()

        if not product_name or not quantity_str:
            messagebox.showerror("Hata", "Ürün adı ve miktar alanları boş olamaz!")
            return

        quantity = int(quantity_str)

        if product_name in self.products:
            product = self.products[product_name]
            if product.sell_product(quantity):
                messagebox.showinfo("Başarılı", f"{quantity} adet {product_name} satıldı!")
                self.update_history(product_name, quantity)
            else:
                messagebox.showerror("Hata", f"Stokta yeterli miktarda {product_name} bulunmamaktadır!")
        else:
            messagebox.showerror("Hata", f"{product_name} adında bir ürün bulunamadı!")

        self.update_product_list()

    def remove_stock(self):
        # Stok silme işlevi
        product_name = self.product_name_entry.get()
        quantity_str = self.quantity_entry.get()

        if not product_name or not quantity_str:
            messagebox.showerror("Hata", "Ürün adı ve miktar alanları boş olamaz!")
            return

        quantity = int(quantity_str)

        if product_name in self.products:
            product = self.products[product_name]
            if product.remove_stock(quantity):
                messagebox.showinfo("Başarılı", f"{quantity} adet {product_name} stoktan düşürüldü.")
            else:
                messagebox.showerror("Hata", f"Stokta yeterli miktarda {product_name} bulunmamaktadır!")
        else:
            messagebox.showerror("Hata", f"{product_name} adında bir ürün bulunamadı!")

        self.update_product_list()

    def update_product_list(self):
        # Eklenen ürünlerin listesini güncelle
        self.stock_listbox.delete(0, tk.END)  # Stok listesini temizle
        for product_name, product in self.products.items():
            self.stock_listbox.insert(tk.END, f"{product_name}: {product.stock_quantity}")

    def update_history(self, product_name, quantity):
        # Sipariş geçmişini güncelle
        self.history_listbox.insert(tk.END, f"Sipariş No: {self.order_counter}, Ürün: {product_name}, Miktar: {quantity}")
        self.order_counter += 1

if __name__ == "__main__":
    app = Application()
    app.mainloop()
