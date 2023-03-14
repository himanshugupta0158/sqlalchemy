import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

# All data
for s in session.query(db.transaction).all():
    print(s.transaction_id, s.date, s.price)


print("*"*20)
print("Transaction with price over 40 : ")

# selected data
for s in session.query(db.transaction).filter(db.transaction.price > 40):
    print(s.transaction_id, s.date, s.price)

