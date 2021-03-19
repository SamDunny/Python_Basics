print ("\nHello World\n")

rat_amt = input("How many rabbits do you think you could fight off by yourself? ")

# have to convert rat_amt to integer (from string), square it, reconvert it to integer (from double), then reconvert back to string (from int)
print(rat_amt + "? Thats not too many, but give it 3 hours and it'd be " + str(int(pow(int(rat_amt), 2))))
print("\n\n\t...its a rabbit mating joke\n")