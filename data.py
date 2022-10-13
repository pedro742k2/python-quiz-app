import requests

__req_params = {
    "amount": 10,
    "type": "boolean"
}
__req = requests.get("https://opentdb.com/api.php", params=__req_params)
__req.raise_for_status()
__data = __req.json()
questions_data = __data["results"]
