import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator, exceptions

# Initialize Main Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x500")
root.config(bg="#f0f2f5")

# Supported languages dictionary
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Arabic": "ar",
    "Hindi": "hi",
    "Portuguese": "pt"
}

# --- Translation Logic ---
def translate_text():
    source_lang_name = source_lang_combobox.get()
    target_lang_name = target_lang_combobox.get()
    input_text = text_input.get("1.0", tk.END).strip()
    
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text to translate.")
        return
        
    source_code = "auto" if source_lang_name == "Auto Detect" else LANGUAGES.get(source_lang_name)
    target_code = LANGUAGES.get(target_lang_name)
    
    try:
        # Call Translation API
        translator = GoogleTranslator(source=source_code, target=target_code)
        translated_text = translator.translate(input_text)
        
        # Display Output
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated_text)
        text_output.config(state=tk.DISABLED)
        
    except exceptions.LanguageNotSupportedException:
        messagebox.showerror("Error", "Selected language pair is not supported.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# --- Optional Feature: Copy to Clipboard ---
def copy_to_clipboard():
    output_text = text_output.get("1.0", tk.END).strip()
    if output_text:
        root.clipboard_clear()
        root.clipboard_append(output_text)
        messagebox.showinfo("Success", "Translated text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy.")

# --- UI Layout ---

# Title
title_label = tk.Label(root, text="Language Translation Tool", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#333")
title_label.pack(pady=10)

# Language Selection Frame
lang_frame = tk.Frame(root, bg="#f0f2f5")
lang_frame.pack(pady=10, fill=tk.X, px=20)

tk.Label(lang_frame, text="From:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=0, padx=5, sticky="w")
source_lang_combobox = ttk.Combobox(lang_frame, values=["Auto Detect"] + list(LANGUAGES.keys()), state="readonly", width=18)
source_lang_combobox.set("Auto Detect")
source_lang_combobox.grid(row=0, column=1, padx=5)

tk.Label(lang_frame, text="To:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=2, padx=5, sticky="w")
target_lang_combobox = ttk.Combobox(lang_frame, values=list(LANGUAGES.keys()), state="readonly", width=18)
target_lang_combobox.set("Spanish")
target_lang_combobox.grid(row=0, column=3, padx=5)

# Input Text Area
tk.Label(root, text="Enter Text:", bg="#f0f2f5", font=("Arial", 11, "bold")).pack(anchor="w", padx=20, pady=(10, 2))
text_input = tk.Text(root, height=6, font=("Arial", 10))
text_input.pack(fill=tk.X, padx=20)

# Action Buttons
btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=15)

translate_btn = tk.Button(btn_frame, text="Translate", command=translate_text, bg="#007bff", fg="white", font=("Arial", 10, "bold"), width=12, relief=tk.FLAT)
translate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy Result", command=copy_to_clipboard, bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=12, relief=tk.FLAT)
copy_btn.grid(row=0, column=1, padx=10)

# Output Text Area
tk.Label(root, text="Translation:", bg="#f0f2f5", font=("Arial", 11, "bold")).pack(anchor="w", padx=20, pady=(10, 2))
text_output = tk.Text(root, height=6, font=("Arial", 10), state=tk.DISABLED, bg="#e9ecef")
text_output.pack(fill=tk.X, padx=20)

# Start Application Loop
root.mainloop()
