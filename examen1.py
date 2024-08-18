import tkinter as tk
import threading
import time

class Multiplication:
    def __init__(self, parent, number, start, end):
        self.number = number
        self.start = start
        self.end = end
        self.frame = tk.Frame(parent)
        self.frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.label = tk.Label(self.frame, text=f"Tabla del {self.number}", font=('Arial', 14))
        self.label.pack(pady=5)
        self.text = tk.Text(self.frame, width=20, height=25, font=('Arial', 12))
        self.text.pack()

    def generate_table(self):
        for i in range(self.start, self.end + 1):
            time.sleep(0.1)  # Simula un proceso que toma tiempo
            result = f"{self.number} x {i} = {self.number * i}\n"
            # Usa after para actualizar la interfaz gráfica en el hilo principal
            self.text.after(0, self.text.insert, tk.END, result)
        self.text.after(0, self.text.insert, tk.END, "Finalizado\n")

def main():
    root = tk.Tk()
    root.title("Tablas de Multiplicar Concurrentes")
    
    # Instancias de la clase Multiplication
    multiplication1 = Multiplication(root, 2, 1, 50)
    multiplication2 = Multiplication(root, 3, 1, 50)
    
    # Crear hilos para la generación de tablas
    thread1 = threading.Thread(target=multiplication1.generate_table)
    thread2 = threading.Thread(target=multiplication2.generate_table)
    
    # Iniciar los hilos
    thread1.start()
    thread2.start()

    root.mainloop()

if __name__ == "__main__":
    main()
