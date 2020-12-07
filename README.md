# Characterizing_Tangle_with_empirical_data
Create on 01.Sept. 2020



# Overview
This repository shows the technical details of the paper "Charactering Tangle with Empirial Data", including `Tangle data extraction`, `Tangle re-construction`, `Tangle simulation` and `data analysis`.

# Data Extraction 
## From raw data to .json file

1. Download the raw data from  http://dertangle.iota.cafe.
2. Check the head and tail milestone. (Tail milstone is the last milestone at a sub-Tangle.) For each raw tangle dataset, it could contain one or more sub-tangles.
3. Extract the milestone list and store in .json file.
4. Extract the sites raw data from each tail milestone of the sub-tangle and store in .json file, including hash, branch_hash, trunk_hash, timestamp, address, value, bundle_hash, current_index, last_index, attachment_timestamp...

# Tangle Re-construction 
## Find the branch and trunk link of each site
Based on the relationship of the branch hash, trunk hash and site hash, collect all branch links and trunk links of each sub-tangle, store in .json files.
## Re-construction
Use the `networkx` re-construct the tangle based on the branch links and trunk links.

# Tangle Simulation 
The simulation refers https://github.com/minh-nghia/TangleSimulator.
This tool can simulate tangles with various alpha and lambda with different Tip Selection Alogrithms, such as MSMS or URTS.

# Data Analysis
We have analysed the topology and performance features of the simulated tangle and real tangle. 
## Diameter
1. Longest path.
2. Shortest path.
3. Diameters

## In-degree
1. Site in-degree distribution.
2. Usual site in-degree.
3. Milestone in-degree. 

## Cumulative Weight
1. Cumulative weight calculation.
2. Cumulative weight analyis.

## Edge Weight
1. Edge weight calculation: The weight difference absolute value between two connected sites. 
2. Analysis

## Milestone Issuing Time
1. Get the milestone timestamp from milestone.json
2. Analyze the milestone issuing rate for every 12 and 24 hours.

## Transaction Confirmation Time
1. Confirmation time calculation. Because the timestamp of site is incredible, we use the milestone and the snapshot date to locate the site issuing time, then calculate the confirmation time.
2. Confirmation time analysis. 


Updating...




