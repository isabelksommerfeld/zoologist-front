import streamlit as st
import requests

st.title("Zoologist - Penguin Species Predictor 🐧")

# Verwendet st.secrets für den API-Link
api_url = st.secrets["API_URL"]

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.

1. Let's ask for:
- island (the location where the penguin lives: Biscoe, Dream or Torgersen)
- bill length (in mm)
- bill depth (in mm)
- flipper length (in mm)
- body mass (in g)
- sex ("Male" or "Female")
"""

# 1. Eingabefelder definieren
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
bill_length = st.number_input("Bill Length (mm)", value=40.0)
bill_depth = st.number_input("Bill Depth (mm)", value=17.0)
flipper_length = st.number_input("Flipper Length (mm)", value=200.0)
body_mass = st.number_input("Body Mass (g)", value=4000.0)
sex = st.selectbox("Sex", ["Male", "Female"])

# 2. Button & API-Anfrage
if st.button("Predict"):
    url = "http://127.0.0.1:8080/predict"

    params = {
        "island": island,
        "bill_length_mm": bill_length,
        "bill_depth_mm": bill_depth,
        "flipper_length_mm": flipper_length,
        "body_mass_g": body_mass,
        "sex": sex,
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            prediction = response.json()
            # Zeigt die vorhergesagte Pinguin-Art an
            st.success(
                f"Predicted species: {prediction.get('species', prediction)}"
            )
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
