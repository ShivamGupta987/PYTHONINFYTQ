#lex_auth_01269438070259712046

def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    
    
    for name in name_list:
        if len(name)>=3 and name[-2:] == 'at':
            count1+=1
        
        if 'at' in name:
            count2+=1
            
            
    print("_at -> ",count1)
    print("%at% -> ",count2)
 
    #Populate the variables: count1 and count2

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    # print("_at -> ",count1)
    # print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)