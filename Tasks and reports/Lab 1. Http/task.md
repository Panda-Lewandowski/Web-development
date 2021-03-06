# Лабораторная работа № 1
## Изучение протокола HTTP
### Задание
Данная работа является вводной в курсе и призвана ознакомить студента с базовым протоколом web – протоколом HTTP.

> Решение оформляется в виде репозитория. По “опытной” части необходимо сделать отчет в markdown разметке (report.md файл в репозитории).

<ol>
<li> Базовая часть работы 
  <ol>
  <li> Цель данной работы – ознакомится с применением протокола HTTP на практике, в реальных системах. Каждый из рассмотренных типов запросов предлагается отправить на несколько известных интернет-сервисов. Впрочем, сервисы указаны лишь как примеры и при желании вы можете выбрать другие (социальные сети, почта, облака, новостные сайты и т.д.).  </li>
  <li> С помощью специального ПО (Postman, либо многочисленные аналоги, например, Restlet Clent - расширение для Chrome) вручную отправить следующие запросы и ответить на предлагаемые вопросы. <ol>
      <li> Запрос OPTIONS. Отправьте запрос на http://mail.ru, http://ya.ru, www.rambler.ru, https://www.google.ru, https://github.com/,   www.apple.com/.
      Для чего используется запрос OPTIONS? Какие коды ответов приходят при этом запросе? Какие сайты правильно обработали запрос и вернули ожидаемые данные? </li>
     <li>   Запрос HEAD.  vk.com, www.apple.com, www.msn.com.
      Для чего нужен запрос HEAD? Какой сайт прислал ожидаемый ответ?
      1.2.3.   Запросы GET и POST. Отправьте по запросу на yandex.ru, google.com и apple.com. Что они вернули? Что содержится в теле ответа? </li></li></ol>
  <li>          Работа с api сайта. Многие крупные сервисы предоставляют открытое api. Как правило, оно реализовано на подходе REST, но это необязательно. Такое api используется сторонними сервисами и приложениями, которые хотят воспользоваться услугами предоставляющего такое api сервиса. Рассмотрим такое api на примере сайта vk.com (при желании можно выбрать другой подходящий сервис). </li>
 <ol>
  <li>   Зайдите на https://vk.com/dev/api_requests и посмотрите структуру запросов к данному api. </li>
  <li>   Используя документацию (https://vk.com/dev/methods) выполните следующие задания (обратите внимание, запросы нужно отправлять не из предложенной на сайте формы, а как в предыдущем задании):
  <ol>
      <li>       Получите список всех факультетов МГТУ им. Н.Э.Баумана. </li>
      <li>        Получите свою аватарку. </li>
      <li> Ответьте на вопросы: какой код ответа присылается от api? Что содержит тело ответа? В каком формате и какой кодировке содержаться данные? Какой веб-сервер отвечает на запросы? Какая версия протокола HTTP используется? </li></ol></li>
  <li>  POST запросы проще отправлять с формы, встроенной в документацию api. Чтобы посмотреть, как выглядит запрос, можно воспользоваться панелью разработчика браузера (F12 в Chrome -> вкладка Hetwork). <ol>
    <li> Отправьте запись на стену любому пользователю/группе и убедитесь, что она пришла. </li> 
    <li>       Ответьте на вопрос: каким образом передаются данные от пользователя к серверу в POST-запросах? </li></ol></li>
  </ol></ol></li>

<li> Реализуйте небольшое серверное приложение, с использованием любого фреймворка. Лучшего всего для этой цели подойдет NodeJS: решение получится очень компактным и простым.
  Сервер должен содержать предоставлять API с поддержкой (GET, POST, DELETE, PUT, OPTION). Данные отправлять в формате json. Конкретное содержание запросов - на ваше усмотрение. Подключите фантазию. (Можно сделать простейший CRUD-сервис с хранением данных в RAM). </li>

<li> Доп. задание. Статика и маршрутизация.
<ol>
<li>   Добавьте папку static (классическое название для статически раздаваемой папки). </li>
<li>   В папке static создайте папки html и img. </li>
<li>   В папке static/html создайте файл index.html со следующим содержанием (или любым другим): 

```html
<head></head>
<body>
<h1>Hello, world!</h1>
<img src=”/img/image.jpg”>
</body>
```
 </li>
<li>   Настройте сервер так, чтобы при запросе из браузера отображалась эта страница. </li>
      <li>          Настройте routing (маршрутизацию) на вашем сервере. Например, чтобы путь /hack тоже отдавал файл index.html, а путь /, по умолчанию отдающий index, выдавал дополнительную страницу hack.html. </li>
<li>         Переименуйте hack.html (содержащую теги html) в hack.txt. Что изменилось? Почему? Как сделать так, чтобы страница отображалась корректно?  </li>
</li>
</li>
</ol>
