SELECT ship_country FROM orders
WHERE ship_country LIKE 'U%'

SELECT orders.order_id,orders.customer_id, freight , ship_country FROM orders
WHERE ship_country LIKE 'N%'
ORDER BY freight DESC
LIMIT 10

SELECT title,home_phone,region FROM employees
WHERE region IS NULL



SELECT COUNT(customers.company_name) FROM customers
WHERE region IS NULL



SELECT suppliers.country, COUNT(company_name) FROM suppliers
GROUP BY suppliers.country ORDER BY COUNT(company_name) DESC


SELECT ship_country,SUM(orders.freight) FROM orders
GROUP BY ship_country HAVING SUM(orders.freight)>2750
ORDER BY SUM(orders.freight) DESC


SELECT country,COUNT(country) FROM suppliers
GROUP BY country ORDER BY COUNT(country)


SELECT * FROM suppliers
GROUP BY country ORDER BY COUNT(country)