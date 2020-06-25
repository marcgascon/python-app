FROM nginx:stable-alpine
RUN  rm /etc/nginx/conf.d/default.conf
COPY web-proxy/web-app.conf /etc/nginx/conf.d/web-app.conf
