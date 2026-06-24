from my_groq import generate_response

def reinforcement_learning_activity():
    print("\n--- REINFORCEMENT LEARNING ACTIVITY--\n")
    prompt = input("Enter a prompt for the AI model(e.g.,'Describe artificial Intelligence'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    initial_response = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Initial AI response: {initial_response}")
    try:
        rating = int(input("Rate the response from 1(bad) to 5(good): ").strip())
        if rating < 1 or rating > 5:
            print("Invalid rating.Using 3.")
            rating = 3
    except ValueError:
        print("Invalid rating.Using 3.")
        rating = 3

    feedback=input("Provide feedback for improvement:").strip()
    improved_response =f"{initial_response} Improved with your feedback: {feedback}"
    print(f"\nImproved AI Response : {improved_response}")
    print("\nReflection :")
    print("1. How did the model's response improve with feedback")
    print("2.How does reinforcement learning help AI to improve its performance over time?")


def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category=input("Enter a category (e.g. , Technology,Environment,health: )").strip()
    item = input(f"Enter a specific {category} topic (eg, 'AI and its way forward' for technology )").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    business_prompt = f"You are a business leader. Explain {item} in a practical and focused manner"
    young_student = f"YOu are a teacher explaining to  child . Explain {item} in a creative way a young child can understand"


    teacher_response = generate_response(teacher_prompt, temperature=0.5, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)
    business_prompt = generate_response(business_prompt, temperature=0.2,max_tokens=500)
    young_student=generate_response(young_student, temperature=0.9, max_tokens=2048)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")
    print(f"\n ---Business leader Perspective---\n{business_prompt}")
    print(f"\n ---Young childrens teacher Perspective\n{young_student}")

    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice = input("> ").strip()

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()

