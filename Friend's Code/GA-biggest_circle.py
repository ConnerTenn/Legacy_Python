# Genetic Algorithm - Integrating graphics
# author: Aniekan Umoren
# course: ICS-3U
# date: 2015-12-23

# ------------------------------ Brainstorming -----------------------------------
'''
    - You will make a background of of circles (rand or not) and determine
      the biggest possible sircle that can fit on the screen withou any collisions.
      
    - Fitness:
        ~ the size of the circle
        ~ if it collides, it's an automatic death
        ~ the bigger it is the better it is

    - Organism: Circle
        ~ use the sprite class for collisions and such
        ~ Chromosome:
            ~ position of the circle (preferably the center)
            ~ radius of the circle
        ~ Crossover:
            ~ use a mathematical merging of genes
            ~ in essense get an average of parents to make children
            ~ maybe you could use the AND or OR logic gates
            ---------------- Alternative Option --------------------
            ~ during cross_over, you could add the the fitness of the parents
            and get the average of their positions
        ~ Mutation:
            ~ a random chance of adding or subtracting a certain amount
            from each value in the chromsosome
    - Natural Selection:
        ~ any cell that collides with anything or extends beyond the screen will
        die automatically.
        ~ cell fitness is based upon their size, the bigger it is, the higher its fitness.
'''          

import pygame
import random
pygame.init()

# -------- Color Palet ---------

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)

# --------- Functions ----------

def growth(lst):
    for i in lst:
        if type(i) is Organism:
            i.chromosome[2] += 10
    return lst

# ------ Pygame Overhead --------

class Organism(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.fitness = 0
        self.chromosome = []
        # Chromosome config: [pos_x,pos_y,diameter]
        self.chromosome.append(random.randrange(0,700))
        self.chromosome.append(random.randrange(0,500))
        self.chromosome.append(random.randrange(0,75)) #Experiment between 50-100
        self.fitness = self.chromosome[2]
            
    # Function used solely by offspring
    def inherit(self,genes):
        self.chromosomes = genes

    # Creates two new offspring
    def crossover(self,partner):
        child1 = []
        child2 = []
        # Uses AVRG and bitwise AND 
        for i in range(3):
            gene = self.chromosome[i] + partner.chromosome[i]
            child1.append(int(gene/2))
            child2.append(self.chromosome[i] & partner.chromosome[i])

        # Mutation portion of the crossover
        for i in range(len(child1)):
            if random.randrange(0,5)+1 == 3:
                if random.randrange(0,1)+1 == 0:
                    child1[i] += 1
                else:
                    child1[i] -= 1
        for i in range(len(child2)):
            if random.randrange(0,5)+1 == 3:
                if random.randrange(0,1)+1 == 0:
                    child2[i] >> 1
                else:
                    child2[i] << 1
        return (child1,child2)
    
    def crossover_2(self,partner):
        child1 = []
        child2 = []
        # Uses AVRG and bitwise AND 
        for i in range(2):
            gene = self.chromosome[i] + partner.chromosome[i]
            child1.append(int(gene/2))
            child2.append(self.chromosome[i] & partner.chromosome[i])
            gene = self.chromosome[i+1] + partner.chromosome[i+1]
        child1.append(gene)
        child2.append(gene)
        
        # Mutation portion of the crossover
        for i in range(len(child1)):
            if random.randrange(0,5)+1 == 3:
                if random.randrange(0,1)+1 == 0:
                    child1[i] += 1
                else:
                    child1[i] -= 1
        for i in range(len(child2)):
            if random.randrange(0,5)+1 == 3:
                if random.randrange(0,1)+1 == 0:
                    child2[i] >> 1
                else:
                    child2[i] << 1
        return (child1,child2)
    
    def apoptosis(self,sprite):
        death = None # possible values: None, True, False
        # "None": means that no collision happened and thus no organisms die
        # "True": means that "this" organism is removed from population
        # "False": means that the organism competing with "this" one dies
        x = self.rect.x + self.chromosome[2]
        y = self.rect.y + self.chromosome[2]
        col1 = pygame.sprite.collide_circle(self,sprite)
        col2 = pygame.sprite.collide_circle(sprite,self)
        if col1 == True or col2 == True:
            # and organism is going to die (check if organism or barrier collision)
            if type(sprite) == Organism:
                # check who is the fitness out of the two organisms
                if self.fitness <= sprite.fitness:
                    # "This" organism is outcompeted and doesn't make it to population
                    death = True
                else:
                    # "This" organism outcompeted the other organism
                    death = False
            else:
                # "This" organism collided with a barrier and results in a death
                death = True
        if x > 700 or y > 500:
            # A part of this organism isn't visible on the screen and results in a death
            death = True
        return death

    def apoptosis_2(self):
        x = self.rect.x + self.chromosome[2]
        y = self.rect.y + self.chromosome[2]
        if x > 700 or y > 700:
            death = True
        else:
            death= None
        return death
    
    # This method interprets the genes and expreses their code
    def phenotype(self):
        size = (self.chromosome[2],self.chromosome[2])
        self.image = pygame.Surface(size)
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.chromosome[0]
        self.rect.y = self.chromosome[1]
        pygame.draw.ellipse(self.image,RED,[0,0,self.chromosome[2],self.chromosome[2]])
        
class Barrier(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() #initialises parent class
        self.data = []
        # Referring to max and min size
        self.min = 10
        self.max = 300
        self.data.append(random.randrange(50,600)+1)
        self.data.append(random.randrange(50,400)+1)
        self.data.append(random.randrange(self.min,self.max+1))
        size =(self.data[2], self.data[2])
        self.image = pygame.Surface(size)
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        #Self.rect tells sprite.Group.draw() where to blit the image on the screen
        self.rect.x = self.data[0]
        self.rect.y = self.data[1]
        # Position of the image surface
        pygame.draw.ellipse(self.image,BLACK,[0,0,self.data[2],self.data[2]],1)
        
    # Ensures that the barriers are spread our nicely
    def check_col(self,barrier_list):
        remove = False
        for circle in barrier_list:
            x = self.rect.x + self.data[2]
            y = self.rect.y + self.data[2]
            col1 = pygame.sprite.collide_circle(self,circle)
            col2 = pygame.sprite.collide_circle(circle,self)
            if col1 == True or col2 == True:
                remove = True
                break
        return remove

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Genetic Algorithm")
clock = pygame.time.Clock()
done = False

# ---------- Creating the Sprites -----------

sprites_group = pygame.sprite.Group()
organism_group = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()
num_barriers = 10
num_population = 100

# Creating barrier sprites
#print("--------- Barrier Objects ------------")
index = 0
while index < num_barriers:
    barrier = Barrier()
    if barrier.check_col(barrier_group) == False:
        barrier_group.add(barrier)
        sprites_group.add(barrier)
        #print(barrier.data)
        index += 1

# Creating Organism Sprites
multi_list = sprites_group.sprites()
organism_list = []
for i in range(num_population):
    circle = Organism()
    circle.phenotype()
    organism_list.append(circle)
multi_list.extend(organism_list)
    
organism_list = organism_list[::-1] # Implementing first come first serve
print(len(organism_list))
i = 0

while i < len(organism_list):
    #print(organism_list[i].chromosome)
    graveyard = [] # Experiment and decide whether to remove or keep
    index = 0
    circle = organism_list[i]
    while index < len(multi_list) and len(organism_list) > 0:
        if circle is not multi_list[index]:
            death = circle.apoptosis(multi_list[index])    
            if death is True:
                for dead in graveyard:
                    multi_list.append(dead)
                    organism_list.append(dead)
                multi_list.remove(circle)
                organism_list.remove(circle)
                break
            elif death is False:
                rip = multi_list.pop(index)
                organism_list.remove(rip)
                graveyard.append(rip)
            elif death is None:
                index += 1
        else:
            if circle.apoptosis_2 is True: 
                multi_list.remove(circle)
                organism_list.remove(circle)
            else:
                index += 1
   
    if death is not True:
        i += 1    
           
# Update sprites_group and organism_group using multi_list
sprites_group.empty()
organism_group.empty()
for circle in multi_list:
    sprites_group.add(circle)
    if type(circle) is Organism:
        organism_group.add(circle)
'''
for organism in sprites_group.sprites():
    try:
        print(organism.chromosome)
    except:
        pass'''
print(len(organism_list))
organism_list.sort(key = lambda x: x.chromosome[2],reverse = True)
# -------------- Main program Loop ----------------
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    sprites_group.draw(screen)
    pygame.display.flip()
    
    #print("--------- Next Generations ----------")
    while len(organism_list) < num_population:
        curr_population = len(organism_list)
        father = random.randrange(0,curr_population-5)
        mother = random.randrange(0,curr_population-5)
        # Creating parent organisms
        
        father = organism_list[father]
        mother = organism_list[mother]
        #print ("Parents: ",father.chromosome, mother.chromosome)
        
        # Creating offspring organisms
        
        offspring = father.crossover_2(mother)
        son = Organism()
        daughter = Organism()
        son.inherit(offspring[0])
        daughter.inherit(offspring[1])
        son.phenotype() # constructing physical features from genotype
        daughter.phenotype() # constructing physical features from genotype
        
        offspring = (son,daughter)
        organism_list.extend(offspring)
        multi_list.extend(offspring)
        #print(offspring)
        
    i = 0
    while i < len(organism_list):
        #print(organism_list[i].chromosome)
        graveyard = [] # Experiment and decide whether to remove or keep
        index = 0
        circle = organism_list[i]
        while index < len(multi_list) and len(organism_list) > 0:
            if circle is not multi_list[index]:
                death = circle.apoptosis(multi_list[index])    
                if death is True:
                    for dead in graveyard:
                        multi_list.append(dead)
                        organism_list.append(dead)
                    multi_list.remove(circle)
                    organism_list.remove(circle)
                    break
                elif death is False:
                    rip = multi_list.pop(index)
                    organism_list.remove(rip)
                    graveyard.append(rip)
                elif death is None:
                    index += 1
            else:
                if circle.apoptosis_2 is True: 
                    multi_list.remove(circle)
                    organism_list.remove(circle)
                else:
                    index += 1
       
        if death is not True:
            i += 1
           
    organism_list.sort(key = lambda x: x.chromosome[2],reverse = True)
    
    multi_list = growth(multi_list)
 
    # Update sprites_group and organism_group using multi_list
    sprites_group.empty()
    organism_group.empty()
    for circle in multi_list:
        sprites_group.add(circle)
        if type(circle) is Organism:
            organism_group.add(circle)
          
        
pygame.quit()
                   
