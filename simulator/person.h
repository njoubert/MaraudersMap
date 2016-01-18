#ifndef PERSON_H
#define PERSON_H

#include <cmath>
#include <map>
#include <vector>

#include "misc.h"

class Person {
  public:
    /** Create a new person. */
    Person(puid_t me) : me_(me) { }
    /** Does nothing. */
    virtual ~Person();

    /** Resize my mental model of the world */
    void resize_model(size_t n) {
      while (model_.size() < n) {
        model_.push_back({0, 0, 0});
      }
    }

    /** Return my playa id */
    puid_t get_id() const {
      return me_;
    }
    /** Return my personal information */
    Pin get_pos() const {
      return get_estimate(me_);
    }
    /** Return an estimate of someone else's info */
    Pin get_estimate(puid_t id) const {
      return model_[id];
    }

    /** Update my internal clock by one second */
    void tick() {
      model_[me_].t++;
    }
    /** Take a step */
    virtual void move() = 0;
    /** Say something. Keep it under 50 bytes. */
    void broadcast() {
      log_.clear();
      say_all();
    }
    /** Listen. Pay attention if it's new and it's not about me. */
    void listen(puid_t who, const Pin& what) {
      if (who != me_ && what.t > model_[who].t) {
        model_[who] = what;
      }
    }

    /** Iterator over broadcast log */
    typedef std::map<puid_t, Pin>::const_iterator log_iterator;
    /** Begin iterator */
    log_iterator begin() const {
      return log_.begin();
    }
    /** End iterator */
    log_iterator end() const {
      return log_.end();
    }

  protected:
    /** Move in a direction */
    void step(feet_t dx, feet_t dy) {
      model_[me_].x += dx;
      model_[me_].y += dy;
    }
    /** Make sure I stay inside the trash fence */
    void stay_inside() {
      // This is pretty coarse, assume a 2 mile square
      const feet_t diam = 2 * FEET_PER_MILE;
      model_[me_].x = std::max(model_[me_].x, 0);
      model_[me_].x = std::min(model_[me_].x, diam);
      model_[me_].y = std::max(model_[me_].y, 0);
      model_[me_].y = std::min(model_[me_].y, diam);
    }
    /** Say everything you need to. Keep it under 50 bytes */
    virtual void say_all() = 0;
    /** Say something about someone */
    void say(puid_t id, const Pin& pin) {
      log_[id] = pin;
    }

  private:
    // My unique id
    puid_t me_;
    // My mental model of the world
    std::vector<Pin> model_;
    // The log I use to talk to the world
    std::map<puid_t, Pin> log_;
};

#endif
