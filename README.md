# Ответовед

Сайт, на котором можно задать вопросы или дать ответы

Развёртывание в целях разработки

1. Установите docker engine (для windows проще установить docker desktop, в комплекте с которым установится и docker engine)
2. Откройте run_project.bat (Windows) или run_project.sh (Unix)

После развёртывания, вы сможете получить доступ к компонентам приложения по следующим адресам

* Frontend (over nginx): http://127.0.0.1:8010
* Backend (over nginx): http://127.0.0.1:8010/api
* Backend (direct): http://127.0.0.1:8008
* Postgres: 127.0.0.1:5432

Все хосты и порты вы можете изменить через файл .env в корне проекта.

Чтобы перезагружать компонент или просматривать его логи, нужно знать
1. Соответсвующую команду в docker
2. Название компонента

### Названия компонентов (`service_name`)
1. frontend
2. backend

### Docker compose команды
1. Перезагрузить сервис -- `docker cowmpose restart service_name`
2. Просмотреть логи сервиса -- `docker compose logs service_name`
3. Посмотреть логи сервиса за последние 5 минут и продолжить получать новые логи -- `docker compose logs service_name --since=5m -f`
