import streamlit as st

def upload():
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

upload()

def  dataAnalyze():
        data = pd.read_excel('TestData.xlsx')
        np.random.seed(42)
        X = data.drop('target', axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X, y, test_size=0.2)
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)
        X_data = pd.read_csv('newTest.csv')
        clf.predict(X_data)
        # #X_test.head()
        prob = clf.predict_proba(X_data[:100])
        # #print(prob)
        X_data["prediction_prob"] = clf.predict(X_data)
        pd.set_option('display.max_rows', None)
        X_data.head()        
      
       
       
if st.button('Start Analyse'):
    dataAnalyze() 
        




