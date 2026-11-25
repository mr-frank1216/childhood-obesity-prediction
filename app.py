
import streamlit as st
import joblib
import pandas as pd

# Load the trained machine learning pipeline
model = joblib.load("obesity_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Childhood Obesity Prediction",
    page_icon="📊",
    layout="wide"
)

# Application heading
st.title("Childhood Obesity Prediction System")

st.write("""
An educational machine learning application that explores
childhood obesity risk patterns using NHANES 2021–2023 data.
""")

st.warning(
    "This application is for educational and research purposes. "
    "It is not a medical diagnosis or a substitute for professional assessment."
)

st.divider()


st.header("Child Demographics")

# Child's age
age = st.number_input(
    "Child's age (years)",
    min_value=3,
    max_value=19,
    value=10,
    step=1
)

# Sex
sex_label = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

sex = 1 if sex_label == "Male" else 2

# Race and Hispanic origin
race_options = {
    "Mexican American": 1,
    "Other Hispanic": 2,
    "Non-Hispanic White": 3,
    "Non-Hispanic Black": 4,
    "Non-Hispanic Asian": 6,
    "Other race, including multiracial": 7
}

race_label = st.selectbox(
    "Race and Hispanic origin",
    list(race_options.keys())
)

race = race_options[race_label]

st.success("Demographic information captured.")


st.header("Household and Food Security")

st.write("Please provide information about the child's household.")

# Household size
household_size = st.selectbox(
    "Total number of people in the household",
    [1, 2, 3, 4, 5, 6, 7],
    help="7 represents 7 or more people."
)

# Household reference person's age group
reference_age_options = {
    "Under 20 years": 1,
    "20–39 years": 2,
    "40–59 years": 3,
    "60 years or older": 4
}

reference_age_label = st.selectbox(
    "Age group of household reference person",
    list(reference_age_options.keys())
)

reference_age = reference_age_options[reference_age_label]

# Household reference person's education
education_options = {
    "Less than high school": 1,
    "High school, GED or some college": 2,
    "College graduate or above": 3
}

education_label = st.selectbox(
    "Education level of household reference person",
    list(education_options.keys())
)

reference_education = education_options[education_label]

# Family income-to-poverty ratio
income_ratio = st.slider(
    "Family income-to-poverty ratio",
    min_value=0.0,
    max_value=5.0,
    value=2.0,
    step=0.1,
    help="Values of 5.0 represent 5.0 or more."
)

# Adult food security
food_security_options = {
    "Full food security": 1,
    "Marginal food security": 2,
    "Low food security": 3,
    "Very low food security": 4,
    "Not recorded": float("nan")
}

food_security_label = st.selectbox(
    "Adult food security category",
    list(food_security_options.keys())
)

food_security = food_security_options[food_security_label]

# Emergency food assistance
emergency_options = {
    "Yes": 1,
    "No": 2,
    "Refused": 7,
    "Don't know": 9,
    "Not recorded": float("nan")
}

emergency_label = st.selectbox(
    "Did the household receive emergency food in the last 12 months?",
    list(emergency_options.keys())
)

emergency_food = emergency_options[emergency_label]

# SNAP benefits
snap_options = {
    "Yes": 1,
    "No": 2,
    "Refused": 7,
    "Don't know": 9,
    "Not recorded / not applicable": float("nan")
}

snap_ever_label = st.selectbox(
    "Has anyone in the household ever received SNAP benefits?",
    list(snap_options.keys())
)

snap_ever = snap_options[snap_ever_label]


# SNAP received in the last 12 months
snap_recent_options = snap_options.copy()
snap_recent_options["Refused"] = float("nan")

snap_12m_label = st.selectbox(
    "Did anyone receive SNAP benefits in the last 12 months?",
    list(snap_recent_options.keys())
)

snap_12m = snap_recent_options[snap_12m_label]


# Currently receiving SNAP benefits
snap_current_label = st.selectbox(
    "Is anyone currently receiving SNAP benefits?",
    list(snap_recent_options.keys())
)

snap_current = snap_recent_options[snap_current_label]
st.success("Household information captured.")


st.header("School Meals and Nutrition")

st.write("Tell us about the child's school meal arrangements.")

yes_no_options = {
    "Yes": 1,
    "No": 2,
    "Refused": 7,
    "Don't know": 9,
    "Not recorded": float("nan")
}

# School attendance
school_attendance_options = yes_no_options.copy()
school_attendance_options["Refused"] = float("nan")

school_label = st.selectbox(
    "Does the child attend kindergarten, primary or secondary school?",
    list(school_attendance_options.keys())
)

school_attendance = school_attendance_options[school_label]


# School lunch availability
lunch_label = st.selectbox(
    "Does the child's school provide school lunches?",
    list(yes_no_options.keys())
)

school_lunch = yes_no_options[lunch_label]

# Lunch payment category
meal_price_options = {
    "Free": 1,
    "Reduced price": 2,
    "Full price": 3,
    "Refused": 7,
    "Don't know": 9,
    "Not recorded / not applicable": float("nan")
}


# Adjust payment options for the model
meal_price_model_options = meal_price_options.copy()
meal_price_model_options["Refused"] = float("nan")

# Lunch payment category
lunch_price_label = st.selectbox(
    "How much does the child pay for school lunch?",
    list(meal_price_model_options.keys())
)

lunch_price = meal_price_model_options[lunch_price_label]


# School breakfast availability
breakfast_label = st.selectbox(
    "Does the child's school provide complete breakfast?",
    list(yes_no_options.keys())
)

school_breakfast = yes_no_options[breakfast_label]


# Breakfast payment category
breakfast_price_label = st.selectbox(
    "How much does the child pay for school breakfast?",
    list(meal_price_model_options.keys())
)

breakfast_price = meal_price_model_options[breakfast_price_label]


# Summer programme meal assistance
summer_options = {
    "Yes": 1,
    "No": 2,
    "Did not attend a summer programme": 3,
    "Refused": 7,
    "Don't know": 9,
    "Not recorded": float("nan")
}
summer_options["Refused"] = float("nan")

summer_label = st.selectbox(
    "Does the child receive free or reduced-price meals at a summer programme?",
    list(summer_options.keys())
)

summer_meals = summer_options[summer_label]

st.success("School meal information captured.")


st.header("Physical Activity and Screen Time")

st.write("Tell us about the child's physical activity and screen habits.")


# Physical activity and screen time
# These NHANES youth questions apply to ages 2–17

if age <= 17:

    # PAQ706: Days physically active
    activity_options = {
        "0 days": 0,
        "1 day": 1,
        "2 days": 2,
        "3 days": 3,
        "4 days": 4,
        "5 days": 5,
        "6 days": 6,
        "7 days": 7,
        "Refused": 77,
        "Don't know": 99,
        "Not recorded": float("nan")
    }

    activity_label = st.selectbox(
        "During the past 7 days, on how many days was the child physically active for at least 60 minutes?",
        list(activity_options.keys())
    )

    physical_activity = activity_options[activity_label]

    # PAQ711: Screen time
    screen_options = {
        "0 hours": 0,
        "1 hour": 1,
        "2 hours": 2,
        "3 hours": 3,
        "4 hours": 4,
        "5 hours": 5,
        "6 hours": 6,
        "7 hours": 7,
        "8 hours": 8,
        "9 or more hours": 9,
        "Refused": 77,
        "Don't know": 99,
        "Not recorded": float("nan")
    }

    screen_label = st.selectbox(
        "On a typical school day, how many hours does the child spend using screens?",
        list(screen_options.keys())
    )

    screen_time = screen_options[screen_label]

    st.success("Physical activity and screen time information captured.")

else:
    physical_activity = float("nan")
    screen_time = float("nan")

    st.info(
        "Physical activity and screen-time questions are not applicable "
        "to participants aged 18–19 in this NHANES youth questionnaire."
    )

# Arrange all 20 inputs in the exact training order

feature_names = [
    "RIDAGEYR",
    "RIAGENDR",
    "RIDRETH3",
    "DMDHHSIZ",
    "DMDHRAGZ",
    "DMDHREDZ",
    "INDFMPIR",
    "FSDAD",
    "FSD151",
    "FSQ165",
    "FSQ012",
    "FSD230",
    "DBQ360",
    "DBQ370",
    "DBQ390",
    "DBQ400",
    "DBQ421",
    "DBQ424",
    "PAQ706",
    "PAQ711"
]

input_data = pd.DataFrame([[
    age,
    sex,
    race,
    household_size,
    reference_age,
    reference_education,
    income_ratio,
    food_security,
    emergency_food,
    snap_ever,
    snap_12m,
    snap_current,
    school_attendance,
    school_lunch,
    lunch_price,
    school_breakfast,
    breakfast_price,
    summer_meals,
    physical_activity,
    screen_time
]], columns=feature_names)

st.divider()
st.subheader("Input Data Verification")

st.write("These are the 20 values prepared for the machine learning model:")

st.dataframe(input_data, use_container_width=True)

# Check that the columns match the saved model
if hasattr(model, "feature_names_in_"):
    if list(input_data.columns) == list(model.feature_names_in_):
        st.success("All 20 feature names and their order match the trained model!")
    else:
        st.error("The input columns do not match the trained model.")
else:
    st.info("The saved model does not expose feature names for comparison.")



st.divider()

st.subheader("Obesity Prediction")

if st.button("Predict Obesity Status", type="primary"):

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    not_obese_probability = probabilities[0] * 100
    obese_probability = probabilities[1] * 100

    if prediction == 1:
        st.warning("The model predicts: Obese")
    else:
        st.success("The model predicts: Not Obese")

    st.write("### Model Prediction Scores")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Not Obese", f"{not_obese_probability:.2f}%")

    with col2:
        st.metric("Obese", f"{obese_probability:.2f}%")

    if prediction == 1:
        st.info(
            "The model identifies this input as belonging to the Obese category. "
            "This is a research prediction based on the information provided, "
            "not a clinical assessment."
        )
    else:
        st.info(
            "The model identifies this input as belonging to the Not Obese category. "
            "This is a research prediction based on the information provided, "
            "not a clinical assessment."
        )

    st.caption(
        "The displayed percentages are model-estimated probabilities. "
        "They are not a medical diagnosis or a guarantee of a child's health status."
    )
