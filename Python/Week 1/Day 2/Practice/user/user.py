class User : 
    def __init__(self , data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.is_rewards_member = False
        self.gold_card_points = 0

    @classmethod 
    def display_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Member: {self.is_rewards_member}')
        print(f'Current Points: {self.gold_card_points}')
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points
my_user = User(80)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(100)
my_user.display_info()


        