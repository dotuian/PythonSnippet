#help(dict)

ab = {
    "A01": "shoukii01@test.com",
    "A02": "shoukii02@test.com",
    "A03": "shoukii03@test.com",
    "A04": "shoukii04@test.com",
    }
print "A01`s address is %s" %ab['A01']

#adding a key/value pair
ab["A05"] = "shoukii05@test.com"


print "\nThere are %d contacts in the address-book\n" %len(ab)
for name, address in ab.items():
    print "Contact %s at %s " %(name, address)

if "A02" in ab:
    print "\nA02`s addresss is %s" %ab["A02"]
