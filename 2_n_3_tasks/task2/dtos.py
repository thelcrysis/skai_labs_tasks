from pydantic import BaseModel


class ProductListingTransactionsRequest(BaseModel):
    productListings: list[dict[str, str]]
    salesTransactions: list[dict[str, str]]


class ProductUnauthorizedSale(BaseModel):
    productID: str
    unauthorizedSellerID: list[str]


class UnauthorizedSalesResponse(BaseModel):
    unauthorizedSales: list[ProductUnauthorizedSale]
