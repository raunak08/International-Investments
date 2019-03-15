# International-Investments

Problem Introduction:


Charles Rosen, a financial analyst in Germany, comes across a folder containing details of an investment he made upon his graduation four years ago. The investment was of 30,000 German Marks (DM) as B-Bonds. These bonds were to mature in 7 years from the time he invested. The bonds attracted lucrative interests which increased by the year and were compounded annually. Charles had an option of withdrawing the bonds whenever he wished and did not sell any bonds for the first four years. However, last year, the German federal government had announced a capital gains tax on interest income. It was designated that the first DM 6,100 a single individual earns in interest per year would be tax-free. Any interest income beyond DM 6,100 would be taxed at a rate of 30 percent. Because of the new tax implemented last year, Charles has decided to re-evaluate the investment. He knows that the new tax affects his potential return on the B-Bonds, but he also knows that most likely a strategy exists for maximizing his return on the bonds. He might be able to decrease the tax he has to pay on interest income by selling portions of his bonds in different years. Charles considers his strategy viable because the government requires investors to pay taxes on interest income only when they sell their B-Bonds. Also, if Charles decides to sell his bonds, his alternative investment opportunities are limited. He contemplated investing in Certificate Deposits (CDs) which would pay him 4.0 percent interest. Finally, Charles concludes that he would make all his transactions on December 31, regardless of the year. Also, since he intends to attend business school in the United States in the fall of the seventh year and plans to pay his tuition for his second, third, and fourth semester with his investment, he does not plan to keep his money in Germany beyond December 31 of the seventh year. Below is the interest rate in 7 years:


Y DM 100  An. %  Interest% DM 30,000
1	107.50	7.50%	 7.50%	    32250.00
2	116.64	8.00%	 8.50%	    34991.25
3	126.55	8.17%	 8.50%	    37965.51
4	137.62	8.31%	 8.75%	    41287.49
5	150.01	8.45%	 9.00%	    45003.36
6	163.51	8.54%	 9.00%	    49053.66
7	178.23	8.61%	 9.00%	    53468.49


We analysed the different scenarios under which Charles might have to make investment decisions starting with the basic condition where he just withdraws the entire DM 30,000 at the end of the 7th year without making any further investment. Then we proceed to the case where he invests in CDs. We then, analysed situations where he invests DM 50,000 instead of DM 30,000. Another interesting situation was the increased exemption on the tax-free amount for married couples. We analysed the case where he plans to marry on the fifth of the investment.


Metaheuristic (Genetic Algorithm)

Introduction:

A metaheuristic is a higher-level procedure or heuristic designed to find, generate, or select a heuristic (partial search algorithm) that may provide a sufficiently good solution to an optimization problem, especially with incomplete or imperfect information or limited computation capacity. Metaheuristics sample a set of solutions which is too large to be completely sampled. Metaheuristics may make few assumptions about the optimization problem being solved, and so they may be usable for a variety of problems.

Metaheuristic algorithms, i.e., optimization methods designed according to the strategies laid out in a metaheuristic framework, are — as the name suggests — always heuristic in nature. This fact distinguishes them from exact methods, that do come with a proof that the optimal solution will be found in a finite (although often prohibitively large) amount of time. Metaheuristics are therefore developed specifically to find a solution that is “good enough” in a computing time that is “small enough”. As a result, they are not subject to combinatorial explosion – the phenomenon where the computing time required to find the optimal solution of NP-hard problems increases as an exponential function of the problem size. 

Metaheuristics have been demonstrated by the scientific community to be a viable, and often superior, alternative to more traditional (exact) methods of mixed-integer optimization such as branch and bound and dynamic programming. Especially for complicated problems or large problem instances, metaheuristics are often able to offer a better trade-off between solution quality and computing time. Moreover, metaheuristics are more flexible than exact methods in two important ways. First, because metaheuristic frameworks are defined in general terms, metaheuristic algorithms can be adapted to fit the needs of most real-life optimization problems in terms of expected solution quality and allowed computing time, which can vary greatly across different problems and different situations. Secondly, metaheuristics do not put any demands on the formulation of the optimization problem (like requiring constraints or objective functions to be expressed as linear functions of the decision variables). However, this flexibility comes at the cost of requiring considerable problem-specific adaptation to achieve good performance. 

Compared to optimization algorithms and iterative methods, metaheuristics do not guarantee that a globally optimal solution can be found on some class of problems. Many metaheuristics implement some form of stochastic optimization, so that the solution found is dependent on the set of random variables generated. In combinatorial optimization, by searching over a large set of feasible solutions, metaheuristics can often find good solutions with less computational effort than optimization algorithms, iterative methods, or simple heuristics. As such, they are useful approaches for optimization problems


Properties:

These are some properties that characterize metaheuristics: 

• Metaheuristics are strategies that guide the search process. 
• The goal is to efficiently explore the search space in order to find near–optimal solutions. 
• Techniques which constitute metaheuristic algorithms range from simple local search procedures to complex learning processes.
• Metaheuristic algorithms are approximate and usually non-deterministic. 
• Metaheuristics are not problem-specific.


Genetic Algorithm:

A genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection. 

In a genetic algorithm, a population of candidate solutions (called individuals, creatures, or phenotypes) to an optimization problem is evolved toward better solutions. Each candidate solution has a set of properties (its chromosomes or genotype) which can be mutated and altered; traditionally, solutions are represented in binary as strings of 0s and 1s, but other encodings are also possible. 

The evolution usually starts from a population of randomly generated individuals, and is an iterative process, with the population in each iteration called a generation. In each generation, the fitness of every individual in the population is evaluated, the fitness is usually the value of the objective function in the optimization problem being solved. The more fit individuals are stochastically selected from the current population, and each individual's genome is modified (recombined and possibly randomly mutated) to form a new generation. The new generation of candidate solutions is then used in the next iteration of the algorithm. Commonly, the algorithm terminates when either a maximum number of generations has been produced, or a satisfactory fitness level has been reached for the population.

A typical genetic algorithm requires: 

1. a genetic representation of the solution domain, 
2. a fitness function to evaluate the solution domain. 

A standard representation of each candidate solution is as an array of bits. Arrays of other types and structures can be used in essentially the same way. The main property that makes these genetic representations convenient is that their parts are easily aligned due to their fixed size, which facilitates simple crossover operations. Variable length representations may also be used, but crossover implementation is more complex in this case. Tree-like representations are explored in genetic programming and graph-form representations are explored in evolutionary programming; a mix of both linear chromosomes and trees is explored in gene expression programming. 

Once the genetic representation and the fitness function are defined, a GA proceeds to initialize a population of solutions and then to improve it through repetitive application of the mutation, crossover, inversion and selection operators.


Case 13.2 Solved by GA:

The case as discussed above, talks about the best strategy by which Charles can withdraw bonds for maximizing his profit. With the implementation of Genetic Algorithm applied for the case, we hope to find the optimal strategy for withdrawal of bonds. The parameters of the Algorithm is discussed as follows: 

Algorithm: 

• Generate a population of possible chromosomes (solutions) which satisfy all constraints which in our case is the combination of different values of decision variables Y5 + Y6 + Y7 such that the Ʃ(Y5 + Y6 + Y7) = 30000. 

• In this case we have assumed the population size to be 100, generated randomly by using Beta Distribution and the function “np.random.dirichlet(length, size) “ . 

• Number of Generations is set to 100 to allow the code to develop the best values. 

• Evaluation of fitness of solutions by calculating the objective function Z which is defined in the fitness function using if-else loop since taxable amount is only applicable after the interest goes beyond 6100 German Marks; if not then the interest*6100 should be considered. 

• For the 100 generations check fitness value by comparing the “past_max” and the “new_max” variables, which is also the stopping criteria. If “past_max >= new_max”, we have already reached the best value the algorithm can conjure. If not then, we update with past value with new value and the iteration is repeated. 

• Select different combinations of chromosomes from the randomly generated to find different fitness values 

• Crossover: Combining different combinations of chromosomes to find the fit and unfit values. Initially chromosomes are selected randomly. In our case we have only allowed 2 chromosomes to be chosen and the 3rd is calculated by subtracting it with 30000 – (sum of 1st two).

• Selection: Select the best solutions to get the best value and keep repeating until the best value is found. For the implementation we had to create an array and pass the random numbers generated by using the above-mentioned function which would then be deemed fit or unfit based on the fitness function. 

• Mutation: We have not allowed the chromosomes to mutate in the code 

• Stopping criteria: If no more than 5 solutions have progressed then stop
