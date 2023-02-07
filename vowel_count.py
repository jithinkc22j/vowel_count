# python program for counting the number of vowels in a text file - python file handling 
vowel = 0
vowels_list = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
d=open('sample.txt', 'r') # change sample.txt into your file name 
data=d.read()
for word in data:
    if word in vowels_list:
        vowel=vowel+1
print("Number of vowels:",vowel)
