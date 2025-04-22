import tkinter as tk
from prototipo_student_management_ui import StudentManagementApp

if __name__ == "__main__":
    janela = tk.Tk()
    app = StudentManagementApp(janela)
    janela.mainloop()
    