import random
#imported random so that we can use its functionality in our program

#generating random integer

randominteger=random.randint(0,1000)
print(randominteger)

#generating floating point number between 0 and 1

randomfloat=random.random()
print(randomfloat)


#generating floating point number between 0 and 100

randomfloat100=100*random.random()
print(randomfloat100)

# generating in range by skipping

randomrange=random.randrange(0,100,21)
print(randomrange)

# generating number of K bit

randomofkbit=random.getrandbits(64)

print(randomofkbit)

#to pick random element from a list of element

map=['aam','emli','aloo','pyaz']
print(random.choice(map))

#to get list of k random member from sample

print(random.sample(map,2))

#making system to generate same number during same time

#seed used to set the time
random.seed(1)
 
print('Generating a random sequence of 4 numbers...')
print([random.randint(1, 100) for i in range(5)])
 
# Reset the seed to 1 again so it will give value same as which id produced during seed(1)
random.seed(1)
 
# We now get the same sequence
print([random.randint(1, 100) for i in range(5)])