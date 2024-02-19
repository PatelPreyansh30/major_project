from base import db
from base.com.vo.user_vo import UserVO


class UserDAO:
    def intert_user(self, user_vo):
        db.session.add(user_vo)
        db.session.commit()

    def view_one_user(self, user_vo):
        user = UserVO.query.filter_by(
            user_id=user_vo.user_id).first()
        return user

    def update_user(self, user_vo):
        db.session.merge(user_vo)
        db.session.commit()
