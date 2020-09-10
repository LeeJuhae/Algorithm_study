import sys

def isSingleData(video):
	data = video[0][0]
	N = len(video)
	for row in video:
		if row.count(data) != N:
			return False
	return True

def divide(video):
	videos = [[],[],[],[]]
	N = len(video)
	for idx, row in enumerate(video):
		n = int(N / 2)
		if idx < n:
			videos[0].append(row[:n])
			videos[1].append(row[n:])
		else:
			videos[2].append(row[:n])
			videos[3].append(row[n:])
	return videos

def compress(video, string):
	if len(video) == 1 or isSingleData(video):
		string += str(video[0][0])
	else:
		string += '('
		videos = divide(video)
		for v in videos:
			string = compress(v, string)
		string += ')'
	return string

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	video = []
	for _ in range(N):
		video.append(list(map(int,list(sys.stdin.readline().rstrip()))))
	print(compress(video, ""))
