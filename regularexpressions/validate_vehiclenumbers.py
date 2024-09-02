# kerala registration vehicle numbers validaition

# starting with KL
# two digits 
# alphabets (one or two)
#  4 digits

from re import fullmatch

vehicle_num="KL-07-DE-1973"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}" # hypen may or may not be there and its optional when "? used"
#  if * then hyphen may come any number of times

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "Valid")