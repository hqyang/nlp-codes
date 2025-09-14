# %% [markdown]
# # Build a Rule-based Sentiment Classifier
# 
# This is a notebook for [NLP at SZTU, fall 2025](https://hqyang.github.io/nlp-fall25/), in which you can attempt to build a rule-based sentiment classifier. It will take in a text `X` and return a `label` of "1" if the sentiment of the text is positive, "-1" if the sentiment of the text is negative, and "0" if the sentiment of the text is neutral. You can test the accuracy of your classifier on the [Stanford Sentiment Treebank](http://nlp.stanford.edu/sentiment/index.html) by running the notebook all the way to end.
# 
# The only thing that you should change in this notebook is the following cell which contains two important elements. The first is `extract_features(X)`, which will extract a dictionary of (named) feature values from the text. You should create this by hand, and a simple example is shown for you. The second is `feature_weights`, a dictionary which will assign a weight to each extracted feature.
# 
# The final way the classifier decides whether to assign a positive, negative, or neutral label is by calculating the dot product `feature_weights * extract_features(X)`, and if the value is greater than zero, return 1, less than zero return -1, and if exactly zero return 0.
# 
# Let's have some fun trying to design a classifier 😁

# %%
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

# %% [markdown]
# ## Data Reading
# 
# Read in the data from the training and dev (or finally test) sets

# %%
def read_xy_data(filename: str) -> tuple[list[str], list[int]]:
    x_data = []
    y_data = []
    with open(filename, 'r') as f:
        for line in f:
            label, text = line.strip().split(' ||| ')
            x_data.append(text)
            y_data.append(int(label))
    return x_data, y_data

# %%
x_train, y_train = read_xy_data('../data/sst-sentiment-text-threeclass/train.txt')
x_test, y_test = read_xy_data('../data/sst-sentiment-text-threeclass/dev.txt')

# %%
print(x_train[0])
print(y_train[0])

# %% [markdown]
# ## Run the Classifier and Calculate Accuracy
# 
# Run the classifier over the training and dev (test) sets and calculate accuracy

# %%
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

# %%
def calculate_accuracy(x_data: list[str], y_data: list[int]) -> float:
    total_number = 0
    correct_number = 0
    for x, y in zip(x_data, y_data):
        y_pred = run_classifier(x)
        total_number += 1
        if y == y_pred:
            correct_number += 1
    return correct_number / float(total_number)

# %%
label_count = {}
for y in y_test:
    if y not in label_count:
        label_count[y] = 0
    label_count[y] += 1
print(label_count)

# %%
train_accuracy = calculate_accuracy(x_train, y_train)
test_accuracy = calculate_accuracy(x_test, y_test)
print(f'Train accuracy: {train_accuracy}')
print(f'Dev/test accuracy: {test_accuracy}')

# %% [markdown]
# ## Error Analysis
# 
# An important part of improving any system is figuring out where it goes wrong. The following two functions allow you to randomly observe some mistaken examples, which may help you improve the classifier. Feel free to write more sophisticated methods for error analysis as well.

# %%
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

# %%
find_errors(x_train, y_train)

# %%



