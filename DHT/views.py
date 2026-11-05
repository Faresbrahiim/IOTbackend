from django.http import HttpResponse

def hello(request):
    return HttpResponse(
        "its our first test : fatima zahrae elmouissy & fares ibrahim"
    )