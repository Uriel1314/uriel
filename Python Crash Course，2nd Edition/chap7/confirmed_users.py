unconfimed_users = ['alice','brian','candace']
confimed_users = []

# 验证每个用户，直到没有未验证的用户为止
while unconfimed_users:
	current_user = unconfimed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confimed_users.append(current_user)

# show verified users
print("\nThe following users have been confirmed:")
for confimed_user in confimed_users:
	print(confimed_user.title())