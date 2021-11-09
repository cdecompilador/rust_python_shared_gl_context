use pyo3::{
    types::*,
    prelude::*,
    wrap_pyfunction, wrap_pymodule
};

#[pymodule]
fn testing(py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m, "clear")]
    fn clear(py: Python, get_proc_addr: &PyAny) -> PyResult<()> {
        gl::load_with(|name| {
            if get_proc_addr.is_callable() {
                let bytes = PyBytes::new(py, name.as_bytes());
                let args = PyTuple::new(py, &[bytes]);
                let obj = get_proc_addr.call1(args).unwrap();
                obj.extract::<u64>().unwrap() as *const _
            } else {
                panic!("Cannot load opengl function, `get_proc_addr` invalid");
            }
        });

        unsafe {
            gl::ClearColor(0.1, 0.2, 0.3, 1.0);
            gl::Clear(gl::COLOR_BUFFER_BIT);
        }

        Ok(())
    }

    Ok(())
}


