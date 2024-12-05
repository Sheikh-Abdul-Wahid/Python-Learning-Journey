# The @property decorator is used to turn a method into a getter for an attribute.
# It allows you to access the value of a private or computed attribute like it's a normal attribute, without calling it as a method.

# The @<property_name>.setter decorator is used to define a setter method for the property.
# It allows you to set the value of the attribute in a controlled way (e.g., with validation or additional logic).

class Employee:

    @property
    def name(self):
        return self.fullname  # When name is accessed, return the value of fullname
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0] # Split the first name (before space) & assign it to fname
        self.lname = value.split(" ")[1] # Split the last name (after space) & assign it to lname
        self.fullname = value  # Store the full name (first + last) in fullname taken from return value of @property

n = Employee()  # Create an instance of the Employee class

n.name = "Alan Beker"  # Set the name property; this will call the setter and store "Alan" in fname, "Beker" in lname, and "Alan Beker" in fullname

print(n.lname, n.fname)  # Print the last name (Beker) and first name (Alan) stored in lname and fname
print(n.fullname)  # Print the full name (Alan Beker) stored in fullname from @name.setter value
print(n.name)      # Access the name property, which calls the getter and returns the full name stored in fullname from @property return value
