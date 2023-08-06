# fasterrisk <!-- omit in toc -->

This repository contains source code to our NeurIPS 2022 paper:

**FasterRisk: Fast and Accurate Interpretable Risk Scores**

# Table of Content <!-- omit in toc -->
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)


# Introduction
Over the last century, risk scores have been the most popular form of predictive model used in healthcare and criminal justice. Risk scores are sparse linear models with integer coefficients; often these models can be memorized or placed on an index card. Below is a risk score example created on the 3rd fold of the [adult dataset](https://github.com/ustunb/risk-slim/tree/master/examples/data) by FasterRisk, predicting salary> 50K.

|                            |             |       |
| :---                       |    ---:     |  :--- |
|1.  No High School Diploma  |   -4 points |   ... |
|2.     High School Diploma  |   -2 points | + ... |
|3.            Age 22 to 29  |   -2 points | + ... |
|4.       Any Capital Gains  |    3 points | + ... |
|5.                 Married  |    4 points | + ... |
|                            |       SCORE | =     |

|      |        |        |        |        |        |        |        |
|:---  | :----: | :----: | :----: | :----: | :----: | :----: | :----: | 
|SCORE |  -8.0  |  -6.0  |  -5.0  |  -4.0  |  -3.0  |  -2.0  |  -1.0  |
|RISK  |   0.1% |   0.4% |   0.7% |   1.2% |   2.3% |   4.2% |   7.6% |
|SCORE |   0.0  |   1.0  |   2.0  |   3.0  |   4.0  |   5.0  |   7.0  |        
|RISK  |  13.3% |  22.3% |  34.9% |  50.0% |  65.1% |  77.7% |  92.4% |

Typically, risk scores have been created either without data or by rounding logistic regression coefficients, but these methods do not reliably produce high-quality risk scores. Recent work used mathematical programming, which is computationally slow.

We introduce an approach for efficiently producing a collection of high-quality risk scores learned from data. Specifically, our approach produces a pool of almost-optimal sparse continuous solutions, each with a different support set, using a beam-search algorithm. Each of these continuous solutions is transformed into a separate risk score through a "star ray" search, where a range of multipliers are considered before rounding the coefficients sequentially to maintain low logistic loss. Our algorithm returns all of these high-quality risk scores for the user to consider. This method completes within minutes and can be valuable in a broad variety of applications.

# Installation

```bash
conda create -n FasterRisk python=3.9 # create a virtual environment
conda activate FasterRisk # activate the virtual environment
python -m pip install fasterrisk # pip install the fasterrisk package
```


# Usage
Please see the [example.ipynb](./docs/example.ipynb) jupyter notebook for a detailed tutorial on how to use FasterRisk in a python environment.

There are two major two classes for the users to interact with:
- **RiskScoreOptimizer**
```python
sparsity = 5 # produce a risk score model with 5 nonzero coefficients 

# import data
X_train, y_train = ...

# initialize a risk score optimizer
m = RiskScoreOptimizer(X = X_train, y = y_train, k = sparsity)

# perform optimization
m.optimize()

# get all top m solutions from the final diverse pool
arr_multiplier, arr_intercept, arr_coefficients = m.get_models() # get m solutions from the diverse pool; Specifically, arr_multiplier.shape=(m, ), arr_intercept.shape=(m, ), arr_coefficients.shape=(m, p)

# get the first solution from the final diverse pool by passing an optional model_index; models are ranked in order of increasing logistic loss
multiplier, intercept, coefficients = m.get_models(model_index = 0) # get the first solution (smallest logistic loss) from the diverse pool; Specifically, multiplier.shape=(1, ), intercept.shape=(1, ), coefficients.shape=(p, )

```

- **RiskScoreClassifier**
```python
# import data
X_featureNames = ... # X_featureNames is a list of strings, each of which is the feature name

# create a classifier
clf = RiskScoreClassifier(multiplier = multiplier, intercept = intercept, coefficients = coefficients, featureNames = featureNames)

# get the predicted label
y_pred = clf.predict(X = X_train)

# get the probability of predicting y[i] with label +1
y_pred_prob = clf.predict_prob(X = X_train)

# compute the logistic loss
logisticLoss_train = clf.compute_logisticLoss(X = X_train, y = y_train)

# get accuracy and area under the ROC curve (AUC)
acc_train, auc_train = clf.get_acc_and_auc(X = X_train, y = y_train) 

# print the risk score model card
m.print_model_card() 
```

# License

`fasterrisk` was created by Jiachang Liu. It is licensed under the terms of the BSD 3-Clause license.

# Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

# Credits <!-- omit in toc -->

`fasterrisk` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
