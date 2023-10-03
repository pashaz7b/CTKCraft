import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("500x500")
root.resizable(False, False)

frame = ctk.CTkFrame(master=root)


def after_authentication():
    global frame
    frame.destroy()

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Simple Login & SignUp Page", text_color="#c10ec4", font=("Arial", 24))
    label.place(x=185, y=230, anchor="center")


def open_signup_page():
    global frame
    frame.destroy()

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Sign Up", text_color="#7611d4", font=("Arial", 24))
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username", corner_radius=20, height=40)
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", corner_radius=20, height=40, show="*")
    entry2.pack(pady=12, padx=10)

    entry3 = ctk.CTkEntry(master=frame, placeholder_text="Email", corner_radius=20, height=40)
    entry3.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Sign Up", corner_radius=20, height=40, command=after_authentication)
    button.place(x=185, y=310, anchor="center")

    checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=5)


def login():
    global frame
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Log In", text_color="#7611d4", font=("Arial", 24))
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username", corner_radius=20, height=40)
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", corner_radius=20, height=40, show="*")
    entry2.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Log In", corner_radius=20, height=40, command=after_authentication)
    button.place(x=185, y=250, anchor="center")

    checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

    label = ctk.CTkLabel(master=frame, text="Don't Have Account? Sign Up", cursor="hand2")
    label.pack(pady=50, padx=10)

    label.bind("<Button-1>", lambda event: open_signup_page())


if __name__ == '__main__':
    login()
    root.mainloop()
