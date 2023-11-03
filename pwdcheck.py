import re
import tkinter as tk

def length(password, minimum_length=8):
    return len(password) >= minimum_length

def character_type(password):

    # Check for character type
    lowercase = re.compile(r'[a-z]')
    uppercase = re.compile(r'[A-Z]')
    digit = re.compile(r'\d')
    special_char = re.compile(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\]')

    # check if the password contain each character type
    check_lowercase = bool(lowercase.search(password))
    check_uppercase = bool(uppercase.search(password))
    check_digit = bool(digit.search(password))
    check_special_char = bool(special_char.search(password))

    # Determine with the password contain all the character type
    return check_lowercase and check_uppercase and check_digit and check_special_char

def check_password_strength(password):
    if length(password) and character_type(password):
        return "Strong"
    
    elif length(password) or character_type(password):
        return "Good"
    
    elif password.isdigit() or password.isalpha() or not length(password):
        return "Weak"

def check_password():
    user_password = password_entry.get()
    strength = check_password_strength(user_password)
    result_label.config(text=f"Password Strength: {strength}")

# Create the main window
window = tk.Tk()
window.title("Password Strength Testing Tool")
window.configure(bg="lemonchiffon")

# Create and configure GUI elements
password_label = tk.Label(window, text="Enter your password:", bg="lemonchiffon")
password_label.pack(padx=100, pady=10)
password_entry = tk.Entry(window)
password_entry.pack(padx=10, pady=10)
check_button = tk.Button(window, text="Check Password Strength", command=check_password)
check_button.pack(padx=10, pady=10)
result_label = tk.Label(window, justify="left", bg="lemonchiffon", text=
                        "1. More than 8 characters\n"
                        "2. At least one capital letter\n"
                        "3. At least one number\n"
                        "4. At least one special character")
result_label.pack(padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
