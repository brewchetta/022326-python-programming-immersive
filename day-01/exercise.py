# REAL WORLD

# Algorithm -- set of instructions

# sort --> famous algorithm

# backend engineer

# when we talk about algorithms -- career programming -- interviews

# whiteboarding - you and an engineer will talk about how to solve and build the algorithm
# they're looking for .... 

# - did you find a solution? 
# - did you make the algo efficient? 
# - did you iterate? 
# - do you have a process?


"""### **ALGORITHMS CHALLENGE:** The Bill Calculator

Let's imagine you're going out to eat at your favorite pizza joint; you ordered a slice-of-pizza and now you want to calculate the bill... using Python.

#### **Prompt.**

**OBJECTIVE:** Given a starting meal price and a tipping quantity (in dollars) as well as a constant tax rate, write a function that calculates and returns the total bill on your meal.

**INPUT:** `calculate_bill(food_price=20.99, amount_in_tips=5)`

**OUTPUT:** `27.826625`

#### **Key Assumptions & Constraints.**

##### **Assumptions** are identified to _simplify the problem and reduce complexity/scope_.
# ALWAYS ask about your assumptions.

##### **Constraints** are identified to _highlight aspects of the problem that are unavoidable or cannot be simplified_.

_"I need to calculate a final bill... what goes into that calculation?"_

- **CONSTRAINT:** Original price of the food.
  - **ASSUME:** It's only one person ordering food.
  - **ASSUME:** That person is only ordering one item for their meal.

- **CONSTRAINT:** Amount tipped on the meal.
  - **ASSUME/GIVEN:** We don't have to calculate tip amount from a percentage.

- **CONSTRAINT:** Amount taxed on the meal.
  - **CONSTRAINT:** We have to calculate amount paid in taxes from a given tax rate/percentage.
  - **ASSUME:** The tax rate is constant and unchanging.
    - **DETAIL:** Let's assume NY tax rate for food. (`0.0875`)
  - **ASSUME:** Tax is imposed _only_ on the original food price.

_"The bill will be a representative combination (the sum) of all three values."_

#### **Process Design.**

#### _The process design almost always leans on your **domain understanding**._

**INPUT:** Function that takes in `2` variables as arguments.
  - One variable tracks the **original food price** (numerical).
  - One variable tracks the **amount paid in tips** (numerical).

**PROCESS:**
1. Set **tax rate** to `0.0875`.
2. Calculate **amount paid in taxes** by multiplying the **tax rate** by the **original food price**.
3. Calculate **total bill** by adding **original food price**, **amount paid in tips**, and **amount paid in taxes**.

**OUTPUT:** Function returns `1` number: the **total bill**.

#### **Pseudocode.**

```
function that calculates bill (food price, amount in tips)

  tax rate <- 0.0875

  amount paid in taxes <- tax rate * food price

  total bill <- food price + amount paid in tips + amount paid in taxes
```

#### **Coding Implementation.**
"""

# def calculate_bill(food_price, amount_in_tips):
#   tax_rate = 0.0875
#   amount_in_taxes = tax_rate * food_price
#   total_bill = food_price + amount_in_tips + amount_in_taxes
#   return total_bill

# """#### **Testing.**"""

# # Should return `27.826625`.
# calculate_bill(food_price=20.99, amount_in_tips=5)

# # Should return `10`.
# calculate_bill(food_price=0, amount_in_tips=10)

# # Should return `108.75`.
# calculate_bill(food_price=100, amount_in_tips=0)

"""#### **Optimization. (Stretch Challenges.)**

1. Change the function so that _tax rate_ is a functional argument/variable.

2. Modify the tip calculation so that instead of taking _tip as a quantity_, the function takes in a **tipping rate**.
  - **ASSUME:** When we calculate the tip based on percentage, we do it using the _pre-tax price_.

3. Round the final bill quantity to _two significant digits_ representing dollars and cents.

4. Convert `food_price` to `food_prices`, which will now represent one-to-many individual prices. The function should then immediately add up all prices into one **sum** before calculating tax or tips.

- 4.5. Update the function such that `food_prices` is now a collection of each menu item and its associated price.

5. Extend the function with a new argument called `is_party_large`. Analyze whether or not the party size is considered large (if `is_party_large` is true/false); if the party is considered large in size, then add an automatic 20% gratuity to the final bill. (The gratuity is considered pre-tax and pre-tips.)
"""

# PSEUDO CODE -- it is meant to give an idea of that you will build

# def calculate_bill():
#   food = get user input for the food
#   tip_amount = get user input for the tip
#   taxation_rate = ten percent
#   taxed_food = food * taxation_rate
#   final_total = food + taxed_food + tip_amount
#   return final_total

def calculate_bill():

  food_amount = float( 
    input("What was the cost of the food? ")
  )

  print( f"A recommended tip is: {food_amount * 0.2}" )

  tip_amount = float(
    input("How much was the tip? ")
  )

  taxation_rate = 0.10

  taxes = food_amount * taxation_rate

  final_total = food_amount + taxes + tip_amount
  print( final_total )
  return final_total


calculate_bill()

# Traceback (most recent call last):
#   File "day-01/exercise.py", line 137, in <module>
#     calculate_bill()
#   File "day-01/exercise.py", line 133, in calculate_bill
#     taxes = food_amount * taxation_rate
# TypeError: can't multiply sequence by non-int of type 'float'