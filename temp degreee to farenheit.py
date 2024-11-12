#temp degreee to farenheit
def tempconv():
    celc=int(input("Enter temperature in celius:"))
    faren=9/5*celc + 32
    print(f"{celc}C = {faren}F")
tempconv()