
Hospital/resident problem
=========================

Use Python implementation in https://github.com/daffidwilde/matching
Academic paper https://joss.theoj.org/papers/10.21105/joss.02169

Tested in tests.py



Algorithm to compute a rank-maximal matching 
============================================


Python Implementation of the algorithm in Irving, R. W., Kavitha, T., Mehlhorn, K., Michail, D., & Paluch, K. E. (2006). Rank-maximal matchings. ACM Transactions on Algorithms (TALG), 2(4), 602-610.
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.92.6742&rep=rep1&type=pdf


## Description of the problem

We start with :
- P, a set of posts (size p)
- A, a set of applicants (size a)
for each applicant (member of A) there is a preference list for posts in P

The goal is to find a matching of A to P such as
- the maximum possible number of applicants are matched to their first choice post,
- and given that condition, the maximum possible number are matched to their second choice post, and so on

Other Definitions: 
- r, the largest rank that an applicant uses to rank any post.
- the *signature* of a matching M is (x1,...,xr), where xi is the number of applicants who are matched in M with one of their i-th choice posts
- A matching that has the maximum signature under this ordering is a *rank-maximal matching*.

## Algorithm

Requires the implementation of algorithm Hopcroft and Karp


## Complexity

O( min(n+C,Csqrt(n) ) m) 

where: 
- C<=r is the maximal rank used in an optimal solution
- n = a + p
- m is the total size of the preference lists
