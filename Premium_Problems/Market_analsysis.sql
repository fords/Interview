
Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10))
create table if not exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int)
create table if not exists Items (item_id int, item_brand varchar(10))
Truncate table Users
insert into Users (user_id, join_date, favorite_brand) values ('1', '2018-01-01', 'Lenovo')
insert into Users (user_id, join_date, favorite_brand) values ('2', '2018-02-09', 'Samsung')
insert into Users (user_id, join_date, favorite_brand) values ('3', '2018-01-19', 'LG')
insert into Users (user_id, join_date, favorite_brand) values ('4', '2018-05-21', 'HP')
Truncate table Orders
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2018-08-02', '2', '1', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2018-08-04', '1', '4', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2018-08-04', '1', '3', '4')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4')
Truncate table Items
insert into Items (item_id, item_brand) values ('1', 'Samsung')
insert into Items (item_id, item_brand) values ('2', 'Lenovo')
insert into Items (item_id, item_brand) values ('3', 'LG')
insert into Items (item_id, item_brand) values ('4', 'HP')

-- /*
Table: Users

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
```
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
Table: Orders
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
```
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
Table: Items
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
```
item_id is the primary key of this table.


Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

The query result format is in the following example:

Users table:
```
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
```
Orders table:
```
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
```
Items table:
```
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
```

Result table:
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
*/



-- CASE JOIN APPROACH

SELECT user_id AS buyer_id,
join_date,
COUNT( CASE WHEN order_date BETWEEN '2019-01-01' AND '2019-12-31' THEN t.order_id ELSE NULL END) AS orders_in_2019
FROM Users u LEFT JOIN  Orders t ON  user_id = buyer_id
GROUP BY user_id;


-- USING SUM
SELECT user_id AS buyer_id,
       join_date,
       sum(if(order_date>='2019-01-01',1,0)) AS orders_in_2019
FROM users u
LEFT JOIN orders o
ON u.user_id=o.buyer_id
GROUP BY u.user_id;


-- DIFFERENT APPROACH (long but fast query)
SELECT Users.user_id AS buyer_id, Users.join_date, IFNULL(sub1.orders_in_2019,0) AS orders_in_2019
FROM Users

LEFT JOIN (

  SELECT COUNT(order_id) AS orders_in_2019, buyer_id
  FROM (
      SELECT LEFT(order_date,4) AS "year", order_id, order_date ,  item_id , buyer_id ,
      seller_id
      FROM Orders
      WHERE LEFT(order_date,4)="2019"
  ) sub
  GROUP BY buyer_id

) sub1
ON sub1.buyer_id  = Users.user_id;
