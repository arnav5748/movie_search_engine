import json
from api import search_movies, search_movie_id
from models import Movie
    
def search_movie_flow():
# search movie block
    movie_name = input("Enter movie name: ")
    print("\n")

    json_return = search_movies(movie_name)
    
    if json_return["Response"] == "False":
        print("Movie not found!")
        return
    
    else:
        for i, name in enumerate(json_return["Search"], start=1):
            print(f"{i}.", name["Title"], f"({name["Year"]})")
        print("\n")
        
        while True: 
            try:
                a = int(input("enter the require index: "))
                if 1 <= a <= len(json_return["Search"]):
                    break
                else:
                    print("Invalid index. Please try again.\n")

            except ValueError:
                print("Please enter a valid number.\n")
                
        movie_full_detail = search_movie_id(json_return["Search"][a-1]["imdbID"])

        movie = Movie(
        movie_full_detail["Title"],
        movie_full_detail["Year"],
        movie_full_detail["Genre"],
        movie_full_detail["Rated"]
        )
        print("~~~~~ MOVIE DETAILS ~~~~~")
        movie.display()

        # fav block 
        fav_q1 = input("wanna add to you favourite?(Y/N): ")
        if fav_q1 == "Y":
            try:
                with open ("favourite.json", "r") as file:
                    favourites = json.load(file)
            except FileNotFoundError:
                favourites = []

            favourites.append(movie.to_dict())

            with open ("favourite.json", "w") as file:
                json.dump(favourites, file)
            

def view_favourite():
# fav print block
    try:
        with open ("favourite.json", "r") as file:
            favourites = json.load(file)
            print("~~~~~ FAVOURITES ~~~~~")
            for i, item in enumerate(favourites, start = 1):
                m = Movie(item["title"], item["year"], item["genre"], item["rating"])
                print(f"{i}.", end="")
                m.display_fav() 

    except FileNotFoundError:
        print("No favourite added so far...")

def remove_favourite():
# remove fav block
    fav_q2 = input("wanna remove favourite?(Y/N): ")
    print("\n")
    if fav_q2 == "Y" :
        try:
            with open ("favourite.json", "r") as file:
                favourites = json.load(file)
                for i, item in enumerate(favourites, start=1):
                    print(f"{i}. {item["title"]}")
            
            print("\n")

            choice = int(input("which item to remove? : "))
            
            if 1 <= choice <= len(favourites) :
                removed = favourites.pop(choice-1)
                with open ("favourite.json", "w") as file:
                    json.dump(favourites, file)
                print(f"{removed['title']} removed!")
            
            else:
                print("Invalid Index")
        
        except FileNotFoundError:
            print("No favourite added so far...")
            
while True:

    print("\n===== MOVIE APP ======")
    print("1. Search Movie")
    print("2. View Favourites")
    print("3. Remove Favourite")
    print("4. Exit")

    choice = input("Enter choice: ")
    print("\n")

    if choice == "1":
        search_movie_flow()
        
    elif choice == "2":
        view_favourite()

    elif choice == "3":
        remove_favourite()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")