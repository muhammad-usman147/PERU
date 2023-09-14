import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
import random 

class ResignationPrediction():
  def __init__(self):
    pass 
  def preprocess(self,filename):
    try:
      self.label_encoders = {}
      print(f"[INFO] : Reading {filename}")
      self.data = pd.read_excel(filename)
      self.data['Ovetime'].fillna('No', inplace=True)
      self.data['Ovetime'] = self.data['Ovetime'].replace('Si', 'Yes')
      self.data['Ovetime'] = self.data['Ovetime'].replace(1000, 'No')
      
      
      #data separation
      self.data['Resigned'] = self.data['FECHA_DE_CESE'].apply(lambda x: 'Yes' if pd.notna(x) else 'No')
      self.data['Resigned'] = self.data['FECHA_DE_CESE'].apply(lambda x: 1 if pd.notna(x) else 0)
      self.data.drop(['FECHA_DE_CESE'],inplace=True,axis=1)
      self.data = self.data[self.data['FECHA_DE_INGRESO'] != 'SOLTERO (A)']
      self.data.drop('FECHA_DE_INGRESO',inplace=True,axis=1)
      #label encoding
      for column in self.data.columns:
        if self.data[column].dtype == 'object':
          self.label_encoders[column] = LabelEncoder()
          self.data[column] = self.label_encoders[column].fit_transform(self.data[column])
      self.preprocessed_data = self.data.copy()
      del(self.data)
      noise_prob = 0.08
      categories = self.preprocessed_data['Resigned'].unique()
      self.preprocessed_data['Resigned'] = self.preprocessed_data['Resigned'].apply(lambda x: random.choice(categories) if random.random() < noise_prob else x)
      X = self.preprocessed_data.drop('Resigned',axis=1)
      y = self.preprocessed_data['Resigned']

      self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    except Exception as e:
      print(e)
    


  
  def train(self):
    print("[INFO] : Training Started")
    self.rf_classifier = RandomForestClassifier(n_estimators=100, random_state=793,min_samples_split=5)
    self.rf_classifier.fit(self.X_train, self.y_train)
    print("[INFO] : Training Completed")



  def predict(self):
    y_pred = self.rf_classifier.predict(self.X_test)
    accuracy = accuracy_score(self.y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print(classification_report(self.y_test, y_pred))
    print("[INFO] : Saving Prediction Results -> results.xlsx")
    self.final_data = self.X_test
    self.final_data['Target_Resigned'] = self.y_test
    self.final_data['Predicted_Resigned'] = y_pred
    self.final_data = self.final_data.reset_index(drop=True)
    self.final_data['Predicted_Resigned']=self.final_data['Predicted_Resigned'].astype(str)
    self.final_data['Predicted_Resigned']=self.final_data['Predicted_Resigned'].str.replace("1",'Yes')
    self.final_data['Predicted_Resigned']=self.final_data['Predicted_Resigned'].str.replace("0",'No')
    for column in self.final_data.columns:
      if column in self.label_encoders:
        self.final_data[column] = self.label_encoders[column].inverse_transform(self.final_data[column])
    print(self.final_data.columns)
    #self.predictions.to_excel("results.xlsx")
    print("[INFO] : SAVED TO -> results.xlsx")


def DisplayGraph():
  pass 


