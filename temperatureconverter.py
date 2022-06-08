tempinc=int(input("Temperature in celcius"))
tempinf=1.8 * tempinc + 32
print("Temperature in Farenheit ", tempinf)
if tempinf > 100:
    print("it is very hot")
elif tempinf < 50:
    print("it is very cold")
else:
    print("it is very nice")
