import re
def assess_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    strength_score = sum(strength_criteria.values())
    
    if strength_score == 5:
        strength = 'Very Strong'
    elif strength_score == 4:
        strength = 'Strong'
    elif strength_score == 3:
        strength = 'Medium'
    elif strength_score == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'
    feedback = []
    if not strength_criteria['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not strength_criteria['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not strength_criteria['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not strength_criteria['digits']:
        feedback.append("Password should include at least one digit.")
    if not strength_criteria['special']:
        feedback.append("Password should include at least one special character.")
    return strength, feedback
def main():
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}")
        for suggestion in feedback:
            print(f" - {suggestion}")
if __name__ == "__main__":
    main()
