import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btn = tk.Button(self, text="Btn")
        self.btn.pack(padx=5, pady=5)
        self.btn.bind('<Button-1>', self.on_btn)
        self.entry_var =  tk.StringVar()
        entry = tk.Entry(textvariable=self.entry_var)
        entry.pack(padx=5, pady=5)

    def on_btn(self, event):
        print(f'on_btn: {self.entry_var.get()}')



if __name__ == '__main__':
    app = App()
    app.mainloop()