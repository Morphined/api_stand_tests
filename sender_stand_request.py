import configuration
import requests
import data


def post_products_kits(product_ids):
    return requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=product_ids,
        headers=data.headers
    )


response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )