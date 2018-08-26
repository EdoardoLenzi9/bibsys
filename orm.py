import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

TEST_DB = 's53821__test_index'
PROD_DB = 's51434__mixnmatch_large_catalogs'
DODO_DB = 's53821__orm_connection_test'
HOST = 'tools.db.svc.eqiad.wmflabs'


Base = declarative_base()
engine = create_engine('mysql://{0}@{1}/{2}'.format('edoardolenzi', 'tools.db.svc.eqiad.wmflabs', 's53821__orm_connection_test'), pool_recycle=3600, echo=True)

if not engine.dialect.has_table(engine, 'test'):  # If table don't exist, Create.
    metadata = MetaData(engine)
    Table('test', metadata,
        Column('Id', Integer, primary_key=True, nullable=False), 
        Column('Name', String),
    metadata.create_all())
