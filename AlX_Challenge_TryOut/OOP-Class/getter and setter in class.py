class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email  # Private attribute, uses double underscore;
                              # to make an attribute protected we use a single underscore: _email
        self.password = password

    # Getter for email
    @property
    def email(self):
        return self.__email

    # Setter for email
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            raise ValueError("Invalid email format. Email must contain '@'.")

# Create an instance of User
user1 = User("sam", "sam@gmail.com", "12345")

# Access the email using the getter
print(user1.email)  # Output: sam@gmail.com

# Modify the email using the setter
try:
    user1.email = "samuel@gmail.com"
    print(user1.email)  # Output: samuel@gmail.com
except ValueError as e:
    print(e)

# Attempt to set an invalid email
try:
    user1.email = "samuel"
except ValueError as e:
    print(e)  # Output: Invalid email format. Email must contain '@'.
