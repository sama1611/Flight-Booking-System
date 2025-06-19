import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkcalendar import DateEntry


def booking_page(container, image, home, reload_reservations):


    def cancel():
        name_e.delete(0, 'end')
        flight_e.delete(0, 'end')
        destination_e.delete(0, 'end')
        departure_e.delete(0, 'end')
        date_e.delete(0, 'end')
        seat_e.delete(0, 'end')
        home.tkraise()

    def submit():
        name = name_e.get()
        flight = flight_e.get()
        des = destination_e.get()
        dep = departure_e.get()
        date = date_e.get()
        seat = seat_e.get()
        if not all([name, flight, des, dep, date, seat]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            con = sqlite3.connect('flights.db')
            cursor = con.cursor()

            cursor.execute('''
                    INSERT INTO reservations (Name, flightnumber, departure, destination, date, seatnumber)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, flight, dep, des, date, seat))

            con.commit()
            con.close()
            reload_reservations()
            messagebox.showinfo("Success", "Your flight has been booked.")
        except:
            messagebox.showerror('error','an error happened')



    booking_frm=tk.Frame(container)
    booking_frm.grid(row=1, column=0, sticky='nsew')

    bg_label = tk.Label(booking_frm,image=image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    data_frm=tk.Frame(booking_frm,bg='light grey')
    nandf_frm1=tk.Frame(data_frm,bg='light grey')
    data_frm1=tk.Frame(data_frm,bg='light grey')



    l_title=tk.Label(booking_frm,text='Book a flight',fg='dark blue',font=('tahoma',24))
    l_title2=tk.Label(booking_frm,text='please fill the data below',fg='grey',font=('tahoma',14))

    l_name=tk.Label(nandf_frm1,text='Name',fg='cornflower blue',font=('tahoma',18),bg='light grey')
    l_flight=tk.Label(nandf_frm1,text='flight number',fg='cornflower blue',font=('tahoma',18),bg='light grey')
    l_destination=tk.Label(data_frm1,text=' destination',fg='cornflower blue',font=('tahoma',18),bg='light grey')
    l_departure = tk.Label(data_frm1, text='departure', fg='cornflower blue', font=('tahoma', 18),bg='light grey')
    l_date= tk.Label(data_frm1, text='Date', fg='cornflower blue', font=('tahoma', 18),bg='light grey')
    l_seat=tk.Label(data_frm1, text=' Seat number', fg='cornflower blue', font=('tahoma', 18),bg='light grey')

    name_e=tk.Entry(nandf_frm1,width=70)
    flight_e=tk.Entry(nandf_frm1,width=70)
    destination_e=tk.Entry(data_frm1)
    departure_e = tk.Entry(data_frm1)
    date_e = DateEntry(data_frm1, width=12, background='darkblue',
                       foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    seat_e=tk.Entry(data_frm1)


    cancel_btn = tk.Button(data_frm1, text='Cancel', command=cancel, font=('tahoma', 18), fg='white', bg='red')
    submit_btn = tk.Button(data_frm1, text='submit', command=submit, font=('tahoma', 18))
    submit_btn.grid(row=7, column=1, pady=10, sticky='e')
    cancel_btn.grid(row=7, column=2, pady=10, padx=10, sticky='w')

    l_name.grid(row=0,column=0,pady=10)
    l_flight.grid(row=2,column=0,pady=10,padx=20)
    l_destination.grid(row=5,column=2,pady=10,sticky='w')
    l_departure.grid(row=5,column=0,pady=10,sticky='w')
    l_date.grid(row=6,column=0,pady=10,sticky='w')
    l_seat.grid(row=6,column=2,pady=10,sticky='w')

    name_e.grid(row=1,column=0,pady=5)
    flight_e.grid(row=3,column=0,columnspan=2,pady=5)
    destination_e.grid(row=5,column=3,pady=5,padx=5,sticky='w')
    departure_e.grid(row=5,column=1,pady=5,sticky='w')
    date_e.grid(row=6,column=1,pady=5,sticky='w')
    seat_e.grid(row=6,column=3,pady=5,padx=5,sticky='w')


    l_title.pack()
    l_title2.pack()
    nandf_frm1.pack()
    data_frm1.pack()
    data_frm.pack(pady=100)
    return booking_frm









