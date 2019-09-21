def weight_on_planets():
   weight_earth = float(input("What do you weigh on earth? "))
   weight_mars = weight_earth * .38
   weight_jupiter = weight_earth * 2.34

   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds."
        % (weight_mars, weight_jupiter))


if __name__ == '__main__':
   weight_on_planets()
