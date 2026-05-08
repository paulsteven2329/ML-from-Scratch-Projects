# Customer Churn Prediction using Decision Tree

This project predicts whether a customer is likely to churn using a Decision Tree Classifier.

## Problem Statement

Customer churn is a major business problem in SaaS, telecom, banking, and subscription-based companies. The goal of this project is to identify customers who are likely to leave based on their usage and account information.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Machine Learning Algorithm

Decision Tree Classifier

## Features Used

- Age
- Tenure
- Monthly Charges
- Support Calls
- Contract Type

## Target

- Churn: Yes or No

## Steps Performed

1. Loaded customer churn dataset
2. Performed basic data analysis
3. Encoded categorical variables
4. Split data into training and testing sets
5. Trained Decision Tree Classifier
6. Evaluated model using accuracy, confusion matrix, and classification report
7. Visualized the decision tree
8. Checked feature importance
9. Saved the trained model

## Key Learning

This project helped me understand:

- Gini impurity
- Pure and impure nodes
- Samples, value, and class in Decision Trees
- Model training and prediction
- Feature importance
- Overfitting control using max_depth and min_samples_leaf

## How to Run

```bash
pip install -r requirements.txt
python src/train_model.py