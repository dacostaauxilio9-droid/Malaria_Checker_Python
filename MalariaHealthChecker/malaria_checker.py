# malaria_checker.py
def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (yes/no): ").strip().lower()
        if ans in ["yes", "no"]:
            return ans
        print("Please answer with yes or no.")

def malaria_risk_assessment():
    print("\n=== Malaria Health Checker ===\n")

    fever = get_yes_no("Do you have a fever?")
    chills = get_yes_no("Do you experience chills/shivering?")
    sweating = get_yes_no("Are you sweating excessively?")
    headache = get_yes_no("Do you have a strong headache?")
    nausea = get_yes_no("Do you feel nausea or vomiting?")
    travelled = get_yes_no("Recently travelled to a malaria-prone area?")

    symptoms = sum([
        fever == "yes",
        chills == "yes",
        sweating == "yes",
        headache == "yes",
        nausea == "yes"
    ])

    if symptoms >= 4 and travelled == "yes":
        result = "HIGH RISK of malaria. Please consult a doctor immediately."
    elif symptoms >= 2:
        result = "MEDIUM RISK. Monitor symptoms and consider a malaria test."
    else:
        result = "LOW RISK. Symptoms do not strongly indicate malaria."

    print("\n--- Assessment Result ---")
    print(result)
    print("-------------------------\n")

if __name__ == "__main__":
    malaria_risk_assessment()
