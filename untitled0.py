import numpy as np
import pickle
import streamlit as st

load_model=pickle.load(open('model_an.sav','rb'))

def pred(input_data):

# change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)


    if (prediction[0]== 0):
        return 'The Person is not anemic'
    else:
        return 'The Person is anemic'




def main():
  st.title('animea')
  Gender=st.number_input('enter age')
  #'Hemoglobin', 'MCH', 'MCHC', 'MCV'
  Hemoglobin=st.number_input('enter heam')
  MCH=st.number_input('enter mch')
  MCHC=st.number_input('enter mchc')
  MCV =st.number_input('enter mcv')
  di=''
  if st.button('check'):
      di=pred([Gender,Hemoglobin,MCH,MCHC,MCV])

  st.success(di)
  

if __name__=='__main__':
    main()

