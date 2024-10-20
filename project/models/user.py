import uuid


class User:
    def __init__(self, name: str):
        """
        Initialize a User instance.

        :param name: str: The name of the user.
        """
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.comments_count: int = 0
        self.rate: int = 0
        self.is_banned: bool = False

    def edit_name(self, new_name: str):
        """
        Edit the user's name.

        :param new_name: str: The new name to set.
        """
        self.name = new_name

    def increment_rate(self):
        """
        Increment the user's rate by 1.
        """
        self.rate += 1

    def ban_user(self):
        """
        Ban the user by setting the 'is_banned' flag to True.
        """
        self.is_banned = True

    def unban_user(self):
        """
        Unban the user by setting the 'is_banned' flag to False.
        """
        self.is_banned = False

    def __repr__(self) -> str:
        """
        Return a string representation of the user.

        :return: String representation of the user.
        """
        return (
            f"User(id={self.id}, name='{self.name}', rate={self.rate}, "
            f"is_banned={self.is_banned}, comments_count={self.comments_count})"
        )
