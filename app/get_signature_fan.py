import random

def get_signature_fan():
    destinations = ["abu-dhabi",
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
    signature_fan = "https://photos.mandarinoriental.com/is/image/MandarinOriental/" + destination + "-hotel-signature-fan?"
    return signature_fan
