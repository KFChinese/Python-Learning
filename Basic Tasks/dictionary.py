monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "Sepecember",
    "Oct": "October",
    "Nov": "November",
    "Dec": "Decemeber",
}

print(monthConversions["Nov"])
# Should print Novemebr

print(monthConversions.get("love", "Not a valid Key"))
