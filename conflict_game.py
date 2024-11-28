import time

# Initialize points
points = 0

# Welcome message
def welcome():
    print("\nWelcome to the Conflict Resolution Simulator!")
    print("Your goal is to navigate through scenarios by making thoughtful decisions.")
    print("Each decision impacts your score and the relationships you build.\n")
    time.sleep(2)

# Scenario: Couples Conflict
def couples_conflict():
    global points
    print("\nScenario: Weekend Plans\n")
    time.sleep(1)
    print("You and your partner are discussing weekend plans.")
    print("You want to go hiking, while your partner prefers a relaxing movie night.")
    print("\nOptions:")
    print("1. Convince your partner to go hiking.")
    print("2. Suggest a compromise: a short hike in the morning, movie at night.")
    print("3. Let your partner decide this time and promise to plan the next weekend together.")
    print("4. Ignore the conversation and hope it resolves itself.\n")

    # Get user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Decision outcomes
    if choice == "1":
        print("\nOutcome: Your partner agrees reluctantly but doesn't enjoy the hike.")
        print("Feedback: While assertiveness is good, ignoring their preference can harm harmony.")
        points += 5  # Low points for one-sided decision
    elif choice == "2":
        print("\nOutcome: Both of you enjoy the weekend with balance and mutual effort.")
        print("Feedback: Great job! Compromise is key to resolving conflicts effectively.")
        points += 20  # High points for collaboration
    elif choice == "3":
        print("\nOutcome: Your partner appreciates your consideration.")
        print("Feedback: Empathy is a strength! However, ensure mutual decisions in the future.")
        points += 15  # Medium points for empathy
    elif choice == "4":
        print("\nOutcome: The conflict remains unresolved, causing tension.")
        print("Feedback: Avoidance rarely leads to resolution. Try engaging in open communication.")
        points -= 10  # Negative points for avoidance
    else:
        print("\nInvalid choice. Please try again.")
        couples_conflict()  # Recur for invalid input
    time.sleep(2)

# Scoring and Feedback
def final_score():
    global points
    print("\n--- Scenario Complete ---")
    print(f"Your final score: {points}")
    if points >= 20:
        print("Excellent! You're a conflict resolution pro!")
    elif 10 <= points < 20:
        print("Good job! You're on the right track to becoming a better mediator.")
    else:
        print("Keep practicing! Conflict resolution is a skill you can improve.\n")
    print("Thank you for playing!\n")
    time.sleep(2)

# Run the game
welcome()
couples_conflict()
final_score()

