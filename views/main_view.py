import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class MainView:
    def __init__(self, presenter):
        self.presenter = presenter
        self.root = tk.Tk()  # Cambié a Tk() para que sea la ventana principal

        self.root.title("Document Filler")
        self.root.geometry("600x300")

        style = ttk.Style()
        style.theme_use("clam")

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="First Names:").grid(row=0, column=0, sticky="e")
        self.first_name_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.first_name_var).grid(row=0, column=1)

        ttk.Label(main_frame, text="Last Names:").grid(row=0, column=2, sticky="e")
        self.last_name_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.last_name_var).grid(row=0, column=3)

        ttk.Label(main_frame, text="Age:").grid(row=1, column=0, sticky="e")
        self.age_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.age_var).grid(row=1, column=1)

        ttk.Label(main_frame, text="Day:").grid(row=1, column=2, sticky="e")
        self.day_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.day_var).grid(row=1, column=3)

        ttk.Label(main_frame, text="Month:").grid(row=1, column=4, sticky="e")
        self.month_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.month_var).grid(row=1, column=5)

        ttk.Label(main_frame, text="Year:").grid(row=1, column=6, sticky="e")
        self.year_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.year_var).grid(row=1, column=7)

        ttk.Label(main_frame, text="Tutor:").grid(row=2, column=0, sticky="e")
        self.tutor_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.tutor_var).grid(row=2, column=1)

        load_doc_btn = ttk.Button(main_frame, text="Load Word Template", command=self.presenter.on_load_document)
        load_doc_btn.grid(row=3, column=0, columnspan=2, pady=10)

        self.generate_docs_btn = ttk.Button(main_frame, text="Generate Documents from Excel", command=self.presenter.on_generate_documents)
        self.generate_docs_btn.grid(row=4, column=0, columnspan=2, pady=10)
        self.generate_docs_btn.config(state="disabled")

        self.save_btn = ttk.Button(main_frame, text="Save Document", command=self.presenter.on_save_document)
        self.save_btn.grid(row=5, column=0, columnspan=2, pady=10)
        self.save_btn.config(state="disabled")

    def get_form_data(self):
        return {
            'FirstNames': self.first_name_var.get(),
            'LastNames': self.last_name_var.get(),
            'Age': self.age_var.get(),
            'Day': self.day_var.get(),
            'Month': self.month_var.get(),
            'Year': self.year_var.get(),
            'Tutor': self.tutor_var.get()
        }

    def set_save_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self.save_btn.config(state=state)

    def set_generate_enabled(self, enabled):
        state = "normal" if enabled else "disabled"
        self.generate_docs_btn.config(state=state)

    def ask_save_path(self):
        return filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])

    def ask_open_file(self, filetypes):
        return filedialog.askopenfilename(filetypes=filetypes)

    def show_success(self, message):
        messagebox.showinfo("Success", message)

    def show_warning(self, message):
        messagebox.showwarning("Warning", message)

    def run(self):
        self.root.mainloop()
