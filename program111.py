### program111.py

import dwelling
def main():
    home = dwelling.House('5 Ash Dr',1800,200000,True,2)
    print(home)
    ### repeat for an Apt instance
    apt = dwelling.Apt('111 Fake Address',1500,0,1100,False)
    print(apt)
    ## condo instance
    condo = dwelling.Condo('123 Faker Address Lane',2000,200000,200,'Pool')
    print(condo)
main()
