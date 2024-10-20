from datetime import datetime
from uuid import UUID

class Comment:

    def __init__(self, author_id: UUID, text: str):
        """
        Initializes a Comment instance.

        :param author_id: UUID: Unique identifier of the comment's author.
        :param text: str: The content of the comment.
        """
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = None
        self.like_count = 0

    def edit_comment(self, new_text: str):
        """
        Edits the content of the comment and updates the update timestamp.

        :param new_text: str: The new content of the comment.
        """
        if new_text != self.text:
            self.text = new_text
            self.update_data = datetime.now()

    def like(self):
        """
        Increases the like count of the comment by 1.
        """
        self.like_count += 1

    def dislike(self):
        """
        Decreases the like count of the comment by 1.
        """
        self.like_count -= 1

    def __repr__(self) -> str:
        """
        Returns a string representation of the Comment instance.

        :return: A string representing the comment's author, content, creation and updated(if was edited) date,
         and like count.
        """
        return (f"Comment(author_id={self.author_id}, "
                f"text='{self.text}', "
                f"likes={self.like_count}, "
                f"created={self.create_data}, "
                f"updated={self.update_data if self.update_data is not None else 'was not edited'})")
