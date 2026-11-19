from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import telebot


@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({'data': data})


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

    def perform_create(self, serializer):
        data = serializer.save()
        temperature = data.temp

        if temperature is not None and temperature > 40:
            message = f"Alerte ! Temperature = {temperature} °C"

            try:
                send_mail(
                    subject="Alerte Temperature",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=["fares.ibrahim.dev@gmail.com"],
                    fail_silently=False,
                )
            except Exception as e:
                print("Gmail error:", e)

            try:
                bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
                bot.send_message(settings.TELEGRAM_CHAT_ID, message)
            except Exception as e:
                print("Telegram error:", e)
