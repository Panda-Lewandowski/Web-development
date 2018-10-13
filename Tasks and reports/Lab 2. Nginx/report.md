## Начальные метрики 

Cкорость отдачи контента на сервере из лабораторной работы №1:

|Контент|Время отдачи |
|---|---|
|Cтраница| 5.647 ms |
|Картинка| 6.228 ms |
|API (GET)| 5.711 ms |
|API (POST)| 2.771 ms |
|API (PUT)| 3.268 ms|
|API (HEAD)| 0.772 ms |
```bash
$ ab -c 10 -n 100 http://127.0.0.1:8000/
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        3626 bytes

Concurrency Level:      10
Time taken for tests:   0.602 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      397900 bytes
HTML transferred:       362600 bytes
Requests per second:    166.22 [#/sec] (mean)
Time per request:       60.160 [ms] (mean)
Time per request:       6.016 [ms] (mean, across all concurrent requests)
Transfer rate:          645.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:    11   58  16.7     55     128
Waiting:       10   51  15.8     48     120
Total:         11   58  16.7     55     128

Percentage of the requests served within a certain time (ms)
  50%     55
  66%     63
  75%     67
  80%     71
  90%     77
  95%     85
  98%    118
  99%    128
 100%    128 (longest request)
```

```bash
$ ab -c 10 -n 100 http://127.0.0.1:8000/static/images/bg.jpg
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /static/images/bg.jpg
Document Length:        1000850 bytes

Concurrency Level:      10
Time taken for tests:   0.622 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      100104100 bytes
HTML transferred:       100085000 bytes
Requests per second:    160.87 [#/sec] (mean)
Time per request:       62.161 [ms] (mean)
Time per request:       6.216 [ms] (mean, across all concurrent requests)
Transfer rate:          157265.41 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:    41   61   5.9     60      83
Waiting:        3    7   3.0      7      24
Total:         41   61   5.9     60      83

Percentage of the requests served within a certain time (ms)
  50%     60
  66%     61
  75%     62
  80%     64
  90%     69
  95%     73
  98%     82
  99%     83
 100%     83 (longest request)

```
## Отдача статического контента

После настройки отдачи статического контента с сервера nginx:

|Контент|Время отдачи |
|---|---|
|Cтраница| 5.821 ms |
|Картинка| 0.746 ms |
|API (GET)| 5.552 ms |
|API (POST)| 2.595 ms |
|API (PUT)| 2.226 ms|
|API (HEAD)| 6.009 ms |

## Кэширование и сжатие 

После настройки nginx как прокси-сервера и включения кеширования и сжатия скорость отдачи контента стала такой:

|Контент|Время отдачи |
|---|---|
|Cтраница| 2.444 ms |
|Картинка| 0.734 ms |
|API (GET)| 0.366 ms |
|API (POST)| 2.984 ms |
|API (PUT)| 3.588 ms|
|API (HEAD)| 0.535 ms |

