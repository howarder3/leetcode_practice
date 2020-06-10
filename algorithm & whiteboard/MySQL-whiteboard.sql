# # 
# # Old Content below(Java):
# # 
# # table name : order_tab
# # date    user_id    bought_A    bought_B
# # 1        101        Y            N
# # 2        101        N            Y
# # 2        102        Y            N
# # 3        103        N            N
# # 4        103        N            Y
# # 4        104        Y            Y
# # 

    
# #----------------------------------------
# 1. select the userids who baught both A and B on data = 2,  
# distinct 重複值只列一次

SELECT distinct 
user_id from order_tab
WHERE date = 2 AND bought_A = 'Y' AND bought_B = 'Y'



# 2. Select all users that have bought both A & B in the history

-- SELECT a.user_id, b.user_id
-- FROM order_tab as a
-- LEFT join order_tab as b
-- ON a.user_id = b.user_id

-- SELECT a.runoob_id, a.runoob_author, b.runoob_count 
-- FROM order_tab as a 
-- LEFT JOIN order_tab as b
-- ON a.user_id = b.user_id


-- OR (聯集)
-- SELECT user_id FROM order_tab WHERE bought_A = 'Y'
-- UNION
-- SELECT user_id FROM order_tab WHERE bought_B = 'Y'

SELECT user_id FROM
(SELECT user_id FROM order_tab WHERE bought_A = 'Y') as a
INNER JOIN
(SELECT user_id FROM order_tab WHERE bought_B = 'Y') as b
ON a.user_id = b.user_id


-- select a.user_id
-- (
--     SELECT distinct user_id from order_tab
--     WHERE bought_A = 'Y' 
-- )a
-- left join
-- (

-- SELECT distinct user_id from order_tab
-- WHERE bought_B = 'Y'
-- )b
-- on a.user_id = b.user_id


# left join / cross join / inner 
# join

# -- hints: 
    
#     1. query all the users have baught A in the history 
#     2. query all the users have baught B in the history
#     3. both baught A & B (union or  join )
```