Code for database class project.
Scenario: Smarthealth Clinic has hired AICodeAssemblers Consulting LLC. to aid in the construction in a new database. In a real life scenario ideally level's of privelege as to data access and AES-256-CBC would be implemented across the database to protect customer/patient medical data. Unfortunately I couldn't get sqlcipher3 to install properly so wasn't able to implement it
python --version == '10.10.10'. 
to run any files toy must first activate the virtual environment for all included file dependencies
- Windows - run env/Scripts/activate to activate the virtual environment installed dependencies
- Linux/Unix 'source env/bin/activate' For Linux or Unix System Environments to activate the virtual environment installed dependencies
- `cd py - source code files`
- `python [file].py` in the command line to execute the code. or run the file
- `python create_database.py` #Creates 'smarthealth.db'
- `python crowsfoot.py` Used the python package graphviz to visualize the Schema using crowsfoot notation
- `python insert_dummydata.py` seperate script used to insert dummy data
- insert_func.py - contains functions to insert data into the database v
- `python Insert_data-GUI.py` : creats a GUI using tkinter and a tab for each individual table with input forms to insert the data through a graphical interface autmatically
- `python schema_visualization.py` : database schema visualization
- `python schema_visualization2.py` : different python packages for visualization
- `python View-database.py` - tkinter GUI for the database
- erd_output.png = Entity relational Diagram

If for any reason a file doesn't run here are all packages used:
- sqlite3
- tkinter, ttkthemes
- networkx (visualization)
- matplotlib (visualization)
- graphviz (visualization)
