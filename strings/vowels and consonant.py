n=int(input())
for _ in range(n):
    a=input()
    vowels= 'aeiouAEIOU'
    vowel_count=0
    consonant_count=0
    for char in a:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    print(vowel_count,consonant_count)