#code for upper header design
for x in range(50):
    print('-',end='')
print('\nWelcome to delivery charges Calculator')
for x in range(30,):
    print('-',end='')
#To checking for users next purchase
another_purchase = 'y'
#Initializing delivery charge, purshase total and number of items to 0
del_charge = 0.0
purchase_total = 0.0
n = 0
#Repeating the delivery calculator if user enters y or Y
while (another_purchase == 'y' or another_purchase == 'Y'):
    purchase_total = float(input('Please enter purchase total:'))
    #checking for purchase total is above 150 or not
    if purchase_total > 150:
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
        #Display of delivery charges and total charges as floating-point numbers with 2 decimal places
        print('Delivery Charges: ',format(del_charge,'.2f'))
        print('Total Charges: ',format(del_charge+purchase_total,'.2f'))
    else:
        #else case if purchase total is below $150
        print('ERR: Sorry, purchase total need to be above $150.')
    #Asking if users wants to use the delivery calculator again
    another_purchase = raw_input('Do you want to calculate delivery charges for another purchase? (y/n)')
print('Thanks for using the delivery charges Calculator!\nSee you again!')

