punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("enter any string:---")

puct_removed_str = ""
for char in my_str:
   if char not in punctuations:
       puct_removed_str = puct_removed_str + char

print(puct_removed_str)