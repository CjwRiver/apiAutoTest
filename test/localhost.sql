# 查看整个表
select * from `user`
# 查看所有成员和密码
select uname,pwd from `user`
# 查看uname为tom的密码
select pwd from `user` where uname='tom'
# 查看id在123之间的uname/pwd
select uname,pwd from `user` where uid in (1,2,3)
# 查看密码为123的总人数
select count(pwd) from `user` where pwd='123'
# 查看不重复的pwd
select distinct pwd from `user`
# 查看pwd包含1的用户
select uname,pwd from `user` where pwd like '1%'
# 查询pwd 为 1的用户
select uname,pwd from `user` where pwd not like '%1%'
# 查看密码为1234的并且uname包含t字母的用户
select uname from `user` where pwd='5534'and uname like '%t%'
# 查看表以密码分组
select * from `user` group by uname
# 插入一条数据
insert into `user` (uname,pwd) values ('xiaoming2','1234')
# 插入一条数据
insert into `user` (uname,pwd) values ('xiaoming5','1234'),('tt','5534')
#
select * from `user` 
