# O usuário digita dois números. Ao clicar no botão, o programa mostra a soma.
import tkinter as tk
def soma():
    numero1 = int(entrada_numero1.get())
    numero2 = int(entrada_numero2.get())
    resultado = numero1 + numero2
    label_somar.config(text=f'A soma dos números é: {resultado}')

janela = tk.Tk()
janela.title('Soma de números')
janela.geometry('200x200')

label_primeiro_numero = tk.Label(janela, text='Digite o primeiro número: ')
label_primeiro_numero.pack(pady=5)
entrada_numero1 = tk.Entry(janela)
entrada_numero1.pack(pady=5)

label_segundo_numero = tk.Label(janela, text='Digite o segundo número: ')
label_segundo_numero.pack()
entrada_numero2 = tk.Entry(janela)
entrada_numero2.pack(pady=5)

botao_somar = tk.Button(janela, text='Somar', command=soma)
botao_somar.pack(pady=5)

label_somar = tk.Label(janela, text='')
label_somar.pack(pady=5)

janela.mainloop()
