def extract_prices(products):
    res = [product.get_price() for product in products]

    return res
