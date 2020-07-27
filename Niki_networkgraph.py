import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib


#avail_font_names = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
#print(avail_font_names)


jobs=pd.read_csv('NikiData.csv')
#print(jobs.head())


jobs['Nikola']='Nikola'
G1=nx.from_pandas_edgelist(jobs, 'Experiences','Skills')
#G1.add_edge('Nikola', 'Physics Studies')
G1.add_edge('Nikola', 'PhD Physics')
G1.add_edge('Nikola', 'MAN')
G1.add_edge('Nikola', 'LabPeers')
G1.add_edge('Nikola', 'Certificates')
pos = nx.kamada_kawai_layout(G1)
#pos = nx.spring_layout(G1)
mysize=jobs['YearsE']+jobs['YearsS']

    
mynodelist=jobs['Experiences'].tolist()+jobs['Skills'].tolist()+["Nikola"]
mysize=jobs['YearsE'].tolist()+jobs['YearsS'].tolist()+[9]
mycolors=["#17E9E0"]*(len(jobs['YearsE'])-6)+["#FCCD04"]*6+["#FCCD04"]* (len(jobs['YearsS'])-6)+["#FFB48F"]*6+["#A64AC9"]
my_new_size = [i * 500 for i in mysize]


nx.draw(G1,pos=pos,with_labels=True,nodelist=mynodelist ,node_size=my_new_size, 
        node_color=mycolors,node_shape="o", alpha=0.95, linewidths=1, font_size=8, 
        font_color="black", width=1, edge_color='#ededed',font_family="Arial Black")


#GCP1=GCP Big Data and ML Fundamentals
#GCP2=Modernizing Data Lakes and Data Warehouses with GCP


