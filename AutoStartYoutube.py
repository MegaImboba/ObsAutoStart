from obswebsocket import obsws, requests
from datetime import datetime

dir(obsws)
OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = "Mine2012craft"

def get_stream_title():
    today = datetime.now()
    weekday = today.strftime("%A")
    date = today.strftime('%d.%m.%Y')

    if weekday == 'Wednesday' or weekday == 'Friday':
        return f"Вечернее служение {date}"
    elif weekday == 'Sunday':
        return f"Воскресное служение {date}"
    else:
        return f"Трансляция {date}"
        
def start_streaming():
    stream_title = get_stream_title()
    ws = obsws(OBS_HOST, OBS_PORT, OBS_PASSWORD)
    try:
        ws.connect()
        print(ws.call(requests.StartStreaming()))
        print(f"Трансляция '{stream_title}' началась!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        ws.disconnect()

if __name__ == "__main__":
    start_streaming()