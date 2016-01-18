#ifndef MISC_H
#define MISC_H

// Some primitive types for distance, time, and identity
typedef int feet_t;
typedef int sec_t;
typedef int puid_t;

// Like it or not, these are facts
const feet_t FEET_PER_MILE = 5280;
const sec_t SECS_PER_DAY = 60 * 60 * 24;

// A point in time and space
struct Pin {
  sec_t t;
  feet_t x;
  feet_t y;
};

#endif
