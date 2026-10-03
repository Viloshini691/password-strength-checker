import re
import math


def calculate_entropy(password):
    character_pool = 0

    if re.search(r"[a-z]", password):
        character_pool += 26

    if re.search(r"[A-Z]", password):
        character_pool += 26

    if re.search(r"[0-9]", password):
        character_pool += 10

    if re.search(r"[^A-Za-z0-9]", password):
        character_pool += 32

    if character_pool == 0:
        return 0

    entropy = len(password) * math.log2(character_pool)

    return round(entropy, 2)


def check_password_strength(password):
    score = 0
    recommendations = []

    print("\n" + "=" * 50)
    print("        PASSWORD SECURITY ANALYSIS")
    print("=" * 50)

    if len(password) >= 12:
        print("Length (12+ characters):       PASS")
        score += 1
    else:
        print("Length (12+ characters):       FAIL")
        recommendations.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        print("Uppercase Letter:              PASS")
        score += 1
    else:
        print("Uppercase Letter:              FAIL")
        recommendations.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        print("Lowercase Letter:              PASS")
        score += 1
    else:
        print("Lowercase Letter:              FAIL")
        recommendations.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        print("Number:                        PASS")
        score += 1
    else:
        print("Number:                        FAIL")
        recommendations.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        print("Special Character:             PASS")
        score += 1
    else:
        print("Special Character:             FAIL")
        recommendations.append("Add at least one special character.")

    entropy = calculate_entropy(password)

    print("-" * 50)
    print(f"Security Score: {score}/5")
    print(f"Estimated Entropy: {entropy} bits")

    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MODERATE"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    print(f"Password Strength: {strength}")

    if recommendations:
        print("\nSecurity Recommendations:")

        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("\nExcellent! Your password meets all security checks.")

    print("=" * 50)


def main():
    print("=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("\nEnter a password to analyze: ")

    check_password_strength(password)


if __name__ == "__main__":
    main()