from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name" : "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"stores":stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    pass


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")


