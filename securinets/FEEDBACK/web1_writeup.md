## Web 1 FEEDBACK
[Ссылка на веб сайт](https://web2.ctfsecurinets.com/)

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/website.png)

Включаем бурп и кидаем в active scan
Он нашел xxe уязвимость , начинаем ковыряться с ней

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/web1.png)

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/web1_2screen.png)

Гуглим про nginx,а именно NGinx Default public www location
находим вот такой путь пробуем вставить 
**/etc/nginx/sites-enabled/default**

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/web1_3.png)

Вот Response:

```
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Sun, 24 Mar 2019 11:44:58 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 2470
```

Request:

```
Thanks For you Feedback sadas
 You should look at the following URL's in order to grasp a solid understanding
 of Nginx configuration files in order to fully unleash the power of Nginx.
 https://www.nginx.com/resources/wiki/start/
 https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
 https://wiki.debian.org/Nginx/DirectoryStructure
 In most cases, administrators will remove this file from sites-enabled/ and
 leave it as reference inside of sites-available where it will continue to be
 updated by the nginx packaging team.
 This file will automatically load configuration files provided by other
 applications, such as Drupal or Wordpress. These applications will be made
 available underneath a path with that package name, such as /drupal8.

 Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
 Default server configuration

server {
	listen 80 default_server;
	listen [::]:80 default_server;
 SSL configuration
 listen 443 ssl default_server;
 listen [::]:443 ssl default_server;
 Note: You should disable gzip for SSL traffic.
 See: https://bugs.debian.org/773332
 Read up on ssl_ciphers to ensure a secure configuration.
 See: https://bugs.debian.org/765782
 Self signed certs generated by the ssl-cert package
 Don't use them in a production server!
 include snippets/snakeoil.conf;
	root /var/www/html/epreuve;
 Add index.php to the list if you are using PHP
	index index.php index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
 First attempt to serve request as file, then
 as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}
 pass PHP scripts to FastCGI server

	location ~ \.php$ {
		include snippets/fastcgi-php.conf;

 With php-fpm (or other unix sockets):
		fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
 With php-cgi (or other tcp sockets):
		fastcgi_pass 127.0.0.1:9000;
	}

 deny access to .htaccess files, if Apache's document root
 concurs with nginx's one

location ~ /\.ht {
	deny all;
}
}

 Virtual Host configuration for example.com

 You can move that to a different file under sites-available/ and symlink that
 to sites-enabled/ to enable it.

server {
	listen 80;
	listen [::]:80;
	server_name example.com;

	root /var/www/example.com;
	index index.html;

	location / {
		try_files $uri $uri/ =404;
	}
}

```

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/web3_2.png)

Видим строку :root /var/www/html/epreuve 
Пытаемся вставить в ее с добавлением /flag 
Забираем наш флаг и 731point :
**Securinets{Xxe_xXE_@Ll_Th3_W@Y}**

![](https://github.com/Boringdreams/writeup/blob/master/securinets/FEEDBACK/png/web1_finish.png)


