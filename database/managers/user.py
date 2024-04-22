from ascend.app import db
from ascend.database.models import User
from ascend.database.schemas.user import UserSchema


class UserManager:
    """
    Contains methods to manage User data.
    """

    @staticmethod
    def get(filter_values, all_users=False):
        """
        Retrieves User records based on filters.

        :param filter_values: A dictionary containing filter criteria (e.g., {'id': 123}).
        :param all_users: A boolean flag indicating whether to retrieve all users with a similar email domain (e.g., "@gmail.com").
        :return: A list of User objects or None if an error occurs.
        """

        try:
            query = db.session.query(User)
            if all_users:
                email_domain = filter_values["email"].split("@")[-1]
                query = query.filter(User.email.like(f"%@{email_domain}"))
            else:
                query = query.filter_by(**filter_values)
            return query.all()

        except Exception as e:
            db.session.rollback()
            print(f"Error retrieving users: {e}")
            return None

    @staticmethod
    def create(user_data):
        """
        Creates a new User instance.

        :param user_data: A dictionary containing user data (e.g., {'username': 'johndoe', 'email': 'johndoe@example.com'}).
        :return: A newly created User object or None if an error occurs.
        """

        try:
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return None

    @staticmethod
    def serialize_user(user):
        """
        Serializes a User object into a dictionary representation.

        :param user: A User object.
        :return: A dictionary containing user data.
        """

        user_schema = UserSchema()
        return user_schema.dump(user)
