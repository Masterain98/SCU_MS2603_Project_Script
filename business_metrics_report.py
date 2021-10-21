import pandas as pd
from db_pool.mysqlhelper import MySqLHelper
from matplotlib import pyplot as plt

db = MySqLHelper()

mertics1_sql = "SELECT pharmacy_order.store_id, SUM(orderdetail.final_total) AS 'October 2021 Sales' FROM orderdetail INNER JOIN pharmacy_order ON pharmacy_order.order_id=orderdetail.order_id INNER JOIN pharmacy ON pharmacy_order.store_id=pharmacy.store_id WHERE orderdetail.order_time >= 1633046400 & orderdetail.order_time <= 1635724799 GROUP BY pharmacy_order.store_id;"

mertics1_sql_result = list(db.selectall(sql=mertics1_sql))
for i in range(len(mertics1_sql_result)):
    mertics1_sql_result[i] = list(mertics1_sql_result[i])
    mertics1_sql_result[i][1] = round(mertics1_sql_result[i][1], 2)

print(mertics1_sql_result)

df = pd.DataFrame(mertics1_sql_result, columns =['store_number', 'Sales'])
print(df)

'''
plt.figure(figsize=(6, 6))
explode = (0, 0, 0, 0, 0)
plt.title("Sales of Pharmacies in October 2021 Grouped by Store Number")
colors = ("SkyBlue", "SlateGrey", "SteelBlue", "Silver", "cornflowerblue")
labels = 'Store 1', 'Store 2', 'Store 3', 'Store 4', 'Store 5'
plt.pie(x=df.Sales, labels=labels,explode=explode, colors=colors, autopct="%.0f%%", counterclock=False, shadow=False)
plt.show()
'''

mertics2_sql = "SELECT order_medicine.medicine_sku, SUM(order_medicine.amount) AS total_sale_quantity FROM order_medicine INNER JOIN medicine ON medicine.medicine_sku=order_medicine.medicine_sku GROUP BY medicine.medicine_sku ORDER BY total_sale_quantity DESC;"
mertics2_sql_result = db.selectall(sql=mertics2_sql)
print(mertics2_sql_result)