local=input("Onde devo apontar?\nR.:")
a=open("faceis\\"+local+".py","a+")
a.write("resp=\"\"\n")
while True:
    com=input("")
    com=com.replace("a resposta","\"+resp+\"")
    if com[:4]=="diz ":
        a.write("print(\""+com[4:]+"\")\n")
    elif com[:9]=="pergunta ":
        a.write("resp=input(\""+com[9:]+"\")\n")
    elif com=="fecha o programa":
        a.write("exit()\n")
    elif com=="terminado":
        a.close()
        exit()
    elif com[:3]=="se " and " for " in com[3:]:
        a.write("if \""+com[3:com.find(" for ")]+"\"==\""+com[com.find(" for ")+5:]+"\":\n    ")
