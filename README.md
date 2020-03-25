# Overloaded-Harbor

This project simulates the behaivior of a harbor given the number of docks that it has and the number of ships arrival that will occur. Details about the harbor are explicit 
described in the section #2 of the project file loacated at `Paper/files/project.pdf`. 

After each simulation the program show the mean of the turn around time of the ships.

## Starting 🚀

To use the project, clone it or download it to your local computer.

### Requirements 📋

It is necessary to have python. The project were developed using python v3.7.4 but in older 
versions it should run perfect because only use standar packages 

### Installation 🔧

To execute the project, simply run:

```
python harbor.py
```

This command run a simulation with 3 docks and 10 ships only 1 time, if you want to change those parameters use `-d`, `-a`, `-t` respectively, just like is showed below

```
python harbor.py -a 1000 -d 20 -t 50
```

To see a description of all possible params execute:
```
python harbor.py --help
```

## Autores ✒️

- **Lazaro Raul** - [stdevRulo](https://github.com/stdevRulo)

## Licencia 📄

This project is under the License (MIT License) - see the file [LICENSE.md](LICENSE.md) for details.

## More

For details about the implementation read the file located at `Paper/Informe-Lazaro-Raul-C412.pdf`.