import sqlite3
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from py.insert_func import *
# Connect to the database
connection = sqlite3.connect('smarthealth.db')

# Create the main window
root = ThemedTk(theme='arc')
root.title('SmartHealth')
root.geometry('600x400')

# Create a tab control
tab_control = ttk.Notebook(root)
tab_control.pack(expand=True, fill='both')

# Function to create an entry widget with a label
def create_entry_with_label(parent, label_text, row, column):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row, column=column, padx=5, pady=5, sticky='w')
    entry = ttk.Entry(parent)
    entry.grid(row=row, column=column+1, padx=5, pady=5, sticky='w')
    return entry

# Function to create a button with a callback function
def create_button(parent, text, command, row, column):
    button = ttk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, padx=5, pady=5, sticky='w')
    return button

# Insert functions callbacks
def insert_patient_callback():
    first_name = patient_first_name_entry.get()
    last_name = patient_last_name_entry.get()
    date_of_birth = patient_dob_entry.get()
    gender = patient_gender_entry.get()
    insert_patient(connection, first_name, last_name, date_of_birth, gender)

def insert_medical_staff_callback():
    first_name = ms_first_name_entry.get()
    last_name = ms_last_name_entry.get()
    role = ms_role_entry.get()
    specialty = ms_specialty_entry.get()
    insert_medical_staff(connection, first_name, last_name, role, specialty)

def insert_appointment_callback():
    patient_id = appointment_patient_id_entry.get()
    staff_id = appointment_staff_id_entry.get()
    appointment_date = appointment_date_entry.get()
    appointment_time = appointment_time_entry.get()
    insert_appointment(connection, patient_id, staff_id, appointment_date, appointment_time)

def insert_medical_record_callback():
    patient_id = mr_patient_id_entry.get()
    staff_id = mr_staff_id_entry.get()
    description = mr_description_entry.get()
    date_created = mr_date_created_entry.get()
    insert_medical_record(connection, patient_id, staff_id, description, date_created)

def insert_billing_callback():
    patient_id = billing_patient_id_entry.get()
    staff_id = billing_staff_id_entry.get()
    service = billing_service_entry.get()
    cost = billing_cost_entry.get()
    payment_status = billing_payment_status_entry.get()
    insert_billing(connection, patient_id, staff_id, service, cost, payment_status)

def insert_inventory_callback():
    item_name = inventory_item_name_entry.get()
    item_description = inventory_item_description_entry.get()
    quantity = inventory_quantity_entry.get()
    insert_inventory(connection, item_name, item_description, quantity)

def insert_clinic_resource_callback():
    resource_name = clinic_resource_name_entry.get()
    resource_description = clinic_resource_description_entry.get()
    quantity = clinic_resource_quantity_entry.get()
    insert_clinic_resource(connection, resource_name, resource_description, quantity)

def insert_clinic_location_callback():
    address = clinic_location_address_entry.get()
    city = clinic_location_city_entry.get()
    state = clinic_location_state_entry.get()
    zip_code = clinic_location_zip_code_entry.get()
    insert_clinic_location(connection, address, city, state, zip_code)

def insert_patient_clinic_location_callback():
    patient_id = patient_clinic_location_patient_id_entry.get()
    location_id = patient_clinic_location_location_id_entry.get()
    insert_patient_clinic_location(connection, patient_id, location_id)

def insert_medical_staff_clinic_location_callback():
    staff_id = medical_staff_clinic_location_staff_id_entry.get()
    location_id = medical_staff_clinic_location_location_id_entry.get()
    insert_medical_staff_clinic_location(connection, staff_id, location_id)

# Create the tabs
patients_tab = ttk.Frame(tab_control)
tab_control.add(patients_tab, text='Patients')

medical_staff_tab = ttk.Frame(tab_control)
tab_control.add(medical_staff_tab, text='Medical Staff')

appointments_tab = ttk.Frame(tab_control)
tab_control.add(appointments_tab, text='Appointments')

medical_records_tab = ttk.Frame(tab_control)
tab_control.add(medical_records_tab, text='Medical Records')

billing_tab = ttk.Frame(tab_control)
tab_control.add(billing_tab, text='Billing')

inventory_tab = ttk.Frame(tab_control)
tab_control.add(inventory_tab, text='Inventory')

clinic_resources_tab = ttk.Frame(tab_control)
tab_control.add(clinic_resources_tab, text='Clinic Resources')

clinic_locations_tab = ttk.Frame(tab_control)
tab_control.add(clinic_locations_tab, text='Clinic Locations')

patient_clinic_locations_tab = ttk.Frame(tab_control)
tab_control.add(patient_clinic_locations_tab, text='Patient Clinic Locations')

medical_staff_clinic_locations_tab = ttk.Frame(tab_control)
tab_control.add(medical_staff_clinic_locations_tab, text='Medical Staff Clinic Locations')

# Create the entry widgets with labels and buttons
patient_first_name_entry = create_entry_with_label(patients_tab, 'First Name:', 0, 0)
patient_last_name_entry = create_entry_with_label(patients_tab, 'Last Name:', 1, 0)
patient_dob_entry = create_entry_with_label(patients_tab, 'Date of Birth:', 2, 0)
patient_gender_entry = create_entry_with_label(patients_tab, 'Gender:', 3, 0)
create_button(patients_tab, 'Insert Patient', insert_patient_callback, 4, 0)

ms_first_name_entry = create_entry_with_label(medical_staff_tab, 'First Name:', 0, 0)
ms_last_name_entry = create_entry_with_label(medical_staff_tab, 'Last Name:', 1, 0)
ms_role_entry = create_entry_with_label(medical_staff_tab, 'Role:', 2, 0)
ms_specialty_entry = create_entry_with_label(medical_staff_tab, 'Specialty:', 3, 0)
create_button(medical_staff_tab, 'Insert Medical Staff', insert_medical_staff_callback, 4, 0)

appointment_patient_id_entry = create_entry_with_label(appointments_tab, 'Patient ID:', 0, 0)
appointment_staff_id_entry = create_entry_with_label(appointments_tab, 'Staff ID:', 1, 0)
appointment_date_entry = create_entry_with_label(appointments_tab, 'Appointment Date:', 2, 0)
appointment_time_entry = create_entry_with_label(appointments_tab, 'Appointment Time:', 3, 0)
create_button(appointments_tab, 'Insert Appointment', insert_appointment_callback, 4, 0)

mr_patient_id_entry = create_entry_with_label(medical_records_tab, 'Patient ID:', 0, 0)
mr_staff_id_entry =create_entry_with_label(medical_records_tab, 'Staff ID:', 1, 0)
mr_description_entry = create_entry_with_label(medical_records_tab, 'Description:', 2, 0)
mr_date_created_entry = create_entry_with_label(medical_records_tab, 'Date Created:', 3, 0)
create_button(medical_records_tab, 'Insert Medical Record', insert_medical_record_callback, 4, 0)

billing_patient_id_entry = create_entry_with_label(billing_tab, 'Patient ID:', 0, 0)
billing_staff_id_entry = create_entry_with_label(billing_tab, 'Staff ID:', 1, 0)
billing_service_entry = create_entry_with_label(billing_tab, 'Service:', 2, 0)
billing_cost_entry = create_entry_with_label(billing_tab, 'Cost:', 3, 0)
billing_payment_status_entry = create_entry_with_label(billing_tab, 'Payment Status:', 4, 0)
create_button(billing_tab, 'Insert Billing', insert_billing_callback, 5, 0)

inventory_item_name_entry = create_entry_with_label(inventory_tab, 'Item Name:', 0, 0)
inventory_item_description_entry = create_entry_with_label(inventory_tab, 'Item Description:', 1, 0)
inventory_quantity_entry = create_entry_with_label(inventory_tab, 'Quantity:', 2, 0)
create_button(inventory_tab, 'Insert Inventory Item', insert_inventory_callback, 3, 0)

clinic_resource_name_entry = create_entry_with_label(clinic_resources_tab, 'Resource Name:', 0, 0)
clinic_resource_description_entry = create_entry_with_label(clinic_resources_tab, 'Resource Description:', 1, 0)
clinic_resource_quantity_entry = create_entry_with_label(clinic_resources_tab, 'Quantity:', 2, 0)
create_button(clinic_resources_tab, 'Insert Clinic Resource', insert_clinic_resource_callback, 3, 0)

clinic_location_address_entry = create_entry_with_label(clinic_locations_tab, 'Address:', 0, 0)
clinic_location_city_entry = create_entry_with_label(clinic_locations_tab, 'City:', 1, 0)
clinic_location_state_entry = create_entry_with_label(clinic_locations_tab, 'State:', 2, 0)
clinic_location_zip_code_entry = create_entry_with_label(clinic_locations_tab, 'Zip Code:', 3, 0)
create_button(clinic_locations_tab, 'Insert Clinic Location', insert_clinic_location_callback, 4, 0)

patient_clinic_location_patient_id_entry = create_entry_with_label(patient_clinic_locations_tab, 'Patient ID:', 0, 0)
patient_clinic_location_location_id_entry = create_entry_with_label(patient_clinic_locations_tab, 'Location ID:', 1, 0)
create_button(patient_clinic_locations_tab, 'Insert Patient Clinic Location', insert_patient_clinic_location_callback, 2, 0)

medical_staff_clinic_location_staff_id_entry = create_entry_with_label(medical_staff_clinic_locations_tab, 'Staff ID:', 0, 0)
medical_staff_clinic_location_location_id_entry = create_entry_with_label(medical_staff_clinic_locations_tab, 'Location ID:', 1, 0)
create_button(medical_staff_clinic_locations_tab, 'Insert Medical Staff Clinic Location', insert_medical_staff_clinic_location_callback, 2, 0)

# Run the main event loop
root.mainloop()



