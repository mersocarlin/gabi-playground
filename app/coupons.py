import csv

couponCosts = 0.0
couponUsage = {}

with open('coupons.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        couponCode = row[5].upper()
        couponAmount = float(row[6])

        if couponCode in couponUsage:
            couponUsage[couponCode] = couponUsage[couponCode] + 1
        else:
            couponUsage[couponCode] = 1

        if couponCode == "BILD20":
            couponCosts = couponCosts + couponAmount

for couponCode in couponUsage:
    if couponUsage[couponCode] > 10:
        print couponCode + " is used " + str(couponUsage[couponCode]) + " times"

print couponCosts
