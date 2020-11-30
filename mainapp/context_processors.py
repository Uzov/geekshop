def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.select_related()

    return {
        "basket": basket,
    }