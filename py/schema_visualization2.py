import sqlite3
import tkinter as tk
from tkinter import ttk

# Your provided functions have been updated to work with SQLite

def create_connection(connection):
    conn = None
    try:
        conn = sqlite3.connect('smarthealth.db')
    except sqlite3.Error as e:
        print(e)

    return conn

def insert_patient(connection, first_name, last_name, date_of_birth, gender):
    cursor = connection.cursor()
    query = """
    INSERT INTO Patients (first_name, last_name, date_of_birth, gender)
    VALUES (?, ?, ?, ?);
    """
    data = (first_name, last_name, date_of_birth, gender)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
def insert_payment_info(connection, patient_id, billing_id, payment_method, payment_date):
    cursor = connection.cursor()
    query = """
    INSERT INTO PaymentInfo (patient_id, billing_id, payment_method, payment_date)
    VALUES (%s, %s, %s, %s);
    """
    data = (patient_id, billing_id, payment_method, payment_date)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_prescription(connection, medical_record_id, inventory_item_id, dosage, frequency, duration):
    cursor = connection.cursor()
    query = """
    INSERT INTO Prescriptions (medical_record_id, inventory_item_id, dosage, frequency, duration)
    VALUES (%s, %s, %s, %s, %s);
    """
    data = (medical_record_id, inventory_item_id, dosage, frequency, duration)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_diagnosis(connection, medical_record_id, diagnosis, date):
    cursor = connection.cursor()
    query = """
    INSERT INTO Diagnoses (medical_record_id, diagnosis, date)
    VALUES (%s, %s, %s);
    """
    data = (medical_record_id, diagnosis, date)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_treatment(connection, medical_record_id, treatment, date):
    cursor = connection.cursor()
    query = """
    INSERT INTO Treatments (medical_record_id, treatment, date)
    VALUES (%s, %s, %s);
    """
    data = (medical_record_id, treatment, date)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

# Add more functions here (insert_medical_staff, insert_appointment, etc.)...

class SmartHealthGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Health Database")
        self.geometry("800x400")
        self.db = "smarthealth.db"

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.patients_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.patients_tab, text="Patients")

        self.create_patient_form()

    def create_patient_form(self):
        # Patient input form
        form_frame = ttk.Frame(self.patients_tab)
        form_frame.pack(side="top", fill="x", pady=10)

        ttk.Label(form_frame, text="First Name:").grid(row=0, column=0, padx=10)
        self.first_name_entry = ttk.Entry(form_frame)
        self.first_name_entry.grid(row=0, column=1, padx=10)

        ttk.Label(form_frame, text="Last Name:").grid(row=0, column=2, padx=10)
        self.last_name_entry = ttk.Entry(form_frame)
        self.last_name_entry.grid(row=0, column=3, padx=10)

        ttk.Label(form_frame, text="Date of Birth:").grid(row=1, column=0, padx=10)
        self.dob_entry = ttk.Entry(form_frame)
        self.dob_entry.grid(row=1, column=1, padx=10)

        ttk.Label(form_frame, text="Gender:").grid(row=1, column=2, padx=10)
        self.gender_entry = ttk.Entry(form_frame)
        self.gender_entry.grid(row=1, column=3, padx=10)

        submit_button = ttk.Button(form_frame, text="Add Patient", command=self.add_patient)
        submit_button.grid(row=2, column=0, columnspan=4, pady=10)

        # Patient list
        list_frame = ttk.Frame(self.patients_tab)
        list_frame.pack(side="top", fill="both", expand=True)

        self.patient_list = ttk.Treeview(list_frame, columns=("First Name", "Last Name", "Date of Birth", "Gender"), show="headings")
        self.patient_list.heading("First Name", text="First Name")
        self.patient_list.heading("Last Name", text="Last Name")
        self.patient_list.heading("Date of Birth", text="Date of Birth")
        self.patient_list.heading("Gender", text="Gender")
        self.patient_list.column("First Name", stretch=True, width=        200)
        self.patient_list.column("Last Name", stretch=True, width=200)
        self.patient_list.column("Date of Birth", stretch=True, width=200)
        self.patient_list.column("Gender", stretch=True, width=200)
        self.patient_list.pack(fill='both', expand=True)

        self.refresh_patient_list()

    def add_patient(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_entry.get()

        conn = create_connection(self.db)
        insert_patient(conn, first_name, last_name, dob, gender)
        conn.close()

        self.refresh_patient_list()

    def refresh_patient_list(self):
        for row in self.patient_list.get_children():
            self.patient_list.delete(row)

        conn = create_connection(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, date_of_birth, gender FROM Patients;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        for row in rows:
            self.patient_list.insert('', 'end', values=row)


if __name__ == "__main__":
    app = SmartHealthGUI()
    app.mainloop()



