import random

def get_signature_fan():
    destinations = [    "abu-dhabi",
                        "bangkok",
                        "barcelona",
                        "wangfujing",
                        "bodrum",
                        "boston",
                        "canouan",
                        "doha",
                        "dubai",
                        "geneva",
                        "guangzhou",
                        "hong-kong",
                        "landmark",
                        "istanbul",
                        "jakarta",
                        "kuala-lumpur",
                        "lake-como",
                        "london",
                        "macau",
                        "madrid",
                        "marrakech",
                        "miami",
                        "milan",
                        "munich",
                        "new-york",
                        "paris",
                        "prague",
                        "riyadh",
                        "santiago",
                        "sanya",
                        "shanghai",
                        "shenzhen",
                        "singapore",
                        "taipei",
                        "tokyo",
                        "washington"
                                        ]

    destination = random.choice(destinations)

    if destination == 'abu-dhabi':
        signature_fan = "https://byconnoisseur.com/wp-content/uploads/2019/05/Emirates-Palace-Hotel.jpg"
        return signature_fan, destination
    elif destination == 'riyadh':
        signature_fan = "https://a.mktgcdn.com/p/wTR1Ao1HyvL2YOOkx874IAekgPcshGB4oarQLJAvdlM/2066x2066.jpg"
        return signature_fan, destination
    elif destination == 'prague':
        signature_fan = "https://photos.mandarinoriental.com/is/image/MandarinOriental/prauge-hotel-signature-fan?"
        return signature_fan, destination
    else:
        signature_fan = "https://photos.mandarinoriental.com/is/image/MandarinOriental/" + destination + "-hotel-signature-fan?"
        return signature_fan, destination
