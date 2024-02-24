import customtkinter
from PIL import Image


class PomodoroApp:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    pomodoro_time = 25
    pomodoro_break_time = 5
    pomodoro_long_break_time = 15

    menu_icon = customtkinter.CTkImage(light_image=Image.open("./menu_icon.png"),
                                       dark_image=Image.open("./menu_icon.png"),
                                       size=(25, 25))

    play_icon = customtkinter.CTkImage(light_image=Image.open("./play_icon.png"),
                                       dark_image=Image.open("./play_icon.png"),
                                       size=(25, 25))

    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title('Pomodoro')
        self.app.geometry(f'{PomodoroApp.WINDOW_WIDTH}x{PomodoroApp.WINDOW_HEIGHT}')
        self.app.resizable(False, False)

        self.timer_display = customtkinter.CTkLabel(self.app,
                                                    text=f"{PomodoroApp.pomodoro_time}:00",
                                                    font=("Arial", 120),
                                                    text_color=("black", "white"))
        self.timer_display.place(x=100, y=100)

        self.menu_button = customtkinter.CTkButton(self.app,
                                                   fg_color="transparent",
                                                   image=PomodoroApp.menu_icon,
                                                   width=25,
                                                   height=25,
                                                   hover=False,
                                                   border_spacing=0,
                                                   command=PomodoroApp.do_menu,
                                                   text="",
                                                   cursor="hand2")
        self.menu_button.place(x=0, y=0)

        self.play_button = customtkinter.CTkButton(self.app,
                                                   fg_color="transparent",
                                                   image=PomodoroApp.play_icon,
                                                   width=25,
                                                   height=25,
                                                   hover=False,
                                                   border_spacing=0,
                                                   command=PomodoroApp.do_play,
                                                   text="",
                                                   cursor="hand2")
        self.play_button.place(x=100, y=400)

    @classmethod
    def do_menu(cls):
        return

    @classmethod
    def do_play(cls):
        return

    def update_timer(self, minutes, seconds):
        self.timer_display.configure(text=f"{minutes:02}:{seconds:02}")
        self.app.update()

    def countdown_timer(self, minutes, seconds):
        if minutes == 0 and seconds == 0:
            return  # Timer finished
        elif seconds == 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1

        self.update_timer(minutes, seconds)
        self.app.after(1000, self.countdown_timer, minutes, seconds)

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    pomodoro_app = PomodoroApp()
    pomodoro_app.countdown_timer(PomodoroApp.pomodoro_time, 0)
    pomodoro_app.run()
