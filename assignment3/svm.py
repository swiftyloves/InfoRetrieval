


# read file
_file = open('train.tsv')
with open('train.tsv', 'r') as _file:
	posts = [line.split('\t') for line in _file.readlines()]

for post in posts:
	post[1] = post[1][:-1]

print(posts[1])


