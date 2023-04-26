class Book:
    
    #Constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.price = None

    #Getters and Setters
    def set_title(self, title):
        self.title = title
        
    def get_title (self):
        return self.title
    
    def set_author(self, author):
        self.author = author
        
    def get_author(self):
        return self.author
    
    def set_year(self, year):
        self.year = year
        
    def get_year(self):
        return self.year
    
    def set_price(self, price):
        self.price = price
    
    def get_price(self):
        return self.price
    
    #Methods
    def contains(self, str):
        return str in self.title
    
    @staticmethod
    def get_title_in_title_case(title):
        words = title.split(" ")
        result = []
        for word in words:
            result.append(word[0].upper() + word[1:].lower())
        return " ".join(result)
    
    def print_authors(self):
        authors = self.get_author().split(',')
        return "Authors: " + ", ".join(authors)
         
#Testing
b1 = Book("the wizard of Oz", "Matthew Salazar,James Ball,John Donald,Barry Allen", 2004)
b1.set_price(50)
b1.set_title(Book.get_title_in_title_case(b1.get_title_in_title_case(b1.get_title())))

print("Information:")
print(b1.print_authors())
print("Title: " + b1.get_title())
print("Year: " + str(b1.get_year()))
print("Price: " + str(b1.get_price()))
