class QuadraticFormula():

    def __init__(self, first, second, third):
        self.first_coefficient = int(first)
        self.second_coefficient = int(second)
        self.third_coefficient = int(third)
    

    def first_step(self):
        exponential = lambda x: x ** 2
        minuend = exponential(self.second_coefficient)
        substrahend = 4*self.first_coefficient*self.third_coefficient
        difference = minuend - substrahend 
        return difference
        
    @staticmethod
    def square_root(value):
        square_root = lambda x: x ** 0.5
        integer = abs(value)
        sqr = square_root(integer)
        return sqr

    
    def addition(self, interger, verify):
        addend1 = self.second_coefficient * -1
        addend2 = interger
        divisor = self.first_coefficient*2

        if verify < 0:
            addend1 = addend1 / divisor
            addend2 = addend2 / divisor
            sum = "{} + {}i".format(round(addend1, 2),round(addend2, 2))

        else:
            sum = round((addend1/divisor) + (addend2/divisor), 2)

        return sum


    def substraction(self, interger, verify):
        minuend = self.second_coefficient * -1
        substrahend = interger
        divisor = self.first_coefficient*2

        if verify < 0:
            minuend = minuend / divisor
            substrahend = substrahend / divisor
            diff = "{} - {}i".format(round(minuend,2),round(substrahend,2))
        else:
            diff = round((minuend/divisor) - (substrahend/divisor),2)
        return diff


    def final_step(self, verify, rounded_sum, rounded_diff):
        if verify < 0:
            print(rounded_sum,",", rounded_diff)
        elif verify ==0:
            print(rounded_sum,",", rounded_diff)
        else:
            print(rounded_sum,",", rounded_diff)


def determine():
    global a,b,c
    a = input("What is the 1st coefficient: ")
    while not a.lstrip("-").replace(".", "", 1).isdigit():
        a = input("Invalid input: ")
            
    b = input("What is the 2nd coefficient: ")
    while not b.lstrip("-").replace(".", "", 1).isdigit():
        b = input("Invalid input: ")

    c = input("What is the 3rd coefficient: ")
    while not c.lstrip("-").replace(".", "", 1).isdigit():
        c = input("Invalid input: ")


def main():
    opinion = "yes"
    while opinion != "no":
        determine()
        quadratic_solver = QuadraticFormula(a,b,c)
        step1 = quadratic_solver.first_step()
        step2 = quadratic_solver.square_root(step1)
        step3 = quadratic_solver.addition(step2, step1)
        step4 = quadratic_solver.substraction(step2, step1)
        quadratic_solver.final_step(step1, step3, step4)
        opinion = input("Continue?(yes/no): ").lower()

main()
