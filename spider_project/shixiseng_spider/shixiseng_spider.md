# 实习僧数据爬取
* 帮我爬取实习僧上面的实习生岗位信息
* 使用selenium，
* Xpath路径：
* 公司名：/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p[1]/a
* 职业名称：/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]/a
* 工资待遇：/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]/span
* 学历要求：0
* 城市名称:/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[2]/span[1]
* 数据存储到mysql，，加上自增的id，按字段顺序存入，空值补为0
* 数据库名：data_analyst_salary,地址：localhost,用户：root，密码：000000
* 表名：shixisheng_job_data
* 字段名：comName，jobName,salary,degree,city,treatment
* 代码要求：定义类，函数，if——name输入请求头参数，职业，城市,获取数据量

* 请求头参数




* 数据请求链接：



* 完整请求 URL