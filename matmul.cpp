#include <iostream>

extern "C" void
matmul_avx512(float * A, float * B, float * C );

void multiply(const float * A, const float * B, const float * C) {
matmul_avx512((float *) A, (float *) B, (float *) C);  
}

extern "C" void
multiply_cpp(float * A, float * B, float C) {
  multiply(A, B, C );  
}
