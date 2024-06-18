if test -f .configured; then
  docker compose up --build;
else
  bash configure.sh
  touch .configured
  docker compose up --build
fi

read -n 1