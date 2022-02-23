#treasure island
#art taken from ascii arts https://www.asciiart.eu/logos/biohazards
print('''
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    

''')
print("\n\n")
print("Welcome to treasure island!")
print("You are standing at the foot of a hill, would you climb up straight? take a turn, left or right?")
ans1=input("Enter S for straight, L for left , R for right.")
if(ans1=='s' or ans1=='S'):
    print("Game over, you slipped and fell due to landslides.")
elif(ans1=='L' or ans1=='l'):
    print("You safely reach the waterfalls lake")
    print("Unfortunately, the boat just left and your surroundings dont seem to be safe, would you swim your way or wait for a boat?")
    ans2=input("Enter S for swim, W for wait")
    if(ans2=='s' or ans2=='S'):
        print("Game over, There were starving reptiles in the waters")
    elif(ans2=='W' or ans2=='w'):
        print("Luckily there was a second boat starting in a few minutes.")
        print("You fell asleep in the boat and find yourself in a room with three doors")
        print("The red door says 'everyone says i'm sus', the green door says 'red sus', the yellow door says 'iykyk'")
        print("what door would you choose?")
        ans3=input("Enter R to take the red door, G for green, Y for yellow")
        if(ans3=='r' or ans3=='R'):
            print("Red isn't always sus, congratulations you've won the game")
        elif(ans3=='G' or ans3=='g'):
            print("G for Game over, G for guilty, not everything that's green is clean")
        else:
            print("Imposter yellow stabs you in the back. Game Over")
else:
    print("Game over, a wild boar attacks you on your way")
