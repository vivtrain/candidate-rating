# candidate-rating
Generate and sort weighted, maximal matchings between jobs and candidates to help one assemble the best possible team.

Usage: `python3 rateCandidates.py`

## Motivation
Building the best possible team from a list of jobs and candidates is a tricky affair. With few jobs or few candidates, or by limiting the number of jobs a candidate can apply to, the problem can be managed, but as the number of applications grows, the number of possibilities explodes exponentially (potentially greater than exponentially).

This algorithm generates all possible teams from (as of now) hardcoded inputs. The input allows individual ratings, which are used to rank the outcomes in decreasing order. This allows one to review the top N options before making a final decision, rather than simply taking the best one, as there may be other factors to consider that are not captured in individual candidate ratings.

## Input Format
// TODO

# Algorithm Description
// TODO

## Complexity Analysis
// TODO
