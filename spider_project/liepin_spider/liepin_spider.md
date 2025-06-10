# 猎聘数据爬取
* 帮我爬取猎聘上面的关于数据分析师的实习生岗位信息
* 使用requests，数据在jobList内参考data_liepin_ex.json文件
* 提取字段：comp.compName，job.title，job.salary，jobDegree，job.labels[2]
* 字段名表示：公司名，职业名称，工资待遇，学历要求，城市名称
* 数据存储到mysql，，加上自增的id，按字段顺序存入，空值补为0
* 数据库名：data_analyst_salary,地址：localhost,用户：root，密码：000000
* 表名：liepin_job_data
* 字段名：comName，jobName,salary,degree,city,treatment
* 代码要求：定义类，函数，if——name输入请求头参数，职业，城市,获取数据量

* 请求头参数




* 数据请求链接：


* 完整请求 URL