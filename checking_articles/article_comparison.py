import tkinter as tk
from tkinter import ttk, messagebox
import string

class ArticleComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مقایسه مقالات")
        self.root.geometry("800x900")
        
        # تنظیم فونت و استایل برای نمایش متن فارسی
        self.farsi_font = ('Tahoma', 10)
        self.root.configure(bg='#f0f0f0')
        
        self.create_widgets()
        
    def create_widgets(self):
        # فریم اصلی
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # عنوان
        title_label = ttk.Label(
            main_frame,
            text="سیستم مقایسه مقالات",
            font=('Tahoma', 14, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # ورودی مقاله اول
        ttk.Label(main_frame, text="متن مقاله اول:", font=self.farsi_font).grid(row=1, column=0, pady=5)
        self.article1_text = tk.Text(main_frame, height=10, width=70, font=self.farsi_font)
        self.article1_text.grid(row=2, column=0, columnspan=2, pady=5)
        
        # ورودی مقاله دوم
        ttk.Label(main_frame, text="متن مقاله دوم:", font=self.farsi_font).grid(row=3, column=0, pady=5)
        self.article2_text = tk.Text(main_frame, height=10, width=70, font=self.farsi_font)
        self.article2_text.grid(row=4, column=0, columnspan=2, pady=5)
        
        # دکمه‌ها
        ttk.Button(
            main_frame,
            text="نمایش کلمات مشترک",
            command=self.show_common_words
        ).grid(row=5, column=0, columnspan=2, pady=10)
        
        # فریم جستجوی کلمات منحصر به فرد
        unique_frame = ttk.LabelFrame(main_frame, text="جستجوی کلمات منحصر به فرد", padding="5")
        unique_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        ttk.Label(unique_frame, text="عنوان مقاله (1 یا 2):", font=self.farsi_font).grid(row=0, column=0, padx=5)
        self.article_number = ttk.Entry(unique_frame, width=5)
        self.article_number.grid(row=0, column=1, padx=5)
        
        ttk.Button(
            unique_frame,
            text="نمایش کلمات منحصر به فرد",
            command=self.show_unique_words
        ).grid(row=0, column=2, padx=5)
        
        # نتایج
        ttk.Label(main_frame, text="نتایج:", font=self.farsi_font).grid(row=7, column=0, pady=5)
        self.results_text = tk.Text(main_frame, height=10, width=70, font=self.farsi_font)
        self.results_text.grid(row=8, column=0, columnspan=2, pady=5)
        
    def process_text(self, text):
        # حذف علائم نگارشی و تبدیل به کلمات
        text = text.lower()
        for punct in string.punctuation:
            text = text.replace(punct, ' ')
        return set(text.split())
        
    def show_common_words(self):
        # دریافت متن مقالات
        article1 = self.article1_text.get("1.0", tk.END)
        article2 = self.article2_text.get("1.0", tk.END)
        
        if not article1.strip() or not article2.strip():
            messagebox.showwarning("خطا", "لطفاً متن هر دو مقاله را وارد کنید.")
            return
            
        # پردازش متن‌ها
        words1 = self.process_text(article1)
        words2 = self.process_text(article2)
        
        # یافتن کلمات مشترک
        common_words = words1.intersection(words2)
        
        # نمایش نتایج
        result_text = "کلمات مشترک:\n\n"
        result_text += ", ".join(sorted(common_words))
        result_text += f"\n\nتعداد کلمات مشترک: {len(common_words)}"
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result_text)
        
    def show_unique_words(self):
        article_num = self.article_number.get().strip()
        
        if article_num not in ['1', '2']:
            messagebox.showwarning("خطا", "لطفاً عدد 1 یا 2 را وارد کنید.")
            return
            
        # دریافت متن مقاله‌ها
        article1 = self.article1_text.get("1.0", tk.END)
        article2 = self.article2_text.get("1.0", tk.END)
        
        if not article1.strip() or not article2.strip():
            messagebox.showwarning("خطا", "لطفاً متن هر دو مقاله را وارد کنید.")
            return
            
        # پردازش متن‌ها
        words1 = self.process_text(article1)
        words2 = self.process_text(article2)
        
        # یافتن کلمات منحصر به فرد
        if article_num == '1':
            unique_words = words1 - words2
            article_title = "مقاله اول"
        else:
            unique_words = words2 - words1
            article_title = "مقاله دوم"
            
        # نمایش نتایج
        result_text = f"کلمات منحصر به فرد {article_title}:\n\n"
        result_text += ", ".join(sorted(unique_words))
        result_text += f"\n\nتعداد کلمات منحصر به فرد: {len(unique_words)}"
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result_text)

def main():
    root = tk.Tk()
    app = ArticleComparisonApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 