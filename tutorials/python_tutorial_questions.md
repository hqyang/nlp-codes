# **集合 Collections**

## **列表 Lists**

1. 定义一个包含"Michael"和"Hart"的列表`names`，并打印列表的第一个元素。
2. 将上述`names`列表添加"Richard"后打印该列表。
3. 打印上述列表`names`的长度。
4. 将上述列表`names`，通过`+=`操作添加["Abi", "Kevin"]后打印该列表。
5. 写出两种创建空列表的代码，并命名为`more_names`。
6. 创建一个列表`stuff`并打印，依次包含整数1、列表["hi", "bye"]、浮点数-0.12和None。

### 列表切片

List slicing is a useful way to access a slice of elements in a list.

1. 定义一个包含[0, 1, 2, 3, 4, 5, 6]的列表`numbers`，打印该列表中从索引0（包含）到索引3（不包含）的元素。
2. 打印上述列表`numbers`两种情况: 1) 从开头到索引3（不包含）的元素; 2)从索引5（包含）到列表结尾的元素。
3. 打印上述列表`numbers`的所有元素。
4. 根据上述列表`numbers`，打印下面三种情况: 1) 列表的最后一个元素; 2) 列表的最后三个元素； 以及3) 从索引3（包含）到倒数第2个元素（不包含）的元素。

## 元组 Tuples

字典是哈希映射

1. 定义一个包含"Michael"和"Hart"的元组`names`，打印元组的第一个元素和元组的长度。
2. 尝试修改元组`names = ("Michael", "Hart")`的第一个元素为"Richard"，写出相应代码，看看发生什么问题？
3. 创建一个空元组`empty`,并打印它。
4. 创建一个只包含元素10的元组`single`，并打印它。

## 字典 Dictionary

1. 写出两种创建空字典的代码,空字典命名为`phonebook`。
2. 先创建一个包含键"Michael"、值"12-37"的字典`phonebook`，再向字典中添加键"Hart"、值"34-23"，写出相应代码。
3. 检查"Michael"和"Kevin"是否在上述定义的字典中`phonebook`并打印结果。
4. 打印上述字典`phonebook`键为"Hart"对应的值。
5. 删除上述字典`phonebook`键"Michael"对应的项后打印该字典。

# 循环 Loops

1. 编写一个for循环，打印0到4（包含0和4）的整数。
2. 定义列表`names = ["Michael", "Hart", "Richard"]`，遍历列表并打印每个元素。
3. 根据上述定义列表`names`，分别用两种方式遍历列表并打印每个元素的索引和值: 第一种用`range(len(names))`，第二种用`enumerate`。
4. 定义字典`phonebook = {"Michael": "12-37", "Hart": "34-23"}`，分别遍历字典的键、值以及键值对并打印，每部分结果中间用"---”隔开。

# NumPy

NumPy是一个Python库，它支持大型多维数组和矩阵的计算，并提供大量优化的高级数学函数集合来操作这些数组。

使用NumPy之前，您可能需要先安装numpy。

有很多方法来管理你的包，但我们建议使用Anaconda。

- 下载Anaconda。当你在一个新项目上工作时，创建一个良好的环境。
- 激活您的conda环境，并使用conda或pip安装该库，如果它们在conda中不可用。
- 如果您在命令行上运行脚本，请在conda环境中运行。
- 如果您使用的是Jupyter笔记本，请将conda环境添加到Jupyter笔记本: [https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874。创建您的Jupyter笔记本，并确认您在conda环境内核中（笔记本的右上角应该显示名称）。如果不是，请转到左上角的Kernel选项卡并单击Change](https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874%E3%80%82%E5%88%9B%E5%BB%BA%E6%82%A8%E7%9A%84Jupyter%E7%AC%94%E8%AE%B0%E6%9C%AC%EF%BC%8C%E5%B9%B6%E7%A1%AE%E8%AE%A4%E6%82%A8%E5%9C%A8conda%E7%8E%AF%E5%A2%83%E5%86%85%E6%A0%B8%E4%B8%AD%EF%BC%88%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%9A%84%E5%8F%B3%E4%B8%8A%E8%A7%92%E5%BA%94%E8%AF%A5%E6%98%BE%E7%A4%BA%E5%90%8D%E7%A7%B0%EF%BC%89%E3%80%82%E5%A6%82%E6%9E%9C%E4%B8%8D%E6%98%AF%EF%BC%8C%E8%AF%B7%E8%BD%AC%E5%88%B0%E5%B7%A6%E4%B8%8A%E8%A7%92%E7%9A%84Kernel%E9%80%89%E9%A1%B9%E5%8D%A1%E5%B9%B6%E5%8D%95%E5%87%BBChange) Kernel以更改为conda环境内核。
1. 导入numpy库（别名np），分别创建数组`x = np.array([1,2,3])`、`y = np.array([[3,4,5]])`、`z = np.array([[6,7],[8,9]])`，并打印这三个数组的形状和z。

**向量**可以表示为形状为（N,）的一维数组或形状为（N, 1）或（1，N）的二维数组。但需要注意的是，形状（N,）、（N, 1）和（1，N）并不相同，可能导致不同的行为（我们将在下面看到一些涉及矩阵乘法和广播的示例）。

矩阵通常表示为形状为（M， N）的二维数组。

确保代码提供预期行为的最佳方法是跟踪数组形状并尝试小型测试用例，或者在不确定时参考文档。

1. 创建数组`a = np.arange(10)`，将其重塑为5行2列的数组`b`，分别打印`a`和`b`。

## **阵列运算 Array Operations**

np.max (见文档https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html).

1. 定义数组`x = np.array([[1,2],[3,4], [5, 6]])`，打印其结果和形状。
2. 分别计算`np.max(x, axis = 1)`和`np.max(x, axis = 1, keepdims = True)`，并打印结果及其形状。
3. 定义数组`A = np.array([[1, 2], [3, 4]])`和`B = np.array([[3, 3], [3, 3]])`，打印A和B以及计算它们的逐元素级乘积并打印。

## 矩阵乘法 matrix multiplication

np.matmul 或 @

1. 根据上述数组`A`和`B`，用两种方式（`np.matmul`和`@`）计算它们的矩阵乘法并打印结果。

## 点积 dot product

1. 定义数组`u = np.array([1, 2, 3])`和`v = np.array([1, 10, 100])`，用两种方式（`np.dot`和`u.dot(v)`）计算它们的点积并打印结果。
2. 定义数组`W = np.array([[1, 2], [3, 4], [5, 6]])`和`v = np.array([1, 10, 100])`，完成下述任务: 
    1. 分别打印`W`和`v`的形状；
    2. 打印`np.dot(v, W)`和`np.dot(v, W)`计算后的形状；
    3. 尝试打印`np.dot(W, v)`，看看发生什么？
    4.  通过转置`W`使其正确执行并打印结果及形状。

## 索引 Indexing

切片/索引numpy数组是Python将（列表）切片概念扩展到N维。

1. 创建形状为(3, 4)的随机数组`x`，分别打印`x[:]`、`x[np.array([0, 2]), :]`、`x[1, 1:3]`、`x[x > 0.5]`、`x[:, :, np.newaxis]`，看看对应的结果跟你想的是不是一样？

## **广播 Broadcasting**

广播这个术语描述了NumPy在算术运算中如何处理不同形状的数组。

**一般广播规则**

当对两个数组进行操作时，NumPy会逐个比较它们的形状。它从末尾（即最右边）维度开始，然后向左工作。在以下情况下，两个维度是兼容的: 

- 它们相等，或者
- 其中一个是1（在这种情况下，轴上的元素沿着维度重复）

更多详细信息：https://numpy.org/doc/stable/user/basics.broadcasting.html

1. 创建形状为(3, 4)的随机数组`x`、形状为(3, 1)的随机数组`y`、形状为(1, 4)的随机数组`z`，计算`s = x + y`和`p = x * z`，并打印`x`、`y`、`s`、`z`、`p`的形状。
2. 创建形状为(3, 3)的全零数组`a`和数组`b = np.array([[1, 2, 3]])`，计算`a + b`并打印结果。
3. 创建形状为(3, 4)的随机数组`a`、形状为(3, 1)的随机数组`b`、形状为(3,)的随机数组`c`，分别计算`result1 = b + b.T`、`result2 = a + c`、`result3 = b + c`，并打印这三个结果的形状。

## 高效NumPy代码

1. 分别用两种方式（嵌套for循环和numpy切片操作）对形状为(1000, 1000)的随机数组`x`中第100行到第999行（包含）的所有元素加5，并使用`%%timeit`测试两种方式的执行效率。

