# SKAI LABS

## How to run
`git clone` this repo.

#### Prerequisites
Provided code should work with variety of different versions and operating systems, but was tested on:
npm 9.8.0
Node v20.5.1
Python 3.10.12
Ubuntu 22.04.3 LTS

## Task 1
- Position yourself at `skai_labs_tasks/1_task/first` (where `skai_labs_tasks` is root repository).
- Run `npm install`.
- Run `npm start`.

Web app should now be running on `http://localhost:5173/` _(this may differ if the port is already occupied.)_

## Tasks 2 & 3
- Position yourself at `skai_labs_tasks/2_n_3_tasks`.
- (Install `venv` if it is not present on the system : `pip install virtualenv`)
- Create a new virutal environment: `python3 -m venv .env` (`virtualenv .env` on Windows)
- Activate the created environment: `source .env/bin/activate` (`.\venv\Scripts\activate` on Windows)
- Install all requirements: `pip install -r requirements.txt`.
- Run `flask --app app run`, development server should be running on `http://127.0.0.1:5000`.

#### Task 2 
Task 2 is implemented as endpoint `POST /task2`

Requests:
```JSON
{
    "productListings": [
        {
            "productID": "123",
            "authorizedSellerID": "A1"
        }
    ],
    "salesTransactions": [
        {
            "productID": "123",
            "sellerID": "B2"
        }
    ]
}
```
results in
```JSON
{
    "unauthorizedSales": [
        {
            "productID": "123",
            "unauthorizedSellerID": [
                "B2"
            ]
        }
    ]
}
```

#### Task 3
Task 3 is implemented as endpoint `POST /task3`

Requests:
```JSON
{
    "start_times": [
        10,
        20,
        30,
        40,
        50,
        60
    ],
    "end_times": [
        15,
        25,
        35,
        45,
        55,
        65
    ]
}
```
results in
```JSON
{
    "max_interviews": 6
}
```

