from db_pool.mysqlhelper import MySqLHelper
import random
import math

db = MySqLHelper()

SQL_customer_order_LIST = []
SQL_orderdetail_LIST = []
SQL_order_medicine_LIST = []
SQL_pharmacy_order_LIST = []

# Get all pharmacy
# NOTHING TO DO HERE SINCE IT IS TOO EASY

# Get all medicine price
all_medicine_price_dict = {}
SQL_ALL_MEDICINE_PRICE = "SELECT `medicine_sku`, `price` FROM medicine"
all_medicine_price = db.selectall(sql=SQL_ALL_MEDICINE_PRICE)
for medicine in all_medicine_price:
    thisSKU = list(medicine)[0].decode("utf-8")
    thisPrice = list(medicine)[1]
    all_medicine_price_dict[thisSKU] = thisPrice
print(all_medicine_price_dict)

# Get all customer id
# [{USER1_ID, USER_INSURANCE1_ID}, {[}USER2_ID, USER_INSURANCE2_ID},...]
all_customer_list = []
SQL_ALL_USER = "SELECT `customer_id`, customer.insurance_id, insurance.discount_rate FROM customer \
INNER JOIN customer_insurance ON customer.insurance_id = customer_insurance.insurance_id \
INNER JOIN insurance ON customer_insurance.company_id = insurance.company_id"
all_customer = list(db.selectall(sql=SQL_ALL_USER))
for item in all_customer:
    item = list(item)
    item[1] = item[1].decode("utf-8")
    currentUser = {"customer_id": item[0], "insurance_id": item[1], "discount_rate": item[2]}
    all_customer_list.append(currentUser)
print(all_customer_list)

# Find prescription
for user in all_customer_list:
    SQL_ALL_SKU_OF_USER = "SELECT `medicine_sku` FROM prescription WHERE `customer_id` = '{}'"
    SQL_ALL_SKU_OF_USER = SQL_ALL_SKU_OF_USER.format(str(user["customer_id"]))
    # print(SQL_ALL_SKU_OF_USER)
    all_prescription_of_user = list(db.selectall(sql=SQL_ALL_SKU_OF_USER))
    numberOfMedicineInThisOrder = random.randint(1, len(all_prescription_of_user))
    # print(numberofMedicineInThisOrder)
    MedicineIndexInThisOrder = random.sample(range(0, len(all_prescription_of_user)), numberOfMedicineInThisOrder)
    # print(MedicineIndexInThisOrder)
    for medicineIndex in MedicineIndexInThisOrder:
        print("=" * 30)
        print("Start of an order")

        # Random time from 10/01/2021 12:00am - 10/10/2021 11:59pm GMT-8
        randomTime = str(random.randint(1633071600, 1633892399))

        # Generate Order ID
        random_ID = ""
        for j in range(16):
            randomNumber = random.randint(0, 9)
            random_ID += str(randomNumber)
        ThisOrderID = random_ID[0:8] + randomTime + random_ID[9:16]
        print("Order ID:", ThisOrderID)

        # Generate SQL for Table 'customer_order'
        customer_order_SQL = "INSERT INTO `customer_order` (`customer_id`, `order_id`) VALUES ('{}', '{}');"
        customer_order_SQL = customer_order_SQL.format(str(user["customer_id"]), ThisOrderID)
        #print("customer_order SQL: " + customer_order_SQL)
        SQL_customer_order_LIST.append(customer_order_SQL)

        # Generate pharmacy for order
        randomPharmacyID = str(random.randint(1, 5))
        print("Order store ID: " + randomPharmacyID)

        # Generate SQL for Table 'pharmacy_order'
        pharmacy_order_SQL = "INSERT INTO `pharmacy_order` (`store_id`, `order_id`) VALUES ('{}', '{}');"
        pharmacy_order_SQL = pharmacy_order_SQL.format(randomPharmacyID, ThisOrderID)
        #print("customer_order SQL: " + pharmacy_order_SQL)
        SQL_pharmacy_order_LIST.append(pharmacy_order_SQL)

        AmountOfThisMedicine = random.randint(1, 3)
        thisMedicineSKU = list(all_prescription_of_user[medicineIndex])[0].decode("utf-8")
        print(str(user["customer_id"]) + " Ordered " + str(AmountOfThisMedicine), thisMedicineSKU, "at", randomTime)

        # Generate SQL for table 'order_medicine'
        order_medicine_SQL = "INSERT INTO `order_medicine` (`order_id`, `medicine_sku`, `amount`) VALUES ('{}', '{}', '{}');"
        order_medicine_SQL = order_medicine_SQL.format(ThisOrderID, thisMedicineSKU, str(AmountOfThisMedicine))
        #print("order_medicine_SQL: " + order_medicine_SQL)
        SQL_order_medicine_LIST.append(order_medicine_SQL)

        # Calculate price
        thisMedicineUnitPrice = all_medicine_price_dict[thisMedicineSKU]
        thisMedicinePrice = thisMedicineUnitPrice * int (AmountOfThisMedicine)
        print("This medicine price: " + str(thisMedicinePrice))

        if len(all_prescription_of_user) > 1:
            secretRandom = random.randint(1, 2)
            if secretRandom == 2:
                anotherMedicineIndex = math.ceil((len(all_prescription_of_user) - 1) / 2)
                anotherMedicineSKU = list(all_prescription_of_user[anotherMedicineIndex])[0].decode("utf-8")
                if anotherMedicineSKU != thisMedicineSKU:
                    AmountOfAnotherMedicine = random.randint(1, 3)
                    print(str(user["customer_id"]) + " Ordered " + str(AmountOfThisMedicine), anotherMedicineSKU, "at", randomTime)

                    # Generate SQL for table 'order_medicine'
                    order_medicine_SQL = "INSERT INTO `order_medicine` (`order_id`, `medicine_sku`, `amount`) VALUES ('{}', '{}', '{}');"
                    order_medicine_SQL = order_medicine_SQL.format(ThisOrderID, anotherMedicineSKU, str(AmountOfAnotherMedicine))
                    #print("order_medicine_SQL: " + order_medicine_SQL)
                    SQL_order_medicine_LIST.append(order_medicine_SQL)

                    # Calculate price
                    anotherMedicineUnitPrice = all_medicine_price_dict[anotherMedicineSKU]
                    anotherMedicinePrice = anotherMedicineUnitPrice * int(AmountOfAnotherMedicine)
                    print("Another medicine price: " + str(anotherMedicinePrice))

        # Calculate total price and generate SQL for Table 'orderdetail'
        print("Discount rate = :" + str(user["discount_rate"]))
        try:
            total_price = thisMedicinePrice + anotherMedicinePrice
        except:
            total_price = thisMedicinePrice
        print("Total price before discount:" + str(total_price))
        total_price = round(total_price * float(int(user["discount_rate"]) / 100), 2)
        print("Total price after discount:" + str(total_price))
        orderdetail_SQL = "INSERT INTO `orderdetail` (`order_id`, `order_time`, `order_price`, `tax`, `final_total`, `status`) VALUES ('{}', FROM_UNIXTIME('{}'), '{}', '{}', '{}', '{}');"
        orderdetail_SQL = orderdetail_SQL.format(ThisOrderID, randomTime, str(total_price), str(0), str(total_price), "finished")
        #print("orderdetail_SQL: " + orderdetail_SQL)
        SQL_orderdetail_LIST.append(orderdetail_SQL)

print("=" * 50)
print("customer_order SQL:")
for item in SQL_customer_order_LIST:
    print(item)
print("=" * 50)
print("orderdetail SQL:")
for item in SQL_orderdetail_LIST:
    print(item)
print("=" * 50)
print("order_medicine SQL:")
for item in SQL_order_medicine_LIST:
    print(item)
print("=" * 50)
print("pharmacy_order SQL:")
for item in SQL_pharmacy_order_LIST:
    print(item)