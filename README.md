# Flask_Escape_from_Dungeons
Небольшой проект на flask. Направленный на закрепление навыков работы с flask-wtf.

Проект в игровой форме предполагает некую локацию с несколькими комнатами. Пользователь может перемещаться в разные стороны: на север, восток, юг или запад.
Для красоты и разнообразия в проект добавлен js/jquery, css и немного сюжета :)

## Запуск проекта
   - Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` Для Unix-систем вместо `pip` потребуется `pip3`.
   - вводим команду: `flask run`
   - альтернативный вариант для Unix-систем - установите gunicorn `pip3 install gunicorn` и введите команду `gunicorn --bind 127.0.0.1:5000 app:app`, в данном случае приложение будет доступно в локальной сети.
   - альтернативный вариант для Windows - установите waitress `pip install waitress` и введите команду `waitress-serve --listen=127.0.0.1:5000 app:app`
   
## Немного скриншотов:
![image](https://user-images.githubusercontent.com/84034483/190683017-0b098718-6012-479f-ad0b-03c8d3d2e066.png)

![image](https://user-images.githubusercontent.com/84034483/190683335-f19af655-3433-45fa-9656-e80051ef6a07.png)

