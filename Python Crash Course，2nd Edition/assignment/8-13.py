# def build_profile(first, last, **user_info):
# 	""" 创建一个字典，其中包含我们知道的有关用户的一切。 """
# 	user_msg = {
# 		'first_name':first.title(),
# 		'last_name':last.title(),
# 	}

# 	for key, value in user_info.items():
# 		user_msg[key] = value

# 	return user_msg


# method 2nd
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last

	for key, value in user_info.items():
		user_info[key] = value
	return user_info 


user_profile = build_profile(
								'albert', 'einstein',
								location = 'princeton',
								field = 'physics')

print(user_profile)