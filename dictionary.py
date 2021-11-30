user =  {
    "name": "Annas",
    "age": 18,
    "is_admin": True,
}
user["username"] = "anasusb11"
user["name"] = "Annas Usbah"

#cara biar tiada error
#name = user["username"]
name = user.get("name")
print( name)