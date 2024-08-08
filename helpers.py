from faker import Faker


def fake_email():
    fake = Faker()
    return fake.email()

def fake_random_password(length):
    fake = Faker()
    return fake.password(length=length)


def fake_chars_password(length):
    fake = Faker()
    return fake.password(length=length, special_chars=True, digits=False, upper_case=False, lower_case=False)
