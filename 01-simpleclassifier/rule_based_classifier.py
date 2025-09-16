# -*- coding: utf-8 -*-
# @Author: Haiqin Yang
# @Date:   2025-09-16 17:41:32
# @Last Modified by:   Haiqin Yang
# @Last Modified time: 2025-09-16 20:37:32

# 构建基于规则的情感分类器

这是[深圳技术大学2025秋季微专业课](https://hqyang.github.io/nlp-fall25/)使用的Jupyter Notebook.下面尝试构建基一个基于规则的情感分类器。它将接收文本“X”并返回一个“标签”，如果文本的情感是积极的，则为“1”，如果文本的情感是消极的，则为“-1”，如果文本的情感是中性的，则为“0”。通过运行这个notebook 你可以在[Stanford Sentiment Treebank](http://nlp.stanford.edu/sentiment/index.html)上测试分类器的准确性。

Notebook唯一需要更改的是以下两个单元格:
1. `extract_features(X)`: 它将从文本中提取（命名的）特征值的字典。您应该自己手动创建字典，下面将为您展示一个简单的示例。
2. `feature_weights`: 这是一个字典，它将为每个提取的特征分配一个权重。

分类器决定是否分配积极、消极或中性标签的最终方法是通过计算点积`feature_weights * extract_features(X)`，如果值大于零，返回1，小于零返回-1，如果正好为零返回0。

让我们来尝试设计一个分类器 😁
"""

def extract_features(x: str) -> dict[str, float]:
    features = {}
    x_split = x.split(' ')

    # Count the number of "good words" and "bad words" in the text
    good_words = ['love', 'good', 'nice', 'great', 'enjoy', 'enjoyed']
    bad_words = ['hate', 'bad', 'terrible', 'disappointing', 'sad', 'lost', 'angry']
    for x_word in x_split:
        if x_word in good_words:
            features['good_word_count'] = features.get('good_word_count', 0) + 1
        if x_word in bad_words:
            features['bad_word_count'] = features.get('bad_word_count', 0) + 1

    # The "bias" value is always one, to allow us to assign a "default" score to the text
    features['bias'] = 1

    return features

feature_weights = {'good_word_count': 1.0, 'bad_word_count': -1.0, 'bias': 0.5}

"""## Data Reading

Read in the data from the training and dev (or finally test) sets
"""

def read_xy_data(filename: str) -> tuple[list[str], list[int]]:
    x_data = []
    y_data = []
    with open(filename, 'r') as f:
        for line in f:
            label, text = line.strip().split(' ||| ')
            x_data.append(text)
            y_data.append(int(label))
    return x_data, y_data

x_train, y_train = read_xy_data('../data/sst-sentiment-text-threeclass/train.txt')
x_test, y_test = read_xy_data('../data/sst-sentiment-text-threeclass/dev.txt')

print(x_train[0])
print(y_train[0])

"""## Run the Classifier and Calculate Accuracy

Run the classifier over the training and dev (test) sets and calculate accuracy
"""

def run_classifier(x: str) -> int:
    score = 0
    for feat_name, feat_value in extract_features(x).items():
        score = score + feat_value * feature_weights.get(feat_name, 0)
    if score > 0:
        return 1
    elif score < 0:
        return -1
    else:
        return 0

def calculate_accuracy(x_data: list[str], y_data: list[int]) -> float:
    total_number = 0
    correct_number = 0
    for x, y in zip(x_data, y_data):
        y_pred = run_classifier(x)
        total_number += 1
        if y == y_pred:
            correct_number += 1
    return correct_number / float(total_number)

label_count = {}
for y in y_test:
    if y not in label_count:
        label_count[y] = 0
    label_count[y] += 1
print(label_count)

train_accuracy = calculate_accuracy(x_train, y_train)
test_accuracy = calculate_accuracy(x_test, y_test)
print(f'Train accuracy: {train_accuracy}')
print(f'Dev/test accuracy: {test_accuracy}')

"""## Error Analysis 误差分析

改进任何系统的一个重要部分就是找出问题出在哪里。下面这个函数允许您随机观察一些错误的示例，这可能有助于您改进分类器。您也可以为错误分析编写更复杂的方法。
"""

import random
def find_errors(x_data, y_data):
    error_ids = []
    y_preds = []
    for i, (x, y) in enumerate(zip(x_data, y_data)):
        y_preds.append(run_classifier(x))
        if y != y_preds[-1]:
            error_ids.append(i)
    for _ in range(5):
        my_id = random.choice(error_ids)
        x, y, y_pred = x_data[my_id], y_data[my_id], y_preds[my_id]
        print(f'{x}\ntrue label: {y}\npredicted label: {y_pred}\n')

find_errors(x_train, y_train)