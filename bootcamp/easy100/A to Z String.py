s = str(input())

a_index = s.find('A')
z_index = s.rfind('Z')

length = (len(s) - a_index) - (len(s) - z_index - 1)
print(length)
