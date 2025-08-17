magicians = ['aung myat thar', 'sayar zin yaw', 'sayar moe', 'zawgyi']
great = []
def make_great(magicians, great):
    while magicians:
        magician = "Great " + magicians.pop()
        great.append(magician)
    
def show_magicians(great):
    print("\nThe following magicians are popular in my country:")
    for magician in great:
        print(magician.title())
        
make_great(magicians, great)
show_magicians(great)
    