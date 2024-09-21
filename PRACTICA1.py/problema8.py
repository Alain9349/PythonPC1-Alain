def main():
    hours, minutes=input("¿Qué hora es? ").split(":")
    if 7.0 <= convert(hours, minutes) <=8.0:
        print("hora del desayuno")
    elif 12.0 <= convert(hours, minutes) <=13.0:
        print("hora del almuerzo")
    elif 18.0 <= convert(hours, minutes) <=19.0:
        print("hora de la cena")
    else:
        print("inclusivo")

def convert(y, x):
    x=int(x)/60
    y=int(y)
    return float(x+y)
if __name__ == "__main__":
    main()