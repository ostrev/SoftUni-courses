from project.user import User
from project.library import Library


class Registration:

    def add_user(self, user: User, library: Library):
        for user_rec in library.user_records:
            if user.user_id == user_rec.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        library.rented_books[user.username] = {}
        # to do a rent book dictionary

    def remove_user(self, user: User, library: Library):
        for user_rec in library.user_records:
            if user.user_id == user_rec.user_id:
                library.user_records.remove(user)
                library.rented_books.pop(user.username)
                return
                # to do a rent book dictionary
        return f"We could not find such user to remove!"


    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    rent_book = library.rented_books[user.username]
                    library.rented_books.pop(user.username)
                    library.rented_books[new_username] = rent_book
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user.user_id}"

            else:
                return f"There is no user with id = {user_id}!"


