# titanic-data-analysis

Project Overview:

This project focuses on analyzing the Titanic dataset, which includes details about the passengers who were onboard the RMS Titanic when it sank in 1912. The main objectives of the project are to import data from a CSV file into a PostgreSQL database, perform data analysis using SQL queries, and demonstrate data handling and database management skills.

**Tools and Technologies Used**

Python: Used for scripting and automating the data import process.
Pandas: Employed for data manipulation and analysis.
SQLAlchemy: Utilized to interact with the PostgreSQL database from Python.
PostgreSQL: The database used to store and manage the Titanic data.
Git: For version control and tracking changes to the project.
GitHub: To host the repository and share the project.
Apache Airflow: Although not used in active data workflows for this project, Airflow was set up and configured, ready to automate potential future workflows

**Project Structure**

titanic-data-analysis/
└── titanic.csv             # Dataset file
└── extract_data.py         # Script to load data into PostgreSQL
└── README.md                   # Project documentation

**Data Preparation and Loading**

Data Extraction:
The Titanic CSV data was loaded into a Pandas DataFrame to inspect and understand the data structure.

Database Setup:
A PostgreSQL database was set up to store the Titanic data.
A table was created with appropriate data types for each column.

Data Loading:
Data from the DataFrame was cleaned and loaded into the PostgreSQL database using SQLAlchemy to handle database connections and transactions.

Data Analysis:
SQL queries were executed to analyze the data:
Count of survivors.
Distribution of passengers by class.
Average fare and age calculations.

Version Control:
Git was used throughout the project for version control.
Regular commits were made to track changes and document the development process.
The project was pushed to GitHub, providing a backup and showcasing the work for potential recruiters and peers.


**How to Run the Project**

Clone the Repository:
git clone https://github.com/shivamgsmi19/titanic-data-analysis.git
cd titanic-data-analysis

Set Up Your Python Environment:
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt

Run the Scripts:
python extract_data.py

Perform Data Analysis:
Connect to your PostgreSQL database using any SQL client.

**Conclusion:**
This project not only provides insights into the tragic Titanic event but also showcases the use of various data engineering tools and techniques to manage and analyze data efficiently. It demonstrates the ability to integrate Python with SQL databases for data science and data engineering applications.

