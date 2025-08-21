# from openai import OpenAI

# client = OpenAI(
#             base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#             api_key="AIzaSyDTr_Tl6-gBsfcGFSIgS7_tUWV426vaCfY",
#         )
# response = client.chat.completions.create(
#             model="gemini-2.0-flash",
#             messages=[{"role": "user", "content": "Hello, world!"}],
#             max_tokens=256,
#             temperature=0.3,
#         )
# print(response)

def main(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    main(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3)

class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def main(self, *args, **kwargs):
        print(args)
        print(kwargs)

a = A(1, 2, 3)
a.main(4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3)

class Animal:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class HasOwner:
    def __init__(self, *, owner, **kwargs):
        super().__init__(**kwargs)
        self.owner = owner

class Timestamped:
    def __init__(self, *, created_at, name, **kwargs):
        super().__init__(**kwargs)
        self.created_at = created_at
        print(name)

class Dog(HasOwner, Timestamped, Animal):
    def __init__(self, *, breed, **kwargs):
        super().__init__(**kwargs)
        self.breed = breed

d = Dog(name="Rex", breed="Labrador", owner="Mia", created_at="2025-08-21")
print(Dog.__mro__)
print(d.name, d.breed, d.owner, d.created_at)  # Rex Labrador Mia 2025-08-21