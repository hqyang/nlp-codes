# -*- coding: utf-8 -*-
# @Author: Haiqin Yang
# @Date:   2025-09-14 09:32:47
# @Last Modified by:   Haiqin Yang
# @Last Modified time: 2025-09-14 09:45:55
# %% [markdown]
# # Python Tutorial
# %% [markdown]
# ## Collections

# %% [markdown]
# Python has several built-in types that are useful for storing and manipulating data: list, tuple, dict. Here is the official Python documentation on these types (and many others): https://docs.python.org/3/library/stdtypes.html.

# %% [markdown]
# ### Lists

# %% [markdown]
# Lists are mutable arrays. Let's see how they work.

# %%
names = ["Michael", "Hart"]

# %%
# Index into list by index
print(names[0])

# %%
# Append to list (appends to end of list)
names.append("Richard")
print(names)

# %%
# Get length of list
print(len(names))

# %%
# Concatenate two lists
# += operator is a short hand for list1 = list1 + list2 (can also be used for -, *, / and on other types of variables)
names += ["Abi", "Kevin"]
print(names)

# %%
# Two ways to create an empty list
more_names = []
more_names = list()

# %%
# Create a list that contains different data types, this is allowed in Python
stuff = [1, ["hi", "bye"], -0.12, None]
print(stuff)

# %% [markdown]
# List slicing is a useful way to access a slice of elements in a list.

# %%
numbers = [0, 1, 2, 3, 4, 5, 6]

# Slices from start index (inclusive) to end index (exclusive)
print(numbers[0:3])

# %%
# When start index is not specified, it is start of list
# When end index is not specified, it is end of list
print(numbers[:3])
print(numbers[5:])

# %%
# : takes the slice of all elements along a dimension, is very useful when working with numpy arrays
print(numbers[:])

# %%
# Negative index wraps around, start counting from the end of list
print(numbers[-1])
print(numbers[-3:])
print(numbers[3:-2])

# %% [markdown]
# ### Tuples

# %% [markdown]
# Tuples are immutable arrays. Let's see how they work.

# %%
# Use parentheses for tuples, square brackets for lists
names = ("Michael", "Hart")

# %%
# Syntax for accessing an element and getting length are the same as lists
print(names[0])
print(len(names))

# %%
# But unlike lists, tuples do not support item re-assignment
names[0] = "Richard"

# %%
# Create an empty tuple
empty = tuple()
print(empty)

# Create a tuple with a single item, the comma is important
single = (10,)
print(single)

# %% [markdown]
# ## Dictionary

# %% [markdown]
# Dictionaries are hash maps. Let's see how they work.

# %%
# Two ways to create an empty dictionary
phonebook = {}
phonebook = dict()

# %%
# Create dictionary with one item
phonebook = {"Michael": "12-37"}
# Add another item
phonebook["Hart"] = "34-23"

# %%
# Check if a key is in the dictionary
print("Michael" in phonebook)
print("Kevin" in phonebook)

# %%
# Get corresponding value for a key
print(phonebook["Hart"])

# %%
# Delete an item
del phonebook["Michael"]
print(phonebook)

# %% [markdown]
# ## Loops

# %%
# Basic for loop
for i in range(5):
    print(i)

# %%
# To iterate over a list
names = ["Michael", "Hart", "Richard"]
for name in names:
    print(name)

# %%
# To iterate over indices and values in a list
# Way 1
for i in range(len(names)):
    print(i, names[i])

print("---")

# Way 2
for i, name in enumerate(names):
    print(i, name)

# %%
# To iterate over a dictionary
phonebook = {"Michael": "12-37", "Hart": "34-23"}

# Iterate over keys
for name in phonebook:
    print(name)

print("---")

# Iterate over values
for number in phonebook.values():
    print(number)

print("---")

# Iterate over keys and values
for name, number in phonebook.items():
    print(name, number)

# %% [markdown]
# ## NumPy
# NumPy is a Python library, which adds support for large, multi-dimensional arrays and matrices, along with a large collection of optimized, high-level mathematical functions to operate on these arrays.

# %% [markdown]
# You may need to install numpy first before importing it in the next cell.
# 
# There are many ways to manage your packages, but the workflow we suggest for this class is to use Anaconda.
#  - Download Anaconda. Create a conda environment when you work on a new project.
#  - Activate your conda environment and install libraries using conda or pip if they are not available in conda.
#  - If you are running scripts on command line, run inside your conda environment.
#  - If you are using a Jupyter notebook, add your conda environment to your Jupyter notebook: https://towardsdatascience.com/get-your-conda-environment-to-show-in-jupyter-notebooks-the-easy-way-17010b76e874. Create your Jupyter notebook and verify you're in your conda environment kernel (top right of notebook should display the name). If you're not, go to the Kernel tab on the top left and click Change kernel to change to your conda environment kernel.

# %%
# Import numpy
import numpy as np

# %%
# Create numpy arrays from lists
x = np.array([1,2,3])
a = np.array([[1,2,3]])


y = np.array([[3,4,5]])
z = np.array([[6,7],[8,9]])

# Let's take a look at their shapes.
# When working with numpy arrays, .shape will be a very useful debugging tool
print(x.shape)
print(y.shape)
print()
print(z)
print(z.shape)

# %% [markdown]
# Vectors can be represented as 1-D arrays of shape (N,) or 2-D arrays of shape (N, 1) or (1, N). But it's important to note that the shapes (N,), (N, 1), and (1,N) are not the same and may result in different behavior (we'll see some examples below involving matrix multiplication and broadcasting).
# 
# Matrices are generally represented as 2-D arrays of shape (M, N).
# 
# The best way to ensure your code gives you the behavior you expect is to keep track of your array shapes and try out small test cases or refer back to documentation when you are unsure.

# %%
a = np.arange(10)
b = a.reshape((5, 2))
print(a)
print()
print(b)

# %% [markdown]
# ### Array Operations

# %% [markdown]
# There are many NumPy operations that can be used to reduce a numpy array along an axis.
# 
# Let's look at the np.max operation (documentation: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html).

# %%
x = np.array([[1,2],[3,4], [5, 6]])
print(x)
print()
print(x.shape)

# %%
print(np.max(x, axis = 1))

# %%
print(np.max(x, axis = 1).shape)

# %%
print(np.max(x, axis = 1, keepdims = True))

# %%
print(np.max(x, axis = 1, keepdims = True).shape)

# %% [markdown]
# Next, let's look at some matrix operations. Let's take an element-wise product (Hadamard product).

# %%
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 3], [3, 3]])
print(A)
print(B)
print("---")
print(A * B)

# %% [markdown]
# We can do matrix multiplication with np.matmul or @.

# %%
# One way to do matrix multiplication
print(np.matmul(A, B))

# Another way to do matrix multiplication
print(A @ B)

# %% [markdown]
# We can take the dot product or a matrix vector product with np.dot.

# %%
u = np.array([1, 2, 3])
v = np.array([1, 10, 100])

print(np.dot(u, v))

# Can also call numpy operations on the numpy array, useful for chaining together multiple operations
print(u.dot(v))

# %%
W = np.array([[1, 2], [3, 4], [5, 6]])
print(v.shape)
print(W.shape)

# This works.
print(np.dot(v, W))
print(np.dot(v, W).shape)

# %%
# This does not. Why?
print(np.dot(W, v))

# %%
# We can fix the above issue by transposing W.
print(np.dot(W.T, v))
print(np.dot(W.T, v).shape)

# %% [markdown]
# ###  Indexing

# %% [markdown]
# Slicing / indexing numpy arrays is a extension of the Python concept of slicing (lists) to N dimensions.

# %%
x = np.random.random((3, 4))

# Selects all of x
print(x[:])

# %%
# Selects the 0th and 2nd rows
print(x[np.array([0, 2]), :])

print("---")

# Selects 1st row as 1-D vector and and 1st through 2nd elements
print(x[1, 1:3])

# %%
# Boolean indexing
print(x[x > 0.5])

# %%
# 3-D vector of shape (3, 4, 1)
print(x[:, :, np.newaxis])

# %% [markdown]
# ### Broadcasting

# %% [markdown]
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
# 
# **General Broadcasting Rules**
# 
# When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimensions and works its way left. Two dimensions are compatible when:
# - they are equal, or
# - one of them is 1 (in which case, elements on the axis are repeated along the dimension)
# 
# More details: https://numpy.org/doc/stable/user/basics.broadcasting.html

# %%
x = np.random.random((3, 4))

y = np.random.random((3, 1))
z = np.random.random((1, 4))

# In this example, y and z are broadcasted to match the shape of x.
# y is broadcasted along dim 1.
s = x + y
# z is broadcasted along dim 0.
p = x * z

# %%
print(x.shape)
print()
print(y.shape)
print(s.shape)

# %%
print(x.shape)
print()
print(s.shape)
print(p.shape)

# %%
a = np.zeros((3, 3))
b = np.array([[1, 2, 3]])
print(a)
print()
print(a+b)

# %% [markdown]
# Let's look at a more complex example.

# %%
a = np.random.random((3, 4))
b = np.random.random((3, 1))
c = np.random.random((3, ))

# %% [markdown]
# What is the expected broadcasting behavior for these operations? What do the following operations give us? What are the resulting shapes?

# %%
result1 = b + b.T

print(b.shape)
print(b.T.shape)
print(result1.shape)
print(result1)

# %%
result2 = a + c

print(a.shape)
print(c.shape)
print(result2.shape)
print(result2)

# %%
result3 = b + c

print(b.shape)
print(c.shape)
print(result3.shape)
print(result3)

# %% [markdown]
# ### Efficient NumPy Code

# %% [markdown]
# When working with numpy arrays, avoid explicit for-loops over indices/axes at all costs. For-loops will dramatically slow down your code (~10-100x).

# %% [markdown]
# We can time code using the %%timeit magic. Let's compare using explicit for-loop vs. using numpy operations.

# %%
%%timeit
x = np.random.rand(1000, 1000)
for i in range(100, 1000):
    for j in range(x.shape[1]):
        x[i, j] += 5

# %%
%%timeit
x = np.random.rand(1000, 1000)
x[np.arange(100,1000), :] += 5

# %%



