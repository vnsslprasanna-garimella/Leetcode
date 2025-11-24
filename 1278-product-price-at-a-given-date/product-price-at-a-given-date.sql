# Write your MySQL query statement below
With changes as (
Select product_id, new_price ,change_date,
row_number() over (partition by product_id order by change_date desc) as rn
from products
where change_date <= '2019-08-16'
)
Select 
p.product_id , coalesce(c.new_price,10) as price
from 
(Select distinct product_id from Products) p
left join changes c on p.product_id = c.product_id and c.rn = 1 
