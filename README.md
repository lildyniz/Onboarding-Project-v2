### Запуск проекта 

#### Клонированируйте, после чего создайте виртуальную среду и установите зависимости в корневой папке

```
git clone https://github.com/lildyniz/Onboarding-Project-v2.git
cd Onboarding-Project-v2
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```
___

#### Перейдите в src, проведите мигарции и создайте админа

```
cd src
python manage.py migrate
```
___

#### Запустите сервер
```
python manage.py runserver
```