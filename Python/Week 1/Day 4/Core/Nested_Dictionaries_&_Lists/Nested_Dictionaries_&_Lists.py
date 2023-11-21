x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#? 1 :
#1
x[1][0]=15
print(x)
#2
students[0]['last_name']='Bryant'
print(students[0]['last_name'])
#3
sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])
#4
z[0]['y']=30
print(z) 
# #? 2 :
#1 
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        print(some_list[i])
iterateDictionary(students) 
#? 3 : 
#1 
def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        for key_name in some_list[i]:
            print(some_list[i][key_name])
iterateDictionary2(['first_name'],students)
#? 4 : 
def printInfo(some_dict):
    for k in some_dict:
        for i in range (0,len(some_dict[k])):
                print(f'{len(some_dict[k])} {k}') #todo ==> i will ask for this tommorow 
                print({some_dict[k][i]})
printInfo(sports_directory)


