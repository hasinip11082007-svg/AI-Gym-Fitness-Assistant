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
    weight = st.number_input("Weight (kg)")
    goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain"])

    if st.button("Generate Diet Plan"):
        st.success(f"Diet Plan Generated for {goal}")

elif menu == "Habit Predictor":
    days = st.slider("Days Missed",0,10)

    if days > 3:
        st.warning("Workout consistency is decreasing.")
    else:
        st.success("Excellent consistency!")

elif menu == "Virtual Gym Buddy":
    mood = st.text_input("How are you feeling today?")

    if mood:
        st.write("Keep going! Every workout matters.")

elif menu == "Performance Score":
    reps = st.slider("Reps",0,50)
    accuracy = st.slider("Accuracy",0,100)

    score = reps*0.4 + accuracy*0.6

    st.metric("Performance Score", round(score,2))

elif menu == "Gym Recommender":
    city = st.text_input("Enter City")

    if city:
        st.write("Recommended Gyms:")
        st.write("• Gold Gym")
        st.write("• Cult Fit")
        st.write("• Anytime Fitness")
