favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)

print("\nSarah's favorite language is " + favorite_languages['sarah'].title() + ".\n")

# Loop through all key in a distionary
for name, lang in favorite_languages.items():
    print(name.title() + "'s favorite language is "+ lang.title())

print()
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
        
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!"
          + " \n")
        
# Loop dictionsry's key in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# Loop all values in a dictionaty
# Reduce replicated using `set`
print("\nThe following languages have been mentioned:")
for lang in set(favorite_languages.values()):
    print(lang.title())

