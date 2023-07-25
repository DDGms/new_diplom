import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


track = post_new_order(data.order_body).json()
new_track = track['track']


def test_get_order_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(new_track))
response = test_get_order_track()
assert response.status_code == 200