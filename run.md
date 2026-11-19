cd ~/Desktop/IOT
python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework

-------------------------------------

python manage.py runserver 0.0.0.0:8000

------------------------------------
in case if it doesn't worked 

sudo firewall-cmd --add-port=8000/tcp


check alert : 
curl -X POST http://localhost:8000/api/post \
  -H "Content-Type: application/json" \
  -d '{"temp": 30, "hum": 50}'

-------------------------------------
varibale d'env 

export TELEGRAM_TOKEN="9232277879:AAEUVaeanfYv9M9vKkYeQtjIAxXQmkVg3VY"
export TELEGRAM_CHAT_ID="8632378179"


---------------------------------------

export EMAIL_HOST_USER="hmsteven37@gmail.com"
export EMAIL_HOST_PASSWORD="cpvv kbcd mprt tpvq"
 