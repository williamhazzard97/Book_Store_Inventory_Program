#Set global variable to hold lists of book records
bookInventory = []

#Define the menu function
def menu():
    print("|-------------------------------------------|")
    print("|       BOOK STORE INVENTORY PROGRAM        |")
    print("|-------------------------------------------|")
    print("[1] Display all books & Summary Report")
    print("[2] Average Price Report")
    print("[3] Genre Stock Report")
    print("[4] Add New Book")
    print("[5] Search Book Titles")
    print("[6] Sort Books A-Z (Title or Genre)")
    print("[7] Graph of Book Genres in Stock")
    print("[8] Quit")

#Define a function to read the data in from the txt file
def readBookData():
    bookDataFile = open('book_store_inventory_data.txt', 'r')

    #Loop through the txt file and create a list for each row of data
    #and append each list to the global variable book inventory 
    for row in bookDataFile:
        bookRecord = []
        startPos = 0
        if not row.startswith('#'):
            for index in range(len(row)):
                if row[index] == ',' or index == len(row) -1:
                    bookRecord.append(row[startPos:index].rstrip())
                    startPos = index + 1
            bookInventory.append(bookRecord)

    bookDataFile.close()

#Define a function to print the entire book inventory in a table format
def printBookInventory():
    
    print('Author','      ','Title','      ','Format','      ','Publisher','      ','Cost','      ','Stock','      ','Genre')
    print('-' * 100)

    #Loop through fields within rows in book inventory list and print each field 
    for bookRecord in bookInventory:
        for field in bookRecord:
            print(field, '\t', end='')
        print()

#Define a function to calculate the total amount of book titles
def totalBookTitles():
    for bookRecord in bookInventory:
        if bookRecord[5] != 0:
            totalBooks = len(bookInventory)

    print('\nTotal Number of Book Titles (in stock): ', totalBooks)

#Define a function that will calculate the total value of books in stock
def totalBooksValue():
    totalValue = 0

    for bookRecord in bookInventory:
        if bookRecord[5] != 0:
            totalValue += (float(bookRecord[4])*int(bookRecord[5]))

    print('\nTotal Value of Books (in stock): £{:.2f}'.format(totalValue))

#Define a function that will calculate the average price of books in stock
def averageBookPrice():
    totalBookPrices = 0

    for bookRecord in bookInventory:
        if bookRecord[5] != 0:
            totalBookPrices += (float(bookRecord[4]))

    averagePrice = totalBookPrices/len(bookInventory)

    print('\nAverage Price of Books (in stock): £{:.2f}'.format(averagePrice))

#Define a function that produces a report detailing the number of books in each genre
def genreReport():
    genreList = ['Fiction:','Biography:','Science:','Religion:']
    fictionCount = 0
    biographyCount = 0
    scienceCount = 0
    religionCount = 0

    
    for bookRecord in bookInventory:
        if bookRecord[5] != 0 and 'iction' in bookRecord[6]:
            fictionCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'iography' in bookRecord[6]:
            biographyCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'cience' in bookRecord[6]:
            scienceCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'eligion' in bookRecord[6]:
            religionCount += (int(bookRecord[5]))
        else:
            print('Error counting genre stocks')

    print("\nGenre Stock Levels: ")
    print()
    print(genreList[0],fictionCount)
    print(genreList[1],biographyCount)
    print(genreList[2],scienceCount)
    print(genreList[3],religionCount)

#Define a function to add book records to book inventory
def addBookRecord():
    print('\nEnter the Details of the New Book')
    newAuthor = str(input('\nAuthor: '))
    newTitle = str(input('\nBook Title: '))
    newFormat = str(input('\nFormat (hb/pb): '))
    newPublisher = str(input('\nPublisher: '))
    newCost = float(input('\nCost: £'))
    newStock = int(input('\nStock Level: '))
    newGenre = str(input('\nGenre: '))

    newBookRecord = [newAuthor, newTitle, newFormat, newPublisher, newCost, newStock, newGenre]

    bookInventory.append(newBookRecord)

    totalBookTitles()
    averageBookPrice()

#Define a function that will search for book titles and alter stock levels accordingly 
def searchBooks():
    print('\nSearch for Book Titles in Inventory')
    bookQuery = str(input('\nEnter Book Title: '))

    #Loop through book records in the book inventory to find a book title that matches the search query
    for bookRecord in bookInventory:
        if bookQuery != '' and bookQuery.lower() in bookRecord[1].lower() and bookRecord[5] != 0:
            print('\nBook Title:',bookRecord[1])
            print('Status: Available')
            print('Stock Level:', bookRecord[5])
            searchOption = str(input('\nPress "S" to make a sale or press "A" to add stock: \n'))
            if searchOption != '' and searchOption == 'S' or searchOption == 's':
                bookRecord[5] = int(bookRecord[5]) - 1
                print('\nNew Stock Level:', bookRecord[5])
            elif searchOption != '' and searchOption == 'A' or searchOption == 'a':
                addStock = int(input('\nEnter how many books to be added to the stock level: '))
                bookRecord[5] = int(bookRecord[5]) + int(addStock)
                print('\nNew Stock Level:', bookRecord[5])
            else:
                print('Invalid Operation')
        elif bookQuery != '' and bookQuery.lower() in bookRecord[1].lower() and bookRecord[5] == 0:
            print(bookRecord[1])
            print('\nStatus: Unavailable', '\nStock Level:', bookRecord[5])

#Define a function that will arrange the book inventory by title or genre in a tabular format        
def sortBooks():
    print('\nSort Books (A-Z) by Title or Genre')
    sortType = str(input('Press "T" to sort by title or press "G" to sort by genre: \n'))

    print('Author','      ','Title','      ','Format','      ','Publisher','      ','Cost','      ','Stock','      ','Genre')
    print('-' * 100)
    if sortType != '' and sortType == 'T' or sortType == 't':
        bookInventory.sort(key=lambda x: x[1])
        for bookRecord in bookInventory:
            for field in bookRecord:
                print(field, '\t', end='')
            print()
    elif sortType != '' and sortType == 'G' or sortType == 'g':
        bookInventory.sort(key=lambda x: x[6])
        for bookRecord in bookInventory:
            for field in bookRecord:
                print(field, '\t', end='')
            print()
    else:
        print('Invalid Operation')

#Define a function that will present a bar chart representing genres and their stock levels
def genreGraph():
    fictionCount = 0
    biographyCount = 0
    scienceCount = 0
    religionCount = 0
    
    for bookRecord in bookInventory:
        if bookRecord[5] != 0 and 'iction' in bookRecord[6]:
            fictionCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'iography' in bookRecord[6]:
            biographyCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'cience' in bookRecord[6]:
            scienceCount += (int(bookRecord[5]))
        elif bookRecord[5] != 0 and 'eligion' in bookRecord[6]:
            religionCount += (int(bookRecord[5]))

    print('\nBar Chart Representing Book Genre Stock Levels: \n')
    print('Fiction:','\t','>' * fictionCount, ' ', fictionCount)
    print('Biography:','\t','>' * biographyCount, ' ', biographyCount)
    print('Science:','\t','>' * scienceCount, ' ', scienceCount)
    print('Religion:','\t','>' * religionCount, ' ', religionCount)

#Call the menu function to display to users
menu()

#Prompt the user to input a menu option
menuOption = int(input("\nSelect an option to continue: \n"))

#Call the function to read the data from the txt file
readBookData()

#Use a loop to implement the menu functionality 
while menuOption != 8:
    if menuOption == 1:
        print("All books in inventory: \n")
        printBookInventory()
        print("\nSummary Report: ")
        totalBookTitles()
        totalBooksValue()
    elif menuOption == 2:
        averageBookPrice()
    elif menuOption == 3:
        genreReport()
    elif menuOption == 4:
        addBookRecord()
    elif menuOption == 5:
        searchBooks()
    elif menuOption == 6:
        sortBooks()
    elif menuOption == 7:
        genreGraph()
    else:
        print("Invalid Menu Selection")

    #Call the menu function again so users can perform another operation
    menu()
    menuOption = int(input("\nSelect an option to continue: \n"))

print("Thank you for using the book store inventory.")
exit()
