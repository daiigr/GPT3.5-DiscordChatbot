from User import User
import json

class UserObjectArrayGenerator:
    """
    This class is used to generate an array of users
    from an array of formated string arrays
    """
   
    def convertFormatedArraytoUserArray(self, FormatedStringArray):
        user_arr = []
        """
        
        """

        FormatedStringArray = json.loads(FormatedStringArray)
        for FormatedStringUser in FormatedStringArray:
            print(FormatedStringUser)
            user_arr.append(User(
            FormatedStringUser[0],
            FormatedStringUser[1],
            FormatedStringUser[2],
            FormatedStringUser[3]))
        return user_arr