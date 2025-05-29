from tkinter import *

# Create main window
window = Tk()
window.title("Article Comparison")
window.geometry("800x600")

# Create text areas for articles
label1 = Label(window, text="First Article:")
label1.pack(pady=5)

text1 = Text(window, height=8, width=60)
text1.pack(pady=5)

label2 = Label(window, text="Second Article:")
label2.pack(pady=5)

text2 = Text(window, height=8, width=60)
text2.pack(pady=5)

# Create result area
result_text = Text(window, height=8, width=60)
result_text.pack(pady=10)

def find_common_words():
    # Get text from both articles
    article1 = text1.get("1.0", END)
    article2 = text2.get("1.0", END)
    
    # Convert to sets of words
    words1 = set(article1.split())
    words2 = set(article2.split())
    
    # Find common words
    common = words1 & words2
    
    # Show results
    result_text.delete("1.0", END)
    result_text.insert("1.0", f"Common words: {len(common)}\n\n")
    result_text.insert(END, " ".join(common))

def find_unique_words():
    # Get article number
    article_num = article_entry.get()
    if article_num not in ['1', '2']:
        return
        
    # Get text from both articles
    article1 = text1.get("1.0", END)
    article2 = text2.get("1.0", END)
    
    # Convert to sets of words
    words1 = set(article1.split())
    words2 = set(article2.split())
    
    # Find unique words
    if article_num == '1':
        unique = words1 - words2
        article = "First"
    else:
        unique = words2 - words1
        article = "Second"
        
    # Show results
    result_text.delete("1.0", END)
    result_text.insert("1.0", f"Unique words in {article} article: {len(unique)}\n\n")
    result_text.insert(END, " ".join(unique))

# Create buttons and entry
common_btn = Button(window, text="Show Common Words", command=find_common_words)
common_btn.pack(pady=5)

select_frame = Frame(window)
select_frame.pack(pady=5)

article_label = Label(select_frame, text="Article Number (1 or 2):")
article_label.pack(side=LEFT, padx=5)

article_entry = Entry(select_frame, width=5)
article_entry.pack(side=LEFT, padx=5)

unique_btn = Button(select_frame, text="Show Unique Words", command=find_unique_words)
unique_btn.pack(side=LEFT, padx=5)

# Start the application
window.mainloop() 