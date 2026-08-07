import requests

url = "http://127.0.0.1:8000/predict/"
payload = {
    "model_name": "transformer_v2",
    "input_data": [0.1, 0.5, 0.9],
    # "threshold" is omitted; the server will use the 0.5 default
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())