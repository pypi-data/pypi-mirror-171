pub mod solver;

use pyo3::prelude::*;

use lazy_static::lazy_static;
use numpy::{IntoPyArray, PyArray1, PyReadonlyArray1};
lazy_static! {
    static ref SOLVER: solver::Solver = solver::Solver::new();
}

#[pymodule]
fn shanten_tools(_py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m)]
    fn shanten(_py: Python, hand: PyReadonlyArray1<u8>) -> usize {
        let hand = hand.as_array();
        let sum = hand.iter().sum::<u8>();
        match sum {
            13 | 14 => SOLVER.shanten(hand, 0),
            10 | 11 => SOLVER.shanten(hand, 1),
            7 | 8 => SOLVER.shanten(hand, 2),
            4 | 5 => SOLVER.shanten(hand, 3),
            1 | 2 => SOLVER.shanten(hand, 4),
            _ => panic!("hand.iter().sum() must be 1, 2, 4, 5, 7, 8, 10, 11, 13 or 14"),
        }
    }
    #[pyfn(m)]
    fn shanten_discard<'py>(py: Python<'py>, hand: PyReadonlyArray1<u8>) -> &'py PyArray1<usize> {
        let hand = hand.as_array();
        let sum = hand.iter().sum::<u8>();
        match sum {
            14 => SOLVER.shanten_discard(hand, 0),
            11 => SOLVER.shanten_discard(hand, 1),
            8 => SOLVER.shanten_discard(hand, 2),
            5 => SOLVER.shanten_discard(hand, 3),
            2 => SOLVER.shanten_discard(hand, 4),
            _ => panic!("hand.iter().sum() must be 2, 5, 8, 11 or 14"),
        }
        .into_pyarray(py)
    }
    Ok(())
}
