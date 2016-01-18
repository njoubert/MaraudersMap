#ifndef SIM_H
#define SIM_H

#include <vector>

#include "misc.h"
#include "person.h"

class Sim {
  public:
    /** Create a new simulation with no people and default runtime */
    Sim() : runtime_(SECS_PER_DAY) { }
    /** Delete people */
    virtual ~Sim();

    /** Set a new simulation time */
    Sim& set_runtime(sec_t runtime) {
      runtime_ = runtime;
      return *this;
    }
    /** Add a new person to the simulation */
    Sim& add_person(Person* p) {
      ppl_.push_back(p);
      for (auto p : ppl_) {
        p->resize_model(ppl_.size());
      }
      return *this;
    }

    /** Run the simulation */
    void run();

  protected:
    /** Returns the current time in seconds */
    sec_t get_time() const {
      return time_;
    }
    /** Returns the number of people */
    size_t num_people() const {
      return ppl_.size();
    }
    /** Returns a person with a given puid */
    Person* get_person(puid_t id) {
      return ppl_[id];
    }

    /** Log the state of the simulation */
    virtual void record() = 0;

  private:
    // The people we're simulating 
    std::vector<Person*> ppl_;
    // The current time
    sec_t time_;
    // Total simulation runtime
    sec_t runtime_;

    /** Can two people hear each other? */
    bool can_hear(const Person* p1, const Person* p2) const;
};

#endif
