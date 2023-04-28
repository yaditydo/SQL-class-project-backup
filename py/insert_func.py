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


def insert_medical_staff(connection, first_name, last_name, role, specialty):
    cursor = connection.cursor()
    query = """
    INSERT INTO MedicalStaff (first_name, last_name, role, specialty)
    VALUES (?, ?, ?, ?);
    """
    data = (first_name, last_name, role, specialty)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_appointment(connection, patient_id, staff_id, appointment_date, appointment_time):
    cursor = connection.cursor()
    query = """
    INSERT INTO Appointments (patient_id, staff_id, appointment_date, appointment_time)
    VALUES (?, ?, ?, ?);
    """
    data = (patient_id, staff_id, appointment_date, appointment_time)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_medical_record(connection, patient_id, staff_id, description, date_created):
    cursor = connection.cursor()
    query = """
    INSERT INTO MedicalRecords (patient_id, staff_id, description, date_created)
    VALUES (?, ?, ?, ?);
    """
    data = (patient_id, staff_id, description, date_created)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_billing(connection, patient_id, staff_id, service, cost, payment_status):
    cursor = connection.cursor()
    query = """
    INSERT INTO Billing (patient_id, staff_id, service, cost, payment_status)
    VALUES (?, ?, ?, ?, ?);
    """
    data = (patient_id, staff_id, service, cost, payment_status)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_inventory(connection, item_name, item_description, quantity):
    cursor = connection.cursor()
    query = """
    INSERT INTO Inventory (item_name, item_description, quantity)
    VALUES (?, ?, ?);
    """
    data = (item_name, item_description, quantity)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_clinic_resource(connection, resource_name, resource_description, quantity):
    cursor = connection.cursor()
    query = """
    INSERT INTO ClinicResources (resource_name, resource_description, quantity)
    VALUES (?, ?, ?);
    """
    data = (resource_name, resource_description, quantity)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_clinic_location(connection, address, city, state, zip_code):
    cursor = connection.cursor()
    query = """
    INSERT INTO ClinicLocations (address, city, state, zip_code)
    VALUES (?, ?, ?, ?);
    """
    data = (address, city, state, zip_code)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()


def insert_patient_clinic_location(connection, patient_id, location_id):
    cursor = connection.cursor()
    query = """
        INSERT INTO PatientClinicLocation (patient_id, location_id)
    VALUES (?, ?);
    """
    data = (patient_id, location_id)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

def insert_medical_staff_clinic_location(connection, staff_id, location_id):
    cursor = connection.cursor()
    query = """
    INSERT INTO MedicalStaffClinicLocation (staff_id, location_id)
    VALUES (?, ?);
    """
    data = (staff_id, location_id)
    cursor.execute(query, data)
    connection.commit()
    cursor.close()



