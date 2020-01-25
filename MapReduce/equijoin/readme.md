EquiJoin on the records present in the table. 
For example:

There are following two records:
R, 3, Sal, Maglite, Nutley, 555-6905
S, 3, 24000, 5000, part1

The output of Map reduce can be 

R, 3, Sal, Maglite, Nutley, 555-6905, S, 3, 24000, 5000, part1

or 

S, 3, 24000, 5000, part1, R, 3, Sal, Maglite, Nutley, 555-6905

but not both
