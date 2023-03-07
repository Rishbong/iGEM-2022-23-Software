#miRNA in question for gen3 switch
HSA_miR_145_5p = "GUCCAGUUUUC CCAGGAAUCCCU" # length = 23nt 
HSA_miR_199a = "ACAGUAGUCUG CACAUUGGUUA" # length = 22

#dictionary defining complimentary base pairing (no wobble pairing present)
baseDict = {"A":"U", "C":"G"}

#list of and regions
andRegions = ("AAAAAA", "UUUUUU", "CCCCCC", "GGGGGG")

#computes complimentary strand 
def compStrand(rnaStrand):
    compliment = ""
    for i in rnaStrand:
        for key, value in baseDict.items():
            if i == key:
                compliment += value
            elif i == value:
                compliment += key
    return compliment

#reverses string
def reverse(rnaStrand):
  return rnaStrand[::-1]


#computes and gate
def andGateGen(Strand1, Strand2):


    #splitting each miRNA
    miRNA1, miRNA2 = compStrand(Strand1[:len(Strand1)//3]), compStrand(Strand2[:len(Strand2)//3])
    print("length of spliced Strand1: ", len(miRNA1))
    print("length of spliced Strand2: ", len(miRNA2))

    #index is incrimented later to update the andRegion such that its adjacent base doesn't match itself
    index = 0

    #this sets the default value of the andRegion to AAAAAA
    andRegion = andRegions[index] 

    #checking to see if the andRegion borders an identical base and changing it to correct this by incrimenting the index
    #this only needs to be done twice as in the "worst case scenario", ALL of the below code will run, making the anndRegion different to BOTH of its neighboring bases
    if (miRNA1[-1] == andRegion[1]):
        index += 1
        andRegion = andRegions[index] 
        if (miRNA2[0] == andRegion[1]):
            index += 1
            andRegion = andRegions[index]

    return((miRNA1 + andRegion + miRNA2))
    #Edwin maybe from here you could do something with recursion to call this function on (Strand[N], strand[N+1]) to output however many and gates we need for a given generation


print(andGateGen(HSA_miR_145_5p, HSA_miR_199a))