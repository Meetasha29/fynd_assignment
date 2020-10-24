from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from connectors.database import db


class BaseModel(db.Model):
    """
    Store Meta data for all the tables
    """

    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), index=True)


class User(BaseModel):
    """
    Table to store User details
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, index=True)
    password = db.Column(db.String(200))
    auth_token = db.Column(db.String(200), unique=True, index=True)

    permissions = db.relationship("UserPermissionMapping")

    def __repr__(self):
        return "<User(username={})>".format(self.username)

    def to_dict(self):
        _user_data = {
            "id": self.id,
            "username": self.username,
            "auth_token": self.auth_token,
            "permissions": [permission.to_dict() for permission in self.permissions],
        }
        return _user_data


class Permissions(BaseModel):
    """
    Table to store permission details
    """

    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    permission_code = db.Column(db.String(100), unique=True, index=True)
    permission_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Permissions(permission_code={})>".format(self.permission_code)

    def to_dict(self):
        permission_data = {
            "id": self.id,
            "permission_code": self.permission_code,
            "permission_name": self.permission_name
        }
        return permission_data


class UserPermissionMapping(BaseModel):
    """
    Table to store user permission mappings
    """

    __tablename__ = "user_permission_map"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('users.username'), nullable=False, index=True)
    permission_code = db.Column(db.String(100), db.ForeignKey('permissions.permission_code'), nullable=False, index=True)

    def __repr__(self):
        return "<UserPermissionMapping(username={}-perm_code={})>".format(
            self.username, self.permission_code)

    def to_dict(self):
        _data = {
            "id": self.id,
            "username": self.username,
            "permission_code": self.permission_code
        }
        return _data


class Movie(BaseModel):
    """
    Table to store Movies details
    """

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    director = db.Column(db.String(200), index=True)
    imdb_score = db.Column(db.Float, index=True)
    popularity_99 = db.Column(db.Float)
    genre = db.Column(JSONB)

    def __repr__(self):
        return "<Movie(name={})>".format(self.name)

    def to_dict(self):
        _movie_data = {
            "id": self.id,
            "name": self.name,
            "director": self.director,
            "imdb_score": self.imdb_score,
            "popularity_99": self.popularity_99,
            "genre": self.genre,
        }
        return _movie_data

