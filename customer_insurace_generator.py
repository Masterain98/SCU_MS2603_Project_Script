from db_pool.mysqlhelper import MySqLHelper
import random

db = MySqLHelper()

# Get all customer id
all_customer_list = []
SQL_ALL_USER = "SELECT insurance_id FROM customer"
all_customer = db.selectall(sql=SQL_ALL_USER)
all_customer = list(all_customer)
for item in all_customer:
    item = list(item)
    all_customer_list.append(item[0].decode("utf-8"))
print(all_customer_list)

# Get all insurance company id
all_insurance_list = []
SQL_ALL_insurance = "SELECT company_id FROM insurance"
all_insurance = db.selectall(sql=SQL_ALL_insurance)
all_insurance = list(all_insurance)
for item in all_insurance:
    item = list(item)
    all_insurance_list.append(item[0])
print(all_insurance_list)

for user in all_customer_list:
    insuranceIndex = random.randint(0, len(all_insurance_list)-1)
    SQL = "INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('{}', '{}');"
    SQL = SQL.format(str(user), all_insurance_list[insuranceIndex])
    print(SQL)

"""
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('1EMYDZYSGF', '4');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('FJAWX2S6VE', '4');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('JP6VM1P12T', '1');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('OVN9P3BBTJ', '8');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('PZ6LOH8S6U', '4');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('T6ZJV1WA2M', '6');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('U64KV4JK03', '8');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('VLEBXINR5R', '5');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('XMVRD4ODMH', '5');
INSERT INTO `customer_insurance` (`insurance_id`, `company_id`) VALUES ('XRTC8NPWS0', '6');
"""