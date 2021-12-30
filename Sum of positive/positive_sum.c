#include <stddef.h>

int positive_sum(const int *values, size_t count){\
  int total = 0;
  for (int i = 0; i < count; i++){
    if (values[i] > 0){
      total += values[i];
    }
  }
  return total;
}