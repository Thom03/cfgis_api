import jwt
from datetime import datetime, timedelta
from config import settings


def handle_token(user):
    """
    Generate and return token
    """

    date = datetime.now() + timedelta(hours=24)
    token = jwt.encode({
        'email': user.email,
        'isAdmin': user.is_superuser,
        'exp': int(date.strftime('%s'))},
        settings.SECRET_KEY,
        algorithm='HS256').decode('utf-8')

    return token
