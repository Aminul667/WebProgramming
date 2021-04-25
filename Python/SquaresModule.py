from functions import square

# another way
# 'import functions'. It imports the whole module.
# then we have to use 'functions.square(i)'

for i in range(10):
    print("{} squared is {}".format(i, square(i)))