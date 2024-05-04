### Запуск проекта 

#### После клонирования создайте виртуальную среду и установите зависимости в корневой папке

```
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```
___

#### Перейдите в src, проведите мигарции, загрузите фикстуры и записутите сервер

```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```