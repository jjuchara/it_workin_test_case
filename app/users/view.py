from sqlalchemy.orm import Session
import bcrypt
import app.models as models
import app.users.schemas as schemas


def get_user_by_username(db: Session, username: str) -> schemas.User:
    """
    find user in db with sertain esername
    """

    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate) -> schemas.User:
    """Create user in db and hashed password"""

    hashed_password = bcrypt.hashpw(
        user.hashed_password.encode("utf-8"), bcrypt.gensalt()
    )
    db_user = models.User(
        username=user.username,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address,
        avatar=user.avatar,
        hashed_password=hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
