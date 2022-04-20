import tkinter as tk
from tkinter import messagebox
from automata import Automata


class App:

    def __init__(self):

        self.bg_color = '#2c313a'
        self.fg_color = '#1f7db7'
        self.text_color = '#7fb474'
        self.btn_color = '#181818'
        self.btn_text_color = '#f0f0f0'
        self.grid_color = '#010101'
        self.live_cell_color = '#00295E'
        self.font = ('Consoles', 11)
        self.btn_font = ("Consoles", 11, 'bold')

        self.window = tk.Tk()
        self.window.geometry('1100x830')
        self.window.minsize(1100, 830)
        self.window.maxsize(1100, 830)
        self.window.configure(background=self.bg_color,
                              highlightcolor=self.fg_color)
        self.window.title('Corona Waves')

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.window.destroy()
                exit(0)

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        self.frame = tk.Canvas(bg='#404040', bd=0, highlightbackground='gray',
                               width=800, height=800)
        self.frame.place(relx=0.26, rely=0.025)
        self.automata = Automata(self)

        self.configuration = tk.LabelFrame(
            master=self.window,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Configuration',
            font=self.font
        )
        self.configuration.place(relx=0.015, rely=0.015)

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Number of creatures:'
        ).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.n_creature = self.createEntry(self.configuration, '1000')
        self.n_creature.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Infection percentage:'
        ).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.n_infected = self.createEntry(self.configuration, '0.2')
        self.n_infected.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Fast movers percentage:'
        ).grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.quick_creatures = self.createEntry(self.configuration, '0.05')
        self.quick_creatures.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Days for healing:'
        ).grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.healing_time = self.createEntry(self.configuration, '10')
        self.healing_time.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='High probability:'
        ).grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.high_probability = self.createEntry(self.configuration, '0.3')
        self.high_probability.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Low probability:'
        ).grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.low_probability = self.createEntry(self.configuration, '0.1')
        self.low_probability.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.configuration,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Threshold:'
        ).grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.threshold = self.createEntry(self.configuration, '0.2')
        self.threshold.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        self.pause_btn = tk.Button(
            master=self.window,
            width=12,
            bg=self.btn_color,
            fg=self.btn_text_color,
            font=self.btn_font,
            text='\u23F8 Pause',
            command=self.pause_btn_action
        )
        self.pause_btn.place(relx=0.02, rely=0.35)

        self.stop_btn = tk.Button(
            master=self.window,
            width=12,
            bg=self.btn_color,
            fg=self.btn_text_color,
            font=self.btn_font,
            text='\u23F9 Stop',
            command=self.stop_btn_action
        )
        self.stop_btn.place(relx=0.135, rely=0.35)

        self.run_btn = tk.Button(
            master=self.window,
            width=27,
            bg=self.btn_color,
            fg=self.btn_text_color,
            font=self.btn_font,
            text='\u23F5 Start   ',
            command=self.run_btn_action
        )
        self.run_btn.place(relx=0.015, rely=0.35)

        self.information = tk.LabelFrame(
            master=self.window,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Information',
            font=self.font
        )
        self.information.place(relx=0.015, rely=0.41)

        tk.Label(
            master=self.information,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Infected creatures:'
        ).grid(row=0, column=0, sticky='w')
        self.n_sick = self.createEntry(self.information, 'n/a')
        self.n_sick.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.information,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Distribution of infection :'
        ).grid(row=1, column=0, sticky='w')
        self.distribution = self.createEntry(self.information, 'n/a')
        self.distribution.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        tk.Label(
            master=self.information,
            font=self.font,
            bg=self.bg_color,
            fg=self.fg_color,
            text='Infection to threshold ratio:'
        ).grid(row=2, column=0, sticky='w')
        self.capacity = self.createEntry(self.information, 'n/a')
        self.capacity.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.window.mainloop()

    def createEntry(self, master, default_value):
        entry = tk.Entry(
            master=master,
            font=self.font,
            width=7,
            bg=self.btn_color,
            justify='center',
            fg=self.btn_text_color
        )
        entry.insert(0, default_value)
        return entry

    def get_input(self):
        error_messages = []
        N, D, X, R, PH, PL, T = 0, 0, 0, 0, 0, 0, 0
        D = float(self.n_infected.get().strip())
        try:
            N = int(self.n_creature.get().strip())
        except ValueError:
            error_messages.append('Number of creatures should be a positive integer.')
        try:
            D = float(self.n_infected.get().strip())
            if D < 0 or D > 1:
                raise ValueError
        except ValueError:
            error_messages.append('Infection percentage should be a float between 0 and 1.')
        try:
            X = int(self.healing_time.get().strip())
        except ValueError:
            error_messages.append('Days for healing should be a positive integer.')
        try:
            R = float(self.quick_creatures.get().strip())
            if R < 0 or R > 1:
                raise ValueError
        except ValueError:
            error_messages.append('Fast movers percentage should be a float between 0 and 1.')
        try:
            PH = float(self.high_probability.get().strip())
            if PH < 0 or PH > 1:
                raise ValueError
        except ValueError:
            error_messages.append('High probability should be a float between 0 and 1.')
        try:
            PL = float(self.low_probability.get().strip())
            if PL < 0 or PL > 1:
                raise ValueError
        except ValueError:
            error_messages.append('Low probability should be a float between 0 and 1.')
        try:
            T = float(self.threshold.get().strip())
            if T < 0 or T > 1:
                raise ValueError
        except ValueError:
            error_messages.append('Threshold should be a float between 0 and 1.')

        if len(error_messages) == 0:
            return N, D, X, R, PH, PL, T
        else:
            messagebox.showerror('Input Error', '\n'.join(error_messages))

    def run_btn_action(self):
        if self.automata.state.is_stopped:
            N, D, X, R, PH, PL, T = self.get_input()
            self.run_btn.place_forget()
            self.automata.set(N, D, X, R, PH, PL, T)
            self.automata.run()
        elif self.automata.state.is_paused:
            self.run_btn.place_forget()
            self.automata.run()

    def pause_btn_action(self):
        self.run_btn.place(relx=0.015, rely=0.35)
        self.run_btn.configure(text='\u23F5 Resume  ', font=self.btn_font)
        self.automata.pause()

    def stop_btn_action(self):
        self.run_btn.place(relx=0.015, rely=0.35)
        self.run_btn.configure(text='\u23F5 Start   ', font=self.btn_font)
        self.automata.stop()
