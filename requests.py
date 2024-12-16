import requests

headers = {
    # Заголовок User-Agent указывает информацию о клиентском приложении, которое делает запрос.
    # В данном случае это имитация запроса из браузера Chrome на Windows 10.
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    
    # Заголовок Accept указывает, какие типы контента клиент готов принимать от сервера.
    # В данном случае мы ожидаем получить данные в формате JSON.
    'Accept': 'application/json',
    
    # Заголовок Cookie отправляет куки на сервер, которые были установлены ранее.
    # Включает идентификатор сессии (sessionid) и другой куки (othercookie), которые могут быть необходимы для аутентификации или сессий.
    'Cookie': 'sessionid=123456789; othercookie=value',

    # Заголовок Referer указывает URL-адрес страницы, с которой был инициирован текущий запрос.
    # Это может помочь серверу понимать, откуда пришел запрос, и делать соответствующие действия.
    'Referer': 'https://example.com',
}

url = "https://example.com/"

response = requests.get(url, headers, timeout=10) # Отправляем запрос на сайт (url - ссылка, headers - заголовки, timeout - если в течение какого то времени сервер не отвечает timeout просто заканчивает)
print(response.ok) # Работает ли сервер или нет

print(response.status_code) # Статус кода

# print(response.text) # Получить код сайта

print(response.url)  # URL-адрес, на который был отправлен запрос
print(response.headers)  # Заголовки, полученные в ответе
print(response.elapsed)  # Время, затраченное на выполнение запроса
print(response.url) # Получаем ссылку
# print(response.json) # Получить ответ в json формате
