import tkinter as tk
import grid


class Window:
    def __init__(self):

        self.window: tk.Tk = None
        self.menuFrame: tk.LabelFrame = None
        self.amountOfCreatures: tk.Entry = None
        self.initiateWithCorona: tk.Entry = None
        self.quickerCreatures: tk.Entry = None
        self.lowProbabilityToInfect: tk.Entry = None
        self.highProbabilityToInfect: tk.Entry = None
        self.infectionThreshold: tk.Entry = None
        self.infectionTime: tk.Entry = None
        self.startBtn: tk.Button = None
        self.applyBtn: tk.Button = None

        self.bgColor = '#2c313a'
        self.fgColor = '#1f7db7'
        self.textColor = '#7fb474'
        self.font = ('Consoles', 12)
        self.btnColor = '#181818'
        self.btnTextColor = '#f0f0f0'
        self.gridColor = '#010101'
        self.liveCellColor = '#00295E'

        self.state = 'paused'  # 'paused'|'running'
        self.Grid = grid.Grid(
            bg=self.gridColor,  #5000, 0.2, 0.05, 10, 0.3, 0.1, 0.2
            fg=self.liveCellColor,
            N=5000,
            D=0.2,
            R=0.05,
            X=10,
            P_high=0.3,
            P_low=0.1,
            T=0.2)

    def initiate(self):

        self.window = tk.Tk()
        self.window.geometry('800x600')
        self.window.configure(background=self.bgColor, highlightcolor=self.fgColor)
        self.window.title('CoronaWaves')

        self.menuFrame = tk.LabelFrame(
            master=self.window,
            bg=self.bgColor,
            fg=self.fgColor,
            text='Settings',
            font=self.font
        )

        padx, pady = 1, 1

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='N'
        ).grid(row=0, column=0, padx=padx, pady=pady)

        self.amountOfCreature = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor
        )
        self.amountOfCreature.grid(row=0, column=1, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='D'
        ).grid(row=0, column=3, padx=padx, pady=pady)

        self.initiateWithCorona = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor,
        )
        self.initiateWithCorona.grid(row=0, column=4, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='R'
        ).grid(row=1, column=0, padx=padx, pady=pady)

        self.quickerCreatures = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor,
        )
        self.quickerCreatures.grid(row=1, column=1, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='P_high'
        ).grid(row=3, column=0, padx=padx, pady=pady)

        self.highProbabilityToInfect = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor
        )
        self.highProbabilityToInfect.grid(row=3, column=1, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='P_low'
        ).grid(row=2, column=0, padx=padx, pady=pady)

        self.lowProbabilityToInfect = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor,
        )
        self.lowProbabilityToInfect.grid(row=2, column=1, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='T'
        ).grid(row=2, column=3, padx=padx, pady=pady)

        self.infectionThreshold = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor,
        )
        self.infectionThreshold.grid(row=2, column=4, padx=padx, pady=pady)

        tk.Label(
            master=self.menuFrame,
            font=self.font,
            bg=self.bgColor,
            fg=self.fgColor,
            text='X'
        ).grid(row=1, column=3, padx=padx, pady=pady)

        self.infectionTime = tk.Entry(
            master=self.menuFrame,
            font=self.font,
            width=3,
            bg=self.btnColor,
            fg=self.btnTextColor,
        )
        self.infectionTime.grid(row=1, column=4, padx=padx, pady=pady)

        self.applyBtn = tk.Button(
            master=self.menuFrame,
            bg=self.btnColor,
            fg=self.btnTextColor,
            font=self.font,
            text=' Apply ',
            command=self.applyBtnAction
        )
        self.applyBtn.grid(padx=padx, pady=pady, row=3, column=10, columnspan=4, sticky=(tk.E, tk.W))

        self.startBtn = tk.Button(
            master=self.menuFrame,
            bg=self.btnColor,
            fg=self.btnTextColor,
            font=("Courier", 25, 'bold'),
            text='\u23F5',
            command=self.startBtnAction
        )
        self.startBtn.grid(padx=padx, pady=pady, row=0, column=10, rowspan=3)

        self.menuFrame.pack(side='bottom', padx=5, pady=5)

        self.Grid.getGrid().pack(side='top', fill='both', expand=True, padx=5, pady=5)

        self.window.mainloop()

    def startBtnAction(self):

        if self.state == 'paused':
            self.state = 'running'
            self.startBtn.configure(text='\u23F8', font=("Courier", 25, 'bold'))
            self.applyBtn.configure(state='disabled')
            self.Grid.resume()
        else:
            self.state = 'paused'
            self.startBtn.configure(text='\u23F5', font=("Courier", 25, 'bold'))
            self.applyBtn.configure(state='normal')
            self.Grid.pause()

    def applyBtnAction(self):

        n = self.amountOfCreature.get().strip()
        d = self.initiateWithCorona.get().strip()
        p_high = self.highProbabilityToInfect.get().strip()
        p_low = self.lowProbabilityToInfect.get().strip()
        r = self.quickerCreatures.get().strip()
        t = self.infectionThreshold.get().strip()
        x = self.infectionTime.get().strip()

        # TODO ADD FUNCTIONALITY TO BUTTONS


if __name__ == '__main__':
    Window().initiate()
