#format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate a positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price= 2703.876
print(f"price is {price:.2f}")

print(f"price is {price: 10}")
print(f"price is {price:<10}")
print(f"price is {price:>10}")
print(f"price is {price:^10}")
print(f"price is {price:,}")

