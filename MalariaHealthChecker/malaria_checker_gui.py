# upgraded_malaria_checker_gui.py
import tkinter as tk
from tkinter import messagebox

def assess():
    # Symptoms weighted scoring
    score = (
        fever_var.get() * 2 +
        chills_var.get() * 2 +
        sweat_var.get() * 2 +
        headache_var.get() * 1 +
        nausea_var.get() * 1 +
        fatigue_var.get() * 1 +
        muscle_var.get() * 1 +
        mosquito_var.get() * 2 +
        travel_var.get() * 2
    )

    age = age_var.get()
    gender = gender_var.get()

    # Adjust score based on age (higher risk if <5 or >50)
    if age < 5 or age > 50:
        score += 1

    # Determine risk level
    if score >= 8:
        risk = "HIGH RISK"
        color = "red"
        advice = "Consult a doctor immediately."
    elif score >= 4:
        risk = "MEDIUM RISK"
        color = "orange"
        advice = "Consider getting tested."
    else:
        risk = "LOW RISK"
        color = "green"
        advice = "Malaria unlikely."

    messagebox.showinfo("Malaria Risk Assessment", f"{risk}\n{advice}")

# GUI setup
root = tk.Tk()
root.title("Upgraded Malaria Health Checker")
root.geometry("400x550")

tk.Label(root, text="Malaria Risk Checker", font=("Arial", 16, "bold")).pack(pady=10)

# Symptoms frame
symptoms_frame = tk.LabelFrame(root, text="Select your symptoms", padx=10, pady=10)
symptoms_frame.pack(padx=10, pady=10, fill="both")

fever_var = tk.IntVar()
chills_var = tk.IntVar()
sweat_var = tk.IntVar()
headache_var = tk.IntVar()
nausea_var = tk.IntVar()
fatigue_var = tk.IntVar()
muscle_var = tk.IntVar()
mosquito_var = tk.IntVar()
travel_var = tk.IntVar()
age_var = tk.IntVar()
gender_var = tk.StringVar(value="M")

tk.Checkbutton(symptoms_frame, text="Fever", variable=fever_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Chills", variable=chills_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Sweating", variable=sweat_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Headache", variable=headache_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Nausea/Vomiting", variable=nausea_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Fatigue", variable=fatigue_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Muscle Pain", variable=muscle_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Recent Mosquito Bites", variable=mosquito_var).pack(anchor="w")
tk.Checkbutton(symptoms_frame, text="Travelled to malaria-prone area", variable=travel_var).pack(anchor="w")

# Age and Gender frame
demo_frame = tk.LabelFrame(root, text="Your Details", padx=10, pady=10)
demo_frame.pack(padx=10, pady=10, fill="both")

tk.Label(demo_frame, text="Age:").pack(anchor="w")
tk.Entry(demo_frame, textvariable=age_var).pack(anchor="w")

tk.Label(demo_frame, text="Gender:").pack(anchor="w")
tk.Radiobutton(demo_frame, text="Male", variable=gender_var, value="M").pack(anchor="w")
tk.Radiobutton(demo_frame, text="Female", variable=gender_var, value="F").pack(anchor="w")

# Check button
tk.Button(root, text="Check Risk", command=assess, bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
