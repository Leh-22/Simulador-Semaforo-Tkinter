# semaforo_tkinter.py
import tkinter as tk

class SemaforoApp:
    def __init__(self, root):
        self.root = root
        root.title("Simulador de Semáforo")

        # Canvas que mostra as luzes
        self.canvas = tk.Canvas(root, width=140, height=320, bg='black')
        self.canvas.pack(padx=10, pady=10)

        # Círculos (luzes)
        self.vermelho = self.canvas.create_oval(20, 20, 120, 120, fill='gray')
        self.amarelo   = self.canvas.create_oval(20, 120, 120, 220, fill='gray')
        self.verde     = self.canvas.create_oval(20, 220, 120, 320, fill='gray')

        # Label para mostrar estado/contador
        self.info = tk.Label(root, text="Parado", font=('Arial', 12))
        self.info.pack(pady=(5,0))

        # Controles
        frame = tk.Frame(root)
        frame.pack(pady=6)
        tk.Button(frame, text="Start", command=self.start).pack(side='left', padx=4)
        tk.Button(frame, text="Stop",  command=self.stop).pack(side='left', padx=4)
        tk.Button(frame, text="Pedestre", command=self.pedestre).pack(side='left', padx=4)

        # Configurações de tempo (segundos)
        self.timings = {'vermelho': 3, 'verde': 3, 'amarelo': 2}

        # Estado interno
        self.seq = ['vermelho', 'verde', 'amarelo']
        # ordem do ciclo
        self.index = 0
        # índice da fase atual na seq
        self.running = False
        self.remaining = 0
        # segundos restantes na fase atual
        self.job = None
        # id do after para cancelar se necessário
        self.pedestrian_request = False

    def start(self):
        if not self.running:
            self.running = True
            self.index = 0
            self.next_phase()

    def stop(self):
        self.running = False
        if self.job:
            self.root.after_cancel(self.job)
            self.job = None
        self.reset_colors()
        self.info.config(text="Parado")

    def pedestre(self):
        # Se o semáforo estiver verde, solicita cedo a troca (reduz o tempo restante)
        if self.running and self.seq[self.index] == 'verde':
            # força a contagem para terminar em 1s (se já for <=1, fica)
            if self.remaining > 1:
                self.remaining = 1
                self.info.config(text="Pedido pedestre: aguarde 1s")

    def reset_colors(self):
        self.canvas.itemconfig(self.vermelho, fill='gray')
        self.canvas.itemconfig(self.amarelo, fill='gray')
        self.canvas.itemconfig(self.verde, fill='gray')

    def update_display(self, state, seconds):
        # pinta as luzes conforme state
        colors = {'vermelho':'gray','amarelo':'gray','verde':'gray'}
        if state == 'vermelho': colors['vermelho'] = 'red'
        if state == 'amarelo':  colors['amarelo']  = 'yellow'
        if state == 'verde':   colors['verde']    = 'green'

        self.canvas.itemconfig(self.vermelho, fill=colors['vermelho'])
        self.canvas.itemconfig(self.amarelo,  fill=colors['amarelo'])
        self.canvas.itemconfig(self.verde,    fill=colors['verde'])
        self.info.config(text=f"{state.capitalize()} — {seconds} s")

    def next_phase(self):
        if not self.running:
            return
        state = self.seq[self.index]
        duration = self.timings[state]
        self.countdown(state, duration)

    def countdown(self, state, seconds):
        if not self.running:
            return
        self.remaining = seconds
        def tick():
            if not self.running:
                return
            if self.remaining <= 0:
                # avança para a próxima fase
                self.index = (self.index + 1) % len(self.seq)
                self.next_phase()
            else:
                self.update_display(state, self.remaining)
                self.remaining -= 1
                # agenda o próximo tick em 1s
                self.job = self.root.after(1000, tick)
        tick()

if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoApp(root)
    root.mainloop()
