"""Solution for Smartlink AB 2: A/A test task."""
from typing import Tuple

import numpy as np
from scipy import stats


def cpc_sample(
    n_samples: int, conversion_rate: float, reward_avg: float, reward_std: float
) -> np.ndarray:
    """Sample data."""
    cvr = np.random.binomial(1, conversion_rate, n_samples)
    cpa = np.random.normal(reward_avg, reward_std, n_samples)
    cpc = cvr * cpa
    return cpc


def t_test(cpc_a: np.ndarray, cpc_b: np.ndarray, alpha=0.05) -> Tuple[bool, float]:
    """Perform T-test.

    Parameters
    ----------
    cpc_a: np.ndarray :
        first samples
    cpc_b: np.ndarray :
        second samples
    alpha :
        (Default value = 0.05)

    Returns
    -------
    Tuple[bool, float] :
        True if difference is significant, False otherwise
        p-value
    """
    _, p = stats.ttest_ind(cpc_a, cpc_b)
    return bool(p < alpha), float(p)


def aa_test(
    n_simulations: int,
    n_samples: int,
    conversion_rate: float,
    reward_avg: float,
    reward_std: float,
    alpha: float = 0.05,
) -> float:
    """Do the A/A test."""

    type_1_errors = np.zeros(n_simulations)
    for i in range(n_simulations):
        sample_a = cpc_sample(n_samples, conversion_rate, reward_avg, reward_std)
        sample_b = cpc_sample(n_samples, conversion_rate, reward_avg, reward_std)

        type_1_errors[i], _ = t_test(sample_a, sample_b, alpha)

    return type_1_errors.sum() / n_simulations
