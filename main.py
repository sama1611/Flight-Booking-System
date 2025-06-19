import tkinter as tk
from PIL import Image, ImageTk
from bookiing import booking_page
from reservations import reservations_page


def show_frame(frame):
    frame.tkraise()

def start_main():
    root=tk.Tk()
    root.title('safe fly co')
    root.state('zoom')

    container=tk.Frame(root)
    container.pack(fill='both',expand=True)

    nav_bar = tk.Frame(container,bg='medium turquoise')
    nav_bar.grid(row=0, column=0, sticky='nsew')

    btn_home = tk.Button(nav_bar, text="Home", command=lambda: show_frame(home_frm))
    btn_booking = tk.Button(nav_bar, text="Booking", command=lambda: show_frame(booking_frm))
    btn_reserve = tk.Button(nav_bar, text="Reservations", command=lambda: show_frame(res_frm))

    btn_home.pack(side='left', padx=10, pady=5)
    btn_booking.pack(side='left', padx=10, pady=5)
    btn_reserve.pack(side='left', padx=10, pady=5)

    bg_img = Image.open(r"C:\Users\a\Downloads\person-waiting-for-onboarding-in-an-airport-illustration-vector.jpg")
    bg_img = bg_img.resize((1500, 1080))
    bg_img_tk = ImageTk.PhotoImage(bg_img)

    container.grid_rowconfigure(0,weight=1)
    container.grid_columnconfigure(0,weight=1)

    home_frm=tk.Frame(container)
    home_frm.grid(row=0, column=0, sticky='nsew')


    res_frm, reload_reservations = reservations_page(container, bg_img_tk, home_frm)
    booking_frm = booking_page(container,bg_img_tk,home_frm,reload_reservations)


    bg_label = tk.Label(home_frm, image=bg_img_tk)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_frm = tk.Frame(home_frm)
    reserve_frm = tk.Frame(home_frm)
    book_frm = tk.Frame(home_frm)

    l1 = tk.Label(welcome_frm, text='welcome to flysafe reservations', font=('sylfaen', 48), fg='medium turquoise')


    l1.grid(row=0, column=0, sticky='ew')

    booking_l = tk.Label(book_frm,
                         text=' Reserve your next flight by providing your  details and flight information.',
                         font=('sylfaen', 12), fg='dim grey', pady=10)
    booking_btn = tk.Button(book_frm, text='book new flight',
                            bg='sky blue', fg='white',
                            font=('tahoma', 18), height=1,
                            command=lambda:show_frame(booking_frm))
    booking_btn.pack()
    booking_l.pack()

    reserve_l = tk.Label(reserve_frm,
                         text=' Manage your existing reservations, view details, edit or cancel if needed',
                         font=('tahoma', 12), fg='dim grey', pady=10)

    reserve_btn = tk.Button(reserve_frm, text='view reservations',
                            bg='sky blue', fg='white',
                            font=('tahoma', 18), height=1,command=lambda:show_frame(res_frm))
    reserve_btn.pack()
    reserve_l.pack()

    home_frm.grid_columnconfigure(0, weight=1)
    home_frm.grid_columnconfigure(1, weight=1)
    home_frm.grid(row=1, column=0, sticky='nsew')

    welcome_frm.grid_columnconfigure(0, weight=1)

    welcome_frm.grid(row=0, column=0,columnspan=3,pady=10,padx=10)
    book_frm.grid(row=1, column=2, pady=70, padx=10)
    reserve_frm.grid(row=2, column=2,pady=20,  padx=50)

    home_frm.tkraise()
    root.mainloop()

start_main()