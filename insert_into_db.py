import db
from sqlalchemy.orm import sessionmaker
import random

# new session
Session = sessionmaker(bind=db.engine)
session = Session()


# adding random data
for i in range(10,20):
    item_id = random.randint(0,1000)
    price = random.randint(20,50)

    tr = db.transaction(i, "2023/03/11",item_id, price)
    session.add(tr)


# save changes in database
session.commit()