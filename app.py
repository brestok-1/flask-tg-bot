from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

key = "6152338360:AAGUDMK81XzNjIQJp9-7sRzWcZZzmrtSgfs"


def get_date():
    target_date = datetime.datetime(2024, 7, 18)
    today = datetime.datetime.today()
    delta = target_date - today
    total_seconds = delta.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return list(map(int, (days, hours, minutes, seconds)))


def send_message(chat_id, text):
    method = 'sendMessage'
    token = '6152338360:AAGUDMK81XzNjIQJp9-7sRzWcZZzmrtSgfs'
    url = f'https://api.telegram.org/bot{token}/{method}'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data)


@app.route('/', methods=['GET', 'POST'])
def recieve_update():  # put application's code here
    if request.method == 'POST':
        chat_id = request.json['message']['chat']['id']
        if request.json['message']['text'] == '!Денис' or request.json['message']['text'] == '!денис':
            send_message(chat_id,
                         f'Внимание!!! До совершеннолетия Дениса осталось {get_date()[0]} дней, {get_date()[1]} часов, {get_date()[2]} минут, {get_date()[3]} секунд!')
        if request.json['message']['text'] == '@all':
            send_message(chat_id,
                         f'@cquyame @sttpdflwr @wolffysc2 @Er4rr0r4 @gschxck4 @mmakkssikk @ddanisimmo @lillchicha @itzvelen @LocD0G @Pacultek @wertByte')
    return {'ok': True}


if __name__ == '__main__':
    app.run()
