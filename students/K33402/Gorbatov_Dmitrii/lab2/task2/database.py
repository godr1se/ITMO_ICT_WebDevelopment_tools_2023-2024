from sqlmodel import SQLModel, create_engine, Session, Field

db_url = 'postgresql://postgres:123@localhost/db_lab2'
engine = create_engine(db_url, echo=False)

class Site(SQLModel, table=True):
    id: int = Field(primary_key=True)
    url: str
    title: str
    method: str

def get_session() -> Session:
    return Session(bind=engine)

def init_db():
    SQLModel.metadata.create_all(engine)