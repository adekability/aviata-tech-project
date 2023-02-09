import sqlalchemy
import config as cfg
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base


engine = sqlalchemy.create_engine(cfg.SQLALCHEMY_DATABASE_URI,
                                  poolclass=NullPool,
                                  pool_pre_ping=True,
                                  connect_args=dict(connect_timeout=30,
                                                    keepalives=1,
                                                    keepalives_idle=5,
                                                    keepalives_interval=2,
                                                    keepalives_count=2))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
