import customtkinter
from PIL import Image
from playsound import playsound


class PomodoroApp:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    pomodoro_time = 25
    pomodoro_break_time = 5
    pomodoro_long_break_time = 15

    control = 0
    beep = 'beep.wav'
    is_idle = True

    settings_icon = customtkinter.CTkImage(light_image=Image.open('settings_icon.png'),
                                           dark_image=Image.open('settings_icon.png'),
                                           size=(27, 27))
    play_icon = customtkinter.CTkImage(light_image=Image.open('./play_icon.png'),
                                       dark_image=Image.open('./play_icon.png'),
                                       size=(60, 60))
    pause_icon = customtkinter.CTkImage(light_image=Image.open('./pause_icon.png'),
                                        dark_image=Image.open('./pause_icon.png'),
                                        size=(60, 60))
    stop_icon = customtkinter.CTkImage(light_image=Image.open('stop_icon.png'),
                                       dark_image=Image.open('stop_icon.png'),
                                       size=(60, 60))

    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title('Pomodoro')
        self.app.geometry(f'{PomodoroApp.WINDOW_WIDTH}x{PomodoroApp.WINDOW_HEIGHT}')
        self.app.resizable(False, False)

        self.timer_display = customtkinter.CTkLabel(self.app,
                                                    text=f"{PomodoroApp.pomodoro_time:02}:00",
                                                    font=("Arial", 120),
                                                    text_color=("black", "white"))
        self.timer_display.place(x=100, y=150)

        self.settings_button = customtkinter.CTkButton(self.app,
                                                       fg_color='transparent',
                                                       image=PomodoroApp.settings_icon,
                                                       width=27,
                                                       height=27,
                                                       hover=False,
                                                       border_spacing=0,
                                                       border_width=0,
                                                       corner_radius=0,
                                                       command=PomodoroApp.do_menu,
                                                       text='',
                                                       cursor='hand2')
        self.settings_button.place(x=455, y=20)

        self.play_button = customtkinter.CTkButton(self.app,
                                                   fg_color='transparent',
                                                   image=PomodoroApp.play_icon,
                                                   hover=False,
                                                   width=60,
                                                   height=60,
                                                   border_spacing=0,
                                                   border_width=0,
                                                   corner_radius=0,
                                                   command=self.do_play,
                                                   text='',
                                                   cursor='hand2')
        self.play_button.place(x=215, y=370)

        self.pause_button = customtkinter.CTkButton(self.app,
                                                    fg_color='transparent',
                                                    image=PomodoroApp.pause_icon,
                                                    hover=False,
                                                    width=60,
                                                    height=60,
                                                    border_spacing=0,
                                                    border_width=0,
                                                    corner_radius=0,
                                                    command=self.do_pause,
                                                    text='',
                                                    cursor='hand2')
        self.pause_button.place(x=280, y=370)

        self.stop_button = customtkinter.CTkButton(self.app,
                                                   fg_color='transparent',
                                                   image=PomodoroApp.stop_icon,
                                                   hover=False,
                                                   width=60,
                                                   height=60,
                                                   border_spacing=0,
                                                   border_width=0,
                                                   corner_radius=0,
                                                   command=self.do_stop,
                                                   text='',
                                                   cursor='hand2')
        self.stop_button.place(x=150, y=370)

    @classmethod
    def do_menu(cls):
        return

    def do_play(self):
        if PomodoroApp.control == 0:
            self.countdown_timer(PomodoroApp.pomodoro_time, 0)
        PomodoroApp.control = 1
        PomodoroApp.is_idle = False
        return

    @staticmethod
    def do_pause():
        PomodoroApp.is_idle = True
        return

    @staticmethod
    def do_stop():
        PomodoroApp.is_idle = True
        PomodoroApp.control = 2
        return

    def update_timer(self, minutes, seconds):
        self.timer_display.configure(text=f'{minutes:02}:{seconds:02}')
        self.app.update()

    def countdown_timer(self, minutes, seconds):
        if PomodoroApp.is_idle:
            if PomodoroApp.control == 2:
                minutes = PomodoroApp.pomodoro_time
                seconds = 0
                self.update_timer(minutes, seconds)
            return self.app.after(1000, self.countdown_timer, minutes, seconds)
        elif minutes == 0 and seconds == 0:
            playsound(PomodoroApp.beep)
            minutes = PomodoroApp.pomodoro_break_time
            return self.app.after(1000, self.countdown_timer, minutes, seconds)
        elif seconds == 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1

        self.update_timer(minutes, seconds)
        self.app.after(1000, self.countdown_timer, minutes, seconds)

    def run(self):
        self.app.mainloop()


if __name__ == '__main__':
    pomodoro_app = PomodoroApp()
    while True:
        pomodoro_app.run()
