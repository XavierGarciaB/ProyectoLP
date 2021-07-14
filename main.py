import tkinter as tk
from sintactico import parser, error_list
from lexico import lexer

root = tk.Tk()
root.title("Proyecto LP")
root.state("zoomed")

screen_width = root.winfo_screenwidth()/10
screen_height = root.winfo_screenheight()

content = tk.Frame(root)
content.pack(pady=10)

lbCodigo = tk.Label(content, text="Código", anchor="w", justify="left")
lbCodigo.pack(fill=tk.X)

codeText = tk.Text(content, width=200, height=int(screen_height/30))
codeText.pack()

# PARA USAR EN ANALIZAR
consoleFrame = tk.Frame(root)
lbConsole = tk.Label(consoleFrame, text="Consola", anchor="w", justify="left")
lbConsole.pack(fill=tk.X)
console = tk.Frame(consoleFrame)
console.pack(pady=10)
scrollbar = tk.Scrollbar(console)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
consoleText = tk.Listbox(console, bg="white", width=200, height=int(screen_height/50), font=('Times', 11), yscrollcommand=scrollbar.set)
consoleText.pack(side=tk.LEFT, fill=tk.BOTH)


def limpiar_consola():
    lexer.lineno = 1
    error_list.clear()
    consoleText.delete(0, tk.END)


def analizar():
    code = codeText.get("1.0", 'end-1c')
    limpiar_consola()
    parser.parse(code)
    if len(error_list) == 0:
        consoleText.insert(tk.END, '~ Lectura terminada sin errores')
    for error in error_list:
        consoleText.insert(tk.END, '-> ' + error)


btnFrame = tk.Frame(root, bg="blue", width=1400, height=100)
btnFrame.pack()

analizarBtn = tk.Button(btnFrame, text='Analizar', width=25, command=analizar)
analizarBtn.grid(row=0, column=0)

limpiarBtn = tk.Button(btnFrame, text='Limpiar', width=25, command=limpiar_consola)
limpiarBtn.grid(row=0, column=1)

consoleFrame.pack()

root.mainloop()
