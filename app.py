import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Gym Assistant", page_icon="🏋️")

st.title("🏋️ AI Gym & Fitness Assistant")

menu = st.sidebar.selectbox(
    "Select Module",
    [
    "Home",
    "AI Gym Trainer",
    "AI Dietician",
    "Smart Gym Assistant",
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="💪 Weekly Workouts",
            value="25"
        )

    with col2:
        st.metric(
            label="🔥 Calories Burned",
            value="1200"
        )

    with col3:
        st.metric(
            label="💧 Daily Water Goal",
            value="2.5 L"
        )

    st.info(
        """
        AI Gym & Fitness Assistant helps users with workout guidance,
        diet planning, calorie tracking, habit monitoring, performance
        analysis, and fitness recommendations.
        """
    )

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

# ---------------- AI GYM TRAINER ----------------

elif menu == "AI Gym Trainer":

    st.header("🏋️ AI Gym Trainer")

    exercise = st.selectbox(
        "Select Exercise",
        ["Pushups", "Squats", "Plank"]
    )

    reps = st.slider(
        "Repetitions Completed",
        0,
        50
    )

    st.success(f"You completed {reps} reps")

    if reps >= 20:
        st.success("Excellent Performance ⭐")
    elif reps >= 10:
        st.info("Good Performance 👍")
    else:
        st.warning("Try increasing repetitions ⚠️")

    st.subheader("Workout Feedback")

    if exercise == "Pushups":
        st.write("Keep your back straight and elbows aligned.")
    elif exercise == "Squats":
        st.write("Maintain proper knee alignment.")
    else:
        st.write("Keep your core engaged during the plank.")

# ---------------- AI DIETICIAN ----------------

elif menu == "AI Dietician":

    st.header("🥗 AI Dietician")

    height = st.number_input("Height (cm)", min_value=1.0, key="diet_height")
    weight = st.number_input("Weight (kg)", min_value=1.0, key="diet_weight")

    if st.button("Calculate BMI", key="diet_bmi"):

        bmi = weight / ((height / 100) ** 2)

        st.success(f"BMI = {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Health Status: Underweight")
        elif bmi < 25:
            st.success("Health Status: Healthy Weight")
        elif bmi < 30:
            st.warning("Health Status: Overweight")
        else:
            st.error("Health Status: Obese")

    st.subheader("💧 Water Intake Calculator")

    if st.button("Calculate Water Intake"):

        water = weight * 35

        st.success(
            f"Recommended Water Intake: {water:.0f} ml ({water/1000:.1f} L)"
        )

    # Calorie Calculator
    st.subheader("🔥 Calorie Calculator")

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=20
    )

    if st.button("Calculate Calories"):

        calories = (
            10 * weight +
            6.25 * height -
            5 * age + 5
        )

        st.success(
            f"Estimated Daily Calories: {calories:.0f}"
        )
# ---------------- SMART GYM ASSISTANT ----------------

elif menu == "Smart Gym Assistant":

    st.header("📡 Smart Gym Assistant")

    heart_rate = st.slider(
        "Current Heart Rate",
        60,
        180,
        100
    )

    st.metric(
        "Heart Rate",
        f"{heart_rate} BPM"
    )

    if heart_rate < 90:
        st.success(
            "You can safely increase workout intensity."
        )

    elif heart_rate < 140:
        st.info(
            "Workout intensity is optimal."
        )

    else:
        st.warning(
            "Reduce workout intensity and take a short rest."
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

    # Weekly Habit Tracking Chart
    habit_data = pd.DataFrame({
        "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Workout":[1,1,0,1,1,0,1]
    })

    st.subheader("📈 Weekly Habit Tracking")
    st.bar_chart(habit_data.set_index("Day"))

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

st.markdown("---")
st.markdown(
    "Developed using Python, Streamlit, Pandas and AI-based fitness recommendations."
)
       
