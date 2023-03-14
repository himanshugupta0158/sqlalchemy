import db
from sqlalchemy.sql import text

query = text("""
SELECT * FROM transactions
""")

data = ( { "transaction_id": 25, "date": "2023/03/11", "item_id": 265, "price" : 56 },
             { "transaction_id": 26, "date": "2023/03/11", "item_id": 656, "price" : 51},
    )

insert_data = []

for i in data:
    insert_data.append(text(f"""INSERT INTO transactions(transaction_id, date, item_id, price) VALUES({i["transaction_id"]}, {i['date']}, {i['item_id']}, {i['price']})"""))

# insert = text("""INSERT INTO transactions(transaction_id, date, item_id, price) VALUES(:transaction_id, :date, :item_id, :price)""")


with db.engine.connect() as con :

    # insert into db
    # for st in insert_data:
    #     print(st)
    #     con.execute(st)


    # query db
    rs = con.execute(statement=query)
    print(rs)
    for row in rs:
        print(row)