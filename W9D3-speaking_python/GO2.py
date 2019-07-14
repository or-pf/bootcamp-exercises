def double(stringi):
    my_list= list(stringi)
    double=[letter*2 for letter in my_list]    
    new_string= "".join(double)
    print(new_string)
    return new_string
double("ngf")
double("kloiuyy")