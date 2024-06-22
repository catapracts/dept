from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List

# FastAPI 애플리케이션 생성
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# SQLAlchemy 설정
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost/test1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 데이터베이스 모델 정의
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(255))

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# SQLAlchemy Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 값을 저장하는 POST 메소드
class DataItem(BaseModel):
    value: str

@app.post("/add", response_model=DataItem)
def store_value(item: DataItem, db: Session = Depends(get_db)):
    db_item = Item(value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 가장 최근에 저장한 값을 반환하는 GET 메소드
@app.get("/get", response_model=DataItem)
def retrieve_value(db: Session = Depends(get_db)):
    db_item = db.query(Item).order_by(Item.id.desc()).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="No stored values")
    return db_item

# 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
