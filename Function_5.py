def factor(bil:int):
    hasil=1
    for i in range (1,bil+1):
        hasil=hasil*i
    return hasil

if __name__ == '__main__':
    bil=int(input("Bilangan\t= "))
    try:
        if bil>=0 :
            print(f"Faktorial {bil}!\t= {factor(bil)}")
        else :
            raise ValueError
        
    except ValueError:
        print("Masukkan nilai minimal 0")
