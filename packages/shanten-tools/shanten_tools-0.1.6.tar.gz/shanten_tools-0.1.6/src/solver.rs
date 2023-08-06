use ndarray::prelude::*;
use ndarray::Array;

pub struct Solver {
    cache_suited: Array1<usize>,
    cache_honor: Array1<usize>,
}

impl Solver {
    fn load_cache_suited() -> Array1<usize> {
        let cache: Vec<usize> = serde_json::from_str(include_str!("shanten_cache_suited.json")).unwrap();
        Array::from(cache)
    }
    fn load_cache_honor() -> Array1<usize> {
        let cache: Vec<usize> = serde_json::from_str(include_str!("shanten_cache_honor.json")).unwrap();
        Array::from(cache)
    }
    pub fn new() -> Self {
        let cache_suited = Solver::load_cache_suited();
        let cache_honor = Solver::load_cache_honor();
        Self { cache_suited, cache_honor }
    }

    pub fn shanten(&self, h: &ArrayView1<u8>, n_meld: usize) -> i32 {
        let code = (1..9).fold(h[0] as usize, |acc, j| acc * 5 + h[j] as usize);
        let mut dp = self.cache_suited.slice(s![code * 10..(code + 1) * 10]).to_owned();

        for i in 1..3 {
            let code = (9*i+1..9*(i+1)).fold(h[9*i] as usize, |acc, j| acc * 5 + h[j] as usize);
            let cache = self.cache_suited.slice(s![code * 10..(code + 1) * 10]);
            for x in (0..5 - n_meld).rev() {
                for a in (x+1..5-n_meld).rev() {
                    dp[a + 5] = std::cmp::min(
                        dp[a + 5],
                        std::cmp::min(
                            dp[x] + cache[a - x + 5],
                            dp[x + 5] + cache[a - x],
                            ),
                    );
                    dp[a] = std::cmp::min(
                        dp[a],
                        dp[x] + cache[a - x],
                    );
                }
                dp[x + 5] = std::cmp::min(
                    dp[x + 5],
                    dp[x] + cache[5],
                );
            }
        }

        let code = (28..34).fold(h[27] as usize, |acc, j| acc * 5 + h[j] as usize);
        let cache = self.cache_honor.slice(s![code * 10..(code + 1) * 10]);

        let mut ans = dp[(4 - n_meld) + 5];
        for x in 0..4-n_meld {
            ans = std::cmp::min(
                ans,
                std::cmp::min(
                    dp[x] + cache[4 - n_meld - x + 5],
                    dp[x + 5] + cache[4 - n_meld - x],
                    ),
            );
        }
        ans = std::cmp::min(
            ans,
            dp[4 - n_meld] + cache[5]
        );

        ans as i32 - 1
    }
}
