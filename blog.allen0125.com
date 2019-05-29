# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream django {
    server unix:///var/www/blog/blog.sock;
    # server 127.0.0.1:8000;
}
# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name blog.allen0125.com;
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /var/www/blog/media;
    }

    location /static {
        alias /var/www/blog/static;
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /var/www/blog/uwsgi_params;
    }
}。
