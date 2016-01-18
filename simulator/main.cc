#include <iostream>

#include "person.h"
#include "sim.h"

using namespace std;

class MyPerson : public Person {
  public:
    MyPerson(puid_t id) : Person(id) { }
    virtual ~MyPerson() { }

    /** Take a random stumble (wow, you're on drugs) and stay in the trash fence */
    virtual void move() {
      feet_t dx = (rand() % 5) - 2;
      feet_t dy = (rand() % 5) - 2;
      step(dx, dy);
      stay_inside();
    }
    /** Tell everyone where you are (this definitely fits in 50 bytes) */
    virtual void say_all() {
      say(get_id(), get_pos());
    }
};

class MySim : public Sim {
  public:
    MySim() : Sim() { }
    virtual ~Sim() { }

  protected:
    /** Prints out a note at the end of the day */
    virtual void record() {
      const size_t time = get_time();
      if ((time > 0) && (time % SECS_PER_DAY == 0)) {
        cout << "Done with day " << (time / SECS_PER_DAY) << endl;
      }
    }
};

int main() {
  const size_t num_people = 50;
  const size_t num_days = 7;

  MySim sim;
  sim.set_runtime(num_days * SECS_PER_DAY);
  for (puid_t i = 0; i < num_people; ++i) {
    sim.add_person(new MyPerson(i));
  }

  sim.run();

  return 0;
}
