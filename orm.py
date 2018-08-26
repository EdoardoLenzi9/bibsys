import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://{0}@{1}/{2}'.format('edoardolenzi', '10.68.23.58', 's53821__orm_connection_test'), pool_recycle=3600, echo=True)

if not engine.dialect.has_table(engine, 'test'):  # If table don't exist, Create.
    metadata = MetaData(engine)
    Table('test', metadata,
        Column('Id', Integer, primary_key=True, nullable=False), 
        Column('Name', String),
    metadata.create_all())
