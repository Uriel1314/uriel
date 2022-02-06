# 练习 8-7 专辑
# 编写一个名为 make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接
# 受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示
# 不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数 make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用
# 这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少
# 在一次调用中指定专辑包含的歌曲数。


# Simple version:
def make_album(artist, title):
	"""创建一个包含专辑信息的字典。"""
	album_dict = {
	'artist': artist.title(),
	'title': title.title(),
	}

	return album_dict


album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)