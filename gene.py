import random

#this is going to be the num of individuals in each generation
POPULATION_SIZE = 100

#this will be all of the valid genes available
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "I love computer science"

#this class will represent individuals in each generation
class Individual():
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    #function to create randome genes
    def mutatedGenes(self):
        global GENES
        #random.choices will select a random letter from the genes set of chars
        gene = random.choices(GENES)
        return gene

    #function to create the chromosome of genes
    def createGenome(self):
        global TARGET
        gnomeLength = len(TARGET)
        #this will get exactly the number of letters in the target from the random gene function
        return [self.mutatedGenes() for _ in range(gnomeLength)]
    
    #fuction to produce offspring
    def mate(self, parent2):
        childChromosome = []
        #we want to look through the genomes in both chromosomes 
        for genome1, genome2 in zip(self.chromosome, parent2.chromosome):

            #get a random probability
            probability = random.random()
            if probability < 0.45:
                childChromosome.append(genome1)

            elif probability < 0.90:
                childChromosome.append(genome2)

            else:
                childChromosome.append(self.mutatedGenes())

        #return the new individual created by the mutations
        return Individual(childChromosome)


    #function to calculate the fitness of the individual
    def calculateFitness(self):
        global TARGET
        fitness = 0

        for gs, gt in zip(self.chromosome, TARGET):
            #if the two genes are not equal, then we increase fitness. In this program, the lower the number, the more fit it is
            if gs != gt: fitness+= 1

        return fitness




        


