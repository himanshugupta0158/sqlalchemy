from sqlalchemy import create_engine , Column
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Connect & create with database
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
base = declarative_base()


# create db table
class transaction(base):

    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)

    def __init__(self, transaction_id, date, item_id, price):
        self.transaction_id = transaction_id
        self.date = date
        self.item_id = item_id
        self.price = price

base.metadata.create_all(engine)