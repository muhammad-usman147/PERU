import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report

class ResignationPrediction():
  def __init__(self):
    pass 
  def preprocess(self,filename):
    try:
      print(f"[INFO] : Reading {filename}")
      self.data = pd.read_excel(filename)
      self.data.drop(columns=['Age','Education','EmployeeNumber','EducationField'],inplace=True,axis=1)
      le = LabelEncoder()
      self.data['Gender'] = le.fit_transform(self.data['Gender'])
      self.data['Department'] = le.fit_transform(self.data['Department'])
      self.data['JobRole'] = le.fit_transform(self.data['JobRole'])
      self.data['MaritalStatus'] = le.fit_transform(self.data['MaritalStatus'])
      self.data['Ovetime'].fillna('No', inplace=True)
      self.data['Ovetime'] = self.data['Ovetime'].replace('Si', 'Yes')
      self.data['Ovetime'] = self.data['Ovetime'].replace(1000, 'No')
      self.data['Ovetime'] = le.fit_transform(self.data['Ovetime'])
      self.data['Resigned'] = self.data['FECHA_DE_CESE'].apply(lambda x: 'Yes' if pd.notna(x) else 'No')
      self.data.drop(['FECHA_DE_CESE'],inplace=True,axis=1)
      self.data = self.data[self.data['FECHA_DE_INGRESO'] != 'SOLTERO (A)']
      # Feature engineering: Extract datetime features
      self.data['FECHA_DE_INGRESO'] = pd.to_datetime(self.data['FECHA_DE_INGRESO'])
      self.data['joining_year'] = self.data['FECHA_DE_INGRESO'].dt.year
      self.data['joining_month'] = self.data['FECHA_DE_INGRESO'].dt.month
      self.data['joining_day'] = self.data['FECHA_DE_INGRESO'].dt.day
      self.data.drop('FECHA_DE_INGRESO',inplace=True,axis=1)
      self.df = self.data.copy()
      self.X = self.data.drop('Resigned',axis=1)
      self.y = self.data['Resigned']
      self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
      smote = SMOTE(sampling_strategy='auto', random_state=42)
      self.X_train_resampled, self.y_train_resampled = smote.fit_resample(self.X_train, self.y_train)
      
    except Exception as e:
      print(e)
    


  
  def train(self):
    print("[INFO] : Training Started")
    self.rf_classifier = RandomForestClassifier(n_estimators=100, random_state=793,min_samples_split=5)
    self.rf_classifier.fit(self.X_train_resampled, self.y_train_resampled)
    print("[INFO] : Training Completed")



  def predict(self):
    y_pred = self.rf_classifier.predict(self.X_test)
    accuracy = accuracy_score(self.y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print(classification_report(self.y_test, y_pred))
    print("[INFO] : Saving Prediction Results -> results.xlsx")
    self.X_test= self.X_test.reset_index()
    self.predictions = pd.concat([pd.DataFrame(self.X_test),pd.DataFrame(y_pred)],axis=1)
    #self.predictions.to_excel("results.xlsx")
    print("[INFO] : SAVED TO -> results.xlsx")


def DisplayGraph():
  pass 


