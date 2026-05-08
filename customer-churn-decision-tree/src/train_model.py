import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    df=pd.read_csv("data/customer_churn.csv")

    df_encoded = pd.get_dummies(df, drop_first=True)

    X = df_encoded.drop("Churn_Yes",axis=1)
    y = df_encoded["Churn_Yes"]

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier(criterion="gini",
                                   max_depth=3,
                                   min_samples_split=2,
                                   random_state=42)
    model.fit(X_train,y_train)

    y_pred =model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    joblib.dump(model,"models/decision_tree_model.pkl")

    print("Model saved successfully!")

if __name__=="__main__":
    train_model()
    