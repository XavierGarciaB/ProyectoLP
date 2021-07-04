import tkinter as tk
from sintactico import parser
from lexico import lexer

root = tk.Tk()
root.title("Proyecto LP")
root.state("zoomed")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

content = tk.Frame(root)
content.pack(pady=10)

lbCodigo = tk.Label(content, text="Código", anchor="w", justify="left")
lbCodigo.pack(fill=tk.X)

codeText = tk.Text(content, width=int(screen_width/10), height=int(screen_height/30))
codeText.pack()

# PARA USAR EN ANALIZAR
console = tk.Frame(root)
lbConsole = tk.Label(console, text="Consola", anchor="w", justify="left")
consoleText = tk.Label(console, text="", bg="white", width=int(screen_width/10), height=int(screen_height/50))


def analizar():
    code = codeText.get("1.0", 'end-1c')
    print(code)
    consoleLog = ""
    result = parser.parse(code)
    print(result)
    consoleText.config(text=consoleLog)


btnFrame = tk.Frame(root, bg="blue", width=1400, height=100)
btnFrame.pack()

analizarBtn = tk.Button(btnFrame, text='Analizar', width=25, command=analizar)
analizarBtn.grid(row=0, column=0)


# PARTES DE LA CONSOLA
console.pack(pady=10)
lbConsole.pack(fill=tk.X)
consoleText.pack()

root.mainloop()
