### Dependencies:

Ubuntu: ```$ sudo apt-get install make g++```
  
OSX: ``` $ sudo port install make g++```
  
### Build

Ubuntu/OSX: ``` $ make ```

### Run

Ubunut/OSX: ``` $ ./sim ```
  
## What's here?

I was on a plane and didn't have internet, so I had to make some assumptions. 
The basic unit of time is a second, and the basic unit of distance is a foot. 
I assume everything happens on a two mile grid that covers the playa.

```main.cc``` creates a simulator and runs it for a week with 50 people; that's pretty much it. 
The code for the simulator is in ```sim.h``` and ```sim.cc```.
The main loop in a method called ```Sim::run()```.
It updates every person's internal clock, tells them to move, and then tells them to broadcast to each other. 
There's a simple attenuation model in ```Sim::can_hear()``` that determines whether two people can hear each other. 
I have no idea whether it's sensible or not. 
After each time step, the simulator writes a report. 
Repeat.

The code for a person is in ```person.h``` and ```person.cc```.
A person is a combination of a playa id ```puid_t``` and a space time coordinate.
I called this a ```Pin``` for lack for a better name.
It's defined in ```misc.h``` along with some other constants and basic types.
A person also has a mental map of pins for everyone else on playa.
A person's mental map of its own location is always correct and up-to-date, but it's model for everyone else can become outdated.

The Simulator and Person classes are pure virtual. 
You can see in ```main.cc``` that I defined two simple subclasses that define the required methods. 

For a person you have to define what it means to walk each time step in ```Person::move()``` 
  (the class in main does something like a random stumble),
  and broadcast your state in ```Person::say()```
  (the class in main just reports its own position). 
You can use a person's public interface to define these methods.
```Person::get_id()``` returns a person's playa id,
  ```Person::get_loc()``` and ```Person::get_estimate()``` return a person's up-to-date location and his estimates of everyone else's positions,
  ```Person::step()``` updates a person's position by a delta,
  and ```Person::stay_inside()``` clamps a person's position to within the bounds of the grid covering the playa.

For a simulator, you have to define what it means to report each time step in ```Sim::report()```
  (the class in main just prints out when it reaches the end of the day). 
You can plug whatever you want in here, an opengl visualization, error plotting, whatever.

The whole thing takes about a minute to simulate a week on the playa. 
All the runtime is in calculating all-pairs distances between people and checking whether they can hear each other.
That's annoying slow for me, but whatever. 
It's good enough.
