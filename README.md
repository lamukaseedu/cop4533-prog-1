# Programming Assignment 1: Matching and Verifying

#### Will Berg: 39326193
#### Lam Nguyen: 88729415

Instructions: clone repo into an empty working directory, run matcher and verifier in IDE or in terminal with no arguments
```
cd src
python matcher.py
python verifier.py
```

Edit example.in and example.out as desired before running code, but program assumes that input/output format matches that described on the Canvas assignment page.

### Part C:
![](./graphs/graph1.png)
![](./graphs/graph2.png)

We measured the runtime of our matcher and verifier by importing the time module on a local development branch and using the time.perf_counter() function at the beginning and end of each program.

The trend we notice is that at small values of n, the change in runtime as n increases is only by a small amount. But, at large values of n, the runtime becomes very long and is noticeable when running the programs. Since the number of possible iterations in the Gale-Shapley algorithm is n^2, at a small value of n such as 8, there are 64 possible iterations. But, at n = 256, there are 65536 possible iterations so the loops in our programs will likely have to run for much longer. 