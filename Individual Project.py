# List of customers [[ID, name, gender, phone]]
lst_customers = [
    [1, "Tom", "Male", 1234], [2, "Jerry", "Male", 1235],
    [3, "Marie", "Female", 2345], [4, "Lisa", "Female", 2346],
    [5, "Donald", "Male", 1236], [6, "Butch", "Male", 1237]
]
# List of books [[ID, name, type, price, quantity]]
lst_books = [
    [1, "Game of Throne", "Novel", 3, 100], [2, "Kingdom", "Novel", 2, 100],
    [3, "Basic statistics", "Math", 7, 100], [4, "Fundamental Physics", "Physics", 4, 100],
    [5, "Linear Algebra", "Math", 1, 100], [6, "Spectrocopy", "Physics", 9, 100],
]
# List of transactions [(customer ID, book ID, amount, total price, day, month, year)]
lst_transactions = [
    [1, 2, 2, 4, 1, 10, 2020], [2, 1, 5, 10, 1, 9, 2020],
    [3, 3, 4, 15, 1, 8, 2020], [1, 4, 10, 9, 1, 7, 2020],
    [3, 5, 1, 10, 1, 6, 2020], [4, 2, 5, 10, 1, 5, 2020],
    [5, 2, 10, 30, 1, 1, 2021]
]

def get_customer(id):
    """
    This function return the position of the customer with id in the list of
customers
    :param id: id of customer we want to search for
    :return:    -1 (customer does not exist),
                otherwise return the position of that customer in the list
    """
    for i in range(len(lst_customers)):
        itemi = lst_customers[i]
        if id == itemi[0]:
            return i
    return -1
def get_book(id):
    """
    This function return the position of the book with id in the list of books
    :param id: id of book we want to search for
    :return:    -1 (book does not exist),
                otherwise return the position of that book in the list
    """
    for i in range(len(lst_books)):
        itemi = lst_books[i]
        if id == itemi[0]:
            return i
    return -1

def show_all_info():
    """
    This function shows the lists of customers, books and transactions.
    It is very useful for testing the correctness of program by hand
    """
    print("\n")
    print("BOOKS : ", lst_books)
    print("CUSTOMERS : ", lst_customers)
    print("TRANSACTIONS : ", lst_transactions)

def feature_1_show_customer():
    """
    The purpose of this feature is to show the information of a customer
    """

    # user enters ID to see if customer exists
    customer_id = int(input("Please enter ID of a customer = "))

    # get the position of the customer
    pos = get_customer(customer_id)

    # if customer does not exist
    if pos == -1:
        print("We do not have a customer with that ID.")
    else:
        item = lst_customers[pos]
        print("We have a customer with that ID: \n", item)

def feature_2_add_book():
    """
    The purpose of this feature is to show the information of a customer
    """

    # user enters ID of a book
    book_id = int(input("Please enter the ID of a book = "))
    book_name = str(input("Please enter name of book = "))
    book_type = str(input("Please enter type of book = "))
    book_price = int(input("Please enter price of book = "))
    book_total_amount = int(input("Please enter total amount of book = "))

    # get position of the book if possible
    pos = get_book(book_id)

    if pos == -1:
        lst_books.append(book_id, book_name, book_type, book_price, book_total_amount)
    else:
        lst_books[pos][1] = book_name
        lst_books[pos][2] = book_type
        lst_books[pos][3] = book_price
        lst_books[pos][4] = book_total_amount

def feature_3_add_transaction():
    """
    The purpose of this feature is to show the information of a customer
    """
    # getting all of the customers details
    customer_id = int(input("Please enter your customer ID = "))
    book_id = int(input("Please enter the ID of the book you have purchased = "))
    no_books = int(input("Please enter the number of books you have purchased = "))
    date_day = int(input("Please enter the day you have purchased this on on = "))
    date_month = str(input("Please enter the month you have purchased this book on = "))
    date_year = int(input("Please enter the year you have purchased this book on in (2000) format = "))

    # getting customer ID position
    pos_customer = get_customer(customer_id)
    # getting book ID position
    pos_book = get_book(book_id)

    # if the book ID doesn't exist
    if pos_book == -1:
        print("That book ID doesn't exist, please select from the main menu and enter the correct details. \n")
        show_all_info()

    # if the customer ID doesn't exist
    elif pos_customer == -1:
        print("That customer ID doesn't exist, please select from the main menu and enter the correct details. \n")
        show_all_info()

    # if both the book ID and customer ID do exist
    if pos_book != -1 and pos_customer != -1:
        # if the customer has tried to purchase too many books
        if no_books > lst_books[pos_book][4]:
            print("There is not enough books of that category so the transaction can not be completed.")

        # if the customer has did everything ok, this runs the transaction
        elif no_books <= lst_books[pos_book][4]:
            lst_books[pos_book][4] = lst_books[pos_book][4] - no_books
            lst_books.append(customer_id, book_id, no_books, date_day, date_month, date_year)
            # discount amount if the amount of books purchased is over 20
            discount = 0.90
            # standard price (no discount)
            if no_books < 20:
                final_price = no_books * lst_books[pos_book][3]

                # if the no. of books purchased is over 20 then the final price is calculated with the discount
                if no_books >= 20:
                    final_price = no_books * lst_books[pos_book][3] * discount
                print("The final price for the books is = ", final_price)

def feature_4_count_book_type():
    """
    The purpose of this feature is to show the information of a customer
    """
    book_type = str(input("Please enter a book type = "))

    # sum for the total cost of the books before working out the average
    sum = 0
    # counter is for counting how many books there are of that type
    counter = 0

    for i in range(len(lst_books)):
        itemi = lst_books[i]
        if book_type == itemi[2]:
            counter += 1
            book_price = lst_books[book_type][3]


    average_price = book_price / counter
    print(average_price, counter)

def feature_5_total_books_purchased_bycustomer():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")
    print("This is feature 2, I will implement it later")

def feature_6_purchases_books_by_type():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")

def feature_7_best_customer_by_purchases():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")

def feature_8_total_purchases_by_year():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")

def feature_9_worst_book():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")

def feature_10_compare_male_female():
    """
    The purpose of this feature is to show the information of a customer
    """
    print("This is feature 2, I will implement it later")

def feature_11_show_book():
    """
    Show all information of a book
    """
    bookid = int(input("Enter a book id: "))
    # get the position in the list of book
    pos = get_book(bookid)
    # if the book does not exist
    if pos == -1:
        print("We do not have a book with id ", bookid)
    # if the book exists
    else:
        item = lst_books[pos]
        print("Name : ", item[1], " Type : ", item[2], " Price : ", item[3], " Quantity : ", item[4])
def feature_12_add_customer():
    """
    Add a customer to the list
    """
    id = int(input("Enter ID : "))
    name = input("Enter name : ")
    gender = input("Enter gender (Male \ Female) : ")
    phone = int(input("Enter phone : "))
    pos = get_customer(id)
    # if customer is new
    if pos == -1:
        lst_customers.append([id, name, gender, phone])
    # if the customer is existing
    else:
        lst_customers[pos] = [id, name, gender, phone]

message = """
--- The book Shop program written by Ruairi ---
Feature 1: Show a customer
Feature 2: Add a book
Feature 3: Add transaction
Feature 4: Count book by type
Feature 5: Purchases by customer
Feature 6: Purchases books by type
Feature 7: Best customers
Feature 8: Total purchases by year
Feature 9: Find the worst book
Feature 10: Compare male and female customers
Feature 11: Show book
Feature 12: Add customer
...
0: Exit program 
"""
# repeatedly run the main menu
while (True):
    # for testing purpose only
    show_all_info()
    # print out all possible choices to users
    print(message   )
    # ask the user to select a choice
    x = int(input("Please enter your choice as indicated above: "))
    # get the choice and choose appropriate action
    if x == 1:
        feature_1_show_customer()
    elif x == 2:
        feature_2_add_book()
    elif x == 3:
        feature_3_add_transaction()
    elif x == 4:
        feature_4_count_book_type()
    elif x == 5:
        feature_5_total_books_purchased_bycustomer()#
    elif x == 6:
        feature_6_purchases_books_by_type()
    elif x == 7:
        feature_7_best_customer_by_purchases()
    elif x == 8:
        feature_8_total_purchases_by_year()
    elif x == 9:
        feature_9_worst_book()
    elif x == 10:
        feature_10_compare_male_female()
    elif x == 11:
        feature_11_show_book()
    elif x == 12:
        feature_12_add_customer()
    else:
        print("Exiting program...")
        break # to stop the while loop

