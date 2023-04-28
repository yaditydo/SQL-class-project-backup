import graphviz

entities = [
    'Patients', 'MedicalStaff', 'Appointments', 'MedicalRecords', 'Billing', 'Inventory', 'ClinicResources', 'ClinicLocations', 'PatientClinicLocations', 'MedicalStaffClinicLocations', 'Prescriptions', 'Allergies'
]

# Create a new Digraph object
erd = graphviz.Graph('ERD', format='png', engine='neato')

# Define node and edge styles
erd.attr('node', shape='ellipse', style='filled', fillcolor='lightblue', fontname='Arial', fontsize='12', fontcolor='black')
erd.attr('edge', fontsize='10', fontname='Arial', fontcolor='black')

# Add nodes to the graph
for entity in entities:
    erd.node(entity)

# Add edges to the graph with crow's foot notation
edges = [
    ('Patients', 'Appointments'),
    ('MedicalStaff', 'Appointments'),
    ('Patients', 'Prescriptions'),
    ('MedicalStaff', 'Prescriptions'),
    ('Patients', 'Billing'),
    ('MedicalStaff', 'Billing'),
    ('Patients', 'MedicalRecords'),
    ('MedicalStaff', 'MedicalRecords'),
    ('Patients', 'Allergies'),
    ('Patients', 'PatientClinicLocations'),
    ('ClinicLocations', 'PatientClinicLocations'),
    ('MedicalStaff', 'MedicalStaffClinicLocations'),
    ('ClinicLocations', 'MedicalStaffClinicLocations'),
    ('ClinicResources', 'Inventory'),
    ('ClinicResources', 'ClinicLocations'),
]

for edge in edges:
    if edge[0] == "Patients" or edge[0] == "MedicalStaff":
        arrowtail = "crowodot"
    else:
        arrowtail = "crow"

    erd.edge(edge[0], edge[1], dir='both', arrowtail=arrowtail, arrowhead='none')

# Render the graph to a file
erd.attr(overlap='false', size='10,10', dpi='100')
erd.render('erd_output', view=True)



