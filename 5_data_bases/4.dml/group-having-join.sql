--максимальное минимальное
SELECT max(rental_rate), min(rental_rate) FROM film;
--среднее
SELECT avg(length) FROM film;
--счетчик
SELECT count(*) FROM actor;
--сумма
SELECT sum(amount), avg(amount) FROM payment
WHERE staff_id = 1;

--вложенные запросы
--найдем все фильмы  продолжительностью выше среднего
--так работать не будет
--SELECT title, length FROM film
--WHERE length >= avg(length)
--нужно вот так
SELECT title, length FROM film
WHERE length >= (SELECT avg(length) FROM film);

--найдем название фильмов, стоимость которых не максимальна
SELECT title, rental_rate FROM film
WHERE rental_rate < (SELECT max(rental_rate) FROM film)
ORDER BY rental_rate DESC;

--группировки
--посчитаем количество актеров в разрезе фамилий (однофамильцы)
SELECT last_name, count(*) FROM actor
GROUP BY last_name
ORDER BY count(*) DESC;

--посчитаем количество фильмов в разрезе рейтингов(распределение рейтингов)
SELECT rating, count(title) FROM film
GROUP BY rating 
ORDER BY count(title) DESC;

--найдем максимальные продажи в разрезе продавцов 
SELECT staff_id, max(amount) FROM payment 
GROUP BY staff_id;

--найдем средние продажи каждого продавца каждому покупателю
SELECT staff_id, customer_id, avg(amount) FROM payment 
GROUP BY staff_id, customer_id 
ORDER BY avg(amount) DESC;

--найдем среднюю продолжительность фильма в разрезе рейтингов в 2006 году
SELECT rating, avg(length) FROM film
WHERE release_year = 2006
GROUP BY rating;

--Оператор HAVING
--отберем только фамилии актеров, которые не повторяются
SELECT last_name, count(*) FROM actor
GROUP BY last_name 
HAVING count(*) = 1;

--отберем и посчитаем только фамилии актеров, которые повторяются
SELECT last_name, count(*) FROM actor
GROUP BY last_name 
HAVING count(*) > 1
ORDER BY count(*) DESC;

--найдем фильмы, у которых есть Super в названии
-- и они сдавались в прокат суммарно более, чем на 5 дней
SELECT title, sum(rental_duration) FROM film
GROUP BY title 
HAVING sum(rental_duration) > 5 AND title LIKE '%Super%';

--ALIAS
--предыдущий запрос с псевдонинами
SELECT title AS t, sum(rental_duration) AS sum_t FROM film AS f
WHERE title LIKE '%Super%'
GROUP BY t
HAVING sum(rental_duration) > 5;

--JOIN
--Объединение таблиц
--выведем имена, фамилии и адреса сотрудников
SELECT first_name, last_name, address FROM staff s 
LEFT JOIN address a ON s.address_id = a.address_id;

--определим количество продаж каждого продавца
SELECT s.last_name, count(amount) FROM payment p
LEFT JOIN staff s ON p.staff_id = s.staff_id
GROUP BY s.last_name;

--посчитаем, сколько актеров играло в каждом фильме
SELECT title, count(actor_id) actor_q FROM film f 
JOIN film_actor a ON f.film_id = a.actor_id 
GROUP BY f.title 
ORDER BY actor_q DESC;

--сколько копий фильмов со словом Super в названии есть в наличии
SELECT title, count(inventory_id) FROM film f 
JOIN inventory i ON f.film_id = i.film_id 
WHERE title LIKE '%Super%'
GROUP BY title;

--выведем список покупателей с количеством их покупок в порядке убывания
SELECT c.last_name n, Count(p.amount) FROM customer c 
LEFT JOIN payment p ON c.customer_id = p.customer_id 
GROUP BY n, p.amount  
ORDER BY amount DESC;

--выведем имена и почтовые адреса всех покупателей из России
SELECT c.last_name, c.first_name, c.email FROM customer c 
JOIN address a ON c.address_id = a.address_id 
JOIN city ON a.city_id = city.city_id 
JOIN country c2 ON city.country_id = c2.country_id 
WHERE country = 'Russian Federation';

