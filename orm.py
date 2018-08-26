import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format('root', 'dba', '127.0.0.1:3306', 'soweego'), pool_recycle=3600, echo=True)

if not engine.dialect.has_table(engine, 'stocazzo'):  # If table don't exist, Create.
    metadata = MetaData(engine)
    Table('stocazzo', metadata,
        Column('Id', Integer, primary_key=True, nullable=False), 
        Column('Country', String),
        Column('Brand', String),
    # Implement the creation
    metadata.create_all())