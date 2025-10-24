print('Welcome to your Anime Favorites Lister')

name = input("What is your name? ")


lahat = []

while True: 
    anime = input("Enter the title of the anime for your list of favotires (or type exit to finish) ").lower()
    print(f" '{anime}' HAS BEEN ADDED TO YOUR LIST!!")
    if anime == 'exit':
        print("You've exited the program")
        break
    lahat.append(anime)

huwat = len(lahat)
print(f"Hi {name}! You're anime list consist of:")
for i in range(1, huwat+1, 1):
    print(f'- {lahat[i-1]}')
    

    