from db_pool.mysqlhelper import MySqLHelper
import random

db = MySqLHelper()

# Get all customer id
all_customer_list = []
SQL_ALL_USER = "SELECT customer_id FROM customer"
all_customer = db.selectall(sql=SQL_ALL_USER)
all_customer = list(all_customer)
for item in all_customer:
    item = list(item)
    all_customer_list.append(item[0])
print(all_customer_list)

# Get all medicine id
all_medicine_list = []
SQL_ALL_medicine = "SELECT medicine_sku FROM medicine"
all_medicine = db.selectall(sql=SQL_ALL_medicine)
all_medicine = list(all_medicine)
for item in all_medicine:
    item = list(item)
    all_medicine_list.append(item[0].decode("utf-8"))
print(all_medicine_list)

for customer in all_customer_list:
    numberofMedicine = random.randint(2, 5)
    #print("numberofMedicine:", numberofMedicine)
    medicineIndex = random.sample(range(0, len(all_medicine_list)), numberofMedicine)
    #print("medicineIndex:", medicineIndex)
    for j in medicineIndex:
        #print("Add", all_medicine_list[j], "to customer ID:", str(customer))
        SQL_prescription_generator = "INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('{}', '{}');"
        SQL_prescription_generator = SQL_prescription_generator.format(str(customer), all_medicine_list[j])
        print(SQL_prescription_generator)

"""
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('111', 'LZAQFRFRL38K');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('111', 'HTQEBULS304F');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('108', '7SVF64IVF2ZY');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('108', 'HTQEBULS304F');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('108', 'LZAQFRFRL38K');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('108', '6HZFQ847PK0T');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('108', '45Z11J0BASMK');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('107', 'FWR4F1VYAJTW');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('107', 'UQDE1NHIT0H3');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('104', '45Z11J0BASMK');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('104', '7KINPC321XTR');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('104', 'HTQEBULS304F');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('104', 'FWR4F1VYAJTW');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('109', 'YXE4BA0B49OF');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('109', '37A8QSOPSPTV');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('103', '6HZFQ847PK0T');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('103', '45Z11J0BASMK');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('103', 'E59FCNY5ILRY');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('103', '7KINPC321XTR');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('103', '56XC3HZMA343');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('110', '56XC3HZMA343');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('110', 'LZAQFRFRL38K');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('110', 'FWR4F1VYAJTW');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('110', '37A8QSOPSPTV');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('106', 'HTQEBULS304F');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('106', '37A8QSOPSPTV');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('106', '8ACIORIGSR0Y');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('106', '45Z11J0BASMK');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('112', '7SVF64IVF2ZY');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('112', '6HZFQ847PK0T');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('112', '56XC3HZMA343');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('112', '45Z11J0BASMK');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('112', 'UQDE1NHIT0H3');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('105', '6HZFQ847PK0T');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('105', '37A8QSOPSPTV');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('105', 'FWR4F1VYAJTW');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('105', 'UQDE1NHIT0H3');
INSERT INTO `prescription` (`customer_id`, `medicine_sku`) VALUES ('105', 'E59FCNY5ILRY');
"""