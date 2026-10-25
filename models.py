class Movie:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre 
        self.rating = rating
    
    def display(self):
        print(f"title: {self.title}")
        print(f"year: {self.year}")
        print(f"genre: {self.genre}")
        print(f"rating: {self.rating}")
        print("\n")

    def to_dict(self):
        return{
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "rating": self.rating
        }
        
    def display_fav(self):
        print(f"{self.title}")
    



