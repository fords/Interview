Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10))
create table if not exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int)
create table if not exists Items (item_id int, item_brand varchar(10))
Truncate table Users
insert into Users (user_id, join_date, favorite_brand) values ('1', '2019-01-01', 'Lenovo')
insert into Users (user_id, join_date, favorite_brand) values ('2', '2019-02-09', 'Samsung')
insert into Users (user_id, join_date, favorite_brand) values ('3', '2019-01-19', 'LG')
insert into Users (user_id, join_date, favorite_brand) values ('4', '2019-05-21', 'HP')
Truncate table Orders
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2019-08-02', '2', '1', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2019-08-04', '1', '4', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2019-08-04', '1', '3', '4')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4')
Truncate table Items
insert into Items (item_id, item_brand) values ('1', 'Samsung')
insert into Items (item_id, item_brand) values ('2', 'Lenovo')
insert into Items (item_id, item_brand) values ('3', 'LG')
insert into Items (item_id, item_brand) values ('4', 'HP')


/*
  Table: Users

  +----------------+---------+
  | Column Name    | Type    |
  +----------------+---------+
  | user_id        | int     |
  | join_date      | date    |
  | favorite_brand | varchar |
  +----------------+---------+
  user_id is the primary key of this table.
  This table has the info of the users of an online shopping website where users can sell and buy items.
  Table: Orders

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | order_id      | int     |
  | order_date    | date    |
  | item_id       | int     |
  | buyer_id      | int     |
  | seller_id     | int     |
  +---------------+---------+
  order_id is the primary key of this table.
  item_id is a foreign key to the Items table.
  buyer_id and seller_id are foreign keys to the Users table.
  Table: Items

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | item_id       | int     |
  | item_brand    | varchar |
  +---------------+---------+
  item_id is the primary key of this table.


  Write an SQL query to find for each user, whether the brand of the second item (by date) they sold is their favorite brand. If a user sold less than two items, report the answer for that user as no.

  It is guaranteed that no seller sold more than one item on a day.

  The query result format is in the following example:

  Users table:
  +---------+------------+----------------+
  | user_id | join_date  | favorite_brand |
  +---------+------------+----------------+
  | 1       | 2019-01-01 | Lenovo         |
  | 2       | 2019-02-09 | Samsung        |
  | 3       | 2019-01-19 | LG             |
  | 4       | 2019-05-21 | HP             |
  +---------+------------+----------------+

  Orders table:
  +----------+------------+---------+----------+-----------+
  | order_id | order_date | item_id | buyer_id | seller_id |
  +----------+------------+---------+----------+-----------+
  | 1        | 2019-08-01 | 4       | 1        | 2         |
  | 2        | 2019-08-02 | 2       | 1        | 3         |
  | 3        | 2019-08-03 | 3       | 2        | 3         |
  | 4        | 2019-08-04 | 1       | 4        | 2         |
  | 5        | 2019-08-04 | 1       | 3        | 4         |
  | 6        | 2019-08-05 | 2       | 2        | 4         |
  +----------+------------+---------+----------+-----------+

  Items table:
  +---------+------------+
  | item_id | item_brand |
  +---------+------------+
  | 1       | Samsung    |
  | 2       | Lenovo     |
  | 3       | LG         |
  | 4       | HP         |
  +---------+------------+

  Result table:
  +-----------+--------------------+
  | seller_id | 2nd_item_fav_brand |
  +-----------+--------------------+
  | 1         | no                 |
  | 2         | yes                |
  | 3         | yes                |
  | 4         | no                 |
  +-----------+--------------------+

  The answer for the user with id 1 is no because they sold nothing.
  The answer for the users with id 2 and 3 is yes because the brands of their second sold items are their favorite brands.
  The answer for the user with id 4 is no because the brand of their second sold item is not their favorite brand.
  */

-- first approach
--used o1.seller_id = o2.seller_id AND o1.order_date > o2.order_date and HAVING(COUNT order_id) =1 to give
--  the order the users sold on the second date. And then used two LEFT JOIN to link the tables together.
SELECT user_id as seller_id,
if(i.item_brand = u.favorite_brand, "yes", "no") as 2nd_item_fav_brand
from Users u left join
    (SELECT o1.seller_id, o1.item_id, o1.order_date
    FROM Orders o1 JOIN Orders o2
    ON o1.seller_id = o2.seller_id AND o1.order_date > o2.order_date
    GROUP BY o1.seller_id, o1.order_date
    HAVING count(o1.order_id) = 1) t
ON u.user_id = t.seller_id
LEFT JOIN Items i
ON t.item_id = i.item_id
ORDER BY u.user_id;


-- second approach
--used a nested sub-query to calculate the "later" order first, and use the WHERE clause to filter out the second order they sold.
-- CASE WHEN is the same as the the IF() function in the first solution.
SELECT user_id AS seller_id,
(CASE WHEN i.item_brand = u.favorite_brand THEN "yes" ELSE "no" END) AS 2nd_item_fav_brand
FROM Users u LEFT JOIN
    (SELECT seller_id, item_id
    FROM orders o1
    WHERE 1 = (SELECT COUNT(order_id) FROM orders o2 WHERE o1.seller_id = o2.seller_id AND         o1.order_date>o2.order_date)) t1
ON u.user_id = t1.seller_id
LEFT JOIN Items i
ON t1.item_id = i.item_id
ORDER BY u.user_id;

-- third approach using limit and offset
select user_id as seller_id,
        (case
            when favorite_brand = (
                            select i.item_brand
                            from Orders o left join Items i
                            on o.item_id = i.item_id
                            where o.seller_id = u.user_id
                            order by o.order_date
                            limit 1 offset 1
                                  ) then "yes" else "no" end
         ) as "2nd_item_fav_brand"
from Users u;


/*

Test
Input:
{"headers":{"Users":["user_id","join_date","favorite_brand"],"Orders":["order_id","order_date","item_id","buyer_id","seller_id"],"Items":["item_id","item_brand"]},"rows":
{"Users":[[1,"2019-01-01","Lenovo"],[2,"2019-02-09","Samsung"],[3,"2019-01-19","LG"],[4,"2019-05-21","HP"]],
"Orders":[[1,"2019-08-01",4,1,2],[2,"2019-08-02",2,1,3],[3,"2019-08-03",3,2,3],[4,"2019-08-04",1,4,2],[5,"2019-08-04",1,3,4],[6,"2019-08-05",4,3,4],[7,"2019-08-06",2,2,4],[8,"2019-08-04",2,3,1]],
"Items":[[1,"Samsung"],[2,"Lenovo"],[3,"LG"],[4,"HP"]]}}

Output:
{"headers":["seller_id","2nd_item_fav_brand"],"values":[[1,"no"],[2,"yes"],[3,"yes"],[4,"yes"]]}
*/
