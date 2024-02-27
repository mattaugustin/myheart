import keras
import pickle
import numpy as np
from PIL import Image
from keras.models import load_model
import streamlit as st

# dir(st)


## Load the saved model
# model = load_model("c:\\ndsha_maps\\learning\\python\\DevAcademy\\Projects\\Week08_Streamlit\\heart_disease_model.h5")
model = load_model("heart_disease_model.h5")


## Create a function for prediction
# with open("hrt_model.pkl", "rb") as file:
#     model_lr = pickle.load

### Create a function for prediction
# def heart_prediction(input):
#     input_array = np.asarray(input)
#     input_Reshape = input.array.reshape(1,-1)
#     prediction = model.predict(input_reshape)
#     print(prediction)
    
#     if (prediction[0] == 0):
#         return "you are not likely to die from heart failure given your health condition"
#     else:
#         return "you are likely to die form heart failure given your health condition"
    
    
    
## Set up the streamlit
def main():
    
    st.set_page_config(page_title = "heart failure predictor" , layout = "wide")
    
    # add image
    image = Image.open("heart.png")
    st.image(image = image , use_column_width= False )
    
    # add title to your application
    st.title("heart failure Predictor Using ANN")
    st.write("Enter your personal data to get heart failure risk evaluation")
    
    ## Take input from users
    age = st.number_input('Age of the patient:',min_value=0, step=1)
    anaemia = st.number_input('Anaemia | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    creatinine_phosphokinase = st.number_input('Level of the CPK enzyme in the blood (mcg/L):',min_value=0, step=1)
    diabetes = st.number_input('Diabetes | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    ejection_fraction = st.number_input('Percentage of blood leaving the heart at each contraction:',min_value=0, step=1)
    high_blood_pressure = st.number_input('Hypertension | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    platelets = st.number_input('Platelet count of blood (kiloplatelets/mL):',min_value=0, step=1)
    serum_creatinine = st.number_input('Level of serum creatinine in the blood (mg/dL):',min_value=0.00, step=0.01)
    serum_sodium = st.number_input('Level of serum sodium in the blood (mEq/L):',min_value=0, step=1)
    sex = st.number_input('Sex | male or female | male = 1 and female = 0:',min_value=0, step=1)
    smoking = st.number_input('Habit of smoking | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    time = st.number_input('Follow-up period (days):',min_value=0, step=1)
    
    
    # prediction
    predict = ""
    
    
    # button for prediction
    if st.button("predict"):
        predict = heart_prediction([age, anaemia,creatinine_phosphokinase, diabetes, ejection_fraction , high_blood_pressure ,
                                   platelets, serum_creatinine , serum_sodium , sex ,smoking , time])
    
    st.success(predict)
    
    

def heart_prediction(input):
    
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
    prediction = model.predict(input_reshape)
    print(prediction)
    
    if (prediction[0] == 0):
        return "you are not likely to die from heart failure given your health condition"
    else:
        return "you are likely to die form heart failure given your health condition"
    

## run our script
main()

# if __name__ == "__main__":
#     main()
    
    
# streamlit run heart_disease.py
# python -m streamlit run heart_disease.py
