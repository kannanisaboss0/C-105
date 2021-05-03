#-----------------------------------------------------------ElectionData2021.py-----------------------------------------------------------#
'''
Importing Modules
-Pandas as pd
-Plotly.Express as pe
-csv
-math
'''
import pandas as pd
import plotly.express as pe
import csv
import math
#Formal Introduction and User Inputs
print("Welcome to ElectionData2021.py. We provide statistical insights on the recent elections conducted in India. Precisely, the states of Assam, Kerala, Pudcherry, Tamil Nadu, West Bengal.")
display_list_index_count=0
display_list_graph_index_count=0
display_list=["Unusable_Index_Element","Assam","Kerala","Puducherry","Tamil Nadu","West Bengal"]
#A new selection method
#Displaying all possible choices
for display_item in display_list[1:]:
    display_list_index_count+=1
    print(str(display_list_index_count)+" "+str(display_item))
choice=int(input("Please enter the index of the corresponding state of which the statistics should be shown:(from the aforementioned list)[Eg. 2 for Kerala, hence type in '2' only]:"))
display_list_graph_index_count=0
display_list_graph=["Unusable_Index_Graph_Array_Element","Bar","Scatter","Pie"]
#Displaying all possible graph choices
for display_item_graph in display_list_graph[1:]:
  display_list_graph_index_count+=1 
  print(str(display_list_graph_index_count)+" "+str(display_item_graph)) 
graph_choice=int(input("Please enter the index of the graph/chart type to be shown:(from the aforementioned list):"))

#Checking validity of input
if(choice<=5):
    state_chosen=display_list[choice]
    print(state_chosen)

    with open("Election_data_"+state_chosen+".csv") as f:
        election_data_csv=csv.reader(f)
        election_data_list=list(election_data_csv)
        
    election_data_list.pop(0)
    mean_sum=0
    election_data_list_length=len(election_data_list)
    election_data_list.pop(election_data_list_length-1)
    election_data_max_list=[]
    victor_party=''
    for entry in range(len(election_data_list)):
        if(election_data_list[entry]!=""):
            mean_sum=mean_sum+int(election_data_list[entry][3])
            election_data_max_list.append(int(election_data_list[entry][3]))
            for party in election_data_list:
                if(int(party[3])==max(election_data_max_list)):
                    victor_party=party[0]
    mean=mean_sum/election_data_list_length
    election_data_max_list_maximum=max(election_data_max_list)   
    standard_deviation_sum=0               
    for unit in range(len(election_data_list)):
        difference=int(unit)-mean
        difference=difference**2
        standard_deviation_sum=standard_deviation_sum+int(difference)
    standard_deviation_quotient=standard_deviation_sum/election_data_list_length
    standard_deviation=math.sqrt(standard_deviation_quotient)
    





    
    percentage_constituent_total=round((election_data_max_list_maximum/mean_sum)*100,2)
    
    print("Total constituencies:"+str(mean_sum))
    print("Number of parties:"+str(election_data_list_length))
    print("Mean value of constituencies won:"+str(round(mean,2)))
    print("Standard deviation of all the parties:"+str(round(standard_deviation,2)))
    print("Winning Party:"+str(victor_party))
    print("Number of constituencies wonby the winning party(both Leading and Won):"+str(election_data_max_list_maximum))
    print("Percentage of total constituencies accquired:"+str((percentage_constituent_total))+"%")
    if(percentage_constituent_total>=50):
      print("Majority:Absolute Majority")
    else:
      print("Majority:Simple Majority")  
    
    graph_dataframe=pd.read_csv("Election_data_"+state_chosen+".csv")
    if(graph_choice==1):
      graph_bar=pe.bar(graph_dataframe,x="Party",y="Total",color="Party",title="Election 2021 Data(Bar Graph)")
      graph_bar.update_layout(shapes=[dict(type="rect",x0=0,x1=election_data_list_length,y0=0,y1=mean,fillcolor="green",layer="below"),dict(type="rect",x0=0,x1=election_data_list_length,y0=standard_deviation,y1=standard_deviation+0.1,fillcolor="red",name="Standard Deviation",layer="below",)])
      graph_bar.update_yaxes(rangemode="tozero")
      graph_bar.show()
      print("Graph Data:")
      print("Y-Axis:Number of constituencies won")
      print("X-Axis:Parties")
      print("Red Line:Standard Deviation Value("+str(round(standard_deviation,2))+")")
      print("Green Zone:Below Mean Value("+str(round(mean,2))+")")
      sub_average_count_graph_1=0
      for entry_total_1 in election_data_max_list:
        if(int(entry_total_1)<round(mean,2)):
          sub_average_count_graph_1+=1
      print(str(sub_average_count_graph_1)+" parties/y have accquired less than "+str(round(mean,2))+" constituencies")
      above_average_count_graph_1=len(election_data_max_list)-sub_average_count_graph_1
      print(str(above_average_count_graph_1)+" parties/y have accquired more than "+str(round(mean,2))+" constituencies")
    if(graph_choice==2):
      graph_scatter=pe.scatter(graph_dataframe,y="Party",x="Total",color="Party",size="Total",size_max=50,title="Election 2021 Data(Scatter Graph)")
      graph_scatter.update_layout(shapes=[dict(type="rect",y0=0,y1=election_data_list_length,x0=0,x1=mean,fillcolor="green",layer="below"),dict(type="rect",y0=0,y1=election_data_list_length,x0=standard_deviation,x1=standard_deviation+0.3,fillcolor="red",name="Standard Deviation",layer="below",)])
      graph_scatter.update_yaxes(rangemode="tozero")
      graph_scatter.show()  
      print("Graph Data:")
      print("Y-Axis:Parties")
      print("X-Axis:Number of constituencies won")
      print("Red Line:Standard Deviation Value("+str(round(standard_deviation,2))+")")
      print("Green Zone:Below Mean Value("+str(round(mean,2))+")")
      sub_average_count_graph_2=0
      for entry_total_2 in election_data_max_list:
        if(int(entry_total_2)<int(round(mean,2))):
          sub_average_count_graph_2+=1
      print(str(sub_average_count_graph_2)+" parties/y have accquired less than "+str(round(mean,2))+" constituencies")
      above_average_count_graph_2=len(election_data_max_list)-(sub_average_count_graph_2)
      print(str(above_average_count_graph_2)+" parties/y have accquired more than" +str(round(mean,2))+" constituencies")  
    if(graph_choice==3):
      graph_pie=pe.pie(graph_dataframe,values="Total",names="Party",color="Party",title="Election 2021 Data(Pie Chart)")
      graph_pie.show()
      print("Graph Data:")
      print("Section:Parties")
      print("Section Value:Number of constituencies won")
      print("Standard Deviation Value:"+str(round(standard_deviation,2)))
      print("Mean Value:"+str(round(mean,2)))
      sub_average_count_graph_3=0
      for entry_total_3 in election_data_max_list:
        if(int(entry_total_3)<int(round(mean,2))):
          sub_average_count_graph_3+=1
      print(str(sub_average_count_graph_3)+" parties/y have accquired less than "+str(round(mean,2))+" constituencies")
      above_average_count_graph_3=len(election_data_max_list)-(sub_average_count_graph_3)
      print(str(above_average_count_graph_3)+" parties/y have accquired more than "+str(round(mean,2))+" constituencies")
    print("Thank You for using ElectionData2021.py") 
    
else:
    print("Request Terminated.")
    print("Invalid Input.")
    print("Thank You for using ElectionData2021.py")    
#-----------------------------------------------------------ElectionData2021.py-----------------------------------------------------------#

    