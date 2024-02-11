from flask import Flask, request
from flask_pydantic import validate

from task2.dtos import ProductListingTransactionsRequest, UnauthorizedSalesResponse
from task2.logic import find_unauthorized_sales
from task3.dtos import InterviewsRequest, MaxInterviewResponse
from task3.logic import calculate_max_intervals


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return (
        "<div align='center'>"
        "<p>Task 2: <code>POST /task2</code></p>"
        "<p>Task 3: <code>POST /task3</code></p>"
        "</div>"
    )


@app.route("/task2", methods=["POST"])
@validate()
def task2(body: ProductListingTransactionsRequest):
    unauthorized_sellers_per_product = find_unauthorized_sales(
        body.productListings,
        body.salesTransactions,
    )
    res = {
        "unauthorizedSales": [
            {
                "productID": product_id,
                "unauthorizedSellerID": unathorized_seller_id_list,
            }
            for product_id, unathorized_seller_id_list in unauthorized_sellers_per_product.items()
        ]
    }

    return UnauthorizedSalesResponse(**res)


@app.route("/task3", methods=["POST"])
@validate()
def task3(body: InterviewsRequest):
    START_TIME, END_TIME = 0, 1
    # Notice intervals are sorted in ascending order by their end times
    interview_intervals = sorted(
        zip(body.start_times, body.end_times),
        key=lambda interval: (interval[END_TIME], interval[START_TIME]),
    )

    max_intervals = calculate_max_intervals(interview_intervals)

    return MaxInterviewResponse(max_interviews=max_intervals)
