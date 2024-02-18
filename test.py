import customtkinter
from PIL import Image

def settings():
    return
    

def update_timer(minutes, seconds):
    timer.configure(text=f"{minutes:02}:{seconds:02}")
    app.update()

def countdown_timer(minutes, seconds):
    if minutes == 0 and seconds == 0:
        return  # Timer finished
    elif seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1

    update_timer(minutes, seconds)
    app.after(1000, countdown_timer, minutes, seconds)

app = customtkinter.CTk()
app.title("Pomodoro")
app.geometry("500x500")
app.resizable(False, False)
app.grid_columnconfigure((0, 1, 2), weight=1)
app.grid_rowconfigure((0, 1, 2), weight=1)

settings_image = customtkinter.CTkImage(light_image=Image.open("/home/pauluke/Downloads/settings_icon.png"),
                                  dark_image=Image.open("/home/pauluke/Downloads/settings_icon.png"),
                                  size=(30, 30))

# Create a label to display the time
timer = customtkinter.CTkLabel(app, text="25:00", font=("Arial", 70))
timer.grid(row=1, column=1, padx=0, pady=0, sticky="ew")

# Crete a settings buttom
settings_button = customtkinter.CTkButton(app, fg_color="transparent",image=settings_image, width=35, height=35, 
                                hover=False, border_spacing=0, corner_radius=20, command=settings, text="")
settings_button.grid(row=0, column=2)

# Start the countdown timer
countdown_timer(25, 0)

app.mainloop()
