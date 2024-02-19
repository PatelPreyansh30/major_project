from base import db,app

class UserVO(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id', db.Integer,
                        primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)
    user = db.Column('user', db.String(255), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'user': self.user
        }

with app.app_context():
    db.create_all()