from sqlalchemy.orm import Session
import bcrypt
import app.models as models
import app.users.schemas as schemas


def get_user_by_username(db: Session, username: str) -> schemas.User:
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = models.User(
        username=user.username,
        phone_number=user.phone_number,
        address=user.address,
        avatar=user.avatar,
        password=hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
