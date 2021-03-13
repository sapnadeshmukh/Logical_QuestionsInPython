pages=int(input("enter pages"))
needed_pages=int(input("which page u want"))
turn=input("enter right or left")
total_pages=pages//2
if  turn=="left":
	print (needed_pages//2)
else:
	print (total_pages-needed_pages//2)