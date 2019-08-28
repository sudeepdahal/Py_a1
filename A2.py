number_of_the_purchase = 0
cost_of_deliveries = 0
def main():
	#code for upper header design
	designCode()
	#To checking for users next purchase
	another_purchase = 'y'
	#Initializing delivery charge, purshase total and number of items to 0
	del_charge = 0.0
	purchase_total = 0.0
	n = 0
	'''try:
		question1 = int(input("Enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Congratulations - you followed the instructions")
	question1 = input("Enter a number: ")
	if question1.isdigit():
		question1= int(question1)
		print('adfadfasdfadsf')
	else:
		 print("Not a number")'''
	#Repeating the delivery calculator if user enters y or Y
	while (another_purchase == 'y' or another_purchase == 'Y'):
		purchase_total = float(input('\nPlease enter purchase total:'))
		#checking for purchase total is above 150 or not
		purchaseTotal = checkPurchaseTotal(purchase_total)
		if purchaseTotal:
			n = int(input('Please enter number of the items:'))
			#Checking if number of items enterd user are negative or 0
			while (n <= 0):
				print('Invalid Number of Items');
				n = int(input('Please enter number of the items:'))
			del_day = int(input('Please enter delivery day ([1] for 1st day and [2] for 2nd day:'))
			#Checking if delivery day are besides 1 or 2
			while not (del_day == 1 or del_day == 2):
				print('Invalid Number of Delivery Days');
				del_day = int(input('Please enter delivery day ([1] for 1st day and [2] for 2nd day:'))
			#Calling the calculating function
			del_charge,total_charges = calCharges(n,del_day,purchase_total)
			#Display of delivery charges and total charges as floating-point numbers with 2 decimal places
			print('Delivery Charges: ',format(del_charge,'.2f'))
			print('Total Charges: ',format(total_charges,'.2f'))
		else:
			#else case if purchase total is below $150
			print('ERR: Sorry, purchase total need to be above $150.')
		#Asking if users wants to use the delivery calculator again
		another_purchase = input('Do you want to calculate delivery charges for another purchase? (y/n)')
	print('Thanks for using the delivery charges Calculator!\nSee you again!\n')
	print('Total number of purchase made: ',number_of_the_purchase)
	print('Total cost of Delivery made: ',format(cost_of_deliveries,'.2f'))
def designCode():
	for x in range(50):
		print('-',end='')
	print('\nWelcome to delivery charges Calculator')
	for x in range(30,):
		print('-',end='')
def checkPurchaseTotal(purchase_total):
	if purchase_total > 150:
		return True
	else:
		return False
	print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
def calCharges(n,del_day,purchase_total):
	#calculation of delivery charges accordingly 
	if n <= 5 and del_day == 1:
		del_charge = 8.0
	elif n <= 5 and del_day == 2:
		del_charge = n * 1.5
	elif n >= 6 and del_day == 1:
		del_charge = n * 2.5
	elif n >= 6 and del_day == 2:
		del_charge = n * 1.2
	else:
		#If non of the case behave accordingly exiting the program
		print('Something went wrong')
		exit()
				
	global number_of_the_purchase,cost_of_deliveries
	number_of_the_purchase += 1
	cost_of_deliveries += del_charge
	return del_charge,purchase_total+del_charge
main()

