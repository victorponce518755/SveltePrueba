n1 =3 
b=n1
def calculo(n1):
    if n1 !=0 and n1 == b:
        
        texto="*"
        print(texto*n1)
        
        calculo(n1-1)
    elif n1 != 0:
        texto = "*"
        espacio=""
        if n1%2 == 0:
            print("soy par")
            print(espacio*(n1-1),texto*n1)
            print("mis espacios son ",espacio*(n1-1) )
        else:
            print(espacio*n1,texto*n1)
            
        
        calculo(n1-1)

if __name__ == "__main__":
    calculo(n1)