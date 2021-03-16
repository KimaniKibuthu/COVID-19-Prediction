import joblib
import streamlit as st

joblib_in = open("rf_classifier.pkl", "rb")
classifier = joblib.load(joblib_in)


def welcome():
    return "Welcome All"


def predict_covid_authentication(cough, fever, sore_throat, shortness_of_breath, head_ache, test_indication):
    """Covid prediction
    This is using docstrings for specifications.
    ---
    parameters:
      - name: cough
        in: query
        type: number
        required: true
      - name: fever
        in: query
        type: number
        required: true
      - name: sore_throat
        in: query
        type: number
        required: true
      - name: shortness_of_breath
        in: query
        type: number
        required: true
      - name: head_ache
        in: query
        type: number
        required: true
      - name: test_indication
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction = classifier.predict([[cough, fever, sore_throat, shortness_of_breath, head_ache, test_indication]])
    if prediction == 1:
        output = 'positive'
    else:
        output = 'negative'
    return output


def main():
    st.title("Covid Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Covid Prediction Web App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    cough = st.selectbox('Are you experiencing a cough? (0: No, 1: Yes)', (0, 1))
    sore_throat = st.selectbox('Are you experiencing a sore throat? (0: No, 1: Yes)', (0, 1))
    fever = st.selectbox('Any fever? (0: No, 1: Yes)', (0, 1))
    shortness_of_breath = st.selectbox('Any shortness of breath on normal day activities? (0: No, 1: Yes)', (0, 1))
    head_ache = st.selectbox('Any headaches? (0: No, 1: Yes)', (0, 1))
    test_indication = st.selectbox(
        'Travel and interaction history(0: Abroad, 1: None that I know, 2: Contact with confirmed covid patient)',
        (0, 1, 2))
    result = ""
    if st.button("Predict"):
        result = predict_covid_authentication(cough, fever, sore_throat, shortness_of_breath, head_ache, test_indication)
        st.success('You are likely to be Covid {}.'.format(result))

    if st.button("Disclaimer"):
        disclaimer = 'This is an estimate as to whether you have covid or not. A covid test will be more accurate.'
        st.success(disclaimer)


if __name__ == '__main__':
    main()
