def get_ordered_comments_by_likes(comments):
    res = comments.copy()
    res.sort(key=lambda x: x.like_count, reverse=True)

    return res
