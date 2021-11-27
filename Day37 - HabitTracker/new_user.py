import requests

pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token":"1057TrsN2DWV6rLGfrZq8yPKZu",
    "username":"wolfbrand",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url=pixela_endpoint, json=params)
print(response.text)