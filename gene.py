import random

#this is going to be the num of individuals in each generation
POPULATION_SIZE = 100

#this will be all of the valid genes available
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "I love computer science"

#this class will represent individuals in each generation
class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    #function to create randome genes
    @classmethod
    def mutatedGenes(self):
        global GENES
        #random.choices will select a random letter from the genes set of chars
        gene = random.choices(GENES)
        return gene

    #function to create the chromosome of genes
    @classmethod
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


def main():
    global POPULATION_SIZE
  
    #current generation
    generation = 1
  
    found = False
    population = []
  
    # create initial population
    for _ in range(POPULATION_SIZE):
                gnome = Individual.createGenome()    
                population.append(Individual(gnome))
  
    while not found:
  
        # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)
  
        # if the individual having lowest fitness score ie. 
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break
  
        # Otherwise generate new offsprings for new generation
        new_generation = []
  
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])
  
        # From 50% of fittest population
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
  
        population = new_generation
  
        print(str(population[0].chromosome))
        print("Generation: {}\tString: {}\tFitness: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))
  
if __name__ == '__main__':
    main()
