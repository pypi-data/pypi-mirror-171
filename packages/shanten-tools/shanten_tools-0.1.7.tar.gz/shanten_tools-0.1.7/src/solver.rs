use ndarray::prelude::*;
use ndarray::Array;

pub struct Solver {
    cache_suited: Array1<usize>,
    cache_honor: Array1<usize>,
}

impl Solver {
    fn load_cache_suited() -> Array1<usize> {
        let cache: Vec<usize> =
            serde_json::from_str(include_str!("shanten_cache_suited.json")).unwrap();
        Array::from(cache)
    }
    fn load_cache_honor() -> Array1<usize> {
        let cache: Vec<usize> =
            serde_json::from_str(include_str!("shanten_cache_honor.json")).unwrap();
        Array::from(cache)
    }
    pub fn new() -> Self {
        let cache_suited = Solver::load_cache_suited();
        let cache_honor = Solver::load_cache_honor();
        Self {
            cache_suited,
            cache_honor,
        }
    }

    fn apply_suit(&self, dp: &mut Array1<usize>, code: usize, n_meld: usize) {
        let cache = self.cache_suited.slice(s![code * 10..(code + 1) * 10]);
        for x in (0..5 - n_meld).rev() {
            for a in (x + 1..5 - n_meld).rev() {
                dp[a + 5] = std::cmp::min(
                    dp[a + 5],
                    std::cmp::min(dp[x] + cache[a - x + 5], dp[x + 5] + cache[a - x]),
                );
                dp[a] = std::cmp::min(dp[a], dp[x] + cache[a - x]);
            }
            dp[x + 5] = std::cmp::min(dp[x + 5], dp[x] + cache[5]);
        }
    }

    pub fn shanten(&self, h: ArrayView1<u8>, n_meld: usize) -> usize {
        let code = (1..9).fold(h[0] as usize, |acc, j| acc * 5 + h[j] as usize);
        let mut dp = self
            .cache_suited
            .slice(s![code * 10..(code + 1) * 10])
            .to_owned();

        for i in 1..3 {
            let code =
                (9 * i + 1..9 * (i + 1)).fold(h[9 * i] as usize, |acc, j| acc * 5 + h[j] as usize);
            self.apply_suit(&mut dp, code, n_meld);
        }

        let code = (28..34).fold(h[27] as usize, |acc, j| acc * 5 + h[j] as usize);
        let cache = self.cache_honor.slice(s![code * 10..(code + 1) * 10]);

        let mut ans = dp[(4 - n_meld) + 5];
        for x in 0..4 - n_meld {
            ans = std::cmp::min(
                ans,
                std::cmp::min(
                    dp[x] + cache[4 - n_meld - x + 5],
                    dp[x + 5] + cache[4 - n_meld - x],
                ),
            );
        }
        ans = std::cmp::min(ans, dp[4 - n_meld] + cache[5]);

        if n_meld == 0 {
            let n_pair = (0..34).map(|i| (h[i] > 1) as usize).sum::<usize>();
            let n_kind = (0..34).map(|i| (h[i] > 0) as usize).sum::<usize>();
            ans = std::cmp::min(ans, 7 - n_pair - if n_kind < 7 { 7 - n_kind } else { 0 });

            let n_thirteen_orphan = (h[0] > 0) as usize
                + (h[8] > 0) as usize
                + (h[9] > 0) as usize
                + (h[17] > 0) as usize
                + (h[18] > 0) as usize
                + (26..34).map(|i| (h[i] > 0) as usize).sum::<usize>();
            let has_thirteen_orphan_pair = h[0] > 1
                || h[8] > 1
                || h[9] > 1
                || h[17] > 1
                || h[18] > 1
                || (26..34).any(|i| h[i] > 1);
            ans = std::cmp::min(
                ans,
                14 - n_thirteen_orphan - has_thirteen_orphan_pair as usize,
            )
        }

        ans
    }

    pub fn shanten_discard(&self, h: ArrayView1<u8>, n_meld: usize) -> Array1<usize> {
        let mut ans = Array1::<usize>::zeros(34);
        let mut h = h.to_owned();
        for i in 0..34 {
            if h[i] == 0 {
                continue;
            }
            h[i] -= 1;
            ans[i] = self.shanten(h.view(), n_meld);
            h[i] += 1;
        }
        ans
    }
}
