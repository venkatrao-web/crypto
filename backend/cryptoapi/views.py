import requests
from django.http import JsonResponse

def crypto_prices(request):
    """
    Fetch live crypto prices from CoinGecko API.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin,ethereum,dogecoin",
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        data = response.json()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


