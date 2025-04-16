""" Crie um programa que permita ao usuário digitar ingredientes de uma receita e adicioná-los a uma lista. Se o campo estiver vazio, mostre uma mensagem pedindo para digitar algo. (Exercício 15)

Implemente a função para excluir os produtos da Listbox """
import tkinter as tk
def register_ingredients():
    ingredients = entry_ingredients.get()
    if ingredients:
        result.insert(tk.END, ingredients)
        entry_ingredients.delete(0, tk.END)
        notice.config(text='')
    else:
        notice.config(text='Enter the ingredient: ', fg='red')

def delete_product():
    global indice_selected
    selected_product = result.curselection()
    if not selected_product:
        notice.config(text='Select a product to delete.', fg='red')
        return
    indice = selected_product[0]
    result.delete(indice)
    clear_fields()
    notice.config(text='Product deleted successfully!', fg='green')
    indice_selected = None

def clear_fields():
    entry_ingredients.delete(0, tk.END)

window = tk.Tk()
window.title('Ingredients')
window.geometry('400x450')

tk.Label(window, text='Enter the ingrediente: ').pack(pady=10)
entry_ingredients = tk.Entry(window)
entry_ingredients.pack(pady=10)

notice = tk.Label(window)
notice.pack(pady=10)

tk.Button(window, text='Click here', command=register_ingredients, fg='green').pack(pady=10)
tk.Button(window, text='Delete product', command=delete_product, fg='green').pack(pady=10)

tk.Label(window, text='List of ingredients: ').pack(pady=10)
result = tk.Listbox(window)
result.pack(pady=10)

window.mainloop()
