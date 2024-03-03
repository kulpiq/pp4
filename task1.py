class Object:
    def __init__(self, title, net, vat):
        self.title = title
        self.net = net
        self.vat = vat

c1 = Object("Clean Code, Robert C. Martin",100, 0.08)
c2 = Object("Applying UML and Patterns, C. Larman", 300, 0.08)
c3 = Object("Shipping", 50, 0.23)

def total_net():
    total_net = c1.net + c2.net + c3.net
    return total_net

def sum_of_vat():
    sum1 = c1.vat* c1.net
    sum2 = c2.vat*c2.net
    sum3 = c3.vat*c3.net
    return sum1 ,sum2, sum3

print(f"|               |  Total net  |     X     |\n|---------------|-------------|-----------|\n| VAT 8%        |     {total_net()}     |    {sum_of_vat()[0]+sum_of_vat()[1]}   |\n| VAT 23%       |     {total_net()}     |    {sum_of_vat()[2]}   |")



