date = input("please enter today's date: \n")
if date.find("/"):
    date = date.replace('/', '-')
    print(date)
mood = input("how was your mood today? \n")

journal = input("Tell yourself about your day today: \n")

with open(f"./records/{date}", 'w') as file:
    file.write(mood + "\n")
    file.write(journal + "\n")
