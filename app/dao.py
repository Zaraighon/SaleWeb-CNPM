def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Laptop"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "iPhone 12",
        "price": 2334,
        "image": "https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-12-xanh-duong-new-600x600-200x200-1.jpg"
    }, {
        "id": 2,
        "name": "iPhone 13",
        "price": 2554,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2021/09/15/image-removebg-preview-12.png"
    }, {
        "id": 3,
        "name": "iPhone 15",
        "price": 2834,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    }, {
        "id": 4,
        "name": "iPhone 12",
        "price": 2334,
        "image": "https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-12-xanh-duong-new-600x600-200x200-1.jpg"
    }, {
        "id": 5,
        "name": "Pixel 5",
        "price": 1334,
        "image": "https://cdn.viettablet.com/images/thumbnails/480/516/detailed/46/google-pixel-5.jpg"
    }, {
        "id": 6,
        "name": "Samsung S20 Ultra",
        "price": 2634,
        "image": "https://cdn.idealo.com/folder/Product/7008/1/7008133/s3_produktbild_gross/samsung-galaxy-s20-ultra-5g.jpg"
    }, ]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products
