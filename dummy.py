import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

fake = Faker()
fake_data = defaultdict(list)
for _ in range(1000):
    fake_data["id"].append(_)
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )
df_fake_data = pd.DataFrame(fake_data)
engine = create_engine('mysql://root:@localhost/sufyan', echo=False)
df_fake_data.to_sql('userinformations', con=engine,index=False)