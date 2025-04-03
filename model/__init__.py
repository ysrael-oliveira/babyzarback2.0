from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from model.base import Base
from model.roupa import Roupa

db_path = 'bancodedados/'
# checks if path exists
if not os.path.exists(db_path):
    os.makedirs(db_path)

# create the database
db = create_engine('sqlite:///%s/db.sqlite3' %db_path)

# instantiate a new session, binding with the created database
Session = sessionmaker(bind=db)

# creates database tables
Base.metadata.create_all(db)