users = {}

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def register():
    print("\n📒 Registration")
    username = input("Create a username: ").strip()
    if username in users:
        print("⚠️ Username already exists. Try again.")
        return None
    password = input("Create a password: ").strip()
    users[username] = password
    print("✅ Registration Successful! Please log in.")

def login():
    attempts = 3
    while attempts > 0:
        print("\n🔐 Log In")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if users.get(username) == password:
            print("🔓 Login Successful!")
            return True
        else:
            attempts -= 1
            print(f"❌ Invalid credentials. Attempts left: {attempts}")
            if attempts == 0:
                retry = input("No attempts left. Do you want to register instead? (Y/N): ").strip().upper()
                if retry == "Y":
                    return None
                else:
                    attempts = 3  # Reset attempts
    return False

def input_data():
    age = int(input_number("Enter your age (years): "))
    while True:
        gender = input("Enter your gender (M/F): ").strip().upper()
        if gender in ["M", "F"]:
            break
        print("⚠️ Please enter 'M' or 'F'.")

    weight = input_number("Enter your weight (kg): ")
    height_cm = input_number("Enter your height (cm): ")
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    print(f"\n📊 Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("⚠️ You are underweight. Consider a nutrient-rich meal plan and consult a healthcare provider.")
    elif 18.5 <= bmi <= 24.9:
        print("✅ You have a healthy weight. Maintain your wellness routine!")
    elif 25 <= bmi <= 29.9:
        print("⚠️ You are overweight. Consider a fitness and balanced diet plan.")
    else:
        print("""⚠️ You are obese. It’s important to seek guidance from a health professional.""")
    print(f"\n📌 Age: {age}, Gender: {gender}")
    return None

def weight_loss_plan():
    print("\n⚖️ Weight Loss Plan")
    input_data()
    print("🍎 Eat more veggies and lean protein.")
    print("🔥 Track your progress weekly!")

def stay_healthy_plan():
    print("\n🛡️ Stay Healthy Plan")
    input_data()
    print("🥗 Food Recommendations:")
    print("- Leafy greens, fruits, lean proteins")
    print("- Whole grains like quinoa and oats")
    print("- Healthy fats like nuts and seeds")
    print("⚕️ Daily activity and stress management")

def gain_muscle_plan():
    print("\n💪 Gain Muscle Plan")
    input_data()
    print("- High protein intake")
    print("- Resistance training 4x/week")
    print("- Monitor progress with photos and metrics")

def mental_wellness_plan():
    print("\n🧘 Mental Wellness Plan")
    input_data()
    print("- Practice mindfulness and gratitude")
    print("- Take breaks and prioritize sleep")
    print("- Seek support when needed")

def energy_boost_plan():
    print("\n⚡ Energy Boost Plan")
    input_data()
    print("- Eat complex carbs and hydrate")
    print("- Take short walks during the day")
    print("- Avoid heavy meals before tasks")

def heart_health_plan():
    print("\n❤️ Heart Health Plan")
    input_data()
    print("- Limit salt and processed foods")
    print("- Moderate cardio exercises")
    print("- Get regular blood pressure checks")

def core_strength_plan():
    print("\n🏋️ Core Strength Plan")
    input_data()
    print("- Core-focused workouts 3x/week")
    print("- Planks, leg raises, and crunches")
    print("- Maintain posture and flexibility")

def sleep_quality_plan():
    print("\n🌙 Sleep Quality Plan")
    input_data()
    print("- Maintain a regular sleep schedule")
    print("- Avoid screens 1 hour before bed")
    print("- Try calming teas or meditation")

def run_app():
    print("✨ Welcome to HealthTrack: Your Wellness Companion!\n")
    while True:
        print("Do you have an account?")
        print("1. Yes, Log In")
        print("2. No, Register")
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            result = login()
            if result:
                break
            elif result is None:
                register()
        elif choice == "2":
            register()
        else:
            print("⚠️ Invalid option. Try again.")

    print("\n🧠 Health Goals Options:")
    print("1. Weight Loss")
    print("2. Stay Healthy")
    print("3. Gain Muscle")
    print("4. Enhance Mental Wellness")
    print("5. Increase Energy Levels")
    print("6. Improve Heart Health")
    print("7. Build Core Strength")
    print("8. Improve Sleep Quality")

    goal = input("Enter your goal (number): ").strip()
    if goal == "1":
        weight_loss_plan()
    elif goal == "2":
        stay_healthy_plan()
    elif goal == "3":
        gain_muscle_plan()
    elif goal == "4":
        mental_wellness_plan()
    elif goal == "5":
        energy_boost_plan()
    elif goal == "6":
        heart_health_plan()
    elif goal == "7":
        core_strength_plan()
    elif goal == "8":
        sleep_quality_plan()
    else:
        print("⚠️ Invalid selection.")

run_app()