import streamlit as st

st.set_page_config(page_title="AI Gym Assistant")

st.title("🏋️ AI Gym & Fitness Assistant")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "AI Dietician",
        "Habit Predictor",
        "Virtual Gym Buddy",
        "Performance Score",
        "Gym Recommender"
    ]
)

if menu == "Home":

    st.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438")

    st.markdown("# 🏋️ AI Gym & Fitness Assistant")
    st.markdown("### Your Smart Personal Trainer")

    st.subheader("BMI Calculator")

    height = st.number_input("Height (cm)", min_value=1.0)
    weight = st.number_input("Weight (kg)", min_value=1.0)

    bmi = None

    if st.button("Calculate BMI"):
        bmi = weight / ((height/100)**2)
        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.write("📌 Underweight Diet Plan")
        elif bmi < 25:
            st.write("📌 Healthy Maintenance Diet")
        else:
            st.write("📌 Weight Loss Diet Plan")

    st.subheader("Performance Progress")

    import pandas as pd

    data = pd.DataFrame({
        "Week":[1,2,3,4,5],
        "Score":[60,70,75,85,90]
    })

    st.line_chart(data.set_index("Week"))
elif menu == "AI Dietician":
    st.subheader("BMI Calculator")

height = st.number_input("Height (cm)", min_value=1.0)
weight = st.number_input("Weight (kg)", min_value=1.0)

if st.button("Calculate BMI"):
    bmi = weight / ((height/100)**2)
    st.success(f"BMI = {bmi:.2f}")

st.subheader("💧 Water Intake Calculator")

if st.button("Calculate Water Intake"):
    water = weight * 35
    st.success(f"Drink {water:.0f} ml per day")

    if st.button("Generate Diet Plan"):
        st.success(f"Diet Plan Generated for {goal}")

elif menu == "Habit Predictor":
    st.subheader("Workout Recommendation")

goal = st.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "General Fitness"]
)

if goal == "Weight Loss":
    st.write("🏃 Recommended: Cardio + HIIT")
elif goal == "Muscle Gain":
    st.write("🏋️ Recommended: Strength Training")
else:
    st.write("🚴 Recommended: Mixed Workout")

elif menu == "Virtual Gym Buddy":
    import random

quotes = [
    "Push yourself because no one else will.",
    "Small progress is still progress.",
    "Stay consistent and trust the process.",
    "Every workout counts."
]

if st.button("Get Motivation"):
    st.success(random.choice(quotes))

question = st.text_input("Ask Fitness Assistant")

if question:
    st.write("🤖 AI Assistant:")
    st.write("Maintain a balanced diet and exercise regularly.")

elif menu == "Performance Score":

    reps = st.slider("Reps",0,50)
    accuracy = st.slider("Accuracy",0,100)

    score = reps*0.4 + accuracy*0.6

    st.metric("Performance Score", round(score,2))

    import pandas as pd

    data = pd.DataFrame({
        "Week":[1,2,3,4,5],
        "Score":[60,70,75,85,90]
    })

    st.line_chart(data.set_index("Week"))
elif menu == "Gym Recommender":
    city = st.text_input("Enter City")

    if city:
        st.write("Recommended Gyms:")
        st.write("• Gold Gym")
        st.write("• Cult Fit")
        st.write("• Anytime Fitness")
