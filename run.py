import time
import os

gen = 0

def printState(m):
	global gen
	total = 0
	os.system('clear')
	for _ in m:
		total += _.count('1')
		print(_)
	print('\nGeneration: %d | Live cells: %d' % (gen, total))
	gen += 1

def run(w, h, m):
	new_m = []
	count = 0
	for _ in range(h):
		tmp = ''
		for __ in range(w):
			if(__ > 0):
				if(m[_][__-1] == '1'):
					count += 1
			if(__ != w-1):
				if(m[_][__+1] == '1'):
					count += 1
			if(_ > 0):
				if(m[_-1][__] == '1'):
					count += 1
				if(__ > 0):
					if(m[_-1][__-1] == '1'):
						count += 1
				if(__ != w-1):
					if(m[_-1][__+1] == '1'):
						count += 1
			if(_ != h-1):
				if(m[_+1][__] == '1'):
					count += 1
				if(__ > 0):
					if(m[_+1][__-1] == '1'):
						count += 1
				if(__ != w-1):
					if(m[_+1][__+1] == '1'):
						count += 1	
			if(m[_][__] == '1' and (count == 2 or count == 3)):
				tmp += '1'
			elif(m[_][__] == '0' and count == 3):
				tmp += '1'
			else:
				tmp += '0'
			count = 0
		new_m.append(tmp)
	return new_m
	
os.system('clear')
m = open('data', 'r').read().replace('\n','').split(',')
printState(m)

while True:
	time.sleep(1)
	m = run(10, 10, m)
	printState(m)

