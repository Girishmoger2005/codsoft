import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()