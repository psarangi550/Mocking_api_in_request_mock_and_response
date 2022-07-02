from faker import Faker
import random

fake=Faker("en-IN")

f_first_names=[fake.first_name() for _ in range(50)]
f_last_names=[fake.last_name() for _ in range(50)]
f_city_names=[fake.city() for _ in range(50)]
f_country=[fake.country() for _ in range(50)]
f_email=[fake.email() for _ in range(50)]
f_url=[fake.url() for _ in range(50)]
f_phone=[fake.msisdn() for _ in range(50)]


result=[]

def fetch_fake_value():
    for i in range(1,51):
        f_name=random.choice(f_first_names)
        l_name=random.choice(f_last_names)
        full_name=f"{f_name} {l_name}"
        email=random.choice(f_email)
        url=random.choice(f_url)
        country=random.choice(f_country)
        city=random.choice(f_city_names)
        address=f"{f_city_names} {f_country}"
        number=random.choice(f_phone)
        result.append(f"{full_name}\n{email}\n{f_url}\n{address}\n{number}\n")
    return result


val=fetch_fake_value()
print(len(val))






