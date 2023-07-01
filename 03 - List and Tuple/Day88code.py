albums=[("welcome to my Nightmare","Alice cooper",1975),
("Bad company","Bad company",1974),
("Nightflight","Budgie",1981),
("More mayhem","Emilda May",2011),
("ride the ligjhtning","Metallica",1984),
]
print(len(albums))
for name,artist,year in albums:
    print("Albums:{}, Artist:{}, year: {}"
         .format(name,artist, year) )