# 练习 6-6 调查
# 在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。
#  创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含
# 在字典中。
#  遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调
# 查的人，打印一条消息邀请他参与调查。

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")