# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

petSpecies = input('Enter the pet species: ')
petAge = int(input('Enter the pet age: '))

if petSpecies == 'dog':
    if petAge < 2:
        print('Puppy food is recommended.')
    else:
        print('Adult dog food is recommended.')
elif petSpecies == 'cat':
    if petAge < 5:
        print('Kitten food is recommended.')
    else:
        print('Senior cat food is recommended.')
else:    
    print('Invalid pet species.')   