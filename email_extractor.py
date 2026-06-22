import re

with open("input.txt", "r") as file:
    text = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Deduplicate while preserving order
seen = set()
unique_emails = [e for e in emails if not (e in seen or seen.add(e))]

with open("emails.txt", "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print(f"{len(unique_emails)} unique email(s) extracted successfully!")