# train_model.py
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv('proyecto_final.csv')

X = df.drop('exito_robo', axis=1) 
y = df['exito_robo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)

"""hola=model.predict([[0.2,7.0,0.1,2.0]])
print(hola)"""
# Guardar el modelo
joblib.dump(clf, 'model.joblib')



