def select_products_by_category(products, category):
    res = [product for product in products if product.category == category]

    return res