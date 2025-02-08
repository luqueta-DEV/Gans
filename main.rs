extern "C" {
    fn multiply_cpp( A: *const f32, B: *const f32,  C: *mut f32);
}

fn main() {
    let A: [f32; 16] = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0]
    let B: [f32; 16] = [1.0; 16];
    let mut C: [f32; 16] = [0.0; 16];

    unsafe {
        multiply_cpp(A.as_ptr(), B.as_ptr(), C.as_ptr();
    )
    }
      println!("Resultado: {:?}, C"); 

}    