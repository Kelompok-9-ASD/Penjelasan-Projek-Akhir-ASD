class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Medicine:
    def __init__(self, name, quantity, id):
        self.name = name
        self.quantity = quantity
        self.id = id
        self.next = None


class Pharmacy:
    def __init__(self):
        self.head = None
        self.size = 0

    # fungsi untuk menambahkan data obat baru
    def add_medicine(self, name, quantity, id):
        new_medicine = Medicine(name, quantity, id)

        if self.head is None:
            self.head = new_medicine
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_medicine

    # fungsi untuk menghapus data obat
    def remove_medicine(self, name):
        if self.head is None:
            return
        
        if self.head.name == name:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    # fungsi untuk melihat output data obat dengan atributnya.
    def display_medicines(self):
        if self.head is None:
            print("No medicines available.")
        else:
            current = self.head
            print("\nMedicines in stock:")
            while current is not None:
                print(f"Nama : {current.name} - Quantity : {current.quantity} - ID : {current.id}")
                current = current.next

    # fungsi untuk melihat output list data obat.
    def update_medicine(self, name, quantity, id):
        current = self.head
        while current is not None:
            if current.name == name:
                current.quantity = quantity
                current.id = id
                return
            current = current.next
        
    # fungsi untuk algoritma jump search
    def search_medicine(self, name):
        current = self.head
        while current is not None:
            if current.name == name:
                return current
            current = current.next
        return None


class PharmacyList:
    def __init__(self):
        self.users = []
        self.pharmacy = Pharmacy()

    def add_user(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)

    def remove_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False
    

    
    def sortbyname(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.name > current.next.name:
                    current.name, current.next.name = current.next.name, current.name
                    current.quantity, current.next.quantity = current.next.quantity, current.quantity
                    current.id, current.next.id = current.next.id, current.id
                    swapped = True
                current = current.next


    def merge_descending(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
		
        if left.id >= right.id:
            result = left
            result.next = self.merge_descending(left.next, right)
        else:
            result = right
        result.next = self.merge_descending(left, right.next)

        return result


    def main_menu(self):
        print("Welcome to the pharmacy laboratory medicine list!")
        while True:
            print("==============================")
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            print("==============================")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if self.login(username, password):
                    self.user_menu()
                else:
                    print("Invalid credentials.")
            elif choice == "2":
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.add_user(username, password)
                print("User registered successfully.")
            elif choice == "3":
                print("Thank you for using the pharmacy medicine list!")
                break
            else:
                print("Invalid choice. Try again.")

    def user_menu(self):
        while True:
            print("==================================")
            print("\n1. Add medicine")
            print("2. Remove medicine")
            print("3. Display medicines")
            print("4. Search about medicines")
            print("5. Sort by ascending")
            print("6. Sort by descending")
            print("7. Exit")
            print("==================================")
            choice = input("Enter your choice: ")

            if choice == "1":

                if self.login_required():
                    name = input("Enter medicine name: ")
                    quantity = int(input("Enter medicine quantity: "))
                    id = int(input("Enter the ID: "))
                    self.pharmacy.add_medicine(name, quantity, id)
                    print("Medicine added successfully.")
                else:
                    break

            elif choice == "2":

                if self.login_required():
                    name = input("Enter medicine name: ")
                    self.pharmacy.remove_medicine(name)
                    print("Medicine removed successfully.")
                else:
                    break

            elif choice == "3":

                if self.login_required():
                    self.pharmacy.display_medicines()
                else:
                    break

            elif choice == "4":

                if self.login_required():
                    name = input("Enter medicine name: ")
                    self.pharmacy.search_medicine(name)
                    print(f"Medicine found")
                    return True
                else:
                    print("Medicine not found")
                    break

            elif choice == "5":

                if self.login_required():
                    pharmacy_laboratory = pharmacy_laboratory.sortbyname()
                    print(self.pharmacy.display_medicines)
                else:
                    break

            elif choice == "6":

                if self.login_required():
                    pharmacy_laboratory = pharmacy_laboratory.merge_descending(pharmacy_laboratory)
                    print(self.pharmacy.display_medicines())
                else:
                    break

            elif choice == "7":

                print("Have a nice day....")
                break
            else:
                print("Invalid choice. Try again.")

    def login_required(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.login(username, password):
            return True
        else:
            print("Invalid credentials.")
            return False

pharmacy_laboratory = PharmacyList()
pharmacy_laboratory.main_menu()