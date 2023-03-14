from sqlalchemy import update, delete
import db

stmt = delete(db.transaction).where(db.transaction.price < 40)
stmt.compile(bind=db.engine)
print(stmt)