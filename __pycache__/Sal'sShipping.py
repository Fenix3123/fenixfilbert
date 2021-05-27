#change this value to find shipping costs for Sals company
weight = 8.4

cost = 0
Ground_prem_shipping = 125
#Ground shipping
if weight <= 2:
   cost = weight * 1.5 + 20
   print("Ground shipping Cost is {:.1f}".format(cost))
elif weight > 2 and weight <= 6:
   cost = weight * 3 + 20
   print("Ground shipping Cost is {:.1f}".format(cost))
elif weight > 6 and weight <= 10:
   cost = weight * 4 + 20
   print("Ground shipping Cost is {:.1f}".format(cost))
elif weight < 10:
   cost = weight * 4.75 + 20
   print("Ground shipping Cost is {:.1f}".format(cost))
print("If you want premium ground shipping its {:.1f}".format(Ground_prem_shipping))

#drone shipping
if weight <= 2:
   cost = weight * 4.5
   print("/nDrone shipping Cost is {:.1f}".format(cost))
elif weight > 2 and weight <= 6:
   cost = weight * 9
   print("Drone shipping Cost is {:.1f}".format(cost))
elif weight > 6 and weight <= 10:
   cost = weight * 12
   print("Drone shipping Cost is {:.1f}".format(cost))
elif weight < 10:
   cost = weight * 14.25
   print("Drone shipping Cost is {:.1f}".format(cost))
   

   




