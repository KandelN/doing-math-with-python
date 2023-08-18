from collections import Counter
from visual import visualize


class Stats():
    """
    Object containg descrete data.
    """
    def __init__(self, numbers):
        self.numbers  = numbers
        
        self.N = len(self.numbers)

    def get_mean(self):
        """
        Returns arithemetic mean of numbers in stat object.
        """
        return ( sum(self.numbers)/self.N )

    def get_median(self):
        """
        Returns arithemetic mean of numbers in stat object.
        """
        self.numbers.sort()
        N = self.N
        if N%2:
            # N is odd.
            m = (N+1)//2
            return(self.numbers[m-1])

        else:
            m1 = N//2
            m2 = N//2 + 1
            v1 = self.numbers[m1 - 1]
            v2 = self.numbers[m2 - 1]
            return (v1 + v2)/2

    def get_modes(self):
        """
        Returns mode of numbers in stat object.
        """
        c = Counter(self.numbers)
        num_freq_list  = c.most_common()
        
        max_freq = num_freq_list[0][1]

        modes = []
        for num, freq in num_freq_list:
            if freq == max_freq:
                modes.append(num)
        return modes
            
    def print_frequency_table(self):
        """
        Prints frequency table of numbers in stat object.
        """
        c = Counter(self.numbers)
        num_freq_list = c.most_common()
        num_freq_list.sort()
        print("Number\tFrequency")
        for num, freq in num_freq_list:
            print("{0}\t{1}".format(num, freq))

    def get_range(self):
        """
        Returns the range of the numbers.
        """
        return max(self.numbers) - min(self.numbers)
    
    def get_variance(self):
        """
        Returns the variance of the numbers.
        """
        d = 0
        mean = self.get_mean()
        for num in self.numbers:
            d += (num - mean)**2
        var = d/self.N
        return var

    def get_sd(self):
        """
        Returns the standard deviation of the numbers.
        """
        var = self.get_variance()
        return var**0.5

    def value_from_percentile(self, p):
        """
        Return the number that corresponds to a specific percentile supplied.
        """
        #determine the position
        if p == 0:
            i = 1
        elif p == 100:
            i = self.N
        else:    
            i = self.N * p/100 + 0.5

        self.numbers.sort()
        if int(i) == i:
            return self.numbers[i -1]    
        else:
            k = int(i)
            f = i - k
            value = (1 - f) * self.numbers[k -1] + f * self.numbers[(k+1) -1]
            return value

    def get_grouped(self, interval):
        """
        Returns a grouped frequency table from the list of numbers.
        """

        self.numbers.sort()
        x0 = self.numbers[0]
        xn = self.numbers[-1]
        a = x0 - x0 % interval    #less than x0 and multiple of interval

        p = 0
        value = x0
        table = dict()
        while a <= xn:
            b = a + interval
            table[(a,b)] = 0

            #loop within the list of numbers
            while value < b:
                table[(a, b)] += 1
                p += 1
                if p < self.N:
                    value = self.numbers[p]
                else:
                    break
                           
            a = b

        print_grouped(table)

    def plot_me(self, filename = "default_descrete_plot.png", s=100):
        """
        Saves a image of plot of the descrete data.
        """
        visualize(y = self.numbers, filename = filename, s= s)
        print(f"\nPlot saved as {filename}")


def find_corr(x, y):
    """
    Returns the correlation coefficient between
    x and y.
    """
    if len(x) != len(y):
        raise ValueError(" Two data sets must be of same length.")

    #Initializing variables
    n = len(x)
    sum_xy = 0      #Sigma(xy)
    sum_x = 0       #Sigma(x)
    sum_y = 0       #Sigma(y)
    sum_x2 = 0      #Sigma(x**2)
    sum_y2 = 0      #Sigma(y**2)
    
    # Calculate Varibales
    for xi, yi in zip(x, y):
        sum_xy += xi * yi
        sum_x += xi
        sum_y += yi
        sum_x2 += xi**2
        sum_y2 += yi**2

    sq_sum_x = sum_x**2
    sq_sum_y = sum_y**2

    # calculate denominator and numerator
    denr = n * sum_xy - sum_x * sum_y
    a = n * sum_x2 - sq_sum_x
    b = n* sum_y2 - sq_sum_y
    numr = ( a * b )**0.5

    # Calculate correlation
    corr = denr / numr
    return corr

def print_grouped(table):
    """
    Prints the grouped frequency table.
    """
    n = 0
    print("Group\t\t\tFrequency")
    for group, freq in table.items():
       print("{0}\t- {1}\t\t{2}".format(group[0], group[1], freq))
       n += freq
    
    print("\t\tTotal :", n, sep="\t")

