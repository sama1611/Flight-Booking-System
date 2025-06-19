import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def reservations_page(container, show_frame, home_frm):
    reservations_frm = tk.Frame(container,bg='pale Turquoise')
    reservations_frm.grid(row=1, column=0, sticky='nsew')

    # ===== Title =====
    title = tk.Label(reservations_frm, text="Your Reservations", font=('tahoma', 24), fg="dark blue")
    title.pack(pady=10)

    # ===== Treeview Table =====
    tree = ttk.Treeview(reservations_frm, columns=('id', 'name', 'flight', 'departure', 'destination', 'date', 'seat'), show='headings')
    for col in tree["columns"]:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=120)

    tree.pack(pady=10)

    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        con = sqlite3.connect("flights.db")
        cur = con.cursor()
        cur.execute("SELECT rowid, Name, flightnumber, departure, destination, date, seatnumber FROM reservations")
        for row in cur.fetchall():
            tree.insert('', 'end', values=row)
        con.close()

    load_data()


    selected_id = None
    entries = {}

    def on_select(event):
        nonlocal selected_id
        selected = tree.focus()
        values = tree.item(selected, 'values')
        if values:
            selected_id = values[0]
            for i, key in enumerate(['name', 'flight', 'departure', 'destination', 'date', 'seat']):
                entries[key].delete(0, 'end')
                entries[key].insert(0, values[i+1])

    tree.bind('<<TreeviewSelect>>', on_select)

    # ===== Entry Fields to Edit =====
    form = tk.Frame(reservations_frm)
    form.pack(pady=10)

    for i, field in enumerate(['name', 'flight', 'departure', 'destination', 'date', 'seat']):
        lbl = tk.Label(form, text=field.capitalize())
        lbl.grid(row=i, column=0, padx=5, pady=5)
        ent = tk.Entry(form, width=40)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[field] = ent

    # ===== Buttons =====
    def update_reservation():
        if not selected_id:
            messagebox.showwarning("No selection", "Please select a reservation to update.")
            return

        updated_values = tuple(entries[k].get() for k in ['name', 'flight', 'departure', 'destination', 'date', 'seat'])

        con = sqlite3.connect("flights.db")
        cur = con.cursor()
        cur.execute("""
            UPDATE reservations
            SET Name=?, flightnumber=?, departure=?, destination=?, date=?, seatnumber=?
            WHERE rowid=?
        """, (*updated_values, selected_id))
        con.commit()
        con.close()
        load_data()
        messagebox.showinfo("Success", "Reservation updated.")

    def delete_reservation():
        if not selected_id:
            messagebox.showwarning("No selection", "Please select a reservation to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?")
        if confirm:
            con = sqlite3.connect("flights.db")
            cur = con.cursor()
            cur.execute("DELETE FROM reservations WHERE rowid=?", (selected_id,))
            con.commit()
            con.close()
            load_data()
            for ent in entries.values():
                ent.delete(0, 'end')
            messagebox.showinfo("Deleted", "Reservation deleted.")

    btns = tk.Frame(reservations_frm)
    btns.pack(pady=10)

    update_btn = tk.Button(btns, text="Update", command=update_reservation, bg='orange')
    delete_btn = tk.Button(btns, text="Delete", command=delete_reservation, bg='red')
    back_btn = tk.Button(btns, text="Back", command=lambda: show_frame(home_frm))

    update_btn.grid(row=0, column=0, padx=10)
    delete_btn.grid(row=0, column=1, padx=10)
    back_btn.grid(row=0, column=2, padx=10)

    return reservations_frm, load_data

