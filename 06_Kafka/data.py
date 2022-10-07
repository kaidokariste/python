from faker import Faker
fake = Faker()

def get_registered_user():
    return {
        "name" : fake.name(),
        "address": fake.address(),
        "created_at": fake.year(),
        "job_position": fake.job()
    }

if __name__ == "__main__":
    print(get_registered_user())