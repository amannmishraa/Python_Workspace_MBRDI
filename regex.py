import re

def main():
    text = "Contact me at user123@gmail.com or call 123-456-7890. Price is 45 dollars."
    phone_match = re.search(r"\d{3}-\d{3}-\d{4}", text)
    if phone_match:
        print("Phone number found:", phone_match.group())

    numbers = re.findall(r"\d+", text)
    print("All numbers found:", numbers)

    email_pattern = r"^\w+@\w+\.\w+$"
    email = "user123@gmail.com"
    if re.match(email_pattern, email):
        print("Valid email:", email)
    else:
        print("Invalid email:", email)

    masked_text = re.sub(r"\d", "X", text)
    print("Masked text:", masked_text)

    value = "12345"
    if re.fullmatch(r"\d+", value):
        print("Value contains only digits")

if __name__ == "__main__":
    main()
