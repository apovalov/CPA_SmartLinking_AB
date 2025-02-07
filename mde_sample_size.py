"""Solution for Smartlink AB 2: Sample size task"""
import numpy as np
from scipy import stats


def calculate_sample_size(
    reward_avg: float, reward_std: float, mde: float, alpha: float, beta: float
) -> int:
    """Calculate sample size.

    Parameters
    ----------
    reward_avg: float :
        average reward
    reward_std: float :
        standard deviation of reward
    mde: float :
        minimum detectable effect
    alpha: float :
        significance level
    beta: float :
        type 2 error probability

    Returns
    -------
    int :
        sample size

    """
    assert mde > 0, "mde should be greater than 0"

    effect = mde * reward_avg
    z_alpha = stats.norm.ppf(1 - alpha / 2, loc=0, scale=1)
    z_beta = stats.norm.ppf(1 - beta, loc=0, scale=1)
    z_scores_sum_squared = (z_alpha + z_beta) ** 2
    sample_size = int(
        np.ceil(z_scores_sum_squared * (2 * reward_std**2) / (effect**2))
    )
    return sample_size


def calculate_mde(
    reward_std: float, sample_size: int, alpha: float, beta: float
) -> float:
    """Calculate minimal detectable effect.

    Parameters
    ----------
    reward_avg: float :
        average reward
    reward_std: float :
        standard deviation of reward
    sample_size: int :
        sample size
    alpha: float :
        significance level
    beta: float :
        type 2 error probability

    Returns
    -------
    float :
        minimal detectable effect

    """
    z_alpha = stats.norm.ppf(1 - alpha / 2, loc=0, scale=1)
    z_beta = stats.norm.ppf(1 - beta, loc=0, scale=1)
    disp_sum_sqrt = (2 * (reward_std**2)) ** 0.5
    mde = (z_alpha + z_beta) * disp_sum_sqrt / np.sqrt(sample_size)

    return mde
