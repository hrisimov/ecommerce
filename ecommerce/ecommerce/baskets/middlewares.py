from ecommerce.baskets.basket import Basket


def set_basket_middleware(get_response):
    def middleware(request, *args, **kwargs):
        request.basket = Basket(request)
        return get_response(request, *args, **kwargs)

    return middleware
