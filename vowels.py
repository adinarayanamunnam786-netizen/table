s="HI HELLO RAJU"
vow=[]
con=[]
l=[vow.append(x) if x in ['A','E','I','O','U'] else con.append(x) for x in s if x!=" "]
print(vow)
print(con)