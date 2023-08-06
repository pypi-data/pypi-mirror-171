# Fixpy

Fixpy is an easy to use package for event-driven programming in python.  
The name stems from "FIXed-point iterations" that can be elegantly implemented using this package (an example is shown below).  
Further applications of this package include for example handling of User-Interfaces or interrupt calls.

## Installation

Fixpy can be quickly installed with pip:

```
pip install fixpy
```

## Quick-Start

In the following, some examples demonstrate the usage of this package.
All examples are also available on [Google Colab](https://colab.research.google.com/drive/1ytmLCpshm7Z7e-QyKtpgxpoAChOspT76?usp=sharing).


Fixpy can be used with a verbose or a shortened syntax.  
First, some verbose examples are shown to explain the basic concepts of the package.  
Then, the same examples are presented using the shortened syntax.

### Verbose Syntax Examples

First, we show a simple example to automatically update a BMI (body mass index) computation:


```python
from fixpy import Variable, Function

weight = Variable(70,name="weight") # introduce a new variable for body weight
height = Variable(1.8,name="height") # introduce a new variable for body height

def compute_bmi(kg,m): # function to compute bmi
  return kg/m**2

bmi = Function(compute_bmi,[weight,height],name="bmi") # now, bmi gets automatically updated, if the value of weight or height changes

print(f"BMI = {bmi.get_value()}") # with get_value(), we can access the value computed in bmi

weight.set_value(80) # now, let's change the weight with set_value()

print(f"new BMI = {bmi.get_value()}") # ... as you can see, the BMI was automatically updated

bmi.plot() # plot a graph of event directions
```

Callback listeners can be simply added and removed as follows:

```python
def print_bmi(new_bmi): # define a callback listener
  print(f"The BMI has changed! BMI = {new_bmi}")

bmi.on_change(print_bmi) # callback listeners can be simply added with on_change()

height.set_value(1.85) # if we change for example height, this will automatically update the bmi and consequently trigger the callback

bmi.remove_callback(print_bmi) # callback listeners can be simply removed with remove_callback()

height.set_value(1.9) # now, the callback listener is not called anymore
```

Now, let's dive a bit deeper into the functioning of fixpy at the example of a fixed-point iteration.

```python
def still_ok(old_value,new_value): # we can define a threshold at which a Variable does not get updated anymore (this becomes important, if you want to work with more complex variables such as vectors / matrices / tensors)
  return abs(old_value-new_value) < 1e-8

x = Variable(2, name="value", still_ok = still_ok, max_recursions=10000, alpha=0.5) # furthermore, we can define a maximum number of iterations and a "low-pass" filter for updates alpha

def golden_ratio_iteration(x):
  return 1/(x-1)

f = Function(golden_ratio_iteration,[x]) # f gets updated whenever x changes

x.observe(f) # using x.observe(f), x gets updated to the value of f whenever f changes
# => this results in a loop that iteratively applies f on x until still_ok or max_recursions is reached
# => this is effectively a fixed point iteration (-> therefore the name fixpy ;)

print(f"x = {x.get_value()} (this corresponds to golden ratio)")
```

Fixpy also works with Strings:

```python
name = Variable("world")

hello_name = Function(lambda n: "Hello "+n+"!", [name], still_ok=None)

print(hello_name.get_value())

name.set_value("universe")

print(hello_name.get_value())
```

## Shortened Syntax Examples
First, let's revise the BMI example:

```python
weight = Variable(70,name="weight") # introduce a new variable for body weight
height = Variable(1.8,name="height") # introduce a new variable for body height

bmi = weight/height**2 # here, a function tree is created that computes the bmi and that gets automatically updated, if the value in weight or height changes

print(f"BMI = {bmi.x}") # instead of get_value() we can simply use x to obtain the computed value

weight.x = 80 # similarly, we can use x to set the value of a variable

print(f"new BMI = {bmi.x}") # ... as you can see, the BMI was automatically updated

bmi.plot() # plot a graph of event directions (this corresponds to the function tree mentioned above)
```

Using the shortened syntax, callback listeners can be simply added and removed as follows:

```python
bmi >> (lambda new_bmi: print(f"The BMI has changed! BMI = {new_bmi}")) # instead of on_change(), we can use >>
# by the way, the following syntax would work just as well:
# (lambda new_bmi: print(f"The BMI has changed! BMI = {new_bmi}")) << bmi

height.x = 1.85 # if we change for example height, this will automatically update the bmi and consequently trigger the callback

bmi.remove_callback() # if we don't pass an argument to remove_callback(), all callbacks will be removed

height.x = 1.9
```
A fixed-point iteration can be described in just 2 lines of code:

```python
x = Variable(2, name="value", still_ok = lambda old, new: abs(old-new)<1e-8, max_recursions=10000, alpha=0.5) # furthermore, we can define a maximum number of iterations and a "low-pass" filter for updates alpha

x << 1/(x-1) # instead of observe, we can use <<
# by the way, the following syntax would work just as well:
# 1/(x-1) >> x

print(f"x = {x.get_value()} (this corresponds to golden ratio)")
```
And this is the shortened syntax for strings:

```python
name = Variable("world")

hello_name = "Hello "+name+"!"

print(hello_name.x)

name.x = "universe"

print(hello_name.x)
```
These were the most important concepts of fixpy.

## More Details

Custom functions can be simply created as follows:

```python
import numpy as np
import matplotlib.pyplot as plt

def polynome(x, *coefficients): # custom polynome function
  def _p(x, *coefficients):
    return sum(c*x**i for i,c in enumerate(coefficients))
  return Function(_p,[x, *coefficients])

x = Variable(np.arange(-1, 3, 0.1), name="x") # btw: variables also work with numpy arrays
coefficients = [Variable(c, name=f"c{i}") for i,c in enumerate([1,0,0])]
p = polynome(x, *coefficients)

plt.plot(x.x,p.x)
plt.show()

p >> (lambda y: (plt.plot(x.x,y), plt.show())) # replot polynome automatically, if results change

Variable.set_values(coefficients,[1,1,-1]) # multiple variables can be set at the same time with set_values() => this triggers the replot callback
```
If you want to define your own Variables with customized funtions, you can inherit from Variable as follows:

```python
class Inversion(Variable):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
  
  def inv(self):
    return Function(lambda x: 1/x,[self])

a = Inversion(10,name="a")
print(f"a_inv = {a.inv().x}")
```