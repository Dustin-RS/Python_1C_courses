def get_ordered_products_by_price(products):
    res = products.copy()
    res.sort(key=lambda x: x.price, reverse=True)

    return res
