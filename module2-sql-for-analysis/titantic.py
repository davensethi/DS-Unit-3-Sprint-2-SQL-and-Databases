"""Not sure what the hell I am doing"""

import pandas as pd



df = pd.read_csv('titanic.csv')
print(df.info())

the_list = [tuple(r) for r in df.to_numpy()]

create_table_statement = """
    CREATE TABLE test_table(
    id SERIAL PRIMARY KEY,
    Survived,
    Pclass,
    Name,
    Sex,
    Age,
    data JSONB
    );
"""