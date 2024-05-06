import tkinter as tk
from tkinter import messagebox

user_database = {
    "admin": "admin123"
}

recipe_list = [
    {
        "name": "Mercimek Çorbası",
        "ingredients": "Mercimek, su, soğan, havuç, tuz, karabiber",
        "quantity": "1 su bardağı mercimek\n1 adet soğan\n1 adet havuç\n",
        "preparation": "1. Mercimek, soğan ve havucu doğrayın.\n2. Tencereye su ekleyin ve kaynatın.\n3. Doğranmış sebzeleri ekleyin ve pişirin.\n4. Baharatlarını ekleyin ve blender ile püre haline getirin."
    },
    {
        "name": "Mantarlı Pilav",
        "ingredients": "Pirinç, mantar, su, tuz, sıvı yağ",
        "quantity": "2 su bardağı pirinç\n200 gr mantar\n",
        "preparation": "1. Pirinci yıkayın ve süzün.\n2. Mantarları doğrayın.\n3. Tencereye sıvı yağ koyun ve mantarları kavurun.\n4. Pirinci ekleyin ve kavurun.\n5. Üzerine su ekleyin ve pişirin."
    },
    {
        "name": "Fırında Tavuk",
        "ingredients": "Tavuk but, baharatlar, zeytinyağı",
        "quantity": "4 adet tavuk but\nKarabiber, tuz, kekik\n",
        "preparation": "1. Tavuk butlarını yıkayın ve baharatlayın.\n2. Fırın tepsisine yerleştirin.\n3. Üzerlerine zeytinyağı gezdirin.\n4. Önceden ısıtılmış fırında pişirin."
    }
]

review_list = {
    "Mercimek Çorbası": "Çok lezzetli bir çorba, tekrar yapacağım.",
    "Mantarlı Pilav": "Harika bir pilav, yanında çok güzel gitti.",
    "Fırında Tavuk": "Tavuklar biraz kuru oldu, daha fazla sos eklemek gerekiyor gibi."
}

def handle_login():
    username = login_username.get()
    password = login_password.get()
    
    if username in user_database and user_database[username] == password:
        open_new_tab()
        root.withdraw()  
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")
    
    login_username.delete(0, tk.END)
    login_password.delete(0, tk.END)

def open_new_tab():
    if is_logged_in():
        tab_window = tk.Toplevel()
        tab_window.title("Yemek Tarifi")
        
        tab_window.attributes('-fullscreen', True)
        
        def exit_application():
            root.destroy()

        exit_btn = tk.Button(tab_window, text="Çıkış", command=exit_application, font=("Helvetica", 14), bg="#FF5733", fg="white")
        exit_btn.pack(side=tk.BOTTOM, pady=5)

        recipes_btn = tk.Button(tab_window, text="Tarifler", command=show_recipes, font=("Helvetica", 14), bg="#3498DB", fg="white")
        recipes_btn.pack(pady=5)
        
        add_recipe_btn = tk.Button(tab_window, text="Tarif Ekle", command=add_recipe_window, font=("Helvetica", 14), bg="#27AE60", fg="white")
        add_recipe_btn.pack(pady=5)
        
        search_recipe_btn = tk.Button(tab_window, text="Tarif Ara", command=search_recipe, font=("Helvetica", 14), bg="#F4D03F", fg="black")
        search_recipe_btn.pack(pady=5)
        
        reviews_btn = tk.Button(tab_window, text="Değerlendirmeler", command=show_reviews, font=("Helvetica", 14), bg="#8E44AD", fg="white")
        reviews_btn.pack(pady=5)
        
        add_review_btn = tk.Button(tab_window, text="Değerlendirme Ekle", command=add_review, font=("Helvetica", 14), bg="#F39C12", fg="black")
        add_review_btn.pack(pady=5)
    else:
        messagebox.showerror("Hata", "Önce giriş yapmalısınız!")

def is_logged_in():
    username = login_username.get()
    password = login_password.get()
    
    return username in user_database and user_database[username] == password

def add_recipe_window():
    add_recipe_window = tk.Toplevel()
    add_recipe_window.title("Tarif Ekle")
    
    recipe_name_label = tk.Label(add_recipe_window, text="Tarif Adı:", font=("Helvetica", 14), bg="#3498DB", fg="white")
    recipe_name_label.pack()
    recipe_name_entry = tk.Entry(add_recipe_window)
    recipe_name_entry.pack()
    
    ingredients_label = tk.Label(add_recipe_window, text="Malzemeler:", font=("Helvetica", 14), bg="#3498DB", fg="white")
    ingredients_label.pack()
    ingredients_entry = tk.Text(add_recipe_window, width=30, height=5)
    ingredients_entry.pack()
    
    ingredient_quantity_label = tk.Label(add_recipe_window, text="Malzeme Miktarı:", font=("Helvetica", 14), bg="#3498DB", fg="white")
    ingredient_quantity_label.pack()
    ingredient_quantity_entry = tk.Entry(add_recipe_window)
    ingredient_quantity_entry.pack()
    
    preparation_label = tk.Label(add_recipe_window, text="Hazırlanışı:", font=("Helvetica", 14), bg="#3498DB", fg="white")
    preparation_label.pack()
    preparation_entry = tk.Text(add_recipe_window, width=30, height=5)
    preparation_entry.pack()
    
    add_recipe_button = tk.Button(add_recipe_window, text="Tarif Ekle", command=lambda: save_recipe(
        recipe_name_entry.get(),
        ingredients_entry.get("1.0", tk.END),
        ingredient_quantity_entry.get(),
        preparation_entry.get("1.0", tk.END),
        add_recipe_window
    ), font=("Helvetica", 14), bg="#27AE60", fg="white")
    add_recipe_button.pack()

def save_recipe(name, ingredients, quantity, preparation, add_recipe_window):
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "quantity": quantity,
        "preparation": preparation
    }
    recipe_list.append(recipe)
    messagebox.showinfo("Tarif Ekle", "Tarif başarıyla kaydedildi.")
    add_recipe_window.destroy()  
def add_review():
    add_review_window = tk.Toplevel()
    add_review_window.title("Değerlendirme Ekle")
    
    recipe_name_label = tk.Label(add_review_window, text="Tarif Adı:", font=("Helvetica", 14), bg="#8E44AD", fg="white")
    recipe_name_label.pack()
    recipe_name_entry = tk.Entry(add_review_window)
    recipe_name_entry.pack()
    
    review_label = tk.Label(add_review_window, text="Değerlendirme:", font=("Helvetica", 14), bg="#8E44AD", fg="white")
    review_label.pack()
    review_entry = tk.Text(add_review_window, width=30, height=5)
    review_entry.pack()
    
    add_review_button = tk.Button(add_review_window, text="Değerlendirme Ekle", command=lambda: save_review(
        recipe_name_entry.get(),
        review_entry.get("1.0", tk.END),
        add_review_window
    ), font=("Helvetica", 14), bg="#F39C12", fg="black")
    add_review_button.pack()

def save_review(recipe_name, review_text, add_review_window):
    if recipe_name in review_list:
        review_list[recipe_name] = review_list[recipe_name] + "\n" + review_text.strip()
    else:
        review_list[recipe_name] = review_text.strip()
    messagebox.showinfo("Değerlendirme Ekle", "Değerlendirme başarıyla kaydedildi.")
    add_review_window.destroy()  
def search_recipe():
    search_recipe_window = tk.Toplevel()
    search_recipe_window.title("Tarif Ara")

    recipe_name_label = tk.Label(search_recipe_window, text="Tarif Adı:", font=("Helvetica", 14), bg="#F4D03F", fg="black")
    recipe_name_label.pack()
    recipe_name_entry = tk.Entry(search_recipe_window)
    recipe_name_entry.pack()

    def search():
        name = recipe_name_entry.get()
        found_recipe = None
        for recipe in recipe_list:
            if recipe['name'] == name:
                found_recipe = recipe
                break
        if found_recipe:
            messagebox.showinfo("Tarif Bulundu", f"Tarif Adı: {found_recipe['name']}\n"
                                                 f"Malzemeler: {found_recipe['ingredients']}\n"
                                                 f"Malzeme Miktarı: {found_recipe['quantity']}\n"
                                                 f"Hazırlanışı: {found_recipe['preparation']}")
        else:
            messagebox.showinfo("Tarif Bulunamadı", "Girdiğiniz isme uygun bir tarif bulunamadı.")
        search_recipe_window.destroy()  
    search_btn = tk.Button(search_recipe_window, text="Ara", command=search, font=("Helvetica", 14), bg="#F4D03F", fg="black")
    search_btn.pack()

def show_reviews():
    review_info = ""
    for recipe_name, review_text in review_list.items():
        review_info += f"{recipe_name}: {review_text}\n\n"
    if review_info:
        messagebox.showinfo("Tarif Değerlendirmeleri", review_info.strip())
    else:
        messagebox.showinfo("Tarif Değerlendirmeleri", "Henüz hiç değerlendirme yapılmamış.")

def show_recipes():
    recipe_info = ""
    for recipe in recipe_list:
        recipe_info += f"Tarif Adı: {recipe['name']}\n"
        recipe_info += f"Malzemeler: {recipe['ingredients']}\n"
        recipe_info += f"Malzeme Miktarı: {recipe['quantity']}\n"
        recipe_info += f"Hazırlanışı: {recipe['preparation']}\n\n"
    if recipe_info:
        messagebox.showinfo("Tarifler", recipe_info.strip())
    else:
        messagebox.showinfo("Tarifler", "Henüz hiç tarif eklenmedi.")

def register():
    username = reg_username.get()
    password = reg_password.get()
    
    if username and password:
        user_database[username] = password
        messagebox.showinfo("Başarılı", "Kayıt işlemi başarıyla tamamlandı.")
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre boş olamaz!")
    
    reg_username.delete(0, tk.END)
    reg_password.delete(0, tk.END)

root = tk.Tk()
root.title("Kullanıcı Girişi")
root.configure(bg="#7D3C98")

root.attributes('-fullscreen', True)

register_frame = tk.Frame(root, bg="#7D3C98")
register_frame.pack(pady=10)

reg_username_label = tk.Label(register_frame, text="Kullanıcı Adı:", bg="#7D3C98", fg="white")  
reg_username_label.grid(row=0, column=0)
reg_username = tk.Entry(register_frame)
reg_username.grid(row=0, column=1)

reg_password_label = tk.Label(register_frame, text="Şifre:", bg="#7D3C98", fg="white")  
reg_password_label.grid(row=1, column=0)
reg_password = tk.Entry(register_frame, show="*")
reg_password.grid(row=1, column=1)

register_btn = tk.Button(register_frame, text="Kayıt Ol", command=register, bg="#FF5733", fg="white") 
register_btn.grid(row=2, columnspan=2, pady=10)

login_frame = tk.Frame(root, bg="#7D3C98")
login_frame.pack(pady=10)

login_username_label = tk.Label(login_frame, text="Kullanıcı Adı:", bg="#7D3C98", fg="white")  
login_username_label.grid(row=0, column=0)
login_username = tk.Entry(login_frame)
login_username.grid(row=0, column=1)

login_password_label = tk.Label(login_frame, text="Şifre:", bg="#7D3C98", fg="white")  
login_password_label.grid(row=1, column=0)
login_password = tk.Entry(login_frame, show="*")
login_password.grid(row=1, column=1)

login_btn = tk.Button(login_frame, text="Giriş Yap", command=handle_login, bg="#FF5733", fg="white")  
login_btn.grid(row=2, columnspan=2, pady=10)

root.mainloop()
