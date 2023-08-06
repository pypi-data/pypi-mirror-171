pub struct Solver {
    cache_suited: Vec<Vec<usize>>,
    cache_honor: Vec<Vec<usize>>,
}
impl Solver {
    pub fn new() -> Self {
        let cache_suited: Vec<Vec<usize>> = serde_json::from_str(include_str!("shanten_cache_suited.json")).unwrap();
        let cache_honor: Vec<Vec<usize>> = serde_json::from_str(include_str!("shanten_cache_suited.json")).unwrap();
        Self { cache_suited, cache_honor }
    }

    pub fn shanten(&self, h: &[usize], n_meld: usize) -> i32 {
        let code = (1..9).fold(h[0], |acc, j| acc * 5 + h[j]);
        let mut dp = self.cache_suited[code].clone();

        for i in 1..3 {
            let code = (1..9).fold(h[9*i], |acc, j| acc * 5 + h[9*i + j]);
            for x in (0..5 - n_meld).rev() {
                for y in (0..2).rev() {
                    for a in x..5 - n_meld {
                        for b in y..2 {
                            dp[a + b * 5] = std::cmp::min(
                                dp[a + b * 5],
                                dp[x + y * 5] + self.cache_suited[code][(a - x) + (b - y) * 5],
                            );
                        }
                    }
                }
            }
        }

        let code = (28..34).fold(h[27], |acc, j| acc * 5 + h[j]);
        for x in (0..5 - n_meld).rev() {
            for y in (0..2).rev() {
                dp[(4 - n_meld) + 5] = std::cmp::min(
                    dp[(4 - n_meld) + 5],
                    dp[x + y * 5] + self.cache_honor[code][(4 - n_meld - x) + (1 - y) * 5],
                );
            }
        }

        dp[4 - n_meld + 5] as i32 - 1
    }
}
