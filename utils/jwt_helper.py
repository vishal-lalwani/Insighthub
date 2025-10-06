# utils/jwt_helper.py
# NOTE: for now we use flask_jwt_extended directly in routes.
# This module is a placeholder for any JWT helper functions you'd like to add,
# e.g. helper to create tokens with custom expiry, or to parse identity.
from flask_jwt_extended import create_access_token

def make_access_token(identity, expires_delta=None):
    """
    identity: a JSON-serializable payload (e.g., {'id': 1, 'role':'admin'})
    expires_delta: datetime.timedelta or None
    """
    return create_access_token(identity=identity, expires_delta=expires_delta)
