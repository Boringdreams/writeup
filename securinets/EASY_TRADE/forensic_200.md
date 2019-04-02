## Forensics 1 EASY TRADE 
Был дан файл _forentrade.pcap_ открываем wireshark'ом

![](https://github.com/Boringdreams/writeup/blob/master/securinets/EASY_TRADE/png/forenc1.png)

видим диалог : give me the key ,securinetsXD , okey listen 0n 4444 f or the file
В wireshark используем фильтр tcp.port == 4444
Или tcp contains flag (если есть поля с 'flag)

![](https://github.com/Boringdreams/writeup/blob/master/securinets/EASY_TRADE/png/forenc2.png)
![](https://github.com/Boringdreams/writeup/blob/master/securinets/EASY_TRADE/png/forenc3.png)

правой кнопкой по data --> export packet bytes скачиваем файл как flag.file 
хм сразу показал,что это архив,но для проверки запускаем терминал 

![](https://github.com/Boringdreams/writeup/blob/master/securinets/EASY_TRADE/png/forenc4.png)

file flag.file -->flag.file: Zip archive data, at least v1.0 to extract
распаковываем видим что нам необходим пароль : securinetsXD
Теперь у нас есть flag.txt в котором находится : c2VjdXJpbmV0c3s5NTRmNjcwY2IyOTFlYzI3NmIxYTlmZjg0NTNlYTYwMX0
Вводим в терминале : 
echo 'c2VjdXJpbmV0c3s5NTRmNjcwY2IyOTFlYzI3NmIxYTlmZjg0NTNlYTYwMX0' | base64 --decode 
Получаем флаг
**securinets{954f670cb291ec276b1a9ff8453ea601}base64**
и свои 200 поинтов
