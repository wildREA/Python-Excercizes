# --------- DATA LIBRARY ---------
conversion = input("Enter a binary number to convert: ")[:8]  # no more than 8 characters (Byte size limit)
convert = conversion.zfill(8)


print(convert + "\n")
# --------- CONDITIONS & CODE ---------
value = int(convert, 2)
print(value)
