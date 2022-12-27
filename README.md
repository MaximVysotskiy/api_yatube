# api_yatube
api_yatube
# api_final_yatube
это проект DRF, который состоит из постов и приложений api.
Приложение Posts включает в себя модели для БД;
Приложение Api включает в себя urlpatterns, views (ModelViewSet), сериализаторы.
Основная идея api_final_yatube заключается в том, чтобы:
* предоставить возможность пройти аутентификацию с помощью JWTAuthentication;
* для получения, создания, обновления и удаления сообщений с разрешением IsAuthenticatedOrReadOnly (получение списка сообщений с разбивкой по страницам с помощью LimitOffsetPagination);
* для получения, создания, обновления и удаления комментария/комментариев к публикации с разрешением IsAuthenticatedOrReadOnly;
* чтобы получить группу/groups с разрешением IsAuthenticatedOrReadOnly;
* чтобы подписаться на пользователя, получите список подписчиков и выполните поиск по следующему имени с разрешением IsAuthenticated.

# чтобы запустить проект:

клонируйте репозиторий:

```
git clone https://github.com/olhao/api_final_yatube.git

cd api_final_yatube
```

создайте и активируйте виртуальное окружение:

```
python -m venv env

source env/bin/activate

python -m pip install --upgrade pip
```

установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

выполните миграции:

```
python manage.py makemigrations

python manage.py migrate
```

запустите проект:

```
python manage.py runserver
```
