def filter_comments_by_author(comments, author):
    res = [comment for comment in comments if comment.author_id == author.id]

    return res
