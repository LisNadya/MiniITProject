#-------------------------------------------------- SRI'S CODE ---------------------------------------------------------
import os
import json

json_obje= open('auth.json')#open authentication file
dataauth = json.load(json_obje)

#--------------------------------------- Authentication ------------------------------------------------
def writefile(): #Writes file for new user
    global user
    m =[]
    d = {}
    book={}
    album=[]
    a=1
    arr=[31,28,31,30,31,30,31,31,30,31,30,31]

    while (a<=12):
        d={}
        m=[]
        book={}
        for i in range (1,(arr[a-1]+1)):
            d ={"expense":0,"day":i}
            m.append(d)
            book[("days")]=m
                        
        book[("month")]=a
        album.append(book)
        a+=1

    

    with open(str(user)+".json","w") as outfile:
        json.dump(album,outfile,indent=4)

    
    
def logup(): #Sign up page
    global user
    global passw
    f = {}
    e = []
    print "************************************************\nSign Up\n************************************************" 
    auth = {}
    user = raw_input ("\n>> Username: ") #New username
    passw = raw_input (">> Password: ") #New password
    reenterpass = raw_input (">> Confirm Password: ") #New password confirm

    if (passw == reenterpass): #If passwords match
        print '\nVerifying...\nPasswords match!\n\nAccount succesfully registered!'
        auth['user'] = user
        auth['passw']= reenterpass
        
        for i in range (1,13):                          
                f ={"salmonth":i,"salary":0,"goal":0}   
                e.append(f)                         
        auth['info']=e
        dataauth.append(auth)
        with open('auth.json','w') as outfile:
            json.dump(dataauth,outfile,indent=4)
            
        os.system ("cls")
        writefile()
        startmenu()
    else: #If passwords fail to match
        print '\nPasswords did not match...'
        reenterpass = raw_input ("\n>> Confirm Password: ") 
        if (passw== reenterpass):
            print '\nVerifying...\nPasswords match!\nAccount succesfully registered!'
            auth['user'] = user
            auth['passw']= reenterpass
                       
            for i in range (1,13):
                    f ={"salmonth":i,"salary":0,"goal":0}   #CHANGES
                    e.append(f)
            auth['info']=e
            dataauth.append(auth)

            
            with open('auth.json','w') as outfile:
                json.dump(dataauth,outfile,indent=4)
            
            writefile()
            os.system ("cls")
            startmenu()
        else:
            print "\nProgram will exit..."
            os.system ("cls")
            startmenu()

def login(): #Log in page
    global user
    global passw
    global data
    global Salary
    global Goal
    global masuk
    global per 
    success = 0
    fail = 3
    print "************************************************\nLog In\n************************************************"
    while True:
        user = raw_input("\n>> Username: ") #Existing user
        passwordguess = raw_input(">> Password: ") #Existing password
        for masuk in range (len(dataauth)):
            try:
                if (dataauth[masuk]['user']== user and dataauth[masuk]['passw'] == passwordguess):
                    success=1
                    per=masuk
            except (KeyError):
                    success = 0
                    break

        if success == 0:
            print "Invalid password and username"
            fail = fail - 1
            print "\nNumber of tries left:", fail
            
        if fail == 0:
            entry = raw_input ("Limit exceeded more than 3 time. Press [ENTER] to exit.")
            os.system("cls")
            break
            
        else:
            if success == 1:
                os.system("cls")
                Salary=dataauth[per]['info'][month-1]['salary']   #CHANGES
                Goal=dataauth[per]['info'][month-1]['goal']         #CHANGES
                # Open json file and load all data into a two-dimensional array 
                with open(user+'.json') as json_file:
                    data = json.load(json_file)
                    
                mainmenu()        

def startmenu(): #Authentication menu page
    print "************************************************\nWelome to Financial Organizer\n************************************************"
    print "\n1. Log in"
    print "2. Sign up\n"
    log = ''
    while (not (log =='1' or log == '2')):
        log = raw_input (">> Do you want to log in or sign up? [1-2]: ") 
        if (log =='1'): 
            os.system("cls")
            login()
        elif (log =='2'):
            os.system("cls")
            logup()

#--------------------------------------- LIS & WANA'S CODE ------------------------------------------------------
import time
import datetime

#Universal constants
Exp = []
MonthName = ['Months', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

Goal = 0
Balance = 0
TotExp = 0
month = 0
numday = 0

localtime = time.asctime( time.localtime(time.time()) )
month=int(datetime.date.today().strftime("%m")) 

#--------------------------------------- Function 1: User Info ------------------------------------------------
def userinfo(): 
    update = ''
    global Salary
    global Goal
    print "************************************************\nWelcome to your user info\n************************************************"
    print "\n1. Update monthly salary\n2. Update monthly savings goal\n3. Back\n"
    while (not(update == '1' or update == '2' or update == '3')):
        Update = input("Which info would you like to update? [1-3]: ")
        
        if (Update == 1): #If user wants to update monthly salary
            i=0
            print "\n------------------------------------------------"
            print "\n1.Update salary on current month\n2.Update salary for a different month\n" 
            while (i==0):
                userchoose = raw_input(">> Choose your function [1-2]: ") #User selects month to update salary
                if (userchoose == '1'):
                    smonth=month
                    i=1
                elif (userchoose == '2'):
                    j = 0
                    while (j == 0):
                        smonth = input(">> Which month would you like to update? [1-12]: ") #User inputs month for salary
                        if (smonth<=12 and smonth>0):
                            j = 1
                            i = 1
                        else:
                            j = 0
                else:
                    i=0
            h = 0
            print ""
            while (h == 0):
                Salary = input(">> Enter current salary: RM ") #User enters monthly salary
                if (Salary >=0):
                    print "\nSalary updated."
                    dataauth[per]['info'][smonth-1]['salary']=Salary
                    with open('auth.json','w') as outfile:
                        json.dump(dataauth,outfile,indent=4)
                    usercontinue = raw_input("\nPress ENTER to continue...") #Pause
                    if (usercontinue==''):
                        os.system("cls")
                        userinfo()
                elif (Salary <0):
                    print "Your salary can't be a negative value. Try again."
                    h = 0
                else:
                    print "Your salary has to be an integer. Try again."
                    h = 0
                    
        elif (Update == 2): #If user wants to update savings goal
            i=0
            print "\n------------------------------------------------"
            print "\n1.Update savings goal on current month\n2.Update savings goal for a different month\n"
            while (i==0):
                userchoose = raw_input(">> Choose your function [1-2]: ") #User selects month to update goal
                if (userchoose == '1'):
                    smonth = month
                    i=1
                elif (userchoose == '2'):
                    j = 0
                    while (j==0):
                        smonth = input(">> Which month would you like to update? [1-12]: ") #User inputs month for goal
                        if (smonth<=12 and smonth>0):
                            j = 1
                            i = 1
                        else:
                            j = 0
                else:
                    i=0
            h = 0
            print ""
            while (h == 0):
                Goal = input(">> Enter monthly savings goal: RM ") #User enters savings goal
                if (Goal >=0):
                    dataauth[per]['info'][smonth-1]['goal']=Goal
                    with open('auth.json','w') as outfile:
                        json.dump(dataauth,outfile,indent=4)
                    print "\nYour goal has been updated."
                    usercontinue = raw_input("\nPress ENTER to continue...") #Pause
                    if (usercontinue==''):
                        os.system("cls")
                        userinfo()
                elif (Goal <0):
                    print "Your goal can't be a negative value. Try again."
                    h = 0
                else:
                    print "Your goal has to be an integer. Try again."
                    h = 0
                
        elif (Update == 3): #Exit to main menu
            os.system("cls")
            mainmenu()
#------------------------------------------- Function 2: Expense update --------------------------------------------------
def moneytracker():
    global DailyExp
    global Salary
    global TotExp
    global user
    global month
    h = 0
    records= {}
    print "\n------------------------------------------------\n" 
    while (h==0):
        DailyExp = input(">> Total daily expense: RM ")#User updates daily expense
        if (DailyExp >=0):
            data[month-1]['days'][numday-1]['expense'] = DailyExp
            
            #Overwrites daily expense into file
            with open(user+'.json','w') as outfile: 
                json.dump(data,outfile,indent=4)
                
            print "\nYour daily expense has been updated..."
            print "\n------------------------------------------------"
            print "\n1. Update another daily expense\n2. Back"
            usercontinue =''
            while(not(usercontinue=='1' or usercontinue=='2')):
                usercontinue = raw_input("\n>>Where would you like to proceed to?[1-2]: ")
                if (usercontinue=='1'):
                    os.system("cls")
                    moneytracker_date()
                elif (usercontinue=='2'):
                    os.system("cls")
                    mainmenu()            
        elif (DailyExp <0):
            print "Your expense can't be a negative value. Try again."
            h = 0  
        else:
            h = 0
                        
def moneytracker_date():
    global numday
    global month
    print "************************************************\nWelcome to your expense tracker\n************************************************"
    print "\nToday is: ", localtime, "\n"
    userpass=''
    while(not(userpass == 'Yes' or userpass == 'yes' or userpass == 'No' or userpass == 'no' or userpass =='Y' or userpass =='N' or userpass =='y' or userpass =='n')):
        userpass = raw_input (">> Would you like to choose another date? [Yes-No]: ")
        if (userpass == "Yes" or userpass =='yes' or userpass =='Y' or userpass =='y'):
            moneytracker_datesetup()#If user wants to change date
        elif (userpass == "No" or userpass =='no' or userpass =='N' or userpass =='n'):
            numday=int(datetime.date.today().strftime("%d"))
            month=int(datetime.date.today().strftime("%m")) 
            moneytracker()#If user doesn't want to change date

def moneytracker_datesetup():
    global month
    global numday
    g = 0
    j = 0
    h = 0
    while (g==0) :
         print "\n************************************************\nChange Your Date\n************************************************\n"
         while (j==0):
             cmonth= raw_input("Enter month [1-12]: ")#Change month in date
             if cmonth == "2"  :
                 daysinmonth=28
                 j = 1
             elif cmonth == "4" or cmonth == "6" or cmonth == "9" or cmonth == "11":
                 daysinmonth=30
                 j = 1
             elif cmonth == "1" or cmonth == "3" or cmonth == "5" or cmonth == "7" or cmonth == "8" or cmonth == "10" or cmonth == "12":
                 daysinmonth=month31
                 j = 1
             else:
                 j = 0
         while (h==0):
            day = input ("Enter day [1-"+`daysinmonth`+"]: ")
            if (day <= daysinmonth) :
                h = 1
            elif (day>daysinmonth):
                print "theres only",daysinmonth,"days in month",MonthName[month]
                h = 0
            else:
                h = 0
        
         
         print "\n>> New date:",day,"/",cmonth,"/2017" 
         userpass=''
         while(not(userpass == 'Yes' or userpass == 'yes' or userpass == 'No' or userpass == 'no' or userpass =='Y' or userpass =='y' or userpass =='N' or userpass =='n')):
              userpass = raw_input (">> Confirm your date? [Y/N]: ")
         if (userpass == "Yes" or userpass =='yes'or userpass =='Y'or userpass =='y'):
              numday=int(day)
              month=int(cmonth)
              moneytracker()
         elif (userpass == "No" or userpass =='no' or userpass =='y'or userpass =='Y'):
              moneytracker_datesetup()
#-----------------------------------------Function 3: User summary------------------------------------------------    
def expenselist():
    global month
    #List of expense
    userpass = ''
    i = 0
    while(not(userpass=='Yes' or userpass=='yes' or userpass=='No' or userpass=='no')):
        userpass = raw_input("View your list of expenses? [Yes-No]: ")
        if (userpass=='Yes' or userpass=='yes' or userpass =='Y'or userpass =='y'):
            while(i == 0):
                viewmonth = input("Which month would you like to view? [1-12]: ")
                if (viewmonth <= 12 and viewmonth > 0):
                    os.system("cls")
                    month = viewmonth
                    #Prints all records from the array
                    print "************************************************"
                    print "List of expenses for", MonthName[month]
                    print "************************************************"
                    print "------------------------------------------------"
                    print "Day \tExpenditures"
                    print "------------------------------------------------"
                    for z in data[month-1]['days']:
                        print(str(z['day'])),
                        v = float(round(z['expense'],2))
                        print ('\t'+('%0.2f' %(v)))
                    print "------------------------------------------------"
                    expenselist_summary()
                    userchoice = ''
                    while(not(userchoice=='Yes' or userchoice=='yes' or userchoice=='No' or userchoice=='no'or userpass =='N'or userpass =='n'or userpass =='Y'or userpass =='y')):
                        userchoice = raw_input(">> Would you like to view another month's list of expense? [Yes-No]: ")
                        if (userchoice=='Yes' or userchoice=='yes'or userpass =='Y'or userpass =='y'):
                            i = 0
                        elif (userchoice=='No' or userchoice=='no'or userpass =='N'or userpass =='n'):
                            os.system("cls")
                            mainmenu()
                else:
                    i = 0
        elif (userpass=='No' or userpass=='no'or userpass =='N'or userpass =='n'):
            os.system("cls")
            mainmenu()
def expenselist_summary():
    TotExp=0
    
    #Balance calculation
    for z in data[month-1]['days']:
        Exp=((int(round(z['expense'],2))))
        TotExp += Exp

    Salary =dataauth[per]['info'][month-1]['salary']
    Goal= dataauth[per]['info'][month-1]['goal']
    Balance = Salary - TotExp #Balance = Salary - Total expense
    
    print ">> Savings goal for",MonthName[month],": RM " + `Goal`
    print "\n>> Monthly salary for",MonthName[month],": RM " + `Salary`
    print ">> Total expenses for",MonthName[month],": RM " + `TotExp`
    print "------------------------------------------------"
    print ">> Total balance for",MonthName[month],": RM " + `Balance`
    print "------------------------------------------------"
    
    if (Balance >= Goal):
        print "\nYou were still within your savings goal!\n"
    else:
        print "\nOh no! You exceeded your savings goal!\n"

def usersummary():
    global Balance
    localtime = time.asctime( time.localtime(time.time()) )
    month=int(datetime.date.today().strftime("%m"))
    success=0
    TotExp=0
    Salary=dataauth[per]['info'][month-1]['salary']
    
    print "************************************************"
    print "Summary of your expenses for", MonthName[month]
    print "************************************************"

    #Balance calculation
    for z in data[month-1]['days']:
        Exp=((int(round(z['expense'],3))))
        TotExp += Exp
    Balance = Salary - TotExp #Balance = Salary - Total expense

   
    #User summary info
    print "\n>> Current savings goal: RM " + `Goal`
    print "\n>> Current monthly salary: RM " + `Salary`
    print ">> Total monthly expenses: RM " + `TotExp`
    print "------------------------------------------------"
    print ">> Total monthly balance: RM " + `Balance`
    print "------------------------------------------------"
    
    #Goal achievement
    if (Balance >= Goal):
        print "\nYou are still within your savings goal!\n"
    else:
        print "\nOh no! You have exceeded your savings goal!\n"

    #List of expenses
    expenselist()

#----------------------------------------------------- Function 4: Currency converter ----------------------------------------------------
majorcountry= ['COUNTRY','AED','ARS','AUD','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HUF','ILS','INR','JPY','KRW','MAD','MXN','NOK','NZD','PHP','PLN','RUB','SEK','SGD','THB','TRY','USD','ZAR']
majorvalue=['RATE','0.84522','3.5706','0.31237','0.73430','0.31547','0.23163','1.5891','5.6251','1.5721','0.21127','0.17756','1.7837','65.873','0.83074','14.882','26.183','260.95','2.2840','4.4048','2.0009','0.33313','11.493','0.89398','13.400','2.0437','0.32446','8.0008','0.83208','0.23015','3.1227']
majorcountryname=['FULLNAME', 'Arab Emirates Dirham', 'Argentine Peso	    ', 'Australian Dollar', 'Brazilian Real	    ', 'Canadian Dollar	    ', 'Swiss Franc	    ', 'Chinese Yuan	    ','Czech Koruna	    ', 'Danish Krone	    ', 'Euro	           ','British Pound Sterling', 'Hong Kong Dollar', 'Hungarian Forint', 'Israeli Sheqel	    ','Indian Rupee	    ','Japanese Yen	    ', 'South Korean Won', 'Moroccan Dirham	    ', 'Mexican Peso	    ', 'Norwegian Krone	    ', 'New Zealand Dollar', 'Philippine Peso	    ', 'Polish Zloty	    ', 'Russian Rouble	    ', 'Swedish Krona	    ','Singapore Dollar','Thai Baht	    ', 'Turkish Lira	    ', 'United States Dollar','South African Rand']#Not done yet

minorcountry= ['COUNTRY','BHD','BOB','CLP','COP','DOP','EGP','IDR','IRR','ISK','JMD','JOD','KES','KWD','LBP','LKR','MYR','NAD','NGN','NPR','OMR','PAB','PEN','PKR','RON','SAR','TWD','UAH','UYU','VEF','VND']
minorvalue=['RATE','0.08654','1.5896','156.10','684.65','10.872','4.1644','3072.0','7464.0','24.393','29.819','0.16318','23.741','0.07006','346.95','35.147','1.00000','3.1227','72.400','23.812','0.08849','0.23015','0.75707','24.114','0.96129','0.86306','6.9577','6.0962','6.4495','2.3015','5231.2']
minorcountryname=['FULLNAME','Baraini Dinar	  ','Bolivian Boliviano','Chilean Peso	  ','Colombian Peso	  ','Dominican Peso	  ','Egyptian Pound	  ','Indonesian Rupiah','Iranian Rial	  ','Icelandic Krona	  ','Jamaican Dollar	  ','Jordanian Dinar	  ','Kenyan Shilling	  ','Kuwaiti Dinar	  ','Lebanese Pound	  ','Sri Lankan Rupee','Malaysian Ringgit','Namibian Dollar	  ','Nigerian Naira	  ','Nepalese Rupee	  ','Omani Rial	     ','Panamanian Balboa','Peruvian Sol	  ','Pakistani Rupee	  ','Romanian Leu	  ','Saudi Riyal	  ','Taiwanese Dollar','Ukraine Hryvnia	  ','Uruguayan Peso	  ','Venezuelan Bolivar','Viatnamese Dong	  ']

exoticcountry= ['COUNTRY','AWG','BAM','BBD','BDT','BGN','BMD','BSD','FJD','GHS','GMD','GTQ','HRK','KHR','LAK','MDL','MGA','MKD','MUR','MVR','PYG','QAR','RSD','SCR','SYP','TND','UGX','XAF','XCD','XOF','XPF']
exoticvalue=['RATE','0.41197','0.41321','0.46030','18.581','0.41321','0.23015','0.23015','0.48312','0.97566','10.625','1.6881','1.5682','932.63','1889.1','4.6941','736.35','13.008','7.9732','3.5345','1283','0.83774','26.009','3.1193','49.324','0.55472','835.29','138.59','0.62140','138.59','25.212']
exoticcountryname=['FULLNAME','Aruban Florin	    ','Convertible Mark','Barbadian Dollar','Bangladeshi Taka','Bulgarian Lev	    ','Bermudian Dollar','Bahamian Dollar	    ','Fijian Dollar	    ','Ghana Cedi	    ','Gambian Dalasi	    ','Guatemalan Quetzal','Croatian Kuna	    ','Cambodian Riel	    ','Lao Kip	         ','Moldovan Leu	    ','Malagasy Ariary	    ','Macedonian Denar','Mauritian Rupee	    ','Maldivian Rufiyaa','Paraguayan Guarani','Qatari Riyal	    ','Serbian Dinar	    ','Seychellois Rupee','Syrian Pound	    ','Tunisian Dinar	    ','Ugandan Shilling','Central African Franc','East Caribbean Dollar','West African Franc','CFP Franc	    ']

currencylist = [majorcountry, majorcountryname, majorvalue, minorcountry, minorcountryname, minorvalue, exoticcountry, exoticcountryname, exoticvalue] 

#---------------------------------------------------- Function 4.1: Exchange rate list ----------------------------------------------------    
def majorcountryrate():
    print "************************************************\nMajor Countries Exchange Rate\n************************************************"
    print "\n-----------------------------------------------------\nNo\t  Currencies\t                    Rate\n-----------------------------------------------------"
    for i in range(1,31,1):
        print `i` +"\t  "+currencylist[0][i]+" - "+currencylist[1][i]+"\t    "+currencylist[2][i]
    print "-----------------------------------------------------"
    userleave = raw_input("\nPress ENTER to go back...")
    if (userleave==""):
        os.system("cls")
        exchangeratemenu()
        
def minorcountryrate():
    print "************************************************\nMinor Countries Exchange Rate\n************************************************"
    print "\n-----------------------------------------------------\nNo\t  Currencies\t                    Rate\n-----------------------------------------------------"
    for i in range(1,31,1):
       print i,"" +"\t  "+currencylist[3][i]+" - "+currencylist[4][i]+"\t    "+currencylist[5][i] 
    print "-----------------------------------------------------"
    userleave = raw_input("\nPress ENTER to go back...")
    if (userleave==""):
        os.system("cls")
        exchangeratemenu()
      
def exoticcountryrate():
    print "************************************************\nExotic Countries Exchange Rate\n************************************************"
    print "\n-----------------------------------------------------\nNo\t  Currencies\t                    Rate\n-----------------------------------------------------"
    for i in range(1,31,1):
        print i,"" +"\t  "+currencylist[6][i]+" - "+currencylist[7][i]+"\t    "+currencylist[8][i]  
    print "-----------------------------------------------------"
    userleave = raw_input("\nPress ENTER to go back...")
    if (userleave==""):
        os.system("cls")
        exchangeratemenu()

def exchangeratemenu():
    print "************************************************\nExchange Rates\n************************************************"
    print "\n1. Major currencies\n2. Minor currencies\n3. Exotic currencies\n4. Back"
    usercontinue = ''
    while (not(usercontinue =='1' or usercontinue =='2' or usercontinue == '3' or usercontinue =='4')):
        usercontinue = raw_input("\n>> Which list of currencies would you like to view? [1-4]: ")
        if (usercontinue == '1'):
            os.system("cls")
            majorcountryrate()
        elif (usercontinue == '2'):
            os.system("cls")
            minorcountryrate()
        elif (usercontinue == '3'):
            os.system("cls")
            exoticcountryrate()
        elif (usercontinue == '4'):
            os.system("cls")
            convertermenu()
#---------------------------------------------------- Function 4.2: Converter calculator ----------------------------------------------------             
def convertercalculation():
    print "************************************************\n Currency Converter Calculator\n************************************************"
    print "\n--------------------------------------------------------------------------\n|No|\tMajor currencies  |No|\tMinor currencies  |No|\tExotic currencies\n--------------------------------------------------------------------------"
    for i in range(1,31,1):
        a = 0+i
        b = 30+i
        c = 60+i
        print "|"+`a`+"|\t"+currencylist[0][i]+" - "+currencylist[2][i]+"\t  |"+`b`+"|\t"+currencylist[3][i]+" - "+currencylist[5][i]+"\t  |"+`c`+"|\t"+currencylist[6][i]+" - "+currencylist[8][i]
    print "--------------------------------------------------------------------------"
    userpass=""
    while(not (userpass=="Yes" or userpass =="yes" or userpass == "No" or userpass == "no")):
        userpass = raw_input("Need reference list for the currency names? [Yes-No]: ")
        if (userpass=="Yes" or userpass=="yes"):
            reference()
        elif (userpass=="No" or userpass=="no"):
            print "\nFrom: MYR - Malaysian Ringgit"
            h = 0
            while(h == 0):
                userchoice = input("Choose a currency [1 - 90]: ")
                if (userchoice > 0 and userchoice < 91):
                    if (userchoice <= 30):
                        k = userchoice
                        print "To:",currencylist[0][k],"-",currencylist[1][k]
                    elif (userchoice <= 60):
                        k = userchoice - 30
                        print "To:",currencylist[3][k],"-",currencylist[4][k]
                    else:
                        k = userchoice - 60
                        print "To:",currencylist[6][k],"-",currencylist[7][k]
                    usermoney = input("\n>> Amount of money: ")
                    if (userchoice <= 30):
                        j = userchoice
                        rate = currencylist[2][j]
                        rate = float(rate)
                        userexchange = rate * usermoney
                        userexchange = "%.2f" % userexchange 
                        userexchangereverse = usermoney / rate
                        userexchangereverse = "%.2f" % userexchangereverse 
                        print "\n>> Results :"
                        print "         >>", usermoney,"MYR = ",userexchange, currencylist[0][j]
                        print "         >>", usermoney,currencylist[0][j], "= ",userexchangereverse," MYR "
                        h = 1
                    elif (userchoice <= 60):
                        j = userchoice - 30
                        rate = currencylist[5][j]
                        rate = float(rate)
                        userexchange = rate * usermoney
                        userexchange = "%.2f" % userexchange 
                        userexchangereverse = usermoney / rate
                        userexchangereverse = "%.2f" % userexchangereverse 
                        print "\n>> Results :"
                        print "         >>", usermoney,"MYR = ",userexchange, currencylist[3][j]
                        print "         >>", usermoney,currencylist[3][j],"= ",userexchangereverse," MYR "
                        h = 1
                    else:
                        j = userchoice - 60
                        rate = currencylist[8][j]
                        rate = float(rate)
                        userexchange = rate * usermoney
                        userexchange = "%.2f" % userexchange 
                        userexchangereverse = usermoney / rate
                        userexchangereverse = "%.2f" % userexchangereverse 
                        print "\n>> Results :"
                        print "         >>", usermoney,"MYR = ",userexchange, currencylist[6][j]
                        print "         >>", usermoney,currencylist[6][j],"= ",userexchangereverse," MYR"
                        h = 1
                else:
                    h = 0
            print "--------------------------------------------------------------------------" 
            print "\n1. Convert another amount\n2. Back"
            proceed = ''
            while not(proceed == '1' or proceed =='2'):
                proceed = raw_input("\n>> Where would you like to proceed to? [1-2]: ")
                if (proceed=='1'):
                    os.system("cls")
                    convertercalculation()
                elif (proceed == '2'):
                    os.system("cls")
                    convertermenu()
#----------------------------------- Function 4.2.1: Currency reference list  ----------------------------------------------------             
def reference():					
    print "************************************************\nReference List for Currencies' Short Forms\n************************************************"
    print "\n1. List for major currencies\n2. List for minor currencies\n3. List for exotic currencies\n4. Back"
    usercontinue= ''
    while not(usercontinue == '1' or usercontinue =='2' or usercontinue =='3' or usercontinue =='4'):
        usercontinue = raw_input("\n>> Which reference list would you to view? [1-4]: ")
        if (usercontinue=='1'):
            os.system("cls")
            refmaj()
        elif (usercontinue == '2'):
            os.system("cls")
            refmin()
        elif (usercontinue == '3'):
            os.system("cls")
            refexo()
        elif (usercontinue == '4'):
            os.system("cls")
            convertercalculation()
           
def refmaj():
    print "************************************************\nReference List for Major Currencies\n************************************************"
    print "\n--------------------------------------\nNo\tMajor Currencies\n--------------------------------------"
    for i in range(1,31,1):
        print `i` + "\t"+currencylist[0][i]+" - "+currencylist[1][i]
    print "------------------------------------------------"
    usercontinue = raw_input("\n>> Press ENTER to continue...")
    if (usercontinue==''):
        os.system("cls")
        reference()
   
def refmin():
    print "************************************************\nReference List for Minor Currencies\n************************************************"
    print "\n--------------------------------------\nNo\tMinor Currencies\n--------------------------------------"
    for i in range(1,31,1):
        print `i`+"\t"+currencylist[3][i]+" - "+currencylist[4][i]
    print "--------------------------------------"
    usercontinue = raw_input("\n>> Press ENTER to continue...")
    if (usercontinue==''):
        os.system("cls")
        reference()
#-----------------------------------------------------------------------------------------------------------------------    
def refexo():
    print "************************************************\nReference List for Exotic Currencies\n************************************************"
    print "\n--------------------------------------\nNo\tExotic Currencies\n--------------------------------------"
    for i in range(1,31,1):
        print `i`+"\t"+currencylist[6][i]+" - "+currencylist[7][i]
    print "--------------------------------------"
    usercontinue = raw_input("\n>> Press ENTER to continue...")
    if (usercontinue==''):
        os.system("cls")
        reference()    
#----------------------------------- Function 4.3: Currency converter menu ----------------------------------------------------  
def convertermenu():
    print "************************************************\nWelcome to Currency Converter\n************************************************"
    print "\n1. Currency converter calculator \n2. Currency exchange rate\n3. Back"
    proceed = ''
    while not(proceed == '1' or proceed =='2' or proceed =='3'):
        proceed = raw_input("\n>> Which page would you like to proceed to? [1-3]: ")
        if (proceed == '1'):
            os.system("cls")
            convertercalculation()
        elif (proceed == '2'):
            os.system("cls")
            exchangeratemenu()
        elif (proceed == '3'):
            os.system("cls")
            mainmenu()
            
#---------------------------------------------------- Function 5: Main Menu ----------------------------------------------------  
def mainmenu():
    i = 0
    global Exp
    print "************************************************\nMoney Management Menu\n************************************************"
    print "\n1. Update user info\n2. Update expenses\n3. View user summary\n4. Currency converter\n5. Sign out\n"
    while (i == 0):
        Page = input(">> Which page would you like to proceed to? [1-5]: ") #Which page user would like to view
        if (Page==1):
            os.system("cls") 
            userinfo()
        elif (Page == 2):
            os.system("cls")
            moneytracker_date()
        elif (Page == 3):
            os.system("cls")
            i = 1
            usersummary()
        elif (Page == 4):
            os.system("cls")
            convertermenu()
        elif (Page == 5):
            os.system("cls")
            print "You have successfully signed out!"
            UserLeave = raw_input("\n>> Press ENTER to continue...")
            if (UserLeave==""):
                os.system("cls")
                startmenu()
        else:
            i = 0
            
#--------------------------------------------------------------------------------------------------------------------------  
startmenu() #Main module
