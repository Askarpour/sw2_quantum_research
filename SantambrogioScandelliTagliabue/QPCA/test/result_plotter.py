import matplotlib.pyplot as plt
from result_utils import filemetrics_fix
#Script used to generate plots of test results and save the image to a file

result = []
DIMENSIONS=[2]
NBITS=7
ITERATIONS=2
RANDOM_INITIAL_VECTORS = 4

TITLE =""
XLABEL =""
YLABEL =""
OUTPUT_FILE_NAME = "graphs/out.png"

#Fetch result data from a file which name is retrieved by specifing parameters
# used for the test
for i in DIMENSIONS:
    result.append(filemetrics_fix(i,NBITS,ITERATIONS,RANDOM_INITIAL_VECTORS))

print("Data fetched from the file: ",result)

plt.figure(0)
print ([i[0][0] for i in result])
plt.plot(DIMENSIONS, [i[0][0] for i in result])

plt.title(TITLE)
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
#plt.savefig(OUTPUT_FILE_NAME)

