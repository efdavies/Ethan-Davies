##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

"""This program calculates profit or loss on a cryptocurrency transaction."""

# Constants

DATA_FILE = "CryptocurrencyTradingData.txt"

def cryptocurrency_calculator():
    """You fill in the details."""
# Startup code
    d={}
    date = None
    with open(DATA_FILE) as fn:
        for line in fn:
            if line[0].isnumeric():
                d[line.strip()]= {}
                date= line.strip()
            else:
                i=line.find(':')
                name=line[:i]
                price=float(line[i+2:])
                d[date][name]= price

    currency= input("Name :")
    units_purchased= int(input("Units Purchased :"))
    purchase_date= input("Purchase Date :")
    sell_date= input("Sell Date :")

    Profit = units_purchased*d[sell_date][currency]-units_purchased*d[purchase_date][currency]
    Profit = float(round(Profit,2))
        # Display profit or loss
    if Profit < 0:
        print(f"Net Loss: ${format(int(-Profit), ',.2f')}")
    else:
        print(f"Net Gain: ${format(int(Profit), ',.2f')}")


if __name__ == "__main__":
    cryptocurrency_calculator()
