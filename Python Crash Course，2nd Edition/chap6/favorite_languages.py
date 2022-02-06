favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages['sarah']

print()

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

for language in favorite_languages.values():
	print(language.title())

print("*"*58)
# 剔除重复的元素
for language in set(favorite_languages.values()):
	print(language.title())

# This is a set not dictionary 
languages = {'C','python','java'}
print(type(languages))

favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")