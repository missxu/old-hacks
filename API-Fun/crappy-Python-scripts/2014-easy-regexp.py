import fileinput
import re

# in 2014, I had to download a crap ton of Chase statements so I can grab some transactions and reformat them. Why? 
# because Chase charges a monthly fee for access to OFX and I personally find the fee offensive
# yes, I'm sure it took me a lot longer to create a py script to deal with it than to just pay the fee
# but what fun would that be? It was a good chance to buff up on python regular expressions

for line in fileinput.input():
    line = re.sub('CHASE            AUTOPAYBUS                 PPD ID: \d+','LW Visa', line.rstrip())
    line = re.sub('Chase QuickPay Electronic Transfer \d+ to ','', line.rstrip())
    line = re.sub('Online Payment \d+ To ','', line.rstrip())
    line = re.sub('Payment to Chase card ending in DDDD \d+/\d+','LW Visa', line.rstrip())
    #Payment to Chase card ending in DDDD 
    # line = re.sub('^\d+','\n?', line.rstrip())
    print(line)
