#Ch 6. Functions Problem 7
#Find best customer from biggest sale
#Program continuosly prompts user until sentinel. First input is sale, second is customer name
def main():
	#Create empty lists
	sales = []
	customer = []
	saleInput = 0
#Prompt then read the input values until sentinel
	print("Please enter sale followed by customer, 0 to quit:")
	
	while saleInput != "0":
		saleInput = input("")
		sales.append(float(saleInput))
		customerInput = input("")
		customer.append(customerInput)

	print(nameofBestCustomer(sales,customer))
#Find best sale record then return matching index in customer record
def nameofBestCustomer(Sales, Customers):
	sale = list(Sales)
	best = sale[0]
	bestIndex = 0
	customer = list(Customers)
	for i in range(1,len(sale)):
		if sale[i] > best:
			best = sale[i]
			bestIndex = i
	return customer[bestIndex]
main()
