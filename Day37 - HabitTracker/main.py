import requests, re, time
USERNAME = "wolfbrand"
TOKEN = "1057TrsN2DWV6rLGfrZq8yPKZu"

pixela_endpoint = "https://pixe.la"

headers = {
    "X-USER-TOKEN":TOKEN
}

def create_graph(name:str, unit:str, type:str, color:str):
    """
    Create a new pixela graph with the given parameters
    """
    # Format name to fit id parameters
    id = str.replace(name, " ", "-").lower()
    id = re.sub("[^a-z0-9-]+", "", id)
    # Gather params
    graph_config = {
        "id":id,
        "name":name,
        "unit":unit,
        "type":type,
        "color":color
    }
    # Get the endpoint and make a request
    graphs_endpoint = f"{pixela_endpoint}/v1/users/{USERNAME}/graphs"
    response = requests.post(url=graphs_endpoint, headers=headers, json=graph_config)
    response_msg = parse_response(response.text)
    if response_msg["isSuccess"] == True:
        print(f"Successfully created graph {name} with id: {id}")
    else:
        print(response.text)

def post_pixel(graph_id:str, quantity:str):
    "Place a pixel at todays date on the pixela graph with id: graph_id"
    today = time.strftime('%Y%m%d')
    pixel_config = {
        "date": today,
        "quantity":quantity
    }    
    pixel_endpoint = f"{pixela_endpoint}/v1/users/{USERNAME}/graphs/{graph_id}"
    response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
    response_msg = parse_response(response.text)
    if response_msg["isSuccess"] == True:
        print(f"Successfully posted pixel to graph id: {graph_id}")
    
def parse_response(response_text):
    """
    Parses the json reponse text from pixela
    """
    true = True
    false = False
    message = eval(response_text)
    return message

post_pixel("walking-graph", "30")