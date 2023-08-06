use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn sum(a: f64, b: f64)->f64 {
    return a +b;
}

/// A Python module implemented in Rust.
#[pymodule]
fn zyhadd(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(sum, m)?)?;
    Ok(())
}