import evolve
import shutil
import sys
import os
import string

if not len(sys.argv) == 5:
    print("USAGE: embla.py <originalfile> <maximumgenerations> <reproductionrate> <.fileextension>")
    exit()

#sets up imput
seed = sys.argv[1]
max = sys.argv[2]
rep = sys.argv[3]
ext = sys.argv[4]
max = int(max)
rep = int(rep)

wdir = os.getcwd() #gets working directory
gen = 1 #sets generation number
wdirgen = wdir + "/G" + str(gen)
ev = evolve.evolve()
wdirseed = wdir + "/" + seed

if not os.path.exists(wdirgen):
    os.makedirs(wdirgen)
wdirgenseed = wdirgen + "/" + seed
shutil.copy(wdirseed, wdirgenseed)
while(gen <= max):
    copy = 0
    next = gen + 1
    wdirnext = wdir + "/G" + str(next)
    nextspecies = wdirnext + "/" + seed
    numspecies = len([name for name in os.listdir(wdirgen) if os.path.isfile(os.path.join(wdirgen, name))])
    if not os.path.exists(wdirnext):
        os.makedirs(wdirnext)
    for i in range(0,numspecies):
        filelist = os.listdir(wdirgen)
        species = wdirgen + "/" + filelist[i]
        for i in range(0,rep):
            if(os.path.isfile(nextspecies)):
                copy = copy + 1
                nextspecies = nextspecies[:-(len(ext))]
                nextspecies = nextspecies + str(copy) + ext
                shutil.copy(species, nextspecies)
                ev.mutate(nextspecies, "char")
            else:
                shutil.copy(species, nextspecies)
                ev.mutate(nextspecies, "char")
    wdirgen = wdir + "/G" + str(next)
    gen = next

print "Done"
exit()
