section .text
global matmul_avx512

matmul_avx512:

  vmovaps zmm0, [rdi]
  vmovaps zmm1, [rsi]
  vfmadd231ps zmm2, zmm0, zmm1
  vmovaps [rdx], zmm2
  ret 