from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from app.schemas.user import UserCreate, UserLogin, Token, UserResponse
from app.models.user import User
from app.utils.password import get_password_hash, verify_password
from app.auth.jwt_handler import create_access_token
from app.config import settings

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate):
    if User.objects(username=user_data.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    user = User(
        username=user_data.username,
        hashed_password=get_password_hash(user_data.password),
        role=user_data.role
    )
    user.save()
    
    return UserResponse(username=user.username, role=user.role)
 
@router.post("/login", response_model=Token)
async def login(user_data: UserLogin):
    user = User.objects(username=user_data.username).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token)
