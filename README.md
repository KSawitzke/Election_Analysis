# Election_Analysis

## Overview
The purpose of this election audit analysis was to provide Seth and Tom with tabulated election results in multiple formats, given the provided data input. In working with them, we have provided an automatic way to feed their .csv vote files in, and return an easy-to-read high level results printout, in both a command prompt feed as well as a .txt file for ease of sharing. Aside from all of the technical advantages, we obviously also counted the votes and determined a victor.

## Election-Audit Results
* 369,711 Total votes were cast in this election. A simple counter is included in the highest level for loop that runs through the entire list of votes.
    `for row in reader:
        total_votes = total_votes + 1`

* The vote breakdown is as follows:
    * Jefferson: 38,855
    * Denver: 306,055
    * Arapahoe: 24,801

    * This code snippet shows how the county tally was kept. The county_name variable takes the value from the county based on indexing each row of the voting data. If it is not found, it is added to the counties list. Then, the votes in the county_votes dictionary are incremented by 1 based on that same county_name variable. This happens within the for loop that runs over the whole dataset.
```
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
```

* Denver county has the largest number of votes, as seen when tallying each county as seen above.

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Similarly to the county count, the candidate count can be kept with an if statement to keep a running list of candidates, and a dictionary with each candidate as a key value.
```
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
```
* This gives us the following results:
    * Charles Casper Stockham: 23.0% of the vote with 85,213 votes
    * Diana DeGette: 73.8% of the vote with 272,892 votes
    * Raymon Anthony Doane: 3.1% of the vote with 11,606 votes

* Based on these totals, Diana wins the election with a landslide, coming in at 73.8% of the vote with 272,892 votes.

## Election Audit Summary
This script can certainly be used to assist with future elections with some minor tweaks. First, rather than using a .csv as the input, the input to the script could be modified to feed directly from a database that the voting machines are connected to. This could allow for the second modification, which would be live counting. If this script was run on a regular interval during voting, you could get much quicker results rather than collecting all of the votes before counting. Since this script is simple and quick to run, you could easily check the .txt output often to see how the candidates are doing. Changing the output into a webform view of some sorts would even allow for pretty visualizations to be added to the ongoing counting.
