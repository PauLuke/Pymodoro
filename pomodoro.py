import customtkinter
import time

app = customtkinter.CTk()
app.title("Pomodoro")
app.geometry("500x500")
app.resizable(False, False)
app.grid_columnconfigure((0, 1, 2), weight=1)
app.grid_rowconfigure((0, 1, 2), weight=1)

timer = customtkinter.CTkLabel(app, text="25:00", font=("Arial", 50))
timer.grid(row=1, column=1, padx=20, pady=20)
time_pomodoro = 25.00

while True:
    time.sleep(0.01)
    time_pomodoro -= 0.01
    timer.configure(text=f"{int(time_pomodoro)}:{int((time_pomodoro - int(time_pomodoro)) * 10)}")
    app.update()
