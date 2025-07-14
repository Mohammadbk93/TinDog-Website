from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db_config import SessionLocal, engine, Base  
import models, schemas
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from utils import hash_password


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#  CORS middleware setup
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  API endpoint for user registration
@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),  
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head><title>Tindog API</title></head>
        <body>
            <h1>🚀 Tindog API is running!</h1>
            <p>Use <code>/register</code> endpoint to register users.</p>
        </body>
    </html>
    """

