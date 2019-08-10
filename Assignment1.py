another_purchase = 'y'
del_charge = 0.0
purchase_total = 0
n = 0
while another_purchase == 'y' or another_purchase == 'Y':
    purchase_total = 0
    while purchase_total >= 0:
        purchase_total = float(input('Please enter purchase total:'))
        if purchase_total > 150:
            n = int(input('Please enter number of the items:'))
            del_day = int(input('Please enter delivery day ([1] for 1st day and [2] for 2nd day:'))
            
            if n <= 5 and del_day == 1:
                del_charge = 8.0
            elif n <= 5 and del_day == 2:
                del_charge = n * 1.5
            elif n >= 6 and del_day == 1:
                del_charge = n * 2.5
            elif n >= 6 and del_day == 2:
                del_charge = n * 1.2
            else:
                print('---')
                #line 17
            print(del_charge)
            print('Delivery Charges: ',format(del_charge,'.2f'))
            print('Total Charges: ',format(del_charge+purchase_total,'.2f'))
        #elif
        else:
            print('ERR: Sorry, purchase total need to be above $150.')
        another_purchase = input('Do you want to calculate delivery charges for another purchase? (y/n)')
print(n)
print('Thanks for using the delivery charges Calculator!/nSee you again!')

