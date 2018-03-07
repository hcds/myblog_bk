---
title: oracle 
date: 2018-02-22 16:37:39
tags: 技術
---

実行計画を読む３つのポイント
データ・アクセス方法
TABLE ACCESS FULL
INDEX UNIQUE SCAN
INDEX RANCE SCAN
INDEX FULL SCAN
INDEX FAST FULL SCAN
INDEX SKIP SCAN
表結合方法
Merge Join([排序]合并联接)
Nested Loops(嵌套循环联接)
Hash Match都是物理运算符。
表結合順序


結論：

A表(大 100000), B表(小 1000), id(索引)
~~~SQL
(1) select * from A where A.id in (select id form B)
(2) select * from A where exists (select 1 form B where id = A.id)
~~~

效率 (1) > (2)

~~~SQL
(3) select * from B where B.id in (select id form A)
(4) select * from B where exists (select 1 form A where id = B.id)
~~~

效率 (4) > (3)

in 是先做子查询然后返回结果集，在和外表作hash join，而exists是对外表作loop，每次loop再对内表进行查询。

查询次数 
(1) A表索引条数 x 1000(B表)
(2) 100000(A表) x B表索引条数
(3) B表索引条数 x 100000(A表)
(4) 1000(B表) x A表索引条数




