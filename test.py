amount = 13
ålder = {'Julia' : 100, 'Anton' : 12, 'Ellen' : 13}
print(ålder)
run = dict(Alexsander = 201, Bergman = 204, Ek = 291)
print(run)
ålder.get('Julia')
print(ålder.get('Julia'))

amount = amount + ålder.get('Julia')
print(f"{amount}")

