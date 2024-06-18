if exist .configured (
docker compose up --build ) else (
configure.bat
echo . > .configured
docker compose up --build )

pause