import tkinter as tk
from tkinter import filedialog
import os

class StudentLoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Öğrenci Giriş Ekranı")
        self.root.geometry("300x200")
        self.root.configure(bg="#f0f0f0")

        self.student_id = None

        # Öğrenci numarası girişi için etiket ve giriş kutusu
        self.label_student_id = tk.Label(root, text="Öğrenci Numarası:", bg="#f0f0f0")
        self.label_student_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_student_id = tk.Entry(root, width=20)
        self.entry_student_id.grid(row=0, column=1, padx=5, pady=5)

        # Şifre girişi için etiket ve giriş kutusu
        self.label_password = tk.Label(root, text="Şifre:", bg="#f0f0f0")
        self.label_password.grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(root, show="*", width=20)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Giriş butonu
        self.login_button = tk.Button(root, text="Giriş", bg="#2196f3", fg="white", width=25, command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def login(self):
        # Giriş butonuna her tıklamada ana arayüze geçiş yap
        self.student_id = self.entry_student_id.get()
        self.root.destroy()
        main_window = tk.Tk()
        app = MainWindow(main_window, self.student_id)
        main_window.mainloop()

class MainWindow:
    def __init__(self, root, student_id):
        self.root = root
        self.student_id = student_id
        self.root.title("Ana Arayüz")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.material_window = MaterialWindow()
        self.student_window = StudentInfoWindow(self.student_id)
        self.course_window = CourseInfoWindow()

        self.upload_material_button = tk.Button(root, text="Materyal Yükle", bg="#2196f3", fg="white", width=25, command=self.material_window.open_window)
        self.upload_material_button.pack(padx=10, pady=10)

        self.student_button = tk.Button(root, text="Öğrenci Bilgisi", bg="#ff9800", fg="white", width=25, command=self.student_window.open_window)
        self.student_button.pack(padx=10, pady=10)

        self.course_button = tk.Button(root, text="Ders Bilgisi", bg="#4caf50", fg="white", width=25, command=self.course_window.show_courses)
        self.course_button.pack(padx=10, pady=10)

class MaterialWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Materyal Yükleme")
        self.window.geometry("400x400")
        self.window.configure(bg="#f0f0f0")
        self.window.withdraw()  # Pencereyi gizle

        # Materyal adı girişi için etiket ve giriş kutusu
        self.label_material_name = tk.Label(self.window, text="Materyal Adı:", bg="#f0f0f0")
        self.label_material_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_material_name = tk.Entry(self.window, width=30)
        self.entry_material_name.grid(row=0, column=1, padx=5, pady=5)

        # Dosya seçme butonu
        self.select_file_button = tk.Button(self.window, text="Dosya Seç", bg="#2196f3", fg="white", width=25, command=self.select_file)
        self.select_file_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Materyal listesi için etiket
        self.label_material_list = tk.Label(self.window, text="Yüklenen Materyaller", bg="#f0f0f0")
        self.label_material_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Materyal listesi
        self.material_listbox = tk.Listbox(self.window, width=50, height=10)
        self.material_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.material_listbox.bind("<Double-Button-1>", self.open_material)

    def select_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Dosya Seç", filetypes=(("Text Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")))
        if filename:
            material_name = os.path.basename(filename)
            self.entry_material_name.delete(0, tk.END)
            self.entry_material_name.insert(0, material_name)
            self.material_listbox.insert(tk.END, material_name)

    def open_material(self, event):
        selected_index = self.material_listbox.curselection()
        if selected_index:
            selected_material = self.material_listbox.get(selected_index)
            os.system(f'start {selected_material}')

    def open_window(self):
        self.window.deiconify()  # Pencereyi görünür yap

    def update_data(self):
        pass

class StudentInfoWindow:
    def __init__(self, student_id):
        self.window = tk.Toplevel()
        self.student_id = student_id
        self.window.title("Öğrenci Bilgi Arayüzü")
        self.window.geometry("300x200")
        self.window.configure(bg="#ffffff")  # Beyaz arka plan rengi
        self.window.withdraw()  # Pencereyi gizle

        # Öğrenci bilgileri için etiketler
        self.label_title = tk.Label(self.window, text="Öğrenci Bilgileri", bg="#ffffff", fg="#333333", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.frame = tk.Frame(self.window, bg="#ffffff")
        self.frame.pack(padx=20, pady=5)

        self.label_student_id = tk.Label(self.frame, text=f"Öğrenci Numarası: {self.student_id}", bg="#ffffff", fg="#333333")
        self.label_student_id.grid(row=0, column=0, sticky="w")

        self.label_student_name = tk.Label(self.frame, text="Öğrenci Adı: John Doe", bg="#ffffff", fg="#333333")
        self.label_student_name.grid(row=1, column=0, sticky="w")

        self.label_attendance = tk.Label(self.frame, text="Ders Katılımı: Katıldı", bg="#ffffff", fg="#333333")
        self.label_attendance.grid(row=2, column=0, sticky="w")

        # Geri dönme butonu
        self.back_button = tk.Button(self.window, text="Geri Dön", bg="#f44336", fg="white", width=10, command=self.close_window)
        self.back_button.pack(pady=10)

    def open_window(self):
        self.window.deiconify()  # Pencereyi görünür yap

    def close_window(self):
        self.window.withdraw()  # Pencereyi gizle

class CourseInfoWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Ders Bilgi Arayüzü")
        self.window.geometry("300x200")
        self.window.configure(bg="#f0f0f0")
        self.window.withdraw()

    def show_courses(self):
        course_info_window = tk.Toplevel(self.window)
        course_info_window.title("Ders Bilgileri")
        course_info_window.geometry("300x300")
        course_info_window.configure(bg="#f0f0f0")

        courses = {
            "Matematik": {"Öğretmen": "Ahmet", "İçerik": "Sayılar ve İşlem Bilgisi"},
            "Fizik": {"Öğretmen": "Mehmet", "İçerik": "Kuvvet ve Hareket"},
            "Kimya": {"Öğretmen": "Ayşe", "İçerik": "Atom ve Molekül Yapısı"}
        }

        course_listbox = tk.Listbox(course_info_window, width=50, height=10)
        course_listbox.pack(padx=10, pady=10)

        def show_course_info(event):
            selected_course = course_listbox.get(course_listbox.curselection())
            info_window = tk.Toplevel(course_info_window)
            info_window.title(selected_course)
            info_window.geometry("300x200")
            info_window.configure(bg="#f0f0f0")

            course_info = courses[selected_course]

            label_course_name = tk.Label(info_window, text=f"Ders Adı: {selected_course}", bg="#f0f0f0")
            label_course_name.pack(padx=10, pady=5, anchor="w")

            label_course_content = tk.Label(info_window, text=f"Ders İçeriği: {course_info['İçerik']}", bg="#f0f0f0")
            label_course_content.pack(padx=10, pady=5, anchor="w")

            label_course_teacher = tk.Label(info_window, text=f"Öğretmen: {course_info['Öğretmen']}", bg="#f0f0f0")
            label_course_teacher.pack(padx=10, pady=5, anchor="w")

            def ask_question():
                question_window = tk.Toplevel(info_window)
                question_window.title("Soru Sor")
                question_window.geometry("300x200")
                question_window.configure(bg="#f0f0f0")

                label_teacher_name = tk.Label(question_window, text=f"Öğretmen: {course_info['Öğretmen']}", bg="#f0f0f0")
                label_teacher_name.pack(padx=10, pady=5, anchor="w")

                entry_question = tk.Entry(question_window, width=30)
                entry_question.pack(padx=10, pady=5)

                def send_question():
                    sent_label = tk.Label(question_window, text="Soru başarıyla öğretmene ulaştırıldı", bg="#f0f0f0")
                    sent_label.pack(padx=10, pady=5)

                send_button = tk.Button(question_window, text="Soru Gönder", bg="#2196f3", fg="white", command=send_question)
                send_button.pack(padx=10, pady=5)

            ask_question_button = tk.Button(info_window, text="Soru Sor", bg="#2196f3", fg="white", command=ask_question)
            ask_question_button.pack(padx=10, pady=5)

            back_button = tk.Button(info_window, text="Geri Dön", bg="#f44336", fg="white", command=info_window.destroy)
            back_button.pack(padx=10, pady=5)

        for course in courses.keys():
            course_listbox.insert(tk.END, course)

        course_listbox.bind("<Double-Button-1>", show_course_info)

# Öğrenci giriş ekranını başlat
root = tk.Tk()
login_window = StudentLoginWindow(root)
root.mainloop()
