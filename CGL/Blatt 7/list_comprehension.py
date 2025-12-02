import random
import matplotlib.pyplot as plt


def generate_random_point_in_square(length):
    """
    Generate a random point in a square of a given side length centered around the origin with the sides aligned with x- and y-axis.
    """
    return tuple([length*random.uniform(-0.5, 0.5), length*random.uniform(-0.5, 0.5)])

def distance(p1, p2):
    """
    Measures the Euclidean distance between the points p1 and p2 in 2D.
    """
    # TODO: implement this function

def point_in_circle(p, center=None, radius=None):
    """
    Checks if the provided point p lies in a circle of a given radius around the provided center.
    """
    # TODO: implement this function


# TODO: generate a list of 10000 random points in a square of side length 2.0 using generate_random_point_in_square and list comprehension
full_list_of_points =

# TODO: generate a list of those points in full_list_of_points that are within a radius of 1.0 of the origin (again using list comprehension)
filtered_list_of_points =

# TODO: print the ratio of the number of points in filtered_list_of_points to the total number of generated points

# TODO: Generate separate lists of the x- and y-values of full_list_of_points and filtered_list_of_points
x_values_full =
y_values_full =

x_values_filtered =
y_values_filtered =

plt.scatter(x_values_full, y_values_full)
plt.scatter(x_values_filtered, y_values_filtered)
plt.show()
