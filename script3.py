count = 0
emails = []
with open("mbox-short.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 1:
                email = words[1]
                emails.append(email)
                print(email)
                count += 1

print(f"Обще кол-во: {count}")

unique_words = []
file = open("romeo.txt", "r", encoding="utf-8")
for line in file:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
file.close()
unique_words.sort()
print(unique_words)