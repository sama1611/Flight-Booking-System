
# ✈️ fly safe .Co – Flight Booking System

This is a Python desktop application for booking and managing flight reservations.  
It features a clean GUI built with **Tkinter** and uses **SQLite** as the database engine.

---

## 📌 Features

- 🛫 Book new flight reservations
- 📋 View all existing reservations in a table
- ✏️ Edit or update reservation details
- ❌ Delete any selected reservation
- 📅 Choose flight dates with a calendar widget
- 🎨 Visual UI with a custom image background
- 🗃️ All data stored in `flights.db` using SQLite

---

## 🖥️ How to Run the App

### 🟢 Option 1 – Run as Python Script

> Requirements:
- Python 3.x
- Libraries: `tkinter`, `pillow`, `tkcalendar`

#### 🔧 Installation Steps:

1. Clone or download the project files
2. Open terminal (cmd) and run:
   ```bash
   pip install pillow tkcalendar
   ```

3. Run the app:
   ```bash
   python main.py
   ```

---

### 🔵 Option 2 – Run the Executable (.exe)

1. Open the `dist/` folder
2. Make sure these files are inside:
   - `main.exe`
   - `flights.db`
   - Background image (e.g. `person-waiting-for-onboarding-in-an-airport-illustration-vector.jpg`)
3. Double-click `main.exe` to launch the app

---

## 🗃️ Database Schema (`reservations` Table)

| Field         | Type    | Description            |
|---------------|---------|------------------------|
| Name          | TEXT    | Passenger name         |
| flightnumber  | TEXT    | Flight number          |
| departure     | TEXT    | Departure location     |
| destination   | TEXT    | Destination location   |
| date          | DATE    | Flight date            |
| seatnumber    | TEXT    | Seat number            |

---

## 👩‍💻 Developed By

**sama yasin**  
Electronics & Communication Engineering ✨  
