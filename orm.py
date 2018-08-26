import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

TEST_DB = 's53821__test_index'
PROD_DB = 's51434__mixnmatch_large_catalogs'
DODO_DB = 's53821__orm_connection_test'
HOST = 'tools.db.svc.eqiad.wmflabs'
USER = 'root'
PASSWORD = 'dba'

#s53821'@'10.68.23.58'

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:dba@localhost/soweego', echo=True)

metadata = MetaData(engine)
table = Table('test', metadata,
    Column('Id', Integer, primary_key=True, nullable=False), 
    Column('Name', Integer),
    metadata.create_all())
table.create()
