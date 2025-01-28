'''
Las tuplas som inmutables
se declaran con ( )
'''

tupla=("uno","dos","tres")
print(tupla)

tuplaVariosDatos=(12,True,23.5,"El gato",12+4j)
print(tuplaVariosDatos)

tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

a,b,c=tupla
print(a,b,c)


#imprime el primer elemento de la tupla