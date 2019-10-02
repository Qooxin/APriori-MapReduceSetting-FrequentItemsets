# APriori-MapReduceSetting-FrequentItemsets
大数据课程作业
在Map Reduce setting下，利用两组mapper, reducer计算给定数据集里的frequent itemsets。

假设有10,000个项目（编号为1至10,000）和10,000个篮子（编号为1至10,000）。提供的是项目列表，其中每一行代表一个购物篮中的项目。
例如，当一个购物篮包含项目1、2和3时，相应的行将为：
123

编写A-Priori算法，以回答以下问题。

问题1：threshold=1000，找出所有frequent itemsets。
问题2：threshold=100，找出frequent itemsets里item最多的itemsets。
