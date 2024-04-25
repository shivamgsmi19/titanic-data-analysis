import pandas as pd
from sqlalchemy import create_engine

pd.set_option('display.max_columns', None)

def load_csv(filename):
    """Load the CSV file into a pandas DataFrame."""
    data = pd.read_csv(filename)  #data here is also known as DataFrame
    data.rename(columns={
    'Survived': 'survived',
    'Pclass': 'pclass',
    'Name': 'name',
    'Sex': 'sex',
    'Age': 'age',
    'Siblings/Spouses Aboard': 'siblings_spouses_aboard',  # Correcting to match the DB column name
    'Parents/Children Aboard': 'parents_children_aboard',  # Correcting to match the DB column name
    'Fare': 'fare'
    }, inplace=True)

    return data

def main():
    db_url = 'postgresql://shivam:@localhost:5432/postgres'
    engine = create_engine(db_url)

    filename = '/Users/shivam/Downloads/titanic.csv'  # Replace this with your CSV file path
    data = load_csv(filename)
    data.to_sql('passengers', con=engine, index=False, if_exists='append') 
    print("Data inserted into database successfully.")
    #print(data.head())  # Display the first few rows of the data

if __name__ == "__main__":
    main()

