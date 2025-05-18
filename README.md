# Тестовое задание  
Общие требования:
- Для решения использовать python версии 3.9 или выше
- Для задания 2 можно использовать библиотеки, задачи 1 и 3 реализовать, используя встроенные средства языка
- Ссылку на репозиторий с готовым тестовым заданием вместе с ссылкой резюме отправлять на: https://t.me/arheugene
- Решение каждой задачи должно быть в папке с ее условием, в файле `solution.py` или в модуле solution 
- К каждой задаче необходимо написать тесты  
# Удачи!

[Задача 1](task1/task1.md)   
[Задача 2](task2/task2.md)  
[Задача 3](task3/task3.md)


## Настройка окружения
Склонировать репозиторий и перейти в него:
```
git clone https://github.com/AndreiAgeev/tetrika_junior.git
```
```
cd tetrika_junior/
```
Создать и активировать вирутальное окружение:<br />
*Для Linux:*
```
python3 -m venv .venv
```
```
source env/bin/activate
```
*Для Windows:*
```
python -m venv .venv
```
```
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:<br />
*Для Linux:*
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
*Для Windows:*
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
## Запуск скриптов решений задач
Для task1 и task3 достаточно перейти в их каталоги и запустить скрипт `solution.py`:
```
python solution.py
```
Для task2 необходимо перейти в каталог *solution* и запустить Scrapy:
```
cd task2/solution/
```
```
scrapy crawl wiki_animals
```
Результаты парсинга будут сформированы в файле `beasts.csv` в каталоге *results* внутри каталога *solution*.

## Запуск тестов
Для запуска тестов необходимо запустить pytest в каталоге *tetrika_junior*:
```
cd tetrika_junior/
```
```
pytest
```
