"""
Jethro Ronald Lee
"""

import matplotlib.pyplot as plt

HILARY_FILE = "hilary_hahn_data.txt"

def main():
    
    liveness_sum = 0
    popularity_sum = 0
    PIECES = 10
    
    live_squared_sum = 0
    pop_squared_sum = 0
    pop_live_prod_sum = 0
    
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", 
             "fuchsia", "saddlebrown", "dimgray"]
    liveness_ratings = []
    popularity_ratings = []
    
    # Opens the file and gathers data regarding the liveliness and popularity 
    # rating of ten of Hilary Hahn's tracks
    
    with open(HILARY_FILE, "r") as infile:
        
        while True:
            
            piece = infile.readline().strip()
            liveness = infile.readline()
            popularity = infile.readline()
            
            if piece == "":
                break
            
            liveness = float(liveness)
            popularity = int(popularity)
            
            liveness_sum += liveness
            popularity_sum += popularity
            
            liveness_ratings.append(liveness)
            popularity_ratings.append(popularity)
            
            # Plots the relationship btwn liveliness & popularity for ten of
            # Hahn's works as determined by Spotify's algorithms
            
            plt.plot(liveness, popularity, "*", label = piece, 
                         color = colors[0])
            
            colors.pop(0)
            
    # Calculates the Pearson's r value for the data shown on this plot 
         
    for livenesses in liveness_ratings:
        live_squared_sum += (livenesses) ** 2
       
        
    for popularities in popularity_ratings:
        pop_squared_sum += (popularities) ** 2
        
    for i in range(len(popularity_ratings)):
        pop_live_prod_sum += liveness_ratings[i] * popularity_ratings[i]
    
    pearson_coeff = ((PIECES * pop_live_prod_sum) - \
                     (liveness_sum * popularity_sum)) / \
                     (((PIECES * live_squared_sum - (liveness_sum) ** 2) ** 
                     0.5) * ((PIECES * pop_squared_sum - (popularity_sum) ** 2) 
                     ** 0.5))
 
    # Determines the strength of the correlation between the liveness and 
    # popularity of Hahn's tracks 
    
    if pearson_coeff > 0:
        if pearson_coeff <= 0.3:
            print("This data presents a weak positive correlation")
        elif pearson_coeff <= 0.7:
            print("This data presents a moderate positive correlation")
        elif pearson_coeff <= 1:
            print("This data presents a strong positive correlation")
            
    if pearson_coeff < 0:
        if pearson_coeff >= -0.3:
            print("This data presents a weak negative correlation")
        elif pearson_coeff >= -0.7:
            print("This data presents a moderate negative correlation")
        elif pearson_coeff >= -1:
            print("This data presents a strong negative correlation")
        elif pearson_coeff == 0:
            print("This data presents no correlation")
            
    # Displays the Pearson's r value, axes labels, title, and legend on the 
    # plot                         
                             
    plt.text(0.2, 12, "r= " + str(round(pearson_coeff, 4)), bbox = 
             {"facecolor": "maroon"}, fontsize = 10, color = "white")
    plt.grid()
    plt.xlabel("Liveness Rating")
    plt.ylabel("Popularity")
    plt.title("Spotify AI Ratings on Hilary Hahn's tracks")
    plt.legend(prop={"size": 6.5})
    plt.figure(figsize = (8, 6), dpi= 1000)
    plt.show()
    plt.savefig('Hilary Hahn plot.png')

main()