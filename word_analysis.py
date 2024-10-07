def golden(name):
    sum = 0
    for c in range(0, len(name)):
        sum+=(ord(name[c])-96)
    sum = sum % len(name)
    if sum == 0:
        return "yes"
    else:
        return "no"
def palindrome(name):
    if name == name[::-1]:
        return "yes"
    else:
        return "no"
def vowel(name):
    counter1 = 0
    counter2 = 0
    for c in range(0, len(name)):
        if name[c] == 'a' or name[c] == 'u' or name[c] == 'i' or name[c] == 'e' or name[c] == 'o':
            counter1 += 1
        else:
            counter2 += 1
    if counter1 >= counter2:
        return "yes"
    else:
        return "no"
def non_vowel(name):
    counter1 = 0
    counter2 = 0
    for c in range(0, len(name)):
        if name[c] == 'a' or name[c] == 'u' or name[c] == 'i' or name[c] == 'e' or name[c] == 'o':
            counter1 += 1
        else:
            counter2 += 1
    if counter1 <= counter2:
        return "yes"
    else:
        return "no"
filename = "D:\\text.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
print("word\tGolden\tPalindrome\tVowel\tNon Vowel")
for line in lines:
    print(line+"\t\t"+golden(line)+"\t\t"+palindrome(line)+"\t\t\t"+vowel(line)+"\t\t"+non_vowel(line)+"\n")