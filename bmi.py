import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            label_result.config(text=f"Your BMI is {bmi:.2f} (Underweight)", fg="red")
        elif 18.5 <= bmi <= 24.9:
            label_result.config(text=f"Your BMI is {bmi:.2f} (Normal)", fg="green")
        else:
            label_result.config(text=f"Your BMI is {bmi:.2f} (Overweight)", fg="red")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.config(bg="#f0f0f0")  

label_title = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
label_title.pack(pady=10)

label_weight = tk.Label(root, text="Enter your weight (kg):", font=("Arial", 12), bg="#f0f0f0", fg="#333333")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root, font=("Arial", 12), width=10)
entry_weight.pack(pady=5)

label_height = tk.Label(root, text="Enter your height (cm):", font=("Arial", 12), bg="#f0f0f0", fg="#333333")
label_height.pack(pady=5)
entry_height = tk.Entry(root, font=("Arial", 12), width=10)
entry_height.pack(pady=5)

btn_calculate = tk.Button(root, text="Calculate BMI", font=("Arial", 12), bg="#4CAF50", fg="white",
                          command=calculate_bmi)
btn_calculate.pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
label_result.pack(pady=10)

root.mainloop()
