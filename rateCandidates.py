#!/bin/python3
from __future__ import annotations
from typing import Set, Dict, List, Tuple

type Job = str
type Rating = float
type Candidate = CandidateProfile
type Team = Dict[Job,Candidate]

class CandidateProfile:
  def __init__(self: CandidateProfile, name: Job, positions: Dict[Job,Rating]):
    self.name: Job = name
    self.positions: Dict[Job,Rating] = positions

# Jobs
Secretary = "Secretary"
Finance = "Finance"
Marketing = "Marketing"
Design = "Design"
Manufacturing = "Manufacturing"
Software = "Software"
allJobs = [ Secretary, Finance, Marketing, Design, Manufacturing, Software, ]

# Candidates
Magnolia = CandidateProfile(
  name="Magnolia Morse",
  positions={ Finance:92.5, Marketing: 82.3 },
)
Bode = CandidateProfile(
  name="Bode Boyle",
  positions={ Design:87.6, Marketing:45.2 },
)
Aliya = CandidateProfile(
  name="Aliya Parrish",
  positions={ Software:94.8, Manufacturing:53.6, Design:66.7, },
)
Karsyn = CandidateProfile(
  name="Karsyn Cook",
  positions={ Marketing:73.1, Finance:21.1 },
)
Aaliyah = CandidateProfile(
  name="Aaliyah Guzman",
  positions={ Manufacturing:67.5, Design:79.4 },
)
Jude = CandidateProfile(
  name="Jude Price",
  positions={ Manufacturing:53.9 },
)
Piper = CandidateProfile(
  name="Piper Bender",
  positions={ Software:87.2, Secretary:69.3 },
)
Zavier = CandidateProfile(
  name="Zavier Fox",
  positions={ Secretary:89.0, Manufacturing:12.3 },
)
Juliette = CandidateProfile(
  name="Juliette Jenkins",
  positions={ Secretary:93.4, Marketing:67.5, Finance:35.3 },
)
Declan = CandidateProfile(
  name="Declan Greene",
  positions={ Manufacturing: 91.3, Finance:29.3 },
)

allCandidates = set([ Magnolia, Bode, Aliya, Karsyn, Aaliyah, Jude, Piper,
                      Zavier, Juliette, Declan, ])

def generateTeams(jobs: List[Job], candidates: Set[Candidate]) -> List[Team]:
  if len(jobs) == 0:
    return [{}]
  else:
    job = jobs.pop()
    worlds: List[Team] = []
    for cand in candidates:
      if job in cand.positions:
        candidates.remove(cand)
        subTeams: List[Team] = generateTeams(jobs.copy(), candidates.copy())
        for sw in subTeams:
          reversedSW = { c:j for j,c in sw.items() }
          if cand not in reversedSW:
            sw[job] = cand
          worlds.append(sw)
        candidates.add(cand)
    return worlds

# Generate all possible teams
allTeams = generateTeams(allJobs.copy(), allCandidates)

# Calculate the overall ranking of each world and sort by best
def rateTeam(world: Team) -> float:
  rating = 0
  for j,c in world.items():
    rating += c.positions[j] / len(allJobs) # Unweighted arithmetic mean
  return round(rating, 2)
rankedTeams = [ (rateTeam(w),w) for w in allTeams ]
rankedTeams.sort(key=lambda tup: tup[0], reverse=True) # Descending by rating

# Generate CSV output
def printRankedTeamCSV(rankedTeam: Tuple[float,Team]):
  print('{:.2f}'.format(rankedTeam[0]), end=",")
  for _,cand in rankedTeam[1].items():
    print(cand.name, end=",")
  print()
print(len(allTeams), "possible teams")
print("score," + ",".join(allJobs))
for rw in rankedTeams:
  printRankedTeamCSV(rw)

