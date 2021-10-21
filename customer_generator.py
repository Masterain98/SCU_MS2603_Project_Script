import requests
import random


def getRandomZipCode(cityName):
    SantaClara = ['95050', '95051', '95052', '95053', '95054', '95055', '95056']
    SanJose = []
    for i in range(72):
        code = 95101 + i
        if code != 95140:
            SanJose.append(str(code))
    Campbell =['95008', '95009', '95011']
    LosGatos = ['95030', '95031', '95032']
    Cupertino = ['95014', '95015']
    Sunnyvale = ['94085', '94086', '94087', '94088', '94089', '94090']

    if cityName == "Santa Clara":
        zipCode = SantaClara[random.randint(0, len(SantaClara))-1]
    elif cityName == "San Jose":
        zipCode = SanJose[random.randint(0, len(SanJose))-1]
    elif cityName == "Campbell":
        zipCode = Campbell[random.randint(0, len(Campbell))-1]
    elif cityName == "Los Gatos":
        zipCode = LosGatos[random.randint(0, len(LosGatos)) - 1]
    elif cityName == "Cupertino":
        zipCode = Cupertino[random.randint(0, len(Cupertino)) - 1]
    else:
        zipCode = Sunnyvale[random.randint(0, len(Sunnyvale)) - 1]
    return zipCode

def getRandomCustomer(number):
    # Return: first name, last name, email, date_of_birth, address, insurance

    # Length = 36
    charList = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]

    # City list, size == 12
    cityList = ["Santa Clara", "San Jose", "Campbell", "Los Gatos", "Cupertino", "Sunnyvale"]

    # return list
    return_list = []

    for i in range(number):
        # print("=" * 20)
        result = requests.get("https://randomuser.me/api/?nat=US").json()["results"][0]
        first_name = result["name"]["first"]
        last_name = result["name"]["last"]
        email = result["email"]
        date_of_birth = result["dob"]["date"][:10]
        street = str(result["location"]["street"]["number"]) + " " + result["location"]["street"]["name"]
        city = cityList[random.randint(0, 5)]
        state = "California"
        zip_code = getRandomZipCode(city)
        insurance_id = ""
        for j in range(10):
            randomNumber = random.randint(0, 35)
            insurance_id += charList[randomNumber]
        '''
        print("first_name:", first_name)
        print("last_name:", last_name)
        print("email:", email)
        print("date_of_birth:", date_of_birth)
        print("street:", street)
        print("city:", city)
        print("state:", state)
        print("zip_code:", zip_code)
        print("insurance_id:", insurance_id)
        '''
        return_result = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "date_of_birth": date_of_birth,
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "insurance_id": insurance_id
        }
        sql_script = "INSERT INTO `customer` (`first_name`, `last_name`, `email`, `date_of_birth`, `street`, `city`, `state`, `zip_code`, `insurance_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');"
        sql_script = sql_script.format(first_name, last_name, email, date_of_birth, street, city, state, zip_code,
                                       insurance_id)
        return_list.append(sql_script)
    return return_list


randomCustomer = getRandomCustomer(50)

for item in randomCustomer:
    print(item)
