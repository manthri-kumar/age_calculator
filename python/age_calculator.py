from datetime import datetime

def calculate_age(birthdate_str):
    # Convert the string to a datetime object
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    
    # Get the current date
    today = datetime.today()
    
    # Calculate the age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return age

# Example usage
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate_str)
print(f"You are {age} years old.")