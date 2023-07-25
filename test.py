import configuration
import requests
import data

# Максим Кузнецов 6-я кагорта - Финальный проект. Инженер по тестированию плюс
def test_get_order_track():
    def post_new_order(body):
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                             json=body)
    track = post_new_order(data.order_body).json()
    new_track = track['track']

    def get_order_track():
        return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(new_track))

    response = get_order_track()
    assert response.status_code == 200