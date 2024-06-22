cd ./backend
copy /-Y ".env.sample" ".env"
cd ../nginx
copy /-Y /N ".env.sample" ".env"
copy /-Y /N "nginx.conf.sample" "nginx.conf"
cd ../postgres
copy /-Y ".env.sample" ".env"
cd ../frontend
copy /-Y ".env.sample" ".env"
cd ../
copy /-Y ".env.sample" ".env"
copy /-Y ".env.prod.sample" ".env.prod"