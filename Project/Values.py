class Values:
    def Validate(self, id, fName, lName, phone, email,waterclock):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        elif not (waterclock.isdigit()):
            return "waterclock"
        else:
            return "SUCCESS"