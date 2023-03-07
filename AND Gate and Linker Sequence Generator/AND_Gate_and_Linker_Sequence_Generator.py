#miRNA in question for gen3 switch
HSA_miR_145_5p = "GUCCAGUUUUCCCAGGAAUCCCU" 
HSA_miR_199a = "ACAGUAGUCUGCACAUUGGUUA"

#dictionary defining complimentary base pairing (no wobble pairing present)
baseDict = {"A":"U", "C":"G"}

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

print(compStrand(HSA_miR_145_5p))