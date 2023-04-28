import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import sqlite3
from py.insert_func import *

def fetch_data(table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    cursor.close()
    return data


def display_data(text_widget, data):
    text_widget.delete(1.0, tk.END)
    for row in data:
        text_widget.insert(tk.END, str(row) + '\n')


class SmartHealthGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Health Database")
        self.geometry("1000x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.create_patient_tab()
        self.create_medical_staff_tab()
        self.create_appointment_tab()
        self.create_medical_record_tab()
        self.create_billing_tab()
        self.create_inventory_tab()
        self.create_clinic_resource_tab()
        self.create_clinic_location_tab()
        self.create_patient_clinic_location_tab()
        self.create_medical_staff_clinic_location_tab()
        self.create_prescription_tab()
        self.create_allergy_tab()

    def create_patient_tab(self):
        self.patient_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.patient_tab, text="Patients")

        self.patient_text = scrolledtext.ScrolledText(self.patient_tab, wrap=tk.WORD)
        self.patient_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Patients")
        display_data(self.patient_text, data)
    def create_medical_staff_tab(self):
        self.medical_staff_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.medical_staff_tab, text="Medical Staff")

        self.medical_staff_text = scrolledtext.ScrolledText(self.medical_staff_tab, wrap=tk.WORD)
        self.medical_staff_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("MedicalStaff")
        display_data(self.medical_staff_text, data)

    def create_appointment_tab(self):
        self.appointment_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.appointment_tab, text="Appointments")

        self.appointment_text = scrolledtext.ScrolledText(self.appointment_tab, wrap=tk.WORD)
        self.appointment_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Appointments")
        display_data(self.appointment_text, data)

    def create_medical_record_tab(self):
        self.medical_record_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.medical_record_tab, text="Medical Records")

        self.medical_record_text = scrolledtext.ScrolledText(self.medical_record_tab, wrap=tk.WORD)
        self.medical_record_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("MedicalRecords")
        display_data(self.medical_record_text, data)

    def create_billing_tab(self):
        self.billing_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.billing_tab, text="Billing")

        self.billing_text = scrolledtext.ScrolledText(self.billing_tab, wrap=tk.WORD)
        self.billing_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Billing")
        display_data(self.billing_text, data)

    def create_inventory_tab(self):
        self.inventory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_tab, text="Inventory")

        self.inventory_text = scrolledtext.ScrolledText(self.inventory_tab, wrap=tk.WORD)
        self.inventory_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Inventory")
        display_data(self.inventory_text, data)

    def create_clinic_resource_tab(self):
        self.clinic_resource_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.clinic_resource_tab, text="Clinic Resources")

        self.clinic_resource_text = scrolledtext.ScrolledText(self.clinic_resource_tab, wrap=tk.WORD)
        self.clinic_resource_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("ClinicResources")
        display_data(self.clinic_resource_text, data)

    def create_clinic_location_tab(self):
        self.clinic_location_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.clinic_location_tab, text="Clinic Locations")

        self.clinic_location_text = scrolledtext.ScrolledText(self.clinic_location_tab, wrap=tk.WORD)
        self.clinic_location_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("ClinicLocations")
        display_data(self.clinic_location_text, data)

    def create_patient_clinic_location_tab(self):
        self.patient_clinic_location_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.patient_clinic_location_tab, text="Patient Clinic Locations")

        self.patient_clinic_location_text = scrolledtext.ScrolledText(self.patient_clinic_location_tab, wrap=tk.WORD)
        self.patient_clinic_location_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("PatientClinicLocation")
        display_data (self.patient_clinic_location_text, data)

    def create_medical_staff_clinic_location_tab(self):
        self.medical_staff_clinic_location_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.medical_staff_clinic_location_tab, text="Medical Staff Clinic Locations")

        self.medical_staff_clinic_location_text = scrolledtext.ScrolledText(self.medical_staff_clinic_location_tab, wrap=tk.WORD)
        self.medical_staff_clinic_location_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("MedicalStaffClinicLocation")
        display_data(self.medical_staff_clinic_location_text, data)

    def create_prescription_tab(self):
        self.prescription_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.prescription_tab, text="Prescriptions")

        self.prescription_text = scrolledtext.ScrolledText(self.prescription_tab, wrap=tk.WORD)
        self.prescription_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Prescriptions")
        display_data(self.prescription_text, data)

    def create_allergy_tab(self):
        self.allergy_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.allergy_tab, text="Allergies")

        self.allergy_text = scrolledtext.ScrolledText(self.allergy_tab, wrap=tk.WORD)
        self.allergy_text.pack(fill=tk.BOTH, expand=True)

        data = fetch_data("Allergies")
        display_data(self.allergy_text, data)


    # Add similar functions for other tabs

    # ...


if __name__ == "__main__":
    #connection to the database
    connection = sqlite3.connect("smarthealth.db")

    app = SmartHealthGUI()
    app.mainloop()

    connection.close()
