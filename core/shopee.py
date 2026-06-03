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


def get_products(keyword: str, page=1, limit=10):
    if not keyword:
        return []

    page = int(page or 1)
    limit = int(limit or 20)

    query = """
    query ProductOffer(
        $keyword: String!,
        $page: Int!,
        $limit: Int!
    ) {
        productOfferV2(
            keyword: $keyword,
            listType: 1,
            sortType: 5,
            page: $page,
            limit: $limit
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
                commission
                shopName
                shopType
                periodStartTime
                periodEndTime
            }
            pageInfo {
                page
                limit
                hasNextPage
            }
        }
    }
    """

    body = {
        "query": query,
        "variables": {
            "keyword": keyword,
            "page": page,
            "limit": limit
        }
    }

    body_json = json.dumps(body, separators=(",", ":"))
    resp = requests.post(
        config["URL"],
        headers={
            "Content-Type": "application/json",
            "Authorization": gerar_auth(body_json)
        },
        data=body_json
    )

    return resp.json()
