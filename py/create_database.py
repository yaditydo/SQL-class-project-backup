import sqlite3
connection = sqlite3.connect("smarthealth.db")
cursor = connection.cursor()

create_table_queries = [
    # Patients
    """
    CREATE TABLE IF NOT EXISTS Patients (
        patient_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        gender TEXT NOT NULL
    );
    """,
    # MedicalStaff
    """
    CREATE TABLE IF NOT EXISTS MedicalStaff (
        staff_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        role TEXT NOT NULL,
        specialty TEXT
    );
    """,
    # Appointments
    """
    CREATE TABLE IF NOT EXISTS Appointments (
        appointment_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        staff_id INTEGER NOT NULL,
        appointment_date TEXT NOT NULL,
        appointment_time TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id)
    );
    """,
    # MedicalRecords
    """
    CREATE TABLE IF NOT EXISTS MedicalRecords (
        record_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        staff_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        date_created TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id)
    );
    """,
    # Billing
    """
    CREATE TABLE IF NOT EXISTS Billing (
        billing_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        staff_id INTEGER NOT NULL,
        service TEXT NOT NULL,
        cost REAL NOT NULL,
        payment_status TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id)
    );
    """,
    # Inventory
    """
    CREATE TABLE IF NOT EXISTS Inventory (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        item_description TEXT,
        quantity INTEGER NOT NULL
    );
    """,
    # ClinicResources
    """
    CREATE TABLE IF NOT EXISTS ClinicResources (
        resource_id INTEGER PRIMARY KEY,
        resource_name TEXT NOT NULL,
        resource_description TEXT,
        quantity INTEGER NOT NULL
    );
    """,
    # ClinicLocations
    """
    CREATE TABLE IF NOT EXISTS ClinicLocations (
        location_id INTEGER PRIMARY KEY,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        zip_code TEXT NOT NULL
    );
    """,
    # PatientClinicLocation
    """
    CREATE TABLE IF NOT EXISTS PatientClinicLocation (
        patient_id INTEGER NOT NULL,
        location_id INTEGER NOT NULL,
        PRIMARY KEY (patient_id, location_id),
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (location_id) REFERENCES ClinicLocations(location_id)
    );
    """,
    # MedicalStaffClinicLocation
    """
    CREATE TABLE IF NOT EXISTS MedicalStaffClinicLocation (
        staff_id INTEGER NOT NULL,
        location_id INTEGER NOT NULL,
        PRIMARY KEY (staff_id, location_id),
        FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id),
        FOREIGN KEY (location_id) REFERENCES ClinicLocations(location_id)
    );
    """,
    # Prescriptions
    """
    CREATE TABLE IF NOT EXISTS Prescriptions (
        prescription_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        staff_id INTEGER NOT NULL,
        medication TEXT NOT NULL,
        dosage TEXT NOT NULL,
        duration TEXT NOT NULL,
        date_prescribed TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
        FOREIGN KEY (staff_id) REFERENCES MedicalStaff(staff_id)
    );
    """,
    # Allergies
    """
    CREATE TABLE IF NOT EXISTS Allergies (
        allergy_id INTEGER PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        allergy_name TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
    );
    """
]

if __name__ == "__main__":
    for query in create_table_queries:
        cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()

    








