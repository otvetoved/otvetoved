FROM nginx:mainline

RUN rm /etc/nginx/conf.d/default.conf

RUN if test -f nginx.conf; then export CONF_FNAME=nginx.conf; else export CONF_FNAME=nginx.conf.sample; fi
COPY ${CONF_FNAME} /etc/nginx/conf.d
