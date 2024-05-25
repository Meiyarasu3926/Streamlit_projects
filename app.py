import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import pickle


diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinson_model = pickle.load(open('parkinson_model.sav', 'rb'))


st.markdown("""
	<style>
    		.stTextInput>div>div>input {
       		background-color: #ADD8E6;  /* Light blue background */
       		color: #000000;  /* Black text */
    }
    	</style>
""", unsafe_allow_html=True)

def predict(new_data, model):
	new_data = np.asarray(new_data)
	new_data = new_data.reshape(1, -1)
	predict = model.predict(new_data)
	
	return predict[0]

with st.sidebar:
	selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction', 'Heart disease Prediction', 'Parkinson Prediction'], icons=['activity', 'heart-pulse', 'person'], default_index=0)
	
	# Diabetes page
if selected == 'Diabetes Prediction':
	st.title('Diabetes Prediction')
	
	col1, col2, col3 = st.columns(3)
	
	with col1:
		Pregnancies = st.text_input("Number of pregnancies")
	with col2:
		Glucose = st.text_input("Glucose level")
	with col3:	
		BloodPressure = st.text_input("Blood pressure value")
	with col1:
		SkinThickness = st.text_input("skin thickness value")
	with col2:
		Insulin = st.text_input("Insulin level")
	with col3:
		BMI = st.text_input("BMI value")
	with col1:
		DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
	with col2:
		Age = st.text_input("Age of the person")
	
	lst = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
	dignosis = '' 
	if st.button('diabetes test'):
		prediction = predict(lst, diabetes_model)
		st.write(prediction)
		if prediction == 1:
			dignosis = "The person is Diabetic"
		else:
			dignosis = "The person is not Diabetic"
	st.success(dignosis)
if selected == 'Heart disease Prediction':
	st.title('Heart disease Prediction')
	
	col1, col2, col3 = st.columns(3)
	
	with col1:
		age = st.text_input("Age of the person")
	with col2:
		sex = st.text_input("Sex")
	with col3:
		cp = st.text_input("chest pain type ")
	with col1:
		trestbps = st.text_input("resting blood pressure")
	with col2:
		chol = st.text_input("serum cholestoral in mg/dl")
	with col3:
		fbs = st.text_input("fasting blood sugar > 120 mg/dl")
	with col1:
		restecg = st.text_input("resting electrocardiographic results (values 0,1,2)")
	with col2:
		thalach = st.text_input("maximum heart rate achieved")
	with col3:
		exang = st.text_input("exercise induced angina")
	with col1:
		oldpeak = st.text_input("ST depression induced by exercise relative to rest")
	with col2:
		slope = st.text_input("the slope of the peak exercise ST segment")
	with col3:
		ca = st.text_input("number of major vessels (0-3) colored by flourosopy")
	with col1:
		thal = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
	
	lst = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
	result = ''
	if st.button('heart disease test'):
		prediction = predict(lst, heart_disease_model)
		if prediction == 1:
			result = 'person have heart disease'
		else:
			result = 'person not have heart disease'
	st.success(result)
if selected == 'Parkinson Prediction':
	st.title('Parkinson Prediction')
	
	col1, col2, col3, col4, col5 = st.columns(5)	
		
	with col1:
        	fo = st.text_input('MDVP:Fo(Hz)')

	with col2:
	        fhi = st.text_input('MDVP:Fhi(Hz)')
	        
	with col3:
        	flo = st.text_input('MDVP:Flo(Hz)')

	with col4:
        	Jitter_percent = st.text_input('MDVP:Jitter(%)')
	
	with col5:
        	Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

	with col1:
        	RAP = st.text_input('MDVP:RAP')

	with col2:
        	PPQ = st.text_input('MDVP:PPQ')

	with col3:
        	DDP = st.text_input('Jitter:DDP')

	with col4:
        	Shimmer = st.text_input('MDVP:Shimmer')

	with col5:
        	Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

	with col1:
        	APQ3 = st.text_input('Shimmer:APQ3')

	with col2:
        	APQ5 = st.text_input('Shimmer:APQ5')

	with col3:
        	APQ = st.text_input('MDVP:APQ')

	with col4:
        	DDA = st.text_input('Shimmer:DDA')

	with col5:
        	NHR = st.text_input('NHR')

	with col1:
        	HNR = st.text_input('HNR')

	with col2:
        	RPDE = st.text_input('RPDE')
	
	with col3:
        	DFA = st.text_input('DFA')

	with col4:
        	spread1 = st.text_input('spread1')

	with col5:
        	spread2 = st.text_input('spread2')
	
	with col1:
        	D2 = st.text_input('D2')

	with col2:
        	PPE = st.text_input('PPE')
	
	res = ''
	lst = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE] 
	if st.button('parkinson test'):
		prediction = predict(lst, parkinson_model)
		
		if prediction == 1:	
			res =  "The person has Parkinson's disease" 
		else:
			res = "The person doesn't have Parkinson's disease"
	
	st.success(res)
