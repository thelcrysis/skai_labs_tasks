from collections import defaultdict
import typing as tp


def find_unauthorized_sales(
    product_listings: list[dict[str, str]],
    sales_transactions: list[dict[str, str]],
) -> dict[str, list[str]]:
    """
    Returns dictionary with productID as a key and list of unauthorized sellers as a value.
    """
    # It is assumed that list of sales transactions is larger than product listings
    # In that case, reorganizing authorized sellers as a dictionary keyed by product_id would
    # lower time complexity for checking if seller is an authorized seller from O(n) to O(1)
    authorized_sellers_per_product: tp.DefaultDict[str, set] = defaultdict(set)
    for product_listing in product_listings:
        product_id = product_listing["productID"]
        authorized_seller_id = product_listing["authorizedSellerID"]
        authorized_sellers_per_product[product_id].add(authorized_seller_id)

    unauthorized_sellers_per_product: tp.DefaultDict[str, list] = defaultdict(list)

    # Iterate through sale transactions and use `authorized_sellers_per_product` to check
    # if the seller is authorized
    for sale_transaction in sales_transactions:
        product_id = sale_transaction["productID"]
        seller_id = sale_transaction["sellerID"]
        if seller_id not in authorized_sellers_per_product[product_id]:
            unauthorized_sellers_per_product[product_id].append(seller_id)

    return dict(unauthorized_sellers_per_product)
