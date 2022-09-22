#Program will ask for user's name and ask how old they are
print("Hey! We haven't met before. What' your name?")

user_name=input()
    #Whatever is typed into the input will become a string
print('Nice to meet you '+user_name+'!')
    #the len() function will count the characters in a string
print('Your name is '+str(len(user_name))+' characters long.')

print('How old are you?')
user_age=input()
    #In order to do math, the input needs to be converted into an integer value.
        #Once the math is calculated, the integer needs to be converted back into a string to be added to the sentance
print('In 4 more years you will be: '+str(int(user_age)+4))

print('See ya!')











