# Solow Library
A Solow simulator to help understand the basics of the Solow Model.
The model is based on the standard Undergraduate thaught Solow Model
with Cobb-Douglas Production functions. For now, the model doesn't take
into account technological growth. The default population and capital
settings are both set to 1 unit at time zero.

### Installation
```
pip install solow-sim
```

### Get started
To start experimenting

```Python
from solow_library import user_interface
user_interface
```
Then, run the python file and follow the instructions.
To play around by yourself,

```Python
from solow_library import solow
```

Formal Documentation should be coming one day, however, here are the
main functions one should be interested in:

Creating an Economy:
```Python
name = "USA"
savings = 0.05
depreciation = 0.05
population_growth = 0.03
capital_ratio = 0.4
time = 200
usa = solow.Economy(name, savings, depreciation,
              population_growth, capital_ratio, time)
print(usa)
```
Access the Time Paths:
```Python
print(usa.data)
# Or for any variables {'Time', 'Capital', 'Population', 'Output', 'Output',
# 'Interest', 'Wage'}
print(usa.data['Wage'])
```

Plot Time Paths:
```Python
usa.plot_all()
```

Introduce A Population Shock:
```Python
shock_size = 0.2
shock_time = 100
usa.population_shock(shock_size,shock_time)
usa.plot_all_shock()
```

Access time paths after the Shock:
```Python
print(usa.data)
#Or, for any of the previous variables with ' - Pop.Shock' added at the end
print(usa.data['Wage - Pop.Shock'])
```