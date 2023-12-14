class User:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def display_info(self):
        print(f"Name: {self.name}, Points: {self.points}")
        return self  

    def enroll(self):
        print(f"{self.name} has been enrolled")
        return self  

    def spend_points(self, amount):
        self.points -= amount
        print(f"{self.name} spent {amount} points")
        return self  


user1 = User("Alice", 100)
user2 = User("Bob", 150)


user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
