def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    
    # Get the first three characters of source and destination
    src = source[:3]
    dest = destination[:3]
    
    # Generate ticket numbers
    for i in range(101, 101 + no_of_passengers):
        ticket_number = f"{airline}:{src}:{dest}:{i}"
        ticket_number_list.append(ticket_number)
    
    # Return the last five ticket numbers or all if less than 5 passengers
    if no_of_passengers >= 5:
        return ticket_number_list[-5:]
    else:
        return ticket_number_list

# Test the function with the provided sample inputs
print(generate_ticket("AI", "Bangalore", "London", 10))
print(generate_ticket("BA", "Australia", "France", 2))

# rewrite
def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    
    # Get the first three characters of source and destination
    src = source[:3]
    dest = destination[:3]
    
    # Generate ticket numbers
    for i in range(101, 101 + no_of_passengers):
        ticket_number = f"{airline}:{src}:{dest}:{i}"
        ticket_number_list.append(ticket_number)
    
    # Return the last five ticket numbers or all if less than 5 passengers
    if no_of_passengers >= 5:
        return ticket_number_list[-5:]
    else:
        return ticket_number_list
    

# Test the function with the provided sample inputs
print(generate_ticket("AI", "Bangalore", "London", 10))
print(generate_ticket("BA", "Australia", "France", 2))
# rewrire


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