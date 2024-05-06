import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restoran Sipariş Yönetim Sistemi")

        # Veritabanı bağlantısı
        self.connection = sqlite3.connect("restaurant.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

        # Stil ayarları
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("Title.TLabel", font=("Helvetica", 18, "bold"))
        self.style.configure("Treeview", font=("Helvetica", 11))
        self.style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        # Renkler
        self.bg_color = "#f2f2f2"  # Arka plan rengi
        self.highlight_bg_color = "#d9d9d9"  # Vurgulanan arka plan rengi
        self.highlight_fg_color = "#000000"  # Vurgulanan metin rengi

        # Ana pencere
        self.root.config(bg=self.bg_color)

        # Başlık
        title_label = ttk.Label(root, text="Restoran Sipariş Yönetim Sistemi", style="Title.TLabel", background=self.bg_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Menü listesi
        menu_frame = ttk.LabelFrame(root, text="Menü", padding=10)
        menu_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.menu_listbox = tk.Listbox(menu_frame, height=10, width=30)
        self.menu_listbox.pack(pady=5)

        # Sepet
        order_frame = ttk.LabelFrame(root, text="Sepet", padding=10)
        order_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.order_text = tk.Text(order_frame, height=10, width=50)
        self.order_text.pack(pady=5)

        # Müşteri bilgileri
        customer_frame = ttk.LabelFrame(root, text="Müşteri Bilgileri", padding=10)
        customer_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        customer_name_label = ttk.Label(customer_frame, text="Müşteri Adı:", background=self.bg_color)
        customer_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.customer_name_entry = ttk.Entry(customer_frame)
        self.customer_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        address_label = ttk.Label(customer_frame, text="Adres:", background=self.bg_color)
        address_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.address_entry = ttk.Entry(customer_frame)
        self.address_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Sipariş işlemleri
        button_frame = ttk.Frame(root, padding=10)
        button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        add_to_cart_button = ttk.Button(button_frame, text="Sepete Ekle", command=self.add_to_cart, style="TButton")
        add_to_cart_button.grid(row=0, column=0, padx=5, pady=5)

        place_order_button = ttk.Button(button_frame, text="Siparişi Tamamla", command=self.place_order, style="TButton")
        place_order_button.grid(row=0, column=1, padx=5, pady=5)

        add_product_button = ttk.Button(button_frame, text="Ürün Ekle", command=self.add_product, style="TButton")
        add_product_button.grid(row=1, column=0, padx=5, pady=5)

        update_stock_button = ttk.Button(button_frame, text="Stok Güncelle", command=self.update_stock, style="TButton")
        update_stock_button.grid(row=1, column=1, padx=5, pady=5)

        # Siparişleri görüntüleme işlemleri
        order_view_frame = ttk.LabelFrame(root, text="Siparişleri Görüntüle", padding=10)
        order_view_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.orders_treeview = ttk.Treeview(order_view_frame, columns=("Customer Name", "Address", "Items", "Status"), style="Treeview")
        self.orders_treeview.heading("#0", text="Order ID")
        self.orders_treeview.heading("Customer Name", text="Müşteri Adı")
        self.orders_treeview.heading("Address", text="Adres")
        self.orders_treeview.heading("Items", text="Sipariş Detayları")
        self.orders_treeview.heading("Status", text="Durum")
        self.orders_treeview.column("#0", width=50)
        self.orders_treeview.column("Customer Name", width=150)
        self.orders_treeview.column("Address", width=150)
        self.orders_treeview.column("Items", width=300)
        self.orders_treeview.column("Status", width=100)
        self.orders_treeview.pack(fill="both", expand=True)

        self.populate_orders_treeview()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS menu (
                                id INTEGER PRIMARY KEY,
                                item TEXT NOT NULL,
                                price REAL NOT NULL,
                                stock INTEGER NOT NULL
                                )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                                id INTEGER PRIMARY KEY,
                                customer_name TEXT NOT NULL,
                                address TEXT NOT NULL,
                                items TEXT NOT NULL,
                                status TEXT NOT NULL
                                )""")
        self.connection.commit()

    def add_to_cart(self):
        selected_item = self.menu_listbox.get(tk.ACTIVE)
        self.order_text.insert(tk.END, selected_item + "\n")

    def place_order(self):
        customer_name = self.customer_name_entry.get()
        address = self.address_entry.get()
        order_items = self.order_text.get("1.0", tk.END)

        # Siparişi veritabanına ekle
        self.cursor.execute("INSERT INTO orders (customer_name, address, items, status) VALUES (?, ?, ?, ?)",
                            (customer_name, address, order_items, "Hazırlanıyor"))
        self.connection.commit()

        # Sipariş formunu temizle
        self.order_text.delete("1.0", tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        # Sipariş tamamlandı mesajı göster
        self.show_order_confirmation(customer_name, address, order_items)

        # Sipariş listesini güncelle
        self.populate_orders_treeview()

    def show_order_confirmation(self, customer_name, address, order_items):
        confirmation_window = tk.Toplevel()
        confirmation_window.title("Sipariş Tamamlandı")
        confirmation_window.configure(bg=self.bg_color)

        confirmation_label = ttk.Label(confirmation_window, text="Sipariş Tamamlandı!", font=("Helvetica", 16, "bold"), background=self.bg_color)
        confirmation_label.grid(row=0, column=0, columnspan=2, pady=10)

        info_label = ttk.Label(confirmation_window, text=f"Müşteri Adı: {customer_name}\nAdres: {address}\n\nSipariş Detayları:\n{order_items}", background=self.bg_color)
        info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ok_button = ttk.Button(confirmation_window, text="Tamam", command=confirmation_window.destroy, style="TButton")
        ok_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_product(self):
        add_product_window = tk.Toplevel()
        add_product_window.title("Ürün Ekle")
        add_product_window.configure(bg=self.bg_color)

        name_label = ttk.Label(add_product_window, text="Ürün Adı:", background=self.bg_color)
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.product_name_entry = ttk.Entry(add_product_window)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)

        price_label = ttk.Label(add_product_window, text="Fiyat:", background=self.bg_color)
        price_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.price_entry = ttk.Entry(add_product_window)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        stock_label = ttk.Label(add_product_window, text="Stok:", background=self.bg_color)
        stock_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.stock_entry = ttk.Entry(add_product_window)
        self.stock_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = ttk.Button(add_product_window, text="Ekle", command=self.add_product_to_menu, style="TButton")
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_product_to_menu(self):
        name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())

        self.cursor.execute("INSERT INTO menu (item, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        self.connection.commit()
        self.refresh_menu()
        messagebox.showinfo("Başarılı", "Ürün başarıyla eklendi.")

    def update_stock(self):
        selected_item = self.menu_listbox.get(tk.ACTIVE)
        selected_item_id = selected_item.split(" - ")[0]

        update_stock_window = tk.Toplevel()
        update_stock_window.title("Stok Güncelle")
        update_stock_window.configure(bg=self.bg_color)

        stock_label = ttk.Label(update_stock_window, text="Yeni Stok Değeri:", background=self.bg_color)
        stock_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.new_stock_entry = ttk.Entry(update_stock_window)
        self.new_stock_entry.grid(row=0, column=1, padx=5, pady=5)

        update_button = ttk.Button(update_stock_window, text="Güncelle", command=lambda: self.update_stock_in_db(selected_item_id), style="TButton")
        update_button.grid(row=1, column=0, columnspan=2, pady=10)

    def update_stock_in_db(self, item_id):
        new_stock = int(self.new_stock_entry.get())
        self.cursor.execute("UPDATE menu SET stock = ? WHERE id = ?", (new_stock, item_id))
        self.connection.commit()
        self.refresh_menu()
        messagebox.showinfo("Başarılı", "Stok başarıyla güncellendi.")

    def refresh_menu(self):
        self.menu_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM menu")
        menu_items = self.cursor.fetchall()
        for item in menu_items:
            self.menu_listbox.insert(tk.END, f"{item[0]} - {item[1]} - {item[2]} TL - Stok: {item[3]}")

    def populate_orders_treeview(self):
        # Mevcut siparişleri temizle
        for record in self.orders_treeview.get_children():
            self.orders_treeview.delete(record)

        # Veritabanından siparişleri al
        self.cursor.execute("SELECT * FROM orders")
        orders = self.cursor.fetchall()

        # Siparişleri treeview'e ekle
        for order in orders:
            self.orders_treeview.insert("", tk.END, text=order[0], values=(order[1], order[2], order[3], order[4]))

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
