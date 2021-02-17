class Passanger:
    def __init__(self, pid, pname, pgender, pdist):
        self.pid = pid
        self.pname = pname
        self.pgender = pgender
        self.pdist = pdist

    def calculate_discount(self, pid, discount_rate):
        for i in pass_list:
            if i.pid == pid:
                discount = (i.pdist*discount_rate)/100
                return discount

class Organization(Passanger):
    def __init__(self, oname, pass_list):
        self.oname = oname
        self.pass_list= pass_list


if __name__ == "__main__":
    pass_list= []
    n = int(input())
    for i in range(n):
        pid = input()
        pname = input()
        pgender = input()
        pdist = int(input())
        pass_list.append(Passanger(pid, pname, pgender, pdist))

    pid = input()
    discount_rate= int(input())
    o = Organization('TCS', pass_list)
    discount = o.calculate_discount(pid, discount_rate)
    if discount < 0:
        print("Passanger not eligible for discount")
    else:
        print("The discout of passanger "+pid+" is "+str(discount))
