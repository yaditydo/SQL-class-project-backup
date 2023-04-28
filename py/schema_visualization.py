import networkx as nx
import matplotlib.pyplot as plt

# Define the nodes and edges for the graph
entities = [
    'Patients', 'MedicalStaff', 'Appointments', 'MedicalRecords', 'Billing', 'Inventory', 'ClinicResources', 'ClinicLocations', 'PatientClinicLocations', 'MedicalstaffClinicLocations', 'Prescriptions', 'Allergies'
]

edges = [
    ("Patients", "Appointments"),
    ("MedicalStaff", "Appointments"),
    ("Patients", "Prescriptions"),
    ("MedicalStaff", "Prescriptions"),
    ("Patients", "Billing"),
    ("MedicalStaff", "Billing"),
    ("Patients", "PatientClinicLocations"),
    ("ClinicLocations", "PatientClinicLocations"),
    ("Patients", "MedicalRecords"),
    ("MedicalStaff", "MedicalRecords"),
    ("Patients", "Allergies"),
    ("MedicalStaff", "MedicalstaffClinicLocations"),
    ("ClinicLocations", "MedicalstaffClinicLocations"),
    ("Inventory", "ClinicResources"),
    ("ClinicLocations", "ClinicResources"),
]

# Create the graph and add nodes and edges
G = nx.Graph()
G.add_nodes_from(entities)
G.add_edges_from(edges)

# Define the layout for the visualization
pos = nx.spring_layout(G, k=1, seed=42)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=1600, node_color='lightblue', font_size=12, font_weight='bold', width=2)
plt.show()


