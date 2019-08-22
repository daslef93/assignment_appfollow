## SQL | 6 *
#### Напишите SQL-запросы из пункта (c.) на соответствующей картинке. внизу  приложите текст запросов или ссылку на файл с запросами

**1. Создание таблиц
**
> create table accounts (
	id INT AUTO_INCREMENT PRIMARY KEY,
	created DATE NOT NULL,
	trial_started DATE,
	trial_ended DATE,
	paid_started DATE,
	paid_cancelled DATE
);

------------


> create table orders (
	id INT AUTO_INCREMENT PRIMARY KEY,
	account_id INT NOT NULL,
	amount INT NOT NULL,
	currency VARCHAR(4) NOT NULL,
	month INT,
	created DATE
);

------------


Для собственного удобства заполнил таблицы случайными данными (использовал mockaroo.com)

**appfollow.accounts table**

![](https://github.com/daslef93/assignment_appfollow/blob/master/img/accounts_query.PNG?raw=true "1")

------------


**appfollow.orders table**

![](https://github.com/daslef93/assignment_appfollow/blob/master/img/orders_query.PNG?raw=true "2")

**2. Генерация отчета
**

> select
	concat(year(curdate()), '/', monthname(curdate())) as YM,
	count(created) as SIGN_UPS, 
    count(trial_started) as TRIAL,
	count(paid_started) as PREMIUM, 
    count(paid_cancelled) as PREMIUM_CHURN
from  appfollow.accounts 
where month(created) = month(curdate()) and year(created) = year(curdate()); where month(created) = month(curdate()) and year(created) = year(curdate()); 

------------

![](https://github.com/daslef93/assignment_appfollow/blob/master/img/monthly_report.PNG?raw=true "2")

------------

**3.  Расчет MRR и Revenue**

> select 
	concat(year(curdate()), '/', monthname(curdate())) as YM,
    avg(amount/month)*count(account_id) as MRR,
    sum(amount) as Revenue
from 
	appfollow.orders 
where 
	month(created) = month(curdate()) and 
	year(created) = year(curdate()) and
    month is not null;

![](https://github.com/daslef93/assignment_appfollow/blob/master/img/monthly_report_mrr.PNG?raw=true "2")		
	


### Комментарии:

- мне понравилась задача;
- с SQL работал только на примитивном уровне, для обеспечения простенького бэкенда, думаю это заметно);
- наибольшие трудности возникли при реализации третьего пункта, где я взял за основу  формулу **MRR = количество__клиентов х средний доход с клиента**, причем если клиент платил более чем за месяц, то я делил общую его сумму на количество месяцев. И всё равно ощущение, что всё гораздо сложнее и я ошибаюсь;
- если MRR - это месячная выручка, то Revenue, методом исключения, - общая, поэтому я просто сложил все доходы. Да, сейчас осознал, что не реализовал приведение к единой валюте, то есть необходимо либо создать таблицу с отношениями между валютами и забирать оттуда коэффициенты, либо реализовать через условную конструкцию (некрасиво, но для трех валют может быть и приемлемо);
