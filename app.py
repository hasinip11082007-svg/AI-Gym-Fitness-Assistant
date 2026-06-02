import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Gym Assistant", page_icon="🏋️")

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

# ---------------- HOME ----------------

if menu == "Home":

    st.image("https://images.unsplash.com/photo-1517836357463-d25dfeac3438")

    st.markdown("# 🏋️ AI Gym & Fitness Assistant")
    st.markdown("### Your Smart Personal Trainer")

    st.subheader("BMI Calculator")

    height = st.number_input("Height (cm)", min_value=1.0)
    weight = st.number_input("Weight (kg)", min_value=1.0)

    if st.button("Calculate BMI"):
        bmi = weight / ((height / 100) ** 2)

        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.write("📌 Underweight Diet Plan")
        elif bmi < 25:
            st.write("📌 Healthy Maintenance Diet")
        else:
            st.write("📌 Weight Loss Diet Plan")

    st.subheader("Performance Progress")

    data = pd.DataFrame({
        "Week": [1, 2, 3, 4, 5],
        "Score": [60, 70, 75, 85, 90]
    })

    st.line_chart(data.set_index("Week"))

# ---------------- AI DIETICIAN ----------------

elif menu == "AI Dietician":

    st.header("🥗 AI Dietician")

    height = st.number_input("Height (cm)", min_value=1.0, key="diet_height")
    weight = st.number_input("Weight (kg)", min_value=1.0, key="diet_weight")

    if st.button("Calculate BMI", key="diet_bmi"):

        bmi = weight / ((height / 100) ** 2)

        st.success(f"BMI = {bmi:.2f}")

        if bmi < 18.5:
            st.write("🥛 Diet: Milk, Eggs, Nuts, Bananas")
        elif bmi < 25:
            st.write("🥗 Diet: Balanced Diet Plan")
        else:
            st.write("🥦 Diet: Low-Calorie Diet Plan")

    st.subheader("💧 Water Intake Calculator")

    if st.button("Calculate Water Intake"):

        water = weight * 35

        st.success(
            f"Recommended Water Intake: {water:.0f} ml ({water/1000:.1f} L)"
        )

# ---------------- HABIT PREDICTOR ----------------

elif menu == "Habit Predictor":

    st.header("📅 Habit Predictor")

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "General Fitness"
        ]
    )

    if goal == "Weight Loss":
        st.write("🏃 Recommended: Cardio + HIIT")
    elif goal == "Muscle Gain":
        st.write("🏋️ Recommended: Strength Training")
    else:
        st.write("🚴 Recommended: Mixed Workout Plan")

# ---------------- VIRTUAL GYM BUDDY ----------------

elif menu == "Virtual Gym Buddy":

    st.header("🤖 Virtual Gym Buddy")

    quotes = [
        "Push yourself because no one else will.",
        "Small progress is still progress.",
        "Stay consistent and trust the process.",
        "Every workout counts.",
        "Success starts with self-discipline."
    ]

    if st.button("Get Motivation"):
        st.success(random.choice(quotes))

   
   question = st.text_input("Ask Fitness Assistant")

if question:

    q = question.lower()

    st.write("🤖 AI Assistant:")

    if "weight loss" in q:
        st.write("Focus on a calorie deficit, cardio workouts, and high-protein meals.")

    elif "muscle" in q or "gain" in q:
        st.write("Increase protein intake and follow a strength-training routine.")

    elif "protein" in q:
        st.write("Good protein sources include eggs, chicken, fish, paneer, tofu, and lentils.")

    elif "water" in q:
        st.write("Aim for 2-4 liters of water daily depending on your activity level.")

    elif "workout" in q:
        st.write("A balanced workout includes cardio, strength training, and flexibility exercises.")

    elif "diet" in q:
        st.write("A healthy diet includes proteins, carbohydrates, healthy fats, fruits, and vegetables.")

    else:
        st.write("I can help with fitness, diet, workouts, hydration, and muscle gain questions.")
# ---------------- PERFORMANCE SCORE ----------------

elif menu == "Performance Score":

    st.header("📊 Performance Score")

    reps = st.slider("Reps", 0, 50)
    accuracy = st.slider("Accuracy (%)", 0, 100)

    score = reps * 0.4 + accuracy * 0.6

    st.metric("Performance Score", round(score, 2))

    data = pd.DataFrame({
        "Week": [1, 2, 3, 4, 5],
        "Score": [60, 70, 75, 85, 90]
    })

    st.line_chart(data.set_index("Week"))

# ---------------- GYM RECOMMENDER ----------------

elif menu == "Gym Recommender":

    st.header("🏢 Gym Recommender")

    city = st.text_input("Enter Your City")

    if city:

        st.write("🏋️ Recommended Gyms:")

        st.write("• Gold Gym")
        st.write("• Cult Fit")
        st.write("• Anytime Fitness")
        st.write("• Fitness One")
       
