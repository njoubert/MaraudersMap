#include "sim.h"

#include <cstdlib>

using namespace std;

Sim::~Sim() {
  for (auto p : ppl_) {
    delete p;
  }
}

void Sim::run() {
  for (time_ = 0; time_ <= runtime_; ++time_) {
    // Advance everyone's clock
    for (auto person : ppl_) {
      person->tick();
    }
    // Advance everyone's position
    for (auto person : ppl_) {
      person->move();
    }
    // Communicate
    for (const auto p1 : ppl_) {
      p1->broadcast();
      for (auto p2 : ppl_) {
        if (can_hear(p1, p2)) {
          for (auto i = p1->begin(), ie = p1->end(); i != ie; ++i) {
            p2->listen(i->first, i->second); 
          }
        }
      }
    }
    // Record
    record();
  }
}

// TODO: No idea if this is reasonable; linear attentuation to a quarter mile
bool Sim::can_hear(const Person* p1, const Person* p2) const {
  const auto dx = p1->get_pos().x - p2->get_pos().x;
  const auto dy = p1->get_pos().y - p2->get_pos().y;
  const auto dist = sqrt(dx*dx + dy*dy);

  const auto qmile = FEET_PER_MILE / 4;
  const int chance = 1000 * dist / qmile;
      
  return (rand() % 1000) >= chance;
}
