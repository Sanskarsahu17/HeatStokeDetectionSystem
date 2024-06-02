import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv('Final_Dataset.csv')
#Deleting the useless column
df.drop(['Unnamed: 0'],axis=1,inplace=True)
#Splitting the Data
X=df.drop('Heat stroke',axis=1)
Y=df['Heat stroke']
# Split the data into training and test sets
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=9)

# Scale the data
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
#Training the Data

classifer = LogisticRegression(max_iter=200, solver='lbfgs')
classifer.fit(x_train_scaled, y_train)

joblib.dump(classifer, 'heat_stroke_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

#Prediction
y_pred = classifer.predict(x_test_scaled)
final_df = pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
#Accuracy and Performance

Model_accuracy=accuracy_score(y_test,y_pred)
print("Accuracy of Heat Stroke Predictor is ",Model_accuracy*100,"%")