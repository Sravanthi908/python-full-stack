class Movie():
    def _init_(self,hero,title,budget):
        self.name = hero
        self.title = title
        self.budget = budget
    def dispaly_info(self):
        print(f"Hero's name is {self.name}")
x = Movie("PSPK ","OG",500)
x.dispaly_info()
x = Movie("yash","KGF",500)
print(x.name)
print(x.title)
print(x.budget)