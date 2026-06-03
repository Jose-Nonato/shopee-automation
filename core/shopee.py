import requests
import time
import json
import hashlib
from dotenv import dotenv_values
config = dotenv_values(".env")


def gerar_auth(payload_str):
    timestamp = str(int(time.time()))

    assinatura = hashlib.sha256(
        f"{config["APP_ID"]}{timestamp}{payload_str}{config["SECRET"]}".encode("utf-8")
    ).hexdigest()

    return (
        f"SHA256 "
        f"Credential={config["APP_ID"]}, "
        f"Timestamp={timestamp}, "
        f"Signature={assinatura}"
    )


def get_products():
    query = """
    {
    productOfferV2(
        keyword: "celular",
        listType: 1,
        sortType: 5,
        page: 1,
        limit: 20
    ) {
        nodes {
        itemId
        productName
        productLink
        offerLink
        imageUrl
        priceMin
        priceMax
        priceDiscountRate
        sales
        ratingStar
        commissionRate
        sellerCommissionRate
        shopeeCommissionRate
        commission
        shopId
        shopName
        shopType
        periodStartTime
        periodEndTime
        }
        pageInfo { page limit hasNextPage }
    }
    }
    """

    body = json.dumps({"query": query}, separators=(",", ":"))
    resp = requests.post(
        config["URL"],
        headers={"Content-Type": "application/json", "Authorization": gerar_auth(body)},
        data=body
    )
    response = resp.json()
    return response["data"]["productOfferV2"]
