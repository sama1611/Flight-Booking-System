# import tkinter as tk
# from bookiing import booking_page
#
# def open_booking():
#     booking_page()
# def reservation():
#     print('this is reservation page')
#
# def open_home():
#     root=tk.Tk()
#     root.title('safe fly co')
#     root.state('zoom')
#
#
#     home_frm=tk.Frame(root)
#     welcome_frm=tk.Frame(home_frm)
#     reserve_frm=tk.Frame(home_frm,bg='light grey')
#     booking_frm=tk.Frame(home_frm,bg='light grey')
#
#     l1=tk.Label(welcome_frm,text='welcome to flysafe reservations',font=('bold',48),fg='dark blue',pady=10)
#     l1.grid(row=0,column=0,columnspan=2)
#
#     l2=tk.Label(welcome_frm,text='Book your flights and manage your reservations with our simple ,\n and intuitive system.',font=('tahoma',18,),fg='grey')
#     l2.grid(row=1, column=0, columnspan=2)
#
#     booking_l=tk.Label(booking_frm,text=' Reserve your next flight by providing your \n details and flight information.',font=('tahoma',18),fg='dim grey',bg='light grey',pady=10)
#     booking_btn=tk.Button(booking_frm,text='book new flight',
#                           bg='sky blue',fg='white',pady=10,
#                           font=('tahoma',20),height=5,
#                           command=open_booking,)
#     booking_btn.pack()
#     booking_l.pack()
#
#     reserve_l=tk.Label(reserve_frm,text=' Manage your existing reservations, \n view details, edit or cancel if needed',font=('tahoma',18),fg='dim grey',bg='light grey',pady=10)
#
#     reserve_btn=tk.Button(reserve_frm,text='view reservations',
#                           bg='sky blue',fg='white',
#                           font=('tahoma',20),height=5,pady=10,
#                           command=reservation)
#     reserve_btn.pack()
#     reserve_l.pack()
#
#
#
#     welcome_frm.grid(row=0,column=0,columnspan=2)
#     booking_frm.grid(row=2,column=0,pady=120)
#     reserve_frm.grid(row=2,column=1,pady=120)
#     home_frm.pack()
#     root.mainloop()
# open_home()
