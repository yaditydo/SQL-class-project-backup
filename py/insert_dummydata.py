import sqlite3

def insert_patients_data(connection):
    # Insert sample patients data
    query = """
    INSERT INTO Patients (first_name, last_name, date_of_birth, gender)
    VALUES ('John', 'Doe', '1980-06-15', 'Male'),
           ('Jane', 'Doe', '1985-09-10', 'Female');
    """
    connection.execute(query)

def insert_medical_staff_data(connection):
    # Insert sample medical staff data
    query = """
    INSERT INTO MedicalStaff (first_name, last_name, role, specialty)
    VALUES ('Sam', 'Smith', 'Doctor', 'Cardiology'),
           ('Sara', 'Brown', 'Nurse', 'Pediatrics');
    """
    connection.execute(query)

def insert_appointments_data(connection):
    # Insert sample appointments data
    query = """
    INSERT INTO Appointments (patient_id, staff_id, appointment_date, appointment_time)
    VALUES (1, 1, '2023-05-01', '09:00:00'),
           (2, 2, '2023-05-01', '10:00:00');
    """
    connection.execute(query)

def insert_medical_records_data(connection):
    # Insert sample medical records data
    query = """
    INSERT INTO MedicalRecords (patient_id, staff_id, description, date_created)
    VALUES (1, 1, 'Regular checkup. Patient in good health.', '2023-04-01'),
           (2, 2, 'Flu symptoms. Prescribed medication.', '2023-04-15');
    """
    connection.execute(query)

def insert_billing_data(connection):
    # Insert sample billing data
    query = """
    INSERT INTO Billing (patient_id, staff_id, service, cost, payment_status)
    VALUES (1, 1, 'Regular checkup', 120.00, 'Paid'),
           (2, 2, 'Flu consultation', 80.00, 'Unpaid');
    """
    connection.execute(query)

def insert_inventory_data(connection):
    # Insert sample inventory data
    query = """
    INSERT INTO Inventory (item_name, item_description, quantity)
    VALUES ('Surgical gloves', 'Latex-free gloves for medical procedures', 500),
           ('Syringes', 'Disposable syringes for injections', 1000);
    """
    connection.execute(query)

def main():
    try:
        conn = sqlite3.connect("smarthealth.db")

        insert_patients_data(conn)
        insert_medical_staff_data(conn)
        insert_appointments_data(conn)
        insert_medical_records_data(conn)
        insert_billing_data(conn)
        insert_inventory_data(conn)

        conn.commit()

    except sqlite3.Error as err:
        print(f"Error: {err}")
        conn.rollback()

    finally:
        conn.close()

if __name__ == "__main__":
    main()





"""In this schema, we have 8 tables, each representing an entity in the SmartHealth Clinic system. Here are the relationships among them:

1. Patients (1 --- 0..*) Appointments
2. MedicalStaff (1 --- 0..*) Appointments
3. Appointments (1 --- 0..*) MedicalRecords
4. MedicalRecords (1 --- 0..*) MedicalRecords
5. Billing (1 --- 0..*) Billing
6. Inventory (1 --- 0..*) Billing
7. ClinicResources (1 --- 0..*) PatientClinicLocation
8. ClinicLocations (1 --- 0..*) PatientClinicLocation
9. PatientClinicLocation (1 --- 0..*) MedicalStaffClinicLocation
10. MedicalStaffClinicLocation (1 --- 0..*) MedicalStaffClinicLocation
11. Prescriptions
12. Allergies
The relationships are modeled using foreign keys and many-to-many relationships are modeled through junction tables, such as PatientClinicLocation and MedicalStaffClinicLocation."""
