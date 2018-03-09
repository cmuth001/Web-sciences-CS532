#!/usr/bin/env Rscript
## Download and install the package
# install.packages("rjson", repos = "http://cran.us.r-project.org")
# https://cran.r-project.org/web/packages/igraphdata/README.html
library(igraph)
library(igraphdata) # provides karate data
setwd(getwd())
set.seed(20)
# convert to graph format
data(karate)
# print(karate)
kclub <- karate

clust <- cluster_edge_betweenness(kclub)

# Original split
origCommunties <- plot.igraph(kclub)
# Second value is number of communities to create
groups <- cutat(clust, 2)
# Assumed should have split
# plot(structure(list(membership=groups), class="communities"), kclub)
connected_components_count <- count_components(kclub)

# index counter for node edges
edgeIndex <- 1
# split into groups, actual
while(connected_components_count != 3){
  # starts at 1
  edgesRemoved <- delete.edges(kclub, clust$removed.edges[seq(1,edgeIndex-1)])
  connected_components_count <- count_components(edgesRemoved)
  # set new Graph
  origCommunties <- edgesRemoved
  #get separate pdf according to the split
  # pdf(paste("Iteration",edgeIndex,".pdf"))
  plot.igraph(origCommunties)
  edgeIndex <- edgeIndex + 1
}

print(paste("Iteration Count",edgeIndex))
# plot.igraph(origCommunties)