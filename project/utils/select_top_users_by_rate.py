def select_top_users_by_rate(users, top_size):
    res = users.copy()
    res.sort(key=lambda x: x.rate, reverse=True)

    return res[:top_size]