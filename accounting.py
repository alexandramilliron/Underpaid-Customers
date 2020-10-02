melon_cost = 1.00

def melonorders(file):
    openfile = open(file)

    for line in openfile:
        line = line.rstrip()
        splitline = line.split('|')
        customer_name = splitline[1]
        customer_melons = float(splitline[2])
        customer_paid = float(splitline[3])
    
    customer_expected = customer_melons * melon_cost
    
    if customer_expected != customer_paid:
        print(f"{customer_name} paid ${customer_paid:.2f},",
          f"expected ${customer_expected:.2f}"
          )

melonorders("customer-orders.txt")