from tkinter import *

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def hotelPage(window):
    clear_window(window)  
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar linked to the Canvas
    scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.config(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas that will contain all the buttons
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Configure rows and columns for the frame using grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=4)
    frame.rowconfigure(2, weight=3)

    # Add buttons with text and images to the frame using grid
    #Button(frame, text="Back", font=("Arial", 12), fg="#01406c", bg="#FF7B07", compound="top", command=Mainpage(window)).grid(row=0, column=0, sticky="wesn",columnspan=1)
    Button(frame, text="Hotel 2", font=("Arial", 12), fg="white", bg="#cc4735", compound="top", command=lambda: print("info")).grid(row=0, column=2, sticky="wesn",columnspan=1)
    hotel_data = [
    {"id": "Hotel1", "img": hotel1_img},
    {"id": "Hotel2", "img": hotel2_img},
    {"id": "Hotel3", "img": hotel3_img},
    {"id": "Hotel4", "img": hotel4_img},
    {"id": "Hotel5", "img": hotel5_img},
    {"id": "Hotel6", "img": hotel6_img},
    # Tambahkan hotel lainnya sesuai kebutuhan
    ]

    # Hotel buttons with images
    for index, hotel in enumerate(hotel_data, start=1):
        name = getname(hotel["id"])
        desc = getdesc(hotel["id"])
        alamat = getalamat(hotel["id"])
        rating = getRating(hotel["id"])
        hotel_img = hotel["img"]
        command = lambda h=hotel["id"]: hotel_page(h)
        # Membuat tombol untuk setiap hotel
        hotel_button = Button(frame, text=f"{name}\n{desc}\n{alamat}\n{rating}", 
                            font=("Helvetica Neue", 12, "bold"), fg="white", bg="#01B489", 
                            image=hotel_img, compound="top", command=hotel1page)
        hotel_button.grid(row=index, column=0, sticky="wesn", columnspan=3)

    # Update the scrollable region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Enable scrolling with mouse wheel
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    #Kamar
    window.title("Main Page")