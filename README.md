# stepik-auto-tests-course
Задания по курсу https://stepik.org/course/575

## Memo настройки окружения курса

На window все работает в WinPython

mkdir environments
cd environments

Создадим виртуальное окружение:

python -m venv selenium_env

Запустим созданный для нас приложением venv файл activate.bat, чтобы активировать окружение:

selenium_env\Scripts\activate.bat

Выйти из нашего окружения: deactivate


Установка selenium для Windows, для тех у кого не работает pip install selenium.

Открываем в браузере страницу библиотеки: https://pypi.org/project/selenium/#files

и скачиваем файл selenium-3.141.0.tar.gz (тип Source).

Сохраняем файл в рабочую папку environments и потом распаковываем архив в папку: selenium-3.141.0

Далее в командной строке заходим в рабочую папку и активируем окружение (как описано было раньше в уроках).

Переходим в папку selenium-3.141.0

cd selenium-3.141.0

Запускаем ручную установку:

..\environments\selenium-3.141.0\python setup.py install

Библиотека установится.

Проверяем, что библиотека действительно установилась: pip list

Мне также еще потребовалась установка библиотеки urllib3, нужна версия urllib3-1.25.3.

Страница библиотеки: https://pypi.org/project/urllib3/#files

Устанавливается аналогично selenium: распаковать, активировать окружение, перейти в папку с архивом, выполнить python setup.py install.

## Установка драйверов браузеров
You can download ChromeDriver here: https://sites.google.com/a/chromium.org/chromedriver/downloads

Then you have multiple options:

add it to your system path |
put it in the same directory as your python script |
specify the location directly via executable_path

driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

## Фиксация пакетов окружения
pip freeze > requirements.txt
применение в новом виртуальном окружении:
pip install -r requirements.txt
